from . import common as com
import os, shutil, subprocess
import random

def add_prob(shortname) :
    com.checkparam(shortname, "[a-zA-Z][a-zA-Z0-9-]*")
    meta:dict = com.load_meta('contest', default=dict())
    if shortname in meta :
        com.die("problem '{0}' already exists!".format(shortname))
    meta[shortname] = {'enabled' : True, 'order' : 0}
    com.save_meta(meta, 'contest')
    shutil.copytree('resource/prob-template', 'contest/' + shortname, symlinks=True)
    subprocess.check_call([com.gconf['editor'], 'contest/' + shortname + '/problem.yaml'])
    com.commit("add problem '{0}'".format(shortname))

def remove_prob(shortname) :
    meta:dict = com.load_meta('contest', default=dict())
    if shortname not in meta :
        com.die("problem '{0}' does not exist!".format(shortname))
    meta.pop(shortname)
    com.save_meta(meta, 'contest')
    shutil.rmtree('contest/' + shortname)
    com.commit("remove problem '{0}'".format(shortname))

def ls_prob() :
    meta:dict = com.load_meta('contest', default=dict())
    if not meta :
        print('There is no problem in this contest.')
    for shortname, desc in meta.items() :
        print('{0}\t{1}\t{2}'.format(shortname, ['', 'enabled'][desc['enabled']], desc['order']))

def sort_prob(method='alphabet') :
    meta:dict = com.load_meta('contest', default=dict())
    keys:list = [key for key, conf in meta.items() if conf['enabled']]
    if method == 'alphabet' :
        keys.sort()
    elif method == 'random' :
        random.shuffle(keys)
    else:
        __usage()
    for i, name in enumerate(keys):
        meta[name]['order'] = i
    com.save_meta(meta, 'contest')
    print('The problems are sorted in the following order:')
    print(*keys)

COMMANDS = {
    'add' :     add_prob,
    'rm'  :     remove_prob,
    'ls' :      ls_prob,
    'sort' :    sort_prob,
}

def __usage() :
    print(
'''Usage: pc prob [<command>] [<args>]

Supported Commands:
    ls                  (Default) List all problems.
    add <shortname>     Add a problem with specified shortname.
    rm <shortname>      Remove a problem with specified shortname.
    sort [<method>]     Sort the problems. Methods can be:
                            alphabet    (Default) Sort the problems in lexicographical 
                                        order of their shortnames.
                            random      Sort the problems randomly.
'''
    )
    exit(0)


def main(cmd='ls', *args) :
    com.setroot()
    if cmd not in COMMANDS:  __usage()
    COMMANDS[cmd](*args)
