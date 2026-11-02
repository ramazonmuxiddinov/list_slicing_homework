def main(royxat):
    """
    Ro'yxat berilgan. Boshidan boshlab har uchinchi elementni qaytaring.
    Argumentlar:
        royxat(list): ro'yxat
    Qaytaradi:
        list: natija ro'yxati
    """
    return royxat[::3]
print(main([8000, 12000, 10000, 9500, 11000, 7000, 13000]))
