# Дополнить скрипт: 5_1_a.py
# Если адрес был введен неправильно, запросить адрес снова.

"""
 1 введнеие данных
 2 обработка данных
   - проверка корректности введения  IP-адреса
   - получение 1 байта (октека IP-адреса) в десятичном формате
   - определение принадлежности IP-адреса к классу
"""

ip_error = True
while ip_error:
    IP = input('INPUT IP -address (10.0.1.1) ')
        #     Обработка данных
    
        #     - получение (октека IP-адреса) в десятичном формате
    
    list_IP = IP.split(".")                        # преобразование строки к списку по разделителю
    print ('list_IP', list_IP)                     # list_IP ['10', '0', '1', '1']
    
        #     Проверка коректности адреса IP-адреса (адрес состоит из 4 элементов) 
    
    if len(list_IP) !=4:                           # равна ли длина списка 4 элемнтам 
        print('Incorrect IPv4 address (not 4 elemants)')
        ip_error = True                                    
        continue                                   # возврат в начало цикла
        #     Проверка коректности адреса IP-адреса (что он состоит из чисел) 
    
    try:
       CLASS_IP_A = int(list_IP[0])                # получение первого октека IP в цисловом фомате
    #   print ('CLASS_IP_A',type(CLASS_IP_A),CLASS_IP_A)    # CLASS_IP <class 'int'> 10
       CLASS_IP_B = int(list_IP[1])
    #   print ('CLASS_IP_B',type(CLASS_IP_B),CLASS_IP_B)    # CLASS_IP <class 'int'> 10
       CLASS_IP_C = int(list_IP[2]) 
    #   print ('CLASS_IP_C',type(CLASS_IP_C),CLASS_IP_C)    # CLASS_IP <class 'int'> 10
       CLASS_IP_D = int(list_IP[3])
    #   print ('CLASS_IP_D',type(CLASS_IP_D),CLASS_IP_D)    # CLASS_IP <class 'int'> 10
    except (ValueError):
        print('Incorrect IPv4 address (not digit)')
        ip_error = True 
        continue
    finally:
        pass
    
        #     Проверка коректности адреса IP-адреса (каждое число в диапазоне от 0 до 255)
    
    if ((CLASS_IP_A >= 0) and (CLASS_IP_A <= 255) and
        (CLASS_IP_B >= 0) and (CLASS_IP_B <= 255) and 
        (CLASS_IP_C >= 0) and (CLASS_IP_C <= 255) and
        (CLASS_IP_D >= 0) and (CLASS_IP_D <= 255)):
        pass
    else: 
        print('Incorrect IPv4 address (out of range digit)')
        ip_error = True 
        continue
    
        #     - определение принадлежности IP-адреса к классу
    
    if (CLASS_IP_A > 0) and (CLASS_IP_A <= 223) :        
        print ('unicast')
        ip_error = False
    elif (CLASS_IP_A > 223) and (CLASS_IP_A <= 239):
        print ('multicast')
        ip_error = False
    elif (CLASS_IP_A == 255) and (CLASS_IP_B == 255) and (CLASS_IP_C == 255) and (CLASS_IP_D == 255):
        print ('local broadcast')
        ip_error = False
    elif (CLASS_IP_A == 0) and (CLASS_IP_B == 0) and (CLASS_IP_C == 0) and (CLASS_IP_D == 0):
        print ('unassigned')
        ip_error = False
    else: 
        print ('unused')
        ip_error = False
    
    