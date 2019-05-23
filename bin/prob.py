from . import common as com
import os, shutil, subprocess

def add_prob(shortname) :
    com.checkparam(shortname, "[a-zA-Z][a-zA-Z0-9-]*")
    meta = com.load_meta('contest', default=dict())
    if shortname in meta :
        com.die("problem '{0}' already exists!".format(shortname))
    meta[shortname] = {'enabled' : True, 'order' : 0}
    com.save_meta(meta, 'contest')
    shutil.copytree('resource/prob-template', 'contest/' + shortname, symlinks=True)
    print(com.gconf)
    subprocess.check_call([com.gconf['editor'], 'contest/' + shortname + '/problem.yaml'])
    com.commit("add problem '{0}'".format(shortname))

def remove_prob(shortname) :
    meta = com.load_meta('contest')
    if shortname not in meta :
        com.die("problem '{0}' does not exist!".format(shortname))
    meta.pop(shortname)
    com.save_meta(meta, 'contest')
    shutil.rmtree('contest/' + shortname)
    com.commit("remove problem '{0}'".format(shortname))

COMMANDS = {
    'add' :     add_prob,
    'rm'  :     remove_prob,
    'remove' :  remove_prob,
}

def main(cmd, *args) :
    com.setroot()
    COMMANDS[cmd](*args)
