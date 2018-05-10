#! /usr/bin/python3
import os

#scripts that can be run inside of pages

def gen_link(path, text):
    return("<a href='"+path+"'>"+text+"</a>")

def gen_index(path, root):
    index=""
    for item in os.listdir(path):
        index=index+str(gen_link(str(root+item), item.split(".")[0]))
    return(index)

