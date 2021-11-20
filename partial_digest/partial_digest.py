#! /usr/bin/env python3
#
def find_distances ( l_length, l, x_length, x, y ):

#*****************************************************************************80
#
## find_distances() determines if the "free" distances include every ||X(I)-Y||.
#
#  Discussion:
#
#    This routine is given a candidate point Y, a set of placed points
#    X(1:X_LENGTH), and a list of unused or "free" distances in
#    L(1:L_LENGTH).  The routine seeks to find in L a copy of the
#    distance from Y to each X.
#
#    If so, then the L array is reordered so that entries
#    L(L_LENGTH-X_LENGTH+1:L_LENGTH) contain theses distances.
#
#    In other words, Y can be added into X, and L_LENGTH reduced to
#    L_LENGTH-X_LENGTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pavel Pevzner,
#    Computational Molecular Biology,
#    MIT Press, 2000,
#    ISBN: 0-262-16197-4,
#    LC: QH506.P47.
#
#  Input:
#
#    integer L_LENGTH, the length of the array.
#
#    Input/integer L(L_LENGTH), the array.  On output,
#    some entries have been shuffled.  In particular, if SUCCESS is TRUE,
#    the entries L(L_LENGTH-X_LENGTH+1:L_LENGTH) contain the distances
#    of X(1:X_LENGTH) to Y.
#
#    integer X_LENGTH, the number of entries in X.
#
#    integer X(X_LENGTH), the number of points
#    already accepted.
#
#    integer Y, a new point that we are considering.
#
#  Output:
#
#    logical SUCCESS, is TRUE if the entries of L included
#    the values of the distance of Y to each entry of X.
#
  l2_length = l_length

  for i in range ( 0, x_length ):

    d = abs ( x[i] - y )

    success = False

    for j in range ( 0, l2_length ):

      if ( l[j] == d ):
        l[j] = l[l2_length-1]
        l[l2_length-1] = d
        l2_length = l2_length - 1
        success = True
        break

    if ( not success ):
      return success, l

  success = True

  return success, l

def find_distances_test ( ):

#*****************************************************************************80
#
## find_distances_test() tests find_distances().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'FIND_DISTANCES_TEST:' )
  print ( '  FIND_DISTANCES takes a candidate location Y' )
  print ( '  and determines whether its distance to each point' )
  print ( '  in the X array is listed in the L array.' )

  n = 5
  l_length = n * ( n - 1 ) // 2
  l = np.array ( [  13, 15, 38, 90, 2, 25, 77, 23, 75, 52 ], dtype = np.int32 )
  i4vec_print ( l_length, l, '  Initial L array:' )

  l, l_max = i4vec_max_last ( l_length, l )
  l_length = l_length - 1

  x = np.zeros ( n )
  x[0] = 0
  x[1] = l_max
  x_length = 2
#
#  Solution is X = (/ 0, 13, 15, 38, 90 /) or (/ 0, 52, 75, 77, 90 /)
#  So Y = 13, 15, 38, 52, 75 or 77 will be acceptable.
#
  l, y = i4vec_max_last ( l_length, l )
  success, l = find_distances ( l_length, l, x_length, x, y )

  print ( '' )
  print ( '  Consider Y = %d' % ( y ) )
  print ( '' )
  if ( success ):
    print ( '  This Y is acceptable.' )
    l_length = l_length - x_length
    x_length = x_length + 1
    x[x_length-1] = y
    i4vec_print ( x_length, x, '  New X array:' )
    i4vec_print ( l_length, l, '  New L array:' )
  else:
    print ( '  This Y is not acceptable.' )

  y = 35
  success, l = find_distances ( l_length, l, x_length, x, y )

  print ( '' )
  print ( '  Consider Y = %d' % ( y ) )
  print ( '' )
  if ( success ):
    print ( '  This Y is acceptable.' )
    l_length = l_length - x_length
    x_length = x_length + 1
    x[x_length-1] = y
    i4vec_print ( x_length, x, '  New X array:' )
    i4vec_print ( l_length, l, '  New L array:' )
  else:
    print ( '  This Y is not acceptable.' )

  return

