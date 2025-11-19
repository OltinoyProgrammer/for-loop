# mevalar = ["olma", "banan", "olcha", "uzum", "nok", "olxo'ri"  ]
# for meva in mevalar:
#     print(f"Men {meva}ni yaxshi ko'raman")






# 1-masala
# for i in range(1, 11):
#     print("i")

# 2-masala
# ismlar = ["Ali", "Vali", "Hasan", "Malika", "Zuhra"]
# for ism in ismlar:
#     print(f"Salom, {ism}! ")

# 3-masala
# print("1 dan 100 gacha juft sonlar")
# for son in range(1, 101, 2):

# 4-masala
# son = 0
# for son1 in range(1, 51):
#     son = son + son1
#     print(son)


# 5-masala
# matn = input("Foydalanuvchi matn kiriting: ")
# uzunlik = 0
# for belgi in matn:
#     uzunlik = uzunlik + 1
# print("Matn uzunligi:", uzunlik , "belgi")


# 6-masala
# print("\n1 dan 50 gacha 3 ga bolinadigan sonlar: ")
# sanoq = 0
# for son in range(1, 51):
#     if son % 3 == 0:
#         print(son)
#         sanoq = sanoq + 1
# print("Jami:", sanoq, "ta son")


# 7-masala
# matn = input("\nMatn kiriting: ")
# unlilar = ["aeiouaеёиоуыэюя"]
# sanoq = 0
# for belgi in matn.lower():
#     if belgi in unlilar:
#         sanoq = sanoq + 1
#         print("Jami unli harflar:", sanoq, "ta")


# 8-masala
# sonlar = [23, 67, 12, 89, 45, 34, 91, 56, 78]
# eng_katta = sonlar[0]
# for son in sonlar:
#     if son > eng_katta:
#         eng_katta = son
#         print(f"Yangi eng katta son: {eng_katta}")
# print(f"Listdagi eng katta son: {eng_katta}")
#
# son = int(input("\nSon kiriting (faktorial):"))

# 9-masala
# son = int(input("Foydalanuvchi son kiriting: "))
# sanoq = 0
# for belgi in son:
#     if belgi in

# 10 - masala
# son = int(input("Son kiriting (faktorial):"))
# if son <0:
#     print("Manfiy sonning faktoriali aniqlanmagan!")
# else:
#     fakt = 1
#     for i in range(1, son + 1):
#         fakt = fakt * i
#         print(son, "ning faktoriali = ", fakt)

# 11-masala
# print("\nMULTIPLIKATSIYA JADVALI")
#
# for i in range(1, 11):
#     for j in range(1,11):
#         print(i * j, end="\t")
#     print()