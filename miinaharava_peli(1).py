"""
pelin pyörittämiseen vaadittavat funktiot
"""
from random import randint, choice
import time
from math import ceil

import haravasto

tila = {
    "kentta": [], 
    "avaamaton_k": [], 
    "nimi": "",
    "miinat": 0,
    "miinojen_paikat": [], 
    "avatut": [], 
    "siirrot": 0,
    "aika_a": 0, 
    "aika_l": 0, 
    "avaamatta": 0, 
    "leveys": 0,
    "korkeus": 0,
    "loppu": False
}

for _ in range(tila["korkeus"]):
    tila["avaamaton_k"].append([" "] * tila["leveys"])
    tila["kentta"].append([" "] * tila["leveys"])

def miinoita(kentta1, sijainnit, vapaat_ruudut, miinat):
    """
    Asettaa kentälle N kpl miinoja satunnaisiin paikkoihin ja
    tallentaa miinojen sijainnit listaan.
    """
    for _ in range(miinat):
        x, y = choice(vapaat_ruudut)
        kentta1[x][y] = "x"
        sijainnit.append((x, y))
        vapaat_ruudut.remove((x, y))

def tulvataytto(avaamatta, kentta, y_aloitus, x_aloitus):
    """
    Merkitsee kentällä olevat tuntemattomat alueet 
    turvalliseksi tulvatäytön avulla. Palauttaa avatut ruudut.
    """
    avatut = []
    koordinaatit = [(y_aloitus,x_aloitus)]
    avatut.append((y_aloitus, x_aloitus))
    while len(koordinaatit) > 0:
        x,y = koordinaatit.pop()
        if kentta[x][y] == "x":
            pass
        elif kentta[x][y] == " ":
            kentta[x][y] = "0"
            avaamatta[x][y] = "0"
            avatut.append((x, y))
            if (x, y) not in tila["avatut"]:
                tila["avatut"].append((x, y))
            mahdolliset_miinat = [[x - 1, y + 1],
                [x - 1, y],
                [x - 1, y - 1],
                [x, y - 1],
                [x + 1, y - 1],
                [x + 1, y],
                [x + 1, y + 1],
                [x, y + 1]]

            for i in range(0, 8):
                local_x, local_y = mahdolliset_miinat[i]
                try:
                    if local_x < 0:
                        pass
                    elif local_y < 0:
                        pass
                    elif kentta[local_x][local_y] == " ":
                        koordinaatit.append((local_x,local_y))
                    elif kentta[local_x][local_y] == "x":
                        pass
                    elif kentta[local_x][local_y] == "0":
                        pass
                    else:
                        pass
                except IndexError:
                    pass

    return avatut

def laske_miinat(x_koordinaatti, y_koordinaatti, kentta):
    """
    Laskee annetun xy koordinaatin ympärillä olvat miinat.
    """
    mahdolliset_miinat = [[x_koordinaatti - 1, y_koordinaatti + 1],
                        [x_koordinaatti - 1, y_koordinaatti],
                        [x_koordinaatti - 1, y_koordinaatti - 1],
                        [x_koordinaatti, y_koordinaatti - 1],
                        [x_koordinaatti + 1, y_koordinaatti - 1],
                        [x_koordinaatti + 1, y_koordinaatti],
                        [x_koordinaatti + 1, y_koordinaatti + 1],
                        [x_koordinaatti, y_koordinaatti + 1]]                 
    miinat = 0
    
    for i in range(0, 8):
        local_y = mahdolliset_miinat[i][0]
        local_x = mahdolliset_miinat[i][1]
        try:
            if local_x < 0:
                pass
            elif local_y < 0:
                pass
            elif kentta[local_x][local_y] == "x":
                miinat += 1
            else:
                pass
        except IndexError:
            pass
                
    return miinat

