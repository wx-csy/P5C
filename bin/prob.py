from . import common as com
import os, shutil, subprocess

def add_prob(shortname) :
    com.checkparam(shortname, "[a-zA-Z][a-zA-Z0-9-]*")
    meta = com.load_meta(default=dict())
    if shortname in meta :
        com.die("problem '{0}' already exists!".format(shortname))
    meta[shortname] = {'enabled' : True, 'order' : 0}
    com.save_meta(meta)
    shutil.copytree('../resource/prob-template', shortname)
    subprocess.check_call([com.config['editor'], shortname + '/problem.yaml'])
    com.commit("add problem '{0}' : {1}".format(shortname, name));

def remove_prob(shortname) :
    meta = com.load_meta()
    if shortname not in meta :
        com.die("problem '{0}' does not exist!".format(shortname))
    meta.pop(shortname)
    com.save_meta(meta)
    shutil.rmtree(shortname)
    com.commit("remove problem '{0}'".format(shortname));

COMMANDS = {
    'add' :     add_lang,
    'rm'  :     remove_lang,
}

def main(cmd, *args) :
    os.chdir('contest')
    COMMANDS[cmd](*args)
