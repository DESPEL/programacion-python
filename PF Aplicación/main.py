import math
import json

from flask import (
    Flask,
    render_template,
    send_from_directory,
    request,
    g,
    session,
    redirect,
    url_for,
    flash
)
from flaskwebgui import FlaskUI

import pokebase as pb

import db
from db import UserNotFound

from config import FlaskConfig, Config

from forms import (
    LoginForm,
    RegisterForm
)

from pokemons import (
    get_pokemon_interval
)

app = Flask(__name__, template_folder="Templates")
app.config.from_object(FlaskConfig)

# ui = FlaskUI(app=app, width=768, height=1024)

def login_required(page):
    def wrapper(*args, **kwargs):
        if not 'username' in session:
            return redirect('/')
        return page(*args, **kwargs)
    wrapper.__name__ = page.__name__
    return wrapper


def themeable(page):
    def wrapper(*args, **kwargs):
        if not 'username' in session or not 'theme' in g.user.config:
            theme = Config.theme[db.get_user('default').config['theme']]
        else:
            if not g.user.config['theme'] in Config.theme:
                theme = Config.theme[db.get_user('default').config['theme']]
            else:
                theme = Config.theme[g.user.config['theme']]
        return page(theme=theme, *args, **kwargs)
    wrapper.__name__ = page.__name__
    return wrapper


def get_favs_interval(num):
    pokemonos = g.user.get_raw_favorites()
    fav_len = len(pokemonos)

    start = num*10 if num*10 < fav_len else fav_len-1
    end = num*10+10 if num*10+10 < fav_len else fav_len
    monos= pokemonos[start:end]
    return monos
    

@app.before_request
def before_request():
    if 'username' in session:
        try:
            g.user = db.get_user(session['username'])
        except UserNotFound:
            session.pop('username', None)



@app.route("/js/<path:path>")
def get_script(path):
    return send_from_directory("scripts", path)


@app.route("/css/<path:path>")
def get_css(path):
    return send_from_directory("styles", path)


@app.route('/')
@themeable
def index(theme):
    if 'username' in session:
        return redirect('/home')
    page_config = Config.format(Config.pages["index"], {
        "username": session.get("username", "Not logged in")
    })
    return render_template('index.jinja', page=page_config, form=RegisterForm(), theme=theme)


@app.route('/login', methods=['GET', 'POST'])
@themeable
def login(theme):
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        session.pop('username', None)

        username = request.form["username"]
        password = request.form["password"]
        session['username'] = username
        return redirect('/home')
    page = Config.pages["login"]
    return render_template("login.jinja", page=page, form=form, theme=theme)


@app.route('/register', methods=['GET', 'POST'])
@themeable
def register(theme):
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        db.register(form.username.data, form.password.data)
        flash(Config.messages["register_success"])
        return redirect(url_for('login'))

    page = Config.pages["register"]
    return render_template("register.jinja", page=page, form=form, theme=theme)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


@app.route('/home')
@login_required
@themeable
def home(theme):
    page = Config.format(Config.pages['home'], {
        'username': session['username']
    })
    return render_template('home.jinja', page=page, theme=theme)


@app.route('/pokemon_list')
@login_required
def pokemon_noinfo_list():
    return redirect('/pokemon_list/0')


@app.route('/pokemon_list/<path:page>')
@login_required
@themeable
def pokemon_list(theme, page):
    npage = int(page)
    monos = get_pokemon_interval(npage*10, npage*10 + 10)['results']
    
    page = Config.format(Config.pages['pokemon_list'], {
        'username': session['username']
    })
    return render_template(
        'pokemon_list.jinja', 
        page=page, 
        pokes=monos, 
        number=npage, 
        favs=g.user.get_favorites_names(), 
        theme=theme,
    )



@app.route('/favorites/<path:num_page>')
@login_required
@themeable
def favorites(theme,num_page):
    npage=int(num_page)
    favs=g.user.get_raw_favorites()
    
    pokes = list(get_favs_interval(npage))
    
    num_p = math.ceil(len(favs)/10)
    
    page = Config.format(Config.pages["favs"], {
        'username': session['username']
    })
    return render_template("FavList.jinja",page=page, number=npage,pokes=pokes, pages=num_p, tam_tot=len(favs), theme=theme)

@app.route('/remove/<path:poke>/<path:idx>/<path:page>')
def remove_fav(poke,idx,page):
    if poke in g.user.get_favorites_names():
        g.user.delete_favorite({"name":poke,"id":idx})
    return redirect(f'/favorites/{page}')

@app.route('/add/<path:page>/<path:pokemon_name>/<path:id>')
def add_pokemon(page, pokemon_name, id):
    if not pokemon_name in g.user.get_favorites_names():
        g.user.add_favorite({"name": pokemon_name, "id": id})
    else:
        g.user.delete_favorite({"name": pokemon_name, "id": id})
        g.user.save()
    return redirect(f'/pokemon_list/{page}')

@app.route('/get/<path:pokemon_name>')
@themeable
def get_pokemon(theme, pokemon_name):
    try:
        pokemon = pb.pokemon(pokemon_name) # Si el pokemon no existe tira un ValueError 
    except ValueError:
        return redirect('/home')

    page = Config.format(Config.pages['poke_details'], {
        'pokename': pokemon_name.capitalize(),
        'username': session.get('username', 'Not logged in')
    })
    return render_template('pokemonDetails.jinja', page=page, pokemon=pokemon, theme=theme)

@app.route('/settings')
@login_required
@themeable
def settings(theme):

    page = Config.format(Config.pages['settings'], {
        'username': session.get('username', 'Not logged in')
    })
    return render_template('settings.jinja', 
        page=page,
        themes=Config.theme,
        theme=theme
    )

@app.route('/set', methods=['POST'])
def set_setting():
    change = request.form
    user = g.user
    for key, val in change.items():
        is_defined = type(Config.__dict__.get(key, None)) == dict
        if is_defined:
            options = Config.__dict__[key]
            if val not in options:
                continue
            user.config[key] = val
            user.save()
    return redirect(url_for('settings'))


app.run(debug=True)
# ui.run()

