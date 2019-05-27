SHORTNAME	:= $(shell basename $(shell pwd))

.PHONY : data sample statement cf clean ALL
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

build/statement/statement.pdf : $(shell find statement -type f)
	mkdir -p $(dir $@)
	xelatex --output-directory=$(dir $@) '\input{../../resource/statement/stat.tex}\begin{document}\subimport{statement/}{stat}\end{document}'
	xelatex --output-directory=$(dir $@) '\input{../../resource/statement/stat.tex}\begin{document}\subimport{statement/}{stat}\end{document}'

data : $(DATAGEN_INPUT_TARGETS) $(DATAGEN_OUTPUT_TARGETS)

sample : $(DATAGEN_SAMPLE_TARGETS)

statement : build/statement/statement.pdf

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
