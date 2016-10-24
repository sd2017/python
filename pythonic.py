import logging
#import unittest
import threading
import cStringIO, traceback




def process_txt_file(txt, oldfile, newfile):

    with  open(oldfile, 'r', encoding='utf-8') as infile, open(newfile, 'w') as outfile:
        for line in infile:
            if line.startswith(txt):
                line = line[0:len(txt)] + ' - Truly a great person!\n'
            outfile.write(line)


def process_all_files_trap_exceptions(all_filenames, fatal_exceptions=(KeyboardInterrupt, MemoryError)):
    bad_filenames = {}
    for one_filename in all_filenames:
        try:
            process_txt_file("searched line",one_filename,one_filename+"out")
        except fatal_exceptions:
               print 'error'
               raise
        except Exception:
            f = cStringIO.StringIO()
            traceback.print_exc(file=f)
            bad_filenames[one_filename] = f.getvalue()
    return bad_filenames

def test_process_all_files_trap_exceptions():
    filenames=["non_existing_file1" , "non_existing_file2"]
    ret=process_all_files_trap_exceptions(filenames)
    print ret.keys()
    assert(set(ret.keys())==set(filenames))

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

num=5
stringnum=str(num)

import copy
def shallow_copy_same_members(existing_list):
  new_list = copy.copy(existing_list)



#On the rare occasions when you also want every item and attribute in the object to be separately
#copied, recursively, use deepcopy:
import copy
def deep_copy_clone_members(existing_list_of_dicts):
    new_list_of_dicts = copy.deepcopy(existing_list_of_dicts)


def test_list_comperhansion():
  theoldlist=[1,2,3,4,4,5,6,7,6.5,5.5,4.5,3.5]
  thenewlist = [x + 100 for x in theoldlist if x > 5]
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




#If the number of items in dictionaries a and b can be very different, then it can be important for
#speed considerations to have the shorter one in the for clause, and the longer one in the if
#clause, of this list comprehension. In such cases, it may be worth sacrificing some conciseness in
#favor of speed, by coding the intersection computation as follows:
def dictionary_intersection(dicta,dictb):
    if len(dicta) < len(dictb):
        inter = dict.fromkeys([x for x in dicta if x not in dictb])
    else:
        inter = dict.fromkeys([x for x in dictb if x not in dicta])

def test_sub_dict_remove():
        seq = {2012, "obama", 2008, "boosh", 1996, "clinton"}
        dict = dictFromSequenceXY(seq)
        subdict = sub_dict_remove(dict, [1996])
        subdict[1972]="nixon"
        print subdict



def dictionary_keys_intersection(dict_phones,dict_addresses):
    for name in set(dict_phones) & set(dict_addresses):
        print name, dict_phones[name], dict_addresses[name]


def dictionary_keys_intersection(seqa,seqb):
    seqa = {1960,"kenedy",1996, "clinton", 2008, "boosh", 2012, "obama"}
    seqb= {1940,"democrats",1972,"republicans", 2008, "republicans", 2012, "democrats"}
    dicta = dictFromSequenceXY(seqa)
    dictb = dictFromSequenceXY(seqb)
    dictionary_keys_intersection(dicta, dictb)

def test_dictionary_keys_intersection():
    assert(False)
