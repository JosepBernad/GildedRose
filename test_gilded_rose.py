import unittest

from GildedRose2 import GildedRose2
from GildedRoseOriginal import GildedRoseOriginal
from Item import Item


class GildedRoseTest(unittest.TestCase):

    names = [
        "Aged Brie",
        "Backstage passes to a TAFKAL80ETC concert",
        "Sulfuras, Hand of Ragnaros",
        ""
    ]

    def testBruteForce(self):
        iterations = 5

        itemsOriginal = []

        for i in range(-100, 100):
            for j in range(-100, 100):
                for name in self.names:
                    itemsOriginal.append(Item(name=name, sell_in=i, quality=j))

        itemsProcessed = itemsOriginal.copy()

        for i in range(1, iterations):
            GildedRoseOriginal(itemsOriginal).update_quality()
            GildedRose2(itemsProcessed).updateQuality()

            for j in range(len(itemsOriginal) - 1):
                if itemsOriginal[i].quality != itemsProcessed[i].quality or \
                        itemsOriginal[i].sell_in != itemsProcessed[i].sell_in:
                    print(itemsOriginal[i])
                    print(itemsProcessed[i])
                    self.assertEqual(itemsOriginal[i].quality, itemsProcessed[i].quality)
                    self.assertEqual(itemsOriginal[i].sell_in, itemsProcessed[i].sell_in)


if __name__ == '__main__':
    unittest.main()
