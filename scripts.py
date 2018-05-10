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

def gen_blog_index(path, root):
    index="<p>"
    flist=os.listdir(path)
    flist.sort(reverse=True, key=lambda r: r.split(".")[0])
    for item in flist:
        index=index+"<h2>"+str(gen_link(str(root+item), item.split(".")[1]))+"</h2>"
        index=index+item.split(".")[0]+"<br>"
    return(index)


