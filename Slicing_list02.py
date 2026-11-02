def main(royxat):
    """
    Ro'yxat berilgan. Uni teskari tartibda qaytaring.
    Argumentlar:
        royxat(list): ro'yxat
    Qaytaradi:
        list: natija ro'yxati
    """
    return royxat[-1::-1]
print(main(["Python", "Matematika", "Ingliz tili", "Fizika"]))
