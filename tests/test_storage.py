"""
to run tests: pipenv run pytest
to run pytest-coverage: pipenv run pytest --cov=packagename tests/
"""

## for debug
## import pdb; pdb.set_trace()

# # generate path to package directory
# import sys, pathlib
# packagename = 'packagename'
# path = str(pathlib.Path(__file__).parents[1]) + '/' + packagename
# if path not in sys.path:
#     sys.path.append(path)

# imports
import pytest
from packagename.storage import DataStore

# set up variables to be used across multiple tests
@pytest.fixture
def datastore():
    return DataStore()

## ----- actual tests -----

def test_getPrice(datastore):
    """
    Test that getPrice works
    """
    assert datastore.getPrice('buy', 'GBP') == 1.72
    assert datastore.getPrice('sell', 'GBP') == 1.68

    assert datastore.getPrice('buy', 'USD') == 1.36
    assert datastore.getPrice('sell', 'USD') == 1.34

def test_getPrice_exception(datastore):
    """
    Test that Error is raised for:
    - e1: invalid base currencies
    - e2: invalid exchange rate pairings
    - e3 & e4: invalid values apart from buy/sell
    """

    with pytest.raises(Exception) as e:
        datastore.getPrice('sell', 'GBP', 'CNY')
    assert str(e.value) == "We only support SGD as a base currency for now, not CNY, sorry!"

    with pytest.raises(Exception) as e2:
        datastore.getPrice('sell', 'AUD')
    assert str(e2.value) == "We do not have the exchange rate for AUD against SGD for now, sorry!"

    with pytest.raises(Exception) as e3:
        datastore.getPrice('hahahaha', 'USD')
    assert str(e3.value) == "Only 'buy' or 'sell' values allowed"

    with pytest.raises(Exception) as e4:
        datastore.getPrice('hahahaha', 'GBP')
    assert str(e4.value) == "Only 'buy' or 'sell' values allowed"