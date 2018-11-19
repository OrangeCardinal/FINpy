from math import sqrt,log,pow, exp
from scipy.stats import norm




def call_delta(price, strike, vol, r, q, remaining_time):
    """
    Calculate the delta of an american style option

    :param price: Underlying Asset Price
    :param strike: Strike Price
    :param vol: Volatility (Percentage)
    :param r: Continuously Compounded risk free interest rate
    :param q: continuously compounded dividend yield
    :param remaining_time: Time to Exipiration (expressed as percentage of a year)
    :return:
    """
    d1 = (log((price/strike)) + remaining_time * (r - q + pow(vol, 2))) / vol * sqrt(remaining_time)
    d2 = d1 - vol * sqrt(remaining_time)


def call_price(price, strike, vol, r, q, remaining_time):
    """
    Calculate the call price of an american style option

    :param price:
    :param strike:
    :param vol:
    :param r:
    :param q:
    :param remaining_time:
    :return:
    """
    d1 = (log((price/strike)) + remaining_time * (r - q + pow(vol, 2))) / vol * sqrt(remaining_time)
    d2 = d1 - vol * sqrt(remaining_time)

    result = (price * exp(-1*q*remaining_time) * norm.cdf(d1)) - (strike*exp(-1*r*remaining_time)*norm.cdf(d2))
    return result

def put_delta():
    pass

def put_price(price, strike, vol, r, q, remaining_time):
    d1 = (log((price / strike)) + remaining_time * (r - q + pow(vol, 2))) / vol * sqrt(remaining_time)
    d2 = d1 - vol * sqrt(remaining_time)

    result = (strike*exp(-1*r*remaining_time) * norm.cdf(-1*d2)) - (price * exp(-1*q*remaining_time) * norm.cdf(-1*d1))
    return result

def gamma(strike_price):
    pass

def rho():
    pass