import unittest
from funkcijos1 import (skaiciu_suma,
                        saraso_suma,
                        didziausias_skaicius,
                        stringas_atbulai,
                        info_apie_sakini,
                        unikalus_sarasas,
                        ar_pirminis,
                        isrikiuoti_nuo_galo,
                        ar_keliamieji,
                        patikrinti_data)
import datetime

class TestFunkcijos1(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(56, skaiciu_suma(45, 5, 6))
        self.assertEqual(48, skaiciu_suma(16, 16, 16))
        self.assertEqual(2, skaiciu_suma(-5, 5, 2))

    def test_saraso_suma(self):
        masyvas1 = [6, 5, 54, 4]
        self.assertEqual(69, saraso_suma(masyvas1))
        masyvas2 = [16, 16, 16]
        self.assertEqual(48, saraso_suma(masyvas2))
        masyvas2 = [99, -16, 15]
        self.assertEqual(98, saraso_suma(masyvas2))

    def test_didziausias_skaicius(self):
        self.assertEqual(4545, didziausias_skaicius(5, 45, 787, 4545, 12))
        self.assertEqual(667, didziausias_skaicius(667, 454, 44, 45, 424))

    def test_stringas_atbulai(self):
        self.assertEqual("akieroN satanoD", stringas_atbulai("Donatas Noreika"))

    def test_info_apie_sakini(self):
        self.assertEqual("Didžiosios: 1, mažosios: 20, skaičiai: 3", info_apie_sakini("Laba diena laba diena lab 522"))

    def test_unikalus_sarasas(self):
        self.assertEqual([4, 5, 'Labas', 6, True, 10], unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]))

    def test_ar_pirminis(self):
        self.assertTrue(ar_pirminis(7))
        self.assertTrue(ar_pirminis(11))
        self.assertFalse(ar_pirminis(4))
        self.assertFalse(ar_pirminis(9))

    def test_isrikiuoti_nuo_galo(self):
        self.assertEqual("keturi trys du Vienas", isrikiuoti_nuo_galo("Vienas du trys keturi"))

    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji(2000))
        self.assertTrue(ar_keliamieji(1996))
        self.assertFalse(ar_keliamieji(1993))
        self.assertFalse(ar_keliamieji(2100))

    def test_patikrinti_data(self):
        now = datetime.datetime.strptime("2023-04-06 15:33:21", "%Y-%m-%d %H:%M:%S")
        self.assertEqual((23, 279.3205479452055, 1213, 8496, 203907.3525, 12234441.15, 734066469.0), patikrinti_data("2000-01-01 12:12:12", now))
