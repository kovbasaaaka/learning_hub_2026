number = int(input())
first_number = number // 1000
second_number = (number % 1000) // 100
third_number = (number % 100) // 10
fourth_number = number % 10
print(f"Цифра в позиции тысяч равна {first_number}\nЦифра в позиции сотен равна {second_number}\nЦифра в позиции десятков равна {third_number}\nЦифра в позиции единиц равна {fourth_number}")
