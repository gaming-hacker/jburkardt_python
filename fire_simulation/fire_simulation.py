#! /usr/bin/env python3
#
UNBURNT = 0
SMOLDERING = 1
BURNING = 2
BURNT = 3

def fire_simulation ( forest_size, prob_spread ):

#*****************************************************************************80
#
## fire_simulation() simulates a fire in a rectangular forest of trees.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    Python version by John Burkardt
#
#  Input:
#
#    integer FOREST_SIZE, the number of trees in a horizontal
#    or vertical line.
#
#    real PROB_SPREAD, the probability that a burning tree will
#    ignite a neighboring tree.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fire_simulation' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  A probabilistic simulation of a forest fire.' )
  print ( '  The forest is a square grid with %d trees on a side.' % ( forest_size ) )
  print ( '  The probability of tree-to-tree spread is %g' % ( prob_spread ) )
#
#  Initialize the values in the forest.
#
  forest = forest_initialize ( forest_size )
#
#  Choose a tree at random where the fire will start.
#
  i_ignite = np.random.random_integers ( 0, forest_size - 1 )
  j_ignite = np.random.random_integers ( 0, forest_size - 1 )
  forest = tree_ignite ( forest_size, forest, i_ignite, j_ignite )

  print ( '' )
  print ( '  Fire starts at tree[%d,%d]' % ( i_ignite, j_ignite ) )
#
#  Let time run until nothing is burning any more.
#
  while ( forest_is_burning ( forest_size, forest ) ):
    forest = forest_burns ( forest_size, forest, prob_spread )
#
#  Display the final forest state.
#
  forest_print ( forest_size, forest, i_ignite, j_ignite )
