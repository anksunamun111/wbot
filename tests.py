import unittest

from wbot import get_location

lat = 127
lon = 88

class TgBotTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual('foo'.upper(), 'FOO')

#     def testGetLocation(self):
 #      tGL = get_location(lat, lon)
  #      self.assertIsNotNone(tGL)

#1

if __name__ == "__main__":
    unittest.main()