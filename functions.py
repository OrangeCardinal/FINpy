def cagr(start_price, end_price, num_days):
    """
    Calculates the Compound Annualized Growth Rate

    :param start_price:
    :param end_price:
    :param num_days: Trading Days or Calendar
    :return:
    """


    cagr = (end_price / start_price) ** (365.0 / num_days) - 1
    return cagr