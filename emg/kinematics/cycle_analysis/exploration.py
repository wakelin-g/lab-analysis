# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: lab
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import mplcatppuccin
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

# %%
# mpl.style.use(["ggplot", "mocha"])
# Comparing primitives

data_path = './wt_1_non-perturbation.csv'
data_input = pd.read_csv(data_path, header=0)
data_input.plot(subplots=True)

plt.show()
