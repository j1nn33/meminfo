# Преобразовать MAC-адрес в двоичную строку (без двоеточий).



MAC = 'AAAA:BBBB:CCCC'
list_mac = MAC.split(":") # преобразование в список

"""
a=(list_mac[0])          # 
a=int(a, 16)             # преобразование строкового элемента списка в шестнацатиричное число 16 - префикс
a=int(list_mac[0], 16)   # преобразование строкового элемента списка в шестнацатиричное число 16 - префикс
print(bin(a))            # преобразование в бинарное число 
"""

print (bin(int(list_mac[0], 16)))
print (bin(int(list_mac[1], 16)))
print (bin(int(list_mac[2], 16)))
