#! /usr/bin/env python3
#
def i4_log_10 ( i ):

#*****************************************************************************80
#
## i4_log_10 returns the integer part of the logarithm base 10 of ABS(X).
#
#  Example:
#
#        I  VALUE
#    -----  --------
#        0    0
#        1    0
#        2    0
#        9    0
#       10    1
#       11    1
#       99    1
#      100    2
#      101    2
#      999    2
#     1000    3
#     1001    3
#     9999    3
#    10000    4
#
#  Discussion:
#
#    i4_log_10 ( I ) + 1 is the number of decimal digits in I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose logarithm base 10 is desired.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm base 10 of
#    the absolute value of X.
#
  import numpy as np

  i = np.floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0
    ten_pow = 10

    i_abs = abs ( i )

    while ( ten_pow <= i_abs ):
      value = value + 1
      ten_pow = ten_pow * 10

  return value

def i4_log_10_test ( ) :

#*****************************************************************************80
#
## i4_log_10_test() tests i4_log_10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ( '' )
  print ( 'i4_log_10_test' )
  print ( '  i4_log_10: whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_log_10_test' )
  print ( '  Normal end of execution.' )
  return

def r8col_flip ( m, n, a ):

#*****************************************************************************80
#
## r8col_flip flips the entries in each column of an R8COL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the array to be examined.
#
#  Output:
#
#    real B(M,N), the flipped array.
#
  import numpy as np

  b = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[i,j] = a[m-1-i,j]

  return b

def r8col_flip_test ( ):

#*****************************************************************************80
#
## r8col_flip_test() tests r8col_flip.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8col_flip_test:' )
  print ( '  r8col_flip flips the columns of an R8COL.' )

  m = 5
  n = 4
  a = r8col_uniform_01 ( m, n )

  r8col_print ( m, n, a, '  Matrix A:' )

  b = r8col_flip ( m, n, a )

  r8col_print ( m, n, b, '  Matrix after column flipping:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_flip_test:' )
  print ( '  Normal end of execution.' )
  return

def r8col_indicator ( m, n ):

#*****************************************************************************80
#
## r8col_indicator sets up an indicator R8COL.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#    The value of each entry suggests its location, as in:
#
#      11  12  13  14
#      21  22  23  24
#      31  32  33  34
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#  Output:
#
#    real TABLE(M,N), the indicator table.
#
  import numpy as np

  table = np.zeros ( ( m, n ), dtype = np.float64 )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      table[i,j] = fac * ( i + 1 ) + ( j + 1 )

  return table

def r8col_indicator_test ( ):

#*****************************************************************************80
#
## r8col_indicator_test() tests r8col_indicator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8col_indicator_test' )
  print ( '  r8col_indicator creates an "indicator" R8COL.' )

  m = 5
  n = 4
  a = r8col_indicator ( m, n )
  r8col_print ( m, n, a, '  The indicator matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_indicator_test' )
  print ( '  Normal end of execution.' )
  return

def r8col_max ( m, n, a ):

#*****************************************************************************80
#
## r8col_max returns the column maximums of an R8COL.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the array to be examined.
#
#  Output:
#
#    real AMAX(N), the maximums of the columns.
#
  import numpy as np

  amax = np.zeros ( n, dtype = np.float64 )

  for j in range ( 0, n ):
    amax[j] = a[0,j]
    for i in range ( 1, m ):
      if ( amax[j] < a[i,j] ):
        amax[j] = a[i,j]

  return amax

def r8col_max_test ( ):

#*****************************************************************************80
#
## r8col_max_test() tests r8col_max
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8col_max_test' )
  print ( '  For an R8COL, an array of column vectors' )
  print ( '  r8col_max computes maximums' )

  a = np.zeros ( [ m, n ] )

  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  r8col_print ( m, n, a, '  The array:' )

  amax = r8col_max ( m, n, a )

  r8vec_print ( n, amax, '  Column maximums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_max_test' )
  print ( '  Normal end of execution.' )
  return

def r8col_mean ( m, n, a ):

#*****************************************************************************80
#
## r8col_mean returns the column means of an R8COL.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Example:
#
#    A =
#      1  2  3
#      2  6  7
#
#    MEAN =
#      1.5  4.0  5.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the array to be examined.
#
#  Output:
#
#    real MEAN(N), the means, or averages, of the columns.
#
  import numpy as np

  mean = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      mean[j] = mean[j] + a[i,j]

  for j in range ( 0, n ):
    mean[j] = mean[j] / float ( m )

  return mean

def r8col_mean_test ( ):

