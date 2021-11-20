#! /usr/bin/env python3
#
def search ( a, b, c ):

#*****************************************************************************80
#
## search() searches integers in [A,B] for a J so that F(J) = C.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, B, the search range.
#
#    integer C, the desired function value.
#
#  Output:
#
#    integer J, the computed solution, or -1
#    if no solution was found.
#
  for i in range ( a, b + 1 ):

    if ( f ( i ) == c ):
      return i

  return ( - 1 )

def search_serial ( a, b, c ):

#*****************************************************************************80
#
## search_serial() searches for a solution to an integer equation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the lower limit of the search.
#
#    integer B, the upper limit of the search.
#
#    integer C, the desired value.
#
#  Output:
#
#    integer J, is:
#    -1, if no solution could be found.
#    otherwise, F(J) = C and A <= J <= B.
#
  import platform
  from time import time

  print ( '' )
  print ( 'search_serial():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Search the integers from A to B' )
  print ( '  for a value J such that F(J) = C.' )
  print ( '' )
  print ( '  A        = %d' % ( a ) )
  print ( '  B        = %d' % ( b ) )
  print ( '  C        = %d' % ( c ) )

  wtime = time ( )

  j = search ( a, b, c )

  wtime = time ( ) - wtime
 
  print ( '' )
  if j == -1:
    print ( '  No solution was found.' )
  else:
    print ( '  Found J = %d' % ( j ) )
    print ( '  Verify F(J) = %d' % ( f ( j ) ) )
  
  print ( '  Time     = %f' % ( wtime ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'search_serial():' )
  print ( '  Normal end of execution.' )
  return j

def search_serial_test ( ):

#*****************************************************************************80
#
## search_serial_test() tests search_serial().
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
  print ( 'search_serial_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test search_serial()' )

  search_serial ( 1,               10000, 45 )
  search_serial ( 1,              100000, 45 )
  search_serial ( 1,             1000000, 45 )
  search_serial ( 1674924000, 1674924999, 45 )
#
#  Terminate.
#
  print ( '' )
  print ( 'search_serial_test:' )
  print ( '  Normal end of execution.' )
  return

def f ( i ):

#*****************************************************************************80
#
## f() is the function we are analyzing.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the argument.
#
#  Output:
#
#    integer VALUE, the value.
#
  i4_huge = 2147483647

  value = i

  for j in range ( 0, 5 ):

    k = ( value // 127773 )

    value = 16807 * ( value - k * 127773 ) - k * 2836

    if ( value <= 0 ):
      value = value + i4_huge

  return value

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
  search_serial_test ( )
  timestamp ( )

