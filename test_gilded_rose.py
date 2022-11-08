import unittest

from GildedRose import GildedRose
from Item import Item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEqual("fixme", items[0].name)


if __name__ == '__main__':
    unittest.main()
