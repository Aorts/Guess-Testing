import guessNum
import unittest
from unittest import mock


class guessNumberTest(unittest.TestCase):
    #guess_int
    @mock.patch('random.randint',return_value=int(9))
    def test_guess_int_1_to_10_should_be_9(self, mock_randint):
        result = guessNum.guess_int(1,10)
        self.assertEqual(result,9,"should be 9")
        mock_randint.assert_called_once()
        mock_randint.guess_int.return_value = 9
        
    @mock.patch('random.randint',return_value=int(516))
    def test_guess_int_10_to_999_should_be_516(self, mock_randint):
        result = guessNum.guess_int(10,999)
        self.assertEqual(result,516,"should be 516")
        mock_randint.assert_called_once()
        mock_randint.guess_int.return_value = 516
    
    @mock.patch('random.randint',return_value=int(17))
    def test_guess_int_80_to_9_should_be_17(self, mock_randint):
        result = guessNum.guess_int(80,9)
        self.assertEqual(result,17,"should be 17")
        mock_randint.assert_called_once()
        mock_randint.guess_int.return_value = 17

    @mock.patch('random.randint',return_value=int(0))
    def test_guess_int_0_to_0_should_be_0(self, mock_randint):
        result = guessNum.guess_int(0,0)
        self.assertEqual(result,0,"should be 0")
        mock_randint.assert_called_once()
        mock_randint.guess_int.return_value = 0

    @mock.patch('random.randint',return_value=int(64))
    def test_guess_int_64_to_64_should_be_64(self, mock_randint):
        result = guessNum.guess_int(64,64)
        self.assertEqual(result,64,"should be 64")
        mock_randint.assert_called_once()
        mock_randint.guess_int.return_value = 64

    @mock.patch('random.randint',return_value=int(-491))
    def test_guess_int_minus999_to_minus1_should_be_minus491(self, mock_randint):
        result = guessNum.guess_int(-999,-1)
        self.assertEqual(result,-491,"should be -491")
        mock_randint.assert_called_once()
        mock_randint.guess_int.return_value = -491

    @mock.patch('random.randint',return_value=int(17))
    def test_guess_int_minus99_to_99_should_be_17(self, mock_randint):
        result = guessNum.guess_int(-99,99)
        self.assertEqual(result,17,"should be 17")
        mock_randint.assert_called_once()
        mock_randint.guess_int.return_value = 17

        
    @mock.patch('random.randint', return_value=130)
    def test_get_random_randint_130(self,mock_randint):
        result = guessNum.guess_int(1,150)
        self.assertEqual(result, 130)
        mock_randint.assert_called_once()
        mock_randint.guess_int.return_value = 130

    @mock.patch('random.randint',return_value=int(2))
    def test_guess_int_1_to_10_should_be_2(self, mock_randint):
        result = guessNum.guess_int(1,10)
        self.assertEqual(result,2,"should be 2")
        mock_randint.assert_called_once()
        mock_randint.guess_int.return_value = 2

    @mock.patch('random.randint',return_value=int(7))
    def test_guess_int_1_to_10_should_be_7(self, mock_randint):
        result = guessNum.guess_int(1,10)
        self.assertEqual(result,7,"should be 7")
        mock_randint.assert_called_once()
        mock_randint.guess_int.return_value = 7

    #guess_float
    @mock.patch('random.uniform',return_value=float(7.5))
    def test_guess_float_1_to_10_should_be_7point5(self, mock_uniform):
        result = guessNum.guess_float(1,10)
        self.assertEqual(result,7.5,"should be 7.5")
        mock_uniform.assert_called_once()
        mock_uniform.guess_int.return_value = 7.5
    
    @mock.patch('random.uniform',return_value=float(12.2879))
    def test_guess_float_11point7_to_12point9_should_be_12point2879(self, mock_uniform):
        result = guessNum.guess_float(11.7,12.9)
        self.assertEqual(result,12.2879,"should be 12.2879")
        mock_uniform.assert_called_once()
        mock_uniform.guess_int.return_value = 12.2879

    @mock.patch('random.uniform',return_value=float(-31.178))
    def test_guess_float_minus_78point91489_to_minus_2point5134_should_be_minus_31_178(self, mock_uniform):
        result = guessNum.guess_float(-78.91489,-2.5134)
        self.assertEqual(result,-31.178,"should be -31.178")
        mock_uniform.assert_called_once()
        mock_uniform.guess_int.return_value = -31.178

    @mock.patch('random.uniform',return_value=float(-51.238619))
    def test_guess_float_minus99_to_minus30_should_be_minus_51_2386195(self, mock_uniform):
        result = guessNum.guess_float(-99,-30)
        self.assertEqual(result,-51.238619,"should be -51.238619")
        mock_uniform.assert_called_once()
        mock_uniform.guess_int.return_value = -51.238619

    @mock.patch('random.randint',return_value=float(0.0))
    def test_guess_float_0_to_0_should_be_0point0(self, mock_uniform):
        result = guessNum.guess_int(0,0)
        self.assertEqual(result,0.0,"should be 0.0")
        mock_uniform.assert_called_once()
        mock_uniform.guess_int.return_value = 0.0

    @mock.patch('random.uniform', return_value=120.02)
    def test_get_random_uniform_1_2_0_0_2(self,mock_uniform):
        result = guessNum.guess_float(0.0,210.0)
        self.assertEqual(result, 120.02)
        mock_uniform.assert_called_once()
        mock_uniform.guess_int.return_value = 120.02

    @mock.patch('random.uniform', return_value=4.8)
    def test_get_random_uniform_4_8(self,mock_uniform):
        result = guessNum.guess_float(0.0,10.0)
        self.assertEqual(result, 4.8)
        mock_uniform.assert_called_once()
        mock_uniform.guess_int.return_value = 4.8

    @mock.patch('random.uniform', return_value=0.15)
    def test_get_random_uniform_0_1_5(self,mock_uniform):
        result = guessNum.guess_float(0.0,10.0)
        self.assertEqual(result, 0.15)
        mock_uniform.assert_called_once()
        mock_uniform.guess_int.return_value = 0.15

    @mock.patch('random.uniform', return_value=12.0211692)
    def test_get_random_uniform_12_0211692(self,mock_uniform):
        result = guessNum.guess_float(10.5,15.5)
        self.assertEqual(result, 12.0211692)
        mock_uniform.assert_called_once()
        mock_uniform.guess_int.return_value = 12.0211692


    @mock.patch('random.uniform', return_value=25.5787628)
    def test_get_random_uniform_25_5787628(self,mock_uniform):
        result = guessNum.guess_float(20.5,30.5)
        self.assertEqual(result, 25.5787628)
        mock_uniform.assert_called_once()
        mock_uniform.guess_int.return_value = 25.5787628
        



if __name__ == '__main__':
    unittest.main()