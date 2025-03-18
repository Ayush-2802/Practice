def maxProfit(prices):
    n = len(prices)
    p = 0
    m = prices[0]
    for i in range(1,n):
        p = max(p,prices[i]-m)
        m = min(m,prices[i])
    return p