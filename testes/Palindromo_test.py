import unittest
import exercicios.Palindromo as P

class PalindromoTestCase(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(P.count_character("a", "arara"), 3)

    def test_letter_separator(self):
        self.assertDictEqual(P.letter_separator("arara"), {'a': 3, 'r': 2})

    def test_letter_separator_case_sensitive(self):
        self.assertDictEqual(P.letter_separator("AraRa"), {'a': 3, 'r': 2})

    def test_is_even_true(self):
        self.assertTrue(P.is_even("arara"))

    def test_is_even_false(self):
        self.assertFalse(P.is_even("marcio"))

    def test_get_even_letter_count(self):
        self.assertEqual(P.get_even_letters_count("arara"), 1)

    def test_get_even_letter_count_more_than_1(self):
        self.assertEqual(P.get_even_letters_count("mario"), 5)

    def test_is_palindromo_true(self):
        self.assertEqual(P.is_palindromo("moraram"), 1)

    def test_is_palindromo_false(self):
        self.assertEqual(P.is_palindromo("algoritmo"), 0)


if __name__ == '__main__':
    unittest.main()
