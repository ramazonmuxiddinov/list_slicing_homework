def main(daromad):
    """
    Allamurodning 6 oylik daromadi ro'yxati berilgan. Birinchi va ikkinchi yarim (3 oydan) daromadlari yig'indilari farqini (ikkinchi − birinchi) qaytaring.
    Argumentlar:
        daromad(list): 6 oylik daromad
    Qaytaradi:
        int: natija
    """
    return abs(sum(daromad[:3])-sum(daromad[3::]))
print(main([6500000, 6500000, 6800000, 7000000, 7200000, 7200000]))
