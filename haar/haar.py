#! /usr/bin/env python3
#
def haar_1d ( n, x ):

#*****************************************************************************80
#
## haar_1d() computes the Haar transform of a vector.
#
#  Discussion:
#
#    For the classical Haar transform, N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real X[N], the vector to be transformed.
#
#  Output:
#
#    real U[N], the transformed vector.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = np.zeros ( n, dtype = np.float64 )
#
#  Determine K, the largest power of 2 such that K <= N.
#
  k = 1
  while ( k * 2 <= n ):
    k = k * 2
  
  while ( 1 < k ):

    k = k // 2

    v[0:k]   = ( u[0:2*k-1:2] + u[1:2*k:2] ) / s
    v[k:2*k] = ( u[0:2*k-1:2] - u[1:2*k:2] ) / s

    u[0:2*k] = v[0:2*k].copy ( )

  return u

def haar_1d_inverse ( n, x ):

#*****************************************************************************80
#
## haar_1d_inverse() computes the inverse Haar transform of a vector.
#
#  Discussion:
#
#    For the classical Haar transform, N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.  
#
#    real X[N], the vector to be transformed.
#
#  Output:
#
#    real U[N], the transformed vector.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = np.zeros ( n )

  k = 1
  while ( k * 2 <= n ):

    v[0:2*k-1:2] = ( u[0:k] + u[0+k:k+k] ) / s
    v[1:2*k:2]   = ( u[0:k] - u[0+k:k+k] ) / s

    u[0:2*k] = v[0:2*k].copy ( )
    k = k * 2

  return u

def haar_1d_test ( ):

#*****************************************************************************80
#
## haar_1d_test() tests haar_1d().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'haar_1d_test():' )
  print ( '  haar_1d() computes the Haar transform of a vector.' )
#
#  Random data.
#
  n = 16
  u = np.random.rand ( n )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  Constant signal.
#
  n = 8
  u = np.ones ( n )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  Linear signal.
#
  n = 16
  u = np.linspace ( 1, n, n )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  Quadratic data.
#
  n = 8
  u = np.array ( [ \
    25.0, 16.0,  9.0,  4.0,  1.0, \
     0.0,  1.0,  4.0 ] )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  N not a power of 2.
#
  n = 99
  u = np.random.rand ( n )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )

  return

def haar_2d ( m, n, x ):

#*****************************************************************************80
#
## haar_2d() computes the Haar transform of an array.
#
#  Discussion:
#
#    For the classical Haar transform, M and N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the dimensions of the array.
#
#    real X[M*N], the array to be transformed.
#
#  Output:
#
#    real U[M*N], the transformed array.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = u.copy ( )
#
#  Determine K, the largest power of 2 such that K <= M.
#
  k = 1
  while ( k * 2 <= m ):
    k = k * 2
#
#  Transform all columns.
#
  while ( 1 < k ):

    k = k // 2

    v[  0:  k,0:n] = ( u[0:2*k-1:2,0:n] + u[1:2*k:2,0:n] ) / s
    v[k+0:k+k,0:n] = ( u[0:2*k-1:2,0:n] - u[1:2*k:2,0:n] ) / s

    u[0:2*k,0:n] = v[0:2*k,0:n].copy ( )
#
#  Determine K, the largest power of 2 such that K <= N.
#
  k = 1
  while ( k * 2 <= n ):
    k = k * 2
#
#  Transform all rows.
#
  while ( 1 < k ):

    k = k // 2

    v[0:m,  0:  k] = ( u[0:m,0:2*k-1:2] + u[0:m,1:2*k:2] ) / s
    v[0:m,k+0:k+k] = ( u[0:m,0:2*k-1:2] - u[0:m,1:2*k:2] ) / s

    u[0:m,0:2*k] = v[0:m,0:2*k].copy ( )

  return u

def haar_2d_inverse ( m, n, x ):

#*****************************************************************************80
#
## haar_2d_inverse() inverts the Haar transform of an array.
#
#  Discussion:
#
#    For the classical Haar transform, M and N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the dimensions of the array.
#
#    real X[M*N], the array to be transformed.
#
#  Output:
#
#    real U[M*N], the transformed array.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = u.copy ( )
#
#  Inverse transform of all rows.
#
  k = 1

  while ( k * 2 <= n ):

    v[0:m,0:2*k-1:2] = ( u[0:m,0:k] + u[0:m,0+k:k+k] ) / s
    v[0:m,1:2*k:2]   = ( u[0:m,0:k] - u[0:m,0+k:k+k] ) / s

    u[0:m,0:2*k] = v[0:m,0:2*k].copy ( )

    k = k * 2
