from __future__ import print_function

from GildedRose2 import *
from GildedRoseOriginal import *

import unittest

if __name__ == "__main__":
    print("OMGHAI!")

    iterations = 4

    itemsOriginal = []
    items = []

    names = [
        "Aged Brie",
        "Backstage passes to a TAFKAL80ETC concert",
        "Sulfuras, Hand of Ragnaros",
        ""
    ]

    for i in range(-100, 100):
        for j in range(-100, 100):
            for name in names:
                items.append(Item(name=name, sell_in=i, quality=j))
                itemsOriginal.append(Item(name=name, sell_in=i, quality=j))

    tc = unittest.TestCase()

    for day in range(1, iterations):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        GildedRoseOriginal(itemsOriginal).update_quality()
        #  GildedRose(items).updateQuality()
        GildedRose2(items).updateQuality()
        for i in range(len(items) - 1):
            if itemsOriginal[i].quality != items[i].quality or itemsOriginal[i].sell_in != items[i].sell_in:
                print(itemsOriginal[i])
                print(items[i])
                tc.assertEqual(itemsOriginal[i].quality, items[i].quality)
                tc.assertEqual(itemsOriginal[i].sell_in, items[i].sell_in)
