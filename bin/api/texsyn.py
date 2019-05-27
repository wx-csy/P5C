from .. import lang, prob
from .. import common as com
import csv, sys, pathlib

def contest() :
    com.setroot()
    print(r'\input{../../resource/statement/stat.tex}')
    print(r'\begin{document}')
    meta:dict = prob.load_problist()
    for shortname in sorted(meta, key=lambda k:meta[k]['order']) :
        print(r'\subimport{../../contest/%s/statement/}{stat.tex}' % shortname)
    print(r'\end{document}')
