from Auto import Auto

class Teherauto(Auto):
    def __init__(self, id, rendszam, tipus, berletidij, lefoglalt_napok):
        super().__init__(id, rendszam, tipus, berletidij)
        self.lefoglalt_napok = lefoglalt_napok
        self.elerhetoseg = True

    def rent(self, nap):
        if nap not in self.lefoglalt_napok:
            self.lefoglalt_napok.append(nap)
            print(f"Teherautó lefoglalva a(z) {nap}. napra.")
        else:
            print("Ez a nap már foglalt.")

    def unrent(self, nap):
        if nap in self.lefoglalt_napok:
            self.lefoglalt_napok.remove(nap)
            print(f"Foglalás törölve a(z) {nap}. napra.")
        else:
            print("Ez a nap nincs lefoglalva.")