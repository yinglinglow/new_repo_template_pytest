def sgd_gbp(buyorsell : str) -> float:
    """
    Returns buy/sell price of GBP against SGD
    """
    gbp = [1.72, 1.68]

    if buyorsell == 'buy':
        return gbp[0]
    else:
        return gbp[1]


def sgd_usd(buyorsell : str) -> float: 
    """
    Returns buy/sell price of USD against SGD
    """
    usd = {'buy': 1.36, 'sell': 1.34}
    return usd.get(buyorsell)