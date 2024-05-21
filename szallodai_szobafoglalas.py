from datetime import datetime
import winsound

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 13000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 18000)
 

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

# Foglalások Kezelése

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)
    
    def foglalas_hozzaad(self, szobaszam, datum):
        for foglalas_hozzaad in self.foglalasok:
            if foglalas_hozzaad.szoba.szobaszam == szobaszam and foglalas_hozzaad.datum == datum:
                print("\nA szoba már foglalt ezen a napon. \nVálasszon másik szobát vagy másik dátumot!")
                return
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append(Foglalas(szoba, datum))
                print("Sikeres foglalás!")
                return szoba.ar
        print("\nA megadott szobaszám nem létezik a szállodában.")

    def lemondas(self, szobaszam, datum):
        for foglalas_hozzaad in self.foglalasok:
            if foglalas_hozzaad.szoba.szobaszam == szobaszam and foglalas_hozzaad.datum == datum:
                self.foglalasok.remove(foglalas_hozzaad)
                return True
        return False
    
    def foglalas_listazasa(self):
        for foglalas_hozzaad in self.foglalasok:
            print(f"Szoba: {foglalas_hozzaad.szoba.szobaszam}, Időpont: {foglalas_hozzaad.datum}")

#Rendszer feltöltése adatokkal: 
#Szalloda létrehozása1
szalloda = Szalloda("Glorius Hotel Makó")

# Szobák hozzáadása
szalloda.szoba_hozzaad(EgyagyasSzoba("101"))
szalloda.szoba_hozzaad(EgyagyasSzoba("102"))
szalloda.szoba_hozzaad(KetagyasSzoba("201"))

# Foglalások hozzáadása
szalloda.foglalas_hozzaad("101", datetime(2024, 6, 7))
szalloda.foglalas_hozzaad("102", datetime(2024, 8, 2))
szalloda.foglalas_hozzaad("201", datetime(2024, 6, 1))
szalloda.foglalas_hozzaad("101", datetime(2024, 7, 15))
szalloda.foglalas_hozzaad("102", datetime(2024, 8, 8))

# Felhasználói interfész
while True:

    print("\nKérem válasszon az alábbi menüpontokból:")
    print("1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Szobák listázása")
    print("5. Kilépés")
    case = input("Kérem adja meg a kiválasztott menüpont számát: ")

    if case == "1":
        szobaszam = input("\nAdja meg a foglalandó szoba számát: ")
        datum = input("Add meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("\nHibás dátum! A foglalás csak jövőbeni időpontra lehetséges.")
            else:
                ar = szalloda.foglalas_hozzaad(szobaszam, datum)
                if ar:
                    print(f"A foglalás sikeres! Az ár: {ar} Ft")
                else:
                    print("\nHibás szobaszám!")
        except ValueError:
            print("\nHibás dátum formátum!")
    elif case == "2":
        szobaszam = input("\nAdja meg a lemondandó foglalás szoba számát: ")
        datum = input("Adja meg a lemondandó foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            siker = szalloda.lemondas(szobaszam, datum)
            if siker:
                print("\nA foglalás sikeresen lemondva.")
            else:
                print("\nNincs ilyen foglalás.")
        except ValueError:
            print("\nHibás dátum formátum!")
    elif case == "3":
        szalloda.foglalas_listazasa()
    elif case == "4":
            print("Szobák száma:")
            print(len(szalloda.szobak))
            print("Egyágyas szobák:")
            for szoba in szalloda.szobak:
                if isinstance(szoba, EgyagyasSzoba):
                    print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar} Ft")
            print("\nKétágyas szobák:")
            for szoba in szalloda.szobak:
                if isinstance(szoba, KetagyasSzoba):
                    print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar} Ft")
    elif case == "5":
        print("Viszontlátásra!")
        break
    else:
        print("\nHibás választás!")