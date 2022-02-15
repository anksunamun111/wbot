import unittest
#from wbot import *
import wbot
import asyncio

class TgBotTests(unittest.TestCase):

    def test_owm_token_is_exists(self):
        import config
        self.assertIsNotNone(config.TOKEN)


    #def test_location(self):
        #model = asyncio.run(get_location(39.92, 116.41))
       # print(model)

    def test_f(self):
        #model = asyncio.run(f())
        print(wbot.f())


    #def test_get_weather(self):
        #with self.assertRaises(Exception):
            #from wbot import get_weather
            #get_weather("вв")

    #def test_get_location(self):
        #from wbot import get_location
        #self.assertIsNotNone(get_location('88', '77'))

if __name__ == "__main__":
    unittest.main()

