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
    'api.mksyn.solbuild' : api.mksyn.solbuild,
    'api.mksyn.validatorbuild' : api.mksyn.validatorbuild,
}

def main(cmd, *args) :
    MODULES[cmd](*args)
