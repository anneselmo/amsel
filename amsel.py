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
       
def insert_modules(text, cats):
    for module in universals:
        text=text.replace("{{"+module+"}}", universals[module])
    for cat  in cats
        for submod in universals[cat]:
            text=text.replace("{{"+module+"}}", universals[cat][module])
    return(text)

def gen(path, dest):
    global universals
    code="proto"
    try:
        os.makedirs(dest)
    except:
        pass
    universals=load_config(path, code)
    print(universals)
    for item in utils.recursive_scan(code, [path]):
        write_page(dest+item.replace(code, "html"), code)
    return("done")

def load_config(path, [cats]):
    print("conf")
    out={}
    for thing in utils.recursive_scan(cat+".conf", [path]):
        out[thing.replace(cat+".conf", "")]=utils.file_dump(thing)
    try:
        out.update(load_json(path+"/config.json"))
    except:
        pass
    return(out)

def write_page(dest, cats):
    try:
        with open(path+"/"+source, 'r') as inp:
            out=insert_modules(inp.read(), [cats])
            out=run_commands(out)
        with open(outpath+"/"+dest, 'w') as fin:
            fin.write(out)
        return(0)
    except:
        return(1)

gen("./in", "./out")
