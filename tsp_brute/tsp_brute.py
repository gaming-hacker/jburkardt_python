#! /usr/bin/env python3
#
def path_cost ( n, distance, p ):

#*****************************************************************************80
#
## path_cost() evaluates the cost of a round trip.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of cities.
#
#    real DISTANCE(N,N), the city to city distance table.
#
#    integer P(N), a permutation of 1:N, the route.
#
#  Output:
#
#    real COST, the cost of the route.
#
  cost = 0.0
  i1 = n - 1
  for i2 in range ( 0, n ):
    cost = cost + distance [ p[i1], p[i2] ]
    i1 = i2

  return cost

def path_cost_test ( ):

#*****************************************************************************80
#
## path_cost_test() tests path_cost.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  distance = np.array ( [\
    [ 0.0,  3.0,  4.0,  2.0,  9.0 ],
    [ 3.0,  0.0,  4.0,  6.0,  3.0 ],
    [ 4.0,  4.0,  0.0,  5.0,  8.0 ],
    [ 2.0,  6.0,  5.0,  0.0,  6.0 ],
    [ 9.0,  3.0,  8.0,  6.0,  0.0 ] ] )

  p = np.array ( [ 0, 3, 2, 1, 4 ] )

  print ( '' )
  print ( 'path_cost_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  path_cost returns the cost of a traveling salesman itinerary.' )

  print ( '' )
  print ( '  Number of cities n = %d' % ( n ) )
  print ( '' )
  print ( '  Distance matrix:' )
  print ( '' )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print ( '  %4g' % ( distance[i,j] ), end = '' )
    print ( '' )

  print ( '' )
  print ( '  Itinerary:' )
  for i in range ( 0, n ):
    print ( '  %2d' % ( p[i] ), end = '' )
  print ( '' )

  cost = path_cost ( n, distance, p )

  print ( '' )
  print ( '  Cost of this path is %g' % ( cost ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'path_cost_test:' )
  print ( '  Normal end of execution.' )
  return

def perm0_next3 ( n, p, more, rank ):

#*****************************************************************************80
#
## perm0_next3 computes permutations of (0,...,N-1).
#
#  Discussion:
#
#    The routine is initialized by calling with MORE = TRUE, in which case
#    it returns the identity permutation.
#
#    If the routine is called with MORE = FALSE, then the successor of the
#    input permutation is computed.
#
#    Trotter's algorithm is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hale Trotter,
#    PERM, Algorithm 115,
#    Communications of the Association for Computing Machinery,
#    Volume 5, 1962, pages 434-435.
#
#  Input:
#
#    integer N, the number of objects being permuted.
#
#    integer P(N).  The current permutation, if MORE is TRUE.  
#    But on a startup call, with MORE FALSE, the input value 
#    of P is not needed.
#
#    bool MORE.  Set to FALSE on an
#    initialization call, and on subsequent inputs should have its output
#    value from the previous call.  
#
#    Input/integer RANK, the rank of the current permutation.  
#
#  Output:
#
#    integer P(N).  The next permutation if MORE is FALSE, 
#    then P is the first permutation in the sequence.
#
#    bool MORE.  TRUE if there was a next
#    permutation to produce, or FALSE if there are no more permutations 
#    to produce.
#
#    integer RANK, the rank of the next permutation.  
#
  if ( not more ):

    for i in range ( 0, n ):
      p[i] = i
    more = True
    rank = 1

  else:

    n2 = n
    m2 = rank
    s = n

    while ( True ):

      q = ( m2 % n2 )
      t = ( m2 % ( 2 * n2 ) )

      if ( q != 0 ):
        break

      if ( t == 0 ):
        s = s - 1

      m2 = ( m2 // n2 )
      n2 = n2 - 1

      if ( n2 == 0 ):
        for i in range ( 0, n ):
          p[i] = i
        more = False
        rank = 1
        break

    if ( n2 != 0 ):

      if ( q == t ):
        s = s - q
      else:
        s = s + q - n2

      t      = p[s-1]
      p[s-1] = p[s]
      p[s]   = t

      rank = rank + 1

  return p, more, rank

def perm0_next3_test ( ):

#*****************************************************************************80
#
## perm0_next3_test() tests perm0_next3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'perm0_next3_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  perm0_next3 generates permutations in order.' )
  print ( '' )

  n = 4
  p = np.zeros ( n )
  more = False
  rank = 0
 
  while ( True ):

    p, more, rank = perm0_next3 ( n, p, more, rank )

    if ( not more ):
      break

    print ( '  %3d:' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( p[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'perm0_next3_test:' )
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

def tsp_brute ( filename ):

#*****************************************************************************80
#
## tsp_brute applies brute force to the TSP problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file containing the distance
#    matrix information.  This is an optional input.  If it is not provided,
#    the program will prompt for it.
#
  import numpy as np
  import platform

  timestamp ( )
  print ( '' )
  print ( 'tsp_brute:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve small traveling salesman problems by brute force.' )
#
#  Get the distance table.
#
  print ( '' )
  print ( '  Distance matrix filename is "%s"' % ( filename ) )

  distance = np.loadtxt ( filename )
#
#  Approve the distance table.
#
  dims = distance.shape

  m = dims[0]
  n = dims[1]

  if ( m != n ):
    print ( '' )
    print ( 'tsp_brute - Fatal error!' )
    print ( '  The distance matrix must be square.' )
    print ( '  Your matrix has M = %d, N = %d', m, n )
    raise Exception ( 'tsp_brute - Fatal error!' )

  v = np.diagonal ( distance )
  test = np.linalg.norm ( v )

  if ( 0.0 < test ):
    print ( '' )
    print ( 'tsp_brute - Fatal error!' )
    print ( '  The distance matrix must have zero diagonal.' )
    print ( '  Your matrix has ||diag(D)|| = %g', test )
    raise Exception ( 'tsp_brute - Fatal error!' )

  test = np.linalg.norm ( distance - distance.transpose ( ) )

  if ( 0.0 < test ):
    print ( '' )
    print ( 'tsp_brute - Fatal error!' )
    print ( '  The distance matrix must be symmetric.' )
    print ( '  Your matrix has ||D-D''|| = %g' % ( test ) )
    raise Exception ( 'tsp_brute - Fatal error!' )
#
#  Print the distance matrix.
#
  print ( '' )
  print ( '  The city-to-city distance matrix:' )
  print ( '' )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print ( '  %4g' % ( distance[i,j] ), end = '' )
    print ( '' )
#
#  Examine every permutation.
#
  total_max = - np.inf
  total_min = np.inf
  total_ave = 0.0

  p = np.zeros ( n, dtype = np.int32 )
  more = False
  rank = 0

  p_min = np.zeros ( n, dtype = np.int32 )

  paths = 0

  while ( True ):

    p, more, rank = perm0_next3 ( n, p, more, rank )

    if ( not more ):
      break

    paths = paths + 1

    total = path_cost ( n, distance, p )

    total_ave = total_ave + total

    if ( total_max < total ):
      total_max = total

    if ( total < total_min ):
      total_min = total
      p_min = p.copy ( )

  total_ave = total_ave / paths
#
#  Report.
#
  print ( '' )
  print ( '  A minimal length itinerary:' )
  print ( '' )
  print ( '  Step  From  To        Distance' )
  print ( '' )
  for i1 in range ( 0, n ):
    i2 = ( ( i1 + 1 ) % n )
    print ( '  %4d    %2d  %2d  %14.6g' \
      % ( i2, p_min[i1], p_min[i2], distance[p_min[i1],p_min[i2]] ) )

  print ( '  ----    --  --  --------------' )
  print ( '  Total:          %14.6g' % ( total_min ) )

  print ( '' )
  print ( '  Number of paths checked = %d' % ( paths ) )
  print ( '' )
  print ( '  Minimum length = %g' % ( total_min ) )
  print ( '  Average length = %g' % ( total_ave ) )
  print ( '  Maximum length = %g' % ( total_max ) )

  return
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_brute' )
  print ( '  Normal end of execution.' )
  return

def tsp_brute_test ( ):

#*****************************************************************************80
#
## tsp_brute_test() tests tsp_brute().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tsp_brute_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  tsp_brute() solves a small traveling salesman problem.' )

  filename = 'five.txt'

  print ( '' )
  print ( '  Call tsp_brute ( %s )' % ( filename ) )
  tsp_brute ( filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_brute_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  tsp_brute_test ( )
  timestamp ( )

