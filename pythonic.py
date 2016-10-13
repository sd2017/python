import logging
import unittest

# class trying(unittest.TestCase):
#    def test_pass(self):
#         logging.getLogger('hide.this').info('HIDE THIS')
#         logging.getLogger('show.this').info('TEST PASS')
#         self.assertEqual(True, True)
#
#     def test_fail(self):
#         logging.getLogger('hide.this').info('HIDE THIS')
#         logging.getLogger('show.this').info('TEST FAIL')
#         self.assertEqual(True, False)


import copy
def shallow_copy_same_members(existing_list):
  new_list = copy.copy(existing_list)



#On the rare occasions when you also want every item and attribute in the object to be separately
#copied, recursively, use deepcopy:
import copy
def deep_copy_clone_members(existing_list_of_dicts):
    new_list_of_dicts = copy.deepcopy(existing_list_of_dicts)


def test_list_comperhansion():
  theoldlist=[1,2,3,4]
  thenewlist = [x + 23 for x in theoldlist if x > 5]
  print thenewlist



#list access

def list_get(L, i, v=None):
  if -len(L) <= i < len(L): return L[i]
  else: return v

#Discussion
#The function in this recipe just checks whether i is a valid index by applying Python's indexing
#rule: valid indices are negative ones down to -len(L) inclusive, and non-negative ones up to
#len(L) exclusive. If almost all calls to list_get pass a valid index value for i, you might prefer an
#alternative approach:
def list_get_egfp(L, i, v=None):
    try: return L[i]
    except IndexError: return v




#function enumerate, which takes any iterable argument and returns an iterator yielding all the
#pairs (two-item tuples) of the form (index, item), one pair at a time. By writing your for loop's
#header clause in the form:
def iterate_with_index(sequence_in):
  sequence=sequence_in
  for index, item in enumerate(sequence):
    yield index,item


def transpose_using_list_compehension(arr):
    arr=[[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
    print [[r[col] for r in arr] for col in range(len(arr[0]))]





def test_dictionary_default_value():
    d=dict()
    print d,d.get('key', 'not found')


def dictionary_exception(d):
    try:
        print d['key']
    except KeyError:
        print 'not found'

#dictionary value is apended to list, first time empty list
def addword(theIndexDict, word, pagenumber):
    theIndexDict.setdefault(word, [ ]).append(pagenumber)


def test_addword():
    dict={}
    addword(dict,"guliver",78)
    addword(dict,"guliver",169)
    addword(dict,"liliput",9)
    addword(dict,"liliput",19)
    print dict


#counting dictionary
def dictInc(theIndexDict,word):
     theIndexDict[word] = theIndexDict.get(word, 0) + 1
def test_dictInc():
    dict={}
    dictInc(dict,"guliver")
    dictInc(dict,"guliver")
    dictInc(dict,"liliput")
    dictInc(dict,"liliput")
    print dict





def dictionary_initializing():
    data = dict(red=1, green=2, blue=3)
    #This is neater than the equivalent use of dictionary-display syntax:
    data = {'red': 1, 'green': 2, 'blue': 3}




def dictionary_initializing_from_sequences(the_keys_list,the_values_list):
 d = dict(zip(the_keys_list, the_values_list))


#large dictionary
import itertools
def dictionary_initializing_from_large_sequences(the_keys_list,the_values_list):
    d = dict(itertools.izip(the_keys_list, the_values_list))
    return d



import string
def dictionary_couting_initializing_with_value():
   count_by_letter = dict.fromkeys(string.ascii_lowercase, 0)
   print count_by_letter

#initializing dictionary from list of pairs
def pairwise(iterable):
    itnext = iter(iterable).next
    while True:
      yield itnext( ), itnext( )

def dictFromSequenceXY(seq):
    return dict(pairwise(seq))

def test_dictFromSequenceXY():
    seq = [2012, "obama", 2008, "boosh", 1996, "clinton", 1972, "nixon"]
    dict=dictFromSequenceXY(seq)
    print dict


#subdictionary
def sub_dict(somedict, somekeys, default=None):
    return dict([ (k, somedict.get(k, default)) for k in somekeys ])

def test_sub_dict():
    seq = [2012, "obama", 2008, "boosh", 1996, "clinton", 1972, "nixon"]
    dict=dictFromSequenceXY(seq)
    subdict=sub_dict(dict,[1972,2008,2012])
    print subdict



#If you want to remove from the original the items you're extracting:
def sub_dict_remove(somedict, somekeys, default=None):
   return dict([ (k, somedict.pop(k, default)) for k in somekeys ])

def test_sub_dict_remove():
    seq = [2012, "obama", 2008, "boosh", 1996, "clinton", 1972 ,"nixon"]
    dict=dictFromSequenceXY(seq)
    subdict=sub_dict_remove(dict,[1996,2008])
    print subdict


#inverting dictionary
def invert_small_dict(d):
  return dict([ (v, k) for k, v in d.iteritems( ) ])

#For large dictionaries, though, it's faster to use the generator izip from the itertools module in
#the Python Standard Library:
from itertools import izip
def invert_large_dict_fast(d):
  return dict(izip(d.itervalues( ), d.iterkeys( )))

def test_invert_large_dict_fast():
    seq = [2012, "obama", 2008, "boosh", 1996, "clinton"]
    dict=dictFromSequenceXY(seq)
    inverted_dict=invert_large_dict_fast(dict)
    print inverted_dict



def test_dictionary_string_function():
    animals = [ ]
    number_of_felines = 0

    def deal_with_a_cat( ):
        global number_of_felines
        print "meow"

    animals.append('feline')
    number_of_felines += 1

    def deal_with_a_dog( ):
        print "bark"

    animals.append('canine')

    def deal_with_a_bear( ):
        print "watch out for the *HUG*!"

    animals.append('ursine')
    tokenDict = {
    "cat": deal_with_a_cat,
    "dog": deal_with_a_dog,
    "bear": deal_with_a_bear,
    }

    # Simulate, say, some words read from a file
    words = ["cat", "bear", "cat", "dog"]
    for word in words:
     # Look up the function to call for each word, and call it
     print tokenDict[word]( )
    nf = number_of_felines
    print 'we met %d feline%s' % (nf, 's'[nf==1:])
    print 'the animals we met were:', ' '.join(animals)






def dictionary_intersection(dicta,dictb):
    inter = dict.fromkeys([x for x in dicta if x in dictb])
    return inter






if __name__=="__main__":
#    import nose
#    test=trying()
#    nose.run()
#nosetests -s -v   pythonic.py
  pass