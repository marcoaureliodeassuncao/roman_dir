import unittest
from src.roman_marco import valida_numero, numero_para_romano


num_romano_1 = 'I'
num_romano_3999 = 'MMMCMXCIX'
num_romano_2 = 'II'


class Tester(unittest.TestCase):

	def test_valida_numero_positivo(self):
		self.assertTrue(valida_numero('20'))
		pass

	def test_valida_numero_maximo_permitido(self):
		self.assertTrue(valida_numero('3999'))
		pass

	def test_valida_numero_negativo(self):
		self.assertFalse(valida_numero('-1'))
		pass

	def test_valida_numero_com_letras(self):
		self.assertFalse(valida_numero('XX'))
		pass

	def test_valida_numero_decimal(self):
		self.assertTrue(valida_numero('2.7'))
		pass

	def test_valida_numer_zero(self):
		self.assertFalse(valida_numero('0'))
		pass

	def test_numero_para_romano(self):
		self.assertEqual(numero_para_romano('1'), num_romano_1)
		pass

	def test_numero_para_romano_maximo_permitido(self):
		self.assertEqual(numero_para_romano('3999'), num_romano_3999)
		pass

	def test_numero_para_romano_negativo(self):
		self.assertFalse(numero_para_romano('-1'))
		pass

	def test_numero_para_romano_letras(self):
		self.assertFalse(numero_para_romano('pizza'))
		pass

	def test_numero_para_romano_decimal(self):
		self.assertEqual(numero_para_romano('2.5'), num_romano_2)
		pass

	def test_numero_para_romano_zero(self):
		self.assertFalse(numero_para_romano('0'))
		pass


if __name__ == '__main__':

	unittest.main()
