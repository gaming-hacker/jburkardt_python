#! /usr/bin/env python3
#
class ngram_score ( object ):

#*****************************************************************************80
#
## ngram_score() is a class for the ngram scoring program.
#
#  Modified:
#
#    30 August 2021
#
#  Author:
#
#    Unknown
#
  def __init__( self, ngramfile, sep = ' ' ):
    ''' load a file containing ngrams and counts, calculate log probabilities '''

    import numpy as np

    self.ngrams = {}
    fh = open ( ngramfile, 'rt' )
    for line in fh:
      key, count = line.split ( sep ) 
      self.ngrams[key] = int ( count )
    self.L = len ( key )
    self.N = sum ( self.ngrams.values() )
#
#  Calculate log probabilities.
#
    for key in self.ngrams.keys():
      self.ngrams[key] = np.log10 ( float ( self.ngrams[key]) / self.N )
    self.floor = np.log10 ( 0.01 / self.N )

  def score ( self, text ):
    ''' compute the score of text '''
    score = 0
    ngrams = self.ngrams.__getitem__
    for i in range ( len ( text ) - self.L + 1 ):
      if text[i:i+self.L] in self.ngrams: 
        score += ngrams ( text[i:i+self.L] )
      else:
        score += self.floor          
    return score

def ngram_score_test1 ( ):

#*****************************************************************************80
#
## ngram_score_test1() tests text against monogram statistics.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ngram_score_test1():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ngram_score() tests a string or text against English ngram statistics.' )
  print ( '  Here we do a test against English monograms.' )
  print ( '' )
  print ( '  Apparently, you want to remove all nonalphabetic information,' )
  print ( '  and uppercase your text.  But you may wish to preserve spaces.' )
  print ( '' )

  fitness = ngram_score ( '../../datasets/ngrams/english_monograms.txt' )
#
#  Notice that NGRAM_SCORE is affected by the case of the text,
#  by spaces, and by punctuation.
# 
  s = 'HELLOWORLD'
  score = fitness.score ( s )
  print ( '  %s length = %d, score = %g' % ( s, len ( s ), score ) )

  s = 'HELLO WORLD'
  score = fitness.score ( s )
  print ( '  %s length = %d, score = %g' % ( s, len ( s ), score ) )

  s = 'helloworld'
  score = fitness.score ( s )
  print ( '  %s length = %d, score = %g' % ( s, len ( s ), score ) )

  s = 'HELLO, WORLD!'
  score = fitness.score ( s )
  print ( '  %s length = %d, score = %g' % ( s, len ( s ), score ) )

  s = 'Hello, world!'
  score = fitness.score ( s )
  print ( '  %s length = %d, score = %g' % ( s, len ( s ), score ) )
#
#  Read text from a file.
#  Oddly enough, HELLOWORLD read from a file gives a different
#  score from HELLOWORLD entered as a string.  It seems to have
#  a terminating character.
#
  filename = 'HELLOWORLD.txt'
  file = open ( filename, 'r' )
  t = file.read ( )
  t = str.upper ( t )
  score = fitness.score ( t  )
  print ( '  %s length = %d, score = %g' % ( filename, len ( t ), score ) )
  file.close ( )
#
#  Read text from a file.
#
  filename = 'desiderata.txt'
  file = open ( filename, 'r' )
  t = file.read ( )
  t = str.upper ( t )
  score = fitness.score ( t  )
  print ( '  %s length = %d, score = %g' % ( filename, len ( t ), score ) )
  file.close ( )
#
#  Compare results for a file of the same length,
#  after rot13 operation.  Score should be much worse.
#
  filename = 'qrfvqrengn.gkg'
  file = open ( filename, 'r' )
  t = file.read ( )
  t = str.upper ( t )
  score = fitness.score ( t  )
  print ( '  %s length = %d, score = %g' % ( filename, len ( t ), score ) )
  file.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ngram_score_test1():' )
  print ( '  Normal end of execution.' )
  return

def ngram_score_test2 ( ):

#*****************************************************************************80
#
## ngram_score_test2() tests text against bigram statistics.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ngram_score_test2():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ngram_score() tests a string or text against English ngram statistics.' )
  print ( '  Here we do a test against English bigrams.' )
  print ( '' )
  print ( '  Apparently, you want to remove all nonalphabetic information,' )
  print ( '  and uppercase your text.  But you may wish to preserve spaces.' )
  print ( '' )

  fitness = ngram_score ( '../../datasets/ngrams/english_bigrams.txt' )
#
#  Notice that NGRAM_SCORE is affected by the case of the text,
#  by spaces, and by punctuation.
# 
  s = 'HELLOWORLD'
  score = fitness.score ( s )
  print ( '  %s length = %d, score = %g' % ( s, len ( s ), score ) )

  s = 'HELLO WORLD'
  score = fitness.score ( s )
  print ( '  %s length = %d, score = %g' % ( s, len ( s ), score ) )

  s = 'helloworld'
  score = fitness.score ( s )
  print ( '  %s length = %d, score = %g' % ( s, len ( s ), score ) )

  s = 'HELLO, WORLD!'
  score = fitness.score ( s )
  print ( '  %s length = %d, score = %g' % ( s, len ( s ), score ) )

  s = 'Hello, world!'
  score = fitness.score ( s )
  print ( '  %s length = %d, score = %g' % ( s, len ( s ), score ) )
#
#  Read text from the file "HELLOWORLD.txt".
#  Oddly enough, HELLOWORLD read from a file gives a different
#  score from HELLOWORLD entered as a string.  It seems to have
#  a terminating character.
#
  filename = 'HELLOWORLD.txt'
  file = open ( filename, 'r' )
  t = file.read ( )
  t = str.upper ( t )
  score = fitness.score ( t  )
  print ( '  %s length = %d, score = %g' % ( filename, len ( t ), score ) )
  file.close ( )
#
#  Read text from the file "desiderata.txt".
#
  filename = 'desiderata.txt'
  file = open ( filename, 'r' )
  t = file.read ( )
  t = str.upper ( t )
  score = fitness.score ( t  )
  print ( '  %s length = %d, score = %g' % ( filename, len ( t ), score ) )
  file.close ( )
#
#  Compare results for a file of the same length,
#  after rot13 operation.  Score should be much worse.
#
  filename = 'qrfvqrengn.gkg'
  file = open ( filename, 'r' )
  t = file.read ( )
  t = str.upper ( t )
  score = fitness.score ( t  )
  print ( '  %s length = %d, score = %g' % ( filename, len ( t ), score ) )
  file.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ngram_score_test2():' )
  print ( '  Normal end of execution.' )
  return

def ngrams_test ( ):

#*****************************************************************************80
#
## ngrams_test() tests ngrams().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2021
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ngrams_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test ngrams()' )

  ngram_score_test1 ( )
  ngram_score_test2 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ngrams_test():' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  ngrams_test ( )
  timestamp ( )

