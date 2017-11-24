# Преобразовать скрипт из задания 4_1_a таким образом, чтобы сеть/маска не
# запрашивались у пользователя, а передавались как аргумент скрипту.
# Алгоритм и описание си 4_1_а
#######################################
                                            # ВВОД ДАННЫХ
from sys import argv                        # использование argv для работы с аргументами из модуля sys
IP = argv[1]                                # argv[1] - Это срез списка. 
                                            # стороне остается список с элементами: ['10.3.1.5/16'] .                                          
                                            
                                            
                                            
                                            
#IPN = input(' Ввод IP-сети в формате: 10.1.1.0/04  ')
#print ('input data')
IP =  '10.3.1.5/16'
#print(IP)
print('-----------')


                                            # РАЗБОР ДАННЫХ

IPH = IP[:-3]                               # все символы кроме последних трех
MASKH = IP[-3:]                             # 3 последних символа
print ("IP - HOST")
print (IPH)
print (MASKH)
print ("##########")

                                            # ПРЕОБРАЗОВАНИЕ АДРЕСА ХОСТА В АДРЕС СЕТИ
                                            # - получение адреса хоста в бинарном виде
                                            #Перевод адреса хоста в бинарный вид по октекам
list_IPH = IPH.split(".")                   # преобразование в список
list_bin_IPH = []                           # создание пустого списка   

"""
                                            a=(list_mac[0])          # 1 и 2 строка
                                            a=int(a, 16)             # преобразование строкового элемента списка в шестнацатиричное число 16 - префикс
                                            a=int(list_mac[0], 16)   # преобразование строкового элемента списка в шестнацатиричное число 16 - префикс тоже самое только одной строкой
                                            print(bin(a))            # преобразование в бинарное число 
"""
element_bin_IPH = (bin(int(list_IPH[0], 10))) 
# print ('int(list_IPH[0], 10))',type(element_bin_IPH), element_bin_IPH)
list_bin_IPH.append (element_bin_IPH[2::])  # добавление элемента в бинарный список  и удаление 2-х первых символов их не будет ровно 8 символов
element_bin_IPH = (bin(int(list_IPH[1], 10))) 
list_bin_IPH.append (element_bin_IPH[2::])
element_bin_IPH = (bin(int(list_IPH[2], 10)))  
list_bin_IPH.append (element_bin_IPH[2::])
element_bin_IPH = (bin(int(list_IPH[3], 10)))
list_bin_IPH.append (element_bin_IPH[2::])
                                            # - получение маски в бинарном виде и десятичном


MASK = IP[-3:]                              # 3 последних символа                                           
                                            # ОБРАБОТКА МАСКИ в бинарный вид по октекам
int_mask = int (MASK[1:])                   # удаление / у маски и преобразование его в число
#print (int_mask)
#print (type(int_mask))
bin_mask = ( '1' * int_mask + '0'*(32-int_mask))   # получения маски в бинарном виде 
#print(bin_mask)
a=one_okt_bin_mask = bin_mask[:8]
b=two_okt_bin_mask = bin_mask[8:16]
c=three_okt_bin_mask = bin_mask[16:24]
d=four_okt_bin_mask = bin_mask[24:]
                                             # получение октеков маски в десятичной системе или adm=int(a,2)
                                             # 10110110 = (1·2^7)+(0·2^6)+(1·2^5)+(1·2^4)+(0·2^3)+(1·2^2)+(1·2^1)+(0·2^0) = 128+32+16+4+2 = 182 
                                             # print (int(a[0])*2**7)
adm=one_okt_dec_mask = (int(a[0])*2**7+int(a[1])*2**6+int(a[2])*2**5+int(a[3])*2**4+int(a[4])*2**3+int(a[5])*2**2+int(a[6])*2**1+int(a[7])*2**0)
bdm=two_okt_dec_mask = (int(b[0])*2**7+int(b[1])*2**6+int(b[2])*2**5+int(b[3])*2**4+int(b[4])*2**3+int(b[5])*2**2+int(b[6])*2**1+int(b[7])*2**0)
cdm=three_okt_dec_mask = (int(c[0])*2**7+int(c[1])*2**6+int(c[2])*2**5+int(c[3])*2**4+int(c[4])*2**3+int(c[5])*2**2+int(c[6])*2**1+int(c[7])*2**0)
ddm=four_okt_dec_mask = (int(d[0])*2**7+int(d[1])*2**6+int(d[2])*2**5+int(d[3])*2**4+int(d[4])*2**3+int(d[5])*2**2+int(d[6])*2**1+int(d[7])*2**0)
                                             # тот же процесс только другим способом    
                                             # (a, b, c, d) получение маски в бинарном виде a=one_okt_dec_mask  - 1 октек маски <class 'str'>
                                             # (ah, bh, ch, dh) получение хоста в бинарном виде ah 8 символов <class 'str'> 
