from packagename.exchangerates import *

class DataStore:

    def __init__(self):
        pass

    def getPrice(self, 
                buyorsell : str, 
                currency : str, 
                basecurrency : str ='SGD'
                ) -> float:

        """
        getPrice(buyorsell, currency, basecurrency='SGD')

        Returns the buy or sell price of a currency against a base currency.

        Parameters
        ----------
        buyorsell : {'buy', 'sell'}
            The buy or sell price.

        currency : str
            The currency to use (against the base currency).

        basecurrency : str, optional
            The base currency against which the price is calulated. Defaults to 'SGD'.

        Returns
        -------
        float
            The buy or sell price of a currency against a base currency.
        
        Example
        -------
        >>> from packagename.storage import DataStore
        >>> ds = DataStore()
        >>> ds.getPrice('buy', 'GBP')
        1.72

        """

        if buyorsell not in ['buy', 'sell']:
            raise ValueError("Only 'buy' or 'sell' values allowed")
        
        # list of available exchange rates for each key (the base currency)
        sgd_pricemap = {
            'GBP': sgd_gbp,
            'USD': sgd_usd,
        }

        # returns function to get the currency price
        if basecurrency == 'SGD':
            get_currencyprice = sgd_pricemap.get(currency)
            if get_currencyprice is None:
                raise ValueError(f"We do not have the exchange rate for {currency} against SGD for now, sorry!")

        else:
            raise ValueError(f"We only support SGD as a base currency for now, not {basecurrency}, sorry!")

        return get_currencyprice(buyorsell)