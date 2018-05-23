#! /usr/bin/python3
import os
import utils

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

def gen_gallery(path, root, tpath, ntpath):
    index="""<div class="container"> <div class="gallery">"""
    flist=os.listdir(path)
    tflist=os.listdir(tpath)
    for item in flist:
        if item in tflist:
            index=index+"""<a href='"""+root+item+"""' target='_blank'><img src='"""+ntpath+item+"""'></a>"""
    index=index+"</div></div>"
    return(index)

def neo_gen_gallery(sdir, fdest, tdest, source, absroot):
    index="""<div class="container"> <div class="gallery">"""
    print("SOURCE", source)
    print("SDIR", sdir)
    flist=os.listdir(source+sdir)
    for item in flist:
        print(item, "X")
        try:
            utils.resize_image(source+sdir+item, 1200, absroot+tdest+item)
            index=index+"""<a href='"""+fdest+item+"""' target='_blank'><img src='"""+tdest+item+"""'></a>"""
        except:
            pass
    index=index+"</div></div>"
    return(index)
