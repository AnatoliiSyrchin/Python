tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

new_list = ((tutors[i], klasses[i]) if i < len(klasses) else (tutors[i], None) for i in range(len(tutors)))

print(type(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
