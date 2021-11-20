#! /usr/bin/env python3
#
import random
import sys
 
def makerule ( data, context ):

#*****************************************************************************80
#
## makerule() makes a rule dict for the given data.
#
#  Discussion:
#
#    This function makes a rule for selecting the next word in a string,
#    based on usage patterns in a given input text.
#
  '''Make a rule dict for given data.'''
  rule = {}
  words = data.split ( ' ' )
  index = context

  for word in words[index:]:

    key = ' '.join(words[index-context:index])

    if key in rule:
      rule[key].append(word)
    else:
      rule[key] = [word]

    index = index + 1
 
    return rule
  
def makestring ( rule, length ):  

#*****************************************************************************80
#
## makestring() makes a string using the given rule.
#
#  Discussion:
#
#    This function generates a string of LENGTH words, using a specified rule.

#
#  Choose a set of starting words at random.
#
  oldwords = random.choice ( list(rule.keys())).split(' ')
  string = ' '.join(oldwords) + ' '
 
  for i in range ( length ):

    try:
      key = ' '.join(oldwords)
      newword = random.choice(rule[key])
      string = string + newword + ' '
 
      for word in range(len(oldwords)):
        oldwords[word] = oldwords[(word + 1) % len(oldwords)]
      oldwords[-1] = newword
 
    except KeyError:
      return string

  return string

def markov_text_test():

  print ( "" )
  print ( "markov_text_test():" )
  print ( "  markov_text() uses Markov methods to imitate a given text." )

  filename = sys.argv[1]
  with open ( filename, encoding = 'utf8' ) as file:
    data = file.read()

  context = int ( sys.argv[2] )
  rule = makerule ( data, context )

  length = int ( sys.argv[3] )
  string = makestring ( rule, length )

  print ( string )

if __name__ == '__main__':
  markov_text_test ( )

