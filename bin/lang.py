from . import common as com
import os, shutil, subprocess, pathlib, shlex

LANG_PATH = com.getroot() + 'lang/'

def identify_source_lang(filename) :
    meta = com.load_meta(LANG_PATH)
    suf = pathlib.Path(filename).suffix 
    for lang, cfg in meta.items() :
        if suf in cfg['ext'] :
            return lang
    return None

def get_lang_dir(lang_shortname) :
    return LANG_PATH + lang_shortname + '/'

def get_compile_script(lang_shortname, src, dest) :
    return ' '.join([get_lang_dir(lang_shortname) + '/compile',
        shlex.quote(src), shlex.quote(dest)])

def add_lang(shortname) :
    com.checkparam(shortname)
    name = com.readparam('Full Name: ', default=shortname)
    ext = com.readparam('File Extension (space-separated): ', default='').split()
    if not ext : com.die("extension list must not be empty")
    meta = com.load_meta('lang/', default=dict())
    if shortname in meta :
        com.die("language '{0}' already exists!".format(shortname))
    meta[shortname] = {
        'name' : name, 
        'ext' : ext,
    }
    com.save_meta(meta, 'lang/')
    shutil.copytree('resource/lang-template', 'lang/' + shortname, symlinks=True)
    subprocess.check_call([com.gconf['editor'], 'lang/' + shortname + '/compile'])
    subprocess.check_call([com.gconf['editor'], 'lang/' + shortname + '/template'])
    com.commit("add language '{0}' : {1}".format(shortname, name))

def remove_lang(shortname):
    meta = com.load_meta('lang')
    if shortname not in meta:
        com.die("language '{0}' does not exist!".format(shortname))
    meta.pop(shortname)
    com.save_meta(meta, 'lang')
    shutil.rmtree('lang/' + shortname)
    com.commit("remove language '{0}'".format(shortname))

COMMANDS = {
    'add' :     add_lang,
    'rm'  :     remove_lang,
}

def __usage() :
    print(
'''Usage: pc lang <command> [<args>]

Supported Commands:
    add <shortname>     add a language with specified shortname
    rm <shortname>      remove a language with specified shortname
'''
    )
    exit(0)

def main(cmd, *args) :
    com.setroot()
    if cmd not in COMMANDS :  __usage()
    COMMANDS[cmd](*args)
