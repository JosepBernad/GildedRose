class Item:
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def increaseQuality(self):
        if self.quality < self.MAX_QUALITY:
            self.quality += 1

    def decreaseQuality(self):
        if self.quality > self.MIN_QUALITY:
            self.quality -= 1

    def increaseQualityBy(self, n):
        for i in range(0, n):
            self.increaseQuality()

    def decreaseSellIn(self):
        self.sell_in -= 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)