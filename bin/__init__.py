from . import lang

MODULES = {
    'lang' :    lang.main
}

def main(cmd, *args) :
    MODULES[cmd](*args)
