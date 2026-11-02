def main(royxat):
    """
    Ro'yxat berilgan. Agar u teskari tartibda ham bir xil bo'lsa True, aks holda False qaytaring.
    Argumentlar:
        royxat(list): ro'yxat
    Qaytaradi:
        bool: javob (True yoki False)
    """
    return royxat[::]==royxat[::-1]
print(main([2, 0, 0, 2]))
print(main([2, 0, 2, 6]))