def avaa_numerot(luukut):
    """
    Piirtää kentälle miinojen määrän avatauille ruuduille.
    """
    l_v = tila["leveys"] - 1
    k = tila["korkeus"] - 1
    if len(luukut) > 1:
        for _, luukku in enumerate(luukut):
            x, y = luukku
            avattavat = [[x - 1, y + 1],
                        [x - 1, y],
                        [x - 1, y - 1],
                        [x, y - 1],
                        [x + 1, y - 1],
                        [x + 1, y],
                        [x + 1, y + 1],
                        [x, y + 1]]

            for z_1 in range(0, 8):
                x_1, y_1 = avattavat[z_1]
                if x_1 <= k and y_1 <= l_v and x_1 >= 0 and y_1 >= 0:
                    if tila["kentta"][x_1][y_1] != "x":
                        tila["avaamaton_k"][x_1][y_1] = tila["kentta"][x_1][y_1]
                        if (x_1, y_1) not in tila["avatut"]:
                            tila["avatut"].append((x_1, y_1))
    else:
        x_1, y_1 = luukut[0]
        if tila["kentta"][x_1][y_1] != "x":
            tila["avaamaton_k"][x_1][y_1] = tila["kentta"][x_1][y_1]
            if (x_1, y_1) not in tila["avatut"]:
                tila["avatut"].append((x_1, y_1))

def tarkista_koordinaatit(y, x):
    """
    Tarkistaa ovatko koordinaatit pelikentällä
    """
    leveys = tila["leveys"] - 1
    korkeus = tila["korkeus"] - 1
    if x < 0 or y < 0:
        return False
    if int(y) > int(korkeus) or int(x) > int(leveys):
        return False
    else:
        return True

def luo_kentta(vaikeus, nimi):
    """
    Luo käyttäjälle piirrettävän kentän sekä piilossa olevan kentän, 
    johon on laskettu miinojen määrät ja niiden sijainnit.
    """
    tila["nimi"] = nimi
    alusta()
    a = 0 # Korkeus
    b_1 = 0 # Leveys
    c = 0 # Miinat

    a, b_1, c = vaikeus

    tila["korkeus"] = int(a)
    tila["leveys"] = int(b_1)
    tila["miinat"] = int(c)

    kentta = []
    tyhja_kentta = []

    for _ in range(a):
        kentta.append([])
        for _ in range(b_1):
            kentta[-1].append(" ")

    for _ in range(a):
        tyhja_kentta.append([])
        for _ in range(b_1):
            tyhja_kentta[-1].append(" ")

    tila["kentta"] = kentta
    tila["avaamaton_k"] = tyhja_kentta

    jaljella = []

    for x in range(a):
        for y in range(b_1):
            jaljella.append((x, y))
    
    tila["avaamatta"] = int((a * b_1) - c)
    miinoita(kentta, tila["miinojen_paikat"], jaljella, c)

def kasittele_hiiri(x, y, nappi, muokkausnapit):
    """
    Käsittelee hiiren napin klikkaukset.
    """
    hiiri = {
        "vasen": haravasto.HIIRI_VASEN,
        "oikea": haravasto.HIIRI_OIKEA,
        "keski": haravasto.HIIRI_KESKI,
    }
    vasen = hiiri["vasen"]
    oikea = hiiri["oikea"]
    keski = hiiri["keski"]

    x = ceil((x / 40) - 1)
    y = ceil((y / 40) - 1)
    arvo = tarkista_koordinaatit(y, x)
    if tila["aika_a"] == 0 and arvo == True:
        tila["aika_a"] = round(time.time())

    if tila["kentta"][y][x] == "x" and nappi == vasen and arvo == True and tila["loppu"] == False:
        tila["siirrot"] += 1
        tarkista_voitto(y ,x)

    if nappi == vasen and arvo == True and tila["loppu"] == False:
        tila["siirrot"] += 1
        avattu = tulvataytto(tila["avaamaton_k"], tila["kentta"], y, x)
        avaa_numerot(avattu)
        tarkista_voitto(y ,x)

    elif nappi == oikea and tila["avaamaton_k"][y][x] == " " and arvo == True and tila["loppu"] == False:
        tila["avaamaton_k"][y][x] = "f"
        tila["siirrot"] += 1
    elif nappi == oikea and tila["avaamaton_k"][y][x] == "f" and arvo == True and tila["loppu"] == False:
        tila["avaamaton_k"][y][x] = " "
        tila["siirrot"] += 1


