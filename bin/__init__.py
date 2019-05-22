from . import lang, prob

MODULES = {
    'lang' :        lang.main,
    'language' :    lang.main,
    'prob' :        prob.main,
    'problem' :     prob.main,
}

def main(cmd, *args) :
    MODULES[cmd](*args)
