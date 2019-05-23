.PHONY : clean ALL
.DEFAULT_GOAL=ALL

build/Makefile.validator-build : meta.json
	mkdir -p $(dir $@)
	../../pc api.mksyn.validatorbuild > $@

build/Makefile.sol-build : $(shell find solution)
	mkdir -p $(dir $@)
	../../pc api.mksyn.solbuild > $@

build/Makefile.data-build : data/datalist
	mkdir -p $(dir $@)
	$< | ../../pc api.mksyn.databuild > $@

build/Makefile.data-gen : data/datalist meta.json
	mkdir -p $(dir $@)
	$< | ../../pc api.mksyn.datagen > $@

include build/Makefile.validator-build
include build/Makefile.sol-build
include build/Makefile.data-build
include build/Makefile.data-gen

datagen : $(DATAGEN_INPUT_TARGETS) $(DATAGEN_OUTPUT_TARGETS)

ALL:

clean :
	rm -rf build

.DELETE_ON_ERROR:
