from . import lang, prob
from . import common
from . import api

MODULES = {
    'lang' :        lang.main,
    'language' :    lang.main,
    'prob' :        prob.main,
    'problem' :     prob.main,
    'api.mksyn.datagen' : api.mksyn.datagen,
    'api.mksyn.databuild' : api.mksyn.databuild,
    'api.mksyn.solbuild' : api.mksyn.solbuild,
    'api.mksyn.validatorbuild' : api.mksyn.validatorbuild,
}

def main(cmd, *args) :
    MODULES[cmd](*args)
