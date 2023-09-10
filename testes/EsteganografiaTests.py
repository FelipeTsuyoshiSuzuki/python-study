import unittest
import exercicios.Esteganografia as E


class MyTestCase(unittest.TestCase):

    def test_convert_fake_to_bacon(self):
        self.assertListEqual(E.fake_to_bacon("iNstITUTo FedERal dE educaCao"),
                             ['A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B',
                              'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A'],
                             "List not correspond")

    def test_convert_fake_to_bacon2(self):
        self.assertListEqual(E.fake_to_bacon(
            "a MaraToNa INtERIf e UM eveNTo DO iNSTItUTo FEDerAL De EducACAo, cIenCIa E TECnoLogia de SAo pauLo QUe "
            "FOi BaSEada nA mARaTONa dE PrOgramACao da SocIedade bRAsILEirA De comPuTACao. eStE EVeNtO e UMa "
            "cOmPeTIcAO de pROgrAmAcaO de compUTaDOres DEsTINAdA Aos aLUnOS dos cUrSOs DA area de informatica dos "
            "campi do instituto federal de sao paulo (tecnicos e superiores)."),
            ['A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B',
             'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A',
             'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A',
             'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A',
             'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B',
             'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A',
             'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A',
             'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B',
             'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B',
             'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A',
             'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B',
             'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B',
             'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
            "List not correspond")

    def test_convert_fake_to_bacon3(self):
        self.assertListEqual(E.fake_to_bacon(
            "eSTEgANogRAfIA E O eSTudo E UsO Das TeCniCas para OCUlTAr a EXisteNcIA dE umA meNSAGEM deNtro de oUtRa, "
            "umA fORMa De SeGUraNcA poR obscurANtIsmo. o PRiMEIRo USO reGisTRado dA pALAvrA DatA DO ANO de 1499, "
            "no livro steganographia, de johannes trithemius."),
            ['A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B',
             'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A',
             'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A',
             'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B',
             'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B',
             'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A',
             'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B',
             'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B',
             'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A'],
            "List not correspond")

    def test_convert_bacon_to_bin(self):
        self.assertEqual(E.convert_bacon_to_bin("ABAABBBB"), "01001111")

    def test_bin_to_char(self):
        self.assertEqual(E.convert_bin_to_char("01001111"), 'O')

    def test_bacon_to_text(self):
        self.assertEqual(E.bacon_to_text(
            ['A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A',
             'A', 'A', 'B', 'A', 'A']), "OLA")

    def test_bacon_to_text2(self):
        self.assertEqual(E.bacon_to_text(
            ['A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A',
             'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B',
             'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B',
             'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A',
             'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A',
             'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A',
             'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B',
             'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B',
             'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A',
             'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B',
             'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']),
            "Encontro amanha naquele local",
            "Texto não corresponde")

    def test_bacon_to_text3(self):
        self.assertEqual(E.bacon_to_text(
            ['A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A',
             'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B',
             'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A',
             'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B',
             'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A',
             'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B',
             'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B',
             'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']),
            "voce vai? Que horas?",
            "Texto não corresponde")


if __name__ == '__main__':
    unittest.main()
