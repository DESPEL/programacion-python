import os
base_dir = os.path.abspath(os.path.dirname(__file__))


class FlaskConfig:
    SECRET_KEY = "NOIMPORTACUALSEAPORQUESINOQUEDACHAFA"

DEFAULT_NAV = {
    "right_links": [
        {"name": "Login", "to": "/login"},
        {"name": "Registro", "to": "/register"},
        {"name": "Bievenido, {username}", "to": "#", "session": True},
        {"name": "Salir", "to": "/logout", "session": True},
    ],
    "left_links": [
        {"name":"<i class='material-icons'>home</i>", "to": "/home", "session": True},
        {"name": "Favs ♥", "to": "/favorites/0", "session": True}
    ]
}


class Config:
    pages = {
        "index": {
            "name": "Inicio",
            "nav": DEFAULT_NAV
        },
        "login": {
            "name": "Login",
            "nav": {
                "right_links": [
                    {"name": "Registro", "to": "/register"},
                ],
                "left_links": [
                    {"name": "Inicio", "to": "/home"}
                ]
            }
        },
        "register": {
            "name": "Registro",
            "nav": {
                "right_links": [
                    {"name": "Login", "to": "/login"},
                    {"name": "Registro", "to": "/register"}
                ]
            }
        },
        "poke_details": {
            "name": "{pokename}",
            "nav": DEFAULT_NAV
        },
        "home": {
            "name": "Inicio",
            "nav": DEFAULT_NAV
        },
        "settings": {
            "name": "Configuración",
            "nav": DEFAULT_NAV
        },
        "pokemon_list": {
            "name": "Lista de pokemons",
            "nav": DEFAULT_NAV
        },
        "favs": {
            "name": "Favoritos",
            "nav": DEFAULT_NAV
        },
    }
    messages = {
        "register_success": '<p class="green-text">Registado existosamente, Inicia sesión</p>'
    }
    theme = {
        'dark': {
            "name": "dark",
            "text_color": "white-text",
            "light_text": "white-text",
            "accent": "yellow darken-3",
            "accent_2": "yellow darken-2",
            "accent_3": "yellow darken-1",
            "bg": "blue-grey darken-4",
            "bg_1": "blue-grey darken-2",
            "enabled_star":"amber-text text-lighten-1",
            "disabled_star":"blue-grey-text text-lighten-3"
        },
        'blue':{
            "name": "blue",
            "text_color": "white-text",
            "light_text": "white-text",
            "accent": "light-blue darken-1",
            "accent_2": "light-blue darken-2",
            "accent_3": "light-blue darken-3",
            "bg": "grey darken-3",
            "bg_1": "grey darken-2",
            "enabled_star":"light-blue-text text-darken-3",
            "disabled_star":"blue-text text-lighten-5"
        },
        'red': {
            "name": "red",
            "text_color": "amber-text text-accent-2",
            "light_text": "white-text",
            "accent": " red darken-4",
            "accent_2": " red darken-3",
            "accent_3": " red darken-2",
            "bg": "grey darken-4",
            "bg_1": "blue-grey darken-4",
            "enabled_star":"red-text text-accent-4",
            "disabled_star":"red-text text-lighten-5" 
        },
        'light': {
            "name": "light",
            "text_color": "black-text",
            "light_text": "white-text",
            "accent": "yellow darken-3",
            "accent_2": "yellow darken-2",
            "accent_3": "yellow darken-1",
            "bg": "white",
            "bg_1": "white",
            "enabled_star":"amber-text text-lighten-1",
            "disabled_star":"grey-text text-lighten-1"
        },
        'nord': {
            "name": "nord",
            "text_color": "white-text",
            "light_text": "white-text",
            "accent": "blue-grey darken-3",
            "accent_2": "blue-grey lighten-1",
            "accent_3": "blue-grey",
            "bg": "blue-grey darken-4",
            "bg_1": "blue-grey darken-3",
            "enabled_star":"blue-grey-text",
            "disabled_star":" blue-grey-text text-lighten-3"
        },
        'pink': {
            "name": "sagiri",
            "text_color": "deep-purple-text text-accent-2",
            "accent": "pink accent-2",
            "accent_2": "pink accent-1",
            "accent_3": "purple accent-1",
            "bg": "pink lighten-5",
            "bg_1": "pink lighten-4",
            "enabled_star":"pink-text text-accent-2",
            "disabled_star":"pink-text text-lighten-5"
        },
        'best theme': {
            "name": "best theme",
            "text_color": "blue-text text-darken-2",
            "accent": "red accent-2",
            "accent_2": "purple accent-1",
            "accent_3": "orange accent-1",
            "bg": "yellow",
            "bg_1": "brown lighten-2",
            "enabled_star":"yellow-text text-accent-2",
            "disabled_star":"indigo-text text-lighten-5"
        },
        'snow': {
            "name": "snow",
            "text_color": "blue-text text-darken-2",
            "accent": "blue",
            "accent_2": "blue lighten-4",
            "accent_3": "blue lighten-3",
            "bg": "blue lighten-5",
            "bg_1": "white",
            "enabled_star":"light-blue-text text-accent-2",
            "disabled_star":"light-blue-text text-lighten-4"
        },
        'leaf': {
            "name": "Leaf",
            "text_color": "black-text",
            "accent": "green lighten-2",
            "accent_2": "green lighten-2",
            "accent_3": "green lighten-1",
            "bg": "green lighten-4",
            "bg_1": "green lighten-5",
            "enabled_star":"red-text text-accent-2",
            "disabled_star":"red-text text-lighten-4"
        },
        'brown': {
            "name": "brown",
            "text_color": "black-text",
            "accent": "brown lighten-2",
            "accent_2": "brown lighten-2",
            "accent_3": "brown lighten-1",
            "bg": "brown lighten-4",
            "bg_1": "brown lighten-5",
            "enabled_star":"brown-text text-accent-2",
            "disabled_star":"brown-text text-lighten-4"
        },
        'komi': {
            "name": "komi",
            "text_color": "white-text ",
            "accent": "red darken-4",
            "accent_2": "red darken-3",
            "accent_3": "red darken-2",
            "bg": " indigo darken-3",
            "bg_1": "indigo lighten",
            "enabled_star":"red-text text-accent-2",
            "disabled_star":"red-text text-lighten-5"
        },
        'bestoTheme2': {
            "name": "Best Theme 2",
            "text_color": "white-text ",
            "accent": "red darken-4",
            "accent_2": "red darken-3",
            "accent_3": "red darken-2",
            "bg": " indigo darken-3",
            "bg_1": "indigo lighten",
            "enabled_star":"red-text text-accent-2",
            "disabled_star":"red-text text-lighten-5"
        },
        'black': {
            "name": "black",
            "text_color": "white-text",
            "accent": "black",
            "accent_2": "black",
            "accent_3": "black",
            "bg": "black",
            "bg_1": "black",
            "enabled_star":"white-text",
            "disabled_star":"grey-text text-darken-4"
        },
    }

    @staticmethod
    def format(config, values):
        result = type(config)()
        if type(config) == dict:
            for key, value in config.items():
                result[key.format(**values)] = Config.format(value, values)
            return result
        elif type(config) == list:
            #pos ya no
            for value in config:
                result.append(Config.format(value, values))
            return result
        elif type(config) == str:
            return config.format(**values)
        return config


if __name__ == "__main__":
    print(Config.format(Config.pages["index"], {
        "username": "test_user"
    }))
