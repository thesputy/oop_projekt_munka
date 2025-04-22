# megjelenites.py

try:
    from tabulate import tabulate
    TABULATE_AVAILABLE = True
except ImportError:
    TABULATE_AVAILABLE = False

def megjelenit_adatokat(objektum_lista, fejlec=None):
    if not objektum_lista:
        print("Nincs megjeleníthető adat.")
        return

    # Ha nincs megadott fejléc, használjuk az objektum __dict__ kulcsait
    if fejlec is None:
        fejlec = list(vars(objektum_lista[0]).keys())

    # Adatok kigyűjtése
    adatok = []
    for obj in objektum_lista:
        sor = []
        for kulcs in fejlec:
            ertek = getattr(obj, kulcs, "")
            if isinstance(ertek, list):
                ertek = ", ".join(map(str, ertek))
            sor.append(ertek)
        adatok.append(sor)

    # Megjelenítés
    if TABULATE_AVAILABLE:
        print(tabulate(adatok, headers=fejlec, tablefmt="grid"))
    else:
        print("⚠️ A 'tabulate' modul nincs telepítve. Használd a 'pip install tabulate' parancsot a szebb táblázatokhoz.\n")
        for sor in adatok:
            print(" | ".join(str(x) for x in sor))
