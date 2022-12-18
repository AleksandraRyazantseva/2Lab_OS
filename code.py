import time
from itertools import product
from hashlib import sha256 as hash_
import threading

def check_onethread(name):
    start_time = time.time()
    for i in product("abcdefghijklmnopqrstuvwxyz", repeat=5):
        if hash_("".join(i).encode("utf-8")).hexdigest() == name:
            print("".join(i), (time.time() - start_time))
            break

print("В каком режиме работать?")
print("Одним потоком или многопотоком? (1 - однопоточно; 0 - многопоточно) > ")
a=int(input())
if (a == 1):
    print("Ввод одной строки или проверка имеющихся? (1 - ввод; 0 - проверка имеющихся) > ")
    vvod=int(input())
first_hash = '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad',\
                 '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b',\
                 '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f'

if (a == 1) and (vvod==0):
    timee = time.time()
    for j in range(3):
        check_onethread(first_hash[j])
    print(time.time() - timee)
elif (a == 1) and (vvod==1):
    print("Введите строку на проверку > ")
    password=input()
    check_onethread(password)
elif (a == 0) :
    print("Алфавит №1 - abcdefghijklmnopqrstuvwxyz")
    print("Алфавит №2 - zyxwvutsrqponmlkjihgfedcba")
    start_time = time.time()
    void_list = []
    def sha(thread, alfavit):
        y = int(0)
        for i in product(alfavit, repeat=5):
            if y == 2:
                print("Дешифровка произведена")
                break
            else:
                x = hash_("".join(i).encode("utf-8")).hexdigest()
                if x == first_hash[0] or x == first_hash[1] or x == first_hash[2]:
                    if x not in void_list:
                        print("".join(i), (time.time() - start_time), "   Найден алфавитом №", thread)
                        y += 1
                        void_list.append(x)

thr1 = threading.Thread(target = sha, args=(1,"abcdefghijklmnopqrstuvwxyz")).start()
thr2 = threading.Thread(target = sha, args=(2,"zyxwvutsrqponmlkjihgfedcba")).start()
