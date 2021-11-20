#! /usr/bin/env python3
#
def i4vec_distances ( k, locate ):

#*****************************************************************************80
#
## i4vec_distances computes a pairwise distance table.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer K, the number of objects.
#
#    integer LOCATE(K), the obect locations.
#
#  Output:
#
#    integer D(K*(K-1)/2), the pairwise distances.
#
  import numpy as np

  d = np.zeros ( k * ( k - 1 ) // 2 )

  l = 0
  for i in range ( 0, k ):
    for j in range ( i + 1, k ):
      d[l] = abs ( locate[i] - locate[j] )
      l = l + 1

  return d

def i4vec_distances_test ( ):

#*****************************************************************************80
#
## i4vec_distances_test tests i4vec_distances.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4vec_distances_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_distances computes the pairwise distances between elements' )
  print ( '  of an I4VEC.' )

  n = 5
  locate = np.array ( [ 0, 3, 10, 20, 100 ], dtype = np.int32 )
  d = i4vec_distances ( n, locate )

  i4vec_print ( n, locate, '  Locations:' )
  i4vec_print ( n * ( n - 1 ) // 2, d, '  Distances:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_distances_test:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print prints an I4VEC.
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
## i4vec_print_test tests i4vec_print.
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
  print ( 'i4vec_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_print prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_print_test:' )
  print ( '  Normal end of execution.' )
  return

def ksub_random ( n, k ):

#*****************************************************************************80
#
## ksub_random selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    Consider the set A(1:N) = 1, 2, 3, ... N.
#    Choose a random index I1 between 1 and N, and swap items A(1) and A(I1).
#    Choose a random index I2 between 2 and N, and swap items A(2) and A(I2).
#    repeat K times.
#    A(1:K) is your random K-subset.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the set from which subsets
#    are drawn.
#
#    integer K, number of elements in desired subsets.
#    1 <= K <= N.
#
#  Output:
#
#    integer A(K), the indices of the randomly
#    chosen elements.
#
  import numpy as np
#
#  Let B index the set.
#
  b = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    b[i] = i
#
#  Choose item 1 from N things,
#  choose item 2 from N-1 things,
#  choose item K from N-K+1 things.
#
  for i in range ( 0, k ): 

    j = np.random.random_integers ( i, n - 1 )

    t    = b[i]
    b[i] = b[j]
    b[j] = t
#
#  Copy the first K elements.
#
  a = np.zeros ( k, dtype = np.int32 )
  for i in range ( 0, k ):
    a[i] = b[i]

  return a

def ksub_random_test ( ):

#*****************************************************************************80
#
## ksub_random_test tests ksub_random.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  k = 3
  n = 100

  print ( '' )
  print ( 'ksub_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ksub_random generates a random K subset of an N set.' )
  print ( '  Set size is N =    %d' % ( n ) )
  print ( '  Subset size is K = %d' % ( k ) )
  print ( '' )

  for i in range ( 0, 10 ):

    a = ksub_random ( n, k )

    for j in range ( 0, k ):
      print ( '  %3d' % ( a[j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ksub_random_test:' )
  print ( '  Normal end of execution.' )
  return

def test_partial_digest ( k, dmax ):

#*****************************************************************************80
#
## test_partial_digest returns a partial digest test problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer K, the number of objects.
#    K must be at least 2.
#
#    integer DMAX, the maximum possible distance.
#    DMAX must be at least K-1.
#
#  Output:
#
#    integer LOCATE(K), the obect locations.
#
#    integer D(K*(K-1)/2), the pairwise distances.
#
  import numpy as np
#
#  Check input.
#
  if ( k < 2 ):
    print ( '\n' )
    print ( 'test_partial_digest - Fatal error!\n' )
    print ( '  Input K < 2.\n' )
    raise Exception ( 'test_partial_digest - Fatal error!' )

  if ( dmax < k - 1 ):
    print ( '\n' )
    print ( 'test_partial_digest - Fatal error!\n' )
    print ( '  DMAX < K - 1.\n' )
    raise Exception ( 'test_partial_digest - Fatal error!' )
#
#  Select LOCATE, which is a random subset of the integers 0 through DMAX.
#
  locate = ksub_random ( dmax - 1, k - 2 )
  locate = np.insert ( locate, 0, 0 )
  locate = np.append ( locate, dmax )
#
#  Compute K*(K+1)/2 pairwise distances.
#
  d = i4vec_distances ( k, locate )
 
  return locate, d

def test_partial_digest_test ( ):

#*****************************************************************************80
#
## test_partial_digest_test() tests test_partial_digest().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'test_partial_digest_test():' )
  print ( '  test_partial_digest() creates test problems for the' )
  print ( '  partial digest problem.' )

  i4vec_distances_test ( )
  i4vec_print_test ( )
  ksub_random_test ( )
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
  i4vec_print ( k * ( k - 1 ) // 2, d, '  Distances:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_partial_digest_test():' )
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
  test_partial_digest_test ( )
  timestamp ( )
 
