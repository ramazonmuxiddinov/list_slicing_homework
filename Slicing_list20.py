def main(qadamlar, n):
    """
    Allamurodning bir haftalik qadamlari ro'yxati berilgan (dushanbadan yakshanbagacha). Son n berilgan. Oxirgi n kunlik qadamlar yig'indisi dastlabki n kunlik qadamlar yig'indisidan qanchaga ko'p (yoki kam) ekanini qaytaring.
    Argumentlar:
        qadamlar(list): qadamlar
        n(int): kunlar soni
    Qaytaradi:
        int: natija
    """
    return sum(qadamlar[-n:])-sum(qadamlar[:n])
print(main([8000, 12000, 10000, 9500, 11000, 7000, 13000],3))
print(main([8000, 12000, 10000, 9500, 11000, 7000, 13000],2))