def i4vec_max_last ( l_length, l ):

#*****************************************************************************80
#
## i4vec_max_last() moves the maximum entry of an I4VEC to the last position.
#
#  Discussion:
#
#    This routine finds the largest entry in an array and moves
#    it to the end of the array.
#
#    If we ignore this last array entry, then the effect is the same
#    as "deleting" the maximum entry from the array.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pavel Pevzner,
#    Computational Molecular Biology,
#    MIT Press, 2000,
#    ISBN: 0-262-16197-4,
#    LC: QH506.P47.
#
#  Input:
#
#    integer L_LENGTH, the length of the array.
#
#    integer L(L_LENGTH), the array.
#
#  Output:
#
#    integer VALUE, the maximum entry in the
#    input array.
#
#    integer L(L_LENGTH), the maximum entry has been shifted to the end.
#
  for i in range ( 1, l_length ):
    if ( l[i] < l[i-1] ):
      t = l[i]
      l[i] = l[i-1]
      l[i-1] = t
 
  value = l[l_length-1];

  return l, value

def i4vec_max_last_test ( ):

#*****************************************************************************80
#
## i4vec_max_last_test() tests i4vec_max_last().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2018
#
#  Author:
#
#   John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'I4VEC_MAX_LAST_TEST' )
  print ( '  I4VEC_MAX_LAST identifies the largest element in an' )
  print ( '  I4VEC, and moves it to the final entry.' )

  x = np.random.random_integers ( 1, 30, size = n )

  i4vec_print ( n, x, '  Input vector:' )

  x, x_max = i4vec_max_last ( n, x )

  print ( '' )
  print ( '  Maximum: %d' % ( x_max ) )

  i4vec_print ( n, x, '  Output vector:' )

  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print() prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_test ( ):

#*****************************************************************************80
#
## i4vec_print_test() tests i4vec_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_PRINT prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def partial_digest_recur ( n, l ):

#*****************************************************************************80
#
## partial_digest_recur() uses recursion on the partial digest problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pavel Pevzner,
#    Computational Molecular Biology,
#    MIT Press, 2000,
#    ISBN: 0-262-16197-4,
#    LC: QH506.P47.
#
#  Input:
#
#    integer N, the number of nodes.
#
#    integer L((N*(N-1))/2), the distances between all pairs
#    of distinct nodes.
#
  import numpy as np
#
#  How long is L?
#
  l_length = ( n * ( n - 1 ) ) // 2
#
#  Find WIDTH, the largest element of L, and move it to the last position.
#
  l, width = i4vec_max_last ( l_length, l )
#
#  Think of L as being 1 entry shorter.
#
  l_length = l_length - 1
#
#  Using WIDTH, set the first two entries of X.
#
  x = np.zeros ( n )
  x[0] = 0
  x[1] = width
  x_length = 2
#
#  Begin recursive operation.
#
  l_length, l, x_length, x = place ( l_length, l, x_length, x )

  return

def partial_digest_recur_test01 ( ):

#*****************************************************************************80
#
## partial_digest_recur_test01() tests partial_digest_recur().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nn2 = ( n * ( n - 1 ) ) // 2
#
#  Set the distance array.
#
  dist = np.array ( [ 2, 2, 3, 3, 4, 5, 6, 7, 8, 10 ], dtype = np.int32 )

  print ( '' )
  print ( 'PARTIAL_DIGEST_RECUR_TEST01' )
  print ( '  PARTIAL_DIGEST_RECUR generates solutions to the partial' )
  print ( '  digest problem, using recursion.' )

  print ( '' )
  print ( '  The number of objects to place is N = %d' % ( n ) )
  print ( '' )
  print ( '  The original placement was 0,3,6,8,10.' )
  print ( '  These placements generate the following distances:' )

  i4vec_print ( nn2, dist, '  Distance array:' )

  print ( '' )
  print ( '  PARTIAL_DIGEST_RECUR may recover the original placements' )
  print ( '  from the pairwise distances.  It may also find other' )
  print ( '  placements that have the same distance array.' )

  partial_digest_recur ( n, dist )

  return