def piirra_kentta():
    """
    Piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.piirra_tekstia(f"Miinoja: {tila['miinat']}", 1, tila["korkeus"] * 40 + 2)
    haravasto.aloita_ruutujen_piirto()
    
    for x, rivi in enumerate(tila["avaamaton_k"]):
        for y, ruutu in enumerate(rivi):
            x_1 = x * 40
            y_2 = y * 40
            
            haravasto.lisaa_piirrettava_ruutu(ruutu, y_2, x_1)
            
    haravasto.piirra_ruudut()

def valitse_ensimmainen_ruutu():
    """
    Valitsee satunnaisen ruudun, joka ei ole miina.
    """
    while True:
        x = randint(0, tila["korkeus"] - 1)
        y = randint(0, tila["leveys"] - 1)

        if tila["kentta"][x][y] != "x":
            return x, y


def pelaa():
    """
    Funktio aloittaa pelin ja laskee piilotetulle kentälle miinojen määrät.
    """
    for i in range(len(tila["kentta"])):
        for j in range(len(tila["kentta"][i])):
            if tila["kentta"][i][j] != "x":
                maara = laske_miinat(j, i, tila["kentta"])
                if maara == 0:
                    tila["kentta"][i][j] = " "
                else:
                    tila["kentta"][i][j] = maara

    haravasto.luo_ikkuna(tila["leveys"]*40, tila["korkeus"] * 40 + 30)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aseta_toistuva_kasittelija(paivita_naytto)
    haravasto.aloita()

def paivita_naytto(aika):
    """
    Käsittelijä funktio ajan päivittämiseen näytölle.
    """
    aika_jaljella = tila["aika_a"] - round(time.time())
    piirra_kentta()
    haravasto.tyhjaa_ikkuna()
    haravasto.aloita_ruutujen_piirto()
    haravasto.piirra_tekstia(f"Aika: {max(0, aika_jaljella)}", 1, tila["korkeus"] * 40 + 10)

    haravasto.aloita_ruutujen_piirto()
    haravasto.piirra_ruudut()

def tarkista_voitto(x ,y):
    """
    tarkistaa voittiko pelaaja
    """
    if tila["kentta"][x][y] == "x":
        tila["loppu"] = True
        tila["aika_l"] = round(time.time()) - tila["aika_a"]
        tallenna_peli("Häviö")
        try:
            for i in range(len(tila["miinojen_paikat"])):
                x, y = tila["miinojen_paikat"][i]
                tila["avaamaton_k"][x][y] = "x"
        except IndexError:
            pass

    elif int(tila["avaamatta"]) == int(len(tila["avatut"])):
        tila["loppu"] = True
        tila["aika_l"] = round(time.time()) - tila["aika_a"]
        tallenna_peli("Voitto")
        haravasto.lopeta()
        print("\n ONNEKSI OLKOON VOITIT PELIN! ")
        input("\n Paina enteriä jatkaaksesi ")

def tallenna_peli(lopputulos):
    """
    tallentaa tilastoihin
    """
    pvm = time.strftime("%d.%m.%Y %H:%M", time.localtime())
    try:
        with open("tilastot.csv", "a") as kohde:
            kohde.write(
                f"{tila['nimi']},{pvm},{tila['aika_l']},{tila['siirrot']},"
                f"{lopputulos},{tila['korkeus']},{tila['leveys']},{tila['miinat']}\n"
            )


    except IOError:
        print("Tallennus epäonnistui.")

def alusta():
    """
    alustaa kentän
    """
    tila["kentta"] = None
    tila["avaamaton_k"] = None
    tila["miinat"] = 0
    tila["miinojen_paikat"] = []
    tila["avatut"] = []
    tila["siirrot"] = 0
    tila["aika_a"] = 0
    tila["aika_l"] = 0
    tila["avaamatta"] = 0
    tila["leveys"] = 0
    tila["korkeus"] = 0
    tila["loppu"] = False
