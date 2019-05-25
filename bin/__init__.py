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
    'api.mksyn.samplegen' : api.mksyn.samplegen,
    'api.mksyn.solution' : api.mksyn.solution,
    'api.mksyn.accessory' : api.mksyn.accessory,
}

def main(cmd, *args) :
    MODULES[cmd](*args)
