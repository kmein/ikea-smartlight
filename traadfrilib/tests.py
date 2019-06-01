import unittest
from decimal import Decimal

from traadfrilib import light, uri

gateway_ip = "0.0.0.0"


class TestLight(unittest.TestCase):
    def test_dim(self):
        self.assertEqual({5851: 255}, light.dim(100))
        self.assertEqual({5851: 0}, light.dim(0))
        self.assertEqual({5851: 127}, light.dim(50))

    def test_toggle(self):
        self.assertEqual({5850: 1}, light.toggle(True))
        self.assertEqual({5850: 0}, light.toggle(False))

    def test_colour(self):
        pass


class TestUri(unittest.TestCase):
    def test_group(self):
        self.assertEqual("coaps://0.0.0.0:5684/15004", uri.group(gateway_ip))
        self.assertEqual("coaps://0.0.0.0:5684/15004/1337", uri.group(gateway_ip, 1337))

    def test_bulb(self):
        self.assertEqual("coaps://0.0.0.0:5684/15001", uri.bulb(gateway_ip))
        self.assertEqual("coaps://0.0.0.0:5684/15001/1337", uri.bulb(gateway_ip, 1337))


if __name__ == "__main__":
    unittest.main()
