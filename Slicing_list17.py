def main(fanlar, n):
    """
    Allamurodning fanlar ro'yxati va indeks n berilgan. Kesish yordamida n-indeksdagi fanni olib tashlab, yangi ro'yxatni qaytaring.
    Argumentlar:
        fanlar(list): fanlar
        n(int): indeks
    Qaytaradi:
        list: natija ro'yxati
    """
    return fanlar[:n]+fanlar[n+1:]
print(main(["Python", "Matematika", "Ingliz tili", "Fizika"],1))
