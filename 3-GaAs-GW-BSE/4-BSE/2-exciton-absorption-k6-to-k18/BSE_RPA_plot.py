#!/usr/bin/env python
#coding: utf-8

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


def plot_Absorb(files, xlim=[0, 10], ylim=None, xtick=None, ytick=None, plabels=None, mode='separately'):
    colors=['r','b','g','c','m','y','brown','pink','purple','k']
    if mode=='separately':
        for i in range(len(files)):
            fname=files[i]+'.dat'
            pname=files[i]+'.png'
            data=np.loadtxt(fname)
            n=len(data)
            omega=[]
            absorb=[]
            for j in range(n):
                omega.append(data[j][0])
                absorb.append(data[j][1])
            fig, ax = plt.subplots()
            p1, = plt.plot(omega, absorb, ls='-', color=colors[i], lw=2, zorder=2)
            plt.xlim(xlim[0], xlim[1])
            plt.ylim(ylim[0], ylim[1])
            plt.yticks (ytick)
            plt.yticks(fontsize =14)
            plt.xticks(xtick)
            plt.xticks(fontsize =14)
            plt.tick_params(axis='both',direction='in')
            plt.ylabel(r'$\epsilon_{2} (\omega)$',fontsize=16)
            plt.xlabel('Energy (eV)',fontsize=16)
            plt.subplots_adjust(top=0.8, bottom=0.2, left=0.2, right=0.8, hspace=0.1, wspace=0.1)
            plt.savefig(pname,dpi=600)
            #plt.show() 
    if mode=='all':
        LINES = []
        omega=[]; absorb=[]
        for i in range(len(files)):
            fname=files[i]+'.dat'
            data=np.loadtxt(fname)
            n=len(data)
            x=[]
            y=[]
            for j in range(n):
                x.append(data[j][0])
                y.append(data[j][1])
            omega.append(x)
            absorb.append(y)
        fig, ax = plt.subplots()
        for i in range(len(files)):
            line, =ax.plot(omega[i], absorb[i], ls='-', color=colors[i], lw=2, zorder=2)
            LINES += [line]
        ax.legend(LINES, plabels, loc='upper left',  fontsize=10, frameon=False)
        plt.xlim(xlim[0], xlim[1])
        plt.ylim(ylim[0], ylim[1])
        plt.yticks (ytick)
        plt.yticks(fontsize =14)
        plt.xticks(xtick)
        plt.xticks(fontsize =14)
        plt.tick_params(axis='both',direction='in')
        plt.ylabel(r'$\epsilon_{2} (\omega)$',fontsize=16)
        plt.xlabel('Energy (eV)',fontsize=16)
        plt.subplots_adjust(top=0.8, bottom=0.2, left=0.2, right=0.8, hspace=0.1, wspace=0.1)
        plt.savefig('BSE_RPA_all.png',dpi=600)

#ax.xaxis.set_major_formatter(plt.NullFormatter())
#plt.legend([p1, p2], ['BSE', 'RPA'], loc='upper left', fontsize=18,shadow=False,frameon=False)

if __name__ == "__main__":
    files=['absorption_noeh', 'absorption_eh']
    plot_Absorb(files, xlim=[1, 6], ylim=[0,40], xtick=None, ytick=None, plabels=['RPA', 'BSE'],  mode='all')
    plot_Absorb(files, xlim=[1, 6], ylim=[0,40], xtick=None, ytick=None, plabels=None,  mode='separately')

