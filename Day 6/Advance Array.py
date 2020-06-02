def buy_and_sell_stock_once(prices):
    profit=0
    for p,i in enumerate(prices):
        if p!=len(prices)-1:
            profit=max(profit,(max(prices[p+1:])-i))

    print("Maximum Profit= ",profit)
buy_and_sell_stock_once([310,315,275,295,260,270,290,230,255,250])
