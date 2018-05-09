#! /usr/bin/python3
import os
import json

import utils

def load_json(temp):
    with open(temp, 'r') as late:
        return(json.load(late))

def scan_html(html):
    index=[]

    for item in html.split("{{"):
        if "}" in item:
            for line in item.split("\n"):
                index.append(line.split("}")[0])

    return(index)
       
def insert_modules(text, specifics):
    for module in universals:
        text=text.replace("{{"+module+"}}", universals[module])
    for module in specifics:
        text=text.replace("{{"+module+"}}", specifics[module])
    return(text)

def gen(path, dest):
    try os.mkdir(dest)
    global universals
    try:
        universals=load_json(path+"/config.json")
        with open(path+"/style.css", 'r') as css:
            universals[css]=css.read()
    except:
        print("/me kindly requests a config.json")
        exit()
    for item in utils.recursive_scan("proto", path):
        write_page(find_specifcs(item), dest+item.replace("proto", "html"))
        return("done")


def write_page(specifics, dest)
    try:
        with open(path+"/"+source, 'r') as inp:
            out=insert_modules(inp.read(), specifics)
            out=run_commands(out)
        with open(outpath+"/"+dest, 'w') as fin:
            fin.write(out)
        return(0)
    except:
        return(1)


gen("./in", "./out")
