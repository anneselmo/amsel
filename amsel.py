#! /usr/bin/python3
import os
import json

import utils
import scripts

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
    i=0
    while "{{" in text:
        if i > 10:
            return(text)
        for module in universals:
            if module not in cats:
                text=text.replace("{{"+module+"}}", universals[module])
        for cat in cats:
            for submod in universals[cat]:
                text=text.replace("{{"+cat+"."+submod+"}}", universals[cat][submod])
        i=i+1
    return(text)

def run_commands(inp):
    i=0
    print(root, "ROOT")
    inp=inp.split("[")
    text, out=[], ""
    for value in inp:
        for part in value.split("]"):
            text.append(part)
    for value in text:
        if value.startswith("!") and value.endswith("!"):
           print(eval("scripts."+(value.replace("!", ""))))

           text[i]=eval("scripts."+(value.replace("!", "")))
        i=i+1 

    for value in text:
        out=out+str(value)
    return(out)

def build_framework(path, dest, cats):
    print(cats)
    for cat in cats:
        for item in utils.recursive_scan(cat, [path]):
            item=item.replace(path, dest)
            item=item.replace(cat, "html")
            print(item, "Q")
            try:
                open(item, 'a').close()
            except:
                build=os.path.abspath(item).rsplit("/", 1)
                os.makedirs(build[0])
                open(item, 'a').close()

    return(0)

def gen(path, dest):
    global universals 
    global root
    global absroot
    root=dest
    absroot=os.path.abspath(root)
    cats=["proto", "site"]
    build_framework(path, dest, cats)
    universals=load_config(path, cats)
    for cat in cats:
        for item in utils.recursive_scan(cat, [path]):
            write_page(item, item.replace(cat, "html").replace(path, dest), cats)
    return("done")

def load_config(path, cats):
    print("conf")
    out={}
    for cat in cats:
        print(cat)
        out[cat]={}
        for thing in utils.recursive_scan(cat+".conf", [path]):
            name=thing.replace(cat+".conf", "")
            name=str(name).split("/")
            try:
                data=load_json(thing)
            except:
                data=utils.file_dump(thing)
            out[cat][name[-1:][0][:-1]]=utils.file_dump(thing)
    try:
        out.update(load_json(path+"/config.json"))
    except:
        pass
    return(out)

def dprint(d):
    for key in d:
        print(key, d[key])
    return("fish")

def write_page(source, dest, cats):
    print("wee")
    #try:
    with open(source, 'r') as inp:
        out=insert_modules(inp.read(), cats)
        out=run_commands(out)
    with open(dest, 'w') as fin:
        fin.write(out)
    return(0)

gen("./in", "./out")
