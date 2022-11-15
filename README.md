# Josep Bernad's Gilded Rose resolution

This is the python version of the Gilded Rose, and its original repository can be found [here](https://github.com/emilybache/GildedRose-Refactoring-Kata).

## 1. Initial analysis

In order to have a deep understanding of the code, I highlighted the different properties of the object ``Item`` that are being evaluated in the `ìf` statements. After this step, I was able to notice that there weren't too many values that were considered in the different evaluations.

```name```:
- _"Aged Brie"_
- _"Backstage passes to a TAFKAL80ETC concert"_
- _"Sulfuras, Hand of Ragnaros"_
- Any other string

```quality```:
- ```> 0```
- ```< 50```

```sell_in```:
- ```< 11```
- ```< 6```
- ```< 0```

I noticed as well that there weren't too many operations (actions) to execute in the ```if``` statements:
- ```quality -= 1``` (if quality wasn't lower than 0)
- ```quality += 1``` (if quality wasn't bigger than 50)
- ```sell_in -= 1```
- ```quality = 0```


Finally, I divided the code in three big blocks in order to try to see what could be simplified. 

The final code with all the visual comments:

![Initial code analysis](./img/InitialCode.png)

## 2. The first attempt

Using all the information from the code with my comments, the first strategy I came out with was to trace all the values that every property had to have in order to execute each action.
The result can be seen in the next image:

![Code ](./img/FirstAttempt-1.png)

After this exercise, I tried to merge and simplify the different actions into only one, having this result:

![Code ](./img/FirstAttempt-2.png)

It didn't take me too much time to realize that this was not a good strategy, but I had some initial conclusions that for sure helped me later on.

## 3. Still no solution but new ideas

The solution was still out of my reach, but I had many ideas and data to keep working:
- I could start dividing the problem by the ```name``` property, that should simplify the code.
- We know that every time the ```quality``` property is increased or decreased, it's previously checked, so it is in the range ```[0, 50]```.
- To simplify even more the code, I had to get rid of as many nested levels as possible. Additionally, I had to create as many ```ìf elif else``` structures as possible, so the flow path was clear and easy to understand.

## 4. How can I test it? Part I

I wanted to be as agile as possible to check my solutions so the first solution I came out with was to compare it with the output of the original ```gilded_rose``` output.
Great, I had a reliable source of valid output to compare to, but... which initial values do I need?

For a quick and dirty solution I basically made all the possible combinations between ```name```, ```quality```, and ```sell_in```.
The first property had to be one of the four values discussed on the first chapter ```{"Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros" and ""}``` and the values of ```quality``` and ```sell_in``` were all the values in the range of ```[-100, 100]```.

This setup created a test set of:

$$$$