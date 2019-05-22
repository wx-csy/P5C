import sys, os, shutil, subprocess, json, re

IDENTIFIER_PAT = '[a-zA-Z]\\w*'

printe = lambda *args : print(*args, file=sys.stderr)

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
    if not os.path.exists(fname) :
        json.dump(default, open(fname, 'w'), indent=2)
    return json.load(open(fname))

def save_meta(meta, fname='meta.json') :
    json.dump(meta, open(fname, 'w'), indent=2)
