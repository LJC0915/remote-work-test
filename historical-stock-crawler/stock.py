import investpy
import json


def get_stock_historical_data(stock, from_date, to_date):
    """
    Args:
        stock (:obj:`str`): symbol of the stock to retrieve historical data from.
        from_date (:obj:`str`): date formatted as `dd/mm/yyyy`, since when data is going to be retrieved.
        to_date (:obj:`str`): date formatted as `dd/mm/yyyy`, until when data is going to be retrieved.
    """
    response = investpy.get_stock_historical_data(
        stock=stock, country='United States', from_date=from_date, to_date=to_date, as_json=True)
    data = json.loads(response)
    historical_data = data['historical']
    return historical_data
