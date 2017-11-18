# Преобразовать IP-адрес (переменная IP) в двоичный формат и вывести вывод
# столбцами на стандартный поток вывода, таким образом:
# первой строкой должны идти десятичные значения байтов
# второй строкой двоичные значения
# Вывод должен быть упорядочен также, как в примере:
# столбцами
# ширина столбца 10 символов
# Пример вывода:
# 10       1        1        1
# 00001010 00000001 00000001 00000001

IP = '10.1.1.1'
print(type(IP))
list_IP = IP.split(".")                       # преобразование в список
list_bin_IP = []                              # создание пустого списка    

element_bin_IP = (bin(int(list_IP[0], 10)))   
"""
a=(list_mac[0])          # 
a=int(a, 16)             # преобразование строкового элемента списка в шестнацатиричное число 16 - префикс
a=int(list_mac[0], 16)   # преобразование строкового элемента списка в шестнацатиричное число 16 - префикс
print(bin(a))            # преобразование в бинарное число 

"""
list_bin_IP.append (element_bin_IP[2::])     # добавление элемента в бинарный список и удаление 2-х первых символов
element_bin_IP = (bin(int(list_IP[1], 10))) 
list_bin_IP.append (element_bin_IP[2::])
element_bin_IP = (bin(int(list_IP[2], 10)))  
list_bin_IP.append (element_bin_IP[2::])
element_bin_IP = (bin(int(list_IP[3], 10)))
list_bin_IP.append (element_bin_IP[2::])


print("{:10} {:10}  {:10}  {:10}".format(list_IP[0], list_IP[1], list_IP[2], list_IP[3]))
print("{:010} {:010}  {:010}  {:010}".format(int(list_bin_IP[0]), int(list_bin_IP[1]), int(list_bin_IP[2]), int(list_bin_IP[3])))

