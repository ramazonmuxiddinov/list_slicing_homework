def main(qadamlar):
    """
    Allamurodning bir haftalik qadamlari ro'yxati berilgan (dushanbadan yakshanbagacha). Dastlabki uch kunlik qadamlarni qaytaring.
    Argumentlar:
        qadamlar(list): qadamlar
    Qaytaradi:
        list: natija ro'yxati
    """
    return qadamlar[:3:1]
print(main([8000, 12000, 10000, 9500, 11000, 7000, 13000]))
