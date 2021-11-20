#! /usr/bin/env python3
#
def backbin_rc ( n, reject, n2, choice ):

#*****************************************************************************80
#
## backbin_rc() uses reverse communication for binary backtracking.
#
#  Discussion:
#
#    If this procedure returns a solution with N2 = N, which is acceptable
#    to the user, then a full solution has been found.
#
#    If this procedure returns N2 = -1, no more potential solutions are
#    available to consider.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the full solution.
#
#    logical REJECT, is TRUE if the proposed partial solution
#    in the first N2 entries of CHOICE must be rejected.  On first call,
#    this value is ignored.
#
#    integer N2, the length of the current
#    partial solution.  On first call, set N2 to -1. 
#
#    integer CHOICE(N), indicates the current
#    partial solution in entries 1 through N2, which will contain 0 or 1.
#    On first call, set CHOICE to []
#
#  Output:
#
#    integer N2, the updated length of the current partial solution.  
#    If the program has exhausted the search space,
#    the value of N2 will be returned as -1.
#
#    integer CHOICE(N), indicates the current partial solution in entries 
#    1 through N2, which will contain 0 or 1.
#

#
#  N2 = -1 means an initialization call.
#
  if ( n2 == -1 ):

    choice[0:n] = -1
    n2 = 1
    choice[n2-1] = 1
#
#  1 <= FOCUS means we asked the user to evaluate CHOICE(1:N2).
#
#  N2 = N means we returned a full prospective solution
#  so in any case we must increment CHOICE.
#
#  Returning REJECT = 1 means no solution begins this way
#  so we must increment CHOICE.
#
  elif ( n2 == n or reject ):

    while ( 1 < n2 ):
      if ( choice[n2-1] == 1 ):
        choice[n2-1] = 0
        break
      choice[n2-1] = -1
      n2 = n2 - 1
#
#  Have we exhausted the solution space?
#
    if ( n2 == 1 ):
      if ( choice[n2-1] == 1 ):
        choice[n2-1] = 0
      else:
        choice[n2-1] = -1
        n2 = -1
#
#  N2 < N and not REJECT means we can increment N2.
#
  else:

    n2 = n2 + 1
    choice[n2-1] = 1

  return n2, choice

def backtrack_binary_rc_test01 ( ):

#*****************************************************************************80
#
## backtrack_binary_rc_test01() seeks binary powers that have a given sum.
#
#  Discussion:
#
#    We consider the binary powers 1, 2, 4, ... 2^(n-1).
#
#    We wish to select some of these powers, so that the sum is equal
#    to a given target value.  We are actually simply seeking the binary
#    representation of an integer.
#
#    A partial solution is acceptable if it is less than the target value.
#
#    We list the powers in descending order, so that the bactracking
#    procedure makes the most significant choices first, thus quickly
#    eliminating many unsuitable choices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 8
  test_num = 3
  targets = np.array ( [ 73, 299, -3 ] )

  print ( '' )
  print ( 'backtrack_binary_rc_test01():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  backbin_rc() finds the binary expansion of' )
  print ( '  an integer between 0 and 255.' )
  print ( '  The choices are 0/1 for the 8 digits.' )

  for test in range ( 0, test_num ):

    target = targets[test]
    print ( '' )
    print ( '  TARGET = %d' % ( target ) )
    call_num = 0
    reject = False
    n2 = -1
    choice = np.zeros ( n, dtype = np.int32 )

    while ( True ):

      n2, choice = backbin_rc ( n, reject, n2, choice )
      call_num = call_num + 1

      if ( n2 == -1 ):
        print ( '  Termination without solution.' )
        break
#
#  Evaluate the integer determined by the choices.
#
      factor = 1
      for i in range ( n, n2, -1 ):
        factor = factor * 2

      result = 0
      for i in range ( 0, n2 ):
        result = result * 2 + choice[i]

      result = result * factor
#
#  If the integer is too big, then we reject it, and
#  all the related integers formed by making additional choices.
#
      reject = ( target < result )
#
#  If we hit the target, then in this case, we can finish because
#  the solution is unique.
#
      if ( result == target ):
        break

    print ( '  Number of calls = %d' % ( call_num ) )
    print ( '  Binary search space = %d' % ( 2 ** n ) )
    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%2d' % ( choice[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'backtrack_binary_rc_test01():' )
  print ( '  Normal end of execution.' )
  return

def backtrack_binary_rc_test02 ( ):

#*****************************************************************************80
#
## backtrack_binary_rc_test02() seeks a subset of numbers which add to a given sum.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 8
  target = 53
  w = np.array ( [ 15, 22, 14, 26, 32, 9, 16, 8 ] )

  print ( '' )
  print ( 'backtrack_binary_rc_test02():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  backbin_rc() seeks subsets of a set W' )
  print ( '  that sum to a given target value.' )
  print ( '  The choices are 0/1 to select each element of W.' )

  print ( '' )
  print ( '  TARGET = %d' % ( target ) )
  print ( '' )
  call_num = 0
  reject = 0
  n2 = -1
  choice = np.zeros ( n, dtype = np.int32 )

  while ( True ):

    n2, choice = backbin_rc ( n, reject, n2, choice )
    call_num = call_num + 1

    if ( n2 == -1 ):
      break
#
#  Evaluate the partial sum.
#
    result = 0
    for i in range ( 0, n2 ):
      result = result + choice[i] * w[i]
#
#  If the sum is too big, then we reject it, and
#  all the related sums formed by making additional choices.
#
    reject = ( target < result )
#
#  If we hit the target, print out the information.
#
    if ( result == target and n2 == n ):
      print ( '  ', end = '' )
      for i in range ( 0, n ):
        print ( '%2d' % ( choice[i] ), end = '' )
      print ( '' )

  print ( '' )
  print ( '  Number of calls = %d' % ( call_num ) )
  print ( '  Binary search space = %d' % ( 2 ** n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'backtrack_binary_rc_test02():' )
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

def backtrack_binary_rc_test ( ):

#*****************************************************************************80
#
## backtrack_binary_rc_test() tests backtrack_binary_rc().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'backtrack_binary_rc_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test backtrack_binary_rc()' )

  backtrack_binary_rc_test01 ( )
  backtrack_binary_rc_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'backtrack_binary_rc_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  backtrack_binary_rc_test ( )
  timestamp ( )

