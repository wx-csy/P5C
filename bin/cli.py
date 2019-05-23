from . import common as com
from . import lang
import os, shutil, subprocess, pathlib, shlex

def create(filename) :
    com.loadgconf()
    srclang = lang.identify_source_lang(filename)
    if srclang :
        temppath = lang.get_lang_dir(srclang) + "/template"
        if os.path.exists(temppath) :
            shutil.copy(temppath, filename)
    editor = com.gconf['editor']
    os.execlp(editor, editor, filename)