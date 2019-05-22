from . import common as com
import os, shutil, subprocess

def add_lang(shortname) :
    com.checkparam(shortname)
    name = com.readparam('Full Name: ', default=shortname)
    ext = com.readparam('File Extension (space-separated): ', default='').split()
    if not ext : die("extension list must not be empty")
    meta = com.load_meta(default=dict())
    if shortname in meta :
        com.die("language '{0}' already exists!".format(shortname))
    meta[shortname] = {
        'name' : name, 
        'ext' : ext,
    }
    com.save_meta(meta)
    shutil.copytree('../resource/lang-template', shortname)
    subprocess.check_call([com.config['editor'], shortname + '/compile'])
    subprocess.check_call([com.config['editor'], shortname + '/run'])
    subprocess.check_call([com.config['editor'], shortname + '/template'])
    com.commit("add language '{0}' : {1}".format(shortname, name));

def remove_lang(shortname) :
    meta = com.load_meta()
    if shortname not in meta :
        com.die("language '{0}' does not exist!".format(shortname))
    meta.pop(shortname)
    com.save_meta(meta)
    shutil.rmtree(shortname)
    com.commit("remove language '{0}'".format(shortname));

COMMANDS = {
    'add' :     add_lang,
    'rm'  :     remove_lang,
}

def main(cmd, *args) :
    os.chdir('lang')
    COMMANDS[cmd](*args)
