from math import sqrt,log,pow, exp, e, pi
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

    result = exp(-1*q*remaining_time) * norm.cdf(d1)
    return result


def call_price(price, strike, vol, risk_free_rate, dividend_rate, remaining_time):
    """
    Calculate the call price of an american style option

    :param price:
    :param strike:
    :param vol:
    :param risk_free_rate:
    :param dividend_rate: As an annualized percentage
    :param remaining_time:
    :return:
    """
    d1 = (log((price/strike)) + remaining_time * (risk_free_rate - dividend_rate + pow(vol, 2))) / vol * sqrt(remaining_time)
    d2 = d1 - vol * sqrt(remaining_time)

    result = (price * exp(-1 * dividend_rate * remaining_time) * norm.cdf(d1)) - (strike * exp(-1 * risk_free_rate * remaining_time) * norm.cdf(d2))
    return result

def call_theta(price, strike, vol, risk_free_rate, dividend_rate, remaining_time, T):
    """

    :param price:
    :param strike:
    :param vol:
    :param risk_free_rate:
    :param dividend_rate: As an annualized percentage
    :param remaining_time:
    :param T: Number of days (can be calendar days or trading days)
    :return:
    """
    d1 = (log((price / strike)) + remaining_time * (risk_free_rate - dividend_rate + pow(vol, 2))) / vol * sqrt(remaining_time)
    d2 = d1 - vol * sqrt(remaining_time)

    term1 = -1 * ((strike * vol * pow(e, -1 * dividend_rate * remaining_time)) / 2 * sqrt(remaining_time)) * (1 / sqrt(2 * pi)) * (pow(e, -1 * pow(d1, 2)))

    term2 = risk_free_rate * strike * pow(e,-1*risk_free_rate*remaining_time) * norm.cdf(d2)

    term3 = dividend_rate * price * pow(e,-1*dividend_rate*remaining_time) * norm.cdf(d1)

    result = 1/T * (term1 - term2 + term3)

def put_delta(price, strike, vol, r, q, remaining_time):
    d1 = (log((price / strike)) + remaining_time * (r - q + pow(vol, 2))) / vol * sqrt(remaining_time)
    result = exp(-1*q*remaining_time) * (norm.cdf(d1) - 1)
    return result

def put_price(price, strike, vol, r, q, remaining_time):
    d1 = (log((price / strike)) + remaining_time * (r - q + pow(vol, 2))) / vol * sqrt(remaining_time)
    d2 = d1 - vol * sqrt(remaining_time)

    result = (strike*exp(-1*r*remaining_time) * norm.cdf(-1*d2)) - (price * exp(-1*q*remaining_time) * norm.cdf(-1*d1))
    return result

def put_theta(price, strike, vol, risk_free_rate, dividend_rate, remaining_time, T):
    """
    Calculates theta for an american style option

    :param price:
    :param strike:
    :param vol:
    :param risk_free_rate:
    :param dividend_rate:
    :param remaining_time:
    :param T:
    :return:
    """
    d1 = (log((price / strike)) + remaining_time * (risk_free_rate - dividend_rate + pow(vol, 2))) / vol * sqrt(remaining_time)
    d2 = d1 - vol * sqrt(remaining_time)

    term1 = -1 * ((strike * vol * pow(e, -1 * dividend_rate * remaining_time)) / 2 * sqrt(remaining_time)) * (1 / sqrt(2 * pi)) * (pow(e, -1 * pow(d1, 2)))

    term2 = risk_free_rate * strike * pow(e,-1*risk_free_rate*remaining_time) * norm.cdf(d2)

    term3 = dividend_rate * price * pow(e,-1*dividend_rate*remaining_time) * norm.cdf(d1)

    result = 1/T * (term1 + term2 - term3)
    return result

def gamma(price, strike, vol, risk_free_rate, q, remaining_time):
    """
    Calculate the gamme for an american style option

    :param price:
    :param strike:
    :param vol:
    :param risk_free_rate:
    :param q:
    :param remaining_time:
    :return: gamma
    """
    d1 = (log((price / strike)) + remaining_time * (risk_free_rate - q + pow(vol, 2))) / vol * sqrt(remaining_time)

    term1  = pow(e,-1 * q * remaining_time) / (strike * vol * sqrt(remaining_time))

    term2 = 1 / sqrt(2 * pi)

    exponent = -1 * pow(d1,2) / 2
    term3 = pow(e, exponent)
    result = term1 * term2 * term3
    return result

def rho():
    pass