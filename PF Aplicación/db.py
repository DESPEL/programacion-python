import os
from os import path
from shutil import copyfile, rmtree
import json

import pokebase as pb

from werkzeug.security import (
    generate_password_hash, check_password_hash
)

try:
    os.mkdir('usuarios')
except FileExistsError:
    pass


class UserNotFound(Exception):
    pass


class DuplicatedUser(Exception):
    pass


class User:
    def __init__(self, info, config):
        self.info = info
        self.config = config
    
    def add_favorite(self, name):
        self.config['pokemon']['favorites'].append(name)
        self.save()

    def delete_favorite(self, name):
        self.config['pokemon']['favorites'].remove(name)
        self.save()

    def get_favorites_names(self):
        return [poke['name'] for poke in self.config['pokemon']['favorites']]

    def get_raw_favorites(self):
        return self.config['pokemon']['favorites']

    def get_favorites(self):
        return [
            pb.pokemon(name) for name in self.config['pokemon']['favorites']]

    def save(self):
        save_user(self)

def save_user(user):
    if type(user) is not User:
        raise ValueError

    username = user.info["username"]
    with open(f"usuarios/{username}/info.json", "w") as f:
        json.dump(user.info, f, indent=4)
    with open(f"usuarios/{username}/config.json", "w") as f:
        json.dump(user.config, f, indent=4)

def get_user(username):
    if not path.exists(f"usuarios/{username}"):
        raise UserNotFound
    
    user_info = {}
    with open(f"usuarios/{username}/info.json") as user_file:
        user_info = json.load(user_file)
    
    user_config = {}
    with open(f"usuarios/{username}/config.json") as config_file:
        user_config = json.load(config_file)

    return User(user_info, user_config)

def can_register(username):
    return not path.exists(f"usuarios/{username}")

def register(username, password):
    if not can_register(username):
        raise DuplicatedUser
    
    hash_ = generate_password_hash(password)

    os.mkdir(f"usuarios/{username}")
    
    user = {
        "username": username,
        "hash": hash_
    }

    with open(f"usuarios/{username}/info.json", "w+") as user_info:
        json.dump(user, user_info, indent=4)
    copyfile('usuarios/default/config.json', f'usuarios/{username}/config.json')

def login(username, password): 
    try:
        user = get_user(username)
        return check_password_hash(user.info["hash"], password)
    except UserNotFound:
        return False

def unregister(username):
    if can_register(username):
        raise UserNotFound
    if '/' in username:
        print("nice")
        return
    rmtree(f'usuarios/{username}')


if __name__ == "__main__":
    unregister("test_user")
    register("test_user", "password")
    user = get_user('test_user')
    user.config["testvalue"] = "Saved"
    user.save()    
    def __init__(self, info, config):
        self.info = info
        self.config = config
    
    def save(self):
        save_user(self)

def save_user(user):
    if type(user) is not User:
        raise ValueError

    username = user.info["username"]
    with open(f"usuarios/{username}/info.json", "w") as f:
        json.dump(user.info, f, indent=4)
    with open(f"usuarios/{username}/config.json", "w") as f:
        json.dump(user.config, f, indent=4)

def get_user(username):
    if not path.exists(f"usuarios/{username}"):
        raise UserNotFound
    
    user_info = {}
    with open(f"usuarios/{username}/info.json") as user_file:
        user_info = json.load(user_file)
    
    user_config = {}
    with open(f"usuarios/{username}/config.json") as config_file:
        user_config = json.load(config_file)

    return User(user_info, user_config)

def can_register(username):
    return not path.exists(f"usuarios/{username}")

def register(username, password):
    if not can_register(username):
        raise DuplicatedUser
    
    hash_ = generate_password_hash(password)

    os.mkdir(f"usuarios/{username}")
    
    user = {
        "username": username,
        "hash": hash_
    }

    with open(f"usuarios/{username}/info.json", "w+") as user_info:
        json.dump(user, user_info, indent=4)
    copyfile('usuarios/default/config.json', f'usuarios/{username}/config.json')

def unregister(username):
    if can_register(username):
        raise UserNotFound
    if '/' in username:
        print("nice")
        return
    rmtree(f'usuarios/{username}')