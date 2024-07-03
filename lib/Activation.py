# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:08:22 2023

@author: gmart
"""
import os
import datetime
import subprocess
def date_today():
    now = datetime.datetime.now()
    form = "%Y-%m-%d_%H:%M:%S"
    date = now.strftime(form)
    return date

dir_doc             = "C:/Users/gmart/Desktop/Captain_boya/CAPTAIN-buoy.github.io"
input_doc           = "Input/"
Output              = "Output/"
lib                 = "lib/"
os.chdir(dir_doc + lib)
from Florimetry import plot_flori
plot_flori(dir_doc)
#Push to web
os.chdir(dir_doc)
today= date_today()
commit = "git commit -am"+' "'+ today + '"'
git_command = ["git status", "git add *",commit,"git pull", "git push"]

for command in git_command:
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    if result.returncode == 0:
        print(f"Salida de Git para '{command}':")
        print(result.stdout)
    else:
        print(f"Error al ejecutar el comando Git '{command}':")
        print(result.stderr)
