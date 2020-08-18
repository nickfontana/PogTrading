import boto3
from decimal import Decimal


def create_transaction(date, pair, price, takeprofit, stoploss, units, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1') 

    table = dynamodb.Table('ForexBot')
    response = table.put_item(
       Item={
            'Date': date,
            'Currency Pair': pair,
            'Price': Decimal(str(price)),
            'Take Profit': Decimal(str(takeprofit)),
            'Stop Loss': Decimal(str(stoploss)),
            'Units': Decimal(str(units))
        }
    )
    return response


if __name__ == '__main__':
    print('add params')
