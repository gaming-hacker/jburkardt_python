#! /usr/bin/env python3
#
def average_length ( ):

#*****************************************************************************80
#
## average_length() estimates the average length of a one-player game.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 September 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'average_length' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Estimate the average length of a game of snakes and ladders.' )

  games = 0
  total = 0

  while ( games < 1000 ):
    games = games + 1
    n = game_length ( )
    total = total + n

  average = total / 1000
  print ( 'Average number of moves is %d' % ( average ) )

  print ( '' )
  print ( 'average_length' )
  print ( '  Normal end of execution.' )

  return

def game_length ( ):

#*****************************************************************************80
#
## game_length() plays a randomly selected game and returns the number of moves.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 September 2014.
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer S, the number of moves.
#
  import numpy as np

  from numpy.random import random_integers  
#
#  Set up the snakes and ladders.
#
  final = np.linspace ( 0, 100, 101, dtype = np.int32 )

  final[1]  =  38
  final[4]  =  14
  final[9]  =  31
  final[16] =   6
  final[21] =  42
  final[28] =  84
  final[36] =  44
  final[48] =  26
  final[49] =  11
  final[51] =  67
  final[56] =  53
  final[62] =  10
  final[64] =  60
  final[71] =  91
  final[80] = 100
  final[87] =  24
  final[93] =  73
  final[95] =  75
  final[98] =  78
#
#  Initial position is 0.
#
  i = 0
  s = 0
#
#  Play until you reach 100.
#
  while ( i < 100 ):
    s = s + 1
    d = random_integers ( 1, 6 )
    i = i + d
    if ( 100 < i ):
      i = 100
    i = final[i]

  return s

def game_length_test ( ):

#*****************************************************************************80
#
## game_length_test() tests game_length().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'game_length_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  game_length reports the length of a single random game of Snakes and Ladders.' )

  n = game_length ( )

  print ( '' )
  print ( '  This random game took %d moves.' % ( n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'game_length_test' )
  print ( '  Normal end of execution.' )

  return

def one_game ( ):

#*****************************************************************************80
#
## one_game() plays one game of Snakes and Ladders, printing every move.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from numpy.random import random_integers  
#
#  FINAL[I] indicates where you end up if your die roll takes you to square I.
#
  final = np.linspace ( 0, 100, 101, dtype = np.int32 )

  final[ 1] =  38
  final[ 4] =  14
  final[ 9] =  31
  final[16] =   6
  final[21] =  42
  final[28] =  84
  final[36] =  44
  final[48] =  26
  final[49] =  11
  final[51] =  67
  final[56] =  53
  final[62] =  10
  final[64] =  60
  final[71] =  91
  final[80] = 100
  final[87] =  24
  final[93] =  73
  final[95] =  75
  final[98] =  78
#
#  Initial position is 0.
#
  i = 0
  moves = 0
#
#  Play until you reach 100.
#
  while ( i < 100 ):
    d = random_integers ( 1, 6 )
    moves = moves + 1
    print ( 'You rolled %d ' % ( d ), end = '' )
    i = i + d
    print ( 'and moved to %d ' % ( i ), end = '' )
    if ( 100 < i ):
      i = 100
      print ( 'and moved back to %d ' % ( i ), end = '' )
    if ( i < final [ i ] ):
      i = final [ i ]
      print ( 'and took a ladder up to %d ' % ( i ), end = '' )
    elif ( final [ i ] < i ):
      i = final [ i ]
      print ( 'and took a snake down to %d' % ( i ), end = '' )

    if ( 100 <= i ):
      print ( 'and you won after %d moves!' % moves )
    else:
      print ( '.' )

  return

def snakes_and_ladders_test ( ):

#*****************************************************************************80
#
## snakes_and_ladders_test() tests snakes_and_ladders().
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
  print ( 'snakes_and_ladders_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test snakes_and_ladders()' )

  average_length ( )
  game_length_test ( )
  one_game ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'snakes_and_ladders_test:' )
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
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  snakes_and_ladders_test ( )
  timestamp ( )

