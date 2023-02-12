class Sobaka:
    count_sobak = 0
    def __init__(self):
        #count_sobak += 1
        self.klichka = ""
        self.poroda = ""
        self.kol_vo_nog = 0
    def printInfo(self):
        print(self.klichka)


listik = list()
for i in range(50):
    bobik = Sobaka()
    listik.append(bobik)