class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def increaseQuality(self):
        self.quality = min(49, self.quality + 1)

    def decreaseQuality(self):
        self.quality = max(0, self.quality - 1)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)