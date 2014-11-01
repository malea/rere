import unittest
from rere import *

class ReReTest(unittest.TestCase):

    def test_raw_regex(self):
        re = RawRegex('ab*')
        self.assertFalse(re.match(''))
        self.assertTrue(re.match('a'))
        self.assertFalse(re.match('aa'))
        self.assertTrue(re.match('ab'))

        # rere's match function must match the whole string, not just a prefix
        # (like re.match)
        self.assertFalse(re.match('aba'))
        self.assertTrue(re.match_prefix('aba'))

    def test_exactly(self):
        re = Exactly('$2+$2')
        self.assertFalse(re.match(''))
        self.assertFalse(re.match('$1+$2+$2'))
        self.assertFalse(re.match('$2+$2+$1'))
        self.assertTrue(re.match('$2+$2'))
        self.assertTrue(re.match_prefix('$2+$2+$1'))
    
    def test_any_char(self):
        re = AnyChar
        self.assertTrue(re.match('a'))
        self.assertTrue(re.match('1'))
        self.assertTrue(re.match(' '))
        self.assertTrue(re.match('\n'))
        self.assertFalse(re.match(''))
        self.assertFalse(re.match('ab'))

    def test_digit(self):
        re = Digit
        self.assertTrue(re.match('1'))
        self.assertFalse(re.match('11'))
        self.assertFalse(re.match('1a'))
        self.assertFalse(re.match('A'))

    def test_letter(self):
        re = Letter
        self.assertTrue(re.match('a'))
        self.assertTrue(re.match('A'))
        self.assertFalse(re.match('1'))
        self.assertFalse(re.match('a2'))
        
    def test_whitespace(self):
        re = Whitespace
        self.assertTrue(re.match(' '))
        self.assertTrue(re.match('\n'))
        self.assertFalse(re.match('2'))
        self.assertFalse(re.match('a 3 '))

    def test_anything(self):
        re = Anything
        self.assertTrue(re.match(''))
        self.assertTrue(re.match('ab'))
        self.assertTrue(re.match('ab\n123'))

    def test_multipart_regex(self):
        re = Exactly('123') + Anything + Exactly('a\n')
        self.assertFalse(re.match(''))
        self.assertFalse(re.match('123'))
        self.assertTrue(re.match('123456a\n'))
        self.assertTrue(re.match('123a\na\n'))

    def test_one_or_more(self):
        re = Exactly('puppy').one_or_more
        self.assertFalse(re.match(''))
        self.assertFalse(re.match('kitten'))
        self.assertTrue(re.match('puppy'))
        self.assertTrue(re.match('puppypuppy'))

    def test_zero_or_more(self):
        re = Exactly('puppy').zero_or_more
        self.assertTrue(re.match(''))
        self.assertFalse(re.match('kitten'))
        self.assertTrue(re.match('puppy'))
        self.assertTrue(re.match('puppypuppy'))

    def test_zero_or_one(self):
        re = Exactly('puppy').zero_or_one
        self.assertTrue(re.match(''))
        self.assertFalse(re.match('kitten'))
        self.assertTrue(re.match('puppy'))
        self.assertFalse(re.match('puppypuppy'))

    def test_multiply_single(self):
        re = Exactly('cat') * 3
        self.assertFalse(re.match(''))
        self.assertFalse(re.match('cat'))
        self.assertTrue(re.match('catcatcat'))

    def test_multiply_multipart(self):
        re = (Exactly('cat') + Exactly('dog')) * 3
        self.assertFalse(re.match(''))
        self.assertFalse(re.match('catdog'))
        self.assertTrue(re.match('catdogcatdogcatdog'))

if __name__ == '__main__':
    unittest.main()
