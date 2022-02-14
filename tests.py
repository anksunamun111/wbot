import unittest
import config

class TgBotTests(unittest.TestCase):

    def test_owm_token_is_exists(self):
        self.assertIsNotNone(config.TOKEN)

    def test_get_weather(self):
        with self.assertRaises(Exception):
            from wbot import get_weather
            get_weather("вв")

if __name__ == "__main__":
    unittest.main()