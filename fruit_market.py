strawberries_price = float(input())
banana_count = float(input())
orange_count = float(input())
raspberries_count = float(input())
strawberries_count = float(input())

raspberries_price = strawberries_price / 2
orange_price = raspberries_price * 0.6
banana_price = 0.2 * raspberries_price

total_price = banana_price * banana_count + raspberries_price * raspberries_count + strawberries_price * strawberries_count + orange_price * orange_count
print(total_price)
