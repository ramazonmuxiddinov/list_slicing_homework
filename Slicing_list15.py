def main(royxat):
    """
    Juft uzunlikdagi ro'yxat berilgan. Uning ikki yarmini o'rnini almashtirib qaytaring. len() va kesishdan foydalaning.
    Argumentlar:
        royxat(list): ro'yxat
    Qaytaradi:
        list: natija ro'yxati
    """
    x=len(royxat)//2
    return royxat[x:]+royxat[:x]
print(main(["Python", "Matematika", "Ingliz tili", "Fizika"]))
