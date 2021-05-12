day_camping = int(input())  # дни на кампания
confectioner = int(input())  # сладкари
cakes_count = int(input())  # торти
waffles_count = int(input())  # гофрети
pancakes_count = int(input())  # палачинки

cakes_price = 45
waffles_price = 5.80
pancakes_price = 3.20

dayly_total = (cakes_price*cakes_count + waffles_price*waffles_count + pancakes_price*pancakes_count) * confectioner

total = dayly_total * day_camping
profit = total - (total /8)
print(profit)