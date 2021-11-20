#! /usr/bin/env python3
#
def latin_random ( dim_num, point_num ):

#*****************************************************************************80
#
## latin_random() returns points in a Latin Random square.
#
#  Discussion:
#
#    In each spatial dimension, there will be exactly one
#    point whose coordinate value lies between consecutive
#    values in the list:
#
#      ( 0, 1, 2, ..., point_num ) / point_num
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
#  Input:
#
#    integer DIM_NUM, the spatial dimension.
#
#    integer POINT_NUM, the number of points.
#
#  Output:
#
#    real X(DIM_NUM,POINT_NUM), the points.
#
  import numpy as np
#
#  Pick DIM_NUM * POINT_NUM random numbers between 0 and 1.
#
  x = np.random.rand ( dim_num, point_num )
#
#  For spatial dimension I,
#    pick a random permutation of 1 to POINT_NUM,
#    force the corresponding I-th components of X to lie in the
#    interval ( PERM(J)-1, PERM(J) ) / POINT_NUM.
#
  for i in range ( 0, dim_num ):

    perm = perm_uniform ( point_num )

    for j in range ( 0, point_num ):

      x[i,j] = ( perm[j] + x[i,j] ) / point_num

  return x

def latin_random_test ( ):

#*****************************************************************************80
#
## latin_random_test() tests latin_random().
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

  dim_num = 2
  point_num = 10

  print ( '' )
  print ( 'latin_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  latin_random() chooses a random Latin Square' )
  print ( '  cell arrangement, and then returns' )
  print ( '  a random point from each cell.' )
  print ( '' )
  print ( '  Spatial dimension =  %d' % ( dim_num ) )
  print ( '  Number of points =   %d' % ( point_num ) )
  print ( '' )
  print ( '  Generate 3 examples:' )
  print ( '' )

  for test in range ( 0, 3 ):

    x = latin_random ( dim_num, point_num )

    print ( x )
#
#  Terminate.
#
  print ( '' )
  print ( 'latin_random_test' )
  print ( '  Normal end of execution.' )
  return

def perm_uniform ( n ):

#*****************************************************************************80
#
## perm_uniform() selects a random permutation of N objects.
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
#  Input:
#
#    integer N, the number of entries in the vector.
#
#  Output:
#
#    integer P[N], a permutation of the digits 0 through N-1.
#
  import numpy as np

  p = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    p[i] = i

  for i in range ( 0, n - 1 ):
    j = np.random.randint ( i, n )
    k    = p[i]
    p[i] = p[j]
    p[j] = k

  return p

def perm_uniform_test ( ):

#*****************************************************************************80
#
## perm_uniform_test() tests perm_uniform().
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

  n = 10

  print ( '' )
  print ( 'perm_uniform_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  perm_uniform randomly selects a permutation.' )
  print ( '' )

  for test in range ( 0, 5 ):
    p = perm_uniform ( n )
    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%4d' % ( p[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'perm_uniform_test' )
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
  latin_random_test ( )
  timestamp ( )

