# 1-m
def kassa(narx, tolov):
    if narx < 0 or tolov < 0:
        print("Xato: manfiy qiymat kiritildi")
    elif tolov >= narx:
        print("Qaytim:", tolov - narx)
    else:
        print("Yetishmaydi:", narx - tolov)


kassa(250, 50)


# 2-m
def bmi_hisobla(boy, vazn):
    bmi = vazn / (boy * boy)
    if bmi < 18.5:
        print("ozg'inlik")
    elif 18.5 < bmi < 25:
        print("Normal")
    elif 25 < bmi < 30:
        print("Ortiqcha vazn")
    else:
        print("xato")

bmi_hisobla(1.75, 70)


# 3-m
def fasl_aniqla(oy):
    oy = oy.lower()
    if oy in ["mart", "aprel", "may"]:
        print("Bahor")
    elif oy in ["iyun", "iyul", "avgust"]:
        print("Yoz")
    elif oy in ["sentabr", "oktabr", "noyabr"]:
        print("Kuz")
    elif oy in ["dekabr", "yanvar", "fevral"]:
        print("Qish")
    else:
        print("Noto‘g‘ri oy")


oy = input("Oy: ")
fasl_aniqla(oy)



# 4-m
def parol_tekshir(parol):
    if len(parol) < 8:
        print("Parol uzunligi 8 belgidan kam")
        return

    raqam_bormi = False
    for i in parol:
        if i.isdigit():
            raqam_bormi = True
            break

    if not raqam_bormi:
        print("Parolda kamida 1 ta raqam bo‘lishi kerak")
    else:
        print("Parol qabul qilindi")

parol_tekshir("salom123")
parol_tekshir("salom")


# 5-m

def transport(masofa, transport):
    if masofa < 0:
        print("Masofa manfiy bo‘lishi mumkin emas")
        return

    if transport == "taksi":
        narx = 5000 + 2000 * masofa
    elif transport == "avtobus":
        narx = 3000 * masofa
    elif transport == "poezd":
        narx = 10000 + 1500 * masofa
    else:
        print("Noto‘g‘ri transport turi kiritildi")
        return

    print(f"Narx: {int(narx)} so‘m")


transport(10, 'taksi')

