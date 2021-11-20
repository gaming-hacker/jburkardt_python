#! /usr/bin/env python3
#
def duel_many_test ( ):

#*****************************************************************************80
#
## duel_many_test() tests duel_simulation() many times, and averages results.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'duel_many_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Repeatedly simulate a duel between combatants' )
  print ( '  who fire alternately at each other, with known probabilities' )
  print ( '  of hitting the other.' )
  
  p = np.array ( [ 0.10, 0.15 ] )

  duel_num = 1000
 
  print ( '' )
  print ( '  In this example, the one shot probabilities are:' )
  print ( '  Player[0]: %g' % ( p[0] ) )
  print ( '  Player[1]: %g' % ( p[1] ) )
  print ( '' )
  print ( '  The number of duels to fight is %d' % ( duel_num ) )

  s, turn_average = duel_simulation ( p, duel_num )

  print ( '' )
  print ( '  Result of the duels:' )
  for player in range ( 0, 2 ):
    print ( '  Player %d winning percentage is %g' % ( player, s[player] ) )

  print ( '' )
  print ( '  The average number of shots fired was %g' % ( turn_average ) )

  return

def duel_once ( p ):

#*****************************************************************************80
#
## duel_once() returns the outcome of a single duel.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Martin Shubik,
#    "Does the Fittest Necessarily Survive?",
#    in Readings in Game Theory and Political Behavior,
#    edited by Martin Shubik,
#    Doubleday, 1954,
#    LC: H61.S53.
#
#  Input:
#
#    real P(2), the probabilities that player I will hit an opponent
#    in a single shot.  Each P(I) should be between 0 and 1.
#
#  Output:
#
#    integer SURVIVOR, the survivor of the duel.
#
  import numpy as np

  turn_num = 0
 
  while ( True ):
#
#  Player 1 fires.
#
    turn_num = turn_num + 1
    r = np.random.rand ( )
    if ( r <= p[0] ):
      survivor = 0
      break
#
#  Player 2 fires.
#
    turn_num = turn_num + 1
    r = np.random.rand ( )
    if ( r <= p[1] ):
      survivor = 1
      break

  return survivor, turn_num

def duel_once_test ( ):

#*****************************************************************************80
#
## duel_once_test() tests duel_once().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'duel_once_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  duel_once simulates a single duel between combatants' )
  print ( '  who fire alternately at each other, with known probabilities' )
  print ( '  of hitting the other.' )
  
  p = np.array ( [ 0.10, 0.15 ] )
 
  print ( '' )
  print ( '  In this example, the one shot probabilities are:' )
  print ( '  Player[0]: %g' % ( p[0] ) )
  print ( '  Player[1]: %g' % ( p[1] ) )

  survivor, turn_num = duel_once ( p )

  print ( '' )
  print ( '  Result of this duel:' )
  print ( '  Player %d survived after %d turns' % ( survivor, turn_num ) )

  return

def duel_simulation ( p, duel_num ):

#*****************************************************************************80
#
## duel_simulation() simulates a duel.
#
#  Discussion:
#
#    Player 1 fires at player 2, and hits with a probability of P(1).
#    If Player 2 misses, then Player 2 fires at Player 1, hitting with
#    a probability of P(2).
#
#    The duel continues with alternating shots until only one player 
#    survives.
#
#    The simulation is intended to estimate the probabilities that a
#    player will survive, and the number of turns required.
#
#    The exact probability that player 1 will survive is
#
#      P(1) / ( P(1) + P(2) - P(1) * P(2) )
#
#    Player 2's chance is
#
#     P(2) * ( 1 - P(1) ) / ( P(1) + P(2) - P(1) * P(2) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Nahin,
#    Duelling Idiots and Other Probability Puzzlers,
#    Princeton University Press, 2000,
#    ISBN13: 978-0691009797,
#    LC: QA273.N29.
#
#    Martin Shubik,
#    "Does the Fittest Necessarily Survive?",
#    in Readings in Game Theory and Political Behavior,
#    edited by Martin Shubik,
#    Doubleday, 1954,
#    LC: H61.S53.
#
#  Input:
#
#    real P(2), the probabilities that player I will hit an opponent
#    in a single shot.  Each P(I) should be between 0 and 1.
#
#    integer DUEL_NUM, the number of duels to run.
#
#  Output:
#
#    real S(2), the estimated probablity that player I will survive.
#
#    real TURN_AVERAGE, the average number of turns required to
#    complete the duel.
#
  import numpy as np

  s = np.zeros ( 2 )
  turn_average = 0

  for duel in range ( 0, duel_num ):
    survivor, turn_num = duel_once ( p )
    s[survivor] = s[survivor] + 1
    turn_average = turn_average + turn_num

  s = s / float ( duel_num )
  turn_average = turn_average / float ( duel_num )

  return s, turn_average

def duel_simulation_test ( ):

#*****************************************************************************80
#
## duel_simulation_test() tests duel_simulation().
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
  print ( 'duel_simulation_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test duel_simulation()' )

  duel_once_test ( )
  duel_many_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'duel_simulation_test' )
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
  duel_simulation_test ( )
  timestamp ( )
 
