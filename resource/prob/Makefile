SHORTNAME	:= $(shell basename $(shell pwd))

.PHONY : data sample cf clean ALL
.DEFAULT_GOAL=ALL

build/Makefile.accessory : meta.json
	mkdir -p $(dir $@)
	../../pc api.mksyn.accessory > $@

build/Makefile.solution : $(shell find solution)
	mkdir -p $(dir $@)
	../../pc api.mksyn.solution > $@

build/Makefile.data-build : data/datalist
	mkdir -p $(dir $@)
	$< | ../../pc api.mksyn.databuild > $@

build/Makefile.data-gen : data/datalist meta.json
	mkdir -p $(dir $@)
	$< | ../../pc api.mksyn.datagen > $@

build/Makefile.sample-gen : data/datalist
	mkdir -p $(dir $@)
	$< | ../../pc api.mksyn.samplegen > $@

include build/Makefile.accessory
include build/Makefile.solution
include build/Makefile.data-build
include build/Makefile.data-gen
include build/Makefile.sample-gen

data : $(DATAGEN_INPUT_TARGETS) $(DATAGEN_OUTPUT_TARGETS)

sample : $(DATAGEN_SAMPLE_TARGETS)

CF_TARGET	= build/package/$(SHORTNAME).zip
cf : data
	rm -rf $(CF_TARGET)
	cd build/data/gen && zip $(shell basename $(CF_TARGET)) *.in *.ans
	mkdir -p $(CF_TARGET)
	mv build/data/gen/$(shell basename $(CF_TARGET)) $(CF_TARGET)

ALL:

clean :
	rm -rf build

.DELETE_ON_ERROR:
