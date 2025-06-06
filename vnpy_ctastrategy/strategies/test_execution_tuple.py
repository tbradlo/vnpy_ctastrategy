from datetime import datetime
from decimal import Decimal
from unittest import TestCase
from unittest.mock import patch

from sortedcontainers import SortedDict
from vnpy_ctastrategy.strategies.execution_tuple import calculate_profit, ExecutionTuple

from vnpy_ctastrategy.backtesting import BacktestingEngine

from vnpy_ctastrategy.base import BacktestingMode

from vnpy.trader.constant import Exchange, Direction, Interval
from vnpy.trader.object import TickData, PositionData
from vnpy_ctastrategy.strategies.grid_buy import GridBuyStrategy


class TestGridBuy(TestCase):

    def test_when_BMW_should_calculateProfit(self):
        # given
        executions = [
            ExecutionTuple(date='2023-08-02T12:26:24Z', price=Decimal('104.18'), volume=Decimal('7')),
            ExecutionTuple(date='2023-08-14T09:00:29Z', price=Decimal('98.98'), volume=Decimal('8')),
            ExecutionTuple(date='2023-09-01T09:39:58Z', price=Decimal('95.4'), volume=Decimal('8')),
            ExecutionTuple(date='2023-10-23T11:38:01Z', price=Decimal('91.95'), volume=Decimal('6')),
            ExecutionTuple(date='2023-10-26T09:03:04Z', price=Decimal('88.63'), volume=Decimal('6')),
            ExecutionTuple(date='2024-02-22T09:03:44Z', price=Decimal('105.64'), volume=Decimal('-5')),
            ExecutionTuple(date='2024-04-04T09:31:47Z', price=Decimal('112.6'), volume=Decimal('-6')),
            ExecutionTuple(date='2024-05-22T09:02:03Z', price=Decimal('93.42'), volume=Decimal('2')),
            ExecutionTuple(date='2024-05-22T09:02:03Z', price=Decimal('93.42'), volume=Decimal('4')),
            ExecutionTuple(date='2024-07-30T13:43:32Z', price=Decimal('86.2'), volume=Decimal('6')),
            ExecutionTuple(date='2024-08-05T03:08:00Z', price=Decimal('79.82'), volume=Decimal('7'))
        ]

        # when
        gotProfit = calculate_profit(executions, 3245)

        # then
        self.assertEqual(-555.44, gotProfit)
