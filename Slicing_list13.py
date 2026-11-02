def main(qadamlar):
    """
    Allamurodning bir haftalik qadamlari ro'yxati berilgan (dushanbadan yakshanbagacha). Ish kunlari (dastlabki 5 kun) va dam olish kunlari (oxirgi 2 kun) qadamlari yig'indisini [ish_kunlari, dam_olish] ro'yxati ko'rinishida qaytaring. Kesish va sum() dan foydalaning.
    Argumentlar:
        qadamlar(list): qadamlar
    Qaytaradi:
        list: natija ro'yxati
    """
    return [ sum(qadamlar[:5]),sum(qadamlar[5::])]
print(main([8000, 12000, 10000, 9500, 11000, 7000, 13000]))
