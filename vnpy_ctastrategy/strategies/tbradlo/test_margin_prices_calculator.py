from decimal import Decimal
from unittest import TestCase

from vnpy_ctastrategy.strategies.tbradlo.buy_margin_prices_calculator import MarginPricesCalculator
from vnpy_ctastrategy.strategies.tbradlo.buy_percentage_prices_calculator import PercentagePricesCalculator
from sortedcontainers import SortedDict


class TestMarginPricesCalculator(TestCase):

    def test_WEHN_dax_SHOULD_calculate_next_buy(self):
        # given
        last_buy_price = Decimal("16000")
        prices_calculator = MarginPricesCalculator(buy_step=Decimal("999"), sell_step=0, price_increments=SortedDict({
            Decimal("0"): Decimal("1")
        }), max_drop=Decimal('0.5'), max_loss=Decimal('6000.0'), contract_size=Decimal('25.0'), position_size=Decimal('0.01'))

        got_next_buy = prices_calculator.next_buy(last_buy_price=Decimal('15959.0'), pos_vol=Decimal('0.11'), pos_price=Decimal('16350.0'), hedge_vol=Decimal('0.10'), hedge_price=Decimal('16053.0'))

        self.assertEqual(Decimal("44.76"), got_next_buy)
