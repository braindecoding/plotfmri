# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 06:00:32 2024

@author: rolly
"""

import os
import sys
import numpy as np
import scipy.io as sio

# Set the saveFnamePostFix
saveFnamePostFix = '-1to2mm_Th1_fromAna_s1071119ROI_resol10'

scriptName = 'make_fmri_roi_visRecon'
print('\n============================================================')
print('\n{}'.format(scriptName))

# ============================================================
# option to print details
verbose = 0

dataPath = 'data/'

# Library paths
libRootPath = '../../lib/'
libLocalPath = '../lib/'
sys.path.append(os.path.join(libRootPath, 'BDTB-1.2.2/'))
sys.path.append(os.path.join(libRootPath, 'spm5/'))
sys.path.append(libLocalPath)

# ------------------------------
# General & Data paths

# Name of the experiment
P_Gen_experiment = 'visual reconstruction fMRI experiment (test new data format)'

# Subject ID
sbjId = 's1'
P_Gen_sbjId = sbjId

# Set path to resliced data
P_Gen_path_data = os.path.join(dataPath, 's1_resliced/')

# Total number of runs
P_Gen_runs_max = 20 + 12  # train + test

# ------------------------------
# fMRI-specific

# TR = secs per sample (1 sample = 1 TR = 1 volume for fMRI)
P_fMRI_TR = 2

# first vol of each run
P_fMRI_begin_vols = 5

# Volume to which the others are aligned
P_fMRI_vol_align = 5

# Number of train samples in a run
nTrainSmpl = 22

# Maps task run numbers 1,2,... to file run letters
P_expList = {
    1: ['a', 'b', 'd', 'e', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 's', 't', 'v', 'w', 'y', 'z', 'ab', 'ac'],#random stimuli
    2: ['c', 'f', 'r', 'u'],#untuk gambar
    3: ['i', 'x'],#untuk huruf NEURA kecil
    4: ['l', 'aa'],#untuk huruf NEURO panjang
    5: ['o', 'ad', 'ae', 'af']#untuk huruf NEURO gepeng
}

P_fMRI_run_names = P_expList[1] + P_expList[2] + P_expList[3] + P_expList[4] + P_expList[5]

P_expListStimId = {
    1: list(range(1, 21)),#random stimulus
    2: list(range(1, 5)),# gambar
    3: list(range(1, 3)),#huruf NEURO
    4: list(range(1, 3)),#huruf NEURO
    5: list(range(1, 5))#huruf NEURO
}

nTrainRuns = len(P_expList[1])
nTestFigRuns = len(P_expList[2])
nTestNeuSRuns = len(P_expList[3])
nTestNeuSLRuns = len(P_expList[4])
nTestNeuSTRuns = len(P_expList[5])
