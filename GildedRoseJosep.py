class GildedRoseJosep(object):

    def __init__(self, items):
        self.items = items

    def updateQuality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                item.increaseQuality()
                item.decreaseSellIn()
                if item.sell_in < 0:
                    item.increaseQuality()

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 6:
                    item.increaseQualityBy(3)
                elif item.sell_in < 11:
                    item.increaseQualityBy(2)
                else:
                    item.increaseQuality()
                item.decreaseSellIn()
                if item.sell_in < 0:
                    item.quality = 0

            elif item.name != "Sulfuras, Hand of Ragnaros":
                item.decreaseQuality()
                item.decreaseSellIn()
                if item.sell_in < 0:
                    item.decreaseQuality()
