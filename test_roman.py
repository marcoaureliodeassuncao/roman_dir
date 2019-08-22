import unittest
from src.roman_marco import valida_numero, numero_para_romano


num_romano_1 = 'I'
num_romano_3999 = 'MMMCMXCIX'
num_romano_2 = 'II'


class Tester(unittest.TestCase):

	def test_valida_numero(self):
		self.assertTrue(valida_numero('20'))
		self.assertTrue(valida_numero('3999'))
		self.assertFalse(valida_numero('-1'))
		self.assertFalse(valida_numero('XX'))
		self.assertTrue(valida_numero('2.7'))
		self.asserFalse(valida_numero('0'))
		pass

	def test_numero_para_romano(self):
		self.assertEqual(numero_para_romano('1'), num_romano_1)
		self.assertEqual(numero_para_romano('3999'), num_romano_3999)
		self.assertFalse(numero_para_romano('-1'))
		self.assertFalse(numero_para_romano('pizza'))
		self.assertEqual(numero_para_romano('2.5'), num_romano_2)
		self.assertFalse(numero_para_romano('0'))
		pass


if __name__ == '__main__':

	unittest.main()
