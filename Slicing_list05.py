def main(royxat, n, k):
    """
    Ro'yxat, n va k berilgan. n-indeksdan k-indeksgacha (k kirmaydi) bo'lgan elementlarni qaytaring.
    Argumentlar:
        royxat(list): ro'yxat
        n(int): boshlang'ich indeks
        k(int): oxirgi indeks
    Qaytaradi:
        list: natija ro'yxati
    """
    return royxat[n:k]
print(main([8000, 12000, 10000, 9500, 11000, 7000, 13000],2,5))
