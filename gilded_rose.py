def increaseValue(n):
    return min(49, n + 1)


def decreaseValue(n):
    return max(0, n - 1)


class GildedRose(object):
    def __init__(self, items):
        self.A = "Aged Brie"
        self.B = "Backstage passes to a TAFKAL80ETC concert"
        self.C = "Sulfuras, Hand of Ragnaros"

        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == self.A:
                item.sell_in -= 1
                item.quality = increaseValue(item.quality)
                if item.sell_in < 0:
                    item.quality = increaseValue(item.quality)

            elif item.name == self.B:
                item.sell_in -= 1
                item.quality = increaseValue(item.quality)
                if item.sell_in < 0:
                    item.quality = 0

            elif item.name != self.C:
                item.sell_in -= 1
                item.quality = decreaseValue(item.quality)
                if item.sell_in < 0:
                    item.quality = decreaseValue(item.quality)

            # ----

            if item.name == self.A or item.name == self.B:
                # item.quality = increaseValue(item.quality)
                if item.sell_in < 11:
                    item.quality = increaseValue(item.quality)
                if item.sell_in < 6:
                    item.quality = increaseValue(item.quality)
            # elif item.name != self.C:
            # item.quality = decreaseValue(item.quality)
            '''
            # ----

            #if item.sell_in < 0:
                #if item.name == self.A:
                    #item.quality = increaseValue(item.quality)
                #elif item.name == self.B:
                    #item.quality = 0
                #elif item.name != self.C:
                    #item.quality = decreaseValue(item.quality)

            
            if item.name != self.A and item.name != self.B:
                if item.quality > 0 and item.name != self.C:
                    item.quality = item.quality - 1  # !A, !B, q > 0, !C
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1  # (A | B), q < 50
                    if item.name == self.B:
                        if item.sell_in < 11 and item.quality < 50:
                            item.quality = item.quality + 1  # B, s < 11, q < 49
                        if item.sell_in < 6 and item.quality < 50:
                            item.quality = item.quality + 1  # B, s < 6, q < 48

            # ----

            if item.name != self.C:
                item.sell_in = item.sell_in - 1

            # ----


            if item.sell_in < 0:
                if item.name != self.A:
                    if item.name != self.B:
                        if item.quality > 0 and item.name != self.C:
                            item.quality = item.quality - 1  # s < 0, !A, !B, !C, q > 0
                    else:
                        item.quality = item.quality - item.quality   # s < 0, B
                elif item.quality < 50:
                    item.quality = item.quality + 1   # s < 0, A
            '''


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
