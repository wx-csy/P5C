from . import lang, prob, cli
from . import common
from . import api

MODULES = {
    'lang' :        lang.main,
    'language' :    lang.main,
    'prob' :        prob.main,
    'problem' :     prob.main,
    'create' :       cli.create,

    'api.mksyn.datagen' : api.mksyn.datagen,
    'api.mksyn.databuild' : api.mksyn.databuild,
    'api.mksyn.solution' : api.mksyn.solution,
    'api.mksyn.accessory' : api.mksyn.accessory,
    'api.texsyn.contest' : api.texsyn.contest,
}

def main(cmd, *args) :
    MODULES[cmd](*args)
