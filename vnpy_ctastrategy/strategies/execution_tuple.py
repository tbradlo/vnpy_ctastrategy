from collections import namedtuple
from decimal import Decimal

ExecutionTuple = namedtuple('ExecutionTuple', ['date', 'price', 'volume'])


def calculate_profit(executions: [ExecutionTuple], position_value: Decimal):
    paid = Decimal('0')
    for execution in executions:
        paid += execution.price * execution.volume
    return float(position_value - paid)