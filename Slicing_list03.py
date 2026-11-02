def main(royxat):
    """
    Ro'yxat berilgan. Uni o'zining teskari tartibdagi nusxasi bilan birlashtirib qaytaring.
    Argumentlar:
        royxat(list): ro'yxat
    Qaytaradi:
        list: natija ro'yxati
    """
    return royxat[::]+royxat[-1::-1]
print(main([26, 178, 74]))