#
#  Report the percentage of forest burned.
#
  percent = get_percent_burned ( forest_size, forest )

  print ( '' )
  print ( '  Percentage of forest burned = %g' % ( percent ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'fire_simulation:' )
  print ( '  Normal end of execution.' )
  return

def fire_simulation_test ( ):

#*****************************************************************************80
#
## fire_simulation_test() tests fire_simulation().
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
#    John Burkardt.
#
  import platform
  
  print ( '' )
  print ( 'fire_simulation_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  fire_simulation() simulates a forest fire.' )

  forest_size = 20
  prob_spread = 0.5
  fire_simulation ( forest_size, prob_spread )
#
#  Terminate.
#
  print ( '' )
  print ( 'fire_simulation_test' )
  print ( '  Normal end of execution.' )
  return

def fire_spreads ( prob_spread ):

#*****************************************************************************80
#
## fire_spreads() determines whether the fire spreads.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    Python version by John Burkardt
#
#  Input:
#
#    real PROB_SPREAD, the probability of spreading.
#
#  Output:
#
#    bool fire_spreads, is TRUE if the fire spreads.
#
  import numpy as np

  u = np.random.rand ( )

  if ( u < prob_spread ):
    value = True
  else:
    value = False
 
  return value

def forest_burns ( forest_size, forest, prob_spread ):

#*****************************************************************************80
#
## forest_burns() models a single time step of the burning forest.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    Python version by John Burkardt
#
#  Input:
#
#    integer FOREST_SIZE, the linear dimension of the forest.
#
#    integer FOREST(FOREST_SIZE,FOREST_SIZE), an
#    array with an entry for each tree in the forest.
#
#    real PROB_SPREAD, the probability that the fire will 
#    spread from a burning tree to an unburnt one.
#
#  Output:
#
#    integer FOREST(FOREST_SIZE,FOREST_SIZE), the updated forest array.
#

#
#  Burning trees burn down;
#  Smoldering trees ignite;
#
  for j in range ( 0, forest_size ):
    for i in range ( 0, forest_size ):
      if ( forest[i,j] == BURNING ):
        forest[i,j] = BURNT
      elif ( forest[i,j] == SMOLDERING ):
        forest[i,j] = BURNING
#
#  Unburnt trees might catch fire.
#
  for j in range ( 0, forest_size ):
    for i in range ( 0, forest_size ):

      if ( forest[i,j] == BURNING ):
#
#  North.
#
        if ( 0 < i ):
          value = fire_spreads ( prob_spread )
          if ( value and forest[i-1,j] == UNBURNT ):
            forest[i-1,j] = SMOLDERING
#
#  South.
#
        if ( i < forest_size - 1 ):
          value = fire_spreads ( prob_spread )
          if ( value and forest[i+1,j] == UNBURNT ):
            forest[i+1,j] = SMOLDERING
#
#  West.
#
        if ( 0 < j ):
          value = fire_spreads ( prob_spread )
          if ( value and forest[i,j-1] == UNBURNT ):
            forest[i,j-1] = SMOLDERING
#
#  East.
#
        if ( j < forest_size - 1 ):
          value = fire_spreads ( prob_spread )
          if ( value and forest[i,j+1] == UNBURNT ):
            forest[i,j+1] = SMOLDERING

  return forest

def forest_initialize ( forest_size ):

#*****************************************************************************80
#
## forest_initialize() initializes the forest values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    Python version by John Burkardt
#
#  Input:
#
#    integer FOREST_SIZE, the linear dimension of the forest.
#
#  Output:
#
#    integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
#    with an entry for each tree in the forest.
#
  import numpy as np

  forest = UNBURNT * np.zeros ( [ forest_size, forest_size ] )

  return forest

def forest_is_burning ( forest_size, forest ):

#*****************************************************************************80
#
## forest_is_burning() reports whether any trees in the forest are burning.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    Python version by John Burkardt
#
#  Input:
#
#    integer FOREST_SIZE, the linear dimension of the forest.
#
#    integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
#    with an entry for each tree in the forest.
#
#  Output:
#
#    bool forest_is_burning, is TRUE if any tree in the forest
#    is in the SMOLDERING or BURNING state.
#
  value = False

  for j in range ( 0, forest_size ):
    for i in range ( 0, forest_size ):
      if ( forest[i,j] == SMOLDERING or forest[i,j] == BURNING ):
        value = True
        return value

  return value

def forest_print ( forest_size, forest, i_ignite, j_ignite ):

#*****************************************************************************80
#
## forest_print() prints the state of the trees in the forest.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    Python version by John Burkardt
#
#  Input:
#
#    integer FOREST_SIZE, the linear dimension of the forest.
#
#    integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
#    with an entry for each tree in the forest.
#
#    integer I_IGNITE, J_IGNITE, the location of the start 
#    of the fire.
#
  import sys as sys

  print ( '' )
  print ( '  Map of fire damage.' )
  print ( '  Fire started at "*".' )
  print ( '  Burned trees are indicated by "."')
  print ( '  Unburned trees are indicated by "X".' )
  print ( '' )

  for i in range ( 0, forest_size ):
    sys.stdout.write ( '  ' )
    for j in range ( 0, forest_size ):
      if ( i == i_ignite and j == j_ignite ):
        sys.stdout.write ( '*' )
      elif ( forest[i,j] == BURNT ):
        sys.stdout.write ( '.' )
      else:
        sys.stdout.write ( 'X' )
    print ( '' )

  return

def get_percent_burned ( forest_size, forest ):

#*****************************************************************************80
#
## get_percent_burned() computes the percentage of the forest that burned.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    Python version by John Burkardt
#
#  Input:
#
#    integer FOREST_SIZE, the linear dimension of the forest.
#
#    integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
#    with an entry for each tree in the forest.
#
#  Output:
#
#    real PERCENT, the percentage of the forest
#    that burned.
#
  total = 0
  for j in range ( 0, forest_size ):
    for i in range ( 0, forest_size ):
      if ( forest[i,j] == BURNT ):
        total = total + 1

  percent = float ( total ) / float ( forest_size ) / float ( forest_size )

  return percent

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

def tree_ignite ( forest_size, forest, i_ignite, j_ignite ):

#*****************************************************************************80
#
## tree_ignite() sets a given tree to the SMOLDERING state.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    Python version by John Burkardt
#
#  Input:
#
#    integer FOREST_SIZE, the linear dimension of 
#    the forest.
#
#    integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
#    with an entry for each tree in the forest.
#
#    integer I_IGNITE, J_IGNITE, the coordinates of the 
#    tree which is to be set to SMOLDERING.
#
#  Output:
#
#    integer FOREST(FOREST_SIZE,FOREST_SIZE), the updated array.
#
  forest[i_ignite,j_ignite] = SMOLDERING

  return forest

if ( __name__ == '__main__' ):
  timestamp ( )
  fire_simulation_test ( )
  timestamp ( )
 
