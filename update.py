#!/usr/bin/python3

import markdown
import sys
import codecs
import datetime
import os

##Basedir
BASEDIR="site/"


now = datetime.date.today()

#get article basename
articlename = sys.argv[1][0:sys.argv[1].find(".")]

#read template & markdown content
template = open("template.html", "r").read()
md = codecs.open(sys.argv[1], mode="r", encoding="utf-8").read()

#replace tags by what it needs to be
template = template.replace("#TITLE#", sys.argv[2])
template = template.replace("#CONTENT#", markdown.markdown(md, output_format="html5"))

path = BASEDIR+"/"+str(now.year)+"/"+str(now.month)+"/"

#Make the path if not exists
os.makedirs(path, exist_ok=True)

#Write the content
output = codecs.open(path+articlename+".html", "w", encoding="utf-8", errors="xmlcharrefreplace")

output.write(template)

output.close()


