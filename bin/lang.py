from . import common as com
import os, shutil

def add_lang(shortname, name) :
    if not name : name = shortname
    meta = com.load_meta(default=dict())
    if shortname in meta :
        com.die("language '{0}' already exists!".format(shortname))
    meta[shortname] = {'name' : name}
    com.save_meta(meta)
    shutil.copytree('../resource/lang-template', shortname)
    com.commit("add language '{0}' : {1}".format(shortname, name));

def remove_lang(shortname) :
    meta = com.load_meta()
    if shortname not in meta :
        com.die("language '{0}' does not exist!".format(shortname))
    name = meta.pop(shortname)['name']
    com.save_meta(meta)
    shutil.rmtree(shortname)
    com.commit("remove language '{0}' : {1}".format(shortname, name));

COMMANDS = {
    'add' :     add_lang,
    'rm'  :     remove_lang,
}

def main(cmd, *args) :
    os.chdir('lang')
    COMMANDS[cmd](*args)
