import sys, os, shutil, subprocess, json

def die(*args) :
    print(*args, file=sys.stderr)
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
