import math
from decimal import Decimal
from sortedcontainers import SortedDict

from vnpy_ctastrategy.strategies.tbradlo.base_prices_calculator import BasePricesCalculator


class MarginPricesCalculator(BasePricesCalculator):

    max_drop: Decimal
    max_loss: Decimal
    contract_size: Decimal
    position_size: Decimal

    def __init__(self, buy_step: Decimal, sell_step: Decimal, price_increments: SortedDict[Decimal, Decimal],
                 max_drop: Decimal, max_loss: Decimal, contract_size: Decimal, position_size: Decimal):
        super().__init__(buy_step, sell_step, price_increments)
        self.max_drop = max_drop
        self.max_loss = max_loss
        self.contract_size = contract_size
        self.position_size = position_size

    def next_buy(self, last_buy_price: Decimal, pos_vol: Decimal, pos_price: Decimal, hedge_vol: Decimal, hedge_price: Decimal, total_swap: Decimal):
        min_price = last_buy_price * self.max_drop
        pos_profit_at_min_price = self.value_at_price(pos_vol, pos_price, min_price)
        hedge_pos_profit_at_min_price = Decimal('-1') * self.value_at_price(hedge_vol, hedge_price, min_price)
        value_at_min_price = pos_profit_at_min_price + hedge_pos_profit_at_min_price
        #
        #
        # absolute_step_no, start_price = self.absolute_step_no(last_buy_price)
        #
        # lower_price_power = round(absolute_step_no)-1
        #
        # precise_lower_buy_price = start_price * self.buy_step ** lower_price_power

        return value_at_min_price, min_price

    def value_at_price(self, pos_vol: Decimal, pos_price: Decimal, min_price: Decimal):
        return pos_vol * self.contract_size * (min_price - pos_price)

    def absolute_step_no(self, buy_price):
        start_price = next(iter(self.price_increments.values()))
        absolute_step_no = math.log(buy_price / start_price, self.buy_step)
        return absolute_step_no, start_price

    def next_buys(self, last_buy_price: Decimal, count: int):
        got_next_buys = []
        for i in range(count):
            last_buy_price = self.next_buy(last_buy_price)
            got_next_buys.append(last_buy_price)
        return got_next_buys

    def sell_prices(self, last_buy_price: Decimal, count: int):
        pass

    def higher_buy_price(self, last_buy_price: Decimal):
        pass