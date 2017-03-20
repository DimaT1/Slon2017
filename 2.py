s = input()
for i in ['ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'Ё', 'У', 'Е', 'Ы', 'А', 'О', 'Э', 'Я', 'И', 'Ю']:
    s = s.replace(i, i + 'с' + i.lower())
s = s.replace('р', 'л')
s = s.replace('Р', 'Л')
print(s)
