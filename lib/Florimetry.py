# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#CAPTAIN BUOY
#Import 
def plot_flori (dir_doc:str)->str:
    import glob
    import numpy as np
    import os
    import matplotlib.pyplot as plt
    #directory
    input_doc           = "Input/"
    Output              = "Output/"
    doc=glob.glob(dir_doc + input_doc + "*.txt")[0]
    
    #read data doc
    with open(doc, "r",encoding='utf-16le') as buoy:
        arch            = buoy.read()
        arch            = arch.split('+')
    linelist            = []
    # read only the lines that begin with RCV
    for ll in arch:
        if "RCV" in ll:
            l   = ll.replace('\n','')
            linelist.append(l)
    
    #date to study
    date            = []
    for i in linelist:
        dif         = (i[4:])
        dif         = dif.split(",")
        date.append(dif)
    
    florimetry      = np.array(date)
    florimetry      = florimetry[:,2].astype(int)
    ind_pares = [i for i in range(len(florimetry)) if i % 2 == 0]
    ind_impares = [i for i in range(len(florimetry)) if i % 2 != 0]
    
    ratio_1           = florimetry[ind_pares]/florimetry[ind_impares]
    ratio_2           = florimetry[ind_impares]/florimetry[ind_pares]
    #plot
    os.chdir(dir_doc + Output)
    fig                     =plt.figure(figsize=(15,10))
    ax                      =fig.add_axes([0.1,0.1,0.8,0.8])
    ax.plot(ratio_1,"b")
    ax.set_xlabel("Date", fontsize=18)
    ax.set_ylabel("Ratio", fontsize=18)
    ax.tick_params(axis='both', labelsize=20) 
    fig.savefig("plot.jpg",dpi=300)
    