ah=bin(int(list_IPH[0]))[2:].zfill(8)
bh=bin(int(list_IPH[1]))[2:].zfill(8)
ch=bin(int(list_IPH[2]))[2:].zfill(8)
dh=bin(int(list_IPH[3]))[2:].zfill(8)
"""
print ('mask')
print ('a',type(a),a)
print ('b',type(b),b)
print ('c',type(c),c)
print ('d',type(d),d)
print ('IP')
print ('ah',type(ah),ah)
print ('bh',type(bh),bh)
print ('ch',type(ch),ch)
print ('dh',type(dh),dh)
"""
                                            # побитовое ставонеие элементов сторок
                                            # 11000000.10101000.00000001.00011111 (IP)
                                            # AND
                                            # 11111111.11111111.11111111.00000000 (Mask)
                                            # =
                                            # 11000000.10101000.00000001.00000000 (Адрес сети в двоичном виде)
                                            
an = (((int(a[0],2)&int(ah[0],2))*10000000)+((int(a[1],2)&int(ah[1],2))*1000000)+ 
 ((int(a[2],2)&int(ah[2],2))*100000)+((int(a[3],2)&int(ah[3],2))*10000)+ 
 ((int(a[4],2)&int(ah[4],2))*1000)+((int(a[5],2)&int(ah[5],2))*100) +
 ((int(a[6],2)&int(ah[6],2))*10)+(int(a[7],2)&int(ah[7],2)))
bn = (((int(b[0],2)&int(bh[0],2))*10000000)+((int(b[1],2)&int(bh[1],2))*1000000)+ 
 ((int(b[2],2)&int(bh[2],2))*100000)+((int(b[3],2)&int(bh[3],2))*10000)+ 
 ((int(b[4],2)&int(bh[4],2))*1000)+((int(b[5],2)&int(bh[5],2))*100) +
 ((int(b[6],2)&int(bh[6],2))*10)+(int(b[7],2)&int(bh[7],2)))
cn = (((int(c[0],2)&int(ch[0],2))*10000000)+((int(c[1],2)&int(ch[1],2))*1000000)+ 
 ((int(c[2],2)&int(ch[2],2))*100000)+((int(c[3],2)&int(ch[3],2))*10000)+ 
 ((int(c[4],2)&int(ch[4],2))*1000)+((int(c[5],2)&int(ch[5],2))*100) +
 ((int(c[6],2)&int(ch[6],2))*10)+(int(c[7],2)&int(ch[7],2)))
dn = (((int(d[0],2)&int(dh[0],2))*10000000)+((int(d[1],2)&int(dh[1],2))*1000000)+ 
 ((int(d[2],2)&int(dh[2],2))*100000)+((int(d[3],2)&int(dh[3],2))*10000)+ 
 ((int(d[4],2)&int(dh[4],2))*1000)+((int(d[5],2)&int(dh[5],2))*100) +
 ((int(d[6],2)&int(dh[6],2))*10)+(int(d[7],2)&int(dh[7],2)))

"""
print('------------')

print ('an',type(an),an)
print ('bn',type(bn),bn)
print ('cn',type(cn),cn)
print ('dn',type(dn),dn)
"""

aipn = int(str(an), 2)
bipn = int(str(bn), 2)
cipn = int(str(cn), 2)
dipn = int(str(dn), 2)





                                            # ВЫВОД ИНФОРМАЦИИ
print ("Network:")

print("{:<8} {:<8}  {:<8}  {:<8}".format(aipn, bipn, cipn, dipn))

print("{:08} {:08} {:08} {:08}".format(an, bn, cn, dn))


print ("Mask:")
print (MASK)
print("{:<8} {:<8} {:<8} {:<8}".format(one_okt_dec_mask, two_okt_dec_mask, three_okt_dec_mask, four_okt_dec_mask))
print("{:8} {:8} {:8} {:8}".format(one_okt_bin_mask, two_okt_bin_mask, three_okt_bin_mask, four_okt_bin_mask))


                                            # Network:
                                            # 10       0        1        0
                                            # 00001010 00000000 00000001 00000000
                                            # Mask:
                                            # /24
                                            # 255      255      255      0
                                            # 11111111 11111111 11111111 00000000