import csv
import json

def chunks(l, n):
  """Yield successive n-sized chunks from l."""
  for i in xrange(0, len(l), n):
    yield l[i:i+n]

decks = ['Standard']
result = {}
for deck in decks:
    path = 'data/{}.csv'.format(deck)
    with open(path) as f:
        reader = csv.reader(f)
        cards = list(reader)
    del cards[0]
    cards_by_level = {}
    levels = list(chunks(cards, 11))
    for level, cards in enumerate(levels):
        cards_hash = {}
        for card in cards:
            cards_hash[card[0]] = {
                'up': card[1],
                'right': card[2],
                'down': card[3],
                'left': card[4],
                'element': card[5]
            }
        cards_by_level[level+1] = cards_hash
    result[deck] = cards_by_level

path = 'data/database.json'
with open(path, 'w') as f:
    json.dump(result, f, indent=2, separators=(',', ': '))

