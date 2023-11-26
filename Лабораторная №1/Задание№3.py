list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

numbers_of_players = len(list_players)
player_in_the_middle = numbers_of_players // 2
list_of_first_team = list_players[0:player_in_the_middle]
list_of_second_team = list_players[player_in_the_middle:]

print(list_of_first_team)
print(list_of_second_team)
