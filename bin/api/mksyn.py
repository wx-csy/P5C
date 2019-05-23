from .. import lang
from .. import common as com
import csv, sys, pathlib

def __get_data_src(gen) :
    return 'data/' + gen

def __get_data_dest(gen) :
    return 'build/data/exec/' + gen + '.exec'

def __get_sol_dest(gen) :
    return 'build/solution/exec/' + gen + '.exec'

def __get_data_in(gen) :
    return 'build/data/gen/' + gen + '.in'

def __get_data_ans(gen) :
    return 'build/data/gen/' + gen + '.ans'

def __get_validator_src() :
    return 'validator/' + com.pconf["validator"]

def __get_validator_dest() :
    return 'build/misc/validator.exec'

def __build_exec(srclang, src, dest) :
    print('''{0} : {1}
\t@mkdir -p $(dir $@)
\t@echo + [{2}] $@
\t@{3}
'''.format(dest, src, srclang.upper(),
        lang.get_compile_script(srclang, str(src), str(dest))))

def validatorbuild() :
    com.setprob()
    src = __get_validator_src()
    dest = __get_validator_dest()
    srclang = lang.identify_source_lang(src)
    __build_exec(srclang, src, dest)

def solbuild() :
    com.setprob()
    for src in pathlib.Path('solution').iterdir() :
        srclang = lang.identify_source_lang(src)
        if not srclang : continue
        dest = __get_sol_dest(src.name)
        __build_exec(srclang, src, dest)

def databuild() :
    com.setprob()
    sgen = set()
    for name, gen, flag, issample, desc in csv.reader(sys.stdin, delimiter='\t'):
        sgen.add(gen)
    for gen in sgen :
        srclang = lang.identify_source_lang(gen)
        if not srclang :
            com.die("unrecognized source file '{0}'".format(gen))
        src = __get_data_src(gen)
        dest = __get_data_dest(gen)
        __build_exec(srclang, src, dest)

def datagen() :
    com.setprob()
    stddest = __get_sol_dest(com.pconf["std"])
    validator = __get_validator_dest()
    for name, gen, flag, issample, desc in csv.reader(sys.stdin, delimiter='\t') :
        datain = __get_data_in(name)
        dataans = __get_data_ans(name)
        print('''{0} : {1} {3}
\t@mkdir -p $(dir $@)
\t@echo + [GEN] $@
\t@$< {2} > $@
\t@echo '*' [VALIDATE] $@
\t@{3} < $@
DATAGEN_INPUT_TARGETS += {0}
'''.format(datain, __get_data_dest(gen), flag, validator))
        print('''{0} : {1} {2}
\t@mkdir -p $(dir $@)
\t@echo + [GEN] $@
\t@$< < {2} > $@
DATAGEN_OUTPUT_TARGETS += {0}
'''.format(dataans, stddest, datain, flag))
