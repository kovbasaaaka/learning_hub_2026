name_of_player = input()
total = 0
# Пока в именах нет имени Александра продолжаем вводить имена

while name_of_player != 'Александра':
  name_of_player = input()
  
# Как только дойдём до Александры, цикл завершится 

name_of_player = input() # И данный input введёт Александру

# После того, как нашли Александру, приступаем к перебору до Левона и прибавляем к счётчику 1, если это имя не Ливон.

while name_of_player != 'Левон':
  name_of_player = input()
  total += 1

print(total)
  
  
