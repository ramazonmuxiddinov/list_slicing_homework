def main(royxat):
    """
    Sonlar ro'yxati berilgan. Juft indekslardagi elementlar yig'indisidan toq indekslardagi elementlar yig'indisini ayirib qaytaring.
    Argumentlar:
        royxat(list): sonlar
    Qaytaradi:
        int: natija
    """
    return sum(royxat[::2])-sum(royxat[1::2])
print(main([8000, 12000, 10000, 9500, 11000, 7000, 13000]))
print(main([1, 2, 3, 4]))
