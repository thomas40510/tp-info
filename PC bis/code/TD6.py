import matplotlib.pyplot as plt
import numpy as np

L1 = [0, 1, 1, 1, 1, 0, 0,
      1, 1, 1, 1, 1, 1, 1,
      1, 0, 0, 0, 0, 1, 1,
      1, 1, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 1,
      1, 1, 0, 1, 1, 0, 1,
      1, 1, 0, 0, 0, 0, 0]


def splitlist(L, n=7):
    Ll = [[] for i in range(n)]
    i = 0
    k = 0
    while k != len(L):
        while len(Ll[i]) < 7:
            Ll[i] += [L[k]]
            k += 1
        i += 1
    return Ll


def parite(L):
    return L[:] + [sum(L) % 2]


def paritesplit(L):
    for l in L:
        l.append(sum(l) % 2)
    return L


def scytale(s, n):
    q, r = len(s) // n, len(s) % n
    nlettres = q + (1 if r != 0 else 0)

    if r != 0:
        s += ' ' * (n - r)

    L = []
    for l in range(n):
        L.append(s[l * nlettres: (l + 1) * nlettres])

    tc = ''
    for i in range(nlettres):
        for j in range(n):
            tc += L[j][i]

    return tc.strip()


def decode_scytale(mes, cle):
    q, r = len(mes) // cle, len(mes) % cle
    nlettres = q + (r != 0)

    if r != 0:
        mes += ' ' * (cle - r)
    L = []
    for i in range(cle):
        L.append([])
    for i in range(len(mes)):
        L[i % cle].append(mes[i])

    tdc = ''
    for l in L:
        for c in l:
            tdc += c

    return tdc


# mes = scytale('LOREM IPSUM DOLOR SIT AMET', 6)
# print(mes)
# print(decode_scytale(mes, 6))

def codage_cesar(mes, cle):
    message = ''
    for car in mes:
        if car == ' ':
            message += car
        else:
            message += chr((ord(car) - 65 + cle) % 26 + 65)
    return (message)


def decode_cesar(mes, cle):
    return codage_cesar(mes, -cle)


def codage_vigenere(mes, cle):
    message = ''
    long = len(cle)
    for rang in range(len(mes)):
        if mes[rang] == ' ':
            message += ' '
        else:
            message += chr((ord(mes[rang]) - 65 + ord(cle[rang % long]) - 65) % 26 + 65)
    return (message)


def decodage_vigenere(mes, cle):
    message = ''
    long = len(cle)
    for rang in range(len(mes)):
        if mes[rang] == ' ':
            message += ' '
        else:
            message += chr((ord(mes[rang]) - 65 - ord(cle[rang % long]) + 65) % 26 + 65)
    return (message)


latin = ['f', 'u', 'th', 'a', 'r', 'k', 'g', 'w', 'h', 'n', 'i', 'j', 'ï',
         'p', 'z', 's', 't', 'b', 'e', 'm', 'l', 'ng', 'd', 'o']
runes = ['\u16a0', '\u16a2', '\u16a6', '\u16a8', '\u16b1', '\u16b2',
         '\u16b7', '\u16b9', '\u16ba', '\u16be', '\u16c1', '\u16c3', '\u16c7',
         '\u16c8', '\u16c9', '\u16ca', '\u16cf', '\u16d2', '\u16d6', '\u16d7',
         '\u16da', '\u16dc', '\u16de', '\u16df']

common = ['', ' ', "'", '.', ',', ';', '?', '!', ':', '\t',
          '\n'] + list('0123456789')
latin = latin + common
runes = runes + common


def transcript(char, alpha1=runes, alpha2=latin):
    if char in alpha1:
        n = alpha1.index(char)
        c = alpha2[n]
    else:
        c = '*'
    return c


def transcript_text(mes):
    s = ''
    for c in mes:
        s += transcript(c)
    return s

msg = transcript_text('ᛗᚨᛁ.ᛏᛖᚱ\tᚱᚨᚾᚨᚨᛚᛏ\tᛒᛚᛖᛊᛊᛊ \nᛖᛊᚳᛊᚨᚳᚱ\tᛟᛞᛖᛞᚱᚢᚱ\tᛗᛖᚱᛁᛚᚾ \nᛊᛖᛖᛖᛗᛖᛖ\tᛏᚢᚳᚾᛏᛃᚨ\tᚢᛞᛖᛚᛖᛁ \nᛊᚾᚠᚷᚢᚱᛏ\tᚨᚨᛊᛖᚾᛊᚳ\tᛏᛗᛏᚢᚠ  \nᚢᚱᛞᚾᚱᛏᛏ\tᛁ,ᛖᛚᛁᛁᛊ\tᚨᛖᚨᚳᚠ  \nᚾᚨᛟᛁᛏᛊᛖ\tᛒᛖᛞᚨᛁᚱᚨ\tᛒᚲᚱᛟᛖ  \nᚲ.ᚲᛏᚾᛖ,\tᛊᛞᛊᚳᛁᚨᚱ\tᛁᛗᚳᚣᚾ')


im1 = plt.imread('Lena.png')
tab = np.shape(im1)
im2 = im1[:, :, 1]
plt.imshow(im2)
plt.show()

