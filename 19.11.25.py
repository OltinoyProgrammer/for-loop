# 8-masala
sonlar = [23, 67, 12, 89, 45, 34, 91, 56, 78]
eng_katta = sonlar[0]
for son in sonlar:
    if son > eng_katta:
        eng_katta = son
        print(f"Yangi eng katta son: {eng_katta}")
print(f"Listdagi eng katta son: {eng_katta}")

son = int(input("\nSon kiriting (faktorial):"))
