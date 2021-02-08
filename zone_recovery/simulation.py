from zone import Zone


def makeDecision(prev_price, current_price, zone: Zone, state: str):

    if (prev_price > zone.up and current_price < zone.up or current_price == zone.up) and state == 'w8 4 Buy':
        return 'Open Buy', 'w8 4 Sell'

    if (prev_price < zone.down and current_price > zone.down or current_price == zone.down) and state == 'w8 4 Sell':
        return 'Open Sell', 'w8 4 Buy'

    if (prev_price < zone.above_target and current_price > zone.above_target or current_price == zone.above_target) and state == 'w8 4 Sell':
        return 'Close Buy', 'w8 4 Buy'

    if (prev_price > zone.below_target and current_price < zone.below_target or current_price == zone.below_target) and state == 'w8 4 Buy':
        return 'Close Sell', 'w8 4 Sell'

    return 'Steady', state


def simulation(df, limit=4, alpha=2, money=1000):

    state = 'w8 4 Sell'
    action = 'Open Buy'
    first_money = money

    buy_cost = 0
    sell_cost = 0

    buy_unit = 0
    sell_unit = 0

    # temp_money = 0

    first_price = df.iloc[0].Price
    prev_price = first_price
    print(action, first_price)
    zone = Zone(first_price, first_price * 0.01, first_price * 0.04)

    for i, row in df[1:].iterrows():

        current_price = row.Price
        action, state = makeDecision(prev_price, current_price, zone, state)
        if action == 'Close Buy' or action == 'Close Sell':
            zone = Zone(current_price, current_price *
                        0.01, current_price * 0.04)
        if(action != 'Steady'):
            print(action, current_price)

        prev_price = current_price