# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from source.util.dataframe_generator import DataFrameGenerator
from source.normality_battery import NormalityBattery

df = DataFrameGenerator(seed=42, size=(1000, 100))
methods = df.__getmethods__()

for method in methods:
    print("starting method: " + method + "()")
    nb = NormalityBattery(getattr(df, method)())
    nb.normality_report(digits=3)
