import sys, os, shutil, subprocess, pathlib
import json, re

IDENTIFIER_PAT = '[a-zA-Z]\\w*'
gconf = None
pconf = None

printe = lambda *args : print(*args, file=sys.stderr)

def loadgconf() :
    global gconf
    gconf = load_meta(getroot() + "/config.json")
    pgconf:dict = load_meta(getroot() + "/private/config.json", default=dict())
    for k, v in pgconf.items() :
        gconf[k] = v

def getroot() :
    path = pathlib.Path.cwd()
    this = './'
    for p in [path] + list(path.parents) :
        if p.joinpath('.p5c').exists() :
            return this
        this += '../'
    return None

def setroot() :
    global gconf
    root = getroot()
    if not root : die('P5C: not a p5c repository')
    os.chdir(root)
    loadgconf()

def getprob():
    path = pathlib.Path.cwd()
    this = './'
    for p in [path] + list(path.parents):
        if p.joinpath('.p5c-prob').exists():
            return (this, p.name)
        this += '../'
    return None


def setprob():
    global pconf
    pn = getprob()
    if not pn: die('P5C: not a p5c problem directory')
    os.chdir(pn[0])
    pconf = load_meta(pn[0], default=dict())
    loadgconf()
    return pn[1]

def checkparam(s, pat=IDENTIFIER_PAT) :
    if not re.fullmatch(pat, s) :
        die("input should match pattern '{0}'".format(pat))

def readparam(prompt='', pat=None, default=None) :
    flag = False
    while not flag :
        s = input(prompt)
        if s == '' :
            if default is not None :
                s = default
                flag = True
            else :
                printe("input should not be empty!")
        elif pat is not None :
            if not re.fullmatch(pat, s) :
                printe("input should match pattern '{0}'".format(pat))
            else :
                flag = True
        else :
            flag = True
    return s

def die(*args) :
    printe(*args)
    exit(1)

def commit(msg, path='.') :
    if subprocess.call(['git', 'add', '--verbose', path]) != 0 :
        die("git: failed to add changes")
    if subprocess.call(['git', 'commit', '-am', msg]) != 0 :
        die("git: failed to commit changes")

def load_meta(fname='meta.json', default=[]) :
    if not pathlib.Path(fname).is_file() :
        if pathlib.Path(fname + '/meta.json').is_file() :
            fname += '/meta.json'
        else :
            json.dump(default, open(fname, 'w'), indent=2)
    return json.load(open(fname))

def save_meta(meta, fname='meta.json') :
    if pathlib.Path(fname).is_dir() : fname += '/meta.json'
    json.dump(meta, open(fname, 'w'), indent=2)