def partial_digest_recur_test02 ( ):

#*****************************************************************************80
#
## partial_digest_recur_test02() considers tests from a library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'PARTIAL_DIGEST_RECUR_TEST02:' )
  print ( '  PARTIAL_DIGEST_RECUR generates solutions to the partial' )
  print ( '  digest problem, using recursion.' )
  print ( '  TEST_PARTIAL_DIGEST creates test problems for the' )
  print ( '  partial digest problem.' )
#
#  Request a sample problem.
#
  k = 6
  dmax = 20

  print ( '' )
  print ( '  Number of nodes = %d' % ( k ) )
  print ( '  Maximum distance = %d' % ( dmax ) )

  locate, d = test_partial_digest ( k, dmax )
#
#  Sort the data.
#
  locate = np.sort ( locate )
  d = np.sort ( d )
#
#  Print the data.
#
  i4vec_print ( k, locate, '  Locations:' )
  i4vec_print ( k * ( k - 1 ) / 2, d, '  Distances:' )
#
#  Solve the problem.
#
  partial_digest_recur ( k, d )

  return

def partial_digest_test ( ):

#*****************************************************************************80
#
## partial_digest_test() tests partial_digest().
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
  print ( 'partial_digest_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test partial_digest()' )

  find_distances_test ( )
  i4vec_max_last_test ( )
  i4vec_print_test ( )
  partial_digest_recur_test01 ( )
#
#  Test02 requires access to the TEST_PARTIAL_DIGEST library.
#
# partial_digest_recur_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'partial_digest_test:' )
  print ( '  Normal end of execution.' )
  return

def place ( l_length, l, x_length, x ):

#*****************************************************************************80
#
## place() tries to place the next point for the partial digest problem.
#
#  Discussion:
#
#    Note that this is a recursive function.  A solution to the
#    partial digest problem is sought by calling this routine repeatedly.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pavel Pevzner,
#    Computational Molecular Biology,
#    MIT Press, 2000,
#    ISBN: 0-262-16197-4,
#    LC: QH506.P47.
#
#  Input:
#
#    integer L_LENGTH, the number of entries in L.
#
#    integer L(L_LENGTH), the array of distances.
#
#    integer X_LENGTH, the number of entries in X.
#
#    integer X(X_LENGTH), the current partial solution.
#
#  Output:
#
#    integer L_LENGTH, the updated number of entries in L.
#
#    integer L(L_LENGTH), the update array of distances.
#
#    integer X_LENGTH, the updated number of entries in X.
#
#    integer X(X_LENGTH), the updated partial solution.
#

#
#  Are we done?
#
  if ( l_length <= 0 ):
    i4vec_print ( x_length, x, '  Solution:' )
    return l_length, l, x_length, x
#
#  Find the maximum remaining distance.
#
  l, y = i4vec_max_last ( l_length, l )
#
#  We can add a point at Y if L contains all the distances from Y to
#  the current X's.
#
  success, l = find_distances ( l_length, l, x_length, x, y )

  if ( success ):
    l_length2 = l_length - x_length
    x_length = x_length + 1
    x[x_length-1] = y
    l_length2, l, x_length, x = place ( l_length2, l, x_length, x )
    x_length = x_length - 1
#
#  We must also consider the case where Y represents the distance
#  to X[1], not X[0].
#
  y = x[1] - y

  success, l = find_distances ( l_length, l, x_length, x, y )

  if ( success ):
    l_length2 = l_length - x_length
    x_length = x_length + 1
    x[x_length-1] = y
    l_length2, l, x_length, x = place ( l_length2, l, x_length, x )
    x_length = x_length - 1

  return l_length, l, x_length, x

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
  partial_digest_test ( )
  timestamp ( )
 
