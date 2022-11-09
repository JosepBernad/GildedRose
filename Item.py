class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def increaseQuality(self):
        self.increaseQualityBy(1)

    def decreaseQuality(self):
        self.quality = max(0, self.quality - 1)

    def increaseQualityBy(self, n):
        self.quality = min(50, self.quality + n)

    def decreaseSellIn(self):
        self.sell_in = self.sell_in - 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)