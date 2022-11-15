import unittest
import logging

from GildedRoseJosep import GildedRoseJosep
from gilded_rose import GildedRose
from Item import Item

class GildedRoseTest(unittest.TestCase):

    NAMES = [
        "Aged Brie",
        "Backstage passes to a TAFKAL80ETC concert",
        "Sulfuras, Hand of Ragnaros",
        ""
    ]

    def testBruteForce(self):
        days = 2

        itemsOriginal = []
        itemsProcessed = []
        itemsProcessedOriginal = []

        for i in range(-100, 100):
            for j in range(-100, 100):
                for name in self.NAMES:
                    itemsOriginal.append(Item(name=name, sell_in=i, quality=j))
                    itemsProcessed.append(Item(name=name, sell_in=i, quality=j))
                    itemsProcessedOriginal.append(Item(name=name, sell_in=i, quality=j))

        for i in range(1, days):
            GildedRose(itemsOriginal).update_quality()
            GildedRoseJosep(itemsProcessed).updateQuality()

            for j in range(len(itemsOriginal) - 1):
                if itemsOriginal[j].quality != itemsProcessed[j].quality or \
                        itemsOriginal[j].sell_in != itemsProcessed[j].sell_in:
                    print("------ " + i.__str__() + " ------")
                    print("Item original:" + itemsOriginal[j].__repr__())
                    print("Item processed original:" + itemsProcessedOriginal[j].__repr__())
                    print("Item processed:" + itemsProcessed[j].__repr__())
                    self.assertEqual(itemsOriginal[j].quality, itemsProcessed[j].quality)
                    self.assertEqual(itemsOriginal[j].sell_in, itemsProcessed[j].sell_in)


if __name__ == '__main__':
    unittest.main()
