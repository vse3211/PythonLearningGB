def out_data(_f_name, _s_name, _b_year, _city, _email, _phone):
    print(f'{_f_name} {_s_name} {_b_year} {_city} {_email} {_phone}')


f_name = input('Введите имя: ')
s_name = input('Введите фамилию: ')
b_year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')
out_data(f_name, s_name, b_year, city, email, phone)
