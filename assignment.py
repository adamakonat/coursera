#!/bin/bash
oldFiles.txt
files=$ (grep " jane " ../data/list.txt | cut -d' ' -f3)
for f in $files; do
if [ -e $HOME$f ]; then
echo $HOME$f >> oldFiles.txt;
fi
done





import sys 
import subprocess
f = open(sys.argv[1], "r")
for line in f.readlines():
old_nane = line.strip()
new_name = old_name.replace("jane", "jdoe")
subprocess.run(["mv", old_name, new_name])
f.close()
