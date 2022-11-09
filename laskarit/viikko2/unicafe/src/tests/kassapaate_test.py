import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        
# Luokan konstruktio oikein

    def test_luotu_kassapaate_kassassa_rahaa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luotu_kassapaate_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luotu_kassapaate_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

# Edulliset
# Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja vaihtorahan suuruus on oikea
    def test_edullisesti_kateisella_riittava_maksu_kassassa_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisesti_kateisella_riittava_maksu_edulliset_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_kateisella_riittava_maksu_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

# Maksu ei riittävä
    def test_edullisesti_kateisella_riittamaton_maksu_kassassa_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisesti_kateisella_riittamaton_maksu_edulliset_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisesti_kateisella_riittamaton_maksu_palautus_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)


# Maukkaat
# Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja vaihtorahan suuruus on oikea
    def test_maukkaasti_kateisella_riittava_maksu_kassassa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaasti_kateisella_riittava_maksu_edulliset_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kateisella_riittava_maksu_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

# Maksu ei riittävä
    def test_maukkaasti_kateisella_riittamaton_maksu_kassassa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaasti_kateisella_riittamaton_maksu_edulliset_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaasti_kateisella_riittamaton_maksu_palautus_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

"""


# Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta


#Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
#Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta

seuraavissa testeissä tarvitaan myös Maksukorttia jonka oletetaan toimivan oikein
# Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
# Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
# Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
# Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
# Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
# Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla

"""