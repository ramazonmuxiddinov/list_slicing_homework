def main(royxat, n):
    """
    Ro'yxat va n berilgan. Dastlabki n ta elementdan tashqari hammasini qaytaring.
    Argumentlar:
        royxat(list): ro'yxat
        n(int): tashlab ketiladigan elementlar soni
    Qaytaradi:
        list: natija ro'yxati
    """
    return royxat[n::]
print(main(["Python", "Matematika", "Ingliz tili", "Fizika"],2))
