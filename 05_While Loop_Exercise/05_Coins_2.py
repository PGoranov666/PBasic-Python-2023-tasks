change_amount = float(input())
change_amount *= 100  # Преобразуваме в стотинки
coins = [200, 100, 50, 20, 10, 5, 2, 1]  # Монети в стотинки
num_coins = 0
coin_index = 0

while change_amount > 0 and coin_index < len(coins):
    coin = coins[coin_index]
    num_coin = change_amount // coin
    num_coins += num_coin
    change_amount -= num_coin * coin
    coin_index += 1

print(int(num_coins))
