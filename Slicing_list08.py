def main(royxat, n):
    """
    Ro'yxat va n berilgan. Oxiridan boshlab n qadam bilan barcha elementlarni qaytaring.
    Argumentlar:
        royxat(list): ro'yxat
        n(int): qadam
    Qaytaradi:
        list: natija ro'yxati
    """
    return royxat[-1::-n]
print(main([8000, 12000, 10000, 9500, 11000, 7000, 13000],2))
print(main([8000, 12000, 10000, 9500, 11000, 7000, 13000],3))