#*****************************************************************************80
#
## r8col_mean_test() tests r8col_mean
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8col_mean_test' )
  print ( '  For an R8COL, an array of column vectors' )
  print ( '  r8col_mean computes means' )

  a = np.zeros ( [ m, n ] )

  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  r8col_print ( m, n, a, '  The array:' )

  mean = r8col_mean ( m, n, a )

  r8vec_print ( n, mean, '  Column means:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_mean_test' )
  print ( '  Normal end of execution.' )
  return

def r8col_min ( m, n, a ):

#*****************************************************************************80
#
## r8col_min returns the column minimums of an R8COL.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the array to be examined.
#
#    real AMIN(N), the minimums of the columns.
#
  import numpy as np

  amin = np.zeros ( n, dtype = np.float64 )

  for j in range ( 0, n ):
    amin[j] = a[0,j]
    for i in range ( 1, m ):
      if ( a[i,j] < amin[j] ):
        amin[j] = a[i,j]

  return amin

def r8col_min_test ( ):

#*****************************************************************************80
#
## r8col_min_test() tests r8col_min
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8col_min_test' )
  print ( '  For an R8COL, an array of column vectors' )
  print ( '  r8col_min computes minimums' )

  a = np.zeros ( [ m, n ] )

  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  r8col_print ( m, n, a, '  The array:' )

  amin = r8col_min ( m, n, a )

  r8vec_print ( n, amin, '  Column minimums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_min_test' )
  print ( '  Normal end of execution.' )
  return

def r8col_normalize_li ( m, n, a ):

#*****************************************************************************80
#
## r8col_normalize_li normalizes an R8COL with the column infinity norm.
#
#  Discussion:
#
#    Each column is scaled so that the entry of maximum norm has the value 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the array to be examined.
#
#  Output:
#
#    real B(M,N), the normalize array.
#
  import numpy as np

  b = a.copy ( )

  for j in range ( 0, n ):

    c = a[0,j]
    for i in range ( 1, m ):
      if ( abs ( c ) < abs ( a[i,j] ) ):
        c = a[i,j]

    if ( c != 0.0 ):
      b[0:m,j] = b[0:m,j] / c

  return b

def r8col_normalize_li_test ( ):

#*****************************************************************************80
#
## r8col_normalize_li_test() tests r8col_normalize_li.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8col_normalize_li_test:' )
  print ( '  r8col_normalize_li normalizes an array A, dividing each' )
  print ( '  column by its maximum element.' )

  m = 5
  n = 4
  a = -5.0
  b = +5.0
  a = r8col_uniform_ab ( m, n, a, b )

  r8col_print ( m, n, a, '  Matrix A:' )

  b = r8col_normalize_li ( m, n, a )

  r8col_print ( m, n, b, '  Matrix after column LI normalization:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_normalize_li_test:' )
  print ( '  Normale end of execution.' )
  return

def r8col_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8col_print prints an R8COL.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2016
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
  r8col_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8col_print_test ( ):

