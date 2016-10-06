#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Random choice
"""
# end_pymotw_header

import random
import itertools

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')


def new_deck():
    return list(itertools.product(
        itertools.chain(xrange(2, 11), FACE_CARDS),
        SUITS,
    ))


SUITS_PAIR = ('H', 'D', 'C', 'S')


def new_fiver():
    return list(itertools.product(
        SUITS_PAIR,
        itertools.chain(xrange(2, 4), xrange(6, 10))

    ))


def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print '%2s%s' % j,
        print


def show_fiver(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:6]
        p_deck = p_deck[6:]
        for j in row:
            print '%2s%s' % j,
        print


# Make a new deck, with the cards in order
deck = new_deck()
dec_fiver = new_fiver()
print 'Initial deck:'
show_fiver(dec_fiver)

# Shuffle the deck to randomize the order
random.shuffle(dec_fiver)
print '\nShuffled deck:'
show_fiver(dec_fiver)

# Deal 4 hands of 5 cards each
hands = [[], [], [], []]

for i in xrange(3):
    for h in hands:
        h.append(dec_fiver.pop())

# Show the hands
print '\nHands:'
for n, h in enumerate(hands):
    print '%d:' % (n + 1),
    for c in h:
        print '%2s%s' % c,
    print

# Show the remaining deck
print '\nRemaining deck:'
show_fiver(dec_fiver)
