import unittest

class TgBotTests(unittest.TestCase):

    def test_d(self):
        from wbot import f
        self.assertEqual(f(), 2)

    def test_get_location(self):
        from wbot import get_location
        self.assertIsNotNone(get_location('88', '77'))

    def test_owm_token_is_exists(self):
        import config
        self.assertIsNotNone(config.TOKEN)

if __name__ == "__main__":
    unittest.main()

