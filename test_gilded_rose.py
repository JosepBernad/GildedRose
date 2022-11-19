import unittest
import random

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

    def testAgedBrie(self):
        days = 2

        s1 = 0
        s2 = 1

        q1 = 48
        q2 = 49
        q3 = 50

        itemsProcessed = [
            Item(name=self.NAMES[0], sell_in=s1, quality=q1),
            Item(name=self.NAMES[0], sell_in=s2, quality=q1),
            Item(name=self.NAMES[0], sell_in=s1, quality=q2),
            # Item(name=self.NAMES[0], sell_in=s2, quality=q2),
            Item(name=self.NAMES[0], sell_in=s1, quality=q2),
            Item(name=self.NAMES[0], sell_in=s2, quality=q3)
        ]

        itemsExpected = [
            Item(name=self.NAMES[0], sell_in=-1, quality=50),
            Item(name=self.NAMES[0], sell_in=0, quality=49),
            Item(name=self.NAMES[0], sell_in=-1, quality=50),
            # Item(name=self.NAMES[0], sell_in=0, quality=50),
            Item(name=self.NAMES[0], sell_in=-1, quality=50),
            Item(name=self.NAMES[0], sell_in=0, quality=50)
        ]

        self.runTest(days, itemsExpected, itemsProcessed)

    def testBackstage(self):
        days = 2

        s1 = 0
        s2 = 5
        s3 = 10
        s4 = 11

        q1 = 47
        q2 = 48
        q3 = 49
        q4 = 50

        itemsProcessed = [
            Item(name=self.NAMES[1], sell_in=s1, quality=q1),
            Item(name=self.NAMES[1], sell_in=s1, quality=q2),
            Item(name=self.NAMES[1], sell_in=s1, quality=q3),
            Item(name=self.NAMES[1], sell_in=s1, quality=q4),
            Item(name=self.NAMES[1], sell_in=s2, quality=q1),
            Item(name=self.NAMES[1], sell_in=s2, quality=q2),
            Item(name=self.NAMES[1], sell_in=s2, quality=q3),
            Item(name=self.NAMES[1], sell_in=s2, quality=q4),
            Item(name=self.NAMES[1], sell_in=s3, quality=q1),
            # Item(name=self.NAMES[1], sell_in=s3, quality=q2),
            Item(name=self.NAMES[1], sell_in=s3, quality=q3),
            Item(name=self.NAMES[1], sell_in=s3, quality=q4),
            Item(name=self.NAMES[1], sell_in=s4, quality=q1),
            # Item(name=self.NAMES[1], sell_in=s4, quality=q2),
            # Item(name=self.NAMES[1], sell_in=s4, quality=q3),
            Item(name=self.NAMES[1], sell_in=s4, quality=q4)
        ]

        itemsExpected = [
            Item(name=self.NAMES[1], sell_in=-1, quality=0),
            Item(name=self.NAMES[1], sell_in=-1, quality=0),
            Item(name=self.NAMES[1], sell_in=-1, quality=0),
            Item(name=self.NAMES[1], sell_in=-1, quality=0),
            Item(name=self.NAMES[1], sell_in=4, quality=50),
            Item(name=self.NAMES[1], sell_in=4, quality=50),
            Item(name=self.NAMES[1], sell_in=4, quality=50),
            Item(name=self.NAMES[1], sell_in=4, quality=50),
            Item(name=self.NAMES[1], sell_in=9, quality=49),
            # Item(name=self.NAMES[1], sell_in=9, quality=50),
            Item(name=self.NAMES[1], sell_in=9, quality=50),
            Item(name=self.NAMES[1], sell_in=9, quality=50),
            Item(name=self.NAMES[1], sell_in=10, quality=48),
            # Item(name=self.NAMES[1], sell_in=10, quality=49),
            # Item(name=self.NAMES[1], sell_in=10, quality=50),
            Item(name=self.NAMES[1], sell_in=10, quality=50)
        ]

        self.runTest(days, itemsExpected, itemsProcessed)

    def testSulfuras(self):
        days = 2

        s1 = random.randint(-2147483648, 2147483647)
        s2 = random.randint(-2147483648, 2147483647)
        s3 = random.randint(-2147483648, 2147483647)
        s4 = random.randint(-2147483648, 2147483647)

        q1 = random.randint(-2147483648, 2147483647)
        q2 = random.randint(-2147483648, 2147483647)
        q3 = random.randint(-2147483648, 2147483647)
        q4 = random.randint(-2147483648, 2147483647)

        itemsProcessed = [
            Item(name=self.NAMES[2], sell_in=s1, quality=q1),
            Item(name=self.NAMES[2], sell_in=s1, quality=q2),
            Item(name=self.NAMES[2], sell_in=s1, quality=q3),
            Item(name=self.NAMES[2], sell_in=s1, quality=q4),
            Item(name=self.NAMES[2], sell_in=s2, quality=q1),
            Item(name=self.NAMES[2], sell_in=s2, quality=q2),
            Item(name=self.NAMES[2], sell_in=s2, quality=q3),
            Item(name=self.NAMES[2], sell_in=s2, quality=q4),
            Item(name=self.NAMES[2], sell_in=s3, quality=q1),
            Item(name=self.NAMES[2], sell_in=s3, quality=q2),
            Item(name=self.NAMES[2], sell_in=s3, quality=q3),
            Item(name=self.NAMES[2], sell_in=s3, quality=q4),
            Item(name=self.NAMES[2], sell_in=s4, quality=q1),
            Item(name=self.NAMES[2], sell_in=s4, quality=q2),
            Item(name=self.NAMES[2], sell_in=s4, quality=q3),
            Item(name=self.NAMES[2], sell_in=s4, quality=q4)
        ]

        itemsExpected = [
            Item(name=self.NAMES[2], sell_in=s1, quality=q1),
            Item(name=self.NAMES[2], sell_in=s1, quality=q2),
            Item(name=self.NAMES[2], sell_in=s1, quality=q3),
            Item(name=self.NAMES[2], sell_in=s1, quality=q4),
            Item(name=self.NAMES[2], sell_in=s2, quality=q1),
            Item(name=self.NAMES[2], sell_in=s2, quality=q2),
            Item(name=self.NAMES[2], sell_in=s2, quality=q3),
            Item(name=self.NAMES[2], sell_in=s2, quality=q4),
            Item(name=self.NAMES[2], sell_in=s3, quality=q1),
            Item(name=self.NAMES[2], sell_in=s3, quality=q2),
            Item(name=self.NAMES[2], sell_in=s3, quality=q3),
            Item(name=self.NAMES[2], sell_in=s3, quality=q4),
            Item(name=self.NAMES[2], sell_in=s4, quality=q1),
            Item(name=self.NAMES[2], sell_in=s4, quality=q2),
            Item(name=self.NAMES[2], sell_in=s4, quality=q3),
            Item(name=self.NAMES[2], sell_in=s4, quality=q4)
        ]

        self.runTest(days, itemsExpected, itemsProcessed)



    def testAnythingElse(self):
        days = 2

        s1 = 0
        s2 = 1

        q1 = 0
        q2 = 1
        q3 = 2

        itemsProcessed = [
            Item(name=self.NAMES[3], sell_in=s1, quality=q1),
            Item(name=self.NAMES[3], sell_in=s2, quality=q1),
            Item(name=self.NAMES[3], sell_in=s1, quality=q2),
            Item(name=self.NAMES[3], sell_in=s2, quality=q2),
            Item(name=self.NAMES[3], sell_in=s1, quality=q2),
            Item(name=self.NAMES[3], sell_in=s2, quality=q3)
        ]

        itemsExpected = [
            Item(name=self.NAMES[3], sell_in=-1, quality=0),
            Item(name=self.NAMES[3], sell_in=0, quality=-0),
            Item(name=self.NAMES[3], sell_in=-1, quality=0),
            Item(name=self.NAMES[3], sell_in=0, quality=0),
            Item(name=self.NAMES[3], sell_in=-1, quality=0),
            Item(name=self.NAMES[3], sell_in=0, quality=2)
        ]

        self.runTest(days, itemsExpected, itemsProcessed)

    def runTest(self, days, itemsExpected, itemsProcessed):
        for i in range(1, days):
            GildedRoseJosep(itemsProcessed).updateQuality()

            for j in range(len(itemsExpected) - 1):
                if itemsExpected[j].quality != itemsProcessed[j].quality or \
                        itemsExpected[j].sell_in != itemsProcessed[j].sell_in:
                    print("------ Day: " + i.__str__() + " ------")
                    print("------ Item: " + j.__str__() + " ------")
                    print("Item expected:" + itemsExpected[j].__repr__())
                    print("Item processed:" + itemsProcessed[j].__repr__())
                    self.assertEqual(itemsExpected[j].quality, itemsProcessed[j].quality)
                    self.assertEqual(itemsExpected[j].sell_in, itemsProcessed[j].sell_in)


if __name__ == '__main__':
    unittest.main()
