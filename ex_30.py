#30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
file_1 = open('users.txt', 'r', encoding='utf-8')
file_2 = open('hobby.txt', 'r', encoding='utf-8')
dictionary = dict(zip(file_1, file_2))
file_res = open('users_hobby.txt', 'w', encoding='utf-8')
for key, val in dictionary.items():
     file_res.write('{}: {}'.format(key, val))
file_1.close()
file_2.close()
file_res.close()