#*****************************************************************************80
#
## r8col_print_test() tests r8col_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8col_print_test' )
  print ( '  r8col_print prints an R8COL.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8col_print ( m, n, v, '  Here is an R8COL:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8col_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8col_print_some prints out a portion of an R8COL.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2016
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

def r8col_print_some_test ( ):

#*****************************************************************************80
#
## r8col_print_some_test() tests r8col_print_some.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8col_print_some_test' )
  print ( '  r8col_print_some prints some of an R8COL.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8col_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8COL:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def r8col_sum ( m, n, a ):

#*****************************************************************************80
#
## r8col_sum sums the columns of an R8COL.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real A(M,N), the array to be examined.
#
#  Output:
#
#    real COLSUM(N), the sums of the columns.
#
  import numpy as np

  colsum = np.zeros ( n )

  for j in range ( 0, n ):
    t = 0.0
    for i in range ( 0, m ):
      t = t + a[i,j]
    colsum[j] = t

  return colsum

def r8col_sum_test ( ):

#*****************************************************************************80
#
## r8col_sum_test() tests r8col_sum
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8col_sum_test' )
  print ( '  For an R8COL, an array of column vectors' )
  print ( '  r8col_sum computes sums' )

  a = np.zeros ( [ m, n ] )

  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  r8col_print ( m, n, a, '  The array:' )

  colsum = r8col_sum ( m, n, a )

  r8vec_print ( n, colsum, '  The column sums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_sum_test' )
  print ( '  Normal end of execution.' )
  return

def r8col_swap ( m, n, a, j1, j2 ):

#*****************************************************************************80
#
## r8col_swap swaps two columns of an R8COL.
#
#  Example:
#
#    Input:
#
#      M = 3, N = 4, I = 2, J = 4
#
#      A = (
#        1  2  3  4
#        5  6  7  8
#        9 10 11 12 )
#
#    Output:
#
#      A = (
#        1  4  3  2
#        5  8  7  6
#        9 12 11 10 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2005
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A(M,N), an array of N columns of length M.
#
#    integer J1, J2, the columns to be swapped.
#
#  Output:
#
#    real A(M,N), the array, with columns swapped.
#
  if ( j1 < 0 or n <= j1 or j2 < 0 or n <= j2 ):
    print ( '' )
    print ( 'r8col_swap - Fatal error!' )
    print ( '  J1 or J2 is out of bounds.' )
    print ( '  J1 =   %d' % ( j1 ) )
    print ( '  J2 =   %d' % ( j2 ) )
    print ( '  N =    %d' % ( n ) )
    raise Exception ( 'r8col_swap - Fatal error!' )

  if ( j1 == j2 ):
    return

  for i in range ( 0, m ):
    t       = a[i,j1]
    a[i,j1] = a[i,j2]
    a[i,j2] = t

  return a

def r8col_swap_test ( ):

#*****************************************************************************80
#
## r8col_swap_test() tests r8col_swap;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 3
  n = 4

  print ( '' )
  print ( 'r8col_swap_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8col_swap swaps two columns of an R8COL.' )

  a = r8col_indicator ( m, n )

  r8col_print ( m, n, a, '  The array:' )

  icol1 = 0
  icol2 = 2

  print ( '' )
  print ( '  Swap columns %d and %d' % ( icol1, icol2 ) )

  a = r8col_swap ( m, n, a, icol1, icol2 )

  r8col_print ( m, n, a, '  The updated matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_swap_test' )
  print ( '  Normal end of execution.' )
  return

def r8col_test ( ):

#*****************************************************************************80
#
## r8col_test() tests r8col().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8col_test():' )
  print ( '  Python version:' )
  print ( '  Test r8col().' )

  i4_log_10_test ( )

  r8col_flip_test ( )
  r8col_indicator_test ( )
  r8col_max_test ( )
  r8col_mean_test ( )
  r8col_min_test ( )
  r8col_normalize_li_test ( )
  r8col_print_test ( )
  r8col_print_some_test ( )
  r8col_sum_test ( )
  r8col_swap_test ( )
  r8col_to_r8vec_test ( )
  r8col_transpose_print_test ( )
  r8col_transpose_print_some_test ( )
  r8col_uniform_01_test ( )
  r8col_uniform_ab_test ( )
  r8col_uniform_abvec_test ( )
  r8col_variance_test ( )

  r8vec_print_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_test():' )
  print ( '  Normal end of execution.' )
  return

def r8col_to_r8vec ( m, n, a ):

#*****************************************************************************80
#
## r8col_to_r8vec copies an R8COL matrix to an R8VEC.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A(M,N), the array to be copied.
#
#  Output:
#
#    real X(M*N), the vector.
#
  import numpy as np

  x = np.zeros ( m * n )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      x[k] = a[i,j]
      k = k + 1

  return x

def r8col_to_r8vec_test ( ):

#*****************************************************************************80
#
## r8col_to_r8vec_test() tests r8col_to_r8vec.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 4
  n = 3

  print ( '' )
  print ( 'r8col_to_r8vec_test' )
  print ( '  r8col_to_r8vec converts an R8COL matrix to an R8VEC vector.' )

  a_r8ge = r8col_indicator ( m, n )

  r8col_print ( m, n, a_r8ge, '  R8COL matrix:' )

  a_r8vec = r8col_to_r8vec ( m, n, a_r8ge )

  r8vec_print ( m * n, a_r8vec, '  Corresponding R8VEC vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_to_r8vec_test:' )
  print ( '  Normal end of execution.' )
  return

def r8col_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8col_transpose_print prints an R8COL, transposed.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2016
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
  r8col_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8col_transpose_print_test ( ):

#*****************************************************************************80
#
## r8col_transpose_print_test() tests r8col_transpose_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8col_transpose_print_test' )
  print ( '  r8col_transpose_print prints an R8COL.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8col_transpose_print ( m, n, v, '  Here is an R8COL, transposed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_transpose_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8col_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8col_transpose_print_some prints a portion of an R8COL, transposed.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
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

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8col_transpose_print_some_test ( ):

#*****************************************************************************80
#
## r8col_transpose_print_some_test() tests r8col_transpose_print_some.
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

  print ( '' )
  print ( 'r8col_transpose_print_some_test' )
  print ( '  r8col_transpose_print_some prints some of an R8COL, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8col_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8COL, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_transpose_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def r8col_uniform_01 ( m, n ):

#*****************************************************************************80
#
## r8col_uniform_01 returns a scaled pseudorandom R8COL.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#  Output:
#
#    real R(M,N), an array of random values between 0 and 1.
#
  import numpy as np
 
  r = np.random.rand ( m, n )

  return r

def r8col_uniform_01_test ( ):

#*****************************************************************************80
#
## r8col_uniform_01_test() tests r8col_uniform_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 May 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 4

  print ( '' )
  print ( 'r8col_uniform_01_test' )
  print ( '  r8col_uniform_01 computes a random R8COL.' )

  v = r8col_uniform_01 ( m, n )

  r8col_print ( m, n, v, '  Random R8COL:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def r8col_uniform_ab ( m, n, a, b ):

#*****************************************************************************80
#
## r8col_uniform_ab returns a scaled pseudorandom R8COL.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A, B, the range of the pseudorandom values.
#
#  Output:
#
#    real R(M,N), an array of random values between A and B.
#
  import numpy as np

  r = a + ( b - a ) * np.random.rand ( m, n )

  return r

def r8col_uniform_ab_test ( ):

#*****************************************************************************80
#
## r8col_uniform_ab_test() tests r8col_uniform_ab.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 4
  a = -1.0
  b = +5.0

  print ( '' )
  print ( 'r8col_uniform_ab_test' )
  print ( '  r8col_uniform_ab computes a random R8COL.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )

  v = r8col_uniform_ab ( m, n, a, b )

  r8col_print ( m, n, v, '  Random R8COL:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_uniform_ab_test:' )
  print ( '  Normal end of execution.' )
  return

def r8col_uniform_abvec ( m, n, a, b ):

#*****************************************************************************80
#
## r8col_uniform_abvec fills an R8COL with scaled pseudorandom numbers.
#
#  Discussion:
#
#    An R8COL is an array of R8 values, regarded as a set of column vectors.
#
#    The user specifies a minimum and maximum value for each row.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in
#    the array.
#
#    real A(M), B(M), the lower and upper limits.
#
#  Output:
#
#    real R(M,N), the array of pseudorandom values.
#
  import numpy as np

  r = np.random.rand ( m, n )

  for i in range ( 0, m ):
    r[i,:] = a[i] + ( b[i] - a[i] ) * r[i,:]

  return r

def r8col_uniform_abvec_test ( ):

#*****************************************************************************80
#
## r8col_uniform_abvec_test() tests r8col_uniform_abvec.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  a = np.array ( ( -1.0, 0.0, 50.0, 100.0, 17.0 ) )
  b = np.array ( ( +1.0, 1.0, 55.0, 100.1, 20.0 ) )

  print ( '' )
  print ( 'r8col_uniform_abvec_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8col_uniform_abvec computes a random scaled R8COL.' )
  print ( '' )
  print ( '   Col         Min         Max' )
  print ( '' )

  for i in range ( 0, m ):
    print ( '  %4d  %10g  %10g' % ( i, a[i], b[i] ) )

  v = r8col_uniform_abvec ( m, n, a, b )

  r8col_print ( m, n, v, '  Random R8COL:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_uniform_abvec_test:' )
  print ( '  Normal end of execution.' )
  return

def r8col_variance ( m, n, a ):

#*****************************************************************************80
#
## r8col_variance returns the variances of an R8COL.
#
#  Discussion:
#
#    An R8COL is an M by N array of R8's, regarded as an array of N columns,
#    each of length M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A(M,N), the array whose variances are desired.
#
#  Output:
#
#    real VARIANCE(N), the variances of the rows.
#
  import numpy as np

  variance = np.zeros ( n )

  for j in range ( 0, n ):

    t = 0.0
    for i in range ( 0, m ):
      t = t + a[i,j]
    mean = t / float ( m )

    t = 0.0
    for i in range ( 0, m ):
      t = t + ( a[i,j] - mean ) ** 2

    if ( 1 < m ):
      t = t / float ( m - 1 )
    else:
      t = 0.0

    variance[j] = t

  return variance

def r8col_variance_test ( ):

#*****************************************************************************80
#
## r8col_variance_test() tests r8col_variance.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'r8col_variance_test' )
  print ( '  For an R8COL, an array of column vectors' )
  print ( '  r8col_variance computes variances' )

  a = np.zeros ( [ m, n ] )

  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8col_print ( m, n, a, '  The array:' )

  variance = r8col_variance ( m, n, a )

  r8vec_print ( n, variance, '  Column variances:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_variance_test' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print prints an R8VEC.
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
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## r8vec_print_test() tests r8vec_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_print_test' )
  print ( '  r8vec_print prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_print_test:' )
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
  r8col_test ( )
  timestamp ( )

