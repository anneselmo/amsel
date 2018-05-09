#! /usr/bin/python3
import os

#scripts that can be run inside of pages

def gen_link(path, text):
    return("<a href='"+path+"'>"+text+"</a>")

def gen_index(path):
    index=""
    for item in os.listdir(path):
        index=index+str(gen_link(str(path+item), item.split(".")[1]))
    return(index) 

        
