#
#oValuation of European call options in Black-SCholes-Merton model
#incl. Vega function and impiled volatility estimation
#bsm_function.py
#

#Analytical Black-Scholes-Merton(BSM) Formula

def bsm_call_value(S0, K, T, r, sigma):

    from math import log, sqrt, exp
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0/ K) + (r + sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(S0/ K) + (r - sigma ** 2) * T) / (sigma * sqrt(T))
    C =
