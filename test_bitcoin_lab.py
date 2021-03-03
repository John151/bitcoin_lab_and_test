import unittest
from unittest import TestCase
from unittest.mock import patch, call
import bitcoin_lab


class TestBitcoinLab(TestCase):

    """Mock input and force to return a value"""
    @patch('builtins.input', side_effect=[5])
    def test_bitcoin_input(self, mock_input):
        bitcoin = bitcoin_lab.get_bitcoin_holdings()
        self.assertEqual(5, bitcoin)

    @patch('builtins.input', side_effect=['pineapple', '', -8, 0, 9.3])
    def test_bitcoin_input_invalid_rejected(self, mock_input):
        bitcoin = bitcoin_lab.get_bitcoin_holdings()
        self.assertEqual(9.3, bitcoin)


    @patch('builtins.print')
    def test_display_result(self, mock_print):
        bitcoin_lab.display_result(2, 2.246)
        mock_print.assert_called_once_with('2 Bitcoin is equivalent to $2.46')


if __name__ == '__main__':
    unittest.main()
