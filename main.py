from berles import Berles
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from megjelenites import megjelenit_adatokat

class RentingSystem:
    def __init__(self):
        self._berles = Berles("GDE Autó bérlő")
        self._init_data()

    def _init_data(self):
        self._berles.vehicles = Szemelyauto(1, "GDE-001", "Suzuki Swift", "25 000 forint / nap", [1])
        self._berles.vehicles = Szemelyauto(2, "GDE-002", "Fiat 500", "17 500 forint / nap", [6, 7])
        self._berles.vehicles = Teherauto(3, "GDE-003", "MAN TGS", "58 400 forint / nap", [11])

    def user_interact(self):
        vehiclesdaily_seen = False
        while True:
            print("\n--- GDE Autókölcsönző ---")
            print("1. Járművek listája")
            print("2. Foglalások megtekintése")
            print("3. Autó bérlése")
            print("4. Bérlés lemondása")
            print("5. Kilépés")

            choice = input("Válasz a fenti menüpontok közül: ")

            if choice == "1":
                megjelenit_adatokat(
                    self._berles.vehicles,
                    fejlec=["id", "rendszam", "tipus", "berleti_dij"]
                )

            elif choice == "2":
                megjelenit_adatokat(
                    self._berles.vehicles,
                    fejlec=["id", "rendszam", "tipus", "lefoglalt_napok"]
                )
                vehiclesdaily_seen = True

            elif choice == "3":
                if not vehiclesdaily_seen:
                    print("Előbb nézze meg a járművek elérhetőségét a 2-es menüpontban!")
                    continue

                autoid = input("Kérem adja meg, hogy melyik autó érdekli (ID): ")
                for auto in self._berles.vehicles:
                    if str(auto.id) == autoid:
                        while True:
                            try:
                                nap = int(input("Add meg, hogy melyik napra szeretnél foglalni: "))
                                if nap not in auto.lefoglalt_napok:
                                    auto.lefoglalt_napok.append(nap)
                                    print(f"Sikeres foglalás! {auto.rendszam} le lett foglalva a(z) {nap}. napra.")
                                    break
                                else:
                                    print("Ez a nap már foglalt. Próbálj másikat.")
                            except ValueError:
                                print("Kérlek, számot adj meg.")
                        break
                else:
                    print("Nincs ilyen azonosítójú autó.")

            elif choice == "4":
                if not vehiclesdaily_seen:
                    print("Előbb nézze meg a járművek elérhetőségét a 2-es menüpontban!")
                    continue

                autoid = input("Kérem adja meg, hogy melyik autóról van szó (ID): ")
                for auto in self._berles.vehicles:
                    if str(auto.id) == autoid:
                        while True:
                            try:
                                nap = int(input("Add meg, melyik napot szeretnéd lemondani: "))
                                if nap in auto.lefoglalt_napok:
                                    auto.lefoglalt_napok.remove(nap)
                                    print(f"A(z) {nap}. napra vonatkozó foglalás törölve.")
                                    break
                                else:
                                    print("Ez a nap nincs lefoglalva ennél az autónál.")
                            except ValueError:
                                print("Kérlek, számot adj meg.")
                        break
                else:
                    print("Nincs ilyen azonosítójú autó.")

            elif choice == "5":
                print("Kilépés a rendszerből.")
                break

if __name__ == "__main__":
    renting_system = RentingSystem()
    renting_system.user_interact()