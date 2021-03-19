#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:23:02 2021

@author: twguest
"""

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from felpy.analysis.statistics.correlation import norm

from mpl_toolkits.axes_grid1 import make_axes_locatable


def intensity_plot(arr,
                   px,
                   py, 
                   title = None,
                   xlabel = None,
                   ylabel = None,
                   context = 'talk',
                   cmap = 'bone',
                   normalise = False):
    
    sns.set_style('dark')
    sns.set_context(context)
    
    if normalise:
        arr = norm(arr)
    
    fig, ax1 = plt.subplots()
    
    img = ax1.imshow(arr,
                     extent = [-(arr.shape[0]//2)*px, (arr.shape[0]//2)*px,
                               -(arr.shape[1]//2)*py, (arr.shape[1]//2)*py],
                     cmap = cmap)
    
    divider = make_axes_locatable(ax1)
    cax = divider.append_axes('right', size='7.5%', pad=0.05)
    
    cbar = fig.colorbar(img, cax)
    cbar.set_label("Intensity (a.u.)")
    
    ax1.set_title(title)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.set_aspect(1.25)
    

from felpy.utils.np_utils import get_mesh
    
def colorbar_plot(arr,
                  mesh = None,
                  label = None,
                  title = None,
                  xlabel = None,
                  ylabel = None,
                  clabel = "",
                  context = 'notebook',
                  sdir = None,
                  cmap = 'bone',
                  normalise = False):
    
    """ 
    plot the correlation function of a pair of 2D arrays (x,y)
    
    :param corr: 2D correlation array (via get_correlation)
    :param mesh: coordinate mesh [np array]
    :param sdir: save directory for output .png
    :param label: figure label
    :param title: figure title
    :param cmap: figure color map
    """
    
    if normalise:
        norm(arr)
        
    sns.set_context(context)
    sns.set_style('dark')
    
    fig, ax1 = plt.subplots()
    
    img = ax1.imshow(arr, cmap = cmap,
                     extent = [np.min(mesh[1])*1e6, np.max(mesh[1])*1e6,
                               np.min(mesh[0])*1e6, np.max(mesh[0])*1e6])
    
    fig.suptitle = title

    divider = make_axes_locatable(ax1)
    cax = divider.append_axes('right', size='7.5%', pad=0.05)

    cbar = fig.colorbar(img, cax)
    cbar.set_label("")
    
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    
    ax1.annotate(label, horizontalalignment = 'left',   
                    verticalalignment = 'bottom',
                    xy = (0,1),
                    c = 'white')
    
    if sdir is None:
        fig.show()
    else:
        fig.savefig(sdir)
        plt.show()
        
        
if __name__ == '__main__':
    
    
    arr = np.random.rand(500,500) * 100
    
    arr = colorbar_plot(arr, get_mesh(arr, 1,1))
    
    
# =============================================================================
#     intensity_plot(arr, 1, 1,
#                    xlabel = "x (m)",
#                    normalise = True)    
#     
# =============================================================================
