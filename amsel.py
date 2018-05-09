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
    for cat in cats:
        print(type(cat), cat)
        try:
            for submod in universals[cat]:
                text=text.replace("{{"+module+"}}", universals[cat][module])
        except:
            pass
    return(text)

def gen(path, dest):
    global universals
    cats=["proto", "site"]
    try:
        os.makedirs(dest)
    except:
        pass
    universals=load_config(path, cats)
    dprint(universals)
    for cat in cats:
        for item in utils.recursive_scan(cat, [path]):
            print(item)
            print("FISH")
            print(dest+item.replace(cat, "html").replace(path, dest))
            write_page(item, item.replace(cat, "html").replace(path, dest), cats)
    return("done")

def load_config(path, cats):
    print("conf")
    out={}
    for cat in cats:
        for thing in utils.recursive_scan(cat+".conf", [path]):
            print(type(thing))
            name=thing.replace(".conf", "")

            print(name)
            name=str(name).split("/")
            print(name)
            print(thing)

            print(name[-1:])
            out[name[-1:][0]]=utils.file_dump(thing)
    try:
        out.update(load_json(path+"/config.json"))
    except:
        pass
    return(out)

def dprint(d):
    for key in d:
        print(key, d[key])
    return("fish")

def run_commands(inp):
    return(inp)

def write_page(source, dest, cats):
    print("wee")
    #try:
    with open(source, 'r') as inp:
        out=insert_modules(inp.read(), cats)
        out=run_commands(out)
    with open(dest, 'w') as fin:
        fin.write(out)
    return(0)
    #except:
    #    return(1)

gen("./in", "./out")
