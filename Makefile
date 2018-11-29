PACKAGE_DIR = package
BUILD_DIR = build
SOURCE_DIR = src

CXX = g++
CXXFLAGS += -std=c++11 -g -O2 -Wall -pipe -I./include

CP = cp

SRCS = $(shell find $(SOURCE_DIR) -name "*.cpp")
OBJS = $(SRCS:$(SOURCE_DIR)/%.cpp=$(BUILD_DIR)/%)

.PHONY : default clean datagen

default : datagen

# generate c++ executables
$(BUILD_DIR)/% : $(SOURCE_DIR)/%.cpp
	@mkdir -p $(dir $@)
	@echo + [C++]\\t\\t$@
	@$(CXX) $(CXXFLAGS) -o $@ $<

# generate answer file
%.ans : %.in $(BUILD_DIR)/std
	@mkdir -p $(dir $@)
	@echo + [GEN]\\t\\t$@
	@$(BUILD_DIR)/std < $< > $@
	
clean :
	rm -rf $(BUILD_DIR)
	rm -rf $(PACKAGE_DIR)

Makefile.data : datamake.py data.yaml
	./datamake.py > Makefile.data

-include Makefile.data

datagen: $(DATA_TARGETS)
.DELETE_ON_ERROR : $(DATA_TARGETS)
