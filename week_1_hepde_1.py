"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
****Sum of Digits / Digital Root****

Given `n`, take the sum of the digits of `n`. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

## **Examples**

```
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
```

*TKM:* 

********Sifrleriň jemi:******** 

n san berilen, n sanyň sifrleriniň jemini tapmaly. Eger şol jemiň bahasy ýeke sifrden köp bolsa onda only ýeke sifre gelýänçä gaýtalamaly. Netijede otrisatel bolmadyk bitin san alynmaly 

**Mysal üçin,** 

```
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
```

- Solution/ Çözülişi:
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'"""""
def digit_sum(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
