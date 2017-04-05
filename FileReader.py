import sys
import Card

first = "Inputs/"

path = first+(sys.argv[1])

f = open(path, 'r')

deck = []

for line in f:
	c = line.split(',')
	deck.insert(0, Card.Card(c[0], c[1], c[2], c[3]))

print(deck)
