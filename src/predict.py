# _*_ coding: utf-8 _*_

"""
Order number prediction of car parts based on time series method.

Author: StrongXGP (xgp1227@gmailcom)
Date:   2018/09/29
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, arma_order_select_ic


def is_stationary(ts, maxlag=15, autolag=None, regression='ct'):
    """Checks if the time series `ts` is stationary."""
    adf_result = adfuller(ts, maxlag=maxlag, autolag=autolag, regression=regression)
    return adf_result[0] < adf_result[4]['%5']


def d_param(ts, max_lag=12):
    """Finds out the differential order."""
    if is_stationary(ts):
        return 0
    else:
        for i in range(1, max_lag + 1):
            if is_stationary(ts.diff(i).dropna()):
                return i


def ARMA_params(ts, max_ar=4, max_ma=2, ic='aic'):
    """Finds out the AR order `p` and the ma order `q`."""
    if ic == 'aic':
        return arma_order_select_ic(ts.dropna(), max_ar=max_ar, max_ma=max_ma, ic=ic).aic_min_order
    elif ic == 'bic':
        return arma_order_select_ic(ts.dropna(), max_ar=max_ar, max_ma=max_ma, ic=ic).bic_min_order
    elif ic == 'hqic':
        return arma_order_select_ic(ts.dropna(), max_ar=max_ar, max_ma=max_ma, ic=ic).hqic_min_order


def main():
    """Process procedure."""

    # Load data
    data_path = "../data/"
    df = pd.read_csv()