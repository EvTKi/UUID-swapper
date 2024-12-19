import os
import uuid
import time

file = '+Герасимов 1 .txt'


def Rand_UUID_arr(n_elem):
    random_uuid = []
    for i in range(n_elem):
        random_uuid.append(uuid.uuid4())
    return random_uuid
    # print(*random_uuid)


def log(x, y):
    with open(f'log {y}.txt', 'w', encoding='UTF-8') as file:
        file.writelines(x)
        file.close()


def timer_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"Время выполнения функции: {
              end_time-start_time} секунд")
    return wrapper


print('начинаю замену UUID')
# Запишем наш файл в массив
file_inside = []
isk_uuid = []
unic_uuid = []
with open(file, 'r', encoding='utf-8') as file:
    file_inside = file.readlines()
    file.close()
# print(file_inside)
# log(file_inside, 'начальный файл')

for line in file_inside:
    # print(f'Элемент {line}')
    num_isk_simv = line.find('#_')
    if num_isk_simv != -1:
        isk_uuid.append(line[num_isk_simv+2:num_isk_simv+34])
        # print(f'D строке {line} UID={isk_uuid}. Длина ={len(isk_uuid)}')
        # Проверить первую строку, м.б. UID модели
for uids in isk_uuid:
    if uids not in unic_uuid:
        unic_uuid.append(uids)
# print(unic_uuid[0])
log(str(unic_uuid), 'UID old')
# print(f'Длина уникальных {len(unic_uuid)}')
swap_uuid = Rand_UUID_arr(len(unic_uuid))
log(str(swap_uuid), 'UID new')
end_file_name_txt = 'Конечный файл.txt'
# print(f'Длина для замены {len(swap_uuid)}')


def replace_uuid(end_file_name):
    with open(end_file_name, 'a+', encoding='UTF-8') as file:
        for line in file_inside:
            # print(f'Элемент {line}')
            num_isk_simv = line.find('#_')
            if num_isk_simv != -1:
                d = line[num_isk_simv+2:num_isk_simv+34]
                num_d = unic_uuid.index(d)
                if num_d != 0:
                    line = line.replace(d, str(swap_uuid[num_d]))
                    file.write(line)
                else:
                    file.write(line)
            else:
                file.write(line)
        # print(f'Что меняем {d} на {
        #       str(swap_uuid[num_d])}. Результат {line}')


replace_uuid(end_file_name_txt)
files_in_dir = os.listdir()
# print(files)

i = 0
while i > -1:
    try:
        os.rename(end_file_name_txt, f'Конечный файл{i}.xml') if i != 0 else os.rename(
            end_file_name_txt, 'Конечный файл.xml')
    except:
        if f'Конечный файл{i}.xml' in files_in_dir:
            i += 1
        else:
            break

print('done')
