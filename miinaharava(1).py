"""
Pääohjelma, tämän ajamalla voit tallata miinoja!
"""
from sys import exit
import os
import miinaharava_peli
import haravasto

vaikeustaso = {
    "helppo": (9, 9, 10),
    "keskivaikea": (15, 15, 40),
    "vaikea": (30, 30, 100),
    "custom": (0, 0, 0)
}
    
def main():
    """
    main funktio joka pyörittelee funktioita
    """
    while True:
        try:
            print("\n Tervetuloa tallaamaan miinoja!")
            kayttajanimi = kysy_nimi()
            tyhjenna()
            print("\n 1. Pelaa")
            print(" 2. Ennätykset")
            print(" 3. Sulje")
            valinta = input("\n Valitse antamalla numero: ")

            if valinta == "1":
                tyhjenna()
                valittu_taso = kysy_vaikeustaso()
                tyhjenna()
                polku = r"spritet"
                haravasto.lataa_kuvat(polku)
                miinaharava_peli.alusta()  # Alusta pelitilanne
                miinaharava_peli.luo_kentta(valittu_taso, kayttajanimi)
                miinaharava_peli.pelaa()
            elif valinta == "2":
                tyhjenna()
                nayta_tilastot()
            elif valinta == "3":
                tyhjenna()
                exit()
            else:
                tyhjenna()
                print("\n ET ANTANUT OIKEAA NUMEROA!")
                input("\n Paina enteriä jatkaaksesi ")
                tyhjenna()
        except KeyboardInterrupt:
            continue
             
def kysy_vaikeustaso():
    """
    Funktio pyytää vaikeutason.
    """
    while True:
        try:
            print("\n Valitse vaikeustaso")
            print("\n 1. Helppo")
            print(" 2. Keskivaikea")
            print(" 3. Vaikea")
            print(" 4. Muu")
            taso = input("\n Valitse antamalla numero: ")

            if taso == "1":
                return vaikeustaso["helppo"]
            if taso == "2":
                return vaikeustaso["keskivaikea"]
            if taso == "3":
                return vaikeustaso["vaikea"]
            if taso == "4":
                pyyda_taso()
                return vaikeustaso["custom"]
            else:
                tyhjenna()
                print("\n ET ANTANUT OIKEAA NUMEROA!")
                input("\n Paina enteriä jatkaaksesi ")
                tyhjenna()
        except KeyboardInterrupt:
            continue
            
def pyyda_taso():
    """
    Pyytää ja asettaa käyttäjan antaman oman vaikeustason.
    """

    def tarkista_syote(syote, virheilmoitus):
        while True:
            try:
                arvo = int(input(syote))
                if arvo <= 0:
                    raise ValueError("Liian pieni arvo.")
                return arvo
            except ValueError:
                tyhjenna()
                print("\n Virheellinen syöte:", virheilmoitus)

    leveys = tarkista_syote(
    "\n Anna kentän leveys: ",
    "Anna kokonaisluku, joka on suurempi kuin 0."
        ) 
    korkeus = tarkista_syote(
        "\n Anna kentän korkeus: ", 
        "Anna kokonaisluku, joka on suurempi kuin 0."
        )
    miinat = tarkista_syote(
        "\n Anna miinojen määrä: ", 
        "Anna kokonaisluku, joka on suurempi kuin 1."
        )

    vaikeustaso["custom"] = (korkeus, leveys, miinat)

def nayta_tilastot():
    """
    Lataa ennätykset csv tiedostosta ja tulostaa ne näytölle.
    """
    try:
        with open("tilastot.csv") as tilastot:
            for rivi in tilastot.readlines():
                tiedot = rivi.rstrip("\n").split(",")
                m, sec = divmod(int(tiedot[2]), 60)
                print(
                f"\n Päivämäärä: {tiedot[1]}, aika: {m} min {sec} sek, nimi: {tiedot[0]}"
                )
                print(
                f" Lopputulos: {tiedot[4]}, siirrot: {tiedot[3]}, "
                f"kentän koko: {tiedot[6]}x{tiedot[5]}, miinat: {tiedot[7]}"
            )


    except FileNotFoundError:
        print("\n Aikaisempia ennätyksiä ei löytynyt.")
        input("\n Paina enteriä jatkaaksesi ")
    except IOError:
        print("\n Tiedosto vioittunut.")
        print(" Tilastoja ei voitu ladata.")
        input("\n Paina enteriä jatkaaksesi ")

    input("\n Paina enteriä palataksesi valikkoon ")
    tyhjenna()
    
def kysy_nimi():
    """
    kysyy käyttäjänimen
    """
    while True:
        try:
            print("\n Jättämällä nimikentän tyhjäksi voit pelata vieraana.")
            nimi = input("\n Anna käyttäjänimi: ")
            return nimi if nimi else "Vieras"
        except KeyboardInterrupt:
            tyhjenna()
            continue

def tyhjenna():
    """
    Funktio tyhjentää komentorivin.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    tyhjenna()
    main()
