#! /usr/bin/env python3
#
def change_making_list ( coin_num, coin_value, target ):

#*****************************************************************************80
#
## change_making_list() solves the change making problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer COIN_NUM, the number of coin denomiations.
#
#    integer COIN_VALUE(COIN_NUM), the value of each coin.
#    These values should be positive integers.
#
#    integer TARGET, the desired sum.
#
#  Output:
#
#    integer A(1:TARGET+1), A(T) lists the smallest number of coins
#    needed to form the sum T, or "Inf" if it is not possible to form
#    this sum.
#
  import numpy as np

  a = np.zeros ( target + 1 )
  for j in range ( 0, target + 1 ):
    a[j] = float ( 'Inf' )
#
#  If T is the value of a coin, then A(T) is 1.
#
  for i in range ( 0, coin_num ):
    j = coin_value[i]
    if ( j <= target ):
      a[j] = 1
#
#  To compute A(T) in general, consider getting there by adding
#  one coin of value V, and looking at A(T-V).
#
  for j in range ( 0, target + 1 ):
    for i in range ( 0, coin_num ):
      if ( 0 <= j - coin_value[i] ):
        a[j] = min ( a[j], a[j-coin_value[i]] + 1 ) 

  return a

def change_making_list_test ( ):

#*****************************************************************************80
#
## change_making_list_test() tests change_making_list().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'change_making_list_test():' )
  print ( '  change_making list() computes A[T], the smallest number ' )
  print ( '  of coins needed to form a given sum T, by computing ' )
  print ( '  the list A[0]...A[T].' )

  test_num, coin_num_list, coin_value_list, target_list = problems ( )

  for test in range ( 0, test_num ):

    coin_num = coin_num_list[test]
    coin_value = coin_value_list[test]
    target = target_list[test]

    print ( '' )
    print ( '  Test %d:' % ( test ) )
    print ( '  Number of coins = %d' % ( coin_num ) )
    print ( '  Values = ' )
    for i in range ( 0, coin_num ):
      print ( '  %d' % ( coin_value[i] ) )
    print ( '' )
    print ( '  Target = %d' % ( target ) )

    a = change_making_list ( coin_num, coin_value, target )

    print ( '' )
    for i in range ( 0, target + 1 ):
      if ( a[i] == float ( 'Inf' ) ):
        print ( '  %3d  Not possible!' % ( i ) )
      else:
        print ( '  %3d  %2d' % ( i, a[i] ) )

  return

def problems ( ):

#*****************************************************************************80
#
## problems() defines some problems.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer test_num, the number of tests available.
#
#    integer coin_num_list[7], the number of coins in each test.
#
#    integer coin_value_list[7][*], the coin values in each test.
#
#    integer target_list[7], the target sum.
#
  import numpy as np

  test_num = 7

  coin_num_list = np.array ( [ \
    3, \
    5, \
    6, \
    7, \
    3, \
    6, \
    3 ] )

  coin_value_list = [ \
    [  5,  9, 13 ], \
    [  1,  4,  5,  8, 11 ], \
    [  1,  5, 10, 25, 50, 100 ], \
    [  1,  2,  6, 12, 24,  48,  60 ], \
    [  1,  3,  4 ], \
    [ 16, 17, 23, 24, 39,  40 ], \
    [  6,  9, 20 ] ]

  target_list = np.array ( [ \
    19, \
    29, \
    96, \
    96, \
     6, \
   100, \
    43 ] )

  return test_num, coin_num_list, coin_value_list, target_list

def problems_test ( ):

#*****************************************************************************80
#
## problems_test() tests problems().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'problems_test():' )
  print ( '  problems() returns a set of sample change making problems.' )

  test_num, coin_num_list, coin_value_list, target_list = problems ( )

  for test in range ( 0, test_num ):

    coin_num = coin_num_list[test]
    coin_value = coin_value_list[test]
    target = target_list[test]

    print ( '' )
    print ( '  Test %d:' % ( test ) )
    print ( '  Number of coins = %d' % ( coin_num ) )
    print ( '  Values = ' )
    for i in range ( 0, coin_num ):
      print ( '  %d' % ( coin_value[i] ) )
    print ( '' )
    print ( '  Target = %d' % ( target ) )

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

  return

def change_making_test ( ):

#*****************************************************************************80
#
## change_making_test() tests change_making().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 June 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'change_making_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  change_making() considers change-making problems.' )

  problems_test ( )
  change_making_list_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'change_making_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  change_making_test ( )
  timestamp ( )
