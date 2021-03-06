#! /usr/bin/env python3
#
def point_in_polygon ( n, x, y, x0, y0 ):

#*****************************************************************************80
#
## point_in_polygon determines if a point is inside a polygon
#
#  Discussion:
#
#    If the points ( x(i), y(i) ) ( i = 1, 2, ..., n ) are,
#    in this cyclic order, the vertices of a simple closed polygon and
#    (x0,y0) is a point not on any side of the polygon, then the
#    procedure determines, by setting "point_in_polygon" to TRUE or FALSE,
#    whether (x0,y0) lies in the interior of the polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Moshe Shimrat,
#    ACM Algorithm 112,
#    Position of Point Relative to Polygon,
#    Communications of the ACM,
#    Volume 5, Number 8, page 434, August 1962.
#
#    Richard Hacker,
#    Certification of Algorithm 112,
#    Communications of the ACM,
#    Volume 5, Number 12, page  606, December 1962.
#
#  Input:
#
#    integer N, the number of nodes or vertices in 
#    the polygon.  N must be at least 3.
#
#    real V(2,N), the vertices of the polygon.
#
#    real P(2), the coordinates of the point to be tested.
#
#  Output:
#
#    bool INSIDE, is TRUE if the point is
#    inside the polygon.
# 
  inside = False

  for i in range ( 0, n ):

    ip1 = ( ( i + 1 ) % n )

    if ( ( y[ip1] < y0 ) == ( y0 <= y[i] ) ):
      t = x0 - x[i] - ( y0 - y[i] ) * ( x[ip1] - x[i] ) / ( y[ip1] - y[i] )
      if ( t < 0.0 ):
        inside = not inside

  return inside

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test tests r8vec2_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_print_test:' )
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

def toms112_test ( ):

#*****************************************************************************80
#
## toms112_test() tests toms112().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'toms112_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  toms112() determines if a point is in a polygon.' )

  n = 5
  x = np.array ( [ 0.0, 1.0, 2.0, 1.0, 0.0 ] )
  y = np.array ( [ 0.0, 0.0, 1.0, 2.0, 2.0 ] )

  r8vec2_print ( n, x, y, '  The polygon vertices:' )

  print ( '' )
  print ( '      Px      Py  Inside' )
  print ( '' )

  test_num = 4
  x0_test = np.array ( [ 1.0, 3.0, 0.0, 0.5 ] )
  y0_test = np.array ( [ 1.0, 4.0, 2.0, -0.25 ] )

  for test in range ( 0, test_num ):
 
    x0 = x0_test[test]
    y0 = y0_test[test]

    inside = point_in_polygon ( n, x, y, x0, y0 )

    print ( '  %6.2g  %6.2g       %d' % ( x0, y0, inside ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'toms112_test()' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  toms112_test ( )
  timestamp ( )

