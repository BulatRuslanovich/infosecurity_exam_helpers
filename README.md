# небольшой тутор

## 1. *find_divisors.py* нужен для вычесления простых делителей в задании rsa, можно юзать и сайт, так что не мастхев
```
Enter number n: 143
The number 143 factors as prime factors: p = 11, q = 13
```

## 2. *solver.py* скрипт покруче, он решает такое уравнение (x^y)mod(z) где x, y, z вводим ручками, нужно как в задачках rsa так и Протоколе Диффи-Хеллмана (как выяснислось, в питоне есть готовая штука, pow(base, exp, mod), ох уж этот питон с готовыми решениями на все случаи жизни)

```
Welcome to the (x^y) mod z computation program!

Enter x: 234
Enter y: 233
Enter z: 546

Result: (234^233) % 546 = 390
```

## 3. *vijener.py* скрипт для расшифровки ключа в задачах с Шифром Виженера, можно и ручками, но так круче и быстрее

![image](https://github.com/user-attachments/assets/00a6b7e3-b1a0-4282-bab2-a6048bae8555)

```
Enter encripted text: п д б й ш е с е ч м а д с д
Enter orginal text: аутентификация
Result: проектирование
```

надеюсь, питон у вас будет
