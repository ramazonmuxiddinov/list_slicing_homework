def main(numbers):
    """
    numbers ro'yxati berilgan. Juft indeksdagi (0, 2, 4, ...) elementlarni qaytaring.
    Argumentlar:
        numbers(list): sonlar
    Qaytaradi:
        list: natija ro'yxati
    """
    return numbers[::2]
print(main([8000, 12000, 10000, 9500, 11000, 7000, 13000]))
