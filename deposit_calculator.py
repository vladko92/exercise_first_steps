deposit_sum = float(input())
duration = int(input())
year_perc = float(input())
interest = (deposit_sum * (year_perc/100))
interest_per_mounth = interest / 12
sum = deposit_sum + duration * interest_per_mounth
print(sum)