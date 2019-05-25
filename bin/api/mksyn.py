from .. import lang
from .. import common as com
import csv, sys, pathlib

def __get_data_src(gen) :
    return 'data/' + gen

def __get_data_dest(gen) :
    return 'build/data/exec/' + gen + '.exec'

def __get_sol_dest(gen) :
    return 'build/solution/exec/' + gen + '.exec'

def __get_data_in(name) :
    return 'build/data/gen/' + name + '.in'

def __get_data_ans(name) :
    return 'build/data/gen/' + name + '.ans'

def __get_sample_in(name) :
    return 'build/data/sample/' + name + '.in'

def __get_sample_ans(name) :
    return 'build/data/sample/' + name + '.ans'

def __get_validator_src() :
    return 'accessory/' + com.pconf["validator"]

def __get_validator_dest() :
    return 'build/accessory/validator.exec'

def __get_checker_src() :
    return 'accessory/' + com.pconf["checker"]

def __get_checker_dest() :
    return 'build/accessory/checker.exec'

def __build_exec(srclang, src, dest, extra='') :
    print('''{0} : {1}
\t@mkdir -p $(dir $@)
\t@echo + [{2}] $@
\t@{3}
{4}
'''.format(dest, src, srclang.upper(),
        lang.get_compile_script(srclang, str(src), str(dest)), extra))

def __build_cp(src, dest, extra='') :
    print('''{0} : {1}
\t@mkdir -p $(dir $@)
\t@echo + [CP] $@
\t@cp {1} {0}
{2}
'''.format(dest, src, extra))

def accessory() :
    com.setprob()
    src = __get_validator_src()
    dest = __get_validator_dest()
    srclang = lang.identify_source_lang(src)
    __build_exec(srclang, src, dest)
    src = __get_checker_src()
    dest = __get_checker_dest()
    srclang = lang.identify_source_lang(src)
    __build_exec(srclang, src, dest)

def solution() :
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

def samplegen() :
    com.setprob()
    for name, gen, flag, issample, desc in csv.reader(sys.stdin, delimiter='\t') :
        if not issample : continue
        __build_cp(__get_data_in(name), __get_sample_in(name),
            'DATAGEN_SAMPLE_TARGETS += ' + __get_sample_in(name))
        __build_cp(__get_data_ans(name), __get_sample_ans(name),
            'DATAGEN_SAMPLE_TARGETS += ' + __get_sample_ans(name))

