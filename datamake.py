#!/usr/bin/env python3
import yaml

targets = []

def gen_testpoint(testpoint) :
    name = testpoint["name"]
    src = testpoint["src"]
    is_manual = src.endswith(".txt")
    flags = str(testpoint.get("flags", ""))

    mk = []
    target = "$(PACKAGE_DIR)/data/" + name + ".in"

    targets.append("$(PACKAGE_DIR)/data/" + name + ".ans")

    target += " : "

    if is_manual :
        target += "$(SOURCE_DIR)/data/" + src
    else : 
        target += "$(BUILD_DIR)/data/" + src
        
    target += " $(BUILD_DIR)/validator"

    mk.append(target)
    mk.append("\t@mkdir -p $(dir $@)")

    if is_manual :
        mk.append("\t@echo + [CP]\\\\t\\\\t$@")
        mk.append("\t@$(CP) $< $@")
    else :
        mk.append("\t@echo + [GEN]\\\\t\\\\t$@")
        mk.append("\t@$(BUILD_DIR)/data/" + src + " " + flags + " < $< > $@")
    
    mk.append("\t@echo + [VALIDATE]\\\\t$@")
    mk.append("\t@$(BUILD_DIR)/validator < $@")
    mk.append("")
    return '\n'.join(mk)

tpl = yaml.load(open("data.yaml").read())

for tp in tpl :
    print(gen_testpoint(tp))
    
print("DATA_TARGETS = \\\n  " + ' \\\n  '.join(targets))

