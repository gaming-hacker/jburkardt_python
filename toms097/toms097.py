#! /usr/bin/env python3
#
def i4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## i4mat_print prints an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    integer A(M,N), the matrix.
#
#    string TITLE, a title.
#
  i4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_print_test ( ):

#*****************************************************************************80
#
## i4mat_print_test tests i4mat_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4mat_print_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test i4mat_print, which prints an I4MAT.' )

  m = 5
  n = 6
  a = np.array ( ( \
    ( 11, 12, 13, 14, 15, 16 ), \
    ( 21, 22, 23, 24, 25, 26 ), \
    ( 31, 32, 33, 34, 35, 36 ), \
    ( 41, 42, 43, 44, 45, 46 ), \
    ( 51, 52, 53, 54, 55, 56 ) ) )
  title = '  A 5 x 6 integer matrix:'
  i4mat_print ( m, n, a, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4mat_print_test:' )
  print ( '  Normal end of execution.' )
  return

def i4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## i4mat_print_some prints out a portion of an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d  ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%7d  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def i4mat_print_some_test ( ):

#*****************************************************************************80
#
## i4mat_print_some_test tests i4mat_print_some.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4mat_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4mat_print_some prints some of an I4MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is I4MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4mat_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def i4mat_shortest_path ( n, m ):

#*****************************************************************************80
#
## i4mat_shortest_path computes the shortest distance between all pairs of points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Floyd,
#    Algorithm 97, Shortest Path,
#    Communications of the ACM,
#    Volume 5, Number 6, June 1962, page 345.
#
#  Input:
#
#    integer N, the number of points.
#
#    integer M(N,N).  M(I,J) contains the length of the direct link between 
#    nodes I and J, or Inf if there is no direct link.
#
#  Output:
#
#    integer M(N,N).  M(I,J) contains the distance between nodes I and J,
#    that is, the length of the shortest path between them.  If there
#    is no such path, then M(I,J) will remain Inf.
#
  i4_huge = 2147483647

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( m[j,i] < i4_huge ):
        for k in range ( 0, n ):
          if ( m[i,k] < i4_huge ):
            s = m[j,i] + m[i,k]
            if ( s < m[j,k] ):
              m[j,k] = s

  return m

def i4mat_shortest_path_test ( ):

#*****************************************************************************80
#
## i4mat_shortest_path_test tests i4mat_shortest_path.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  i4_huge = 2147483647

  n = 6

  a = np.array ( [ \
    [  0,  2,  5, -1, -1, -1 ], \
    [ -1,  0,  7,  1, -1,  8 ], \
    [ -1, -1,  0,  4, -1, -1 ], \
    [ -1, -1, -1,  0,  3, -1 ], \
    [ -1, -1,  2, -1,  0,  3 ], \
    [ -1,  5, -1,  2,  4,  0 ] ] )

  print ( '' )
  print ( 'i4mat_shortest_path_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4mat_shortest_path uses Floyd\'s algorithm to find the' )
  print ( '  shortest distance between all pairs of nodes' )
  print ( '  in a directed graph, starting from the initial array' )
  print ( '  of direct node-to-node distances.' )

  print ( '' )
  print ( '  In the initial direct distance array, if' )
  print ( '    A(I,J) = Inf,' )
  print ( '  this indicates there is NO directed link from' )
  print ( '  node I to node J.  In that case, the value of' )
  print ( '  of A(I,J) is essentially "infinity".' )

  i4mat_print ( n, n, a, '  Initial direct-link distances:' )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( a[i,j] == -1 ):
        a[i,j] = i4_huge

  a = i4mat_shortest_path ( n, a )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( a[i,j] == i4_huge ):
        a[i,j] = -1

  print ( '' )
  print ( '  In the final shortest distance array, if' )
  print ( '    A(I,J) = -1,' )
  print ( '  this indicates there is NO directed path from' )
  print ( '  node I to node J.' )

  i4mat_print ( n, n, a, '  Final distance matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4mat_shortest_path_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print prints an R8MAT.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## r8mat_print_test tests r8mat_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_print prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_print_some_test tests r8mat_print_some.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_print_some prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_shortest_path ( n, m ):

#*****************************************************************************80
#
## r8mat_shortest_path computes the shortest distance between all pairs of points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Floyd,
#    Algorithm 97, Shortest Path,
#    Communications of the ACM,
#    Volume 5, Number 6, June 1962, page 345.
#
#  Input:
#
#    integer N, the number of points.
#
#    real M(N,N).  M(I,J) contains the length of the direct link between 
#    nodes I and J, or Inf if there is no direct link.
#
#  Output:
#
#    real M(N,N).  M(I,J) contains the distance between nodes I and J,
#    that is, the length of the shortest path between them.  If there
#    is no such path, then M(I,J) will remain Inf.
#
  import numpy as np

  huge = np.finfo(float).max

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( m[j,i] < huge ):
        for k in range ( 0, n ):
          if ( m[i,k] < huge ):
            s = m[j,i] + m[i,k]
            if ( s < m[j,k] ):
              m[j,k] = s

  return m

def r8mat_shortest_path_test ( ):

#*****************************************************************************80
#
## r8mat_shortest_path_test tests r8mat_shortest_path.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  huge = np.finfo(float).max

  n = 6

  a = np.array ( [ \
    [  0.0,  2.0,  5.0, -1.0, -1.0, -1.0 ], \
    [ -1.0,  0.0,  7.0,  1.0, -1.0,  8.0 ], \
    [ -1.0, -1.0,  0.0,  4.0, -1.0, -1.0 ], \
    [ -1.0, -1.0, -1.0,  0.0,  3.0, -1.0 ], \
    [ -1.0, -1.0,  2.0, -1.0,  0.0,  3.0 ], \
    [ -1.0,  5.0, -1.0,  2.0,  4.0,  0.0 ] ] )
 
  print ( '' )
  print ( 'r8mat_shortest_path_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_shortest_path uses Floyd\'s algorithm to find the' )
  print ( '  shortest distance between all pairs of nodes' )
  print ( '  in a directed graph, starting from the initial array' )
  print ( '  of direct node-to-node distances.' )

  print ( '' )
  print ( '  In the initial direct distance array, if' )
  print ( '    A(I,J) = Inf,' )
  print ( '  this indicates there is NO directed link from' )
  print ( '  node I to node J.  In that case, the value of' )
  print ( '  of A(I,J) is essentially "infinity".' )

  r8mat_print ( n, n, a, '  Initial direct-link distances:' )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( a[i,j] == -1.0 ):
        a[i,j] = np.finfo(float).max

  a = r8mat_shortest_path ( n, a )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( a[i,j] == np.finfo(float).max ):
        a[i,j] = -1.0

  print ( '' )
  print ( '  In the final shortest distance array, if' )
  print ( '    A(I,J) = -1,' )
  print ( '  this indicates there is NO directed path from' )
  print ( '  node I to node J.' )

  r8mat_print ( n, n, a, '  Final distance matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_shortest_path_test' )
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

def toms097_test ( ):

#*****************************************************************************80
#
## toms097_test() tests toms097().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'toms097_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test toms097().' )

  i4mat_shortest_path_test ( )
  r8mat_shortest_path_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'toms097_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  toms097_test ( )
  timestamp ( )

