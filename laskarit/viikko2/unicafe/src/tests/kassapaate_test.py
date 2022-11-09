import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti_riittaa = Maksukortti(1000)
        self.kortti_riittamaton = Maksukortti(100)
        
# Luokan konstruktio oikein
    def test_luotu_kassapaate_kassassa_rahaa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luotu_kassapaate_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luotu_kassapaate_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

# Edulliset käteisellä
    def test_edullisesti_kateisella_riittava_maksu_kassassa_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisesti_kateisella_riittava_maksu_edulliset_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_kateisella_riittava_maksu_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_edullisesti_kateisella_riittamaton_maksu_kassassa_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisesti_kateisella_riittamaton_maksu_edulliset_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisesti_kateisella_riittamaton_maksu_palautus_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

# Maukkaat käteisellä
    def test_maukkaasti_kateisella_riittava_maksu_kassassa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaasti_kateisella_riittava_maksu_edulliset_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kateisella_riittava_maksu_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_maukkaasti_kateisella_riittamaton_maksu_kassassa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaasti_kateisella_riittamaton_maksu_edulliset_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaasti_kateisella_riittamaton_maksu_palautus_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

#Edulliset kortilla
    def test_edullisesti_kortilla_riittava_maksu_edulliset_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_riittaa)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_kortilla_riittava_maksu_summa_veloitetaan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_riittaa)
        self.assertEqual(self.kortti_riittaa.saldo, 760)

    def test_edullisesti_kortilla_riittava_maksu_onnistui(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti_riittaa), True)

    def test_edullisesti_kortilla_riittamaton_maksu_edulliset_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_riittamaton)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisesti_kortilla_riittamaton_maksu_summa_veloitetaan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_riittamaton)
        self.assertEqual(self.kortti_riittamaton.saldo, 100)

    def test_edullisesti_kortilla_riittamaton_maksu_epaonnistui(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti_riittamaton), False)

#Maukkaat kortilla
    def test_maukkaasti_kortilla_riittava_maksu_maukkaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_riittaa)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kortilla_riittava_maksu_summa_veloitetaan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_riittaa)
        self.assertEqual(self.kortti_riittaa.saldo, 600)

    def test_maukkaasti_kortilla_riittava_maksu_onnistui(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti_riittaa), True)

    def test_maukkaasti_kortilla_riittamaton_maksu_maukkaat_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_riittamaton)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaasti_kortilla_riittamaton_maksu_summa_veloitetaan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_riittamaton)
        self.assertEqual(self.kortti_riittamaton.saldo, 100)

    def test_maukkaasti_kortilla_riittamaton_maksu_epaonnistui(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti_riittamaton), False)


    def test_edullisesti_kortilla_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_riittaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaasti_kortilla_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_riittaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
"""

# Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
# Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla

"""