#probability
import random
def random_pick(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item


def test_random_pick():
    lista=list()
    for i in range (0,10):
         lista.append(random_pick([1   ,2   ,3   ,4   ,5   ,6   ,7   ,8   ,9  ,10],
                                  [0.05,0.02,0.03,0.15,0.35,0.01,0.01,0.18,0.1,0.1]))
    print lista


#random picks  with weight
import random
def random_picks_weight(sequence, relative_odds):
    table = [ z for x, y in zip(sequence, relative_odds) for z in [x]*y ]
    while True:
        yield random.choice(table)

import itertools
def test_random_picks_weight():
  x = random_picks_weight('ciao', [1, 1, 3, 2])
  list_two_chars=list()
  for two_chars in zip('boo', x):
       list_two_chars.append(''.join(two_chars))
  print list_two_chars
  print ''.join(itertools.islice(x, 20))
#bc oa oa

#icacaoco



#module check name simbol
# import _ _builtin_ _
# def ensureDefined(name, defining_code, target=_ _builtin_ _):
#     if not hasattr(target, name):
#         d = { }
#         exec defining_code in d
#         assert name in d, 'Code %r did not set name %r' % (defining_code, name)
#         setattr(target, name, d[name])


#sort dictionary
def sortedDictValues(adict):
    keys = adict.keys( )
    keys.sort( )
    return [adict[key] for key in keys]


#sort case insensitive
def case_insensitive_sort_1(string_list):
    def compare(a, b): return cmp(a.lower( ), b.lower( ))
    string_list.sort(compare)

def test_case_insensitive_sort_1():
    string_list=["kennedy","Truman","nixson","roozvelt","Raigen","Ford","Obama","boosh"]
    print case_insensitive_sort_1(string_list)


#yield return one element , next time function is called , next element will be return
def flatten(nested):
  for sublist in nested:
    for element in sublist:
      yield element

def test_flatten():
    nested = [[1, 2], [3, 4], [5]]
    flatten(nested)
    for num in flatten(nested):
        print num



#heap
#import heapq
#    heapq.heapify(the_list)



#priority Q
class prioq(object):
    def __init__(self):
        self.q = [ ]
        self.i = 0
    def push(self, item, cost):
        heapq.heappush(self.q, (-cost, self.i, item))
        self.i += 1
    def pop(self):
        return heapq.heappop(self.q)[-1]


#top 10
import heapq
def top10(data):
    return heapq.nsmallest(10, data)



#search in sorted list
import bisect
def bisect(L,x):
    x_insert_point = bisect.bisect_right(L, x)
    x_is_present = L[x_insert_point-1:x_insert_point] == [x]


#qsort
def qsort(L):
    if len(L) <= 1: return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] + \
                qsort([ge for ge in L[1:] if ge >= L[0]])





import marshal
def serializing_primitive():
    data = {12:'twelve', 'feep':list('ciao'), 1.23:4+5j, (1,2,3):u'wer'}
    bytes = marshal.dumps(data)
#You can now sling bytes around as you wish (e.g., send it across a network, put it as a BLOB in
#a database, etc.), as long as you keep its arbitrary binary bytes intact. Then you can reconstruct
#the data structure from the bytestring at any time:
    redata = marshal.loads(bytes)





import cPickle
def serializing_non_primitive(data):
    text = cPickle.dumps(data)
    #or to a binary string, a choice that is faster and takes up less space:
    bytes = cPickle.dumps(data, 2)
    #You can now sling text or bytes around as you wish (e.g., send across a network, include as a
    #BLOB in a databasesee Recipe 7.10, Recipe 7.11, and Recipe 7.12) as long as you keep text or
    #bytes intact. In the case of bytes, it means keeping the arbitrary binary bytes intact. In the case
    #of text, it means keeping its textual structure intact, including newline characters. Then you can
    #reconstruct the data at any time, regardless of machine architecture or Python release:
    readata1 = cPickle.loads(text)
    readata2 = cPickle.loads(bytes)
    print readata1
    print readata2

#serialize and compress
import cPickle, gzip
def save(filename, *objects):
    ''' save objects into a compressed diskfile '''
    fil = gzip.open(filename, 'wb')
    for obj in objects: cPickle.dump(obj, fil, proto=2)
    fil.close( )

def load(filename):
    ''' reload objects from a compressed diskfile '''
    fil = gzip.open(filename, 'rb')
    while True:
        try: yield cPickle.load(fil)
        except EOFError: break
    fil.close( )




#print DB by row name
def fields(cursor):
    """ Given a DB API 2.0 cursor object that has been executed, returns
    a dictionary that maps each field name to a column index, 0 and up. """
    results = { }
    for column, desc in enumerate(cursor.description):
        results[desc[0]] = column
    return results




def prety_print_database(cursor, data=None, check_row_lengths=False):
    if not data:
        data = cursor.fetchall( )
    names = [ ]
    lengths = [ ]
    rules = [ ]
    for col, field_description in enumerate(cursor.description):
        field_name = field_description[0]
        names.append(field_name)
        field_length = field_description[2] or 12
        field_length = max(field_length, len(field_name))
        if check_row_lengths:
            # double-check field length, if it's unreliable
            data_length = max([ len(str(row[col])) for row in data ])
            field_length = max(field_length, data_length)
            lengths.append(field_length)
            rules.append('-' * field_length)
    format = " ".join(["%%-%ss" % l for l in lengths])
    result = [ format % tuple(names), format % tuple(rules) ]
    for row in data:
        result.append(format % tuple(row))
    return "\n".join(result)


