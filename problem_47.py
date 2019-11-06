"""
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.
For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
a = [9, 11, 8, 5, 7, 10]

def max_profit_v1(array):
    max_diff = float("-inf")
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[j] > array[i] and array[j] - array[i] > max_diff:
                max_diff = array[j] - array[i]
    
    return max_diff

def max_profit_v2(price):
    minprice =  float("inf") 
    maxprice = 0
    for i in range(len(price)):
        if price[i] < minprice:
            minprice = price[i]
        
        elif price[i] - minprice > maxprice:
            maxprice =  price[i] - minprice

    return maxprice


print(max_profit_v1(a))
print(max_profit_v2(a))
