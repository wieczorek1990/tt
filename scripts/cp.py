import json
import shutil

colors = ['red', 'blue']
corrects = {
  "Doomtrain": "Doom Train",
  "Biggs, Wedge": "Wedge, Biggs"
}
path = 'data/database.json'
decks = json.load(open(path))

for deck_name, deck in decks.iteritems():
    for level, cards in deck.iteritems():
        if len(cards) != 11:
            raise Exception('Each level must have 11 cards')
        for card in cards.keys():
            filename = ''
            if card in corrects:
                filename = card + '.jpg'
                card = corrects[card]
            for color in colors:
                src = "decks/{color}/{card}.jpg".format(color=color, card=card)
                dst = "cards/{deck_name}/{color}/{level}/{filename}".format(
                    deck_name=deck_name, color=color, level=level, filename=filename)
                shutil.copy(src, dst)

