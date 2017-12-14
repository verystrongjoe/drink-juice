import unittest

def upper_reverse(text) :
    return ''.join(reversed(text.upper()))



class TestUpperReverse(unittest.TestCase) :
    def test_upper_reverse(self):
        self.assertEqual(upper_reverse('hello'), 'OLLEH')