#
#  Inverse transform of all columns.
#
  k = 1

  while ( k * 2 <= m ):

    v[0:2*k-1:2,0:n] = ( u[0:k,0:n] + u[0+k:k+k,0:n] ) / s
    v[1:2*k:2,0:n]   = ( u[0:k,0:n] - u[0+k:k+k,0:n] ) / s

    u[0:2*k,0:n] = v[0:2*k,0:n].copy ( )

    k = k * 2

  return u

def haar_2d_test ( ):

#*****************************************************************************80
#
## haar_2d_test() tests haar_2d().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'haar_2d_test():' )
  print ( '  haar_2d() computes the Haar transform of an array.' )
  print ( '  haar_2d_inverse() inverts the transform.' )
#
#  Demonstrate successful inversion.
#
  m = 16
  n = 4
  u = np.random.rand ( m, n )

  r8mat_print ( m, n, u, '  Input array U:' )

  v = haar_2d ( m, n, u )

  r8mat_print ( m, n, v, '  Transformed array V:' )

  w = haar_2d_inverse ( m, n, v )

  r8mat_print ( m, n, w, '  Recovered array W:' )
#
#  M, N not powers of 2.
#
  m = 37
  n = 53
  u = np.random.rand ( m, n )

  v = haar_2d ( m, n, u )

  w = haar_2d_inverse ( m, n, v )

  err = r8mat_diff_frobenius ( m, n, u, w )

  print ( '' )
  print ( '  M = %d, N = %d, ||haar_2d_inverse(haar_2d(u))-u|| = %g' \
    % ( m, n, err ) )

  return

def haar_test ( ):

#*****************************************************************************80
#
## haar_test() tests haar().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'haar_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test haar().' )

  haar_1d_test ( )
  haar_2d_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'haar_test()' )
  print ( '  Normal end of execution.' )
  return

def r8mat_diff_frobenius ( m, n, a, b ):

#*****************************************************************************80
#
## r8mat_diff_frobenius(): Frobenius norm of the difference of two R8MAT's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
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
#    real A(M,N), B(M,N), the matrices for which we
#    are to compute the Frobenius norm of the difference.
#
#  Output:
#
#    real DIF, the Frobenius norm of A-B.
#
  import numpy as np

  diff = np.sqrt ( np.sum ( np.sum ( ( a[0:m,0:n] - b[0:m,0:n] ) ** 2 ) ) )

  return diff

def r8mat_diff_frobenius_test ( ):

#*****************************************************************************80
#
## r8mat_diff_frobenius_test() tests r8mat_diff_frobenius().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'r8mat_diff_frobenius_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_diff_frobenius() computes the Frobenius norm of' )
  print ( '  the difference of two R8MATs.' )

  m = 2
  n = 3

  a = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], \
    [ 21.0, 22.0, 23.0 ] ] )

  b = np.array ( [ \
    [ 10.0, 13.0, 12.0 ], \
    [ 23.0, 21.0, 24.0 ] ] )

  c = a - b

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )
  r8mat_print ( m, n, c, '  C = A-B:' )

  diff = r8mat_diff_frobenius ( m, n, a, b )

  print ( '' )
  print ( '  Frobenius norm ||A-B|| = %g' % ( diff ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_diff_frobenius_test():' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
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
## r8mat_print_test() tests r8mat_print().
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
  print ( 'r8mat_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_print() prints an R8MAT.' )

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
  print ( 'r8mat_print_test():' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
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
## r8mat_print_some_test() tests r8mat_print_some().
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
  print ( 'r8mat_print_some_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_print_some() prints some of an R8MAT.' )

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
  print ( 'r8mat_print_some_test():' )
  print ( '  Normal end of execution.' )
  return

def r8vec_diff_norm ( n, a, b ):

#*****************************************************************************80
#
## r8vec_diff_norm() returns the L2 norm of the difference of R8VEC's.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    real A(N), B(N), the vectors.
#
#  Output:
#
#    real VALUE, the L2 norm of A - B.
#
  import numpy as np

  value = np.sqrt ( np.sum ( ( a[0:n] - b[0:n] ) ** 2 ) )

  return value

def r8vec_diff_norm_test ( ):

#*****************************************************************************80
#
## r8vec_diff_norm_test() tests r8vec_diff_norm().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_diff_norm_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_diff_norm(): L2 norm of the difference of two R8VECs.' )

  n = 6
  v = np.array ( [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0 ], dtype = np.float64 )
  w = np.array ( [ 1.0, 2.0, 3.0, 5.0, 5.0, 6.0 ], dtype = np.float64 )
  
  print ( '' )
  print ( '  I    V[I]  W[I]' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '%2d  %f  %f' % ( i, v[i], w[i] ) )

  d = r8vec_diff_norm ( n, v, w )

  print ( '' )
  print ( '  L2 norm of vector difference ||V-W|| is %g' % ( d ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_diff_norm_test():' )
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

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  haar_test ( )
  timestamp ( )