def test_prety_print_database(cursor, data=None, check_row_lengths=False):
    prety_print_database(cursor, data, False)
    raise












#debug util
import sys, traceback
traceOutput = sys.stdout
watchOutput = sys.stdout
rawOutput = sys.stdout
    # calling 'watch(secretOfUniverse)' prints out something like:
    # File "trace.py", line 57, in _ _testTrace
    # secretOfUniverse <int> = 42
watch_format = ('File "%(fileName)s", line %(lineNumber)d, in'
        ' %(methodName)s\n %(varName)s <%(varType)s>'
        ' = %(value)s\n\n')
def watch(variableName):
    if __debug__:
        stack = traceback.extract_stack( )[-2:][0]
        actualCall = stack[3]
        if actualCall is None:
            actualCall = "watch([unknown])"
            left = actualCall.find('(')
            right = actualCall.rfind(')')
            paramDict = {} # dict(varName=actualCall[left+1:right]).strip( ),varType=str(type(variableName))[7:-2],value=repr(variableName),methodName=stack[2],lineNumber=stack[1],fileName=stack[0])
        watchOutput.write(watch_format % paramDict)
    # calling 'trace("this line was executed")' prints out something like:
    # File "trace.py", line 64, in ?
    # this line was executed
    trace_format = ('File "%(fileName)s", line %(lineNumber)d, in'
    ' %(methodName)s\n %(text)s\n\n')
def trace(text):
    if __debug__:
        stack = traceback.extract_stack( )[-2:][0]
    paramDict = dict(text=text,
    methodName=stack[2],
    lineNumber=stack[1],
    fileName=stack[0])
    watchOutput.write(trace_format % paramDict)
# calling 'raw("some raw text")' prints out something like:
# Just some raw text
def raw(text):
    if __debug__:
        rawOutput.write(text)



