import unittest


from wbot import get_location

lat = 127
lon = 88

class TgBotTests(unittest.TestCase):

    def testGetLocation(self):
        tGL = get_location(lat, lon)
        self.assertIsNotNone(tGL)

if __name__ == "__main__":
    unittest.main()