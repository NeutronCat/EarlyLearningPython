# carly's clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
for price in prices:
  total_price += price
average_price = total_price / len(prices)
new_prices = [price - 5 for price in prices]
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
average_daily_revenue = total_revenue / 7
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]


print(prices)
print(total_price)
print("Average Haircut Price: "+str(average_price))
print(new_prices)
print("Total Revenue: "+str(total_revenue))
print(average_daily_revenue)
print(cuts_under_30)