# #traceback
# import sys, traceback
# def print_exc_plus( ):
# """ Print the usual traceback information, followed by a listing of
# all the local variables in each frame.
# """
#     tb = sys.exc_info( )[2]
#     while tb.tb_next:
#     tb = tb.tb_next
#     stack = [ ]
#     f = tb.tb_frame
# while f:
# stack.append(f)
# f = f.f_back
# stack.reverse( )
# traceback.print_exc( )
# print "Locals by frame, innermost last"
# for frame in stack:
# print
# print "Frame %s in %s at line %s" % (frame.f_code.co_name,
# frame.f_code.co_filename,
# frame.f_lineno)
# for key, value in frame.f_locals.items( ):
# print "\t%20s = " % key,
# # we must _absolutely_ avoid propagating exceptions, and str(value)
# # COULD cause any exception, so we MUST catch any...:
# try:
# print value
# except:
# print "<ERROR WHILE PRINTING VALUE>"
#
#
#
# #start debugger on exception
# # code snippet to include in your sitecustomize.py
# import sys
# def info(type, value, tb):
# if hasattr(sys, 'ps1') or not (
# sys.stderr.isatty( ) and sys.stdin.isatty( )
# ) or issubclass(type, SyntaxError):
# # Interactive mode, no tty-like device, or syntax error: nothing
# # to do but call the default hook
# sys._ _excepthook_ _(type, value, tb)
# else:
# import traceback, pdb
# # You are NOT in interactive mode; so, print the exception...
# traceback.print_exception(type, value, tb)
# print
# # ...then start the debugger in post-mortem mode
# pdb.pm( )
# sys.excepthook = info
#
#
#
#
# #doc test
# >>> import toy
# >>> toy.add('a', 'b')
# 'ab'
# >>> toy.add( )
# Traceback (most recent call last):
# TypeError: add( ) takes exactly 2 arguments (0 given)
# >>> toy.add(1, 2, 3)
# Traceback (most recent call last):
# TypeError: add( ) takes exactly 2 arguments (3 given)
# and add at the end of toy.py a few more lines:
# import unittest
# suite = doctest.DocFileSuite('test_toy.txt')
# unittest.TextTestRunner( ).run(suite)
#
#
#
# #threadpool
# import threading, Queue, time, sys
# # Globals (start with a capital letter)
# Qin = Queue.Queue( )
# Qout = Queue.Queue( )
# Qerr = Queue.Queue( )
# Pool = [ ]
# def report_error( ):
# ''' we "report" errors by adding error information to Qerr '''
#     Qerr.put(sys.exc_info( )[:2])
# def get_all_from_queue(Q):
# ''' generator to yield one after the others all items currently
# in the Queue Q, without any waiting
# '''
#     try:
#     while True:
#         yield Q.get_nowait( )
#     except Queue.Empty:
#     raise StopIteration
# def do_work_from_queue( ):
# ''' the get-some-work, do-some-work main loop of worker threads '''
#     while True:
#         command, item = Qin.get( ) # implicitly stops and waits
#         if command == 'stop':
#     break
#     try:
#         # simulated work functionality of a worker thread
#     if command == 'process':
#         result = 'new' + item
#     else:
#         raise ValueError, 'Unknown command %r' % command
#     except:
#     # unconditional except is right, since we report _all_ errors
#     report_error( )
#     else:
#     Qout.put(result)
# def make_and_start_thread_pool(number_of_threads_in_pool=5, daemons=True):
# ''' make a pool of N worker threads, daemonize, and start all of them '''
#     for i in range(number_of_threads_in_pool):
#     new_thread = threading.Thread(target=do_work_from_queue)
#     new_thread.setDaemon(daemons)
#     Pool.append(new_thread)
#     new_thread.start( )
# def request_work(data, command='process'):
#     ''' work requests are posted as (command, data) pairs to Qin '''
#     Qin.put((command, data))
#     def get_result( ):
# return Qout.get( ) # implicitly stops and waits
# def show_all_results( ):
#     for result in get_all_from_queue(Qout):
#     print 'Result:', result
# def show_all_errors( ):
#     for etyp, err in get_all_from_queue(Qerr):
#     print 'Error:', etyp, err
# def stop_and_free_thread_pool( ):
#     # order is important: first, request all threads to stop...:
#     for i in range(len(Pool)):
#     request_work(None, 'stop')
#     # ...then, wait for each of them to terminate:
#     for existing_thread in Pool:
#     existing_thread.join( )
#     # clean up the pool from now-unused thread objects
#     del Pool[:]
#
#
#
#
# #multi threading on io function
#
# import threading, time, Queue
# class MultiThread(object):
# def _ _init_ _(self, function, argsVector, maxThreads=5, queue_results=False):
#     self._function = function
#     self._lock = threading.Lock( )
#     self._nextArgs = iter(argsVector).next
#     self._threadPool = [ threading.Thread(target=self._doSome)
#     for i in range(maxThreads) ]
#     if queue_results:
#     self._queue = Queue.Queue( )
#     else:
#     self._queue = None
#     def _doSome(self):
#     while True:
#     self._lock.acquire( )
#     try:
#     try:
#     args = self._nextArgs( )
#     except StopIteration:
#     break
#     finally:
#     self._lock.release( )
#     result = self._function(args)
#     if self._queue is not None:
#     self._queue.put((args, result))
# def get(self, *a, **kw):
#     if self._queue is not None:
#     return self._queue.get(*a, **kw)
#     else:
#     raise ValueError, 'Not queueing results'
# def start(self):
#     for thread in self._threadPool:
#     time.sleep(0) # necessary to give other threads a chance to run
#     thread.start( )
#     def join(self, timeout=None):
#     for thread in self._threadPool:
#     thread.join(timeout)
#     if _ _name_ _=="_ _main_ _":
# import random
# def recite_n_times_table(n):
#     for i in range(2, 11):
#     print "%d * %d = %d" % (n, i, n * i)
#     time.sleep(0.3 + 0.3*random.random( ))
#     mt = MultiThread(recite_n_times_table, range(2, 11))
#     mt.start( )
#     mt.join( )
#     print "Well done kids!"
#
#
#
#
# #messege passing
# import candygram as cg
# class ExampleThread(object):
#     """A thread-class with just a single counter value and a stop flag."""
#     def _ _init_ _(self):
#     """ Initialize the counter to 0, the running-flag to True. """
#         self.val = 0
#         self.running = True
#     def increment(self):
#     """ Increment the counter by one. """
#         self.val += 1
#     def sendVal(self, msg):
#     """ Send current value of counter to requesting thread. """
#         req = msg[0]
#         req.send((cg.self( ), self.val))
#     def setStop(self):
#     """ Set the running-flag to False. """
#         self.running = False
#     def run(self):
#         """ The entry point of the thread. """
#         # Register the handler functions for various messages:
#         r = cg.Receiver( )
#         r.addHandler('increment', self.increment)
#         r.addHandler((cg.Process, 'value'), self.sendVal, cg.Message)
#         r.addHandler('stop', self.setStop)
#         # Keep handling new messages until a stop has been requested
#         while self.running:
#             r.receive( )
#         #To start a thread running this code under candygram, use:
#         counter = cg.spawn(ExampleThread( ).run)
#
#
#
#
# #thread dictionary
# try:
# import threading
# except ImportError:
# import dummy_threading as threading
# _tss = threading.local( )
# def get_thread_storage( ):
#     return _tss._ _dict_ _
#
#
# #running programs
# import os
#     f = os.popen('gnuplot', 'w')
#     print >>f, "set yrange[-300:+300]"
#     for n in range(300):
#       print >>f, "plot %i*cos(x)+%i*log(x+10)" % (n, 150-n)
#     f.flush( )
#     f.close( )
#
#
#
#
#
# #make exe compiling py
# from distutils.core import setup
# import sys, os, py2exe
# # the key trick with our arguments and Python's sys.path
# name = sys.argv[1]
# sys.argv[1] = 'py2exe'
# sys.path.append(os.path.dirname(os.path.abspath(name)))
# setup(name=name[:-3], scripts=[name])
# #Save this as makexe.py in the Tools\Scripts\ folder of your Python installation. (You should
# #always add this folder to your Windows PATH because it contains many useful tools.) Now, from a
# #Windows command prompt, you're able to cd to a directory where you have placed a script (say
# #C:\MyDir\), and there run, say:
# C:\MyDir> makexe.py myscript.py
#
#
# #linux python exe
# #!/bin/sh
# PYTHON=$(which python 2>/dev/null)
# if [ x ! -x "x$PYTHON" ] ; then
# echo "python executable not found - cannot continue!"
# exit 1
# fi
# exec $PYTHON - $0 $@ << END_OF_PYTHON_CODE
# import sys
# version = sys.version_info[:2]
# if version < (2, 3):
# print 'Sorry, need Python 2.3 or better; %s.%s is too old!' % version
# sys.path.insert(0, sys.argv[1])
# del sys.argv[0:2]
# import main
# main.main( )
# END_OF_PYTHON_CODE
#
#
# python web
# command = 'urllib2.urlopen(' + "'" + self.server_url + self.server_service_ir + self.server_index + key_string + "'" + ')\n'
#
#
#
# module
# import dir1.dir2.file   # ---> dir0 in search0    dir0/dir1/dir2/file.py   --- each dir contain empty __init__.py file
#
# tuple
# =====
# Operation Interpretation
# () An empty tuple
# t1 = (0,) A one-item tuple (not an expression)
# t2 = (0, 'Ni', 1.2, 3) A four-item tuple
# t2 = 0, 'Ni', 1.2, 3 Another four-item tuple (same as prior line)
# t3 = ('abc', ('def', 'ghi')) Nested tuples
# t1[i]
# t3[i][j]
# t1[i:j]
# len(t1)
# Index, index of index, slice, length
# t1 + t2
# t2 * 3
# Concatenate, repeat
# for x in t
# 'spam' in t2
# Iteration, membership
#
#
# #comparison , address comparison
# >>> L1 == L2, L1 is L2 # Equivalent? Same object?
# (True, False)
#
#
#
# Function Description
# chr(n) Returns a one-character string with ordinal n
# (0 <= n < 256)
# eval(source[, globals[, locals]]) Evaluates a string as an expression and returns
# the value
# enumerate(seq) Yields (index, value) pairs suitable for iteration
# ord(c) Returns the integer ordinal value of a onecharacter
# string
# range([start,] stop[, step]) Creates a list of integers
# reversed(seq) Yields the values of seq in reverse order, suitable
# for iteration
# sorted(seq[, cmp][, key][, reverse]) Returns a list with the values of seq in sorted order
# xrange([start,] stop[, step]) Creates an xrange object, used for iteration
# zip(seq1, seq2,...) Creates a new sequence suitable for parallel
# iteration
#
#







if __name__=="__main__":
    test_process_all_files_trap_exceptions()
    #import nose
    #test=trying()
    #nose.run()
    #nosetests -s -v   pythonic.py
