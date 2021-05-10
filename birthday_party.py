hall_rental = int(input())
cake = 0.20 * hall_rental
drink = cake - 0.45 * cake
animator = hall_rental / 3
total_price = (hall_rental + cake + drink + animator)
print(total_price)
