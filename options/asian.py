import numpy
from math import sqrt,log
from scipy.stats import norm

def price_asian_call(initial_price, strike, interest, remaining_time, sigma, periods_monitored):
    """
    Price an Asian call using the geometric mean of the Black-Scholes-Merton model

    :param initial_price: 
    :param strike: 
    :param interest: 
    :param remaining_time: 
    :param sigma: 
    :param periods_monitored: 
    :return: 
    """
    ## Auxiliary parameters
    r_GM = 0.5 * (interest * (periods_monitored + 1) / periods_monitored - sigma ** 2 * (1.0 - 1.0 / periods_monitored ** 2) / 6.0)
    sigma_GM = sigma * numpy.sqrt((2.0 * periods_monitored ** 2 + 3.0 * periods_monitored + 1.0) / (6.0 * periods_monitored ** 2))

    d_plus = log(initial_price / (strike * numpy.exp(-r_GM * remaining_time))) / (sigma_GM * sqrt(remaining_time)) + sigma_GM * numpy.sqrt(remaining_time) / 2.0
    d_minus = d_plus - sigma_GM * numpy.sqrt(remaining_time)

    ## Pricing formula
    price = numpy.exp(-interest * remaining_time) * (initial_price * numpy.exp(r_GM * remaining_time) * norm.cdf(d_plus) - strike * norm.cdf(d_minus))

    return price