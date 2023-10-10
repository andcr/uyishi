class SotuvMashinasi:
    def __init__(self):
        self.ichimliklar = {}

    def addBeverage(self, ichimlik_nomi, sotish_narxi):
        self.ichimliklar[ichimlik_nomi] = sotish_narxi

    def getPrice(self, ichimlik_nomi):
        if ichimlik_nomi in self.ichimliklar:
            return self.ichimliklar[ichimlik_nomi]
        else:
            return -1.0

sotuv_mashinasi = SotuvMashinasi()

sotuv_mashinasi.addBeverage("Coca Cola", 3200)
sotuv_mashinasi.addBeverage("Suv", 1000)
sotuv_mashinasi.addBeverage("Pepsi", 2500)
narxi = sotuv_mashinasi.getPrice("Coca Cola")
if narxi != -1.0:
    print(f"Coca Cola narxi: {narxi}")
else:
    print("Bu ichimlik mavjud emas")

narxi = sotuv_mashinasi.getPrice("Fanta")
if narxi != -1.0:
    print(f"Fanta narxi: {narxi}")
else:
    print("Bu ichimlik mavjud emas")
