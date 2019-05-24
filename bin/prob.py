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

def ls_prob() :
    meta = com.load_meta('contest')
    if not meta :
        print('There is no problem in this contest.')
    for shortname, desc in meta.items() :
        print('{0}\t{1}\t{2}'.format(shortname, ['', 'enabled'][desc['enabled']], desc['order']))

COMMANDS = {
    'add' :     add_prob,
    'rm'  :     remove_prob,
    'remove' :  remove_prob,
    'ls' :      ls_prob,
}

def main(cmd='ls', *args) :
    com.setroot()
    COMMANDS[cmd](*args)
