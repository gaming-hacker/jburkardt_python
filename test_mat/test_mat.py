#! /usr/bin/env python3
#
from __future__ import division

def a123_matrix ( ):

#*****************************************************************************80
#
## a123_matrix() returns the A123 matrix.
#
#  Example:
#
#    1 2 3
#    4 5 6
#    7 8 9
#
#  Properties:
#
#    A is integral.
#
#    A is not symmetric.
#
#    A is singular.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(3,3), the matrix.
#
  import numpy as np

  a = np.zeros ( ( 3, 3 ) )

  k = 0
  for i in range ( 0, 3 ):
    for j in range ( 0, 3 ):
      k = k + 1
      a[i,j] = float ( k )

  return a

def a123_determinant ( ):

#*****************************************************************************80
#
## a123_determinant() returns the determinant of the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 0.0

  return value

def a123_eigen_left ( ):

#*****************************************************************************80
#
## a123_eigen_left() returns the left eigenvectors of the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(3,3), the eigenvectors.
#
  import numpy as np

  a = np.array ( [ \
    [ -0.464547273387671, -0.570795531228578, -0.677043789069485 ], \
    [ -0.882905959653586, -0.239520420054206,  0.403865119545174 ], \
    [  0.408248290463862, -0.816496580927726,  0.408248290463863 ] ] )

  return a

def a123_eigen_right ( ):

#*****************************************************************************80
#
## a123_eigen_right() returns the right eigenvectors of the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(3,3), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ -0.231970687246286,  -0.785830238742067,   0.408248290463864 ], \
    [ -0.525322093301234,  -0.086751339256628,  -0.816496580927726 ], \
    [ -0.818673499356181,   0.612327560228810,   0.408248290463863 ] ] )

  return a

def a123_eigenvalues ( ):

#*****************************************************************************80
#
## a123_eigenvalues() returns the eigenvalues of the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real LAM(3), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
   [ 16.116843969807043 ], \
   [ -1.116843969807043 ], \
   [  0.0 ] ] )

  return lam

def a123_null_left ( ):

#*****************************************************************************80
#
## a123_null_left() returns a left null vector for the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(3), a left null vector.
#
  import numpy as np

  x = np.array ( [ [ 1.0 ], [ -2.0 ], [ 1.0 ] ] )

  return x

def a123_null_right ( ):

#*****************************************************************************80
#
## a123_null_right() returns a right null vector for the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(3), a right null vector.
#
  import numpy as np

  x = np.array ( [ [ 1.0 ], [ -2.0 ], [ 1.0 ] ] )

  return x

def a123_plu ( ):

#*****************************************************************************80
#
## a123_plu() returns the PLU factors of the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real P(3,3), L(3,3), U(3,3), the PLU factors.
#
  import numpy as np

  p = np.array ( [ \
     [ 0.0,     1.0,     0.0 ], \
     [ 0.0,     0.0,     1.0 ], \
     [ 1.0,     0.0,     0.0 ] ] )

  l = np.array ( [ \
      [ 1.000000000000000,                 0.0,                 0.0 ], \
      [ 0.142857142857143,   1.000000000000000,                 0.0 ], \
      [ 0.571428571428571,   0.500000000000000,   1.000000000000000 ] ] )

  u = np.array ( [ \
   [ 7.000000000000000,   8.000000000000000,   9.000000000000000 ], \
   [               0.0,   0.857142857142857,   1.714285714285714 ], \
   [               0.0,                 0.0,   0.000000000000000 ] ] )

  return p, l, u

def a123_rhs ( ):

#*****************************************************************************80
#
## a123_rhs() returns the A123 right hand side.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real B(3), the right hand side vector.
#
  import numpy as np

  b = np.array ( [ [ 10.0 ], [ 28.0 ], [ 46.0 ] ] )

  return b

def a123_solution ( ):

#*****************************************************************************80
#
## a123_solution() returns the A123 solution vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(3), the solution.
#
  import numpy as np

  x = np.array ( [ [ 3.0 ], [ 2.0 ], [ 1.0 ] ] )

  return x

def aegerter_matrix ( n ):

#*****************************************************************************80
#
## aegerter_matrix() returns the AEGERTER matrix.
#
#  Formula:
#
#    if ( I == N )
#      A(I,J) = J
#    else if ( J == N )
#      A(I,J) = I
#    else if ( I == J )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  1
#    0  1  0  0  2
#    0  0  1  0  3
#    0  0  0  1  4
#    1  2  3  4  5
#
#  Square Properties:
#
#    A is integral: int ( A ) = A.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is border-banded.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
 
  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == n - 1 ):
        a[i,j] = j + 1
      elif ( j == n - 1 ):
        a[i,j] = i + 1
      elif ( i == j ):
        a[i,j] = 1.0
      else:
        a[i,j] = 0.0

  return a

def aegerter_condition ( n ):

#*****************************************************************************80
#
## aegerter_condition() returns the L1 condition of the AEGERTER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real COND, the L1 condition.
#
  a = aegerter_matrix ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )

  b = aegerter_inverse ( n )
  b_norm = r8mat_norm_l1 ( n, n, b )

  rcond = a_norm * b_norm

  return rcond

def aegerter_determinant ( n ):

#*****************************************************************************80
#
## aegerter_determinant() returns the determinant of the AEGERTER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = ( n - ( ( n - 1 ) * n * ( 2 * n - 1 ) ) / 6 )

  return determ

def aegerter_eigenvalues ( n ):

#*****************************************************************************80
#
## aegerter_eigenvalues() returns the eigenvalues of the AEGERTER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  determ = n - ( ( n - 1 ) * n * ( 2 * n - 1 ) ) / 6

  lam[0] = 0.5 * ( n + 1 - np.sqrt ( ( n + 1 ) ** 2 - 4.0 * determ ) )

  for i in range ( 1, n - 1 ):
    lam[i] = 1.0

  lam[n-1] = 0.5 * ( n + 1 + np.sqrt ( ( n + 1 ) ** 2 - 4.0 * determ ) )

  return lam

def aegerter_inverse ( n ):

#*****************************************************************************80
#
## aegerter_inverse() returns the inverse of the AEGERTER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  v = np.zeros ( n )

  for i in range ( 0, n - 1 ):
    v[i] = i + 1

  for j in range ( 0, n - 1 ):
    a[j,j] = 1.0
    for i in range ( 0, n - 1 ):
      a[i,j] = a[i,j] - v[i] * v[j] / ( n * n )

  for i in range ( 0, n - 1 ):
    a[i,n-1] = v[i] / ( n * n )

  for j in range ( 0, n - 1 ):
    a[n-1,j] = v[j] / ( n * n )

  a[n-1,n-1] = - 1.0 / ( n * n )

  return a

def antisymmetric_random_determinant ( n, key ):

#*****************************************************************************80
#
## antisymmetric_random_determinant(): determinant of ANTISYMMETRIC_RANDOM matrix.
#
#  Discussion:
#
#    If N is odd, the determinant is 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michael Wimmer,
#    Algorithm 923: Efficient Numerical Computation of the Pfaffian for
#    Dense and Banded Skew-Symmetric Matrices,
#    ACM Transactions on Mathematical Software,
#    Volume 38, Number 4, Article 30, August 2012.
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    determ = 0.0
  else:
    A = antisymmetric_random_matrix ( n, key )
    determ = ( pfaffian_ltl ( A ) ) ** 2

  return determ

def antisymmetric_random_matrix ( n, key ):

#*****************************************************************************80
#
## antisymmetric_random_matrix() returns the ANTISYMMETRIC_RANDOM matrix.
#
#  Discussion:
#
#    This is a random antisymmetric matrix.
#
#  Example:
#
#    N = 5
#
#     0.0000  -0.1096   0.0813   0.9248   -0.0793
#     0.1096   0.0000   0.1830   0.1502    0.8244
#    -0.0813  -0.1830   0.0000   0.0899   -0.2137
#    -0.9248  -0.1502  -0.0899   0.0000   -0.4804
#     0.0793  -0.8244   0.2137   0.4804    0.0000
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is antisymmetric: A' = -A.
#
#    Because A is antisymmetric, it is normal: A*A' = A'*A.
#
#    Because A is normal, it is diagonalizable.
#
#    Because A is diagonalizable, it is not defective: 
#    it has a full set of eigenvectors.
#
#    The diagonal of A is zero.
#
#    All the eigenvalues of A are imaginary.
#
#    If N is odd, then det ( A ) = 0.
#
#    A is not diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2008
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  n2 = ( n * ( n - 1 ) ) // 2
  
  np.random.seed ( key )

  t = np.random.normal ( 0.0, 1.0, size = n2 )

  k = 0
  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      A[i,j] =   t[k]
      A[j,i] = - t[k]
      k = k + 1

  return A

def antisymmetric_random_test ( ):

#*****************************************************************************80
#
## antisymmetric_random_test() tests antisymmetric_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'antisymmetric_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  antisymmetric_random_matrix() computes the antisymmetric_random matrix.' )

  m = 5
  n = 5
  key = 123456789
  A = antisymmetric_random_matrix ( n, key )
  r8mat_print ( m, n, A, '  antisymmetric_random matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'antisymmetric_random_test' )
  print ( '  Normal end of execution.' )
  return

def archimedes_matrix ( ):

#*****************************************************************************80
#
## archimedes_matrix() returns the 7 by 8 ARCHIMEDES matrix.
#
#  Formula:
#
#      6   -5    0   -6    0    0    0    0
#      0   20   -9  -20    0    0    0    0
#    -13    0   42  -42    0    0    0    0
#      0   -7    0    0   12   -7    0    0
#      0    0   -9    0    0   20   -9    0
#      0    0    0  -11    0    0   30  -11
#    -13    0    0    0  -13    0    0   42
#
#  Discussion:
#
#    "The sun god had a herd of cattle, consisting of bulls and cows,
#    one part of which was white, a second black, a third spotted, and
#    a fourth brown.  Among the bulls, the number of white ones was
#    one half plus one third the number of the black greater than
#    the brown; the number of the black, one quarter plus one fifth
#    the number of the spotted greater than the brown; the number of
#    the spotted, one sixth and one seventh the number of the white
#    greater than the brown.  Among the cows, the number of white ones
#    was one third plus one quarter of the total black cattle; the number
#    of the black, one quarter plus one fifth the total of the spotted
#    cattle; the number of spotted, one fifth plus one sixth the total
#    of the brown cattle; the number of the brown, one sixth plus one
#    seventh the total of the white cattle.  What was the composition
#    of the herd?"
#
#    The 7 relations involving the 8 numbers W, X, Y, Z, w, x, y, z,
#    have the form:
#
#      W = ( 5/ 6) *   X + Z
#      X = ( 9/20) *   Y + Z
#      Y = (13/42) *   W + Z
#      w = ( 7/12) * ( X + x )
#      x = ( 9/20) * ( Y + y )
#      y = (11/30) * ( Z + z )
#      z = (13/42) * ( W + w )
#
#    These equations may be multiplied through to an integral form
#    that is embodied in the above matrix.
#
#    A more complicated second part of the problem imposes additional
#    constraints (W+X must be square, Y+Z must be a triangular number).
#
#  Properties:
#
#    A is integral: int ( A ) = A.
#
#    A has full row rank.
#
#    It is desired to know a solution X in positive integers of
#
#      A * X = 0.
#
#    The null space of A is spanned by multiples of the null vector:
#
#      [ 10,366,482 ]
#      [  7,460,514 ]
#      [  7,358,060 ]
#      [  4,149,387 ]
#      [  7,206,360 ]
#      [  4,893,246 ]
#      [  3,515,820 ]
#      [  5,439,213 ]
#
#    and this is the smallest positive integer solution of the
#    equation A * X = 0.
#
#    Thus, for the "simple" part of Archimedes's problem, the total number
#    of cattle of the Sun is 50,389,082.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998.
#
#  Output:
#
#    integer A(7,8), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
   [   6, -5,  0,  -6,   0,  0,  0,   0 ], \
   [   0, 20, -9, -20,   0,  0,  0,   0 ], \
   [ -13,  0, 42, -42,   0,  0,  0,   0 ], \
   [   0, -7,  0,   0,  12, -7,  0,   0 ], \
   [   0,  0, -9,   0,   0, 20, -9,   0 ], \
   [   0,  0,  0, -11,   0,  0, 30, -11 ], \
   [ -13,  0,  0,   0, -13,  0,  0,  42 ] ] )

  return a

def archimedes_null_right ( ):

#*****************************************************************************80
#
## archimedes_null_right() returns a right null vector for the ARCHIMEDES matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(8), a right null vector.
#
  import numpy as np

  x = np.array ( [  \
    [ 10366482.0 ], \
    [  7460514.0 ], \
    [  7358060.0 ], \
    [  4149387.0 ], \
    [  7206360.0 ], \
    [  4893246.0 ], \
    [  3515820.0 ], \
    [  5439213.0 ] ] )

  return x

def archimedes_test ( ):

#*****************************************************************************80
#
## archimedes_test() tests archimedes_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ARCHIMEDES_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  archimedes_matrix() computes the ARCHIMEDES matrix.' )

  m = 7
  n = 8
  a = archimedes_matrix ( )
  r8mat_print ( m, n, a, '  ARCHIMEDES matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCHIMEDES_test' )
  print ( '  Normal end of execution.' )
  return

def bab_matrix ( n, alpha, beta ):

#*****************************************************************************80
#
## bab_matrix() returns the BAB matrix.
#
#  Example:
#
#    N = 5
#    ALPHA = 5, BETA = 2
#
#    5  2  .  .  .
#    2  5  2  .  .
#    .  2  5  2  .
#    .  .  2  5  2
#    .  .  .  2  5
#
#  Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is Toeplitz: constant along diagonals.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    CM da Fonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, BETA, the parameters.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = alpha

  for i in range ( 0, n - 1 ):
    a[i,i+1] = beta
    a[i+1,i] = beta
 
  return a

def bab_test ( ):

#*****************************************************************************80
#
## bab_test() tests bab_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bab_matrix( ) computes the BAB matrix.' )

  n = 5
  alpha = np.random.rand ( )
  beta = np.random.rand ( )
  a = bab_matrix ( n, alpha, beta )
  r8mat_print ( n, n, a, '  BAB matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'bab_test' )
  print ( '  Normal end of execution.' )
  return

def bab_condition ( n, alpha, beta ):

#*****************************************************************************80
#
## bab_condition() returns the L1 condition of the BAB matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, BETA, the parameters.
#
#  Output:
#
#    real COND, the L1 condition number.
#
  a = bab_matrix ( n, alpha, beta )
  a_norm = r8mat_norm_l1 ( n, n, a )

  b = bab_inverse ( n, alpha, beta )
  b_norm = r8mat_norm_l1 ( n, n, b )

  cond = a_norm * b_norm

  return cond

def bab_determinant ( n, alpha, beta ):

#*****************************************************************************80
#
## bab_determinant() returns the determinant of the BAB matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, BETA, parameters that define the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ_nm1 = alpha

  if ( n == 1 ):
    determ = determ_nm1
    return determ

  determ_nm2 = determ_nm1
  determ_nm1 = alpha * alpha - beta * beta

  if ( n == 2 ):
    determ = determ_nm1
    return determ

  for i in range ( n - 2, 0, -1 ):
 
    determ = alpha * determ_nm1 - beta * beta * determ_nm2

    determ_nm2 = determ_nm1
    determ_nm1 = determ

  return determ

def bab_eigen_right ( n, alpha, beta ):

#*****************************************************************************80
#
## bab_eigen_right() returns the right eigenvectors of the BAB matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real ALPHA, BETA, the parameters.
#
#  Output:
#
#    real A(N,N), the right eigenvector matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( ( i + 1 ) *  ( j + 1 ) ) * np.pi / float ( n + 1 )
      a[i,j] = np.sqrt ( 2.0 / float ( n + 1 ) ) * np.sin ( angle )

  return a

def bab_eigenvalues ( n, alpha, beta ):

#*****************************************************************************80
#
## bab_eigenvalues() returns the eigenvalues of the BAB matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, BETA, the parameters.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    lam[i] = alpha + 2.0 * beta * np.cos ( angle )

  return lam

def bab_inverse ( n, alpha, beta ):

#*****************************************************************************80
#
## bab_inverse() returns the inverse of the BAB matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, BETA, the parameters.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  if ( beta == 0.0 ):

    if ( alpha == 0.0 ):
      print ( '' )
      print ( 'bab_inverse - Fatal error!' )
      print ( '  ALPHA = BETA = 0.' )
      raise Exception ( 'bab_inverse - Fatal error!' )

    for i in range ( 0, n ):
      a[i,i] = 1.0 / alpha

  else:

    x = 0.5 * alpha / beta

    u = cheby_u_polynomial ( n, x )

    for i in range ( 1, n + 1 ):
      for j in range ( 1, i + 1 ):
        a[i-1,j-1] = r8_mop ( i + j ) * u[j-1] * u[n-i] / u[n] / beta
      for j in range ( i + 1, n + 1 ):
        a[i-1,j-1] = r8_mop ( i + j ) * u[i-1] * u[n-j] / u[n] / beta

  return a

def bauer_matrix ( ):

#*****************************************************************************80
#
## bauer_matrix() returns the BAUER matrix.
#
#  Example:
#
#    -74   80  18 -11  -4  -8
#     14  -69  21  28   0   7
#     66  -72  -5   7   1   4
#    -12   66 -30 -23   3  -3
#      3    8  -7  -4   1   0
#      4  -12   4   4   0   1
#
#  Properties:
#
#    The matrix is integral.
#
#    The inverse matrix is integral.
#
#    The matrix is ill-conditioned.
#
#    The determinant is 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Virginia Klema, Alan Laub,
#    The Singular Value Decomposition: Its Computation and Some Applications,
#    IEEE Transactions on Automatic Control,
#    Volume 25, Number 2, April 1980.
#
#  Output:
#
#    real A(6,6), the matrix.
#
  import numpy as np

  a = np.array ( [ \
   [ -74.0,  80.0,  18.0, -11.0,  -4.0,  -8.0 ], \
   [  14.0, -69.0,  21.0,  28.0,   0.0,   7.0 ], \
   [  66.0, -72.0,  -5.0,   7.0,   1.0,   4.0 ], \
   [ -12.0,  66.0, -30.0, -23.0,   3.0,  -3.0 ], \
   [   3.0,   8.0,  -7.0,  -4.0,   1.0,   0.0 ], \
   [   4.0, -12.0,   4.0,   4.0,   0.0,   1.0 ] ] )

  return a

def bauer_condition ( ):

#*****************************************************************************80
#
## bauer_condition() returns the L1 condition of the BAUER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the condition.
#
  a_norm = 307.0
  b_norm = 27781.0
  value = a_norm * b_norm

  return value

def bauer_determinant ( ):

#*****************************************************************************80
#
## bauer_determinant() returns the determinant of the BAUER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def bauer_inverse ( ):

#*****************************************************************************80
#
## bauer_inverse() returns the inverse of the BAUER matrix.
#
#  Example:
#
#      1       0      -7     -40     131     -84
#      0       1       7      35    -112      70
#     -2       2      29     155    -502     319
#     15     -12    -192   -1034    3354   -2130
#     43     -42    -600   -3211   10406   -6595
#    -56      52     764    4096  -13276    8421
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(6,6), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [   1.0,       0.0,      -7.0,     -40.0,     131.0,     -84.0 ], \
    [   0.0,       1.0,       7.0,      35.0,    -112.0,      70.0 ], \
    [  -2.0,       2.0,      29.0,     155.0,    -502.0,     319.0 ], \
    [  15.0,     -12.0,    -192.0,   -1034.0,    3354.0,   -2130.0 ], \
    [  43.0,     -42.0,    -600.0,   -3211.0,   10406.0,   -6595.0 ], \
    [ -56.0,      52.0,     764.0,    4096.0,  -13276.0,    8421.0 ] ] )

  return a

def bauer_test ( ):

#*****************************************************************************80
#
## bauer_test() tests bauer_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bauer_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bauer_matrix() computes the BAUER matrix.' )

  n = 6
  a = bauer_matrix ( )
  r8mat_print ( n, n, a, '  BAUER matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'bauer_test' )
  print ( '  Normal end of execution.' )
  return

def bernstein_matrix ( n ):

#*****************************************************************************80
#
## bernstein_matrix() returns the BERNSTEIN matrix.
#
#  Discussion:
#
#    The Bernstein matrix of order N is an NxN matrix A which can be used to
#    transform a vector of power basis coefficients C representing a polynomial 
#    P(X) to a corresponding Bernstein basis coefficient vector B:
#
#      B = A * C
#
#    The N power basis vectors are ordered as (1,X,X^2,...X^(N-1)) and the N 
#    Bernstein basis vectors as ((1-X)^(N-1), X*(1-X)^(N-2),...,X^(N-1)).
#
#  Example:
#
#    N = 5
#
#    1    -4     6    -4     1
#    0     4   -12    12    -4
#    0     0     6   -12     6
#    0     0     0     4    -4
#    0     0     0     0     1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the Bernstein matrix.
#
  import numpy as np
  from scipy.special import comb

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      a[i,j] = r8_mop ( j - i ) * comb ( n - 1 - i, j - i ) \
        * comb ( n - 1, i )

  return a

def bernstein_test ( ):

#*****************************************************************************80
#
## bernstein_test() tests bernstein_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bernstein_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bernstein_matrix() computes the BERNSTEIN matrix.' )

  m = 5
  n = m

  a = bernstein_matrix ( n )
 
  r8mat_print ( m, n, a, '  BERNSTEIN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'bernstein_test' )
  print ( '  Normal end of execution.' )
  return

def bernstein_determinant ( n ):

#*****************************************************************************80
#
## bernstein_determinant() returns the determinant of the BERNSTEIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  from scipy.special import comb

  value = 1.0
  for i in range ( 0, n ):
    value = value * comb ( n - 1, i )

  return value

def bernstein_inverse ( n ):

#*****************************************************************************80
#
## bernstein_inverse() returns the inverse of the BERNSTEIN matrix.
#
#  Discussion:
#
#    The inverse Bernstein matrix of order N is an NxN matrix A which can 
#    be used to transform a vector of Bernstein basis coefficients B
#    representing a polynomial P(X) to a corresponding power basis 
#    coefficient vector C:
#
#      C = A * B
#
#    The N power basis vectors are ordered as (1,X,X^2,...X^(N-1)) and the N 
#    Bernstein basis vectors as ((1-X)^(N-1), X*(1_X)^(N-2),...,X^(N-1)).
#
#  Example:
#
#    N = 5
#
#   1.0000    1.0000    1.0000    1.0000    1.0000
#        0    0.2500    0.5000    0.7500    1.0000
#        0         0    0.1667    0.5000    1.0000
#        0         0         0    0.2500    1.0000
#        0         0         0         0    1.0000
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the inverse Bernstein matrix.
#
  from scipy.special import comb
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      a[i,j] = comb ( j, i ) / comb ( n - 1, i )

  return a

def bernstein_poly_01 ( n, x ):

#*****************************************************************************80
#
## bernstein_poly_01() evaluates the Bernstein polynomials defined on [0,1].
#
#  Discussion:
#
#    The Bernstein polynomials are assumed to be based on [0,1].
#
#  Formula:
#
#    B(N,I)(X) = [N!/(I!*(N-I)!)] * (1-X)^(N-I) * X^I
#
#  First values:
#
#    B(0,0)(X) = 1
#
#    B(1,0)(X) =      1-X
#    B(1,1)(X) =               X
#
#    B(2,0)(X) =     (1-X)^2
#    B(2,1)(X) = 2 * (1-X)   * X
#    B(2,2)(X) =               X^2
#
#    B(3,0)(X) =     (1-X)^3
#    B(3,1)(X) = 3 * (1-X)^2 * X
#    B(3,2)(X) = 3 * (1-X)   * X^2
#    B(3,3)(X) =               X^3
#
#    B(4,0)(X) =     (1-X)^4
#    B(4,1)(X) = 4 * (1-X)^3 * X
#    B(4,2)(X) = 6 * (1-X)^2 * X^2
#    B(4,3)(X) = 4 * (1-X)   * X^3
#    B(4,4)(X) =               X^4
#
#  Special values:
#
#    B(N,I)(X) has a unique maximum value at X = I/N.
#
#    B(N,I)(X) has an I-fold zero at 0 and and N-I fold zero at 1.
#
#    B(N,I)(1/2) = C(N,K) / 2^N
#
#    For a fixed X and N, the polynomials add up to 1:
#
#      Sum ( 0 <= I <= N ) B(N,I)(X) = 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the degree of the Bernstein polynomials to be
#    used.  For any N, there is a set of N+1 Bernstein polynomials,
#    each of degree N, which form a basis for polynomials on [0,1].
#
#    real X, the evaluation point.
#
#  Output:
#
#    real B[0:N], the values of the N+1 Bernstein polynomials at X.
#
  import numpy as np

  b = np.zeros ( n + 1 )

  if ( n == 0 ):
 
    b[0] = 1.0
 
  elif ( 0 < n ):
 
    b[0] = 1.0 - x
    b[1] = x
 
    for i in range ( 1, n ):
      b[i+1] = x * b[i]
      for j in range ( i - 1, -1, -1 ):
        b[j+1] = x * b[j] + ( 1.0 - x ) * b[j+1]
      b[0] = ( 1.0 - x ) * b[0]

  return b

def bernstein_vandermonde ( n ):

#*****************************************************************************80
#
## bernstein_vandermonde() returns the Bernstein Vandermonde matrix.
#
#  Discussion:
#
#    The Bernstein Vandermonde matrix of order N is constructed by
#    evaluating the N Bernstein polynomials of degree N-1 at N equally
#    spaced points between 0 and 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the Bernstein Vandermonde matrix.
#
  import numpy as np

  v = np.zeros ( [ n, n ] )

  if ( n == 1 ):
    v[0,0] = 1.0
    return v

  for i in range ( 0, n ):
    x = float ( i ) / float ( n - 1 )
    b = bernstein_poly_01 ( n - 1, x )
    for j in range ( 0, n ):
      v[i,j] = b[j]

  return v

def bernstein_vandermonde_test ( ):

#*****************************************************************************80
#
## bernstein_vandermonde_test() tests bernstein_vandermonde().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bernstein_vandermonde_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bernstein_vandermonde returns an NxN matrix whose (I,J) entry' )
  print ( '  is the value of the J-th Bernstein polynomial of degree N-1' )
  print ( '  evaluated at the I-th equally spaced point in [0,1].' )

  n = 8
  a = bernstein_vandermonde ( n )
  r8mat_print ( n, n, a, '  Bernstein Vandermonde ( 8 ):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'bernstein_vandermonde_test' )
  print ( '  Normal end of execution.' )
  return

def bimarkov_random_matrix ( n, key ):

#*****************************************************************************80
#
## bimarkov_random_matrix() returns the BIMARKOV_RANDOM matrix.
#
#  Discussion:
#
#    This is a random biMarkov or doubly stochastic matrix.
#
#  Example:
#
#    N = 5
#
#    1/5   1/5   1/5   1/5   1/5
#    1/2   1/2    0     0     0
#    1/6   1/6   2/3    0     0
#    1/12  1/12  1/12  3/4    0
#    1/20  1/20  1/20  1/20  4/5
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    0 <= A(I,J) <= 1.0 for every I and J.
#
#    A has constant row sum 1.
#
#    A has constant column sum 1.
#
#    All the eigenvalues of A have modulus 1.
#
#    1 is always an eigenvalue of A, with eigenvector (1,1,...,1).
#
#    The eigenvalue 1 lies on the boundary of all the Gershgorin
#    row or column sum disks.
#
#    Every doubly stochastic matrix is a combination
#      A = w1 * P1 + w2 * P2 + ... + wk * Pk
#    of permutation matrices, with positive weights w that sum to 1.
#    (Birkhoff's theorem, see Horn and Johnson.)
#
#    A is a Markov matrix.
#
#    A is a transition matrix.
#
#    A is not diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Roger Horn, Charles Johnson,
#    Matrix Analysis,
#    Cambridge, 1985.
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#

#
#  Get a random orthogonal matrix.
#
  a = orthogonal_random_matrix ( n, key )
#
#  Square each entry.
#
  a = a**2

  return a

def bimarkov_random_test ( ):

#*****************************************************************************80
#
## bimarkov_random_test() tests bimarkov_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bimarkov_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bimarkov_random_matrix computes the bimarkov_random matrix.' )

  n = 3
  key = 123456789
  a = bimarkov_random_matrix ( n, key )
  r8mat_print ( n, n, a, '  bimarkov_random matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'bimarkov_random_test' )
  print ( '  Normal end of execution.' )
  return

def bis_matrix ( alpha, beta, m, n ):

#*****************************************************************************80
#
## bis_matrix() returns the BIS matrix().
#
#  Discussion:
#
#    BIS is a bidiagonal scalar matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = ALPHA
#    else if ( J = I+1 )
#      A(I,J) = BETA
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 7, BETA = 2, M = 5, N = 4
#
#    7  2  0  0
#    0  7  2  0
#    0  0  7  2
#    0  0  0  7
#    0  0  0  0
#
#  Rectangular Properties:
#
#    A is bidiagonal.
#
#    Because A is bidiagonal, it has property A (bipartite).
#
#    A is upper triangular.
#
#    A is banded with bandwidth 2.
#
#    A is Toeplitz: constant along diagonals.
#
#  Square Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular if and only if ALPHA is nonzero.
#
#    det ( A ) = ALPHA^N.
#
#    LAMBDA(1:N) = ALPHA.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, BETA, the scalars which define the
#    diagonal and first superdiagonal of the matrix.
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )
  
  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( j == i ):
        a[i,j] = alpha
      elif ( j == i + 1 ):
        a[i,j] = beta
      else:
        a[i,j] = 0.0

  return a

def bis_test ( ):

#*****************************************************************************80
#
## bis_test() tests bis_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bis_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bis_matrix() computes the BIS matrix.' )

  m = 5
  n = 5
  alpha = np.random.rand ( )
  beta = np.random.rand ( )
  a = bis_matrix ( alpha, beta, m, n )
  r8mat_print ( m, n, a, '  BIS matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'bis_test' )
  print ( '  Normal end of execution.' )
  return

def bis_condition ( alpha, beta, n ):

#*****************************************************************************80
#
## bis_condition() computes the L1 condition of the BIS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, BETA, the scalars which define the
#    diagonal and first superdiagonal of the matrix.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = abs ( alpha ) + abs ( beta )
  ba = abs ( beta / alpha )
  b_norm = ( ba ** n - 1.0 ) / ( ba - 1.0 ) / abs ( alpha )
  value = a_norm * b_norm

  return value

def bis_determinant ( alpha, beta, n ):

#*****************************************************************************80
#
## bis_determinant() returns the determinant of the BIS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, BETA, the scalars which define the
#    diagonal and first superdiagonal of the matrix.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = alpha ** n

  return determ

def bis_eigenvalues ( alpha, beta, n ):

#*****************************************************************************80
#
## bis_eigenvalues() returns the eigenvalues of the BIS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, BETA, the scalars which define the
#    diagonal and first superdiagonal of the matrix.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real LAM(N), the eigenvalues of the matrix.
#
  import numpy as np

  lam = np.ones ( n )

  lam = lam * alpha

  return lam

def bis_inverse ( alpha, beta, n ):

#*****************************************************************************80
#
## bis_inverse() returns the inverse of a bidiagonal scalar matrix.
#
#  Formula:
#
#    if ( I <= J )
#      A(I,J) = (-BETA)^(J-I) / ALPHA^(J+1-I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 7.0, BETA = 2.0, N = 4
#
#    0.1429   -0.0408    0.0117   -0.0033
#        0     0.1429   -0.0408    0.0117
#        0          0    0.1429   -0.0408
#        0          0         0    0.1429
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is upper triangular
#
#    A is Toeplitz: constant along diagonals.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    det ( A ) = (1/ALPHA)^N.
#
#    LAMBDA(1:N) = 1 / ALPHA.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, BETA, the scalars which define the
#    diagonal and first superdiagonal of the matrix.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  if ( alpha == 0.0 ):
    print ( '' )
    print ( 'bis_inverse - Fatal error!' )
    print ( '  The input parameter ALPHA was 0.' )
    raise Exception ( 'bis_inverse - Fatal error!' )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i <= j ):
        a[i,j] = ( - beta ) ** ( j - i ) / alpha ** ( j - i + 1 )

  return a

def biw_matrix ( n ):

#*****************************************************************************80
#
## biw_matrix() returns the BIW matrix.
#
#  Discussion:
#
#    BIW is a bidiagonal matrix of Wilkinson.   Originally, this matrix
#    was considered for N = 100.
#
#  Formula:
#
#    if ( I == J )
#      A(I,J) = 0.5 + I / ( 10 * N )
#    else if ( J == I+1 )
#      A(I,J) = -1.0
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#    0.52 -1.00  0.00  0.00  0.00
#    0.00  0.54 -1.00  0.00  0.00
#    0.00  0.00  0.56 -1.00  0.00
#    0.00  0.00  0.00  0.58 -1.00
#    0.00  0.00  0.00  0.00  0.60
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )
  
  for i in range ( 0, n ):
    a[i,i] = 0.5 + float ( i + 1 ) / float ( 10 * n )
  for i in range ( 0, n - 1 ):
    a[i,i+1] = - 1.0

  return a

def biw_condition ( n ):

#*****************************************************************************80
#
## biw_condition() computes the L1 condition of the BIW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  if ( n == 1 ):
    a_norm = 0.6
  else:
    a_norm = 1.6

  b_norm = 0.0
  j = n
  for i in range ( n, 0, -1 ):
    aii = 0.5 + float ( i ) / float ( 10 * n )
    if ( i == j ):
      bij = 1.0 / aii
    elif ( i < j ):
      bij = bij / aii
    b_norm = b_norm + abs ( bij )

  value = a_norm * b_norm

  return value

def biw_determinant ( n ):

#*****************************************************************************80
#
## biw_determinant() returns the determinant of the BIW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0
  for i in range ( 0, n ):
    value = value * ( 0.5 + float ( i + 1 ) / float ( 10 * n ) )

  return value

def biw_inverse ( n ):

#*****************************************************************************80
#
## biw_inverse() returns the inverse of the BIW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )
  
  for j in range ( n - 1, -1, -1 ):
    for i in range ( n - 1, -1, -1 ):

      aii = 0.5 + float ( i + 1 ) / float ( 10 * n )
      aiip1 = - 1.0

      if ( i == j ):
        b[i,j] = 1.0 / aii
      elif ( i < j ):
        t = aiip1 * b[i+1,j]
        b[i,j] = - t / aii

  return b

def biw_test ( ):

#*****************************************************************************80
#
## biw_test() tests biw_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'biw_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  biw_matrix() computes the BIW matrix.' )

  m = 5
  n = 5
  a = biw_matrix ( n )
  r8mat_print ( m, n, a, '  BIW matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'biw_test' )
  print ( '  Normal end of execution.' )
  return

def bodewig_matrix ( ):

#*****************************************************************************80
#
## bodewig_matrix() returns the BODEWIG matrix.
#
#  Example:
#
#    2   1   3   4
#    1  -3   1   5
#    3   1   6  -2
#    4   5  -2  -1
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    Test Matrix A27,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 2.0,  1.0,  3.0,  4.0 ], \
    [ 1.0, -3.0,  1.0,  5.0 ], \
    [ 3.0,  1.0,  6.0, -2.0 ], \
    [ 4.0,  5.0, -2.0, -1.0 ] ] )
 
  return a

def bodewig_condition ( ):

#*****************************************************************************80
#
## bodewig_condition() returns the L1 condition of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the L1 condition number.
#
  value = 10.436619718309862

  return value

def bodewig_determinant ( ):

#*****************************************************************************80
#
## bodewig_determinant() returns the determinant of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 568.0

  return determ

def bodewig_eigen_right ( ):

#*****************************************************************************80
#
## bodewig_eigen_right() returns the right eigenvectors of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
  [  0.263462395147524,   0.560144509774526,   \
     0.378702689441644,  -0.688047939843040 ], \
  [  0.659040718046439,   0.211632763260098,   \
     0.362419048574935,   0.624122855455373 ], \
  [ -0.199633529128396,   0.776708263894565,   \
    -0.537935161097828,   0.259800864702728 ], \
  [ -0.675573350827063,   0.195381612446620,   \
     0.660198809976478,   0.263750269148100 ] ] )

  return a

def bodewig_eigenvalues ( ):

#*****************************************************************************80
#
## bodewig_eigenvalues() returns the eigenvalues of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real LAMBDA(4,1), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
    [ -8.028578352396531 ], \
    [  7.932904717870018 ], \
    [  5.668864372830019 ], \
    [ -1.573190738303506 ] ] )

  return lam

def bodewig_inverse ( ):

#*****************************************************************************80
#
## bodewig_inverse() returns the inverse of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a  = np.array ( [ \
    [ -139.0,  165.0,  79.0,  111.0 ], \
    [  165.0, -155.0, -57.0,   -1.0 ], \
    [   79.0,  -57.0,  45.0,  -59.0 ], \
    [  111.0,   -1.0, -59.0,  -11.0 ] ] )

  for j in range ( 0, 4 ):
    for i in range ( 0, 4 ):
      a[i,j] = a[i,j] / 568.0

  return a

def bodewig_plu ( ):

#*****************************************************************************80
#
## bodewig_plu() returns the PLU factors of the BODEWIG matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real P(4,4), L(4,4), U(4,4), the factors.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  p = np.array ( [ \
    [ 0.0, 0.0, 0.0, 1.0 ], \
    [ 0.0, 1.0, 0.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 0.0 ], \
    [ 1.0, 0.0, 0.0, 0.0 ] ] )

  l = np.array ( [ \
    [ 1.00, 0.00,              0.00,              0.00 ], \
    [ 0.25, 1.00,              0.00,              0.00 ], \
    [ 0.75, 0.647058823529412, 1.00,              0.00 ], \
    [ 0.50, 0.352941176470588, 0.531531531531532, 1.00 ] ] )

  u = np.array ( [ \
    [ 4.00,  5.00, -2.00,              -1.00 ], \
    [ 0.00, -4.25,  1.50,               5.25 ], \
    [ 0.00,  0.00,  6.529411764705882, -4.647058823529412 ], \
    [ 0.00,  0.00,  0.00,               5.117117117117118 ] ] )

  return p, l, u

def bodewig_rhs ( ):

#*****************************************************************************80
#
## bodewig_rhs() returns the BODEWIG right hand side.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real B(4,1), the right hand side vector.
#
  import numpy as np

  b = np.array ( [ [ 29.0 ], [ 18.0 ], [ 15.0 ], [ 4.0 ] ] )

  return b

def bodewig_solution ( ):

#*****************************************************************************80
#
## bodewig_solution() returns the bodewig_solution
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(4,1), the solution.
#
  import numpy as np

  x = np.array ( [ [ 1.0 ], [ 2.0 ], [ 3.0 ], [ 4.0 ] ] )

  return x

def bodewig_test ( ):

#*****************************************************************************80
#
## bodewig_test() tests bodewig_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bodewig_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bodewig_matrix() computes the BODEWIG matrix.' )

  n = 4
  a = bodewig_matrix ( )
  r8mat_print ( n, n, a, '  BODEWIG matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'bodewig_test' )
  print ( '  Normal end of execution.' )
  return

def boothroyd_matrix ( n ):

#*****************************************************************************80
#
## boothroyd_matrix() returns the BOOTHROYD matrix.
#
#  Formula:
#
#    A(I,J) = C(N+I-1,I-1) * C(N-1,N-J) * N / ( I + J - 1 )
#
#  Example:
#
#    N = 5
#
#     5    10    10     5     1
#    15    40    45    24     5
#    35   105   126    70    15
#    70   224   280   160    35
#   126   420   540   315    70
#
#  Properties:
#
#    A is not symmetric.
#
#    A is positive definite.
#
#    det ( A ) = 1.
#
#    The inverse matrix has the same entries, but with alternating sign.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from scipy.special import comb
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):

      a[i,j] = comb ( n + i, i ) * comb ( n - 1, n - j - 1 ) * float ( n ) \
        / float ( i + j + 1 )

  return a

def boothroyd_condition ( n ):

#*****************************************************************************80
#
## boothroyd_condition() computes the L1 condition of the BOOTHROYD matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  from scipy.special import comb

  a_norm = 0.0

  for j in range ( 0, n ):
    s = 0.0
    for i in range ( 0, n ):
      s = s + comb ( n + i, i ) * comb ( n - 1, n - j - 1 ) * float ( n ) \
        / float ( i + j + 1 )
    a_norm = max ( a_norm, s )

  b_norm = a_norm

  value = a_norm * b_norm
 
  return value

def boothroyd_determinant ( n ):

#*****************************************************************************80
#
## boothroyd_determinant() returns the determinant of the BOOTHROYD matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0
 
  return value

def boothroyd_inverse ( n ):

#*****************************************************************************80
#
## boothroyd_inverse() returns the inverse of the BOOTHROYD matrix.
#
#  Example:
#
#    N = 5
#
#      5   -10    10    -5     1
#    -15    40   -45    24    -5
#     35  -105   126   -70    15
#    -70   224  -280   160   -35
#    126  -420   540  -315    70
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from scipy.special import comb
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      a[i,j] = r8_mop ( i + j ) * comb ( n + i, i ) \
        * comb ( n-1, n-j-1 ) * float ( n  ) / float ( i + j + 1 )

  return a

def boothroyd_test ( ):

#*****************************************************************************80
#
## boothroyd_test() tests boothroyd_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'boothroyd_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  boothroyd_matrix() computes the BOOTHROYD matrix.' )

  m = 5
  n = m
  a = boothroyd_matrix ( n )
  r8mat_print ( m, n, a, '  BOOTHROYD matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'boothroyd_test' )
  print ( '  Normal end of execution.' )
  return

def borderband_matrix ( n ):

#*****************************************************************************80
#
## borderband_matrix() returns the BORDERBAND matrix.
#
#  Formula:
#
#    If ( I = J )
#      A(I,I) = 1
#    else if ( I = N )
#      A(N,J) = 2^(1-J)
#    else if ( J = N )
#      A(I,N) = 2^(1-I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#     1  0   0   0   1
#     0  1   0   0  1/2
#     0  0   1   0  1/4
#     0  0   0   1  1/8
#     1 1/2 1/4 1/8  1
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is border-banded.
#
#    A has N-2 eigenvalues of 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = 1.0
      elif ( j == n - 1 ):
        a[i,j] = 1.0 / ( 2 ** i )
      elif ( i == n - 1 ):
        a[i,j] = 1.0 / ( 2 ** j )
      else:
        a[i,j] = 0.0

  return a

def borderband_determinant ( n ):

#*****************************************************************************80
#
## borderband_determinant() returns the determinant of the BORDERBAND matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 0.0
  for i in range ( 1, n ):
    determ = determ - 2.0 ** ( 2 - 2 * i )
  determ = determ + 1.0

  return determ

def borderband_inverse ( n ):

#*****************************************************************************80
#
## borderband_inverse() returns the inverse of the BORDERBAND matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the inverse matrix.
#
  import numpy as np

  p, l, u = borderband_plu ( n )

  p_inverse = np.transpose ( p )

  l_inverse = tri_l1_inverse ( n, l )

  u_inverse = tri_u_inverse ( n, u )

  lipi = r8mat_mm ( n, n, n, l_inverse, p_inverse )
  
  a = r8mat_mm ( n, n, n, u_inverse, lipi )

  return a

def borderband_lu ( n ):

#*****************************************************************************80
#
## borderband_lu() returns the LU factors of the BORDERBAND matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real L(N,N), U(N,N), the factors.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == j ):
        l[i,j] = 1.0
      elif ( i == n - 1 ):
        l[i,j] = 1.0 / 2.0 ** j

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == n - 1 and j == n - 1 ):
        u[i,j] = 0.0
        for k in range ( 2, n ):
          u[i,j] = u[i,j] - 2.0 ** ( 2 - 2 * k )
      elif ( i == j ):
        u[i,j] = 1.0
      elif ( j == n - 1 ):
        u[i,j] = 1.0 / 2.0 ** i

  return l, u

def borderband_plu ( n ):

#*****************************************************************************80
#
## borderband_plu() returns the PLU factors of the BORDERBAND matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 June 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    p[i,i] = 1.0

  l = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == j ):
        l[i,j] = 1.0
      elif ( i == n - 1 ):
        l[i,j] = 1.0 / 2.0 ** j

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == n - 1 and j == n - 1 ):
        u[i,j] = 0.0
        for k in range ( 2, n ):
          u[i,j] = u[i,j] - 2.0 ** ( 2 - 2 * k )
      elif ( i == j ):
        u[i,j] = 1.0
      elif ( j == n - 1 ):
        u[i,j] = 1.0 / 2.0 ** i

  return p, l, u

def borderband_test ( ):

#*****************************************************************************80
#
## borderband_test() tests borderband_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'borderband_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  borderband_matrix() computes the BORDERBAND matrix.' )

  m = 5
  n = m
  a = borderband_matrix ( n )
  r8mat_print ( m, n, a, '  BORDERBAND matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'borderband_test' )
  print ( '  Normal end of execution.' )
  return

def bvec_next_grlex ( n, bvec ):

#*****************************************************************************80
#
## bvec_next() generates the next binary vector in GRLEX order.
#
#  Discussion:
#
#    N = 3
#
#    Input      Output
#    -----      ------
#    0 0 0  =>  0 0 1
#    0 0 1  =>  0 1 0
#    0 1 0  =>  1 0 0
#    1 0 0  =>  0 1 1
#    0 1 1  =>  1 0 1
#    1 0 1  =>  1 1 0
#    1 1 0  =>  1 1 1
#    1 1 1  =>  0 0 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    integer BVEC[N], a vector.  
#
#  Output:
#
#    integer BVEC[N], the successor vector.  
#

#
#  Initialize locations of 0 and 1.
#
  if ( bvec[0] == 0 ):
    z = 0
    o = -1
  else:
    z = -1
    o = 0
#
#  Moving from right to left, search for a "1", preceded by a "0".
#
  for i in range ( n - 1, 0, -1 ):
    if ( bvec[i] == 1 ):
      o = i
      if ( bvec[i-1] == 0 ):
        z = i - 1
        break
#
#  BVEC = 0
#
  if ( o == -1 ):
    bvec[n-1] = 1
#
#  01 never occurs.  So for sure, B(1) = 1.
#
  elif ( z == -1 ):

    s = 0
    for i in range ( 0, n ):
      s = s + bvec[i]

    if ( s == n ):

      for i in range ( 0, n ):
        bvec[i] = 0

    else:

      for i in range ( 0, n - s - 1 ):
        bvec[i] = 0

      for i in range ( n - s - 1, n ):
        bvec[i] = 1
      type ( n - s - 1 )
#
#  Found the rightmost "01" string.
#  Replace it by "10".
#  Shift following 1's to the right.
#
  else:

    bvec[z] = 1
    bvec[o] = 0

    s = 0
    for i in range ( o + 1, n ):
      s = s + bvec[i]

    for i in range ( o + 1, n - s ):
      bvec[i] = 0
    
    for i in range ( n - s, n ):
      bvec[i] = 1

  return bvec

def bvec_next_grlex_test ( ):

#*****************************************************************************80
#
## bvec_next_grlex_test() tests bvec_next_grlex().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'bvec_next_grlex_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bvec_next_grlex() computes binary vectors in GRLEX order.' )
  print ( '' )

  b = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, 17 ):
    print ( '  %2d:  ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( '%1d' % ( b[j] ), end = '' )
    print ( '' )
    b = bvec_next_grlex ( n, b )
#
#  Terminate.
#
  print ( '' )
  print ( 'bvec_next_grlex_test():' )
  print ( '  Normal end of execution.' )
  return

def c8_i ( ):

#*****************************************************************************80
#
## c8_i() returns the value of the imaginary unit as a C8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the value of the imaginary unit.
#
  value = 1j

  return value

def c8_i_test ( ):

#*****************************************************************************80
#
## c8_i_test() tests c8_i().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'c8_i_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8_i returns the value of the imaginary unit.' )

  c1 = c8_i ( )
  print ( '' )
  print ( '  C1=c8_i ( ) = (%g,%g)' % ( c1.real, c1.imag ) )
  c2 = c1 * c1
  print ( '' )
  print ( '  C2= C1 * C1 = (%g,%g)' % ( c2.real, c2.imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8_i_test:' )
  print ( '  Normal end of execution.' )
  return

def c8mat_identity ( n ):

#*****************************************************************************80
#
## c8mat_identity returns the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    complex C(N,N), the identity matrix.
#
  import numpy as np

  c = np.zeros ( ( n, n ), 'complex' )

  for i in range ( 0, n ): 
    c[i][i] = complex ( 1.0, 0.0 )

  return c

def c8mat_is_eigen_right ( n, k, a, x, lam ):

#*****************************************************************************80
#
## c8mat_is_eigen_right() determines the error in a right eigensystem.
#
#  Discussion:
#
#    A C8MAT is a matrix of complex values.
#
#    This routine computes the Frobenius norm of
#
#      A * X - X * LAMBDA
#
#    where
#
#      A is an N by N matrix,
#      X is an N by K matrix (each of K columns is an eigenvector)
#      LAMBDA is a K by K diagonal matrix of eigenvalues.
#
#    This routine assumes that A, X and LAMBDA are all real.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer K, the number of eigenvectors.
#    K is usually 1 or N.
#
#    complex A(N,N), the matrix.
#
#    complex X(N,K), the K eigenvectors.
#
#    complex LAM(K), the K eigenvalues.
#
#  Output:
#
#    complex VALUE, the Frobenius norm
#    of the difference matrix A * X - X * LAM, which would be exactly zero
#    if X and LAM were exact eigenvectors and eigenvalues of A.
#
  c = c8mat_mm ( n, n, k, a, x )

  for j in range ( 0, k ):
    for i in range ( 0, n ):
      c[i,j] = c[i,j] - lam[j] * x[i,j]

  value = c8mat_norm_fro ( n, k, c )

  return value

def c8mat_identity_test ( ):

#*****************************************************************************80
#
## c8mat_identity_test() tests c8mat_identity().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 4
  n = 4

  print ( '' )
  print ( 'c8mat_identity_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8mat_identity returns the complex identity matrix.' )

  c = c8mat_identity ( n )

  c8mat_print ( m, n, c, '  Identity matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8mat_identity_test:' )
  print ( '  Normal end of execution.' )
  return

def c8mat_indicator ( m, n ):

#*****************************************************************************80
#
## c8mat_indicator returns the indicator matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    complex C(M,N), the indicator matrix.
#
  import numpy

  c = numpy.zeros ( ( m, n ), 'complex' )

  for j in range ( 0, n ): 
    for i in range ( 0, m ):
      c[i][j] = complex ( i + 1, - j - 1 )

  return c

def c8mat_indicator_test ( ):

#*****************************************************************************80
#
## c8mat_indicator_test() tests c8mat_indicator().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 3

  print ( '' )
  print ( 'c8mat_indicator_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8mat_indicator returns the complex indicator matrix.' )

  c = c8mat_indicator ( m, n )

  c8mat_print ( m, n, c, '  Indicator matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8mat_indicator_test:' )
  print ( '  Normal end of execution.' )
  return

def c8mat_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## c8mat_mm() multiplies two C8MAT's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    complex A(N1,N2), B(N2,N3), the matrices to multiply.
#
#  Output:
#
#    complex C(N1,N3), the product matrix C = A * B.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ), dtype = np.complex64 )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def c8mat_norm_fro ( m, n, a ):

#*****************************************************************************80
#
## c8mat_norm_fro() returns the Frobenius norm of a C8MAT.
#
#  Discussion:
#
#    The Frobenius norm is defined as
#
#      c8mat_norm_fro = sqrt (
#        sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J) * A(I,J) )
#
#    The matrix Frobenius norm is not derived from a vector norm, but
#    is compatible with the vector L2 norm, so that:
#
#      c8vec_norm_l2 ( A * x ) <= c8mat_norm_fro ( A ) * c8vec_norm_l2 ( x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
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
#    complex A(M,N), the matrix whose norm is desired.
#
#  Output:
#
#    real VALUE, the norm of A.
#
  import numpy as np

  value = \
    np.sqrt \
    ( \
      np.sum \
      ( \
        np.sum \
        ( \
          ( \
            np.abs \
            ( \
              a \
            ) \
          ) ** 2 \
        ) \
      ) \
   )

  return value

def c8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## c8mat_print prints a C8MAT.
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
#    complex A(M,N), the matrix.
#
#    string TITLE, a title.
#
  c8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def c8mat_print_test ( ):

#*****************************************************************************80
#
## c8mat_print_test() tests c8mat_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'c8mat_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8mat_print prints an C8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ complex(10.0, 1.0), complex(10.0, 2.0), complex(10.0, 3.0) ], \
    [ complex(20.0, 1.0), complex(20.0, 2.0), complex(20.0, 3.0) ], \
    [ complex(30.0, 1.0), complex(30.0, 2.0), complex(30.0, 3.0) ], \
    [ complex(40.0, 1.0), complex(40.0, 2.0), complex(40.0, 3.0) ] ], \
    dtype = np.complex128 )

  c8mat_print ( m, n, v, '  Here is a C8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8mat_print_test:' )
  print ( '  Normal end of execution.' )
  return

def c8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## c8mat_print_some prints out a portion of an C8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    complex A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 4

  print ( '' )
  print  ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '       %7d              ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  %12gi ' % ( a.real[i,j], a.imag[i,j] ) ),

      print ( '' )

  return

def c8mat_print_some_test ( ):

#*****************************************************************************80
#
## c8mat_print_some_test() tests c8mat_print_some().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'c8mat_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8mat_print_some prints some of an C8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ complex(10.0, 1.0), complex(10.0, 2.0), complex(10.0, 3.0), \
      complex(10.0, 4.0), complex(10.0, 5.0), complex(10.0, 6.0) ], \
    [ complex(20.0, 1.0), complex(20.0, 2.0), complex(20.0, 3.0), \
      complex(20.0, 4.0), complex(20.0, 5.0), complex(20.0, 6.0) ], \
    [ complex(30.0, 1.0), complex(30.0, 2.0), complex(30.0, 3.0), \
      complex(30.0, 4.0), complex(30.0, 5.0), complex(30.0, 6.0) ], \
    [ complex(40.0, 1.0), complex(40.0, 2.0), complex(40.0, 3.0), \
      complex(40.0, 4.0), complex(40.0, 5.0), complex(40.0, 6.0) ] ], \
    dtype = np.complex128 )

  c8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is a C8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8mat_print_some_test:' )
  print ( '  Normal end of execution. ')
  return

def c8mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## c8mat_uniform_01 returns a unit pseudorandom C8MAT.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
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
#    integer M, N, the number of rows and columns in the matrix.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    complex C(M,N), the pseudorandom complex matrix.
#
#    integer SEED, a seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'c8mat_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'c8mat_uniform_01 - Fatal error!' )

  c = np.zeros ( ( m, n ), 'complex' )

  for i2 in range ( 0, n ): 
    for i1 in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      if ( seed < 0 ):
        seed = seed + i4_huge

      r = np.sqrt ( seed * 4.656612875E-10 )

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      if ( seed < 0 ):
        seed = seed + i4_huge

      theta = 2.0 * np.pi * seed * 4.656612875E-10

      c[i1][i2] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c, seed

def c8mat_uniform_01_test ( ):

#*****************************************************************************80
#
## c8mat_uniform_01_test() tests c8mat_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 3
  seed = 123456789

  print ( '' )
  print ( 'c8mat_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8mat_uniform_01 computes a random C8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = c8mat_uniform_01 ( m, n, seed )

  c8mat_print ( m, n, v, '  Random C8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8mat_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def c8_uniform_01 ( seed ):

#*****************************************************************************80
#
## c8_uniform_01 returns a unit pseudorandom C8.
#
#  Discussion:
#
#    The angle should be uniformly distributed between 0 and 2 * PI,
#    the square root of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
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
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    complex C, the pseudorandom complex value.
#
#    integer SEED, a seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647

  seed = np.floor ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'c8_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'c8_uniform_01 - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = np.sqrt ( seed * 4.656612875E-10 )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  theta = 2.0 * np.pi * seed * 4.656612875E-10

  c = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c, seed

def c8_uniform_01_test ( ):

#*****************************************************************************80
#
## c8_uniform_01_test() tests c8_uniform_01().
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
  import platform

  seed = 123456789

  print ( '' )
  print ( 'c8_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8_uniform_01 computes pseudorandom complex values' )
  print ( '  in the unit circle.' )

  print ( '' )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 0, 10 ):
    x, seed = c8_uniform_01 ( seed )
    print ( '  %6d  ( %g, %g )' % ( i, x.real, x.imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def c8vec_print ( n, a, title ):

#*****************************************************************************80
#
## c8vec_print prints a C8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    complex A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %12g  %12g' % ( i, a.real[i], a.imag[i] ) )

def c8vec_print_test ( ):

#*****************************************************************************80
#
## c8vec_print_test() tests c8vec_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'c8vec_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8vec_print prints an C8VEC.' )

  n = 4
  v = np.array ( [ complex ( 1.0, 2.0 ), \
                   complex ( 3.0, 4.0 ), \
                   complex ( 5.0, 6.0 ), \
                   complex ( 7.0, 8.0 ) ], dtype = np.complex128 )
  c8vec_print ( n, v, '  Here is a C8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8vec_print_test:' )
  print ( '  Normal end of execution.' )
  return

def c8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## c8vec_uniform_01 returns a unit pseudorandom C8VEC.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
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
#    integer N, the number of values to compute.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    complex C(N), the pseudorandom complex vector.
#
#    integer SEED, a seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'c8vec_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'c8vec_uniform_01 - Fatal error!' )

  c = np.zeros ( n, 'complex' )

  for j in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    r = np.sqrt ( seed * 4.656612875E-10 )

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    theta = 2.0 * np.pi * seed * 4.656612875E-10

    c[j] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c, seed

def c8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## c8vec_uniform_01_test() tests c8vec_uniform_01().
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
  import platform

  seed = 123456789

  print ( '' )
  print ( 'c8vec_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8vec_uniform_01 computes pseudorandom complex values' )
  print ( '  in the unit circle.' )

  print ( '' )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  n = 10

  [ x, seed ] = c8vec_uniform_01 ( n, seed )

  for i in range ( 0, n ):
    print ( '  %6d  ( %f, %f )' % ( i, x[i].real, x[i].imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8vec_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def c8vec_unity ( n ):

#*****************************************************************************80
#
## c8vec_unity returns the N roots of unity.
#
#  Discussion:
#
#    X(1:N) = exp ( 2 * PI * (0:N-1) / N )
#
#    X(1:N)^N = ( (1,0), (1,0), ..., (1,0) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#  Output:
#
#    complex A(N), the array.
#
  import numpy as np

  a = np.zeros ( n, 'complex' )

  for i in range ( 0, n ):
    t = 2.0 * np.pi * float ( i ) / float ( n )
    a[i] = np.cos ( t ) + 1j * np.sin ( t )

  return a

def c8vec_unity_test ( ):

#*****************************************************************************80
#
## c8vec_unity_test() tests c8vec_unity().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'c8vec_unity_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8vec_unity returns the N roots of unity.' )

  n = 12

  x = c8vec_unity ( n )

  c8vec_print ( n, x, '  The N roots of unity:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'c8vec_unity_test:' )
  print ( '  Normal end of execution.' )
  return

def carry_matrix ( n, alpha ):

#*****************************************************************************80
#
## carry_matrix() returns the CARRY matrix.
#
#  Discussion:
#
#    We assume that arithmetic is being done in base ALPHA.  We are adding
#    a column of N digits base ALPHA, as part of adding N random numbers.
#    We know the carry digit, between 0 and N-1, that is being carried into the
#    column sum (the incarry digit), and we want to know the probability of
#    the various carry digits 0 through N-1 (the outcarry digit) that could
#    be carried out of the column sum.
#
#    The carry matrix summarizes this data.  The entry A(I,J) represents
#    the probability that, given that the incarry digit is I-1, the
#    outcarry digit will be J-1.
#
#  Formula:
#
#    A(I,J) = ( 1 / ALPHA )^N * sum ( 0 <= K <= J-1 - floor ( I-1 / ALPHA ) )
#      (-1)^K * C(N+1,K) * C(N-I+(J-K)*ALPHA, N )
#
#  Example:
#
#    ALPHA = 10, N = 4
#
#    0.0715 0.5280 0.3795 0.0210
#    0.0495 0.4840 0.4335 0.0330
#    0.0330 0.4335 0.4840 0.0495
#    0.0210 0.3795 0.5280 0.0715
#
#  Square Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is a Markov matrix.
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    LAMBDA(I) = 1 / ALPHA^(I-1)
#
#    det ( A ) = 1 / ALPHA^((N*(N-1))/2)
#
#    The eigenvectors do not depend on ALPHA.
#
#    A is generally not normal: A' * A /= A * A'.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Holte,
#    Carries, Combinatorics, and an Amazing Matrix,
#    The American Mathematical Monthly,
#    February 1997, pages 138-149.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ALPHA, the numeric base used in the addition.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from scipy.special import comb
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):

      temp = 0.0
      s = -1.0

      for k in range ( 0, j - ( i // alpha ) + 1 ):
        s = - s
        c1 = comb ( n + 1, k )
        c2 = comb ( n - i - 1 + ( j + 1 - k ) * alpha, n )
        temp = temp + s * c1 * c2

      a[i,j] = temp / alpha ** n

  return a

def carry_determinant ( n, alpha ):

#*****************************************************************************80
#
## carry_determinant() returns the determinant of the CARRY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ALPHA, the numeric base used in the addition.
#
#  Output:
#
#    real DETERM, the determinant.
#
  power = ( n * ( n - 1 ) ) // 2
  determ = 1.0 / alpha ** power
 
  return determ

def carry_eigen_left ( n, alpha  ):

#*****************************************************************************80
#
## carry_eigen_left() returns the left eigenvectors for the CARRY matrix.
#
#  Formula:
#
#    A(I,J) = sum ( 0 <= K <= J-1 )
#      (-1)^K * C(N+1,K) * ( J - K )^(N+1-I)
#
#  Example:
#
#    N = 4
#
#    1  11  11   1
#    1   3  -3  -1
#    1  -1  -1   1
#    1  -3   3  -1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    Column 1 is all 1's, and column N is (-1)^(I+1).
#
#    The top row is proportional to a row of Eulerian numbers, and
#    can be normalized to represent the stationary probablities
#    for the carrying process when adding N random numbers.
#
#    The bottom row is proportional to a row of Pascal's triangle,
#    with alternating signs.
#
#    The product of the left and right eigenvector matrices of
#    order N is N! times the identity.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Holte,
#    Carries, Combinatorics, and an Amazing Matrix,
#    The American Mathematical Monthly,
#    February 1997, pages 138-149.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ALPHA, the numeric base used in the addition.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from scipy.special import comb
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      s = -1.0
      for k in range ( 0, j + 1 ):
        s = - s
        a[i,j] = a[i,j] + s * comb ( n + 1, k ) * ( j + 1 - k ) ** ( n - i )

  return a

def carry_eigen_right ( n, alpha ):

#*****************************************************************************80
#
## carry_eigen_right() returns the right eigenvectors of the CARRY matrix.
#
#  Formula:
#
#    A(I,J) = sum ( N+1-J) <= K <= N )
#      S1(N,K) * C(K,N+1-J) ( N - I )^(K-N+J-1)
#
#    where S1(N,K) is a signed Sterling number of the first kind.
#
#  Example:
#
#    N = 4
#
#    1   6  11   6
#    1   2  -1  -2
#    1  -2  -1   2
#    1  -6  11  -6
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    The first column is all 1's.
#
#    The last column is reciprocals of binomial coefficients with
#    alternating sign multiplied by (N-1).
#
#    The top and bottom rows are the unsigned and signed Stirling numbers
#    of the first kind.
#
#    The entries in the J-th column are a degree (J-1) polynomial
#    in the row index I.  (Column 1 is constant, the first difference
#    in column 2 is constant, the second difference in column 3 is
#    constant, and so on.)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Holte,
#    Carries, Combinatorics, and an Amazing Matrix,
#    The American Mathematical Monthly,
#    February 1997, pages 138-149.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ALPHA, the numeric base used in the addition.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from scipy.special import comb
  import numpy as np

  s1 = stirling_matrix ( n, n )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( n - j, n + 1 ):
        if ( n - 1 - i == 0 and k - n + j == 0 ):
          a[i,j] = a[i,j] + s1[n-1,k-1] * comb ( k, n - j )
        else:
          a[i,j] = a[i,j] + s1[n-1,k-1] * comb ( k, n - j ) \
            * ( n - i - 1 ) ** ( k - n + j )

  return a

def carry_eigenvalues ( n, alpha ):

#*****************************************************************************80
#
## carry_eigenvalues() returns the eigenvalues of the CARRY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ALPHA, the numeric base used in the addition.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    lam[i] = 1.0 / alpha ** i

  return lam

def carry_inverse ( n, alpha ):

#*****************************************************************************80
#
## carry_inverse() returns the inverse of the CARRY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ALPHA, the numeric base used in the addition.
#
#    integer ALPHA, the numeric base used in the addition.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from scipy.special import factorial

  v = carry_eigen_left ( n, alpha )

  d = carry_eigenvalues ( n, alpha )
  d[0:n] = 1.0 / d[0:n]
  d_inv = diagonal_matrix ( n, n, d )

  u = carry_eigen_right ( n, alpha )

  dv = r8mat_mm ( n, n, n, d_inv, v )

  a = r8mat_mm ( n, n, n, u, dv )

  t = factorial ( n )
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a[i,j] = a[i,j] / t

  return a

def carry_test ( ):

#*****************************************************************************80
#
## carry_test() tests carry_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'carry_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  carry_matrix() computes the CARRY matrix.' )

  m = 4
  n = m
  alpha = 10
  a = carry_matrix ( alpha, n )
  r8mat_print ( m, n, a, '  CARRY matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'carry_test' )
  print ( '  Normal end of execution.' )
  return

def cauchy_matrix ( n, x, y ):

#*****************************************************************************80
#
## cauchy_matrix() returns the CAUCHY matrix.
#
#  Formula:
#
#    A(I,J) = 1.0 / ( X(I) + Y(J) )
#
#  Example:
#
#    N = 5, X = ( 1, 3, 5, 8, 7 ), Y = ( 2, 4, 6, 10, 9 )
#
#    1/3  1/5  1/7  1/11 1/10
#    1/5  1/7  1/9  1/13 1/12
#    1/7  1/9  1/11 1/15 1/14
#    1/10 1/12 1/14 1/18 1/17
#    1/9  1/11 1/13 1/17 1/16
#
#    or, in decimal form,
#
#    0.333333      0.200000      0.142857      0.0909091     0.100000
#    0.200000      0.142857      0.111111      0.0769231     0.0833333
#    0.142857      0.111111      0.0909091     0.0666667     0.0714286
#    0.100000      0.0833333     0.0714286     0.0555556     0.0588235
#    0.111111      0.0909091     0.0769231     0.0588235     0.0625000
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is totally positive if 0 < X(1) < ... < X(N) and 0 < Y1 < ... < Y(N).
#
#    A will be singular if any X(I) equals X(J), or
#    any Y(I) equals Y(J), or if any X(I)+Y(J) equals zero.
#
#    A is generally not normal: A' * A /= A * A'.
#
#    The Hilbert matrix is a special case of the Cauchy matrix.
#
#    The Parter matrix is a special case of the Cauchy matrix.
#
#    The Ris or "ding-dong" matrix is a special case of the Cauchy matrix.
#
#    det ( A ) = product ( 1 <= I < J <= N ) ( X(J) - X(I) )* ( Y(J) - Y(I) )
#           / product ( 1 <= I <= N, 1 <= J <= N ) ( X(I) + Y(J) )
#
#    The inverse of A is
#
#      INVERSE(A)(I,J) = product ( 1 <= K <= N ) [ (X(J)+Y(K)) * (X(K)+Y(I)) ] /
#            [ (X(J)+Y(I)) * product ( 1 <= K <= N, K /= J ) (X(J)-X(K))
#                          * product ( 1 <= K <= N, K /= I ) (Y(I)-Y(K)) ]
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.26,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 54, 
#    LC: QA263.G68.
#
#    Nicholas Higham,
#    Accuracy and Stability of Numerical Algorithms,
#    SIAM, 1996.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition
#    Addison-Wesley, Reading, Massachusetts, 1973, page 36.
#
#    Olga Taussky, Marvin Marcus,
#    Eigenvalues of finite matrices,
#    in Survey of Numerical Analysis, 
#    Edited by John Todd,
#    McGraw-Hill, New York, pages 279-313, 1962.
#
#    Evgeny Tyrtyshnikov,
#    Cauchy-Toeplitz matrices and some applications,
#    Linear Algebra and Applications,
#    Volume 149, 1991, pages 1-18.
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N), Y(N), vectors that determine A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ): 

      if ( x[i] + y[j] == 0.0 ):
        print ( '' )
        print ( 'CAUCHY - Fatal error!' )
        print ( '  The denominator X(I)+Y(J) was zero' )
        print ( '  for I = %d' % ( i ) )
        print ( '  X(I)  = %g' % ( x[i] ) )
        print ( '  and J = %d' % ( j ) )
        print ( '  Y(J)  = %g' % ( y[j] ) )
        raise Exception ( 'CAUCHY - Fatal error!' )

      a[i,j] = 1.0 / ( x[i] + y[j] )

  return a

def cauchy_determinant ( n, x, y ):

#*****************************************************************************80
#
## cauchy_determinant() returns the determinant of the CAUCHY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N), Y(N), vectors that determine A.
#
#  Output:
#
#    real DETERM, the determinant.
#
  top = 1.0
  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      top = top * ( x[j] - x[i] ) * ( y[j] - y[i] )

  bottom = 1.0
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      bottom = bottom * ( x[i] + y[j] )

  determ = top / bottom

  return determ

def cauchy_inverse ( n, x, y ):

#*****************************************************************************80
#
## cauchy_inverse() returns the inverse of the CAUCHY matrix.
#
#  Formula:
#
#    A(I,J) = product ( 1 <= K <= N ) [(X(J)+Y(K))*(X(K)+Y(I))] /
#      [ (X(J)+Y(I)) * product ( 1 <= K <= N, K /= J ) (X(J)-X(K))
#                    * product ( 1 <= K <= N, K /= I ) (Y(I)-Y(K)) ]
#
#  Example:
#
#    N = 5, X = ( 1, 3, 5, 8, 7 ), Y = ( 2, 4, 6, 10, 9 )
#
#       241.70      -2591.37       9136.23      10327.50     -17092.97
#     -2382.19      30405.38    -116727.19    -141372.00     229729.52
#      6451.76     -89667.70     362119.56     459459.00    -737048.81
#     10683.11    -161528.55     690983.38     929857.44   -1466576.75
#    -14960.00     222767.98    -942480.06   -1253376.00    1983696.00
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    The sum of the entries of A equals the sum of the entries of X and Y.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition,
#    Addison-Wesley, Reading, Massachusetts, 1973, page 36.
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N), Y(N), vectors that determine A.
#    The following conditions on X and Y must hold:
#      X(I)+Y(J) must not be zero for any I and J;
#      X(I) must never equal X(J);
#      Y(I) must never equal Y(J).
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
#
#  Check the data.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( x[i] + y[j] == 0.0 ):
        print ( '' )
        print ( 'cauchy_inverse - Fatal error!' )
        print ( '  The denominator X(I)+Y(J) was zero' )
        print ( '  for I = %d' % ( i ) )
        print ( '  and J = %d' % ( j ) )
        raise Exception ( 'cauchy_inverse - Fatal error!' )

      if ( i != j and x[i] == x[j] ):
        print ( '' )
        print ( 'cauchy_inverse - Fatal error!' )
        print ( '  X(I) equals X(J)' )
        print ( '  for I = %d' % ( i ) )
        print ( '  and J = %d' % ( j ) )
        raise Exception ( 'cauchy_inverse - Fatal error!' )

      if ( i != j and y[i] == y[j] ):
        print ( '' )
        print ( 'cauchy_inverse - Fatal error!' )
        print ( '  Y(I) equals Y(J)' )
        print ( '  for I =%d' % ( i ) )
        print ( '  and J = %d' % ( j ) )
        raise Exception ( 'cauchy_inverse - Fatal error!' )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      top = 1.0
      bot1 = 1.0
      bot2 = 1.0

      for k in range ( 0, n ):

        top = top * ( x[j] + y[k] ) * ( x[k] + y[i] )

        if ( k != j ):
          bot1 = bot1 * ( x[j] - x[k] )

        if ( k != i ):
          bot2 = bot2 * ( y[i] - y[k] )

      a[i,j] = top / ( ( x[j] + y[i] ) * bot1 * bot2 )

  return a

def cauchy_test ( ):

#*****************************************************************************80
#
## cauchy_test() tests cauchy_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cauchy_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cauchy_matrix() computes the CAUCHY matrix.' )

  m = 4
  n = m
  x = np.random.rand ( n )
  y = np.random.rand ( n )
  a = cauchy_matrix ( n, x, y )
  r8mat_print ( n, n, a, '  CAUCHY matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'cauchy_test' )
  print ( '  Normal end of execution.' )
  return

def cheby_diff1_matrix ( n ):

#*****************************************************************************80
#
## cheby_diff1_matrix() returns the cheby_diff1 matrix.
#
#  Discussion:
#
#    cheby_diff1 is the Chebyshev Differentiation matrix.
#
#  Example:
#
#    N = 6
#
#    8.5000 -10.4721   2.8944  -1.5279   1.1056  -0.5000
#    2.6180  -1.1708  -2.0000   0.8944  -0.6810   0.2764
#   -0.7236   2.0000  -0.1708   1.6180   0.8944  -0.3820
#    0.3820  -0.8944   1.6180   0.1708  -2.0000   0.7236
#   -0.2764   0.6180  -0.8944   2.0000   1.1708  -2.6180
#    0.5000  -1.1056   1.5279  -2.8944  10.4721  -8.5000
#
#  Properties:
#
#    A is antisymmetric.
#
#    If 1 < N, then det ( A ) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Lloyd Trefethen,
#    Spectral Methods in MATLAB,
#    SIAM, 2000, page 54.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  if ( n == 1 ):
    a[0,0] = 1.0
    return a

  c = np.zeros ( n )
  c[0] = 2.0
  for i in range ( 1, n - 1 ):
    c[i] = 1.0
  c[n-1] = 2.0
#
#  Get the Chebyshev points.
#
  x = np.zeros ( n + 1 )
  for i in range ( 0, n + 1 ):
    x[i] = np.cos ( np.pi * float ( i ) / float ( n - 1 ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
 
      if ( i != j ):
        a[i,j] = ( -1.0 ) ** ( i + j ) * c[i] / ( c[j] * ( x[i] - x[j] ) )
      elif ( i == 0 ):
        a[i,i] = float ( 2 * ( n - 1 ) ** 2 + 1 ) / 6.0
      elif ( i == n - 1 ):
        a[i,i] = - float ( 2 * ( n - 1 ) ** 2 + 1 ) / 6.0
      else:
        a[i,i] = - 0.5 * x[i] / ( 1.0 - x[i] ** 2 )

  return a

def cheby_diff1_determinant ( n ):

#*****************************************************************************80
#
## cheby_diff1_determinant() returns the determinant of the cheby_diff1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( 1 == n ):
    determ = 1.0
  else:
    determ = 0.0

  return determ

def cheby_diff1_null_left ( m, n ):

#*****************************************************************************80
#
## cheby_diff1_null_left() returns a left null vector for the cheby_diff1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(M), the vector.
#
  import numpy as np

  if ( ( m % 2 ) == 1 ):

    x = np.zeros ( m )
    x[0] = 1.0
    t = -2.0
    for i in range ( 1, m - 1 ):
      x[i] = t
      t = -t
    x[m-1] = 1.0

  else:

    x = np.zeros ( m )

  return x

def cheby_diff1_null_right ( m, n ):

#*****************************************************************************80
#
## cheby_diff1_null_right() returns a right null vector for the cheby_diff1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(N), the vector.
#
  import numpy as np

  if ( n % 2 == 1 ):
    x = np.ones ( n )
  else:
    x = np.zeros ( n )

  return x

def cheby_diff1_test ( ):

#*****************************************************************************80
#
## cheby_diff1_test() tests cheby_diff1().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cheby_diff1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cheby_diff1_matrix() computes the cheby_diff1 matrix.' )

  m = 5
  n = 5
  a = cheby_diff1_matrix ( n )
  r8mat_print ( m, n, a, '  cheby_diff1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'cheby_diff1_test' )
  print ( '  Normal end of execution.' )
  return

def cheby_t_matrix ( n ):

#*****************************************************************************80
#
## cheby_t_matrix() returns the cheby_t matrix.
#
#  Example:
#
#    N = 11
#
#    1  .   .    .    .    .    .    .     .   .   .
#    .  1   .    .    .    .    .    .     .   .   .
#   -1  .   2    .    .    .    .    .     .   .   .
#    . -3   .    4    .    .    .    .     .   .   .
#    1  .  -8    .    8    .    .    .     .   .   .
#    .  5   .  -20    .   16    .    .     .   .   .
#   -1  .  18    .  -48    .   32    .     .   .   .
#    . -7   .   56    . -112    .   64     .   .   .
#    1  . -32    .  160    . -256    .   128   .   .
#    .  9   . -120    .  432    . -576     . 256   .
#   -1  .  50    . -400    . 1120    . -1280   . 512
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is reducible.
#
#    A is lower triangular.
#
#    Each row of A sums to 1.
#
#    det ( A ) = 2^( (N-1) * (N-2) / 2 )
#
#    A is not normal: A' * A /= A * A'.
#
#    For I = 1:
#      LAMBDA(1) = 1
#    For 1 < I
#      LAMBDA(I) = 2^(I-2)
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  a[0,0] = 1.0

  if ( n == 1 ):
    return a

  a[1,1] = 1.0

  if ( n == 2 ):
    return

  for i in range ( 2, n ):
    for j in range ( 0, n ):
      if ( j == 0 ):
        a[i,j] = - a[i-2,j]
      else:
        a[i,j] = 2.0 * a[i-1,j-1] - a[i-2,j]

  return a

def cheby_t_determinant ( n ):

#*****************************************************************************80
#
## cheby_t_determinant() returns the determinant of the cheby_t matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  power = ( ( n - 1 ) * ( n - 2 ) ) // 2
  determ = 2 ** power

  return determ

def cheby_t_inverse ( n ):

#*****************************************************************************80
#
## cheby_t_inverse() returns the inverse of the cheby_t matrix.
#
#  Example:
#
#    N = 11
#
#      1   .   .  .   .  .  .  .  .  .  .
#      .   1   .  .   .  .  .  .  .  .  .
#      1   .   1  .   .  .  .  .  .  .  .  /   2
#      .   3   .  1   .  .  .  .  .  .  .  /   4
#      3   .   4  .   1  .  .  .  .  .  .  /   8
#      .  10   .  5   .  1  .  .  .  .  .  /  16
#     10   .  15  .   6  .  1  .  .  .  .  /  32
#      .  35   . 21   .  7  .  1  .  .  .  /  64
#     35   .  56  .  28  .  8  .  1  .  .  / 128
#      . 126   . 84   . 36  .  9  .  1  .  / 256
#    126   . 210  . 120  . 45  . 10  .  1  / 512
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,1] = 1.0

    if ( 2 < n ):

      for i in range ( 2, n ):
        for j in range ( 0, n ):
          if ( j == 0 ):
            a[i,j] =                      a[i-1,j+1]   / 2.0
          elif ( j == 1 ):
            a[i,j] = ( 2.0 * a[i-1,j-1] + a[i-1,j+1] ) / 2.0
          elif ( j < n - 1 ):
            a[i,j] = (       a[i-1,j-1] + a[i-1,j+1] ) / 2.0
          else:
            a[i,j] =         a[i-1,j-1]                / 2.0

  return a

def cheby_t_test ( ):

#*****************************************************************************80
#
## cheby_t_test() tests cheby_t_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cheby_t_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cheby_t_matrix() computes the cheby_t matrix.' )

  m = 5
  n = m
  a = cheby_t_matrix ( n )
  r8mat_print ( m, n, a, '  cheby_t matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'cheby_t_test' )
  print ( '  Normal end of execution.' )
  return

def cheby_u_polynomial ( n, x ):

#*****************************************************************************80
#
## cheby_u_polynomial evaluates the Chebyshev polynomials of the second kind.
#
#  Differential equation:
#
#    (1-X*X) Y'' - 3 X Y' + N (N+2) Y = 0
#
#  First terms:
#
#    U(0)(X) =   1
#    U(1)(X) =   2 X
#    U(2)(X) =   4 X^2 -   1
#    U(3)(X) =   8 X^3 -   4 X
#    U(4)(X) =  16 X^4 -  12 X^2 +  1
#    U(5)(X) =  32 X^5 -  32 X^3 +  6 X
#    U(6)(X) =  64 X^6 -  80 X^4 + 24 X^2 - 1
#    U(7)(X) = 128 X^7 - 192 X^5 + 80 X^3 - 8X
#
#  Recursion:
#
#    U(0)(X) = 1,
#    U(1)(X) = 2 * X,
#    U(N)(X) = 2 * X * U(N-1)(X) - U(N-2)(X)
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) ( 1 - X^2 ) * U(N)(X)^2 dX = PI/2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the highest polynomial to compute.
#
#    real X, the point at which the polynomials are to be computed.
#
#  Output:
#
#    real CX(1:N+1), the values of the N+1 Chebyshev polynomials.
#
  import numpy as np

  cx = np.zeros ( n + 1 )

  cx[0] = 1.0

  if ( n < 1 ):
    return cx

  cx[1] = 2.0 * x

  for i in range ( 2, n + 1 ):
    cx[i] = 2.0 * x * cx[i-1] - cx[i-2]

  return cx

def cheby_u_polynomial_test ( ):

#*****************************************************************************80
#
## cheby_u_polynomial_test() tests cheby_u_polynomial().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cheby_u_polynomial_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cheby_u_polynomial evaluates Chebyshev U polynomials at X.' )

  n = 10
  x = 0.25
  c = cheby_u_polynomial ( n, x )

  r8vec_print ( n + 1, c, '  Chebyshev U polynomials:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'cheby_u_polynomial_test' )
  print ( '  Normal end of execution.' )
  return

def cheby_u_matrix ( n ):

#*****************************************************************************80
#
## cheby_u_matrix() returns the cheby_u matrix.
#
#  Example:
#
#    N = 11
#
#    1  .   .    .    .    .    .     .     .   .    .
#    .  2   .    .    .    .    .     .     .   .    .
#   -1  .   4    .    .    .    .     .     .   .    .
#    . -4   .    8    .    .    .     .     .   .    .
#    1  . -12    .   16    .    .     .     .   .    .
#    .  6   .  -32    .   32    .     .     .   .    .
#   -1  .  24    .  -80    .   64     .     .   .    .
#    . -8   .   80    . -192    .   128     .   .    .
#    1  . -40    .  240    . -448     .   256   .    .
#    . 10   . -160    .  672    . -1024     . 512    .
#   -1  .  60    . -560    . 1792     . -2304   . 1024
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is generally not normal: A' * A /= A * A'.
#
#    A is lower triangular.
#
#    A is reducible.
#
#    The entries of row N sum to N.
#
#    det ( A ) = 2^((N*(N-1))/2).
#
#    LAMBDA(I) = 2^(I-1)
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  a[0,0] = 1.0

  if ( n == 1 ):
    return a

  a[1,1] = 2.0

  if ( n == 2 ):
    return a

  for i in range ( 2, n ):
    for j in range ( 0, n ):
      if ( j == 0 ):
        a[i,j] = - a[i-2,j]
      else:
        a[i,j] = 2.0 * a[i-1,j-1] - a[i-2,j]

  return a

def cheby_u_determinant ( n ):

#*****************************************************************************80
#
## cheby_u_determinant() returns the determinant of the cheby_u matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  power = ( n * ( n - 1 ) ) // 2
  determ = 2.0 ** power

  return determ

def cheby_u_inverse ( n ):

#*****************************************************************************80
#
## cheby_u_inverse() returns the inverse of the cheby_u matrix.
#
#  Example:
#
#    N = 11
#
#      1   .   .  .   .  .  .  .  .  .  .
#      .   1   .  .   .  .  .  .  .  .  .  /    2
#      1   .   1  .   .  .  .  .  .  .  .  /    4
#      .   2   .  1   .  .  .  .  .  .  .  /    8
#      2   .   3  .   1  .  .  .  .  .  .  /   16
#      .   5   .  4   .  1  .  .  .  .  .  /   32
#      5   .   9  .   5  .  1  .  .  .  .  /   64
#      .  14   . 14   .  6  .  1  .  .  .  /  128
#     14   .  28  .  20  .  7  .  1  .  .  /  256
#      .  42   . 48   . 27  .  8  .  1  .  /  512
#     42   .  90  .  75  . 35  .  9  .  1  / 1024
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,1] = 0.5

    if ( 2 < n ):

      for i in range ( 2, n ):
        for j in range ( 0, n ):
          if ( j == 0 ):
            a[i,j] =                      a[i-1,j+1]   / 2.0
          elif ( j < n - 1 ):
            a[i,j] = (       a[i-1,j-1] + a[i-1,j+1] ) / 2.0
          else:
            a[i,j] =         a[i-1,j-1]                / 2.0

  return a

def cheby_u_test ( ):

#*****************************************************************************80
#
## cheby_u_test() tests cheby_u_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cheby_u_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cheby_u_matrix() computes the cheby_u matrix.' )

  m = 5
  n = m
  a = cheby_u_matrix ( n )
  r8mat_print ( m, n, a, '  cheby_u matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'cheby_u_test' )
  print ( '  Normal end of execution.' )
  return

def cheby_van1_matrix ( m, a, b, n, x ):

#*****************************************************************************80
#
## cheby_van1_matrix() returns the Chebyshev Vandermonde-like matrix for [A,B].
#
#  Discussion:
#
#    Normally, the Chebyshev polynomials are defined on -1 <= XI <= +1.
#    Here, we assume the Chebyshev polynomials have been defined on the
#    interval A <= X <= B, using the mapping
#      XI = ( - ( B - X ) + ( X - A ) ) / ( B - A )
#    so that
#      ChebyAB(A,B;X) = Cheby(XI).
#
#    if ( I == 1 ) then
#      V(1,1:N) = 1;
#    elseif ( I == 2 ) then
#      V(2,1:N) = XI(1:N);
#    else
#      V(I,1:N) = 2.0 * XI(1:N) * V(I-1,1:N) - V(I-2,1:N);
#
#  Example:
#
#    M = 5, A = -1, B = +1, N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    1  1   1    1    1
#    1  2   3    4    5
#    1  7  17   31   49
#    1 26  99  244  485
#    1 97 577 1921 4801
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    Stability analysis of algorithms for solving confluent
#    Vandermonde-like systems,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 11, 1990, pages 23-41.
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    real A, B, the interval.
#
#    integer N, the number of values in X, and the number
#    of columns in the matrix.
#
#    real X(N), the abscissas.
#
#  Output:
#
#    real V(M,N), the matrix.
#
  import numpy as np
#
#  Compute the normalized abscissas in [-1,+1].
#
  xi = np.zeros ( n )

  for i in range ( 0, n ):
    xi[i] = ( - 1.0 * ( b - x[i]     )   \
              + 1.0 * (     x[i] - a ) ) \
            /         ( b        - a )
#
#  Compute the matrix.
#
  v = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    v[0,j] = 1.0
    v[1,j] = xi[j]
    for i in range ( 2, m ):
      v[i,j] = 2.0 * xi[j] * v[i-1,j] - v[i-2,j]

  return v

def cheby_van1_test ( ):

#*****************************************************************************80
#
## cheby_van1_test() tests cheby_van1_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cheby_van1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cheby_van1_matrix() computes the cheby_van1 matrix.' )

  m = 5
  x_lo = -5.0
  x_hi = +5.0
  x = np.linspace ( x_lo, x_hi, m )

  n = m
  a = cheby_van1_matrix ( m, x_lo, x_hi, n, x )
  r8mat_print ( m, n, a, '  cheby_van1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'cheby_van1_test' )
  print ( '  Normal end of execution.' )
  return

def cheby_van2_matrix ( n ):

#*****************************************************************************80
#
## cheby_van2_matrix() returns the cheby_van2 matrix.
#
#  Discussion:
#
#    cheby_van2 is the Chebyshev Vandermonde-like matrix.
#
#  Discussion:
#
#    The formula for this matrix has been slightly modified, by a scaling
#    factor, in order to make it closer to its inverse.
#
#  Formula:
#
#    A(I,J) = ( 1 / sqrt ( N - 1 ) ) * cos ( (I-1) * (J-1) * PI / (N-1) )
#
#  Example:
#
#    N = 4
#
#                 1      1           1           1
#    1/sqrt(3) *  1  COS(PI/3)   COS(2*PI/3) COS(3*PI/3)
#                 1  COS(2*PI/3) COS(4*PI/3) COS(6*PI/3)
#                 1  COS(3*PI/3) COS(6*PI/3) COS(9*PI/3)
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The entries of A are based on the extrema of the Chebyshev
#    polynomial T(n-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  if ( n == 1 ):
    a[0,0] = 1.0
    return a

  t = np.sqrt ( float ( n - 1 ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( i * j ) * np.pi / float ( n - 1 )
      a[i,j] = np.cos ( angle ) / t

  return a

def cheby_van2_determinant ( n ):

#*****************************************************************************80
#
## cheby_van2_determinant() returns the determinant of the cheby_van2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  import numpy as np

  if ( n <= 0 ):
    determ = 0.0
  elif ( n == 1 ):
    determ = 1.0
  else:
    determ = r8_mop ( float ( n // 2 ) ) * np.sqrt ( 2.0 ) ** ( 4 - n )

  return determ

def cheby_van2_inverse ( n ):

#*****************************************************************************80
#
## cheby_van2_inverse inverts the cheby_van2 matrix.
#
#  Discussion:
#
#    cheby_van2 is the Chebyshev Vandermonde-like matrix.
#
#  Formula:
#
#    if ( I == 1 or N ) .and. ( J == 1 or N ) then
#      A(I,J) = ( 1 / (2*sqrt(N-1)) ) * cos ( (I-1) * (J-1) * PI / (N-1) )
#    else if ( I == 1 or N ) .or. ( J == 1 or N ) then
#      A(I,J) = ( 1 / (  sqrt(N-1)) ) * cos ( (I-1) * (J-1) * PI / (N-1) )
#    else
#      A(I,J) = ( 2 /    sqrt(N-1)  ) * cos ( (I-1) * (J-1) * PI / (N-1) )
#
#
#  Example:
#
#    N = 4
#
#                1/2    1             1           1/2
#    1/sqrt(3) *  1   2*COS(PI/3)   2*COS(2*PI/3)       COS(3*PI/3)
#                 1   2*COS(2*PI/3) 2*COS(4*PI/3)       COS(6*PI/3)
#                1/2    COS(3*PI/3)   COS(6*PI/3) 1/2 * COS(9*PI/3)
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The entries of A are based on the extrema of the Chebyshev
#    polynomial T(n-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = float ( i * j ) * np.pi / float ( n - 1 )

      a[i,j] = np.cos ( angle )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 2.0 * a[i,j] / np.sqrt ( float ( n - 1 ) )

  for j in range ( 0, n ):
    a[0,j]   = 0.5 * a[0,j]
    a[n-1,j] = 0.5 * a[n-1,j]

  for i in range ( 0, n ):
    a[i,0]   = 0.5 * a[i,0]
    a[i,n-1] = 0.5 * a[i,n-1]

  return a

def cheby_van2_test ( ):

#*****************************************************************************80
#
## cheby_van2_test() tests cheby_van2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cheby_van2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cheby_van2_matrix() computes the cheby_van2 matrix.' )

  m = 5
  n = 5
  a = cheby_van2_matrix ( n )
  r8mat_print ( m, n, a, '  cheby_van2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'cheby_van2_test' )
  print ( '  Normal end of execution.' )
  return

def cheby_van3_matrix ( n ):

#*****************************************************************************80
#
## cheby_van3_matrix() returns the cheby_van3 matrix.
#
#  Discussion:
#
#    cheby_van3 is the Chebyshev Vandermonde-like matrix.
#
#  Formula:
#
#    A(I,J) = cos ( (I-1) * (J-1/2) * PI / N )
#
#  Example:
#
#    N = 4
#
#        1            1           1            1
#    COS(  PI/8)  COS(3*PI/8) COS( 5*PI/8) COS( 7*PI/8)
#    COS(2*PI/8)  COS(6*PI/8) COS(10*PI/8) COS(14*PI/8)
#    COS(3*PI/8)  COS(9*PI/8) COS(15*PI/8) COS(21*PI/8)
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is "almost" orthogonal.  A * A' = a diagonal matrix.
#
#    The entries of A are based on the zeros of the Chebyshev polynomial T(n).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = float ( i * ( 2 * j + 1 ) ) * np.pi / float ( 2 * n )

      a[i,j] = np.cos ( angle )

  return a

def cheby_van3_determinant ( n ):

#*****************************************************************************80
#
## cheby_van3_determinant() returns the determinant of the cheby_van3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  import numpy as np

  determ = r8_mop ( n + 1 ) * np.sqrt ( float ( n ) ** n ) \
    / np.sqrt ( 2.0 ** ( n - 1 ) )
 
  return determ

def cheby_van3_inverse ( n ):

#*****************************************************************************80
#
## cheby_van3_inverse inverts the cheby_van3 matrix.
#
#  Discussion:
#
#    cheby_van3 is the Chebyshev Vandermonde-like matrix.
#
#  Formula:
#
#    if J == 1 then
#      A(I,J) = (1/N) * cos ( (I-1/2) * (J-1) * PI / N )
#    else if 1 < J then
#      A(I,J) = (2/N) * cos ( (I-1/2) * (J-1) * PI / N )
#
#  Example:
#
#    N = 4
#
#    1/4  1/2 cos(  PI/8)  1/2 cos( 2*PI/8)  1/2 cos( 3*PI/8)
#    1/4  1/2 cos(3*PI/8)  1/2 cos( 6*PI/8)  1/2 cos( 9*PI/8)
#    1/4  1/2 cos(5*PI/8)  1/2 cos(10*PI/8)  1/2 cos(15*PI/8)
#    1/4  1/2 cos(7*PI/8)  1/2 cos(14*PI/8)  1/2 cos(21*PI/8)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = float ( ( 2 * i + 1 ) * j ) * np.pi / float ( 2 * n )

      a[i,j] = np.cos ( angle ) / float ( n )

  for i in range ( 0, n ):
    for j in range ( 1, n ):
      a[i,j] = 2.0 * a[i,j]

  return a

def cheby_van3_test ( ):

#*****************************************************************************80
#
## cheby_van3_test() tests cheby_van3_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cheby_van3_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cheby_van3_matrix() computes the cheby_van3 matrix.' )

  m = 5
  n = m
  a = cheby_van3_matrix ( n )
  r8mat_print ( m, n, a, '  cheby_van3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'cheby_van3_test' )
  print ( '  Normal end of execution.' )
  return

def chow_matrix ( alpha, beta, m, n ):

#*****************************************************************************80
#
## chow_matrix() returns the CHOW matrix.
#
#  Discussion:
#
#    By making ALPHA small compared with BETA, the eigenvalues can
#    all be made very close to BETA, and this is useful as a test
#    of eigenvalue computing routines.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = ALPHA + BETA
#    else if ( J <= I+1 ) then
#      A(I,J) = ALPHA^(I+1-J)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, BETA = 3, M = 5, N = 5
#
#     5  1  0  0  0
#     4  5  1  0  0
#     8  4  5  1  0
#    16  8  4  5  1
#    32 16  8  4  5
#
#    ALPHA = ALPHA, BETA = BETA, M = 5, N = 5
#
#    ALPHA+BETA 1          0          0          0
#    ALPHA^2    ALPHA+BETA 1          0          0
#    ALPHA^3    ALPHA^2    ALPHA+BETA 1          0
#    ALPHA^4    ALPHA^3    ALPHA^2    ALPHA+BETA 1
#    ALPHA^5    ALPHA^4    ALPHA^3    ALPHA^2    ALPHA+BETA
#
#  Rectangular Properties:
#
#    A is Toeplitz: constant along diagonals.
#
#    A is lower Hessenberg.
#
#  Square Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    If ALPHA is 0.0, then A is singular if and only if BETA is 0.0.
#
#    If BETA is 0.0, then A will be singular if 1 < N.
#
#    If BETA is 0.0 and N = 1, then A will be singular if ALPHA is 0.0.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    For 1 <= I < N-(N+1)/2,
#
#      LAMBDA(I) = BETA + 4 * ALPHA * cos ( i * pi / ( N+2 ) )^2,
#
#    For N-(N+1)/2+1 <= I <= N
#
#      LAMBDA(I) = BETA
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    TS Chow,
#    A class of Hessenberg matrices with known eigenvalues and inverses,
#    SIAM Review,
#    Volume 11, Number 3, 1969, pages 391-395.
#
#    Graeme Fairweather,
#    On the eigenvalues and eigenvectors of a class of Hessenberg matrices,
#    SIAM Review,
#    Volume 13, Number 2, 1971, pages 220-221.
#
#  Input:
#
#    real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    real BETA, the BETA value.  A typical value is 0.0.
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( i == j - 1 ):
        a[i,j] = 1.0
      elif ( i == j ):
        a[i,j] = alpha + beta
      elif ( j + 1 <= i ):
        a[i,j] = alpha ** ( i + 1 - j )
      else:
        a[i,j] = 0.0

  return a

def chow_determinant ( alpha, beta, n ):

#*****************************************************************************80
#
## chow_determinant() returns the determinant of the CHOW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    real BETA, the BETA value.  A typical value is 0.0.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  import numpy as np

  determ = 1.0

  k = n - ( n // 2 )

  for i in range ( 1, k + 1 ):
    angle = float ( i ) * np.pi / float ( n + 2 )
    determ = determ * ( beta + 4.0 * alpha * ( np.cos ( angle ) ) ** 2 )

  determ  = determ * beta ** ( n - k )

  return determ

def chow_eigen_left ( alpha, beta, n ):

#*****************************************************************************80
#
## chow_eigen_left() returns the left eigenvector matrix for the CHOW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    real BETA, the BETA value.  A typical value is 0.0.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real V(N,N), the left eigenvector matrix.
#
  import numpy as np

  v = np.zeros ( ( n, n ) )

  k = n - ( ( n + 1 ) // 2 )

  for i in range ( 0, k ):
    angle = float ( i + 1 ) * np.pi / float ( n + 2 )
    for j in range ( 0, n ):
      v[i,j] = alpha ** ( n - j - 1 ) * 2.0 ** ( n - j - 2 ) \
        * ( np.cos ( angle ) ) ** ( n - j ) \
        * np.sin ( ( n - j + 1 ) * angle ) / np.sin ( angle )

  for i in range ( k, n ):
    v[i,n-2] = -alpha
    v[i,n-1] = 1.0

  return v

def chow_eigen_right ( alpha, beta, n ):

#*****************************************************************************80
#
## chow_eigen_right() returns the right eigenvectors of the CHOW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    real BETA, the BETA value.  A typical value is 0.0.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real U(N,N), the right eigenvector matrix.
#
  import numpy as np

  u = np.zeros ( ( n, n ) )

  k = n - ( ( n + 1 ) // 2 )

  for j in range ( 0, k ):
    angle = float ( j + 1 ) * np.pi / float ( n + 2 )
    for i in range ( 0, n ):
      u[i,j] = alpha ** ( i ) * 2.0 ** ( i - 1 ) \
        * ( np.cos ( angle ) ) ** ( i - 1 ) \
        * np.sin ( float ( i + 2 ) * angle ) / np.sin ( angle )

  for j in range ( k, n ):
    u[0,j] = 1.0
    u[1,j] = -alpha

  return u

def chow_eigenvalues ( alpha, beta, n ):

#*****************************************************************************80
#
## chow_eigenvalues() returns the eigenvalues of the CHOW matrix.
#
#  Example:
#
#    ALPHA = 2, BETA = 3, N = 5
#
#    9.49395943
#    6.10991621
#    3.0
#    3.0
#    3.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    real BETA, the BETA value.  A typical value is 0.0.
#
#    integer N, the order of A.
#
#  Output:
#
#    real LAM(N), the eigenvalues of A.
#
  import numpy as np

  lam = np.zeros ( n )

  k = n - ( ( n + 1 ) // 2 )

  for i in range ( 0, k ):
    angle = float ( i + 1 ) * np.pi / float ( n + 2 )
    lam[i] = beta + 4.0 * alpha * ( np.cos ( angle ) ) ** 2

  for i in range ( k, n ):
    lam[i] = beta

  return lam

def chow_inverse ( alpha, beta, n ):

#*****************************************************************************80
#
## chow_inverse() returns the inverse of the Chow matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the ALPHA value.  A typical value is 1.0.
#
#    real BETA, the BETA value.  A typical value is 0.0.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  if ( 0.0 == alpha and beta == 0.0 ):

    print ( '' )
    print ( 'chow_inverse - Fatal error!' )
    print ( '  The Chow matrix is not invertible, because' )
    print ( '  ALPHA = 0 and BETA = 0.' )
    raise Exception ( 'chow_inverse - Fatal error!' )

  elif ( 0.0 == alpha and beta != 0.0 ):

    for i in range ( 0, n ):
      for j in range ( 0, n ):

        if ( i <= j ):
          a[i,j] = r8_mop ( j - i ) / beta ** ( j + 1 - i )

  elif ( 0.0 != alpha and beta == 0.0 ):

    if ( 1 < n ):
      print ( '' )
      print ( 'chow_inverse - Fatal error!' )
      print ( '  The Chow matrix is not invertible, because' )
      print ( '  BETA = 0 and 1 < N.' )
      raise Exception ( 'chow_inverse - Fatal error!' )

    a[0.0] = 1.0 / alpha

  else:

    d = np.zeros ( n + 1 )

    d[0] = 1.0
    d[1] = beta
    for i in range ( 2, n + 1 ):
      d[i] = beta * d[i-1] + alpha * beta * d[i-2]

    dp = np.zeros ( n + 2 )
    dp[0] = 1.0 / beta
    dp[1] = 1.0
    dp[2] = alpha + beta
    for i in range ( 2, n + 1 ):
      dp[i+1] = d[i] + alpha * d[i-1]

    for i in range ( 0, n ):
      for j in range ( 0, i ):
        a[i,j] = - alpha * ( alpha * beta ) ** ( i - j ) * dp[j] * d[n-1-i] \
          / dp[n+1]

      for j in range ( i, n ):
        a[i,j] = r8_mop ( i + j ) * dp[i+1] * d[n-j] / ( beta * dp[n+1] )

  return a

def chow_test ( ):

#*****************************************************************************80
#
## chow_test() tests chow_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'chow_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  chow_matrix computes the CHOW matrix.' )

  m = 5
  n = 5
  alpha = np.random.rand ( )
  alpha = round ( 50.0 * alpha ) / 5.0
  beta = np.random.rand ( )
  beta = round ( 50.0 * beta ) / 5.0
  a = chow_matrix ( alpha, beta, m, n )
  r8mat_print ( m, n, a, '  CHOW matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'chow_test' )
  print ( '  Normal end of execution.' )
  return

def circulant_matrix ( m, n, x ):

#*****************************************************************************80
#
## circulant_matrix() returns the CIRCULANT matrix.
#
#  Formula:
#
#    K = 1 + mod ( J-I, N )
#    A(I,J) = X(K)
#
#  Example:
#
#    M = 4, N = 4, X = ( 1, 2, 3, 4 )
#
#    1  2  3  4
#    4  1  2  3
#    3  4  1  2
#    2  3  4  1
#
#    M = 4, N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    1  2  3  4  5
#    5  1  2  3  4
#    4  5  1  2  3
#    3  4  5  1  2
#
#    M = 5, N = 4, X = ( 1, 2, 3, 4 )
#
#    1  2  3  4
#    5  1  2  3
#    4  5  1  2
#    3  4  5  1
#    1  2  3  4
#
#  Discussion:
#
#    Westlake lists the following "special" circulants:
#
#      B2, X = ( T^2, 1, 2, ..., T, T+1, T, T-1, ..., 1 ),
#      with T = ( N - 2 ) / 2
#
#      B3, X = ( N+1, 1, 1, ..., 1 )
#
#      B5, X = ( 1, 2, 3, ..., N ).
#
#  Rectangular Properties:
#
#    The product of two circulant matrices is a circulant matrix.
#
#    The transpose of a circulant matrix is a circulant matrix.
#
#    A circulant matrix C, whose first row is (c1, c2, ..., cn), can be
#    written as a polynomial in the upshift matrix U:
#
#      C = c1 * I + c2 * U + c3 * U^2 + ... + cn * U^(n-1).
#
#    A is a circulant: each row is shifted once to get the next row.
#
#  Square Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A commutes with any other circulant matrix.
#
#    A is normal.
#
#    The transpose of A is also a circulant matrix.
#
#    The inverse of A is also a circulant matrix.
#
#    The Fourier matrix is the eigenvector matrix for every circulant matrix.
#
#    Because the Fourier matrix F diagonalizes A, the inverse (or
#    pseudoinverse, if any LAMBDA is circulant) can be written
#
#      inverse ( A ) = (F*) * 1/LAMBDA * F
#
#    A is symmetric if, for all I, X(I+1) = X(N-I+1).
#
#    If R is an N-th root of unity, that is, R is a complex number such
#    that R^N = 1, then
#
#      Y = X(1) + X(2)*R + X(3)*R^2 + ... + X(N)*R^(N-1)
#
#    is an eigenvalue of A, with eigenvector
#
#     ( 1, R, R^2, ..., R^(N-1) )
#
#    and left eigenvector
#
#      ( R^(N-1), R^(N-2), ..., R^2, R, 1 ).
#
#    Although there are exactly N distinct roots of unity, the circulant
#    may have repeated eigenvalues, because of the behavior of the polynomial.
#    However, the matrix is guaranteed to have N linearly independent
#    eigenvectors.
#
#    A is not diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis,
#    Circulant Matrices,
#    John Wiley, 1979, QA188.D37.
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 22, 
#    LC: QA263.G68.
#
#    Joan Westlake,
#    Test Matrix A24,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#    real X(N), the values in the first row of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      k = i4_modp ( j - i, n )
      a[i,j] = x[k]

  return a

def circulant_test ( ):

#*****************************************************************************80
#
## circulant_test() tests circulant_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'circulant_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  circulant_matrix() computes the circulant matrix.' )

  m = 4
  n = 5
  x = np.array ( [ 1, 2, 3, 4, 5 ] )
  a = circulant_matrix ( m, n, x )
  r8mat_print ( m, n, a, '  circulant matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'circulant_test' )
  print ( '  Normal end of execution.' )
  return

def clement1_matrix ( n ):

#*****************************************************************************80
#
## clement1_matrix() returns the CLEMENT1 matrix.
#
#  Formula:
#
#    if ( J = I+1 )
#      A(I,J) = sqrt(I*(N-I))
#    else if ( I = J+1 )
#      A(I,J) = sqrt(J*(N-J))
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#       .    sqrt(4)    .       .       .
#    sqrt(4)    .    sqrt(6)    .       .
#       .    sqrt(6)    .    sqrt(6)    .
#       .       .    sqrt(6)    .    sqrt(4)
#       .       .       .    sqrt(4)    .
#
#  Properties:
#
#    A is tridiagonal.
#
#    A is banded, with bandwidth 3.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The diagonal of A is zero.
#
#    A is singular if N is odd.
#
#    About 64 percent of the entries of the inverse of A are zero.
#
#    The eigenvalues are plus and minus the numbers
#
#      N-1, N-3, N-5, ..., (1 or 0).
#
#    If N is even,
#
#      det ( A ) = (-1)**(N/2) * (N-1) * (N+1)**(N/2)
#
#    and if N is odd,
#
#      det ( A ) = 0
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
#  Reference:
#
#    Paul Clement,
#    A class of triple-diagonal matrices for test purposes,
#    SIAM Review,
#    Volume 1, 1959, pages 50-52.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i + 1 ):
        a[i,j] = np.sqrt ( float ( ( i + 1 ) * ( n - i - 1 ) ) )
      elif ( i == j + 1 ):
        a[i,j] = np.sqrt ( float ( ( j + 1 ) * ( n - j - 1 ) ) )
      else:
        a[i,j] = 0.0

  return a

def clement1_determinant ( n ):

#*****************************************************************************80
#
## clement1_determinant() returns the determinant of the CLEMENT1 matrix.
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
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    determ = 0.0
  else:
    determ = 1.0
    for i in range ( 1, n, 2 ):
      determ = determ * float ( ( i ) * ( n - i ) )

    if ( ( n // 2 ) % 2 == 1 ):
      determ = - determ

  return determ

def clement1_inverse ( n ):

#*****************************************************************************80
#
## clement1_inverse() returns the inverse of the CLEMENT1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.  N must not be odd%
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( ( n % 2 ) == 1 ):
    print ( '' )
    print ( 'clement1_inverse - Fatal error!' )
    print ( '  The Clement matrix is singular for odd N.' )
    raise Exception ( 'clement1_inverse - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):

      for j in range ( i, n - 1, 2 ):

        if ( j == i ):
          prod = 1.0 / np.sqrt ( float ( ( j + 1 ) * ( n - j - 1 ) ) )
        else:
          prod = - prod \
            * np.sqrt ( float ( ( j ) * ( n - j ) ) ) \
            / np.sqrt ( float ( ( j + 1 ) * ( n - j - 1 ) ) )
 
        a[i,j+1] = prod
        a[j+1,i] = prod

  return a

def clement1_test ( ):

#*****************************************************************************80
#
## clement1_test() tests clement1_matrix().
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
  import platform

  print ( '' )
  print ( 'clement1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  clement1_matrix() computes the CLEMENT1 matrix.' )

  m = 4
  n = m
  a = clement1_matrix ( n )
  r8mat_print ( n, n, a, '  CLEMENT1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'clement1_test' )
  print ( '  Normal end of execution.' )
  return

def clement2_matrix ( n, x, y ):

#*****************************************************************************80
#
## clement2_matrix() returns the CLEMENT2 matrix.
#
#  Formula:
#
#    if ( J = I + 1 ) then
#      A(I,J) = X(I)
#    else if ( I = J + 1 ) then
#      A(I,J) = Y(J)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5, X and Y arbitrary:
#
#       .   X(1)    .     .     .
#     Y(1)   .    X(2)    .     .
#       .   Y(2)    .   X(3)    .
#       .     .   Y(3)    .   X(4)
#       .     .     .   Y(4)    .
#
#    N = 5, X=(1,2,3,4), Y=(5,6,7,8):
#
#       .     1     .     .     .
#       5     .     2     .     .
#       .     6     .     3     .
#       .     .     7     .     4
#       .     .     .     8     .
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    The diagonal of A is zero.
#
#    A is singular if N is odd.
#
#    About 64 percent of the entries of the inverse of A are zero.
#
#    If N is even,
#
#      det ( A ) = (-1)^(N/2) * product ( 1 <= I <= N/2 )
#        ( X(2*I-1) * Y(2*I-1) )
#
#    and if N is odd,
#
#      det ( A ) = 0.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Clement,
#    A class of triple-diagonal matrices for test purposes,
#    SIAM Review,
#    Volume 1, 1959, pages 50-52.
#
#    Alan Edelman, Eric Kostlan,
#    The road from Kac's matrix to Kac's random polynomials.
#    In Proceedings of the Fifth SIAM Conference on Applied Linear Algebra,
#    edited by John Lewis,
#    SIAM, 1994,
#    pages 503-507.
#
#    Robert Gregory, David Karney,
#    Example 3.19,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 46, 
#    LC: QA263.G68.
#
#    Olga Taussky, John Todd,
#    Another look at a matrix of Mark Kac,
#    Linear Algebra and Applications,
#    Volume 150, 1991, pages 341-360.
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N-1), Y(N-1), the first super and
#    subdiagonals of the matrix A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i + 1 ):
        a[i,j] = x[i]
      elif ( i == j + 1 ):
        a[i,j] = y[j]
      else:
        a[i,j] = 0.0

  return a

def clement2_determinant ( n, x, y ):

#*****************************************************************************80
#
## clement2_determinant() returns the determinant of the CLEMENT2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N-1), Y(N-1), the first super and
#    subdiagonals of the matrix A.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    determ = 0.0
  else:
    determ = 1.0
    for i in range ( 0, n - 1, 2 ):
      determ = determ * x[i] * y[i]

    if ( ( n // 2 ) % 2 == 1 ):
      determ = - determ

  return determ

def clement2_inverse ( n, x, y ):

#*****************************************************************************80
#
## clement2_inverse() returns the inverse of the Clement3 matrix.
#
#  Example:
#
#    N = 6, X and Y arbitrary:
#
#     0                1/Y1 0         -X2/(Y1*Y3) 0   X2*X4/(Y1*Y3*Y5)
#     1/X1             0    0          0          0    0
#     0                0    0          1/Y3       0   -X4/(Y3*Y5)
#    -Y2/(X1*X3)       0    1/X3       0          0    0
#     0                0    0          0          0    1/Y5
#     Y2*Y4/(X1*X3*X5) 0   -Y4/(X3*X5) 0          1/X5 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Clement,
#    A class of triple-diagonal matrices for test purposes,
#    SIAM Review,
#    Volume 1, 1959, pages 50-52.
#
#  Input:
#
#    integer N, the order of A.  N must not be odd%
#
#    real X(N-1), Y(N-1), the first super and
#    subdiagonals of the matrix A.  None of the entries
#    of X or Y may be zero.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( ( n % 2 ) == 1 ):
    print ( '' )
    print ( 'clement2_inverse - Fatal error!' )
    print ( '  The  Clement matrix is singular for odd N.' )
    raise Exception ( 'clement2_inverse - Fatal error!' )

  for i in range ( 0, n - 1 ):

    if ( x[i] == 0.0 ):
      print ( '' )
      print ( 'clement2_inverse - Fatal error!' )
      print ( '  The matrix is singular' )
      print ( '  X(I) = 0 for I = %d' % ( i ) )
      raise Exception ( 'clement2_inverse - Fatal error!' )
    elif ( y[i] == 0.0 ):
      print ( '' )
      print ( 'clement2_inverse - Fatal error!' )
      print ( '  The matrix is singular' )
      print ( '  Y(I) = 0 for I = %d' % ( i ) )
      raise Exception ( 'clement2_inverse - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):

      for j in range ( i, n - 1, 2 ):

        if ( j == i ):
          prod1 = 1.0 / y[j]
          prod2 = 1.0 / x[j]
        else:
          prod1 = - prod1 * x[j-1] / y[j]
          prod2 = - prod2 * y[j-1] / x[j]

        a[i,j+1] = prod1
        a[j+1,i] = prod2

  return a

def clement2_test ( ):

#*****************************************************************************80
#
## clement2_test() tests clement2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'clement2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  clement2_matrix() computes the CLEMENT2 matrix.' )

  m = 4
  n = m
  x = - 5.0 + 10.0 * np.random.rand ( n - 1 )
  y = - 5.0 + 10.0 * np.random.rand ( n - 1 )

  a = clement2_matrix ( n, x, y )
  r8mat_print ( m, n, a, '  CLEMENT2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'clement2_test' )
  print ( '  Normal end of execution.' )
  return

def clement3_matrix ( n, x, y ):

#*****************************************************************************80
#
## clement3_matrix() returns the Clement3 matrix.
#
#  Formula:
#
#    if ( J = I + 1 ) then
#      A(I,J) = X(I)
#    else if ( I = J + 1 ) then
#      A(I,J) = Y(J)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5, X and Y arbitrary:
#
#       .   X(1)    .     .     .
#     Y(1)   .    X(2)    .     .
#       .   Y(2)    .   X(3)    .
#       .     .   Y(3)    .   X(4)
#       .     .     .   Y(4)    .
#
#    N = 5, X=(1,2,3,4), Y=(5,6,7,8):
#
#       .     1     .     .     .
#       5     .     2     .     .
#       .     6     .     3     .
#       .     .     7     .     4
#       .     .     .     8     .
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    The Clement1 and Clement2 matrices are special cases of this one.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    The diagonal of A is zero.
#
#    A is singular if N is odd.
#
#    About 64 percent of the entries of the inverse of A are zero.
#
#    If N is even,
#
#      det ( A ) = (-1)^(N/2) * product ( 1 <= I <= N/2 )
#        ( X(2*I-1) * Y(2*I-1) )
#
#    and if N is odd,
#
#      det ( A ) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Clement,
#    A class of triple-diagonal matrices for test purposes,
#    SIAM Review,
#    Volume 1, 1959, pages 50-52.
#
#    Alan Edelman, Eric Kostlan,
#    The road from Kac's matrix to Kac's random polynomials.
#    In Proceedings of the Fifth SIAM Conference on Applied Linear Algebra,
#    edited by John Lewis,
#    SIAM, 1994,
#    pages 503-507.
#
#    Robert Gregory, David Karney,
#    Example 3.19,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 46, 
#    LC: QA263.G68.
#
#    Olga Taussky, John Todd,
#    Another look at a matrix of Mark Kac,
#    Linear Algebra and Applications,
#    Volume 150, 1991, pages 341-360.
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N-1), Y(N-1), the first super and
#    subdiagonals of the matrix A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i + 1 ):
        a[i,j] = x[i]
      elif ( i == j + 1 ):
        a[i,j] = y[j]
      else:
        a[i,j] = 0.0

  return a

def clement3_test ( ):

#*****************************************************************************80
#
## clement3_test() tests clement3_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'clement3_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CLEMENT3 computes the CLEMENT3 matrix.' )

  m = 4
  n = m
  x = - 5.0 + 10.0 * np.random.rand ( n - 1 )
  y = - 5.0 + 10.0 * np.random.rand ( n - 1 )

  a = clement3_matrix ( n, x, y )
  r8mat_print ( m, n, a, '  CLEMENT3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'clement3_test' )
  print ( '  Normal end of execution.' )
  return

def clement3_determinant ( n, x, y ):

#*****************************************************************************80
#
## clement3_determinant() returns the determinant of the CLEMENT3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N-1), Y(N-1), the first super and
#    subdiagonals of the matrix A.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    determ = 0.0
  else:
    determ = 1.0
    for i in range ( 0, n - 1, 2 ):
      determ = determ * x[i] * y[i]

    if ( ( n // 2 ) % 2 == 1 ):
      determ = - determ

  return determ

def colleague_matrix ( n, c ):

#*****************************************************************************80
#
## colleague_matrix() returns the COLLEAGUE matrix.
#
#  Discussion:
#
#    The colleague matrix is an analog of the companion matrix, adapted
#    for use with polynomials represented by a sum of Chebyshev polynomials.
#
#    Let the N-th degree polynomial be defined by
#
#      P(X) = C(N)*T_N(X) + C(N-1)*T_(N-1)(X) + ... + C(1)*T1(X) + C(0)*T0(X)
#
#    where T_I(X) is the I-th Chebyshev polynomial.
#
#    Then the roots of P(X) are the eigenvalues of the colleague matrix A(C):
#
#        0   1   0   ...  0                        0    0    0   ...   0
#       1/2  0  1/2  ...  0                        0    0    0   ...   0
#        0  1/2  0   ...  0      - 1/(2*C(N)) *    0    0    0   ...   0
#       ... ... ...  ... ...                      ...  ...  ...  ...  ...
#       ... ... ...   0  1/2                      ...  ...  ...  ...   0
#       ... ... ...  1/2  0                       C(0) C(1) C(2) ... C(N-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    I J Good,
#    The Colleague Matrix: A Chebyshev Analogue of the Companion Matrix,
#    The Quarterly Journal of Mathematics,
#    Volume 12, Number 1, 1961, pages 61-68.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real C(0:N), the coefficients of the polynomial.
#    C(N) should not be zero#
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  if ( n == 1 ):

    a[0,0] = - c[0] / c[1]

  else:

    a[0,1] = 1.0

    for i in range ( 1, n ):
      a[i,i-1] = 0.5

    for i in range ( 1, n - 1 ):
      a[i,i+1] = 0.5

    for j in range ( 0, n ):
      a[n-1,j] = a[n-1,j] - 0.5 * c[j] / c[n]

  return a

def colleague_test ( ):

#*****************************************************************************80
#
## colleague_test() tests colleague_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'colleague_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  colleague_matrix() computes the COLLEAGUE matrix.' )

  m = 5
  n = m
  c = - 5.0 + 10.0 * np.random.rand ( n + 1 )
  a = colleague_matrix ( n, c )
 
  r8mat_print ( m, n, a, '  COLLEAGUE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'colleague_test' )
  print ( '  Normal end of execution.' )
  return

def combin_matrix ( alpha, beta, n ):

#*****************************************************************************80
#
## combin_matrix() returns the COMBIN matrix.
#
#  Formula:
#
#    If ( I = J ) then
#      A(I,J) = ALPHA + BETA
#    else
#      A(I,J) = BETA
#
#  Example:
#
#    N = 5, ALPHA = 2, BETA = 3
#
#    5 3 3 3 3
#    3 5 3 3 3
#    3 3 5 3 3
#    3 3 3 5 3
#    3 3 3 3 5
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    det ( A ) = ALPHA^(N-1) * ( ALPHA + N * BETA ).
#
#    LAMBDA(1:N-1) = ALPHA,
#    LAMBDA(N) = ALPHA + N * BETA.
#
#    The eigenvector associated with LAMBDA(N) is (1,1,1,...,1)/sqrt(N).
#
#    The other N-1 eigenvectors are simply any (orthonormal) basis
#    for the space perpendicular to (1,1,1,...,1).
#
#    A is nonsingular if ALPHA /= 0 and ALPHA + N * BETA /= 0.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.25,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 53,
#    LC: QA263.G68.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition,
#    Addison-Wesley, Reading, Massachusetts, 1973, page 36.
#
#  Input:
#
#    real ALPHA, BETA, scalars that define A.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a[i,j] = beta
    a[j,j] = a[j,j] + alpha

  return a

def combin_condition ( alpha, beta, n ):

#*****************************************************************************80
#
## combin_condition() returns the L1 condition of the COMBIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, BETA, scalars that define A.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real COND, the L1 condition.
#
  a_norm = abs ( alpha + beta ) + ( n - 1 ) * abs ( beta )

  b_norm_top = abs ( alpha + ( n - 1 ) * beta ) + ( n - 1 ) * abs ( beta )

  b_norm_bot = abs ( alpha * ( alpha + n * beta ) )

  b_norm = b_norm_top / b_norm_bot

  cond = a_norm * b_norm

  return cond

def combin_determinant ( alpha, beta, n ):

#*****************************************************************************80
#
## combin_determinant() returns the determinant of the COMBIN matrix.
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
#    real ALPHA, BETA, scalars that define the matrix.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = alpha ** ( n - 1 ) * ( alpha + n * beta )
 
  return determ

def combin_eigen_right ( alpha, beta, n ):

#*****************************************************************************80
#
## combin_eigen_right() returns the right eigenvectors of the COMBIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, BETA, scalars that define A.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real X(N,N), the right eigenvectors.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )

  for j in range ( 0, n - 1 ):
    x[  0,j] = +1.0
    x[j+1,j] = -1.0

  j = n - 1
  for i in range ( 0, n ):
    x[i,j] = 1.0

  return x

def combin_eigenvalues ( alpha, beta, n ):

#*****************************************************************************80
#
## combin_eigenvalues() returns the eigenvalues of the COMBIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, BETA, scalars that define A.
#
#    integer N, the order of A.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n - 1 ):
    lam[i] = alpha
  lam[n-1] = alpha + n * beta

  return lam

def combin_inverse ( alpha, beta, n ):

#*****************************************************************************80
#
## combin_inverse() returns the inverse of the combinatorial matrix A.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = (ALPHA+(N-1)*BETA) / (ALPHA*(ALPHA+N*BETA))
#    else
#      A(I,J) =             - BETA / (ALPHA*(ALPHA+N*BETA))
#
#  Example:
#
#    N = 5, ALPHA = 2, BETA = 3
#
#           14 -3 -3 -3 -3
#           -3 14 -3 -3 -3
#   1/34 *  -3 -3 14 -3 -3
#           -3 -3 -3 14 -3
#           -3 -3 -3 -3 14
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is Toeplitz: constant along diagonals.
#
#    det ( A ) = 1 / (ALPHA^(N-1) * (ALPHA+N*BETA)).
#
#    A is well defined if ALPHA /= 0.0 and ALPHA+N*BETA /= 0.
#
#    A is also a combinatorial matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition,
#    Addison-Wesley, Reading, Massachusetts, 1973, page 36.
#
#  Input:
#
#    real ALPHA, BETA, scalars that define the matrix.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  if ( alpha == 0.0 ):
    print ( '' )
    print ( 'combin_inverse - Fatal error!' )
    print ( '  The entries of the matrix are undefined' )
    print ( '  because ALPHA = 0.' )
    raise Exception ( 'combin_inverse - Fatal error!' )
  elif ( alpha + n * beta == 0.0 ):
    print ( '' )
    print ( 'combin_inverse - Fatal error!' )
    print ( '  The entries of the matrix are undefined' )
    print ( '  because ALPHA+N*BETA is zero.' )
    raise Exception ( 'combin_inverse - Fatal error!' )

  bot = alpha * ( alpha + n * beta )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = ( alpha + float ( n - 1 ) * beta ) / bot
      else:
        a[i,j] = - beta / bot

  return a

def combin_test ( ):

#*****************************************************************************80
#
## combin_test() tests combin_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'combin_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  combin_matrix() computes the COMBIN matrix.' )

  n = 4
  alpha = np.random.rand ( )
  alpha = round ( 50.0 * alpha ) / 5.0
  beta = np.random.rand ( )
  beta = round ( 50.0 * beta ) / 5.0
  a = combin_matrix ( alpha, beta, n )
  r8mat_print ( n, n, a, '  COMBIN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'combin_test' )
  print ( '  Normal end of execution.' )
  return

def companion_matrix ( n, x ):

#*****************************************************************************80
#
## companion_matrix() returns the companion matrix A for a monic polynomial.
#
#  Formula:
#
#    Let the monic N-th degree polynomial be defined by
#
#      P(t) = t^N + X(N)*t^(N-1) + X(N-1)*t^(N-2) + ... + X(2)*t + X(1)
#
#    Then
#
#      A(1,J) = X(N+1-J) for J=1 to N
#      A(I,I-1) = 1      for I=2 to N
#      A(I,J) = 0        otherwise
#
#    A is called the companion matrix of the polynomial P(t), and the
#    characteristic equation of A is P(t) = 0.
#
#    Matrices of this form are also called Frobenius matrices.
#
#    The determinant of a matrix is unaffected by being transposed,
#    and only possibly changes sign if the rows are "reflected", so
#    there are actually many possible ways to write a companion matrix:
#
#    A B C D  A 1 0 0  0 1 0 0  0 0 1 0  0 0 1 A
#    1 0 0 0  B 0 1 0  0 0 1 0  0 1 0 0  0 1 0 B
#    0 1 0 0  C 0 0 1  0 0 0 1  1 0 0 0  1 0 0 C
#    0 0 1 0  D 0 0 0  D C B A  A B C D  0 0 0 D
#
#  Example:
#
#    N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    5 4 3 2 1
#    1 0 0 0 0
#    0 1 0 0 0
#    0 0 1 0 0
#    0 0 0 1 0
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular if and only if X(1) is nonzero.
#
#    The eigenvalues of A are the roots of P(t) = 0.
#
#    If LAMBDA is an eigenvalue of A, then a corresponding eigenvector is
#      ( 1, LAMBDA, LAMBDA^2, ..., LAMBDA^(N-1) ).
#
#    If LAMBDA is an eigenvalue of multiplicity 2, then a second 
#    corresponding generalized eigenvector is
#
#      ( 0, 1, 2 * LAMBDA, ..., (N-1)*LAMBDA^(N-2) ).
#
#    For higher multiplicities, repeatedly differentiate with respect to LAMBDA.
#
#    Any matrix with characteristic polynomial P(t) is similar to A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989,
#    section 7.4.6.
#
#    Charles Kenney, Alan Laub,
#    Controllability and stability radii for companion form systems,
#    Math. Control Signals Systems, 1 (1988), pages 239-256.
#    (Gives explicit formulas for the singular values.)
#
#    James Wilkinson,
#    The Algebraic Eigenvalue Problem,
#    Oxford University Press,
#    1965, page 12.
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N), the coefficients of the polynomial 
#    which define A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):

      if ( i == 0 ):
        a[i,j] = x[n-1-j]
      elif ( i == j + 1 ):
        a[i,j] = 1.0
      else:
        a[i,j] = 0.0

  return a

def companion_condition ( n, x ):

#*****************************************************************************80
#
## companion_condition() returns the L1 condition of the COMPANION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N), the polynomial coefficients.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = abs ( x[0] )
  for i in range ( 1, n ):
    a_norm = max ( a_norm, 1.0 + abs ( x[i] ) )

  b_norm = 1.0 / abs ( x[0] )
  for i in range ( 1, n ):
    b_norm = max ( b_norm, 1.0 + abs ( x[i] ) / abs ( x[0] ) )

  value = a_norm * b_norm
 
  return value

def companion_determinant ( n, x ):

#*****************************************************************************80
#
## companion_determinant() returns the determinant of the COMPANION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N), the polynomial coefficients.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    determ = + x[0]
  else:
    determ = - x[0]
 
  return determ

def companion_inverse ( n, x ):

#*****************************************************************************80
#
## companion_inverse() returns the inverse of the COMPANION matrix.
#
#  Example:
#
#    N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    0    1    0    0    0
#    0    0    1    0    0
#    0    0    0    1    0
#    0    0    0    0    1
#   1/1 -5/1 -4/1 -3/1 -2/1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989,
#    section 7.4.6.
#
#    Charles Kenney, Alan Laub,
#    Controllability and stability radii for companion form systems,
#    Math. Control Signals Systems,
#    Volume 1, 1988, pages 239-256.
#
#    James Wilkinson,
#    The Algebraic Eigenvalue Problem,
#    Oxford University Press,
#    1965, page 12.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N), the coefficients of the polynomial
#    which define the matrix.  X(1) must not be zero.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
 
      if ( i == n - 1 ):

        if ( j == 0 ):
          a[i,j] = 1.0 / x[0]
        else:
          a[i,j] = - x[n-j] / x[0]

      elif ( i == j - 1 ):
        a[i,j] = 1.0

  return a

def companion_test ( ):

#*****************************************************************************80
#
## companion_test() tests companion_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'companion_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  companion_matrix() computes the COMPANION matrix.' )

  n = 5
  x = - 5.0 + 10.0 * np.random.rand ( n )

  a = companion_matrix ( n, x )
  m = n
  r8mat_print ( m, n, a, '  COMPANION matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'companion_test' )
  print ( '  Normal end of execution.' )
  return

def complete_symmetric_poly ( n, r, x ):

#*****************************************************************************80
#
## complete_symmetric_poly() evaluates a complete symmetric polynomial.
#
#  Discussion:
#
#    N\R  0   1         2               3
#      +--------------------------------------------------------
#    0 |  1   0         0               0
#    1 |  1   X1        X1^2            X1^3
#    2 |  1   X1+X2     X1^2+X1X2+X2^2  X1^3+X1^2X2+X1X2^2+X2^3
#    3 |  1   X1+X2+X3  ...
#
#    If X = ( 1, 2, 3, 4, 5, ... ) then
#
#    N\R  0     1     2     3     4 ...
#      +--------------------------------------------------------
#    0 |  1     0     0     0     0
#    1 |  1     1     1     1     1
#    2 |  1     3     7    15    31
#    3 |  1     6    25    90   301
#    4 |  1    10    65   350  1701
#    5 |  1    15   140  1050  6951
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#    0 <= N.
#
#    integer R, the degree of the polynomial.
#    0 <= R.
#
#    real X(N), the value of the variables.
#
#  Output:
#
#    real VALUE, the value of TAU(N,R)(X).
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'complete_symmetric_poly - Fatal error!' )
    print ( '  N < 0.' )
    raise Exception ( 'complete_symmetric_poly - Fatal error!' )

  if ( r < 0 ):
    print ( '' )
    print ( 'complete_symmetric_poly - Fatal error!' )
    print ( '  R < 0.' )
    raise Exception ( 'complete_symmetric_poly - Fatal error!' )

  tau_length = max ( n, r ) + 1
  tau = np.zeros ( tau_length )

  tau[0] = 1.0
  for nn in range ( 0, n ):
    for rr in range ( 1, r + 1 ):
      tau[rr] = tau[rr] + x[nn] * tau[rr-1]

  value = tau[r]

  return value

def complete_symmetric_poly_test ( ):

#*****************************************************************************80
#
## complete_symmetric_poly_test() tests complete_symmetric_poly().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'complete_symmetric_poly_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  complete_symmetric_poly() evaluates a complete symmetric' )
  print ( '  polynomial in a given set of variables X.' )
 
  n = 5
  x = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )
  r8vec_print ( n, x, '  Variable vector X:' )

  print ( '' )
  print ( '   N\\R     0       1       2       3       4       5' )
  print ( '' )

  for nn in range ( 0, n + 1 ):
    print ( '  %2d' % ( nn ), end = '' )
    for rr in range ( 0, 6 ):
      value = complete_symmetric_poly ( nn, rr, x )
      print ( '  %6d' % ( value ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'complete_symmetric_poly_test:' )
  print ( '  Normal end of execution.' )
  return

def complex_i_matrix ( ):

#*****************************************************************************80
#
## complex_i_matrix() returns the complex_i matrix.
#
#  Discussion:
#
#    This is a 2 by 2 matrix that behaves like the imaginary unit.
#
#  Formula:
#
#    0 1
#   -1 0
#
#  Properties:
#
#    A is integral: int ( A ) = A.
#
#    A is anti-involutional: A * A = - I
#
#    A * A * A * A = I
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(2,2): the matrix.
#
  import numpy as np

  a = np.array ( [
    [  0.0, 1.0 ], \
    [ -1.0, 0.0 ] \
  ] )

  return a

def complex_i_determinant ( ):

#*****************************************************************************80
#
## complex_i_determinant() returns the determinant of the complex_i matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 1.0

  return determ

def complex_i_inverse ( ):

#*****************************************************************************80
#
## complex_i_inverse() returns the inverse of the complex_i matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(2,2), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [  0.0, -1.0 ], \
    [ +1.0,  0.0 ] ] )

  return a

def complex_i_test ( ):

#*****************************************************************************80
#
## complex_i_test() tests complex_i_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'complex_i_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  complex_i_matrix() computes the complex_i matrix.' )

  m = 2
  n = m

  a = complex_i_matrix ( )
  r8mat_print ( m, n, a, '  complex_i matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'complex_i_test' )
  print ( '  Normal end of execution.' )
  return

def conex1_matrix ( alpha ):

#*****************************************************************************80
#
## conex1_matrix() returns the CONEX1 matrix.
#
#  Discussion:
#
#    The CONEX1 matrix is a counterexample to the LINPACK condition
#    number estimator RCOND available in the LINPACK routine DGECO.
#
#  Formula:
#
#    1  -1 -2*ALPHA   0
#    0   1    ALPHA    -ALPHA
#    0   1  1+ALPHA  -1-ALPHA
#    0   0  0           ALPHA
#
#  Example:
#
#    ALPHA = 100
#
#    1  -1  -200     0
#    0   1   100  -100
#    0   1   101  -101
#    0   0     0   100
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [
    [ 1.0, -1.0, -2.0 * alpha,   0.0         ], \
    [ 0.0,  1.0,        alpha,       - alpha ], \
    [ 0.0,  1.0,  1.0 + alpha, - 1.0 - alpha ], \
    [ 0.0,  0.0,  0.0,                 alpha ] \
  ] )

  return a

def conex1_condition ( alpha ):

#*****************************************************************************80
#
## conex1_condition() returns the L1 condition of the CONEX1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = max ( 3.0, 3.0 * abs ( alpha ) + abs ( 1.0 + alpha ) )
  v1 = abs ( 1.0 - alpha ) + abs ( 1.0 + alpha ) + 1.0
  v2 = 2.0 * abs ( alpha ) + 1.0
  v3 = 2.0 + 2.0 / abs ( alpha )
  b_norm = max ( v1, max ( v2, v3 ) )
  value = a_norm * b_norm

  return value

def conex1_determinant ( alpha ):

#*****************************************************************************80
#
## conex1_determinant() returns the determinant of the CONEX1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = alpha

  return determ

def conex1_inverse ( alpha ):

#*****************************************************************************80
#
## conex1_inverse() returns the inverse of the CONEX1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.zeros ( ( 4, 4 ) )

  a[0,0] =  1.0
  a[0,1] =  1.0 - alpha
  a[0,2] =        alpha
  a[0,3] =  2.0

  a[1,0] =  0.0
  a[1,1] =  1.0 + alpha
  a[1,2] =      - alpha
  a[1,3] =  0.0

  a[2,0] =  0.0
  a[2,1] = -1.0
  a[2,2] =  1.0
  a[2,3] =  1.0 / alpha

  a[3,0] = 0.0
  a[3,1] = 0.0
  a[3,2] = 0.0
  a[3,3] = 1.0 / alpha

  return a

def conex1_test ( ):

#*****************************************************************************80
#
## conex1_test() tests conex1_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'conex1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  conex1_matrix() computes the CONEX1 matrix.' )

  m = 4
  n = m
  alpha = 1.0 + 99.0 * np.random.rand ( n )

  a = conex1_matrix ( alpha )
  r8mat_print ( m, n, a, '  CONEX1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'conex1_test' )
  print ( '  Normal end of execution.' )
  return

def conex2_matrix ( alpha ):

#*****************************************************************************80
#
## conex2_matrix() returns the CONEX2 matrix.
#
#  Discussion:
#
#    CONEX2 is a 3 by 3 LINPACK condition number counterexample.
#
#  Formula:
#
#    1   1-1/ALPHA^2 -2
#    0   1/ALPHA     -1/ALPHA
#    0   0            1
#
#  Example:
#
#    ALPHA = 100
#
#    1  0.9999  -2
#    0  0.01    -0.01
#    0  0        1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is upper triangular.
#
#    det ( A ) = 1 / ALPHA.
#
#    LAMBDA = ( 1, 1/ALPHA, 1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#    A common value is 100.0.  ALPHA must not be zero.
#
#  Output:
#
#    real A(3,3), the matrix.
#
  import numpy as np

  if ( alpha == 0.0 ):
    print ( '' )
    print ( 'CONEX2 - Fatal error!' )
    print ( '  The input value of ALPHA was zero.' )
    raise Exception ( 'CONEX2 - Fatal error!' )

  a = np.array ( [ \
    [ 1.0, ( alpha * alpha - 1.0 ) / ( alpha * alpha ), -2.0         ], \
    [ 0.0,                     1.0 / alpha,             -1.0 / alpha ], \
    [ 0.0,                     0.0,                      1.0         ] \
  ] )

  return a

def conex2_condition ( alpha ):

#*****************************************************************************80
#
## conex2_condition() returns the L1 condition of the CONEX2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  c1 = 1.0
  c2 = abs ( 1.0 - 1.0 / alpha ** 2 ) + 1.0 / abs ( alpha )
  c3 = 3.0 + 1.0 / abs ( alpha )
  a_norm = max ( c1, max ( c2, c3 ) )
  c1 = 1.0
  c2 = abs ( ( 1.0 - alpha * alpha ) / alpha ) + abs ( alpha )
  c3 = abs ( ( 1.0 + alpha * alpha ) / alpha ** 2 ) + 2.0
  b_norm = max ( c1, max ( c2, c3 ) )
  value = a_norm * b_norm

  return value

def conex2_determinant ( alpha ):

#*****************************************************************************80
#
## conex2_determinant() returns the determinant of the CONEX2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 1.0 / alpha

  return determ

def conex2_inverse ( alpha ):

#*****************************************************************************80
#
## conex2_inverse() returns the inverse of the CONEX2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#    A common value is 100.0.  ALPHA must not be zero.
#
#  Output:
#
#    real A(3,3), the matrix.
#
  import numpy as np

  a = np.zeros ( ( 3, 3 ) )

  if ( alpha == 0.0 ):
    print ( '' )
    print ( 'conex2_inverse - Fatal error!' )
    print ( '  The input value of ALPHA was zero.' )
    raise Exception ( 'conex2_inverse - Fatal error!' )
 
  a[0,0] = 1.0
  a[0,1] = ( 1.0 - alpha * alpha ) / alpha
  a[0,2] = ( 1.0 + alpha * alpha ) / alpha ** 2

  a[1,0] = 0.0
  a[1,1] = alpha
  a[1,2] = 1.0

  a[2,0] = 0.0
  a[2,1] = 0.0
  a[2,2] = 1.0

  return a

def conex2_test ( ):

#*****************************************************************************80
#
## conex2_test() tests conex2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'conex2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  conex2_matrix() computes the CONEX2 matrix.' )

  m = 3
  n = m
  alpha = 1.0 + 99.0 * np.random.rand ( n )

  a = conex2_matrix ( alpha )
  r8mat_print ( m, n, a, '  CONEX2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'conex2_test' )
  print ( '  Normal end of execution.' )
  return

def conex3_matrix ( n ):

#*****************************************************************************80
#
## conex3_matrix() returns the CONEX3 matrix.
#
#  Formula:
#
#    if ( I = J and I < N )
#      A(I,J) =  1.0 for 1<=I<N
#    else if ( I = J = N )
#      A(I,J) = -1.0
#    else if ( J < I )
#      A(I,J) = -1.0
#    else
#      A(I,J) =  0.0
#
#  Example:
#
#    N = 5
#
#     1  0  0  0  0
#    -1  1  0  0  0
#    -1 -1  1  0  0
#    -1 -1 -1  1  0
#    -1 -1 -1 -1 -1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is lower triangular.
#
#    det ( A ) = -1.
#
#    A is unimodular.
#
#    LAMBDA = ( 1, 1, 1, 1, -1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j < i ):
        a[i,j] = -1.0
      elif ( j == i and i != n - 1 ):
        a[i,j] = 1.0
      elif ( j == i and i == n - 1 ):
        a[i,j] = - 1.0
      else:
        a[i,j] = 0.0

  return a

def conex3_condition ( n ):

#*****************************************************************************80
#
## conex3_condition() returns the L1 condition of the CONEX3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real COND, the L1 condition number.
#
  cond = float ( n ) * 2.0 ** ( n - 1 )

  return cond

def conex3_determinant ( n ):

#*****************************************************************************80
#
## conex3_determinant() returns the determinant of the CONEX3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = - 1.0

  return determ

def conex3_inverse ( n ):

#*****************************************************************************80
#
## conex3_inverse() returns the inverse of the CONEX3 matrix.
#
#  Example:
#
#    N = 5
#
#     1  0  0  0  0
#     1  1  0  0  0
#     2  1  1  0  0
#     4  2  1  1  0
#    -8 -4 -2 -1 -1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i < n - 1 ):
      
        if ( j < i ):
          a[i,j] = 2.0 ** ( i - j - 1 )
        elif ( i == j ):
          a[i,j] = 1.0

      elif ( i == n - 1 ):
      
        if ( j < i ):
          a[i,j] = - 2.0 ** ( i - j - 1 )
        else:
          a[i,j] = -1.0

  return a

def conex3_test ( ):

#*****************************************************************************80
#
## conex3_test() tests conex3_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'conex3_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  conex3_matrix() computes the CONEX3 matrix.' )

  n = 5
  a = conex3_matrix ( n )
  r8mat_print ( n, n, a, '  CONEX3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'conex3_test' )
  print ( '  Normal end of execution.' )
  return

def conex4_matrix ( ):

#*****************************************************************************80
#
## conex4_matrix() returns the CONEX4 matrix.
#
#  Discussion:
#
#    7  10   8   7
#    6   8  10   9
#    5   7   9  10
#    5   7   6   5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [
    [ 7.0, 10.0,  8.0,  7.0 ], \
    [ 6.0,  8.0, 10.0,  9.0 ], \
    [ 5.0,  7.0,  9.0, 10.0 ], \
    [ 5.0,  7.0,  6.0,  5.0 ] \
  ] )

  return a

def conex4_condition ( ):

#*****************************************************************************80
#
## conex4_condition() returns the L1 condition of the CONEX4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real COND, the L1 condition number.
#
  a_norm = 33.0
  b_norm = 136.0
  cond = a_norm * b_norm

  return cond

def conex4_determinant ( ):

#*****************************************************************************80
#
## conex4_determinant() returns the determinant of the CONEX4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = -1.0

  return determ

def conex4_inverse ( ):

#*****************************************************************************80
#
## conex4_inverse() returns the inverse of the CONEX4 matrix.
#
#  Discussion:
#
#   -41  -17   10   68
#    25   10   -6  -41
#    10    5   -3  -17
#    -6   -3    2   10
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
   [ -41.0,  -17.0,   10.0,   68.0 ], \
   [  25.0,   10.0,   -6.0,  -41.0 ], \
   [  10.0,    5.0,   -3.0,  -17.0 ], \
   [  -6.0,   -3.0,    2.0,   10.0 ] ] )

  return a

def conex4_test ( ):

#*****************************************************************************80
#
## conex4_test() tests conex4_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'conex4_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  conex4_matrix() computes the CONEX4 matrix.' )

  m = 4
  n = m

  a = conex4_matrix ( )
  r8mat_print ( m, n, a, '  CONEX4 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'conex4_test' )
  print ( '  Normal end of execution.' )
  return

def conference_matrix ( n ):

#*****************************************************************************80
#
## conference_matrix() returns the CONFERENCE matrix.
#
#  Discussion:
#
#    A conference matrix is a square matrix A of order N, with a zero
#    diagonal, and only 1's and -1's on the offdiagonal, with the property
#    that:
#
#      A * A' = (N-1) * I.
#
#    The algorithm employed here is only valid when N - 1
#    is an odd prime, or a power of an odd prime.
#
#    Conference matrices have a relationship with Hadamard matrices:
#
#      If mod ( P, 4 ) == 3, A is antisymmetric, and
#        I + A is hadamard;
#      Else A is symmetric, and
#        (   I + A, - I + A )
#        ( - I + A, - I - A) is Hadamard.
#
#  Example:
#
#    N = 8
#
#     0  1  1  1  1  1  1  1
#    -1  0 -1 -1  1 -1  1  1
#    -1  1  0 -1 -1  1 -1  1
#    -1  1  1  0 -1 -1  1 -1
#    -1 -1  1  1  0 -1 -1  1
#    -1  1 -1  1  1  0 -1 -1
#    -1 -1  1 -1  1  1  0 -1
#    -1 -1 -1  1 -1  1  1  0
#
#  Properties:
#
#    If N-1 is prime, then A[2:N,2:N] is a circulant matrix.
#
#    If N-1 = 1 mod 4, then A is symmetric.
#
#    If N-1 = 3 mod 4, then A is antisymmetric.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.  N-1 must be an
#    odd prime, or a power of an odd prime.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == 0 and j == 0 ):
        a[i,j] = 0.0
      elif ( i == 0 ):
        a[i,j] = 1.0
      elif ( j == 0 ):
        if ( ( ( n - 1 ) % 4 ) == 1 ):
          a[i,j] = 1.0
        else:
          a[i,j] = -1.0
      else:
        l = legendre_symbol ( i - j, n - 1 )
        a[i,j] = float ( l )

  return a

def conference_determinant ( n ):

#*****************************************************************************80
#
## conference_determinant() returns the determinant of the CONFERENCE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.  N-1 must be an 
#    odd prime, or a power of an odd prime.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  if ( ( ( n - 1 ) % 4 ) == 1 ):
    value = - np.sqrt ( float ( n - 1 ) ** n )
  else:
    value = + np.sqrt ( float ( n - 1 ) ** n )

  return value

def conference_inverse ( n ):

#*****************************************************************************80
#
## conference_inverse() returns the inverse of the CONFERENCE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A[N,N], the matrix.
#
  import numpy as np
 
  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == 0 and j == 0 ):
        a[i,j] = 0.0
      elif ( i == 0 ):
        a[i,j] = 1.0
      elif ( j == 0 ):
        if ( ( ( n - 1 ) % 4 ) == 1 ):
          a[i,j] = 1.0
        else:
          a[i,j] = - 1.0
      else:
        l = legendre_symbol ( i - j, n - 1 )
        a[i,j] = float ( l )

  if ( ( ( n - 1 ) % 4 ) == 3 ):
    for i in range ( 0, n ):
      for j in range ( 0, n ):
        a[i,j] = - a[i,j]

  if ( 1 < n ):
    for i in range ( 0, n ):
      for j in range ( 0, n ):
        a[i,j] = a[i,j] / float ( n - 1 )

  return a

def conference_test ( ):

#*****************************************************************************80
#
## conference_test() tests conference_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'conference_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  conference_matrix() computes the CONFERENCE matrix.' )
#
#  Note that N-1 must be an odd prime or a power of an odd prime.
#
  n = 6
  a = conference_matrix ( n )
  r8mat_print ( n, n, a, '  CONFERENCE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'conference_test' )
  print ( '  Normal end of execution.' )
  return

def creation_matrix ( m, n ):

#*****************************************************************************80
#
## creation_matrix() returns the CREATION matrix.
#
#  Example:
#
#    M = 5, N = 5
#
#    0  0  0  0  0
#    1  0  0  0  0
#    0  2  0  0  0
#    0  0  3  0  0
#    0  0  0  4  0
#
#  Properties:
#
#    A is integral: int ( A ) = A.
#
#    A is strictly lower triangular.
#
#  Square properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is singular.
#
#    A has the null vector ( 0, 0, ..., 0, 1 ).
#
#    det ( A ) = 0.
#
#    LAMBDA(1:N) = 0
#
#    A is zero except for the first lower diagonal. A^2 is zero except for
#    the second lower diagonal.  A^(N-1) is the last nonzero power of A,
#    with a single nonzero entry in the (N,1) position.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of A.
#
#    integer N, the number of columns of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      if ( i == j + 1 ):
        a[i,j] = float ( j + 1 )
      else:
        a[i,j] = 0.0

  return a

def creation_determinant ( n ):

#*****************************************************************************80
#
## creation_determinant() returns the determinant of the CREATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 0.0

  return determ

def creation_null_left ( m, n ):

#*****************************************************************************80
#
## creation_null_left() returns a left null vector for the CREATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(M), the vector.
#
  import numpy as np

  x = np.zeros ( m )
  x[0] = 1.0

  return x

def creation_null_right ( m, n ):

#*****************************************************************************80
#
## creation_null_right() returns a right null vector for the CREATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(N), the vector.
#
  import numpy as np

  x = np.zeros ( n )
  x[n-1] = 1.0

  return x

def creation_test ( ):

#*****************************************************************************80
#
## creation_test() tests creation_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'creation_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  creation_matrix() computes the CREATION matrix.' )

  m = 5
  n = 4
  a = creation_matrix ( m, n )
  r8mat_print ( m, n, a, '  CREATION matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'creation_test' )
  print ( '  Normal end of execution.' )
  return

def daub10_matrix ( n ):

#*****************************************************************************80
#
## daub10_matrix() returns the daub10 matrix.
#
#  Discussion:
#
#    The daub10 matrix is the daubechies wavelet transformation matrix
#    with 10 coefficients.
#
#  Properties:
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 10 and a multiple of 2.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( n < 10 or ( n % 2 ) != 0 ):
    print ( '' )
    print ( 'daub10 - Fatal error!' )
    print ( '  N must be at least 10 and a multiple of 2.' )
    raise Exception ( 'daub10 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c = np.array ( [ \
    0.1601023979741929, \
    0.6038292697971895, \
    0.7243085284377726, \
    0.1384281459013203, \
   -0.2422948870663823, \
   -0.0322448695846381, \
    0.0775714938400459, \
   -0.0062414902127983, \
   -0.0125807519990820, \
    0.0033357252854738 ] )

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]                    =   c[0]
    a[i,i+1]                  =   c[1]
    a[i,i4_wrap(i+2,0,n-1)]   =   c[2]
    a[i,i4_wrap(i+3,0,n-1)]   =   c[3]
    a[i,i4_wrap(i+4,0,n-1)]   =   c[4]
    a[i,i4_wrap(i+5,0,n-1)]   =   c[5]
    a[i,i4_wrap(i+6,0,n-1)]   =   c[6]
    a[i,i4_wrap(i+7,0,n-1)]   =   c[7]
    a[i,i4_wrap(i+8,0,n-1)]   =   c[8]
    a[i,i4_wrap(i+9,0,n-1)]   =   c[9]

    a[i+1,i]                  =   c[9]
    a[i+1,i+1]                = - c[8]
    a[i+1,i4_wrap(i+2,0,n-1)] =   c[7]
    a[i+1,i4_wrap(i+3,0,n-1)] = - c[6]
    a[i+1,i4_wrap(i+4,0,n-1)] =   c[5]
    a[i+1,i4_wrap(i+5,0,n-1)] = - c[4]
    a[i+1,i4_wrap(i+6,0,n-1)] =   c[3]
    a[i+1,i4_wrap(i+7,0,n-1)] = - c[2]
    a[i+1,i4_wrap(i+8,0,n-1)] =   c[1]
    a[i+1,i4_wrap(i+9,0,n-1)] = - c[0]

  return a

def daub10_condition ( n ):

#*****************************************************************************80
#
## daub10_condition() returns the L1 condition of the daub10 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real VALUE, the condition.
#
  import numpy as np

  c = np.array ( [ \
    0.1601023979741929, \
    0.6038292697971895, \
    0.7243085284377726, \
    0.1384281459013203, \
   -0.2422948870663823, \
   -0.0322448695846381, \
    0.0775714938400459, \
   -0.0062414902127983, \
   -0.0125807519990820, \
    0.0033357252854738 ] )

  a_norm = np.sum ( np.abs ( c ) )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub10_determinant ( n ):

#*****************************************************************************80
#
## daub10_determinant() returns the determinant of the daub10 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = + 1.0

  return determ

def daub10_inverse ( n ):

#*****************************************************************************80
#
## daub10_inverse() returns the inverse of the daub10 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = daub10_matrix ( n )
  a = np.transpose ( a )

  return a

def daub10_test ( ):

#*****************************************************************************80
#
## daub10_test() tests daub10_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'daub10_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  daub10_matrix() computes the daub10 matrix.' )

  m = 20
  n = m

  a = daub10_matrix ( n )
  r8mat_print ( m, n, a, '  daub10 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'daub10_test' )
  print ( '  Normal end of execution.' )
  return

def daub12_matrix ( n ):

#*****************************************************************************80
#
## daub12_matrix() returns the daub12 matrix.
#
#  Discussion:
#
#    The daub12 matrix is the daubechies wavelet transformation matrix
#    with 12 coefficients.
#
#  Properties:
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 12 and a multiple of 2.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( n < 12 or ( n % 2 ) != 0 ):
    print ( '' )
    print ( 'daub12_matrix - Fatal error!' )
    print ( '  N must be at least 12 and a multiple of 2.' )
    raise Exception ( 'daub12_matrix - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c = np.array ( [ \
    0.1115407433501095, \
    0.4946238903984533, \
    0.7511339080210959, \
    0.3152503517091982, \
   -0.2262646939654400, \
   -0.1297668675672625, \
    0.0975016055873225, \
    0.0275228655303053, \
   -0.0315820393174862, \
    0.0005538422011614, \
    0.0047772575109455, \
   -0.0010773010853085 ] )

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]                    =   c[0]
    a[i,i+1]                  =   c[1]
    a[i,i4_wrap(i+2,0,n-1)]   =   c[2]
    a[i,i4_wrap(i+3,0,n-1)]   =   c[3]
    a[i,i4_wrap(i+4,0,n-1)]   =   c[4]
    a[i,i4_wrap(i+5,0,n-1)]   =   c[5]
    a[i,i4_wrap(i+6,0,n-1)]   =   c[6]
    a[i,i4_wrap(i+7,0,n-1)]   =   c[7]
    a[i,i4_wrap(i+8,0,n-1)]   =   c[8]
    a[i,i4_wrap(i+9,0,n-1)]   =   c[9]
    a[i,i4_wrap(i+10,0,n-1)]  =   c[10]
    a[i,i4_wrap(i+11,0,n-1)]  =   c[11]

    a[i+1,i]                   =   c[11]
    a[i+1,i+1]                 = - c[10]
    a[i+1,i4_wrap(i+2,0,n-1)]  =   c[9]
    a[i+1,i4_wrap(i+3,0,n-1)]  = - c[8]
    a[i+1,i4_wrap(i+4,0,n-1)]  =   c[7]
    a[i+1,i4_wrap(i+5,0,n-1)]  = - c[6]
    a[i+1,i4_wrap(i+6,0,n-1)]  =   c[5]
    a[i+1,i4_wrap(i+7,0,n-1)]  = - c[4]
    a[i+1,i4_wrap(i+8,0,n-1)]  =   c[3]
    a[i+1,i4_wrap(i+9,0,n-1)]  = - c[2]
    a[i+1,i4_wrap(i+10,0,n-1)] =   c[1]
    a[i+1,i4_wrap(i+11,0,n-1)] = - c[0]

  return a

def daub12_condition ( n ):

#*****************************************************************************80
#
## daub12_condition() returns the L1 condition of the daub12 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real VALUE, the condition.
#
  import numpy as np

  c = np.array ( [ \
    0.1115407433501095, \
    0.4946238903984533, \
    0.7511339080210959, \
    0.3152503517091982, \
   -0.2262646939654400, \
   -0.1297668675672625, \
    0.0975016055873225, \
    0.0275228655303053, \
   -0.0315820393174862, \
    0.0005538422011614, \
    0.0047772575109455, \
   -0.0010773010853085 ] )

  a_norm = np.sum ( np.abs ( c ) )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub12_determinant ( n ):

#*****************************************************************************80
#
## daub12_determinant() returns the determinant of the daub12 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = - 1.0

  return determ

def daub12_inverse ( n ):

#*****************************************************************************80
#
## daub12_inverse() returns the inverse of the daub12 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = daub12_matrix ( n )
  a = np.transpose ( a )

  return a

def daub12_test ( ):

#*****************************************************************************80
#
## daub12_test() tests daub12_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'daub12_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  daub12_matrix() computes the daub12 matrix.' )

  m = 24
  n = m

  a = daub12_matrix ( n )
  r8mat_print ( m, n, a, '  daub12 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'daub12_test' )
  print ( '  Normal end of execution.' )
  return

def daub2_matrix ( n ):

#*****************************************************************************80
#
## daub2_matrix() returns the daub2 matrix.
#
#  Discussion:
#
#    The daub2 matrix is the daubechies wavelet transformation matrix
#    with 2 coefficients.
#
#    The daub2 matrix is also known as the Haar matrix.
#
#  Properties:
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 2 and a multiple of 2.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( n < 2 or ( n % 2 ) != 0 ):
    print ( '' )
    print ( 'daub2 - Fatal error!' )
    print ( '  N must be at least 2 and a multiple of 2.' )
    raise Exception ( 'daub2 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c0 = np.sqrt ( 2.0 ) / 2.0
  c1 = np.sqrt ( 2.0 ) / 2.0

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]     =   c0
    a[i,i+1]   =   c1

    a[i+1,i]   =   c1
    a[i+1,i+1] = - c0

  return a

def daub2_condition ( n ):

#*****************************************************************************80
#
## daub2_condition() returns the L1 condition of the daub2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real VALUE, the condition.
#
  import numpy as np

  c0 = np.sqrt ( 2.0 ) / 2.0
  c1 = np.sqrt ( 2.0 ) / 2.0

  a_norm = np.abs ( c0 ) + np.abs ( c1 )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub2_determinant ( n ):

#*****************************************************************************80
#
## daub2_determinant() returns the determinant of the daub2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 1.0

  return determ

def daub2_inverse ( n ):

#*****************************************************************************80
#
## daub2_inverse() returns the inverse of the daub2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = daub2_matrix ( n )
  a = np.transpose ( a )

  return a

def daub2_test ( ):

#*****************************************************************************80
#
## daub2_test() tests daub2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'daub2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  daub2_matrix() computes the daub2 matrix.' )

  m = 4
  n = m

  a = daub2_matrix ( n )
  r8mat_print ( m, n, a, '  daub2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'daub2_test' )
  print ( '  Normal end of execution.' )
  return

def daub4_matrix ( n ):

#*****************************************************************************80
#
## daub4_matrix() returns the daub4 matrix.
#
#  Discussion:
#
#    The daub4 matrix is the daubechies wavelet transformation matrix
#    with 4 coefficients.
#
#  Properties:
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 4 and a multiple of 2.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( n < 4 or ( n % 2 ) != 0 ):
    print ( '' )
    print ( 'daub4 - Fatal error!' )
    print ( '  N must be at least 4 and a multiple of 2.' )
    raise Exception ( 'daub4 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c0 = ( 1.0 + np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )
  c1 = ( 3.0 + np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )
  c2 = ( 3.0 - np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )
  c3 = ( 1.0 - np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]                    =   c0
    a[i,i+1]                  =   c1
    a[i,i4_wrap(i+2,0,n-1)]   =   c2
    a[i,i4_wrap(i+3,0,n-1)]   =   c3

    a[i+1,i]                  =   c3
    a[i+1,i+1]                = - c2
    a[i+1,i4_wrap(i+2,0,n-1)] =   c1
    a[i+1,i4_wrap(i+3,0,n-1)] = - c0

  return a

def daub4_condition ( n ):

#*****************************************************************************80
#
## daub4_condition() returns the L1 condition of the daub4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real VALUE, the condition.
#
  import numpy as np

  c0 = ( 1.0 + np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )
  c1 = ( 3.0 + np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )
  c2 = ( 3.0 - np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )
  c3 = ( 1.0 - np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )

  a_norm = np.abs ( c0 ) + np.abs ( c1 ) + np.abs ( c2 ) + np.abs ( c3 )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub4_determinant ( n ):

#*****************************************************************************80
#
## daub4_determinant() returns the determinant of the daub4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = - 1.0

  return determ

def daub4_inverse ( n ):

#*****************************************************************************80
#
## daub4_inverse() returns the inverse of the daub4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = daub4_matrix ( n )
  a = np.transpose ( a )

  return a

def daub4_test ( ):

#*****************************************************************************80
#
## daub4_test() tests daub4_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'daub4_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  daub4_matrix() computes the daub4 matrix.' )

  m = 8
  n = m

  a = daub4_matrix ( n )
  r8mat_print ( m, n, a, '  daub4 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'daub4_test' )
  print ( '  Normal end of execution.' )
  return

def daub6_matrix ( n ):

#*****************************************************************************80
#
## daub6_matrix() returns the daub6 matrix.
#
#  Discussion:
#
#    The daub6 matrix is the daubechies wavelet transformation matrix
#    with 6 coefficients.
#
#  Properties:
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 6 and a multiple of 2.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( n < 6 or ( n % 2 ) != 0 ):
    print ( '' )
    print ( 'daub6 - Fatal error!' )
    print ( '  N must be at least 6 and a multiple of 2.' )
    raise Exception ( 'daub6 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c0 =  1.0 + np.sqrt ( 10.0 ) +       np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c1 =  5.0 + np.sqrt ( 10.0 ) + 3.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c2 = 10.0 - np.sqrt ( 40.0 ) + 2.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c3 = 10.0 - np.sqrt ( 40.0 ) - 2.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c4 =  5.0 + np.sqrt ( 10.0 ) - 3.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c5 =  1.0 + np.sqrt ( 10.0 ) -       np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )

  c0 = c0 / np.sqrt ( 512.0 )
  c1 = c1 / np.sqrt ( 512.0 )
  c2 = c2 / np.sqrt ( 512.0 )
  c3 = c3 / np.sqrt ( 512.0 )
  c4 = c4 / np.sqrt ( 512.0 )
  c5 = c5 / np.sqrt ( 512.0 )

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]                    =   c0
    a[i,i+1]                  =   c1
    a[i,i4_wrap(i+2,0,n-1)]   =   c2
    a[i,i4_wrap(i+3,0,n-1)]   =   c3
    a[i,i4_wrap(i+4,0,n-1)]   =   c4
    a[i,i4_wrap(i+5,0,n-1)]   =   c5

    a[i+1,i]                  =   c5
    a[i+1,i+1]                = - c4
    a[i+1,i4_wrap(i+2,0,n-1)] =   c3
    a[i+1,i4_wrap(i+3,0,n-1)] = - c2
    a[i+1,i4_wrap(i+4,0,n-1)] =   c1
    a[i+1,i4_wrap(i+5,0,n-1)] = - c0

  return a

def daub6_condition ( n ):

#*****************************************************************************80
#
## daub6_condition() returns the L1 condition of the daub6 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real VALUE, the condition.
#
  import numpy as np

  c0 =  1.0 + np.sqrt ( 10.0 ) +         np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c1 =  5.0 + np.sqrt ( 10.0 ) +   3.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c2 = 10.0 - np.sqrt ( 40.0 ) +   2.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c3 = 10.0 - np.sqrt ( 40.0 ) -   2.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c4 =  5.0 + np.sqrt ( 10.0 ) -   3.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c5 =  1.0 + np.sqrt ( 10.0 ) -         np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )

  c0 = c0 / np.sqrt ( 512.0 )
  c1 = c1 / np.sqrt ( 512.0 )
  c2 = c2 / np.sqrt ( 512.0 )
  c3 = c3 / np.sqrt ( 512.0 )
  c4 = c4 / np.sqrt ( 512.0 )
  c5 = c5 / np.sqrt ( 512.0 )

  a_norm = np.abs ( c0 ) + np.abs ( c1 ) \
         + np.abs ( c2 ) + np.abs ( c3 ) \
         + np.abs ( c4 ) + np.abs ( c5 )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub6_determinant ( n ):

#*****************************************************************************80
#
## daub6_determinant() returns the determinant of the daub6 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = + 1.0

  return determ

def daub6_inverse ( n ):

#*****************************************************************************80
#
## daub6_inverse() returns the inverse of the daub6 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = daub6_matrix ( n )
  a = np.transpose ( a )

  return a

def daub6_test ( ):

#*****************************************************************************80
#
## daub6_test() tests daub6_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'daub6_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  daub6_matrix() computes the daub6 matrix.' )

  m = 12
  n = m

  a = daub6_matrix ( n )
  r8mat_print ( m, n, a, '  daub6 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'daub6_test' )
  print ( '  Normal end of execution.' )
  return

def daub8_matrix ( n ):

#*****************************************************************************80
#
## daub8_matrix() returns the daub8 matrix.
#
#  Discussion:
#
#    The daub8 matrix is the daubechies wavelet transformation matrix
#    with 8 coefficients.
#
#  Properties:
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 8 and a multiple of 2.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( n < 8 or ( n % 2 ) != 0 ):
    print ( '' )
    print ( 'daub8 - Fatal error!' )
    print ( '  N must be at least 8 and a multiple of 2.' )
    raise Exception ( 'daub8 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c0 =   0.2303778133088964
  c1 =   0.7148465705529154
  c2 =   0.6308807679298587
  c3 =  -0.0279837694168599
  c4 =  -0.1870348117190931
  c5 =   0.0308413818355607
  c6 =   0.0328830116668852
  c7 =  -0.0105974017850690

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]                    =   c0
    a[i,i+1]                  =   c1
    a[i,i4_wrap(i+2,0,n-1)]   =   c2
    a[i,i4_wrap(i+3,0,n-1)]   =   c3
    a[i,i4_wrap(i+4,0,n-1)]   =   c4
    a[i,i4_wrap(i+5,0,n-1)]   =   c5
    a[i,i4_wrap(i+6,0,n-1)]   =   c6
    a[i,i4_wrap(i+7,0,n-1)]   =   c7

    a[i+1,i]                  =   c7
    a[i+1,i+1]                = - c6
    a[i+1,i4_wrap(i+2,0,n-1)] =   c5
    a[i+1,i4_wrap(i+3,0,n-1)] = - c4
    a[i+1,i4_wrap(i+4,0,n-1)] =   c3
    a[i+1,i4_wrap(i+5,0,n-1)] = - c2
    a[i+1,i4_wrap(i+6,0,n-1)] =   c1
    a[i+1,i4_wrap(i+7,0,n-1)] = - c0

  return a

def daub8_condition ( n ):

#*****************************************************************************80
#
## daub8_condition() returns the L1 condition of the daub8 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real VALUE, the condition.
#
  import numpy as np

  c = np.array ( [ \
    0.2303778133088964, \
    0.7148465705529154, \
    0.6308807679298587, \
   -0.0279837694168599, \
   -0.1870348117190931, \
    0.0308413818355607, \
    0.0328830116668852, \
   -0.0105974017850690 ] )

  a_norm = np.sum ( np.abs ( c ) )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub8_determinant ( n ):

#*****************************************************************************80
#
## daub8_determinant() returns the determinant of the daub8 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = - 1.0

  return determ

def daub8_inverse ( n ):

#*****************************************************************************80
#
## daub8_inverse() returns the inverse of the daub8 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = daub8_matrix ( n )
  a = np.transpose ( a )

  return a

def daub8_test ( ):

#*****************************************************************************80
#
## daub8_test() tests daub8_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'daub8_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  daub8_matrix() computes the daub8 matrix.' )

  m = 16
  n = m

  a = daub8_matrix ( n )
  r8mat_print ( m, n, a, '  daub8 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'daub8_test' )
  print ( '  Normal end of execution.' )
  return

def defective_condition ( ):

#*****************************************************************************80
#
## defective_condition() returns the L1 condition of the DEFECTIVE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the condition.
#
  value = 4.0

  return value

def defective_determinant ( ):

#*****************************************************************************80
#
## defective_determinant() returns the determinant of the DEFECTIVE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def defective_eigen_left ( ):

#*****************************************************************************80
#
## defective_eigen_left() returns the left eigenvectors of the DEFECTIVE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(2,1), the left eigenvectors.
#
  import numpy as np

  a = np.array ( [ \
    [ 0.0 ], \
    [ 1.0 ] ] )

  return a

def defective_eigen_right ( ):

#*****************************************************************************80
#
## defective_eigen_right() returns the right eigenvectors of the DEFECTIVE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(2,1), the right eigenvectors.
#
  import numpy as np

  a = np.array ( [ \
    [ 1.0 ], \
    [ 0.0 ] ] )

  return a

def defective_eigenvalues ( ):

#*****************************************************************************80
#
## defective_eigenvalues() returns the eigenvalues of the DEFECTIVE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real LAMDA(2), the eigenvalues.
#
  import numpy as np

  lamda = np.array ( [ \
    [ 1.0 ], \
    [ 1.0 ] ] )

  return lamda

def defective_inverse ( ):

#*****************************************************************************80
#
## defective_inverse() returns the inverse of the DEFECTIVE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(2,2), the matrix.
#
  import numpy as np


  a = np.array( [ \
    [ 1.0, -1.0 ], \
    [ 0.0,  1.0 ] ] )

  return a

def defective_matrix ( ):

#*****************************************************************************80
#
## defective_matrix() returns the DEFECTIVE matrix.
#
#  Example:
#
#    1 1
#    0 1
#
#  Properties:
#
#    A is an integer matrix.
#
#    A is a zero-one matrix.
#
#    A is not symmetric.
#
#    A is a Toeplitz matrix.
#
#    A is upper triangular.
#
#    A is unit upper triangular.
#
#    A has the eigenvalues (1,1).
#
#    A only has one eigenvector: (1,0).
#
#    A is defective.
#
#    The determinant of A is 1.
#
#    A is not diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(2,2), the matrix.
#
  import numpy as np

  a = np.array( [ \
    [ 1.0, 1.0 ], \
    [ 0.0, 1.0 ] ] )

  return a

def defective_test ( ):

#*****************************************************************************80
#
## defective_test() tests defective_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'defective_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  defective_matrix() computes the defective matrix.' )

  m = 2
  n = 2
  a = defective_matrix ( )
  r8mat_print ( m, n, a, '  defective matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'defective_test' )
  print ( '  Normal end of execution.' )
  return

def diagonal_matrix ( m, n, x ):

#*****************************************************************************80
#
## diagonal_matrix() returns a DIAGONAL matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = X(I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 5, N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    1 0 0 0 0
#    0 2 0 0 0
#    0 0 3 0 0
#    0 0 0 4 0
#    0 0 0 0 5
#
#  Square Properties:
#
#    A is banded, with bandwidth 1.
#
#    A is nonsingular if, and only if, each X(I) is nonzero.
#
#    The inverse of A is a diagonal matrix with diagonal values 1/X(I).
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    LAMBDA(1:N) = X(1:N).
#
#    The matrix of eigenvectors of A is the identity matrix.
#
#    det ( A ) = product ( 1 <= I <= N ) X(I).
#
#    Because A is diagonal, it has property A (bipartite).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#    real X(min(M,N)), the diagonal entries of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( i == j ):
        a[i,j] = x[i]

  return a

def diagonal_condition ( n, x ):

#*****************************************************************************80
#
## diagonal_condition() returns the L1 condition of the DIAGONAL matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N), the diagonal elements.
#
#  Output:
#
#    real COND, the L1 condition.
#
  import numpy as np

  cond = np.max ( np.abs ( x ) ) / np.min ( np.abs ( x ) )

  return cond

def diagonal_determinant ( n, x ):

#*****************************************************************************80
#
## diagonal_determinant() returns the determinant of the DIAGONAL matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N-1), the diagonal elements.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0
  for i in range ( 0, n ):
    value = value * x[i]

  return value

def diagonal_eigen_left ( n, d ):

#*****************************************************************************80
#
## diagonal_eigen_left() returns left eigenvectors of the DIAGONAL matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real D(N), the diagonal entries.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  return a

def diagonal_eigen_right ( n, d ):

#*****************************************************************************80
#
## diagonal_eigen_right() returns right eigenvectors of the DIAGONAL matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real D(N), the diagonal entries.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  return a

def diagonal_eigenvalues ( n, x ):

#*****************************************************************************80
#
## diagonal_eigenvalues() returns the eigenvalues of the DIAGONAL matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N), the diagonal entries.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.copy ( x )

  return lam

def diagonal_inverse ( n, x ):

#*****************************************************************************80
#
## diagonal_inverse() returns the inverse of the DIAGONAL matrix.
#
#  Discussion:
#
#    The diagonal entries must be nonzero.
#
#  Example:
#
#    M = 5, N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    1  0   0   0   0
#    0 1/2  0   0   0
#    0  0  1/3  0   0
#    0  0   0  1/4  0
#    0  0   0   0  1/5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N , the number of rows and columns 
#    of the matrix.
#
#    real X(N), the diagonal entries of the matrix.
#
#  Output:
#
#    real A(N,N), the inverse of the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0 / x[i]

  return a

def diagonal_test ( ):

#*****************************************************************************80
#
## diagonal_test() tests diagonal_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'diagonal_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  diagonal_matrix() computes the DIAGONAL matrix.' )

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )

  a = diagonal_matrix ( m, n, x )
 
  r8mat_print ( m, n, a, '  DIAGONAL matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'diagonal_test' )
  print ( '  Normal end of execution.' )
  return

def dif1cyclic_matrix ( n ):

#*****************************************************************************80
#
## dif1cyclic_matrix() returns the cyclic first difference matrix.
#
#  Example:
#
#    N = 5
#
#    0 +1  .  . -1
#   -1  0 +1  .  .
#    . -1  0 +1  .
#    .  . -1  0 +1
#   +1  .  . -1  0
#
#  Square Properties:
#
#    A is integral: int ( A ) = A.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is antisymmetric: A' = -A.
#
#    Because A is antisymmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A has constant row sum = 0.
#
#    A has constant column sum = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )
    a[i,im1] = -1.0

    ip1 = i4_wrap ( i + 1, 0, n - 1 )
    a[i,ip1] = +1.0

  return a

def dif1cyclic_determinant ( n ):

#*****************************************************************************80
#
## dif1cyclic_determinant() returns the determinant of the DIF1CYCLIC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 0.0

  return determ

def dif1cyclic_null_left ( m, n ):

#*****************************************************************************80
#
## dif1cyclic_null_left() returns a left null vector of the DIF1CYCLIC matrix.
#
#  Discussion:
#
#    (1,1,1,...,1) is always a null vector.
#
#    If M is even,
#
#    (A,B,A,B,A,B,...,A,B) is also a null vector, for any A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of A.
#
#  Output:
#
#    real X(M), the null vector.
#
  import numpy as np

  if ( ( m % 2 ) != 0 ):

    x = np.ones ( m )

  else:

    a = 1.0
    b = 2.0
    x = np.zeros ( m )
    
    for i in range ( 0, m ):
      x[i] = a
      t = a
      a = b
      b = t

  return x

def dif1cyclic_null_right ( m, n ):

#*****************************************************************************80
#
## dif1cyclic_null_right() returns a right null vector of the DIF1CYCLIC matrix.
#
#  Discussion:
#
#    (1,1,1,...,1) is always a null vector.
#
#    If N is even,
#
#    (A,B,A,B,A,B,...,A,B) is also a null vector, for any A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of A.
#
#  Output:
#
#    real X(N), the null vector.
#
  import numpy as np

  if ( ( n % 2 ) != 0 ):

    x = np.ones ( n )

  else:

    a = 1.0
    b = 2.0
    x = np.zeros ( n )
    
    for i in range ( 0, n ):
      x[i] = a
      t = a
      a = b
      b = t

  return x

def dif1cyclic_test ( ):

#*****************************************************************************80
#
## dif1cyclic_test() tests dif1cyclic_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'dif1cyclic_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dif1cyclic_matrix() computes the DIF1CYCLIC matrix.' )

  m = 5
  n = m

  a = dif1cyclic_matrix ( n )
 
  r8mat_print ( m, n, a, '  DIF1CYCLIC matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'dif1cyclic_test' )
  print ( '  Normal end of execution.' )
  return

def dif1_matrix ( m, n ):

#*****************************************************************************80
#
## dif1_matrix() returns the DIF1 matrix.
#
#  Discussion:
#
#    DIF1 is the first difference matrix.
#
#    For a set of N points X(I) with equal spacing H, and a set of data
#    values Y(I) associated with those points, the product 
#    1/(2*H) * A * Y returns an approximation to the first derivative
#    of Y(X) at the interior points X(2:N-1).
#
#  Example:
#
#    N = 5
#
#    0 +1  .  .  .
#   -1  0 +1  .  .
#    . -1  0 +1  .
#    .  . -1  0 +1
#    .  .  . -1  0
#
#  Rectangular Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is integral: int ( A ) = A.
#
#    A is Toeplitz: constant along diagonals.
#
#  Square Properties:
#
#    A is antisymmetric: A' = -A.
#
#    Because A is antisymmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    If N is even, then A is nonsingular.
#    If N is odd, then A is singular.
#
#    If N is even, det ( A ) = 1.0.
#    If N is odd, det ( A ) = 0.0.
#
#    If N is odd, a null vector is ( 1, 0, 1, 0, ..., 1, 0, 1 )..
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
      
    if ( 0 <= i - 1 ):
      a[i,i-1] = -1.0

    if ( i + 1 <= n - 1 ):
      a[i,i+1] = +1.0

  return a

def dif1_determinant ( n ):

#*****************************************************************************80
#
## dif1_determinant() returns the determinant of the DIF1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 0 ):
    determ = 1.0
  else:
    determ = 0.0

  return determ

def dif1_inverse ( n ):

#*****************************************************************************80
#
## dif1_inverse() returns the inverse of the DIF1 matrix.
#
#  Discussion:
#
#    The inverse only exists when N is even.
#
#  Example:
#
#    N = 8
#
#    0 -1  0 -1  0 -1  0 -1
#    1  0  0  0  0  0  0  0
#    0  0  0 -1  0 -1  0 -1
#    1  0  1  0  0  0  0  0
#    0  0  0  0  0 -1  0 -1
#    1  0  1  0  1  0  0  0
#    0  0  0  0  0  0  0 -1
#    1  0  1  0  1  0  1  0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( ( n % 2 ) != 0 ):
    print ( '' )
    print ( 'dif1_inverse - Fatal error!' )
    print ( '  Inverse only exists for N even.' )
    raise Exception ( 'dif1_inverse - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n - 1, 2 ):
    for j in range ( i + 1, n, 2 ):
      a[i,j] = -1.0

  for i in range ( 1, n, 2 ):
    for j in range ( 0, i, 2 ):
      a[i,j] = 1.0

  return a

def dif1_null_left ( m, n ):

#*****************************************************************************80
#
## dif1_null_left() returns a left null vector for the DIF1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(M), a left null vector.
#
  import numpy as np

  x = np.zeros ( m )

  if ( ( m % 2 ) == 0 ):
    print ( '' )
    print ( 'dif1_null_left - Fatal error!' )
    print ( '  The matrix is not singular for even M.' )
    raise Exception ( 'dif1_null_left - Fatal error!' )

  for i in range ( 0, m, 2 ):
    x[i] = 1.0

  return x

def dif1_null_right ( m, n ):

#*****************************************************************************80
#
## dif1_null_right() returns a right null vector for the DIF1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(N), a right null vector.
#
  import numpy as np

  x = np.zeros ( n )

  if ( ( n % 2 ) == 0 ):
    print ( '' )
    print ( 'dif1_null_right - Fatal error!' )
    print ( '  The matrix is not singular for even N.' )
    raise Exception ( 'dif1_null_right - Fatal error!' )

  for i in range ( 0, n, 2 ):
    x[i] = 1.0

  return x

def dif1_test ( ):

#*****************************************************************************80
#
## dif1_test() tests dif1_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'dif1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dif1_matrix() computes the DIF1 matrix.' )

  m = 5
  n = m

  a = dif1_matrix ( m, n )
 
  r8mat_print ( m, n, a, '  DIF1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'dif1_test' )
  print ( '  Normal end of execution.' )
  return

def dif2cyclic_matrix ( n ):

#*****************************************************************************80
#
## dif2cyclic_matrix() returns the cyclic second difference matrix.
#
#  Example:
#
#    N = 5
#
#    2 -1  .  . -1
#   -1  2 -1  .  .
#    . -1  2 -1  .
#    .  . -1  2 -1
#   -1  .  . -1  2
#
#  Square Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    A is a circulant: each row is shifted once to get the next row.
#
#    A is (weakly) row diagonally dominant.
#
#    A is (weakly) column diagonally dominant.
#
#    A is singular.
#
#    det ( A ) = 0.
#
#    (1,1,...,1) is a null vector of A.
#
#    A is cyclic tridiagonal.
#
#    A is Toeplitz: constant along diagonals.
#
#    A has constant row sum = 0.
#
#    A has constant column sum = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )
    a[i,im1] = -1.0

    a[i,i] = 2.0

    ip1 = i4_wrap ( i + 1, 0, n - 1 )
    a[i,ip1] = -1.0

  return a

def dif2cyclic_determinant ( n ):

#*****************************************************************************80
#
## dif2cyclic_determinant() returns the determinant of the DIF2CYCLIC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 0.0

  return determ

def dif2cyclic_null_left ( m, n ):

#*****************************************************************************80
#
## dif2cyclic_null_left() returns a left null vector for the DIF2CYCLIC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(M), a right null vector.
#
  import numpy as np

  x = np.ones ( m )

  return x

def dif2cyclic_null_right ( m, n ):

#*****************************************************************************80
#
## dif2cyclic_null_right() returns a right null vector for the DIF2CYCLIC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(N), a right null vector.
#
  import numpy as np

  x = np.ones ( n )

  return x

def dif2cyclic_test ( ):

#*****************************************************************************80
#
## dif2cyclic_test() tests dif2cyclic_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'dif2cyclic_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dif2cyclic_matrix computes the DIF2CYCLIC matrix.' )

  m = 5
  n = m

  a = dif2cyclic_matrix ( n )
 
  r8mat_print ( m, n, a, '  DIF2CYCLIC matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'dif2cyclic_test' )
  print ( '  Normal end of execution.' )
  return

def dif2_matrix ( m, n ):

#*****************************************************************************80
#
## dif2_matrix() returns the second difference matrix.
#
#  Example:
#
#    N = 5
#
#    2 -1  .  .  .
#   -1  2 -1  .  .
#    . -1  2 -1  .
#    .  . -1  2 -1
#    .  .  . -1  2
#
#  Rectangular Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is integral: int ( A ) = A.
#
#    A is Toeplitz: constant along diagonals.
#
#  Square Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is positive definite.
#
#    A is an M matrix.
#
#    A is weakly diagonally dominant, but not strictly diagonally dominant.
#
#    A has an LU factorization A = L * U, without pivoting.
#
#      The matrix L is lower bidiagonal with subdiagonal elements:
#
#        L(I+1,I) = -I/(I+1)
#
#      The matrix U is upper bidiagonal, with diagonal elements
#
#        U(I,I) = (I+1)/I
#
#      and superdiagonal elements which are all -1.
#
#    A has a Cholesky factorization A = L * L', with L lower bidiagonal.
#
#      L(I,I) =    sqrt ( (I+1) / I )
#      L(I,I-1) = -sqrt ( (I-1) / I )
#
#    The eigenvalues are
#
#      LAMBDA(I) = 2 + 2 * COS(I*PI/(N+1))
#                = 4 SIN^2(I*PI/(2*N+2))
#
#    The corresponding eigenvector X(I) has entries
#
#       X(I)(J) = sqrt(2/(N+1)) * sin ( I*J*PI/(N+1) ).
#
#    Simple linear systems:
#
#      x = (1,1,1,...,1,1),   A*x=(1,0,0,...,0,1)
#
#      x = (1,2,3,...,n-1,n), A*x=(0,0,0,...,0,n+1)
#
#    det ( A ) = N + 1.
#
#    The value of the determinant can be seen by induction,
#    and expanding the determinant across the first row:
#
#      det ( A(N) ) = 2 * det ( A(N-1) ) - (-1) * (-1) * det ( A(N-2) )
#                = 2 * N - (N-1)
#                = N + 1
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.18,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 45, 
#    LC: QA263.G68.
#
#    Morris Newman, John Todd,
#    Example A8,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    John Todd,
#    Example A8,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Academic Press, 1977, page 1.
#
#    Joan Westlake,
#    Test Matrix A15,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    if ( 0 <= i - 1 and i - 1 < n ):
      a[i,i-1] = -1.0
    if ( i < n ):
      a[i,i] = 2.0
    if ( i + 1 < n ):
      a[i,i+1] = -1.0

  return a

def dif2_condition ( n ):

#*****************************************************************************80
#
## dif2_condition() returns the L1 condition of the DIF2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  if ( n == 1 ):
    a_norm = 2.0
  elif ( n == 2 ):
    a_norm = 3.0
  else:
    a_norm = 4.0

  b_norm = 0.0
  for j in range ( 1, n + 1 ):
    t = 0.0
    for i in range ( 1, n + 1 ):
      if ( i <= j ):
        t = t + float ( i * ( n - j + 1 ) ) / float ( n + 1 )
      else:
        t = t + float ( j * ( n - i + 1 ) ) / float ( n + 1 )

    b_norm = max ( b_norm, t )

  value = a_norm * b_norm

  return value

def dif2_determinant ( n ):

#*****************************************************************************80
#
## dif2_determinant() returns the determinant of the DIF2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = n + 1

  return determ

def dif2_eigen_right ( n ):

#*****************************************************************************80
#
## dif2_eigen_right() returns the right eigenvectors of the DIF2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the right eigenvector matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( ( i + 1 ) *  ( j + 1 ) ) * np.pi / float ( n + 1 )
      a[i,j] = np.sqrt ( 2.0 / float ( n + 1 ) ) * np.sin ( angle )

  return a

def dif2_eigenvalues ( n ):

#*****************************************************************************80
#
## dif2_eigenvalues() returns the eigenvalues of the second difference matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    lam[i] = 4.0 * ( np.sin ( angle ) ) ** 2

  return lam

def dif2_inverse ( n ):

#*****************************************************************************80
#
## dif2_inverse() returns the inverse of the second difference matrix.
#
#  Formula:
#
#    if ( I <= J )
#      A(I,J) = I * (N-J+1) / (N+1)
#    else
#      A(I,J) = J * (N-I+1) / (N+1)
#
#  Example:
#
#    N = 4
#
#            4 3 2 1
#    (1/5) * 3 6 4 2
#            2 4 6 3
#            1 2 3 4
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    det ( A ) = 1 / ( N + 1 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros  ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = float ( ( i + 1 ) * ( n - j ) ) / float ( n + 1 )
      else:
        a[i,j] = float ( ( j + 1 ) * ( n - i ) ) / float ( n + 1 )

  return a

def dif2_llt ( n ):

#*****************************************************************************80
#
## dif2_llt() returns the lower triangular Cholesky factor of the DIF2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = np.sqrt ( float ( i + 2 ) ) / np.sqrt ( float ( i + 1 ) )

  for i in range ( 1, n ):
    a[i,i-1] = - np.sqrt ( float ( i ) ) / np.sqrt ( float ( i + 1 ) )

  return a

def dif2_lu ( n ):

#*****************************************************************************80
#
## dif2_lu() returns the LU factors of the DIF2 matrix.
#
#  Discussion:
#
#    A = L * U
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real L(N,N), U(N,N), the LU factors of A.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    l[i,i] = 1.0
  for i in range ( 0, n - 1 ):
    l[i+1,i] = - float ( i + 1 ) / float ( i + 2 )

  u = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    u[i,i] = float ( i + 2 ) / float ( i + 1 )
  for i in range ( 0, n - 1 ):
    u[i,i+1] = -1.0

  return l, u

def dif2_plu ( n ):

#*****************************************************************************80
#
## dif2_plu() returns the PLU factors of the DIF2 matrix.
#
#  Discussion:
#
#    A = P * L * U
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the pivot
#    matrix, the unit lower triangular matrix, and the upper
#    triangular matrix that form the PLU factoriztion of A.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    p[i,i] = 1.0

  l = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    l[i,i] = 1.0
  for i in range ( 0, n - 1 ):
    l[i+1,i] = - float ( i + 1 ) / float ( i + 2 )

  u = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    u[i,i] = float ( i + 2 ) / float ( i + 1 )
  for i in range ( 0, n - 1 ):
    u[i,i+1] = -1.0

  return p, l, u

def dif2_rhs ( m, k ):

#*****************************************************************************80
#
## dif2_rhs() returns the DIF2 right hand side.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the row dimension.
#
#    integer K, the column dimension ( should be 2).
#
#  Output:
#
#    real B(M,K), the right hand side matrix.
#
  import numpy as np

  b = np.zeros ( ( m, k ) )

  if ( 1 <= k ):
    b[0,0]   = 1.0
    b[m-1,0] = 1.0

    if ( 2 <= k ):
      b[m-1,1] = float ( m + 1 )

  return b

def dif2_rtr ( n ):

#*****************************************************************************80
#
## dif2_rtr() returns the upper triangular Cholesky factor of the DIF2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = np.sqrt ( float ( i + 2 ) ) / np.sqrt ( float ( i + 1 ) )

  for i in range ( 1, n ):
    a[i-1,i] = - np.sqrt ( float ( i ) ) / np.sqrt ( float ( i + 1 ) )

  return a

def dif2_solution ( n, k ):

#*****************************************************************************80
#
## dif2_solution() returns the DIF2 solution matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the row dimension.
#
#    integer K, the column dimension (should be 2).
#
#  Output:
#
#    real X(N,K), the solution matrix.
#
  import numpy as np

  x = np.zeros ( ( n, k ) )

  if ( 1 <= k ):

    for i in range ( 0, n ):
      x[i,0] = 1.0

    if ( 2 <= k ):
      for i in range ( 0, n ):
        x[i,1] = float ( i + 1 )

  return x

def dif2_test ( ):

#*****************************************************************************80
#
## dif2_test() tests dif2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'dif2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dif2_matrix computes the DIF2 matrix.' )

  m = 5
  n = m

  a = dif2_matrix ( m, n )
 
  r8mat_print ( m, n, a, '  DIF2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'dif2_test' )
  print ( '  Normal end of execution.' )
  return

def dorr_matrix ( alpha, n ):

#*****************************************************************************80
#
## dorr_matrix() returns the DORR matrix.
#
#  Formula:
#
#    if ( I <= (N+1) / 2 )
#
#      if ( J = I - 1 )
#        A(I,J) = - ALPHA * (N+1)^2
#      else if ( J = I )
#        A(I,J) = 2 * ALPHA * (N+1)^2 + 0.5 * (N+1) - I
#      else if ( J = I + 1 )
#        A(I,J) = - ALPHA * (N+1)^2 - 0.5 * (N+1) + I
#      else
#        A(I,J) = 0
#
#    else
#
#      if ( J = I - 1 )
#        A(I,J) = - ALPHA * (N+1)^2 + 0.5 * (N+1) - I
#      else if ( J = I )
#        A(I,J) = 2 * ALPHA * (N+1)^2 - 0.5 * (N+1) + I
#      else if ( J = I + 1 )
#        A(I,J) = - ALPHA * (N+1)^2
#      else
#        A(I,J) = 0
#
#  Example:
#
#    ALPHA = 7, N = 5
#
#     506 -254    0    0    0
#    -252  505 -253    0    0
#       0 -252  504 -252    0
#       0    0 -253  505 -252
#       0    0    0 -254  506
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is row diagonally dominant, since the absolute value of the diagonal
#    entry always equals ( or exceeds, I = 1 and N ) the sum of the
#    absolute values of the two off diagonal row entries.
#
#    A is irreducibly diagonally dominant, and hence nonsingular.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is an M matrix.
#
#    0 < INVERSE(A).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    A is symmetrizable.  There is a positive definite diagonal matrix
#    D so that INVERSE(D)*A*D is symmetric.
#
#    The eigenvalues of A are positive, so the matrix
#    INVERSE(D)*A*D is positive definite.
#
#    The Gauss-Seidel and Jacobi iterative methods for solving
#    A*x = b both converge.  Furthermore, if RHO(GS) is the
#    spectral radius of the Gauss-Seidel iteration matrix, and
#    RHO(J) the spectral radius of the Jacobi iteration matrix,
#    then RHO(GS) = RHO(J)^2 < 1.
#
#    A is ill-conditioned for small values of ALPHA.  The
#    test case used N = 100, and ALPHA=0.01, 0.003, 0.001 and
#    1.0D-10.  The matrix A was already very ill-conditioned for
#    ALPHA = 0.003, with the minimum eigenvalue being 1.8D-12, and
#    the maximum one being 199.87.
#
#    The columns of INVERSE(A) vary greatly in norm.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Fred Dorr,
#    An example of ill-conditioning in the numerical solution of
#    singular perturbation problems,
#    Mathematics of Computation,
#    Volume 25, Number 114, 1971, pages 271-283.
#
#  Input:
#
#    real ALPHA, scalar that defines the matrix.
#    A typical value of ALPHA is 0.01.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  np1_r8 = float ( n + 1 )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
 
      if ( i + 1 <= ( ( n + 1 ) // 2 ) ):

        if ( j == i - 1 ):
          a[i,j] = - alpha * np1_r8 ** 2
        elif ( j == i ):
          a[i,j] = 2.0 * alpha * np1_r8 ** 2 + 0.5 * np1_r8 - float ( i + 1 )
        elif ( j == i + 1 ):
          a[i,j] = - alpha * np1_r8 ** 2 - 0.5 * np1_r8 + float ( i + 1 )

      else:

        if ( j == i - 1 ):
          a[i,j] = - alpha * np1_r8 ** 2 + 0.5 * np1_r8 - float ( i + 1 )
        elif ( j == i ):
          a[i,j] = 2.0 * alpha * np1_r8 ** 2 - 0.5 * np1_r8 + float ( i + 1 )
        elif ( j == i + 1 ):
          a[i,j] = - alpha * np1_r8 ** 2
 
  return a

def dorr_determinant ( alpha, n ):

#*****************************************************************************80
#
## dorr_determinant() returns the determinant of the DORR matrix.
#
#  Discussion:
#
#    The DORR matrix is a special case of the TRIV matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the parameter.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np
#
#  Form the three diagonals.
#
  x = np.zeros ( n - 1 )
  y = np.zeros ( n )
  z = np.zeros ( n - 1 )

  np1_r8 = float ( n + 1 )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i + 1 <=  ( ( n + 1 ) // 2 ) ):

        if ( j == i - 1 ):
          x[i-1] = - alpha * np1_r8 ** 2
        elif ( j == i ):
          y[i] = 2.0 * alpha * np1_r8 ** 2 + 0.5 * np1_r8 - float ( i + 1 )
        elif ( j == i + 1 ):
          z[i] = - alpha * np1_r8 ** 2 - 0.5 * np1_r8 + float ( i + 1 )

      else:

        if ( j == i - 1 ):
          x[i-1] = - alpha * np1_r8 ** 2 + 0.5 * np1_r8 - float ( i + 1 )
        elif ( j == i ):
          y[i] = 2.0 * alpha * np1_r8 ** 2 - 0.5 * np1_r8 + float ( i + 1 )
        elif ( j == i + 1 ):
          z[i] = - alpha * np1_r8 ** 2
#
#  Now evaluate the determinant.
#
  determ_nm1 = y[n-1]

  if ( n == 1 ):
    value = determ_nm1
    return value

  determ_nm2 = determ_nm1
  determ_nm1 = y[n-2] * y[n-1] - z[n-2] * x[n-2]

  if ( n == 2 ):
    value = determ_nm1
    return value

  for i in range ( n - 3, -1, -1 ):

    value = y[i] * determ_nm1 - z[i] * x[i] * determ_nm2

    determ_nm2 = determ_nm1
    determ_nm1 = value

  return value

def dorr_inverse ( alpha, n ):

#*****************************************************************************80
#
## dorr_inverse() returns the inverse of the DORR matrix.
#
#  Discussion:
#
#    The DORR matrix is a special case of the TRIV matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    CM daFonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Input:
#
#    real ALPHA, the parameter.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the inverse of the matrix.
#
  import numpy as np
#
#  Form the three diagonals.
#
  x = np.zeros ( n - 1 )
  y = np.zeros ( n )
  z = np.zeros ( n - 1 )

  np1 = float ( n + 1 )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i + 1 <= ( ( n + 1 ) // 2 ) ):

        if ( j == i - 1 ):
          x[i-1] = - alpha * np1 ** 2
        elif ( j == i ):
          y[i] = 2.0 * alpha * np1 ** 2 + 0.5 * np1 - float ( i + 1 )
        elif ( j == i + 1 ):
          z[i] = - alpha * np1 ** 2 - 0.5 * np1 + float ( i + 1 )

      else:

        if ( j == i - 1 ):
          x[i-1] = - alpha * np1 ** 2 + 0.5 * np1 - float ( i + 1 )
        elif ( j == i ):
          y[i] = 2.0 * alpha * np1 ** 2 - 0.5 * np1 + float ( i + 1 )
        elif ( j == i + 1 ):
          z[i] = - alpha * np1 ** 2
#
#  Now evaluate the inverse.
#
  a = np.zeros ( ( n, n ) )

  d = np.zeros ( n )
  e = np.zeros ( n )

  d[n-1] = y[n-1]
  for i in range ( n - 2, -1, -1 ):
    d[i] = y[i] - x[i] * z[i] / d[i+1]

  e[0] = y[0]
  for i in range ( 1, n ):
    e[i] = y[i] - x[i-1] * z[i-1] / e[i-1]

  for i in range ( 0, n ):

    for j in range ( 0, i + 1 ):

      p1 = 1.0
      for k in range ( j, i ):
        p1 = p1 * x[k]
      p2 = 1.0
      for k in range ( i + 1, n ):
        p2 = p2 * d[k]
      p3 = 1.0
      for k in range ( j, n ):
        p3 = p3 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 * p2 / p3

    for j in range ( i + 1, n ):

      p1 = 1.0
      for k in range ( i, j ):
        p1 = p1 * z[k]
      p2 = 1.0
      for k in range ( j + 1, n ):
        p2 = p2 * d[k]
      p3 = 1.0
      for k in range ( i, n ):
        p3 = p3 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 * p2 / p3

  return a

def dorr_test ( ):

#*****************************************************************************80
#
## dorr_test() tests dorr_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'dorr_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dorr_matrix computes the DORR matrix.' )

  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  a = dorr_matrix ( alpha, n )
  r8mat_print ( n, n, a, '  DORR matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'dorr_test' )
  print ( '  Normal end of execution.' )
  return

def downshift_matrix ( n ):

#*****************************************************************************80
#
## downshift_matrix() returns the DOWNSHIFT matrix.
#
#  Formula:
#
#    if ( I-J == 1 mod ( n ) )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 4
#
#    0 0 0 1
#    1 0 0 0
#    0 1 0 0
#    0 0 1 0
#
#  Rectangular properties:
#
#    A is integral: int ( A ) = A.
#
#    A is a zero/one matrix.
#
#  Square Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular.
#
#    A is a permutation matrix.
#
#    det ( A ) = (-1)^(N-1)
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    A is an N-th root of the identity matrix.
#    Therefore, the inverse of A = A^(N-1).
#
#    Any circulant matrix generated by a column vector v can be regarded as
#    the Krylov matrix ( v, A*v, A^2*V, ..., A^(N-1)*v).
#
#    The inverse of A is the upshift operator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i4_modp ( i - j, n ) == 1 ):
        a[i,j] = 1.0

  return a

def downshift_condition ( n ):

#*****************************************************************************80
#
## downshift_condition() returns the L1 condition of the DOWNSHIFT matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE the L1 condition.
#
  a_norm = 1.0
  b_norm = 1.0
  value = a_norm * b_norm

  return value

def downshift_determinant ( n ):

#*****************************************************************************80
#
## downshift_determinant() returns the determinant of the DOWNSHIFT matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 0 ):
    determ = - 1.0
  else:
    determ = 1.0

  return determ

def downshift_inverse ( n ):

#*****************************************************************************80
#
## downshift_inverse() returns the inverse of the DOWNSHIFT matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the inverse.
#
  a = upshift_matrix ( n )

  return a

def downshift_test ( ):

#*****************************************************************************80
#
## downshift_test() tests downshift_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'downshift_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  downshift_matrix computes the DOWNSHIFT matrix.' )

  m = 5
  n = m

  a = downshift_matrix ( n )
 
  r8mat_print ( m, n, a, '  DOWNSHIFT matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'downshift_test' )
  print ( '  Normal end of execution.' )
  return

def eberlein_matrix ( alpha, n ):

#*****************************************************************************80
#
## eberlein_matrix() returns the Eberlein matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = - ( 2 * I - 1 ) * ( N - 1 ) - ( I - 1 ) * ALPHA + 2 * ( I - 1 )^2
#    else if ( J = I+1 )
#      A(I,J) = I * ( N + ALPHA - I )
#    else if ( J = I-1 )
#      A(I,J) = ( I - 1 ) * ( N - I + 1 )
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5, ALPHA = 2
#
#    -4   6   0   0   0
#     4 -12  10   0   0
#     0   6 -16  12   0
#     0   0   6 -16  12
#     0   0   0   4 -12
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    The matrix is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    The sum of the entries in any row except the last one is ALPHA.
#
#    The sum of the entries in the last row is -(N-1)*ALPHA.
#
#    The sum of the entries in any column is zero.
#
#    A is singular.
#
#    det ( A ) = 0
#
#    A has the LEFT null vector ( 1, 1, ..., 1 ).
#
#    LAMBDA(I) = - ( I - 1 ) * ( ALPHA + I ).
#
#    Left eigenvectors are
#
#      V^J(I) = 1/COMB(N-1,I-1) * sum ( 0 <= K <= min ( I, J ) ) [ (-1)^K *
#        COMB(N-1-K,N-I) * COMB(J-1,K) * COMB(ALPHA+J-1+K, K )
#
#    For ALPHA = -2, ..., -2*(N-1), the matrix is defective with two or more
#    pairs of eigenvectors coalescing.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Patricia Eberlein,
#    A Two-Parameter Test Matrix,
#    Mathematics of Computation,
#    Volume 18, 1964, pages 296-298.
#
#    Joan Westlake,
#    Test Matrix A41,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Input:
#
#    real ALPHA, the parameter.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i ):

        a[i,j] = - ( ( 2 * i + 1 ) * ( n - 1 )  +  i * alpha - 2 * i * i )

      elif ( j == i + 1 ):

        a[i,j] =  ( i + 1 ) * ( n - i - 1 + alpha )

      elif ( j == i - 1 ):

        a[i,j] = float ( i * ( n - i ) )

  return a

def eberlein_determinant ( alpha, n ):

#*****************************************************************************80
#
## eberlein_determinant() returns the determinant of the EBERLEIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 0.0

  return determ

def eberlein_null_left ( m, n ):

#*****************************************************************************80
#
## eberlein_null_left() returns a left null vector of the EBERLEIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(M), the left null vector.
#
  import numpy as np

  x = np.ones ( m )

  return x

def eberlein_test ( ):

#*****************************************************************************80
#
## eberlein_test() tests eberlein_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'eberlein_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  eberlein_matrix() computes the EBERLEIN matrix.' )

  m = 4
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  alpha = alpha_lo + ( alpha_hi - alpha_lo ) * np.random.rand ( )

  a = eberlein_matrix ( alpha, n )
  r8mat_print ( m, n, a, '  EBERLEIN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'eberlein_test' )
  print ( '  Normal end of execution.' )
  return

def eulerian_matrix ( m, n ):

#*****************************************************************************80
#
## eulerian_matrix() returns the EULERIAN matrix.
#
#  Definition:
#
#    A run in a permutation is a sequence of consecutive ascending values.
#
#    E(I,J) is the number of permutations of I objects which contain
#    exactly J runs.
#
#  Examples:
#
#     N = 7
#
#     1     0     0     0     0     0     0
#     1     1     0     0     0     0     0
#     1     4     1     0     0     0     0
#     1    11    11     1     0     0     0
#     1    26    66    26     1     0     0
#     1    57   302   302    57     1     0
#     1   120  1191  2416  1191   120     1
#
#  Recursion:
#
#    E(I,J) = J * E(I-1,J) + (I-J+1) * E(I-1,J-1).
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is nonnegative.
#
#    A is unit lower triangular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, 1986.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  a[0,0] = 1.0

  for i in range ( 1, m ):
    a[i,0] = 1.0
    for j in range ( 1, n ):
      a[i,j] = float ( j + 1 ) * a[i-1,j] + float ( i - j + 1 ) * a[i-1,j-1]

  return a

def eulerian_determinant ( n ):

#*****************************************************************************80
#
## eulerian_determinant() returns the determinant of the EULERIAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 1.0

  return determ

def eulerian_inverse ( n ):

#*****************************************************************************80
#
## eulerian_inverse() returns the inverse of the EULERIAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the inverse of the Eulerian matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
#
#  Set up the Eulerian matrix.
#
  b = eulerian_matrix ( n, n )
#
#  Compute the inverse A of a unit lower triangular matrix B.
#
  for j in range ( 0, n ):
    for i in range ( 0, n ):

      if ( i == j ):

        a[i,j] = 1.0

      elif ( j < i ):

        t = 0.0
        for k in range ( j, i ):
          t = t + b[i,k] * a[k,j]
        a[i,j] = - t

  return a

def eulerian_test ( ):

#*****************************************************************************80
#
## eulerian_test() tests eulerian_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'eulerian_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  eulerian_matrix() computes the EULERIAN matrix.' )

  m = 4
  n = m

  a = eulerian_matrix ( m, n )
  r8mat_print ( m, n, a, '  EULERIAN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'eulerian_test' )
  print ( '  Normal end of execution.' )
  return

def exchange_matrix ( m, n ):

#*****************************************************************************80
#
## exchange_matrix() returns the EXCHANGE matrix.
#
#  Formula:
#
#    if ( I + J = N + 1 )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 4, N = 5
#
#    0 0 0 0 1
#    0 0 0 1 0
#    0 0 1 0 0
#    0 1 0 0 0
#
#    M = 5, N = 5
#
#    0 0 0 0 1
#    0 0 0 1 0
#    0 0 1 0 0
#    0 1 0 0 0
#    1 0 0 0 0
#
#  Rectangular properties:
#
#    A is integral: int ( A ) = A.
#
#    A is a zero/one matrix.
#
#  Square Properties:
#
#    A is nonsingular.
#
#    A is a permutation matrix.
#
#    A has property A.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    A is involutional: A * A = I.
#
#    A is a square root of the identity matrix.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    det ( A ) = ( -1 )^(N/2).
#
#    There are N/2 eigenvalues of -1, and (N+1)/2 eigenvalues of 1.
#
#    For each pair of distinct vector indices I1 and I2 that sum to N+1, there
#    is an eigenvector which has a 1 in the I1 and I2 positions and 0 elsewhere,
#    and there is an eigenvector for -1, with a 1 in the I1 position and a -1
#    in the I2 position.  If N is odd, then there is a single eigenvector
#    associated with the index I1 = (N+1)/2, having a 1 in that index and zero
#    elsewhere, associated with the eigenvalue 1.
#
#    The exchange matrix is also called the "counter-identity matrix".
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns 
#    of the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i + j == n - 1 ):
        a[i,j] = 1.0

  return a

def exchange_condition ( n ):

#*****************************************************************************80
#
## exchange_condition() returns the L1 condition of the EXCHANGE matrix.
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
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = 1
  b_norm = 1
  value = a_norm * b_norm

  return value

def exchange_determinant ( n ):

#*****************************************************************************80
#
## exchange_determinant() returns the determinant of the EXCHANGE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  n2 = ( n // 2 )

  if ( ( n2 % 2 ) == 0 ):
    value = 1.0
  else:
    value = -1.0

  return value

def exchange_eigen_right ( n ):

#*****************************************************************************80
#
## exchange_eigen_right() returns the right eigenvectors of the EXCHANGE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real X(N,N), the eigenvector matrix.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )

  n2 = ( n // 2 )

  for j in range ( 0, n2 ):

    i = n - 1 - j

    x[j,j] =  1.0
    x[i,j] = -1.0

    x[j,i] =  1.0
    x[i,i] =  1.0

  if ( ( n % 2 ) == 1 ):
    x[n2,n2] = 1.0

  return x

def exchange_eigenvalues ( n ):

#*****************************************************************************80
#
## exchange_eigenvalues() returns the eigenvalues of the exchange matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  n2 = ( n // 2 )

  for i in range ( 0, n2 ):
    lam[i] = -1.0
  for i in range ( n2, n ):
    lam[i] = +1.0

  return lam

def exchange_inverse ( n ):

#*****************************************************************************80
#
## exchange_inverse() returns the inverse of the exchange matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  a = exchange_matrix ( n, n )

  return a

def fibonacci1_matrix ( n, f1, f2 ):

#*****************************************************************************80
#
## fibonacci1_matrix() returns the FIBONACCI1 matrix.
#
#  Example:
#
#    N = 5
#    F1 = 1, F2 = 2
#
#    1  2  3  5  8
#    2  3  5  8 13
#    3  5  8 13 21
#    5  8 13 21 34
#    8 13 21 34 55
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    If F1 and F2 are integral, then so is A.
#
#    If A is integral, then det ( A ) is integral, and
#    det ( A ) * inverse ( A ) is integral.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    If B is the Fibonacci iteration matrix:
#
#      B * A(F1,F2) = A(F2,F2+F1) = A(F2,F3)
#
#    and in general,
#
#      B^N * A(F1,F2) = A(F(N+1),F(N+2))
#
#    For 2 < N, the matrix is singular, because row 3 is the sum
#    of row 1 and row 2.
#
#    For 2 <= N,
#      rank ( A ) = 2
#
#    If N = 1, then
#      det ( A ) = 1
#    else if N = 2 then
#      det ( A ) = -1
#    else if 1 < N then
#      det ( A ) = 0
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real F1, F2, the first two elements of the sequence
#    that will generate the Fibonacci sequence.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  a[0,0] = f1

  if ( 1 < n ):

    a[1,0] = f2
    a[0,1] = f2

    fnm2 = f1
    fnm1 = f2
    fn   = fnm1 + fnm2

    for k in range ( 2, n + n - 1 ):

      i = min ( k,     n - 1 )
      j = max ( 0, k - n + 1 )

      while ( 0 <= i and j < n ):
        a[i,j] = fn
        i = i - 1
        j = j + 1

      fnm2 = fnm1
      fnm1 = fn
      fn   = fnm1 + fnm2

  return a

def fibonacci1_determinant ( n, f1, f2 ):

#*****************************************************************************80
#
## fibonacci1_determinant() returns the determinant of the FIBONACCI1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real F1, F2, the first two elements of the sequence
#    that will generate the Fibonacci sequence.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( n == 1 ):
    determ = 1.0
  elif ( n == 2 ):
    determ = -1.0
  else:
    determ = 0.0

  return determ

def fibonacci1_null_left ( m, n, f1, f2 ):

#*****************************************************************************80
#
## fibonacci1_null_left() returns a left null vector of the FIBONACCI1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real F1, F2, the first two elements of the sequence
#    that will generate the Fibonacci sequence.
#
#  Output:
#
#    real X(M), a null vector.
#
  import numpy as np

  if ( m < 3 ):
    print ( '' )
    print ( 'fibonacci1_null_left - Fatal error!' )
    print ( '  3 <= M is required.' )
    raise Exception ( 'fibonacci1_null_left - Fatal error!' )

  x = np.zeros ( m )

  x[m-3] = -1.0
  x[m-2] = -1.0
  x[m-1] = +1.0 

  return x

def fibonacci1_null_right ( m, n, f1, f2 ):

#*****************************************************************************80
#
## fibonacci1_null_right() returns a right null vector of the FIBONACCI1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real F1, F2, the first two elements of the sequence
#    that will generate the Fibonacci sequence.
#
#  Output:
#
#    real X(N), a null vector.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'fibonacci1_null_right - Fatal error!' )
    print ( '  3 <= N is required.' )
    raise Exception ( 'fibonacci1_null_right - Fatal error!' )

  x = np.zeros ( n )

  x[n-3] = -1.0
  x[n-2] = -1.0
  x[n-1] = +1.0 

  return x

def fibonacci2_lu ( n ):

#*****************************************************************************80
#
## fibonacci2_lu() returns the LU factors of the Fibonacci2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real L(N,N), U(N,N), the LU factors.
#
  import numpy as np

  L = np.zeros ( ( n, n ) )
  L[0,1] = 1.0
  L[1,0] = 1.0
  for i in range ( 2, n ):
    L[i,i-1] = 1.0
    L[i,i] = 1.0

  U = np.eye ( n )
  U[0,1] = 1.0

  return L, U

def fibonacci2_matrix ( n ):

#*****************************************************************************80
#
## fibonacci2_matrix() returns the FIBONACCI2 matrix.
#
#  Example:
#
#    N = 5
#
#    0 1 0 0 0
#    1 1 0 0 0
#    0 1 1 0 0
#    0 0 1 1 0
#    0 0 0 1 1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is integral: int ( A ) = A.
#
#    A is a zero/one matrix.
#
#    If N = 1 then
#      det ( A ) = 0
#    else
#      det ( A ) = (-1)^(N-1)
#
#    If 1 < N, then A is unimodular.
#
#    For 2 <= N, A has the eigenvalues:
#
#      PHI   (once),
#      1     (N-2) times,
#      1-PHI (once).
#
#    When applied to a Fibonacci1 matrix B, the Fibonacci2 matrix
#    A produces the "next" Fibonacci1 matrix C = A*B.
#
#    Let PHI be the golden ratio (1+sqrt(5))/2.
#
#    For 2 <= N, the eigenvalues and eigenvectors are:
#
#    LAMBDA(1)     = PHI,     vector = (1,PHI,PHI^2,...PHI^(N-1));
#    LAMBDA(2:N-1) = 1        vector = (0,0,0,...,0,1);
#    LAMBDA(N)     = 1 - PHI. vector = (1,1-PHI,(1-PHI)^2,...(1-PHI)^(N-1))
#
#    Note that there is only one eigenvector corresponding to 1.
#    Hence, for 3 < N, the matrix is defective.  This fact means, 
#    for instance, that the convergence of the eigenvector in the power 
#    method will be very slow.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):

        if ( j == 1 ):
          a[i,j] = 1.0

      else:

        if ( j == i - 1 or j == i ):
          a[i,j] = 1.0

  return a

def fibonacci2_condition ( n ):

#*****************************************************************************80
#
## fibonacci2_condition() returns the L1 condition of the FIBONACCI2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  if ( n == 1 ):
    print ( '' )
    print ( 'fibonacci2_condition - Fatal error!' )
    print ( '  The condition number is infinite for N=1' )
    raise Exception ( 'fibonacci2_condition - Fatal error!' )

  if ( n == 1 ):
    a_norm = 0.0
  elif ( n == 2 ):
    a_norm = 2.0
  else:
    a_norm = 3.0
  b_norm = float ( n )
  value = a_norm * b_norm

  return value

def fibonacci2_determinant ( n ):

#*****************************************************************************80
#
## fibonacci2_determinant() returns the determinant of the FIBONACCI2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( n == 1 ):
    determ = 0.0
  else:
    determ = -1.0

  return determ

def fibonacci2_eigen_right ( n ):

#*****************************************************************************80
#
## fibonacci2_eigen_right(): right eigenvectors of the FIBONACCI2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real X(N,N), the eigenvector matrix.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )

  phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0
#
#  Column 0
#
  j = 0
  p = 1.0
  for i in range ( 0, n ):
    x[i,j] = p
    p = p * phi
#
#  Columns 1 through N-2
#
  for j in range ( 1, n - 1 ):
    x[n-1,j] = 1.0
#
#  Column N-1
#
  j = n - 1
  p = 1.0
  for i in range ( 0, n ):
    x[i,j] = p
    p = p * ( 1.0 - phi )

  return x

def fibonacci2_eigenvalues ( n ):

#*****************************************************************************80
#
## fibonacci2_eigenvalues() returns the eigenvalues of the FIBONACCI2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  if ( 1 < n ):
    phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0
    lam[0] = phi
    for i in range ( 1, n - 1 ):
      lam[i] = 1.0
    lam[n-1] = 1.0 - phi

  return lam

def fibonacci2_inverse ( n ):

#*****************************************************************************80
#
## fibonacci2_inverse() returns the inverse of the FIBONACCI2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  if ( n == 1 ):
    print ( '' )
    print ( 'fibonacci2_inverse - Fatal error!' )
    print ( '  The inverse does not exist for N = 1.' )
    raise Exception ( 'fibonacci2_inverse - Fatal error!' )
#
#  Column 1.
#
  j = 0
  s = -1.0
  for i in range ( 0, n ):
    a[i,j] = s
    s = -s
#
#  Column 2
#
  j = 1
  a[0,j] = 1.0
#
#  Columns 3:N
#
  for j in range ( 2, n ):
    s = 1.0
    for i in range ( j, n ):
      a[i,j] = s
      s = - s

  return a

def fibonacci3_matrix ( n ):

#*****************************************************************************80
#
## fibonacci3_matrix() returns the FIBONACCI3 matrix.
#
#  Example:
#
#    N = 5
#
#    1 -1  0  0  0
#    1  1 -1  0  0
#    0  1  1 -1  0
#    0  0  1  1 -1
#    0  0  0  1  1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is integral: int ( A ) = A.
#
#    The determinant of A is the Fibonacci number F(N+1).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 1, n ):
    a[i,i-1] = 1.0

  for i in range ( 0, n ):
    a[i,i] = 1.0

  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  return a

def fibonacci3_determinant ( n ):

#*****************************************************************************80
#
## fibonacci3_determinant() returns the determinant of the FIBONACCI3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  f1 = 0
  f2 = 0
  f3 = 1

  for i in range ( 0, n ): 
    f1 = f2
    f2 = f3
    f3 = f1 + f2

  value = f3

  return value

def fibonacci3_inverse ( n ):

#*****************************************************************************80
#
## fibonacci3_inverse() returns the inverse of the FIBONACCI3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    CM daFonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the inverse of the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  d = np.zeros ( n )

  d[n-1] = 1.0
  for i in range ( n - 2, -1, -1 ):
    d[i] = 1.0 + 1.0 / d[i+1]

  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):

      p1 = 1.0
      for k in range ( i + 1, n ):
        p1 = p1 * d[k]
      p2 = 1.0
      for k in range ( 0, n - j ):
        p2 = p2 * d[k]
      a[i,j] = r8_mop ( i + j ) * p1 / p2

    for j in range ( i + 1, n ):
      p1 = 1.0
      for k in range ( j + 1, n ):
        p1 = p1 * d[k]
      p2 = 1.0
      for k in range ( 0, n - i ):
        p2 = p2 * d[k]
      a[i,j] = p1 / p2

  return a

def fibonacci3_test ( ):

#*****************************************************************************80
#
## fibonacci3_test() tests fibonacci3_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'fibonacci3_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  fibonacci3_test() computes the FIBONACCI3 matrix.' )

  m = 5
  n = m

  a = fibonacci3_matrix ( n )
  r8mat_print ( m, n, a, '  FIBONACCI3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'fibonacci3_test' )
  print ( '  Normal end of execution.' )
  return

def fiedler_matrix ( m, n, x ):

#*****************************************************************************80
#
## fiedler_matrix() returns the FIEDLER matrix.
#
#  Formula:
#
#    A(I,J) = abs ( X(I) - X(J) )
#
#  Example:
#
#    M = 5, N = 5, X = ( 1, 2, 3, 5, 9 )
#
#    0  1  2  4  8
#    1  0  1  3  7
#    2  1  0  2  6
#    4  3  2  0  4
#    8  7  6  4  0
#
#  Rectangular Properties:
#
#    A has a zero diagonal.
#
#  Square Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    det ( A ) = (-1)^N * 2^(N-2)
#      * ( X(1) - X(N) ) * product ( 2 <= I <= N ) ( X(I) - X(I-1) ).
#
#    A is nonsingular if the X(I) are distinct.
#
#    The inverse is cyclic tridiagonal; that is, it is tridiagonal, except
#    for nonzero (1,N) and (N,1) entries.
#
#    A has a dominant positive eigenvalue, and all others are negative.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gabor Szego,
#    Solution to problem 3705,
#    American Mathematical Monthly,
#    Volume 43, Number 4, 1936, pages 246-259.
#
#    John Todd,
#    Example A14,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Academic Press, 1977, page 159.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#    real X( max (M,N) ), the values that define A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
        a[i,j] = np.abs ( x[i] - x[j] )

  return a

def fiedler_determinant ( n, x ):

#*****************************************************************************80
#
## fiedler_determinant() returns the determinant of the FIEDLER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N), the fiedler elements.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 2.0 ** ( n - 2 )

  if ( ( n % 2 ) == 1 ):
    determ = - determ

  for i in range ( 0, n - 1 ):
    for j in range ( i + 1, n ):
      if ( x[j] < x[i] ):
        t    = x[j]
        x[j] = x[i]
        x[i] = t
        determ = - determ

  determ = determ * ( x[n-1] - x[0] )

  for i in range ( 1, n ):
    determ = determ * ( x[i] - x[i-1] )

  return determ

def fiedler_inverse ( n, x ):

#*****************************************************************************80
#
## fiedler_inverse() returns the inverse of the FIEDLER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N), the values that define A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  d1 = 0.5 / ( x[n-1] - x[0] )
  d2 = 0.5 / ( x[0] - x[1] )

  a[0,n-1] = + d1
  a[0,0] = + d1 + d2
  a[0,1] =      - d2

  for i in range ( 1, n - 1 ):
    d1 = 0.5 / ( x[i-1] - x[i] )
    d2 = 0.5 / ( x[i] - x[i+1] )
    a[i,i-1] = - d1
    a[i,i]   = + d1 + d2
    a[i,i+1] =      - d2

  d1 = 0.5 / ( x[n-2] - x[n-1] )
  d2 = 0.5 / ( x[n-1] - x[0] )

  a[n-1,n-2] = - d1
  a[n-1,n-1] =   d1 + d2
  a[n-1,0]   =      + d2

  return a

def fiedler_test ( ):

#*****************************************************************************80
#
## fiedler_test() tests fiedler_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'fiedler_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  fiedler_matrix() computes the FIEDLER matrix.' )

  m = 5
  n = m
  x_lo = -5.0
  x_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )

  a = fiedler_matrix ( m, n, x )
 
  r8mat_print ( m, n, a, '  FIEDLER matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'fiedler_test' )
  print ( '  Normal end of execution.' )
  return

def forsythe_matrix ( alpha, beta, n ):

#*****************************************************************************80
#
## forsythe_matrix() returns the FORSYTHE matrix.
#
#  Discussion:
#
#    The Forsythe matrix represents a Jordan canonical matrix, perturbed
#    by a rank one update.
#
#  Formula:
#
#    If ( I = J )
#      A(I,J) = BETA
#    else if ( J = I+1 )
#      A(I,J) = 1
#    else if ( I = N and J = 1 ) then
#      A(I,J) = ALPHA
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, BETA = 3, N = 5
#
#    3 1 0 0 0
#    0 3 1 0 0
#    0 0 3 1 0
#    0 0 0 3 1
#    2 0 0 0 3
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The characteristic equation of A is
#
#      ( BETA - LAMBDA )^N - (-1)^N*ALPHA = 0
#
#    The eigenvalues of A are
#
#      LAMBDA(I) = BETA
#        + abs ( ALPHA )^1/N * exp ( 2 * I * PI * sqrt ( - 1 ) / N )
#
#    Gregory and Karney consider the special case where BETA is 0,
#    and ALPHA is a "small" value.  In that case, the characteristic
#    equation is LAMBDA^N - ALPHA = 0, and the eigenvalues are the
#    N-th root of ALPHA times the N roots of unity.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 5.22,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 103, 
#    LC: QA263.G68.
#
#  Input:
#
#    real ALPHA, BETA, define the matrix.  A typical 
#    value of ALPHA is the square root of the machine precision; a typical
#    value of BETA is 0.0.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i ):
        a[i,j] = beta
      elif ( j == i + 1 ):
        a[i,j] = 1.0
      elif ( i == n - 1 and j == 0 ):
        a[i,j] = alpha

  return a

def forsythe_determinant ( alpha, beta, n ):

#*****************************************************************************80
#
## forsythe_determinant() returns the determinant of the FORSYTHE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, BETA, parameters that define the matrix.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = r8_mop ( n - 1 ) * alpha + beta ** n

  return value

def forsythe_inverse ( alpha, beta, n ):

#*****************************************************************************80
#
## forsythe_inverse() returns the inverse of the Forsythe matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969,
#    ISBN: 0882756494,
#    LC: QA263.G68.
#
#  Input:
#
#    real ALPHA, BETA, define the matrix.  
#    The Forsythe matrix does not have an inverse if both ALPHA and BETA
#    are zero.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np
 
  a = np.zeros ( ( n, n ) )

  if ( beta == 0.0 and alpha == 0.0 ):

    print ( '' )
    print ( 'forsythe_inverse - Fatal error!' )
    print ( '  The Forsythe matrix is not invertible if' )
    print ( '  both ALPHA and BETA are 0.' )
    raise Exception ( 'forsythe_inverse - Fatal error!' )

  elif ( beta == 0.0 ):

    for j in range ( 0, n ):
      for i in range ( 0, n ):
 
        if ( j == n - 1 ):
          a[i,j] = 1.0 / alpha
        elif ( j == i - 1 ):
          a[i,j] = 1.0
#
#  Set up the original Jordan matrix as B.
#
  else:
#
#  Compute inverse of unperturbed Jordan matrix.
#
    for j in range ( 0, n ):
      for i in range ( 0, n ):

        if ( i <= j ):
          a[i,j] =  - ( - 1.0 / beta ) ** ( j + 1 - i )
#
#  Add rank one perturbation.
#
    z = - 1.0 / beta

    for j in range ( 0, n ):
      for i in range ( 0, n ):
        a[i,j] = a[i,j] - alpha * z ** ( n + 1 + j - i ) \
                / ( 1.0 - alpha * z ** n )

  return a

def forsythe_test ( ):

#*****************************************************************************80
#
## forsythe_test() tests forsythe_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'forsythe_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  forsythe_matrix() computes the FORSYTHE matrix.' )

  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  beta = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  a = forsythe_matrix ( alpha, beta, n )
  r8mat_print ( n, n, a, '  FORSYTHE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'forsythe_test' )
  print ( '  Normal end of execution.' )
  return

def fourier_cosine_matrix ( n ):

#*****************************************************************************80
#
## fourier_cosine_matrix() returns the discrete Fourier Cosine Transform matrix.
#
#  Example:
#
#    N = 5
#
#    0.447214      0.447214      0.447214      0.447214      0.447214
#    0.601501      0.371748      0.000000     -0.371748     -0.601501
#    0.511667     -0.195440     -0.632456     -0.195439      0.511667
#    0.371748     -0.601501      0.000000      0.601501     -0.371748
#    0.195439     -0.511667      0.632456     -0.511668      0.195439
#
#  Properties:
#
#    A * A' = I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    a[0,j] = 1.0 / np.sqrt ( float ( n ) )

  for i in range ( 1, n ) :
    for j in range ( 0, n ):
      
      angle = float ( i ) * float ( 2 * j + 1 ) * np.pi / float ( 2 * n )
      a[i,j] = np.sqrt ( 2.0 ) * np.cos ( angle ) / np.sqrt ( float ( n ) )

  return a

def fourier_cosine_determinant ( n ):

#*****************************************************************************80
#
## fourier_cosine_determinant() returns the determinant of the fourier_cosine matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    value = + 1.0
  else:
    value = -1.0

  return value

def fourier_cosine_inverse ( n ):

#*****************************************************************************80
#
## fourier_cosine_inverse() returns the inverse of the fourier_cosine matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = fourier_cosine_matrix ( n )

  a = np.transpose ( a )

  return a

def fourier_cosine_test ( ):

#*****************************************************************************80
#
## fourier_cosine_test() tests fourier_cosine_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'fourier_cosine_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  fourier_cosine_matrix() computes the fourier_cosine matrix.' )

  m = 5
  n = m

  a = fourier_cosine_matrix ( n )
  r8mat_print ( m, n, a, '  fourier_cosine matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'fourier_cosine_test' )
  print ( '  Normal end of execution.' )
  return

def fourier_sine_matrix ( n ):

#*****************************************************************************80
#
## fourier_sine_matrix() returns the fourier_sine matrix.
#
#  Discussion:
#
#    This is the discrete Fourier Sine Transform matrix.
#
#    This matrix is occasionally known as the "Newman" matrix.
#
#  Formula:
#
#    A(I,J) = sqrt ( 2 / (N+1) ) * SIN ( I * J * PI / (N+1) )
#
#  Example:
#
#    N = 5
#
#     0.288675     0.5    0.577350    0.5    0.288675
#     0.5          0.5    0.0        -0.5   -0.5
#     0.577350     0.0   -0.577350    0.0    0.577350
#     0.5         -0.5    0.0         0.5   -0.5
#     0.288675    -0.5    0.577350   -0.5    0.288675
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    A is involutional: A * A = I.
#
#    A is generally not positive definite.
#
#    All eigenvalues of A have absolute value 1.
#
#    A is the eigenvector matrix of the second difference matrix (-1,2,-1).
#
#    A can be used to compute the Discrete Fourier Sine Transform of
#    a set of data X,
#       DFST ( X ) = A * X
#    A second multiplication by A recovers the original data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.11,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 41, 
#    LC: QA263.G68.
#
#    Nicholas Higham, Desmond Higham,
#    Large growth factors in Gaussian elimination with pivoting,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, 1989, pages 155-164.
#
#    Joan Westlake,
#    Test Matrix A7,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  s = np.sqrt ( 2.0 / float ( n + 1 ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( ( i + 1 ) * ( j + 1 ) ) * np.pi / float ( n + 1 )
      a[i,j] = np.sin ( angle ) * s

  return a

def fourier_sine_determinant ( n ):

#*****************************************************************************80
#
## fourier_sine_determinant() returns the determinant of the fourier_sine matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    value = + 1.0
  else:
    value = -1.0

  return value

def fourier_sine_inverse ( n ):

#*****************************************************************************80
#
## fourier_sine_inverse() returns the inverse of the fourier_sine matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  a = fourier_sine_matrix ( n )

  return a

def fourier_sine_test ( ):

#*****************************************************************************80
#
## fourier_sine_test() tests fourier_sine_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'fourier_sine_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  fourier_sine_matrix() computes the fourier_sine matrix.' )

  m = 5
  n = m

  a = fourier_sine_matrix ( n )
  r8mat_print ( m, n, a, '  fourier_sine matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'fourier_sine_test' )
  print ( '  Normal end of execution.' )
  return

def frank_matrix ( n ):

#*****************************************************************************80
#
## frank_matrix() returns the FRANK matrix.
#
#  Formula:
#
#    if ( I <= J )
#      A(I,J) = N+1-J
#    elseif ( J = I-1 )
#      A(I,J) = N-J
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    N = 5
#
#    5 4 3 2 1
#    4 4 3 2 1
#    . 3 3 2 1
#    . . 2 2 1
#    . . . 1 1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is upper Hessenberg.
#
#    A is integral: int ( A ) = A.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    The eigenvalues of A are related to the zeros of the Hermite
#    polynomials.
#
#    The eigenvalues of A are real and positive, and occur in reciprocal
#    pairs, LAMBDA and 1/LAMBDA.
#
#    For N = 12, the eigenvalues of A range from 32.2 to 0.031, with
#    the smaller eigenvalues having a condition number of 10^7,
#    meaning that a change in the matrix of order 10^(-7) can
#    result in a change in the eigenvalue of order 1.  The actual
#    eigenvalues are:
#
#      0.031028060644010
#      0.049507429185278
#      0.081227659240405
#      0.143646519769220
#      0.284749720558478
#      0.6435053190048555
#      1.55398870913210790
#      3.511855948580757194
#      6.961533085567122113
#     12.311077408868526120
#     20.198988645877079428
#     32.228891501572160750
#
#    If N is odd, 1 is an eigenvalue of A.
#
#    The (N/2) smaller eigenvalues of A are ill-conditioned.
#
#    For large N, the computation of the determinant of A
#    comes out very far from its correct value of 1.
#
#    Simple linear systems:
#      x = (0,0,0,...,1),   A*x = (1,1,1,...,1)
#      x = (1,1,1,...,1),   A*x = n * ( (n+1)/2, (n+3)/2, (n+3)/2, ..., (n+3)/2)
#
#    The condition number grows slightly faster than n!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Patricia Eberlein,
#    A note on the matrices denoted by $B n$,
#    SIAM Journal on Applied Mathematics,
#    Volume 20, 1971, pages 87-92.
#
#    Werner Frank,
#    Computing eigenvalues of complex matrices by determinant
#    evaluation, and by methods of Danilewski and Wielandt,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, 1958, pages 378-392.
#
#    Gene Golub, James Wilkinson,
#    Ill-conditioned eigensystems and the computation of the Jordan
#    canonical form,
#    SIAM Review,
#    Volume 18, Number 4, 1976, pages 578-619.
#
#    Robert Gregory, David Karney,
#    Example 5.14,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 92,
#    LC: QA263.G68.
#
#    H Rutishauser,
#    On test matrices,
#    Programmation en Mathematiques
#    Numeriques, Editions Centre Nat. Recherche Sci., Paris, 165,
#    1966, pages 349-365.  Section 9.
#
#    J M Varah,
#    A generalization of the Frank matrix,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 7, Number 3, August 1986, pages 835-839.
#
#    Joan Westlake,
#    Test Matrix A37,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#    James Wilkinson,
#    Error analysis of floating-point computation,
#    Numerische Mathematik,
#    Volume 2, 1960, pages 319-340.
#
#    James Wilkinson,
#    The Algebraic Eigenvalue Problem,
#    Oxford University Press, 1965, pages 92-93.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i <= j ):
        a[i,j] = float ( n - j )
      elif ( j == i - 1 ):
        a[i,j] = float ( n - j - 1 )

  return a

def frank_determinant ( n ):

#*****************************************************************************80
#
## frank_determinant() returns the determinant of the FRANK matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = 1.0
 
  return determ

def frank_inverse ( n ):

#*****************************************************************************80
#
## frank_inverse() returns the inverse of the FRANK matrix.
#
#  Formula:
#
#    if ( I = J-1 )
#      A(I,J) = -1
#    elseif ( I = J )
#      if ( I = 1 )
#        A(I,J) = 1
#      else
#        A(I,J) = N + 2 - I
#    elseif ( J < I )
#      A(I,J) = - (N+1-I) * A(I-1,J)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#     1  -1  0  0  0
#    -4   5 -1  0  0
#    12 -15  4 -1  0
#   -24  30 -8  3 -1
#    24 -30  8 -3  2
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is lower Hessenberg.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    A is integral: int ( A ) = A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j - 1 ):
        a[i,j] = - 1.0
      elif ( i == j ):
        if ( i == 0 ):
          a[i,j] = 1.0
        else:
          a[i,j] = float ( n + 1 - i )
      elif ( j < i ):
        a[i,j] = - float ( n - i ) * a[i-1,j]

  return a

def frank_rhs ( m, k ):

#*****************************************************************************80
#
## frank_rhs() returns the FRANK right hand side.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the row dimension.
#
#    integer K, the column dimension ( should be 2).
#
#  Output:
#
#    real B(M,K), the right hand side matrix.
#
  import numpy as np

  b = np.zeros ( ( m, k ) )

  if ( 1 <= k ):
    for i in range ( 0, m ):
      b[i,0] = 1.0

    if ( 2 <= k ):
      b[0,1] = float ( ( m * ( m + 1 ) ) // 2 )
      for i in range ( 1, m ):
        b[i,1] = float ( ( ( m - i ) * ( m + 3 - i ) ) // 2 )

  return b

def frank_solution ( n, k ):

#*****************************************************************************80
#
## frank_solution() returns the FRANK solution matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 November 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the row dimension.
#
#    integer K, the column dimension ( should be 2).
#
#  Output:
#
#    real X(N,K), the solution matrix.
#
  import numpy as np

  x = np.zeros ( ( n, k ) )

  if ( 1 <= k ):
    x[n-1,0] = 1.0

    if ( 2 <= k ):
      for i in range ( 0, n ):
        x[i,1] = 1.0

  return x

def frank_test ( ):

#*****************************************************************************80
#
## frank_test() tests frank_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'frank_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  frank_matrix() computes the FRANK matrix.' )

  m = 5
  n = m
  a = frank_matrix ( n )
  r8mat_print ( m, n, a, '  FRANK matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'frank_test' )
  print ( '  Normal end of execution.' )
  return

def gfpp_matrix ( n, alpha ):

#*****************************************************************************80
#
## gfpp_matrix() returns the GFPP matrix.
#
#  Discussion:
#
#    The GFPP matrix has maximal growth factor for Gauss elimination.
#
#  Formula:
#
#    if ( I = J or J = N )
#      A(I,J) = 1.0
#    elseif ( J < I )
#      A(I,J) = - abs ( ALPHA )
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5, ALPHA = 1
#
#    A =
#
#    1     0     0     0     1
#   -1     1     0     0     1
#   -1    -1     1     0     1
#   -1    -1    -1     1     1
#   -1    -1    -1    -1     1
#
#    P = Identity
#
#    L =
#
#    1     0     0     0     0
#   -1     1     0     0     0
#   -1    -1     1     0     0
#   -1    -1    -1     1     0
#   -1    -1    -1    -1     1
#
#    U =
#
#    1     0     0     0     1
#    0     1     0     0     2
#    0     0     1     0     4
#    0     0     0     1     8
#    0     0     0     0    16
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    If ALPHA is between 0 and 1, then Gaussian elimination with partial
#    pivoting yields a controllable growth factor of (1+ALPHA)^(N-1).
#    and a P factor which is the identity, an L factor equal to the lower
#    triangle of A, and an U factor which is equal to the identity matrix,
#    except that the last column is
#
#      [ 1, ALPHA+1, (ALPHA+1)^2, ...(ALPHA+1)^N-1 ].
#
#    If ALPHA is not between 0 and 1, then Gauss elimination WITHOUT
#    pivoting will yield the same pivot growth factor and PLU factorization
#    just described, but Gauss elimination with partial pivoting will not.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham, Desmond Higham,
#    Large growth factors in Gaussian elimination with pivoting,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, 1989, pages 155-164.
#
#    Lloyd Trefethen, David Bau,
#    Numerical Linear Algebra,
#    SIAM, 1997, pages 165-166.
#
#  Input:
#
#    integer N, the order of A.
#
#    real ALPHA, determines subdiagonal elements.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j or j == n - 1 ):
        a[i,j] = 1.0
      elif ( j < i ):
        a[i,j] = - abs ( alpha )

  return a

def gfpp_condition ( n, alpha ):

#*****************************************************************************80
#
## gfpp_condition() returns the L1 condition of the GFPP matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, determines subdiagonal elements.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = 1.0 + float ( n - 1 ) * abs ( alpha )
  b_norm = 1.0
  value = a_norm * b_norm

  return value

def gfpp_determinant ( n, alpha ):

#*****************************************************************************80
#
## gfpp_determinant() returns the determinant of the GFPP matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, determines subdiagonal elements.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = ( 1.0 + abs ( alpha ) ) ** ( n - 1 )

  return value

def gfpp_inverse ( n, alpha ):

#*****************************************************************************80
#
## gfpp_inverse() returns the inverse of the GFPP matrix.
#
#  Example:
#
#    N = 5, ALPHA = 1
#
#    0.5000   -0.2500   -0.1250   -0.0625   -0.0625
#         0    0.5000   -0.2500   -0.1250   -0.1250
#         0         0    0.5000   -0.2500   -0.2500
#         0         0         0    0.5000   -0.5000
#    0.5000    0.2500    0.1250    0.0625    0.0625
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, determines subdiagonal elements.
#
#  Output:
#
#    real A(N,N), the inverse matrix.
#
  import numpy as np

  p, l, u = gfpp_plu ( n, alpha )
  
  p_inverse = np.transpose ( p )

  l_inverse = tri_l1_inverse ( n, l )

  u_inverse = tri_u_inverse ( n, u )

  lp_inverse = r8mat_mm ( n, n, n, l_inverse, p_inverse )

  a = r8mat_mm ( n, n, n, u_inverse, lp_inverse )
  
  return a

def gfpp_lu ( n, alpha ):

#*****************************************************************************80
#
## gfpp_lu() returns the LU factorization of the GFPP matrix.
#
#  Discussion
#
#    This factorization assumes that Gaussian elimination is performed
#    without pivoting.  If ALPHA is not between 0 and 1, then the
#    PLU factors returned here will not be the PLU factors derived from
#    Gaussian elimination with pivoting.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, determines subdiagonal elements.
#
#  Output:
#
#    real L(N,N), U(N,N), the factors.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      l[i,j] = - abs ( alpha )
    l[i,i] = 1.0

  u = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    u[i,i] = 1.0
  
  s = 1.0
  u[0,n-1] = s
  for i in range ( 1, n ):
    u[i,n-1] = 1.0 + abs ( alpha ) * s
    s = s + u[i,n-1]

  return l, u

def gfpp_plu ( n, alpha ):

#*****************************************************************************80
#
## gfpp_plu() returns the PLU factorization of the GFPP matrix.
#
#  Discussion
#
#    This factorization assumes that Gaussian elimination is performed
#    without pivoting.  If ALPHA is not between 0 and 1, then the
#    PLU factors returned here will not be the PLU factors derived from
#    Gaussian elimination with pivoting.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, determines subdiagonal elements.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the P, L, U factors
#    of the matrix.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    p[i,i] = 1.0

  l = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      l[i,j] = - abs ( alpha )
    l[i,i] = 1.0

  u = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    u[i,i] = 1.0
  
  s = 1.0
  u[0,n-1] = s
  for i in range ( 1, n ):
    u[i,n-1] = 1.0 + abs ( alpha ) * s
    s = s + u[i,n-1]

  return p, l, u

def gfpp_test ( ):

#*****************************************************************************80
#
## gfpp_test() tests gfpp_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gfpp_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gfpp_matrix() computes the GFPP matrix.' )

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )

  a = gfpp_matrix ( n, alpha )
  r8mat_print ( m, n, a, '  GFPP matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'gfpp_test' )
  print ( '  Normal end of execution.' )
  return

def givens_matrix ( m, n ):

#*****************************************************************************80
#
## givens_matrix() returns the GIVENS matrix.
#
#  Discussion:
#
#    Note that this is NOT the "Givens rotation matrix".  This
#    seems to be more commonly known as the Moler matrix%
#
#  Formula:
#
#    A(I,J) = 2 * min ( I, J ) - 1
#
#  Example:
#
#    N = 5
#
#    1 1 1 1 1
#    1 3 3 3 3
#    1 3 5 5 5
#    1 3 5 7 7
#    1 3 5 7 9
#
#  Rectangular Properties:
#
#    A is integral: int ( A ) = A.
#
#  Square Properties:
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The inverse of A is tridiagonal.
#
#    A has a simple Cholesky factorization.
#
#    A has eigenvalues
#
#      LAMBDA(I) = 0.5 * sec ( ( 2 * I - 1 ) * PI / ( 4 * N ) )^2
#
#    The condition number P(A) is approximately 16 N^2 / PI^2.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Morris Newman, John Todd,
#    Example A9,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    John Todd,
#    Example A9,
#    Basic Numerical Mathematics, Volume 2: Numerical Algebra,
#    Academic Press, New York, 1977, page 1.
#
#    Joan Westlake,
#    Test Matrix A8,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = float ( 2 * min ( i, j ) + 1 )

  return a

def givens_condition ( n ):

#*****************************************************************************80
#
## givens_condition() returns the L1 condition of the GIVENS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  import numpy as np

  a_norm = float ( n * n )

  if ( n == 1 ):
    b_norm = 1.0
  else:
    b_norm = 2.0

  value = a_norm * b_norm

  return value

def givens_determinant ( n ):

#*****************************************************************************80
#
## givens_determinant() returns the determinant of the GIVENS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  value = 1.0

  for i in range ( 1, n + 1 ):
    angle = float ( 2 * i - 1 ) * np.pi / float ( 4 * n )
    value = value * 0.5 / ( np.cos ( angle ) ) ** 2

  return value

def givens_eigenvalues ( n ):

#*****************************************************************************80
#
## givens_eigenvalues() returns the eigenvalues of the GIVENS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real LAMBDA(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( 2 * i + 1 ) * np.pi / float ( 4 * n )
    lam[i] = 0.5 / ( np.cos ( angle ) ) ** 2

  return lam

def givens_inverse ( n ):

#*****************************************************************************80
#
## givens_inverse() returns the inverse of the GIVENS matrix.
#
#  Formula:
#
#    if ( I = J = 1 )
#      A(I,J) = 1.5
#    elseif ( I = J < N )
#      A(I,J) = 1.0
#    elseif ( I = J = N )
#      A(I,J) = 0.5
#    elseif ( J = I+1 or J = I-1 )
#      A(I,J) = -0.5
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#           3 -1  0  0  0
#          -1  2 -1  0  0
#    1/2 *  0 -1  2 -1  0
#           0  0 -1  2 -1
#           0  0  0 -1  1
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        if ( i == 0 ):
          a[i,j] = 1.5
        elif ( i < n - 1 ):
          a[i,j] = 1.0
        else:
          a[i,j] = 0.5
      elif ( i == j + 1 ):
        a[i,j] = - 0.5
      elif ( i == j - 1 ):
        a[i,j] = - 0.5

  return a

def givens_llt ( n ):

#*****************************************************************************80
#
## givens_llt() returns the Cholesky factor of the GIVENS matrix.
#
#  Example:
#
#    N = 5
#
#    1    0        0        0       0
#    1  sqrt(2)    0        0       0
#    1  sqrt(2)  sqrt(2)    0       0
#    1  sqrt(2)  sqrt(2)  sqrt(2)   0
#    1  sqrt(2)  sqrt(2)  sqrt(2) sqrt(2)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  j = 0
  for i in range ( 0, n ):
    a[i,j] = 1.0

  for j in range ( 1, n ):
    for i in range ( j, n ):
      a[i,j] = np.sqrt ( 2.0 )

  return a

def givens_lu ( n ):

#*****************************************************************************80
#
## givens_lu() returns the LU factors of the GIVENS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( j, n ):
      l[i,j] = 1.0

  u = np.zeros ( ( n, n ) )

  i = 0
  for j in range ( 0, n ):
    u[i,j] = 1.0

  for i in range ( 1, n ):
    for j in range ( i, n ):
      u[i,j] = 2.0

  return l, u

def givens_plu ( n ):

#*****************************************************************************80
#
## givens_plu() returns the PLU factors of the GIVENS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( j, n ):
      l[i,j] = 1.0

  u = np.zeros ( ( n, n ) )

  i = 0
  for j in range ( 0, n ):
    u[i,j] = 1.0

  for i in range ( 1, n ):
    for j in range ( i, n ):
      u[i,j] = 2.0

  return p, l, u

def givens_test ( ):

#*****************************************************************************80
#
## givens_test() tests givens_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'givens_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  givens_matrix() computes the GIVENS matrix.' )

  m = 5
  n = m

  a = givens_matrix ( m, n )
 
  r8mat_print ( m, n, a, '  GIVENS matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'givens_test' )
  print ( '  Normal end of execution.' )
  return

def gk316_matrix ( n ):

#*****************************************************************************80
#
## gk316_matrix() returns the GK316 matrix.
#
#  Discussion:
#
#    GK316 is a Gregory and Karney test matrix.
#
#  Formula:
#
#    if ( I == N )
#      A(I,J) = J
#    elseif ( J == N )
#      A(I,J) = I
#    elseif ( I == J )
#      A(I,J) = 1.0
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    N = 5
#
#     1  0  0  0  1
#     0  1  0  0  2
#     0  0  1  0  3
#     0  0  0  1  4
#     1  2  3  4  5
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A has property A (the first set is 1:N-1, the second is just N).
#
#    A is integral: int ( A ) = A.
#
#    det ( A ) = - N * ( N + 1 ) * ( 2 * N - 5 ) / 6.
#
#    N-2 eigenvalues are equal to 1, while the remaining eigenvalues
#    are the roots of X^2 - (N+1)*X - N*(N+1)*(2*N-5)/6 = 0.
#
#    A is border-banded.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Aegerter,
#    Construction of a Set of Test Matrices,
#    Communications of the ACM,
#    Volume 2, Number 8, 1959, pages 10-12.
#
#    Robert Gregory, David Karney,
#    Example 3.16, Example 4.15,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 44, page 74,
#    LC: QA263.G68.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == n - 1 ):
        a[i,j] = float ( j + 1 )
      elif ( j == n - 1 ):
        a[i,j] = float ( i + 1 )
      elif ( i == j ):
        a[i,j] = 1.0

  return a

def gk316_determinant ( n ):

#*****************************************************************************80
#
## gk316_determinant() returns the determinant of the GK316 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = - float ( n * ( n + 1 ) * ( 2 * n - 5 ) ) / 6.0

  return value

def gk316_inverse ( n ):

#*****************************************************************************80
#
## gk316_inverse() returns the inverse of the GK316 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  t = 6.0 / float ( n * ( n + 1 ) * ( 2 * n - 5 ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
 
      if ( i == j and i < n - 1 ):
        a[i,j] = 1.0 - t * float ( ( i + 1 ) * ( i + 1 ) )
      elif ( i == j and i == n - 1 ):
        a[i,j] = - t
      elif ( i < n - 1 and j < n - 1 ):
        a[i,j] = - t * float ( ( i + 1 ) * ( j + 1 ) )
      elif ( i == n - 1 ):
        a[i,j] = t * float ( j + 1 )
      elif ( j == n - 1 ):
        a[i,j] = t * float ( i + 1 )

  return a

def gk316_test ( ):

#*****************************************************************************80
#
## gk316_test() tests gk316_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'gk316_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gk316_matrix() computes the GK316 matrix.' )

  m = 5
  n = m

  a = gk316_matrix ( n )
 
  r8mat_print ( m, n, a, '  GK316 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'gk316_test' )
  print ( '  Normal end of execution.' )
  return

def gk323_matrix ( m, n ):

#*****************************************************************************80
#
## gk323_matrix() returns the GK323 matrix, a Gregory and Karney test matrix.
#
#  Discussion:
#
#    This matrix is occasionally known as the "Todd" matrix.
#
#  Formula:
#
#    A(I,J) = abs ( I - J )
#
#  Example:
#
#    N = 5
#
#     0  1  2  3  4
#     1  0  1  2  3
#     2  1  0  1  2
#     3  2  1  0  1
#     4  3  2  1  0
#
#  Rectangular Properties:
#
#    A is integral: int ( A ) = A.
#
#    A is a special case of the Fiedler matrix.
#
#  Square Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    det ( A ) = (-1)^(N-1) * 2^(N-2) * ( N - 1 ).
#
#    A has a dominant positive eigenvalue, and N-1 real negative eigenvalues.
#
#    If N = 2 mod 4, then -1 is an eigenvalue, with an eigenvector
#    of the form ( 1, -1, -1, 1, 1, -1, -1, 1, ... ).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   08 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.23,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 51, 
#    LC: QA263.G68.
#
#  Input:
#
#    integer M, N, the number of rows and columns 
#    of the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i  in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = float ( abs ( i - j ) )

  return a

def gk323_determinant ( n ):

#*****************************************************************************80
#
## gk323_determinant() returns the determinant of the GK323 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = r8_mop ( n - 1 ) * 2.0 ** ( n - 2 ) * float ( n - 1 )

  return value

def gk323_inverse ( n ):

#*****************************************************************************80
#
## gk323_inverse() returns the inverse of the GK323 matrix.
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        if ( i == 0 or i == n - 1 ):
          a[i,j] = - 0.5 * float ( n - 2 ) / float ( n - 1 )
        else:
          a[i,j] = - 1.0
      elif ( i == j + 1 or i == j - 1 ):
        a[i,j] = 0.5
      elif ( i == 0 and j == n - 1 ):
        a[i,j] = 0.5 / float ( n - 1 )
      elif ( i == n - 1 and j == 0 ):
        a[i,j] = 0.5 / float ( n - 1 )

  return a

def gk323_test ( ):

#*****************************************************************************80
#
## gk323_test() tests gk323_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gk323_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gk323_matrix() computes the GK323 matrix.' )

  m = 5
  n = m

  a = gk323_matrix ( m, n )
 
  r8mat_print ( m, n, a, '  GK323 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'gk323_test' )
  print ( '  Normal end of execution.' )
  return

def gk324_matrix ( m, n, x ):

#*****************************************************************************80
#
## gk324_matrix() returns the GK324 matrix.
#
#  Discussion:
#
#    This is Gregory and Karney example matrix 3.24.
#
#  Example:
#
#    M = N = 5
#
#    X = ( 11, 12, 13, 14 )
#
#     1  1  1  1  1
#    11  1  1  1  1
#    11 12  1  1  1
#    11 12 13  1  1
#    11 12 13 14  1
#
#  Properties:
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   09 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 51, 
#    LC: QA263.G68.
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    
#    * real X(N-1), the first N-1 entries of the
#      last row, if M <= N, 
#    or 
#    * real X(N), the N entries of the last row,
#      if N < M.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = 1.0
      else:
        a[i,j] = x[j]

  return a

def gk324_determinant ( n, x ):

#*****************************************************************************80
#
## gk324_determinant() returns the determinant of the GK324 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N-1), the first N-1 entries of the last row.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  for i in range ( 0, n - 1 ):
    value = value * ( 1.0 - x[i] )

  return value

def gk324_inverse ( n, x ):

#*****************************************************************************80
#
## gk324_inverse() returns the inverse of the GK324 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 51, 
#    LC: QA263.G68.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N-1), the first N-1 entries of the last row.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i < n - 1 ):

        if ( j == i ):
          a[i,j] = 1.0 / ( 1.0 - x[i] )
        elif ( j == i + 1 ):
          a[i,j] = - 1.0 / ( 1.0 - x[i] )

      elif ( i == n - 1 ):

        if ( j == 0 ):

          a[i,j] = - x[0] / ( 1.0 - x[0] )

        elif ( j < n - 1 ):

          a[i,j] = ( x[j-1] - x[j] ) / ( 1.0 - x[j] ) / ( 1.0 - x[j-1] )

        elif ( j == n - 1 ):

          a[i,j] = 1.0 / ( 1.0 - x[n-2] )

  return a

def gk324_test ( ):

#*****************************************************************************80
#
## gk324_test() tests gk324_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gk324_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gk324_matrix() computes the GK324 matrix.' )

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  if ( n < m ):
    x_n = n
  else:
    x_n = n - 1

  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( x_n )

  a = gk324_matrix ( m, n, x )
 
  r8mat_print ( m, n, a, '  GK324 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'gk324_test' )
  print ( '  Normal end of execution.' )
  return

def golub_determinant ( n, key ):

#*****************************************************************************80
#
## golub_determinant() returns the determinant of the golub matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a seed for the random number generator.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def golub_inverse ( n, key ):

#*****************************************************************************80
#
## golub_inverse() returns the inverse of a golub matrix.
#
#  Discussion:
#
#    These matrices are the product of random unit lower and unit upper 
#    triangular matrices.
#
#    These matrices tend to be badly conditioned.
#
#  Properties:
#
#    A can be LU factored without pivoting.
#
#    det(A) = 1.
#
#    For values of n greater than 10, the determinant cannot may not be 
#    reliably computed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer KEY, a seed for the random number generator.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  np.random.seed ( key )
 
  s = 10.0

  L = identity_matrix ( n, n )
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      v = np.random.normal ( 0.0, 1.0 )
      L[i,j] = s * v

  Linv = r8mat_l1_inverse ( L )

  U = identity_matrix ( n, n )
  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      v = np.random.normal ( 0.0, 1.0 )
      U[i,j] = s * v

  Uinv = r8mat_u1_inverse ( U )

  A = np.matmul ( Uinv, Linv )

  return A

def golub_lu ( n, key ):

#*****************************************************************************80
#
## golub_lu() returns the LU factors of a golub matrix.
#
#  Discussion:
#
#    These matrices are the product of random unit lower and unit upper 
#    triangular matrices.
#
#    These matrices tend to be badly conditioned.
#
#  Properties:
#
#    A can be LU factored without pivoting.
#
#    det(A) = 1.
#
#    For values of n greater than 10, the determinant cannot may not be 
#    reliably computed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer KEY, a seed for the random number generator.
#
#  Output:
#
#    real L(N,N), U(N,N), the LU factors.
#
  import numpy as np

  np.random.seed ( key )

  s = 10.0

  L = identity_matrix ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      v = np.random.normal ( 0.0, 1.0 )
      L[i,j] = s * v

  U = identity_matrix ( n, n )

  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      v = np.random.normal ( 0.0, 1.0 )
      U[i,j] = s * v

  return L, U

def golub_matrix ( n, key ):

#*****************************************************************************80
#
## golub_matrix() returns the golub matrix.
#
#  Discussion:
#
#    These matrices are the product of random unit lower and unit upper 
#    triangular matrices.
#
#    These matrices tend to be badly conditioned.
#
#  Properties:
#
#    A can be LU factored without pivoting.
#
#    det(A) = 1.
#
#    For values of n greater than 10, the determinant cannot may not be 
#    reliably computed.
#
#    A(1,1) = 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer KEY, a seed for the random number generator.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  np.random.seed ( key )

  s = 10.0

  L = identity_matrix ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      v = np.random.normal ( 0.0, 1.0 )
      L[i,j] = s * v

  U = identity_matrix ( n, n )

  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      v = np.random.normal ( 0.0, 1.0 )
      U[i,j] = s * v

  A = np.matmul ( L, U )

  return A

def golub_plu ( n, key ):

#*****************************************************************************80
#
## golub_plu() returns the PLU factors of a golub matrix.
#
#  Discussion:
#
#    These matrices are the product of random unit lower and unit upper 
#    triangular matrices.
#
#    These matrices tend to be badly conditioned.
#
#  Properties:
#
#    A can be LU factored without pivoting.
#
#    det(A) = 1.
#
#    For values of n greater than 10, the determinant cannot may not be 
#    reliably computed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 January 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer KEY, a seed for the random number generator.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the LU factors.
#
  import numpy as np

  np.random.seed ( key )

  P = identity_matrix ( n, n )

  s = 10.0

  L = identity_matrix ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      v = np.random.normal ( 0.0, 1.0 )
      L[i,j] = s * v

  U = identity_matrix ( n, n )

  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      v = np.random.normal ( 0.0, 1.0 )
      U[i,j] = s * v

  return P, L, U

def golub_test ( ):

#*****************************************************************************80
#
## golub_test() tests golub_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'golub_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  golub_matrix() computes the golub matrix.' )

  m = 5
  n = 5
  key = 123456789
  a = golub_matrix ( n, key )
  r8mat_print ( m, n, a, '  golub matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'golub_test' )
  print ( '  Normal end of execution.' )
  return

def grcar_matrix ( m, n, k ):

#*****************************************************************************80
#
## grcar_matrix() returns the GRCAR matrix.
#
#  Formula:
#
#    if ( I == J+1 )
#      A(I,J) = -1.0
#    elseif ( I <= J and J <= I+K )
#      A(I,J) = 1.0
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    M = 5, N = 5, K = 2
#
#     1  1  1  0  0
#    -1  1  1  1  0
#     0 -1  1  1  1
#     0  0 -1  1  1
#     0  0  0 -1  1
#
#  Rectangular Properties:
#
#    The diagonal and first K superdiagonals are 1, while the first
#    subdiagonal is -1.
#
#    A is banded, with bandwidth K+2.
#
#    A is integral: int ( A ) = A.
#
#    A is upper Hessenberg.
#
#    A is Toeplitz: constant along diagonals.
#
#  Square Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    The eigenvalues are sensitive.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The family of matrices is nested as a function of N.
#
#    A is not diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Grcar,
#    Operator coefficient methods for linear equations,
#    Technical Report SAND89-8691, 
#    Sandia National Laboratories, Albuquerque,
#    New Mexico, 1989 (Appendix 2).
#
#    NM Nachtigal, L Reichel, Lloyd Trefethen,
#    A hybrid GMRES algorithm for nonsymmetric linear systems,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 13, 1992, pages 796-825.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#    integer K, the number of superdiagonals of 1's.  
#    K should be no greater than N-1.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):

    for j in range ( 0, n ):

      if ( i == j + 1 ):
        a[i,j] = -1.0
      elif ( i <= j and j <= i + k ):
        a[i,j] = 1.0
      else:
        a[i,j] = 0.0

  return a

def grcar_test ( ):

#*****************************************************************************80
#
## grcar_test() tests grcar_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'grcar_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  grcar_matrix() computes the grcar matrix.' )

  m = 5
  n = 5
  k = 2
  a = grcar_matrix ( m, n, k )
  r8mat_print ( m, n, a, '  grcar matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'grcar_test' )
  print ( '  Normal end of execution.' )
  return

def hamming_matrix ( m, n ):

#*****************************************************************************80
#
## hamming_matrix() computes the HAMMING matrix.
#
#  Example:
#
#    M = 3, N = 7
#
#    1 1 1 0 1 0 0
#    1 1 0 1 0 1 0
#    1 0 1 1 0 0 1
#
#    7 6 5 3 4 2 1 <-- binary interpretation of columns
#
#  Discussion:
#
#    For a given order M, the Hamming matrix is a rectangular array
#    of M rows and (2^M)-1 columns.  The entries of the matrix are
#    0 and 1.  The columns of A should be interpreted as the binary
#    representations of the integers between 1 and (2^M)-1.
#
#    We can also think of the columns as representing nonempty subsets
#    of an M set.  With this perspective, the columns of the matrix
#    are listed by order of size of subset.  For a given size, the columns
#    are ordered lexicographically.
#
#    The Hamming matrix can be viewed as an embodiment of the Hamming
#    code.  The nonsingleton columns correspond to data bits, and the
#    singleton columns correspond to check bits.  Each row of the
#    matrix represents a condition that the data bits and check bits
#    must satisfy.
#
#  Properties:
#
#    A has full row rank.
#
#    The last M columns of A contain the M by M identity matrix.
#
#    A is integral: int ( A ) = A.
#
#    A is a zero-one matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in the matrix.
#
#    integer N, the number of columns in the matrix.
#    N must be equal to 2^M-1.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  if ( n != ( 2 ** m - 1 ) ):
    print ( '' )
    print ( 'HAMMING - Fatal error!' )
    print ( '  M = %d' % ( m ) )
    print ( '  N = %d' % ( n ) )
    print ( '  but N = 2^M-1 is required.' )
    raise Exception ( 'HAMMING - Fatal error!' )

  a = np.zeros ( ( m, n ) )

  b = np.zeros ( m, dtype = np.int32 )

  for j in range ( n - 1, -1, -1 ):
    b = bvec_next_grlex ( m, b )
    for i in range ( 0, m ):
      a[i,j] = float ( b[i] )

  return a

def hamming_null_right ( m, n ):

#*****************************************************************************80
#
## hamming_null_right() returns a right null vector for the HAMMING matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(N), a right null vector.
#
  import numpy as np

  if ( n != ( ( 2 ** m ) - 1 ) ):
    print ( '' )
    print ( 'hamming_null_right - Fatal error!' )
    print ( '  M = %d' % ( m ) )
    print ( '  N = %d' % ( n ) )
    print ( '  but N = 2^M-1 is required.' )
    raise Exception ( 'hamming_null_right - Fatal error!' )

  if ( m < 2 ):
    print ( '' )
    print ( 'hamming_null_right - Fatal error!' )
    print ( '  M must be at least 2.' )
    raise Exception ( 'hamming_null_right - Fatal error!' )

  x = np.zeros ( n )

  x[0] =  1.0
  for j in range ( n - m, n ):
    x[j] = -1.0

  return x

def hamming_test ( ):

#*****************************************************************************80
#
## hamming_test() tests hamming_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hamming_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hamming_matrix() computes the HAMMING matrix.' )

  m = 3
  n = ( 2 ** 3 ) - 1
  a = _matrix ( m, n )
  r8mat_print ( m, n, a, '  HAMMING matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hamming_test' )
  print ( '  Normal end of execution.' )
  return

def hankel_n_matrix ( n ):

#*****************************************************************************80
#
## hankel_n_matrix() returns the hankel_n matrix.
#
#  Formula:
#
#    A(I,J) = I+J-1 for I+J-1 <= N + 1
#           = 0     otherwise 
#
#  Example:
#
#    N = 5
#
#    1  2  3  4  5
#    2  3  4  5  0
#    3  4  5  0  0
#    4  5  0  0  0
#    5  0  0  0  0
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    determinant ( A ) = (-1)^(N/2) * N^N
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n - j ):
      a[i,j] = float ( i + j + 1 )
    for i in range ( n - j, n ):
      a[i,j] = 0.0

  return a

def hankel_n_condition ( n ):

#*****************************************************************************80
#
## hankel_n_condition() returns the L1 condition of the hankel_n matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  import numpy as np

  v = np.zeros ( n )

  v[0] = 1.0 / float ( n )
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      v[i] = v[i] - ( n + j - i ) * v[j]
    v[i] = v[i] / n

  a_norm = float ( n * ( n + 1 ) ) / 2.0
  b_norm = np.sum ( abs ( v ) )
  value = a_norm * b_norm

  return value

def hankel_n_determinant ( n ):

#*****************************************************************************80
#
## hankel_n_determinant() returns the determinant of the hankel_n matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  determ = r8_mop ( ( n // 2 ) ) * ( n ** n )

  return determ

def hankel_n_inverse ( n ):

#*****************************************************************************80
#
## hankel_n_inverse() returns the inverse of the hankel_n matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  v = np.zeros ( n )

  v[0] = 1.0 / float ( n )
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      v[i] = v[i] - float ( n + j - i ) * v[j]
    v[i] = v[i] / float ( n )

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( n - 1 - j, n ):
      a[i,j] = v[i+j+1-n]

  return a

def hankel_n_test ( ):

#*****************************************************************************80
#
## hankel_n_test() tests hankel_n_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hankel_n_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hankel_n_matrix() computes the hankel_n matrix.' )

  m = 5
  n = m
  a = hankel_n_matrix ( n )
  r8mat_print ( m, n, a, '  hankel_n matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hankel_n_test' )
  print ( '  Normal end of execution.' )
  return

def hankel_inverse ( n, x ):

#*****************************************************************************80
#
## hankel_inverse() returns the inverse of a Hankel matrix.
#
#  Discussion:
#
#    An NxN Hankel matrix is defined by a vector X of length 2*N-1
#    containing the first row and (most of) the last column.
#
#    If X = ( 1, 2, 3, 4, 5, 6, 7, 8, 9 )
#
#    then the Hankel matrix A is:
#
#      1  2  3  4  5
#      2  3  4  5  6
#      3  4  5  6  7
#      4  5  6  7  8
#      5  6  7  8  9
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Miroslav Fiedler,
#    Hankel and Loewner Matrices
#
#  Input:
#
#    integer N, the order of the Hankel matrix.
#
#    real X(2*N-1), the vector that defines the matrix.
#
#  Output:
#
#    real B(N,N), the inverse matrix.
#
  import numpy as np
#
#  Define the matrix.
#
  A = hankel_matrix ( n, x )
#
#  Solve two linear systems.
#
  p = np.zeros ( n )
  p[0:n-1] = x[n:2*n-1]
  p[n-1] = 0.0
# p = np.concatenate ( [ x[n:2*n-1], 0.0 ] )
  A.shape
  p.shape
  u = np.linalg.solve ( A, p )

  q = np.zeros ( n )
  q[n-1] = 1.0
  v = np.linalg.solve ( A, q )
#
#  Construct four matrices.
#
  z1 = np.zeros ( n )
  w1 = np.concatenate ( [ v[1:n], z1 ] )
  M1 = hankel_matrix ( n, w1 )

  z2 = np.zeros ( n-1 )
  w2 = np.concatenate ( [ z2, u ] )
  M2 = toeplitz_matrix ( n, w2 )

  z3 = np.zeros ( n )
  z3[0] = -1.0
  w3 = np.concatenate ( [ u[1:n], z3 ] )
  M3 = hankel_matrix ( n, w3 )

  z4 = np.zeros ( n-1 )
  w4 = np.concatenate ( [ z4, v ] )
  M4 = toeplitz_matrix ( n, w4 )
#
#  Construct the inverse matrix.
#
  B = np.matmul ( M1, M2 ) - np.matmul ( M3, M4 )

  return B

def hankel_matrix ( n, x ):

#*****************************************************************************80
#
## hankel_matrix() returns a HANKEL matrix.
#
#  Formula:
#
#    A(I,J) = X(I+J-1)
#
#  Example:
#
#    N = 5, X = ( 1, 2, 3, 4, 5, 6, 7, 8, 9 )
#
#    1  2  3  4  5
#    2  3  4  5  6
#    3  4  5  6  7
#    4  5  6  7  8
#    5  6  7  8  9
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    The family of matrices is nested as a function of N.
#
#    A is not diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(2*N-1), the vector that defines A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a[i,j] = x[j+i]

  return a

def hankel_matrix_test ( ):

#*****************************************************************************80
#
## hankel_matrix_test() tests hankel_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hankel_matrix_test\n' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hankel_matrix() computes ta Hankel matrix.' )
  print ( '' )

  n = 5
  x = np.random.normal ( 0.0, 1.0, size = ( 2 * n - 1 ) )
  A = hankel_matrix ( n, x )
  r8mat_print ( n, n, A, '  A Hankel matrix' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hankel_test' )
  print ( '  Normal end of execution.' )

  return

def hanowa_matrix ( alpha, n ):

#*****************************************************************************80
#
## hanowa_matrix() returns the Hanowa matrix.
#
#  Formula:
#
#    If ( I = J )
#      A(I,J) = ALPHA
#    else if ( I <= N/2 and J = I+N/2 )
#      A(I,J) = -I
#    else if ( N/2 < I and J = I-N/2 )
#      A(I,J) = I-N/2
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 17, N = 6
#
#    17  0  0 -1  0  0
#     0 17  0  0 -2  0
#     0  0 17  0  0 -3
#     1  0  0 17  0  0
#     0  2  0  0 17  0
#     0  0  3  0  0 17
#
#  Properties:
#
#    A is generally not symmetric: A' ~= A.
#
#    A is nonsingular.
#
#    A is antisymmetric: A' = -A.
#
#    Because A is antisymmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A has complex eigenvalues
#
#      LAMBDA(2*I-1) = ALPHA + I * sqrt ( -1 )
#      LAMBDA(2*I)   = ALPHA - I * sqrt ( -1 )
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
#  Reference:
#
#    E Hairer, SP Norsett, G Wanner,
#    Solving Ordinary Differential Equations I: Nonstiff Problems,
#    Springer Verlag, Berlin, 1987, pages 86-87.
#
#  Input:
#
#    real ALPHA, the scalar defining the Hanowa matrix.  A
#    typical value is -1.0.
#
#    integer N, the order of A.  N must be even.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  if ( ( n % 2 ) != 0 ):
    print ( '' )
    print ( 'hanowa_matrix - Fatal error!' )
    print ( '  Input N = %d' % ( n ) )
    print ( '  but N must be a multiple of 2.' )
    raise Exception ( 'hanowa_matrix - Fatal error!' )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = alpha
      elif ( i + 1 <= ( n // 2 ) and j == i + ( n // 2 ) ):
        a[i,j] = float ( - i - 1 )
      elif ( ( n // 2 ) < i + 1 and j == i - ( n // 2 ) ):
        a[i,j] = float ( i + 1 - ( n // 2 ) )

  return a

def hanowa_determinant ( alpha, n ):

#*****************************************************************************80
#
## hanowa_determinant() returns the determinant of the HANOWA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#    A common value is -1.
#
#    integer N, the order of the matrix.  N must be even.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) != 0 ):
    print ( '' )
    print ( 'hanowa_determinant - Fatal error!' )
    print ( '  Input N = %d' % ( n ) )
    print ( '  but N must be a multiple of 2.' )
    raise Exception ( 'hanowa_determinant - Fatal error!' )

  determ = 1.0

  ihi = ( n // 2 )
  for i in range ( 1, ihi + 1 ):
    determ = determ * ( alpha * alpha + i * i )

  return determ

def hanowa_inverse ( alpha, n ):

#*****************************************************************************80
#
## hanowa_inverse() returns the inverse of the HANOWA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining the Hanowa matrix.  A
#    typical value is -1.0.
#
#    integer N, the order of A.  N must be even.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( ( n % 2 ) != 0 ):
    print ( '' )
    print ( 'hanowa_inverse - Fatal error!' )
    print ( '  The matrix order N must be even.' )
    raise Exception ( 'hanowa_inverse - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  n2 = ( n // 2 )

  for i in range ( 0, n2 ):

    ip1 = float ( i + 1 )

    a[i,   i]    =   alpha / ( alpha * alpha + ip1 * ip1 )
    a[i+n2,i]    = -  ip1  / ( alpha * alpha + ip1 * ip1 )

    a[i+n2,i+n2] =   alpha / ( alpha * alpha + ip1 * ip1 )
    a[i,   i+n2] = +  ip1  / ( alpha * alpha + ip1 * ip1 )

  return a

def hanowa_test ( ):

#*****************************************************************************80
#
## hanowa_test() tests hanowa_matrix().
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
  import platform

  print ( '' )
  print ( 'hanowa_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hanowa_matrix() computes the HANOWA matrix.' )

  m = 6
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )

  a = hanowa_matrix ( alpha, n )
  r8mat_print ( m, n, a, '  HANOWA matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hanowa_test' )
  print ( '  Normal end of execution.' )
  return

def harman_matrix ( ):

#*****************************************************************************80
#
## harman_matrix() returns the Harman matrix.
#
#  Formula:
#
#   1.00  0.85  0.81  0.86  0.47  0.40  0.30  0.38
#   0.85  1.00  0.88  0.83  0.38  0.33  0.28  0.41
#   0.81  0.88  1.00  0.80  0.38  0.32  0.24  0.34
#   0.86  0.83  0.80  1.00  0.44  0.33  0.33  0.36
#   0.47  0.38  0.38  0.44  1.00  0.76  0.73  0.63
#   0.40  0.33  0.32  0.33  0.76  1.00  0.58  0.58
#   0.30  0.28  0.24  0.33  0.73  0.58  1.00  0.54
#   0.38  0.41  0.34  0.36  0.63  0.58  0.54  1.00
#
#  Properties:
#
#    A is symmetric.
#
#    A is a correlation matrix for 8 physical variables measured
#    for 305 girls.
#
#    The rows and columns of the matrix correspond to the variables
#    1) height
#    2) arm span
#    3) length of forearm
#    4) length of lower leg
#    5) weight
#    6) bitrochanteric diameter
#    7) chest girth
#    8) chest width
#
#    The largest two eigenvalues are 
#
#      LAMBDA(1) = 4.67 
#
#    with eigenvector
#
#      V(1) = 0.40, 0.39, 0.38, 0.39, 0.35, 0.31, 0.29, 0.31
#
#    and 
#
#      LAMBDA(2)= 1.77
#
#    with eigevector
#
#      V(2) = 0.28 0.33 0.34 0.30 -0.39, -0.40 -0.44 -0.31
#
#    The best rank 2 approximation to the matrix, in the least squares
#    sense, is
#
#      [ V(1) V(2) ] * Diag ( LAMBDA(1), LAMBDA(2) ) * [ V(1) V(2) ]'
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
#  Reference:
#
#    HH Harman,
#    Modern Factor Analysis,
#    The University of Chicago Press, 1960.
#
#    Lawrence Huber, Jacqueline Meulman, Willem Heiser,
#    Two Purposes for Matrix Factorization: A Historical Appraisal,
#    SIAM Review, Volume 41 : number 1, pages 68-82.
#
#  Output:
#
#    real A(8,8), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 1.00, 0.85, 0.81, 0.86, 0.47, 0.40, 0.30, 0.38 ], \
    [ 0.85, 1.00, 0.88, 0.83, 0.38, 0.33, 0.28, 0.41 ], \
    [ 0.81, 0.88, 1.00, 0.80, 0.38, 0.32, 0.24, 0.34 ], \
    [ 0.86, 0.83, 0.80, 1.00, 0.44, 0.33, 0.33, 0.36 ], \
    [ 0.47, 0.38, 0.38, 0.44, 1.00, 0.76, 0.73, 0.63 ], \
    [ 0.40, 0.33, 0.32, 0.33, 0.76, 1.00, 0.58, 0.58 ], \
    [ 0.30, 0.28, 0.24, 0.33, 0.73, 0.58, 1.00, 0.54 ], \
    [ 0.38, 0.41, 0.34, 0.36, 0.63, 0.58, 0.54, 1.00 ] ])

  return a

def harman_condition ( ):

#*****************************************************************************80
#
## harman_condition() returns the L1 condition of the HARMAN matrix.
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
#  Output:
#
#    real VALUE, the L1 condition number.
#
  a_norm = 5.07
  b_norm = 15.200976381839961
  value = a_norm * b_norm

  return value

def harman_determinant ( ):

#*****************************************************************************80
#
## harman_determinant() returns the determinant of the HARMAN matrix.
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
#  Output:
#
#    real VALUE, the determinant.
#
  value = 9.547789295599994E-04

  return value

def harman_inverse ( ):

#*****************************************************************************80
#
## harman_inverse() returns the inverse of the HARMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(8,8), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
  [  5.505750442924552,  -2.024827472733320, \
    -0.525564377998213,  -2.414725599885703, \
    -0.742871704140835,  -0.432339085897328, \
     0.506363394364808,   0.231316810459756 ], \
  [ -2.024827472733320,   6.632253606390529, \
    -3.266421707396942,  -1.157009948040102, \
     0.941928425100928,   0.010152122779319, \
    -0.318255180872113,  -0.850127918526706 ], \
  [ -0.525564377998213,  -3.266421707396943, \
     4.945029645612116,  -0.799896971199349, \
    -0.384019974978888,  -0.082141525217929, \
     0.342191583208235,   0.250391407726364 ], \
  [ -2.414725599885702,  -1.157009948040101, \
    -0.799896971199349,   4.769523661962869, \
    -0.343306754780455,   0.462478615948815, \
    -0.415704081428472,   0.119432120786903 ], \
  [ -0.742871704140835,   0.941928425100928, \
    -0.384019974978887,  -0.343306754780455, \
     3.941357428629264,  -1.549806320843210, \
    -1.467270532044103,  -0.641583610147637 ], \
  [ -0.432339085897328,   0.010152122779319, \
    -0.082141525217929,   0.462478615948815, \
    -1.549806320843210,   2.524233450449795, \
    -0.122867685019045,  -0.399766570085388 ], \
  [  0.506363394364808,  -0.318255180872113, \
     0.342191583208235,  -0.415704081428472, \
    -1.467270532044103,  -0.122867685019045, \
     2.276170982094793,  -0.262113772509967 ], \
  [  0.231316810459756,  -0.850127918526706, \
     0.250391407726364,   0.119432120786903, \
    -0.641583610147637,  -0.399766570085388, \
    -0.262113772509967,   1.910127138708912 ] ] )

  return a

def harman_test ( ):

#*****************************************************************************80
#
## harman_test() tests harman_matrix().
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
  import platform

  print ( '' )
  print ( 'harman_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  harman_matrix() computes the HARMAN matrix.' )

  n = 8
  a = harman_matrix ( )
  r8mat_print ( n, n, a, '  HARMAN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'harman_test' )
  print ( '  Normal end of execution.' )
  return

def hartley_matrix ( n ):

#*****************************************************************************80
#
## hartley_matrix() returns the HARTLEY matrix.
#
#  Formula:
#
#    A(I,J) = SIN ( 2*PI*(i-1)*(j-1)/N ) + COS( 2*PI*(i-1)*(j-1)/N )
#
#  Example:
#
#    N = 5
#
#    1.0000    1.0000    1.0000    1.0000    1.0000
#    1.0000    1.2601   -0.2212   -1.3968   -0.6420
#    1.0000   -0.2212   -0.6420    1.2601   -1.3968
#    1.0000   -1.3968    1.2601   -0.6420   -0.2212
#    1.0000   -0.6420   -1.3968   -0.2212    1.2601
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A arises in the Hartley transform.
#
#    A * A = N * I, in other words, A is "almost" involutional,
#    and inverse ( A ) = ( 1 / N ) * A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    D Bini, P Favati,
#    On a matrix algebra related to the discrete Hartley transform,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 14, 1993, pages 500-507.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = 2.0 * np.pi * float ( i * j ) / float ( n )

      a[i,j] = np.sin ( angle ) + np.cos ( angle )

  return a

def hartley_condition ( n ):

#*****************************************************************************80
#
## hartley_condition() returns the L1 condition of the HARTLEY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = float ( n )
  b_norm = 1.0
  value = a_norm * b_norm

  return value

def hartley_determinant ( n ):

#*****************************************************************************80
#
## hartley_determinant() returns the determinant of the HARTLEY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  import numpy as np

  if ( ( n % 2 ) == 1 ):
    determ = np.sqrt ( float ( n ** n ) )
  else:
    determ = - np.sqrt ( float ( n ** n ) )

  return determ

def hartley_inverse ( n ):

#*****************************************************************************80
#
## hartley_inverse() returns the inverse of the HARTLEY matrix.
#
#  Formula:
#
#    A(I,J) = (1/N) * SIN ( 2*PI*(i-1)*(j-1)/N ) + COS( 2*PI*(i-1)*(j-1)/N )
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    D Bini, P Favati,
#    On a matrix algebra related to the discrete Hartley transform,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 14, 1993, pages 500-507.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = 2.0 * np.pi * float ( i * j ) / float ( n )

      a[i,j] = ( np.sin ( angle ) + np.cos ( angle ) ) / float ( n )

  return a

def hartley_test ( ):

#*****************************************************************************80
#
## hartley_test() tests hartley_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hartley_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hartley_matrix() computes the HARTLEY matrix.' )

  m = 5
  n = m

  a = hartley_matrix ( n )
 
  r8mat_print ( m, n, a, '  HARTLEY matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hartley_test' )
  print ( '  Normal end of execution.' )
  return

def helmert2_matrix ( n, x ):

#*****************************************************************************80
#
## helmert2_matrix() returns the HELMERT2 matrix.
#
#  Formula:
#
#    Row 1 = the vector, divided by its L2 norm.
#
#    Row 2 is computed by the requirements that it be orthogonal to row 1,
#    be nonzero only from columns 1 to 2, and have a negative diagonal.
#
#    Row 3 is computed by the requirements that it be orthogonal to
#    rows 1 and 2, be nonzero only from columns 1 to 3, and have a
#    negative diagonal, and so on.
#
#  Properties:
#
#    The first row of A should be the vector X, divided by its L2 norm.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    A is not symmetric: A' ~= A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    HO Lancaster,
#    The Helmert Matrices,
#    American Mathematical Monthly,
#    Volume 72, 1965, pages 4-12.
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N), the vector that defines the first row.
#    X must not have 0 L2 norm, and its first entry must not be 0.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  x_norm_l2 = np.linalg.norm ( x )

  if ( x_norm_l2 == 0.0 ):
    print ( '' )
    print ( 'HELMERT2 - Fatal error!' )
    print ( '  Input vector has zero L2 norm.' )
    raise Exception ( 'HELMERT2 - Fatal error!' )

  if ( x[0] == 0.0 ):
    print ( '' )
    print ( 'HELMERT2 - Fatal error!' )
    print ( '  Input vector has X[0] = 0.' )
    raise Exception ( 'HELMERT2 - Fatal error!' )

  w = np.zeros ( n )
  for i in range ( 0, n ):
    w[i] = ( x[i] / x_norm_l2 ) ** 2

  s = np.zeros ( n )
  s[0] = w[0]
  for i in range ( 1, n ):
    s[i] = s[i-1] + w[i]

  for j in range ( 0, n ):
    a[0,j] = np.sqrt ( w[j] )

  for i in range ( 1, n ):
    for j in range ( 0, i ):
      a[i,j] = np.sqrt ( w[i] * w[j] / ( s[i] * s[i-1] ) )
    a[i,i] = - np.sqrt ( s[i-1] / s[i] )

  return a

def helmert2_determinant ( n ):

#*****************************************************************************80
#
## helmert2_determinant() returns the determinant of the HELMERT2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 0 ):
    determ = -1.0
  else:
    determ = +1.0

  return determ

def helmert2_inverse ( n, x ):

#*****************************************************************************80
#
## helmert2_inverse() returns the inverse of the HELMERT2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N), the vector that defines the first row.
#
#  Output:
#
#    real A(N,N), the inverse matrix.
#
  import numpy as np

  a = helmert2_matrix ( n, x )

  a = np.transpose ( a )

  return a

def helmert2_test ( ):

#*****************************************************************************80
#
## helmert2_test() tests helmert2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'helmert2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  helmert2_matrix() computes the HELMERT2 matrix.' )

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )
  a = helmert2_matrix ( n, x )
 
  r8mat_print ( m, n, a, '  HELMERT2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'helmert2_test' )
  print ( '  Normal end of execution.' )
  return

def helmert_matrix ( n ):

#*****************************************************************************80
#
## helmert_matrix() returns the HELMERT matrix.
#
#  Formula:
#
#    If I == 0 then
#      A(I,J) = 1 / sqrt ( N )
#    else if J < I then
#      A(I,J) = 1 / sqrt ( I * ( I + 1 ) )
#    else if J == I then
#      A(I,J) = -I / sqrt ( I * ( I + 1 ) )
#    else
#      A(I,J) = 0
#
#  Discussion:
#
#    The matrix given above by Helmert is the classic example of
#    a family of matrices which are now called Helmertian or
#    Helmert matrices.
#
#    A matrix is a (standard) Helmert matrix if it is orthogonal,
#    and the elements which are above the diagonal and below the
#    first row are zero.
#
#    If the elements of the first row are all strictly positive,
#    then the matrix is a strictly Helmertian matrix.
#
#    It is possible to require in addition that all elements below
#    the diagonal be strictly positive, but in the reference, this
#    condition is discarded as being cumbersome and not useful.
#
#    A Helmert matrix can be regarded as a change of basis matrix
#    between a pair of orthonormal coordinate bases.  The first row
#    gives the coordinates of the first new basis vector in the old
#    basis.  Each later row describes combinations of (an increasingly
#    extensive set of) old basis vectors that constitute the new
#    basis vectors.
#
#    Helmert matrices have important applications in statistics.
#
#  Example:
#
#    N = 5
#
#    0.4472    0.4472    0.4472    0.4472    0.4472
#    0.7071   -0.7071         0         0         0
#    0.4082    0.4082   -0.8165         0         0
#    0.2887    0.2887    0.2887   -0.8660         0
#    0.2236    0.2236    0.2236    0.2236   -0.8944
#
#  Properties:
#
#    A is generally not symmetric: A' ~= A.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    Because A is orthogonal, it is normal: A' * A = A * A'.
#
#    A is not symmetric: A' ~= A.
#
#    det ( A ) = (-1)^(N+1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    HO Lancaster,
#    The Helmert Matrices,
#    American Mathematical Monthly,
#    Volume 72, 1965, pages 4-12.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
#
#  A begins with the first row, diagonal, and lower triangle set to 1.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):
        a[i,j] = 1.0 / np.sqrt ( n )
      elif ( j < i ):
        a[i,j] = 1.0 / np.sqrt ( float ( i * ( i + 1 ) ) )
      elif ( i == j ):
        a[i,j] = float ( - i ) / np.sqrt ( float ( i * ( i + 1 ) ) )

  return a

def helmert_determinant ( n ):

#*****************************************************************************80
#
## helmert_determinant() returns the determinant of the HELMERT matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 0 ):
    determ = - 1.0
  else:
    determ = 1.0

  return determ

def helmert_inverse ( n ):

#*****************************************************************************80
#
## helmert_inverse() returns the inverse of the HELMERT matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the inverse matrix.
#
  import numpy as np

  a = helmert_matrix ( n )

  a = np.transpose ( a )

  return a

def helmert_test ( ):

#*****************************************************************************80
#
## helmert_test() tests helmert_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'helmert_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  helmert_matrix() computes the HELMERT matrix.' )

  m = 5
  n = m

  a = helmert_matrix ( n )
 
  r8mat_print ( m, n, a, '  HELMERT matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'helmert_test' )
  print ( '  Normal end of execution.' )
  return

def hermite_matrix ( n ):

#*****************************************************************************80
#
## hermite_matrix() returns the HERMITE matrix.
#
#  Example:
#
#    N = 11
#
#        1     .      .      .       .     .      .     .      .   .    .
#        .     2      .      .       .     .      .     .      .   .    .
#       -2     .      4      .       .     .      .     .      .   .    .
#        .   -12      .      8       .     .      .     .      .   .    .
#       12     .    -48      .      16     .      .     .      .   .    .
#        .   120      .   -160       .    32      .     .      .   .    .
#     -120     .    720      .    -480     .     64     .      .   .    .
#        . -1680      .   3360       . -1344      .   128      .   .    .
#     1680     . -13440      .   13440     .  -3584     .    256   .    .
#        . 30240      . -80640       . 48384      . -9216      . 512    .
#   -30240     . 302400      . -403200     . 161280     . -23040   . 1024
#
#  Properties:
#
#    A is generally not symmetric: A' ~= A.
#
#    A is lower triangular.
#
#    det ( A ) = 2^((N*(N-1))/2)
#
#    LAMBDA(I) = 2^(I-1).
#
#    A is integral: int ( A ) = A.
#
#    A is reducible.
#
#    Successive diagonals are zero, positive, zero, negative.
#
#    A is generally not normal: A' * A ~= A * A'.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np
  
  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,1] = 2.0

    for i in range ( 2, n ):
      for j in range ( 0, n ):
        if ( j == 0 ):
          a[i,j] =                  - 2.0 * ( i - 1 ) * a[i-2,j]
        else:
          a[i,j] = 2.0 * a[i-1,j-1] - 2.0 * ( i - 1 ) * a[i-2,j]

  return a

def hermite_determinant ( n ):

#*****************************************************************************80
#
## hermite_determinant() returns the determinant of the HERMITE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  power = ( n * ( n - 1 ) ) // 2
  value = 2.0 ** power

  return value

def hermite_inverse ( n ):

#*****************************************************************************80
#
## hermite_inverse() returns the inverse of the HERMITE matrix.
#
#  Example:
#
#    N = 11
#
#        1     .     .     .     .    .    .  .  . . .
#        .     1     .     .     .    .    .  .  . . .  /    2
#        2     .     1     .     .    .    .  .  . . .  /    4
#        .     6     .     1     .    .    .  .  . . .  /    8
#       12     .    12     .     1    .    .  .  . . .  /   16
#        .    60     .    20     .    1    .  .  . . .  /   32
#      120     .   180     .    30    .    1  .  . . .  /   64
#        .   840     .   420     .   42    .  1  . . .  /  128
#     1680     .  3360     .   840    .   56  .  1 . .  /  256
#        . 15120     . 10080     . 1512    . 72  . 1 .  /  512
#    30240     . 75600     . 25200    . 2520  . 90 . 1  / 1024
#
#  Properties:
#
#    A is generally not symmetric: A' ~= A.
#
#    A is nonnegative.
#
#    A is lower triangular.
#
#    det ( A ) = 1 / 2^((N*(N-1))/2)
#
#    LAMBDA(I) = 1 / 2^(I-1)
#
#    A is reducible.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,1] = 0.5

    if ( 2 < n ):

      for i in range ( 2, n ):
        for j in range ( 0, n ):
          if ( j == 0 ):
            a[i,j] = ( float ( i - 1 ) * a[i-2,j]              ) / 2.0
          else:
            a[i,j] = ( float ( i - 1 ) * a[i-2,j] + a[i-1,j-1] ) / 2.0

  return a

def hermite_test ( ):

#*****************************************************************************80
#
## hermite_test() tests hermite_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hermite_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hermite_matrix() computes the HERMITE matrix.' )

  m = 5
  n = m

  a = hermite_matrix ( n )
 
  r8mat_print ( m, n, a, '  HERMITE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hermite_test' )
  print ( '  Normal end of execution.' )
  return

def herndon_matrix ( n ):

#*****************************************************************************80
#
## herndon_matrix() returns the HERNDON matrix.
#
#  Formula:
#
#    c = ( n * ( n + 1 ) * ( 2 * n - 5 ) ) / 6
#    a(n,n) = - 1 / c
#    for i = 1 : n - 1
#      a(i,n) = a(n,i) = i / c
#      a(i,i) = ( c - i*i ) / c
#      for j = 1, i - 1
#        a(i,j) = a(j,i) = - i * j / c
#       end
#     end
#
#  Example:
#
#    N = 5
#
#     0.96  -0.08  -0.12  -0.16   0.04
#    -0.08   0.84  -0.24  -0.32   0.08
#    -0.12  -0.24   0.64  -0.48   0.12
#    -0.16  -0.32  -0.48   0.36   0.16
#     0.04   0.08   0.12   0.16  -0.04
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal: A' * A = A * A'.
#
#    The eigenvalues of A are:
#
#      1 (multiplicity N-2),
#      6 / ( P * ( N + 1 ),
#      P / ( N * ( 5 - 2 * N ) ),
#
#    where
#
#      P = 3 + sqrt ( ( 4 * N - 3 ) * ( N - 1 ) * 3 / ( N + 1 ) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Herndon,
#    Algorithm 52, A Set of Test Matrices,
#    Communications of the ACM,
#    April, 1961.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  c = float ( n * ( n + 1 ) * ( 2 * n - 5 ) ) / 6.0

  a[n-1,n-1] = - 1.0 / c

  for i in range ( 0, n - 1 ):

    a[i,n-1] = float ( i + 1 ) / c
    a[n-1,i] = float ( i + 1 ) / c
    a[i,i]   = ( c - float ( ( i + 1 ) * ( i + 1 ) ) ) / c

    for j in range ( 0, i ):

      a[i,j] = - float ( ( i + 1 ) * ( j + 1 ) ) / c
      a[j,i] = - float ( ( i + 1 ) * ( j + 1 ) ) / c

  return a

def herndon_determinant ( n ):

#*****************************************************************************80
#
## herndon_determinant() returns the determinant of the HERNDON matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 6.0 / float ( ( n + 1 ) * n * ( 5 - 2 * n ) )

  return value

def herndon_inverse ( n ):

#*****************************************************************************80
#
## herndon_inverse() returns the inverse of the Herndon matrix.
#
#  Formula:
#
#    if ( I == N )
#      A(I,J) = J
#    else if ( J == N )
#      A(I,J) = I
#    else if ( I == J )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  1
#    0  1  0  0  2
#    0  0  1  0  3
#    0  0  0  1  4
#    1  2  3  4  5
#
#  Properties:
#
#    A is symmetric.
#
#    A is border-banded.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Herndon,
#    Algorithm 52, A Set of Test Matrices,
#    Communications of the ACM,
#    April, 1961.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n - 1 ):
    a[i,i] = 1.0

  for i in range ( 0, n - 1 ):
    a[i,n-1] = float ( i + 1 )

  for j in range ( 0, n - 1 ):
    a[n-1,j] = float ( j + 1 )

  a[n-1,n-1] = float ( n )

  return a

def herndon_test ( ):

#*****************************************************************************80
#
## herndon_test() tests herndon_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'herndon_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  herndon_matrix() computes the HERNDON matrix.' )

  m = 5
  n = m

  a = herndon_matrix ( n )
 
  r8mat_print ( m, n, a, '  HERNDON matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'herndon_test' )
  print ( '  Normal end of execution.' )
  return

def hess4_matrix ( ):

#*****************************************************************************80
#
## hess4_matrix() returns the HESS4 matrix.
#
#  Example:
#
#    4+8i  7+6i  7+10i 7+10i
#    9+9i  8+1i  8+10i 2 +5i
#    0     8+3i  7+ 2i 7 +8i
#    0     0     4+10i 0 +1i
#
#  Properties:
#
#    A is integral.
#
#    A is not symmetric.
#
#    A is complex.
#
#    A is upper Hessenberg.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    complex A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 4+8*1j,  7+6*1j,  7+10*1j, 7+10*1j ], \
    [ 9+9*1j,  8+1*1j,  8+10*1j, 2+ 5*1j ], \
    [ 0+0*1j,  8+3*1j,  7+ 2*1j, 7+ 8*1j ], \
    [ 0+0*1j,  0+0*1j,  4+10*1j, 0+ 1*1j ] ] )

  return a

def hess4_determinant ( ):

#*****************************************************************************80
#
## hess4_determinant() returns the determinant of the HESS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    complex VALUE, the determinant.
#
  value = 6.393999999999999e+03 - 4.548000000000000e+03*1j

  return value

def hess4_eigen_right ( ):

#*****************************************************************************80
#
## hess4_eigen_right() returns the right eigenvectors of the HESS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    complex A(4,4), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ -0.330070042547862-0.222298022567869*1j, \
      1.000000000000000+0.000000000000000*1j, \
      0.335490948571943-0.068002965084462*1j, \
      0.952157320531579+0.250709960744793*1j ], \
    [ 1.000000000000000+0.000000000000000*1j, \
      0.503205870426247-0.824241552742355*1j, \
     -0.768179408120474+0.010513990305666*1j, \
      1.000000000000000+0.000000000000000*1j ], \
    [ 0.257417722386482+0.309094498615456*1j, \
     -0.215016769732540+0.275479867860766*1j, \
      1.000000000000000+0.000000000000000*1j, \
      0.501508766439785-0.172182272014276*1j ], \
    [-0.842630039297297+0.197751498603984*1j, \
     -0.238196952722339+0.597205448629795*1j, \
     -0.972653465585451-0.104040336437224*1j, \
      0.218561824850003+0.044757232962382*1j ] ] )

  return a

def hess4_eigenvalues ( ):

#*****************************************************************************80
#
## hess4_eigenvalues() returns the eigenvalues of the HESS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    complex LAMBA(4), the eigenvalues.
#
  import numpy as np

  lamda = np.array ( [ \
        3.324431041502838- 2.742026572531628*1j, \
        0.568541187348097+ 6.826204344246118*1j, \
       -5.153228803481162- 8.729936381660266*1j, \
       20.260256574630240+16.645758609945791*1j ] )

  return lamda

def hess4_inverse ( ):

#*****************************************************************************80
#
## hess4_inverse() returns the pseudo-inverse of the HESS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    complex B(4,4), the matrix.
#
  import numpy as np

  b = np.array ( [ \
  [  0.055479592005787-0.046555961144460*1j, \
    0.008223391741817-0.036847046349424*1j, \
   -0.072930346088215+0.062294774161839*1j, \
   -0.165446110076836-0.054339835569198*1j ], \
  [ 0.098221887702513+0.072992359285429*1j, \
    0.151056059735374+0.029715821031667*1j, \
   -0.013605643493308-0.002639735159144*1j, \
    0.008483821182396+0.004783299771276*1j ], \
  [ 0.003980766488315+0.005177436032039*1j, \
    0.146615375569659-0.028025222381794*1j, \
   -0.103971410909060-0.013897712983173*1j, \
   -0.060517409011307-0.035851294367129*1j] , \
  [-0.048947708484049+0.045728154803651*1j, \
   -0.018713432435338+0.036423414026287*1j, \
    0.034460691461767-0.089345132191411*1j, \
    0.012773614147975+0.031294087761181*1j ] ] )

  return b

def hess4_test ( ):

#*****************************************************************************80
#
## hess4_test() tests hess4_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hess4_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hess4_matrix() returns the HESS4 matrix.' )

  m = 4
  n = 4
  a = hess4_matrix ( )

  c8mat_print ( m, n, a, '  HESS4 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hess4_test' )
  print ( '  Normal end of execution.' )
  return

def hess5_matrix ( ):

#*****************************************************************************80
#
## hess5_matrix() returns the HESS5 matrix.
#
#  Example:
#
#     9     4     1     3     2
#     4     3     1     7     1
#     0     3     1     2     4
#     0     0     5     5     1
#     0     0     0     1     2
#
#  Properties:
#
#    A is integral.
#
#    A is not symmetric.
#
#    A is upper Hessenberg.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(5,5), the matrix.
# 
  import numpy as np

  a = np.array ( [ \
    [ 9.0,     4.0,     1.0,     3.0,     2.0 ], \
    [ 4.0,     3.0,     1.0,     7.0,     1.0 ], \
    [ 0.0,     3.0,     1.0,     2.0,     4.0 ], \
    [ 0.0,     0.0,     5.0,     5.0,     1.0 ], \
    [ 0.0,     0.0,     0.0,     1.0,     2.0 ] ] )

  return a

def hess5_determinant ( ):

#*****************************************************************************80
#
## hess5_determinant() returns the determinant of the HESS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1479.0

  return value

def hess5_eigen_right ( ):

#*****************************************************************************80
#
## hess5_eigen_right() returns the right eigenvectors of the HESS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    complex A(5,5), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ -0.4048+0.0000*j, -0.2788-0.1981*j, -0.2788+0.1981*j,  1.0000+0.0000*j,  1.0000+0.0000*j ], \
    [  1.0000+0.0000*j,  1.0000+0.0000*j,  1.0000+0.0000*j,  0.0372+0.0000*j,  0.5780+0.0000*j ], \
    [  0.0565+0.0000*j, -0.0712-0.9695*j, -0.0712+0.9695*j, -0.2064+0.0000*j,  0.1887+0.0000*j ], \
    [  0.1687+0.0000*j, -0.3560+0.6933*j, -0.3560-0.6933*j, -0.5057+0.0000*j,  0.1379+0.0000*j ], \
    [ -0.8231+0.0000*j,  0.1938-0.0411*j,  0.1938+0.0411*j, -0.0966+0.0000*j,  0.0139+0.0000*j ] ] )

  return a

def hess5_eigenvalues ( ):

#*****************************************************************************80
#
## hess5_eigenvalues() returns the eigenvalues of the HESS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    complex LAMDA(4), the eigenvalues.
#
  import numpy as np

  lamda = np.array ( [ \
     1.795071645585215 + 0.000000000000000*j, \
    -0.484650565840867 + 3.050399870879445*j, \
    -0.484650565840867 - 3.050399870879445*j, \
     7.232089690415871 + 0.000000000000000*j, \
    11.942139795680633 + 0.000000000000000*j ] )

  return lamda

def hess5_inverse ( ):

#*****************************************************************************80
#
## hess5_inverse() returns the inverse of the HESS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real B(5,5), the matrix.
#
  import numpy as np

  b = np.array ( [ \
    [  0.131845841784990, -0.046653144016227, -0.129141311697093,  0.008789722785666,   0.145368492224476 ], \
    [ -0.024340770791075,  0.054766734279919,  0.311020960108181, -0.068289384719405,  -0.590939824205544 ], \
    [  0.073022312373225, -0.164300202839757,  0.066937119675456,  0.204868154158215,  -0.227180527383367 ], \
    [ -0.081135902636917,  0.182555780933063, -0.074374577417174, -0.005409060175794,   0.141311697092630 ], \
    [  0.040567951318458, -0.091277890466531,  0.037187288708587,  0.002704530087897,   0.429344151453685 ] ] )

  return b

def hess5_test ( ):

#*****************************************************************************80
#
## hess5_test() tests hess5_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hess5_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hess5_matrix() returns the HESS5 matrix.' )

  m = 5
  n = 5
  a = hess5_matrix ( )

  r8mat_print ( m, n, a, '  HESS5 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hess5_test' )
  print ( '  Normal end of execution.' )
  return

def hilbert_matrix ( m, n ):

#*****************************************************************************80
#
## hilbert_matrix() returns the HILBERT matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( I + J - 1 )
#
#  Example:
#
#    N = 5
#
#    1/1 1/2 1/3 1/4 1/5
#    1/2 1/3 1/4 1/5 1/6
#    1/3 1/4 1/5 1/6 1/7
#    1/4 1/5 1/6 1/7 1/8
#    1/5 1/6 1/7 1/8 1/9
#
#  Rectangular Properties:
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#  Square Properties:
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is totally positive.
#
#    A is a Cauchy matrix.
#
#    A is nonsingular.
#
#    A is very ill-conditioned.
#
#    The entries of the inverse of A are all integers.
#
#    The sum of the entries of the inverse of A is N*N.
#
#    The ratio of the absolute values of the maximum and minimum
#    eigenvalues is roughly EXP(3.5*N).
#
#    The determinant of the Hilbert matrix of order 10 is
#    2.16417... * 10^(-53).
#
#    If the (1,1) entry of the 5 by 5 Hilbert matrix is changed from
#    1 to 24/25, the matrix is exactly singular.  And there
#    is a similar rule for larger Hilbert matrices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    MD Choi,
#    Tricks or treats with the Hilbert matrix,
#    American Mathematical Monthly,
#    Volume 90, 1983, pages 301-312.
#
#    Robert Gregory, David Karney,
#    Example 3.8,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 33,
#    LC: QA263.G68.
#
#    Nicholas Higham,
#    Accuracy and Stability of Numerical Algorithms,
#    Society for Industrial and Applied Mathematics, Philadelphia, PA,
#    USA, 1996; section 26.1.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition
#    Addison-Wesley, Reading, Massachusetts, 1973, page 37.
#
#    Morris Newman and John Todd,
#    Example A13,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, 1958, pages 466-476.
#
#    Joan Westlake,
#    Test Matrix A12,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / float ( i + j + 1 )

  return a

def hilbert_determinant ( n ):

#*****************************************************************************80
#
## hilbert_determinant() returns the determinant of the HILBERT matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  top = 1.0
  for i in range ( 1, n + 1 ):
    for j in range ( i + 1, n + 1 ):
      top = top * float ( ( j - i ) * ( j - i ) )

  bottom = 1.0
  for i in range ( 1, n + 1 ):
    for j in range ( 1, n + 1 ):
      bottom = bottom * float ( i + j - 1 )

  value = top / bottom

  return value

def hilbert_inverse ( n ):

#*****************************************************************************80
#
## hilbert_inverse() returns the inverse of the Hilbert matrix.
#
#  Formula:
#
#    A(I,J) =  (-1)^(I+J) * (N+I-1)! * (N+J-1)! /
#           [ (I+J-1) * ((I-1)!*(J-1)!)^2 * (N-I)! * (N-J)! ]
#
#  Example:
#
#    N = 5
#
#       25    -300     1050    -1400     630
#     -300    4800   -18900    26880  -12600
#     1050  -18900    79380  -117600   56700
#    -1400   26880  -117600   179200  -88200
#      630  -12600    56700   -88200   44100
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is almost impossible to compute accurately by general routines
#    that compute the inverse.
#
#    A is the exact inverse of the Hilbert matrix; however, if the
#    Hilbert matrix is stored on a finite precision computer, and
#    hence rounded, A is actually a poor approximation
#    to the inverse of that rounded matrix.  Even though Gauss elimination
#    has difficulty with the Hilbert matrix, it can compute an approximate
#    inverse matrix whose residual is lower than that of the
#    "exact" inverse.
#
#    All entries of A are integers.
#
#    The sum of the entries of A is N^2.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
#
#  Set the (1,1) entry.
#
  a[0,0] = n * n
#
#  Define Row 1, Column J by recursion on Row 1 Column J-1
#
  i = 0
  for j in range ( 1, n ):
    a[i,j] = - a[i,j-1] * float ( ( n + j ) * ( i + j ) * ( n - j ) ) \
      / float ( ( i + j + 1 ) * j * j )
#
#  Define Row I by recursion on row I-1
#
  for i in range ( 1, n ):
    for j in range ( 0, n ):

      a[i,j] = - a[i-1,j] * float ( ( n + i ) * ( i + j ) * ( n- i ) ) \
        / float ( ( i + j + 1 ) * i * i )

  return a

def hilbert_test ( ):

#*****************************************************************************80
#
## hilbert_test() tests hilbert_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hilbert_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hilbert_matrix() returns the HILBERT matrix.' )

  m = 5
  n = m

  a = hilbert_matrix ( m, n )
 
  r8mat_print ( m, n, a, '  HILBERT matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hilbert_test' )
  print ( '  Normal end of execution.' )
  return

def householder_matrix ( n, x ):

#*****************************************************************************80
#
## householder_matrix() constructs a HOUSEHOLDER matrix.
#
#  Discussion:
#
#    A Householder matrix is also called an elementary reflector.
#
#  Formula:
#
#     A = I - ( 2 * X * X' ) / ( X' * X )
#
#  Example:
#
#    N = 5, X = ( 1, 1, 1, 0, -1 )
#
#   1/2 -1/2 -1/2  0  1/2
#  -1/2  1/2 -1/2  0  1/2
#  -1/2 -1/2  1/2  0  1/2
#    0    0    0   1   0
#   1/2  1/2  1/2  0  1/2
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    inverse ( A ) = A.
#
#    det ( A ) = -1.
#
#    A is unimodular.
#
#    If Y and Z are nonzero vectors of equal length, and
#      X = ( Y - Z ) / NORM(Y-Z),
#    then
#      A * Y = Z.
#
#    A represents a reflection through the plane which
#    is perpendicular to the vector X.  In particular, A*X = -X.
#
#    LAMBDA(1) = -1;
#    LAMBDA(2:N) = +1.
#
#    If X is the vector used to define H, then X is the eigenvector
#    associated with the eigenvalue -1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989.
#
#    Pete Stewart,
#    Introduction to Matrix Computations,
#    Academic Press, 1973,
#
#    James Wilkinson,
#    The Algebraic Eigenvalue Problem,
#    Oxford University Press, 1965.
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N), the vector that defines the 
#    Householder matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  xdot = 0.0
  for i in range ( 0, n ):
    xdot = xdot + x[i] * x[i]

  if ( 0.0 < xdot ):

    for i in range ( 0, n ):
      for j in range ( 0, n ):
        a[i,j] = a[i,j] - 2.0 * x[i] * x[j] / xdot

  return a

def householder_determinant ( n, x ):

#*****************************************************************************80
#
## householder_determinant() returns the determinant of the HOUSEHOLDER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N), the vector.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = -1.0
 
  return value

def householder_inverse ( n, x ):

#*****************************************************************************80
#
## householder_inverse() returns the inverse of a HOUSEHOLDER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N), the vector that defines the 
#    Householder matrix.
#
#  Output:
#
#    real A(N,N), the eigenvalues.
#
  a = householder_matrix ( n, x )

  return a

def householder_test ( ):

#*****************************************************************************80
#
## householder_test() tests householder_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'householder_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  householder_matrix() returns the HOUSEHOLDER matrix.' )

  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )

  a = householder_matrix ( n, x )
  m = n
  r8mat_print ( m, n, a, '  HOUSEHOLDER matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'householder_test' )
  print ( '  Normal end of execution.' )
  return

def i4_factor ( n ):

#*****************************************************************************80
#
## i4_factor() factors an integer into prime factors.
#
#  Discussion:
#
#    N = NLEFT * Product ( 1 <= I <= NFACTOR ) FACTOR(I)^EXPONENT(I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be factored.  N may be positive,
#    negative, or 0.
#
#  Output:
#
#    integer NFACTOR, the number of prime factors of N discovered
#    by the routine.
#
#    integer FACTOR(NFACTOR), the prime factors of N.
#
#    integer EXPONENT(NFACTOR).  EXPONENT(I) is the power of
#    the FACTOR(I) in the representation of N.
#
#    integer NLEFT, the factor of N that the routine could not
#    divide out.  If NLEFT is 1, then N has been completely factored.
#    Otherwise, NLEFT represents factors of N involving large primes.
#
  import numpy as np

  nfactor = 0

  factor_list = []
  exponent_list = []

  nleft = n

  if ( n == 0 ):
    factor = np.zeros ( 0 )
    exponent = np.zeros ( 0 )
    return nfactor, factor, exponent, nleft

  if ( abs ( n ) == 1 ):
    nfactor = 1
    factor_list.append ( 1 )
    exponent_list.append ( 0 )
    factor = np.ones ( 1 )
    exponent = np.zeros ( 1 )
    return nfactor, factor, exponent, nleft
#
#  Find out how many primes we stored.
#
  maxprime = prime ( -1 )
#
#  Try dividing the remainder by each prime.
#
  for i in range ( 1, maxprime + 1 ):

    p = prime ( i )

    if ( ( abs ( nleft ) ) % p == 0 ):

      nfactor = nfactor + 1
      factor_list.append ( p )
      exponent_list.append ( 0 )

      while ( True ):

        exponent_list[nfactor-1] = exponent_list[nfactor-1] + 1
        nleft = ( nleft // p )

        if ( ( abs ( nleft ) ) % p != 0 ):
          break

      if ( abs ( nleft ) == 1 ):
        break

  factor = np.zeros ( nfactor )
  exponent = np.zeros ( nfactor )
  for i in range ( 0, nfactor ):
    factor[i] = factor_list[i]
    exponent[i] = exponent_list[i]
  return nfactor, factor, exponent, nleft

def i4_factor_test ( ):

#*****************************************************************************80
#
## i4_factor_test() tests i4_factor().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_factor_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_factor factors an integer.' )

  n = 2 * 2 * 17 * 37

  print ( '' )
  print ( '  The integer is %d' % ( n ) )

  nfactor, factor, power, nleft = i4_factor ( n )

  print ( '' )
  print ( '  Prime representation:' )
  print ( '' )
  print ( '  I, FACTOR(I), POWER(I)' )
  print ( '' )
  if ( abs ( nleft ) != 1 ):
    print ( '  %6d  %6d  (UNFACTORED PORTION)' % ( 0, nleft ) )

  for i in range ( 0, nfactor ):
    print ( '  %6d  %6d  %6d' % ( i, factor[i], power[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_factor_test' )
  print ( '  Normal end of execution.' )
  return

def i4_is_even ( i ):

#*****************************************************************************80
#
## i4_is_even() returns TRUE if I is even.
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
#    integer I, the integer to be tested.
#
#  Output:
#
#    boolean VALUE, is TRUE if I is even.
#
  value = ( ( i % 2 ) == 0 )

  return value

def i4_is_even_test ( ) :

#*****************************************************************************80
#
## i4_is_even_test() tests i4_is_even().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_is_even_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_is_even reports whether an I4 is even.' )
  print ( ' ' )
  print ( '         I  i4_is_even(I)' )
  print ( ' ' )

  for i in range ( -2, 26 ):
    j = i4_is_even ( i )
    print ( '  %8d  %r' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_is_even_test' )
  print ( '  Normal end of execution.' )
  return

def i4_is_odd ( i ):

#*****************************************************************************80
#
## i4_is_odd() returns TRUE if I is odd.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the integer to be tested.
#
#  Output:
#
#    bool VALUE, is TRUE if I is odd.
#
  value = ( ( i % 2 ) == 1 )

  return value

def i4_is_odd_test ( ) :

#*****************************************************************************80
#
## i4_is_odd_test() tests i4_is_odd().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_is_odd_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_is_odd reports whether an I4 is odd.' )
  print ( '' )
  print ( '         I  i4_is_odd(I)' )
  print ( '' )

  for i in range ( -2, 26 ):
    j = i4_is_odd ( i )
    print ( '  %8d  %r' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_is_odd_test' )
  print ( '  Normal end of execution.' )
  return

def i4_is_prime ( n ) :

#*****************************************************************************80
#
## i4_is_prime() reports whether an I4 is prime.
#
#  Discussion:
#
#    A simple, unoptimized sieve of Eratosthenes is used to
#    check whether N can be divided by any integer between 2
#    and SQRT(N).
#
#    Note that negative numbers, 0 and 1 are not considered prime.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be tested.
#
#  Output:
#
#    bool VALUE, is TRUE if N is prime, and FALSE otherwise.
#
  import numpy as np

  if ( n <= 0 ):
    value = False
    return value

  if ( n == 1 ):
    value = False
    return value

  if ( n <= 3 ):
    value = True
    return value

  nhi = int ( np.sqrt ( float ( n ) ) )

  for i in range ( 2, nhi + 1 ):
    if ( ( n % i ) == 0 ):
      value = False
      return value

  value = True

  return value

def i4_is_prime_test ( ) :

#*****************************************************************************80
#
## i4_is_prime_test() tests i4_is_prime().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_is_prime_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_is_prime reports whether an I4 is prime.' )
  print ( '' )
  print ( '         I  i4_is_prime(I)' )
  print ( '' )

  for i in range ( -2, 26 ):
    j = i4_is_prime ( i )
    print ( '  %8d  %r' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_is_prime_test' )
  print ( '  Normal end of execution.' )
  return

def i4_log_10 ( i ):

#*****************************************************************************80
#
## i4_log_10() returns the integer part of the logarithm base 10 of ABS(X).
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
## i4_log_10_test() tests i4_log_10().
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
  import platform

  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ( '' )
  print ( 'i4_log_10_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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

def i4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## i4mat_print() prints an I4MAT.
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

def i4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## i4mat_print_some() prints out a portion of an I4MAT.
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
  incx = 10

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

def i4_modp ( i, j ):

#*****************************************************************************80
#
## i4_modp() returns the nonnegative remainder of I4 division.
#
#  Discussion:
#
#    If
#      NREM = i4_modp ( I, J )
#      NMULT = ( I - NREM ) / J
#    then
#      I = J * NMULT + NREM
#    where NREM is always nonnegative.
#
#    The MOD function returns a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, i4_modp(A,360) is between 0 and 360, always.
#
#  Example:
#
#        I     J     MOD  i4_modp    Factorization
#
#      107    50       7       7    107 =  2 *  50 + 7
#      107   -50       7       7    107 = -2 * -50 + 7
#     -107    50      -7      43   -107 = -3 *  50 + 43
#     -107   -50      -7      43   -107 =  3 * -50 + 43
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
#    integer I, the number to be divided.
#
#    integer J, the number that divides I.
#
#  Output:
#
#    integer VALUE, the nonnegative remainder when I is divided by J.
#
  if ( j == 0 ):
    print ( '' )
    print ( 'i4_modp - Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    raise Exception ( 'i4_modp - Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + abs ( j )

  return value

def i4_modp_test ( ):

#*****************************************************************************80
#
## i4_modp_test() tests i4_modp().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 4

  n_vec = np.array ( ( 107, 107, -107, -107 ) )
  d_vec = np.array ( ( 50, -50, 50, -50 ) )

  print ( '' )
  print ( 'i4_modp_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_modp factors a number' )
  print ( '  into a multiple M and a positive remainder R.' )
  print ( '' )
  print ( '    Number   Divisor  Multiple Remainder' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    r = i4_modp ( n, d )
    m = ( n - r ) // d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  print ( '' )
  print ( '  Repeat using Python % Operator:' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_modp_test' )
  print ( '  Normal end of execution.' )
  return

def i4_rise ( x, n ):

#*****************************************************************************80
#
## i4_rise() returns the rising factorial function [X]^N.
#
#  Discussion:
#
#    [X]^N = X * ( X + 1 ) * ( X + 2 ) * ... * ( X + N - 1 ).
#
#    Note that the number of ways of arranging N objects in M ordered
#    boxes is [M]^N.  (Here, the ordering of the objects in each box matters).
#    Thus, 2 objects in 2 boxes have the following 6 possible arrangements:
#
#      -|12, 1|2, 12|-, -|21, 2|1, 21|-.
#
#    Moreover, the number of non-decreasing maps from a set of
#    N to a set of M ordered elements is [M]^N / N!.  Thus the set of
#    nondecreasing maps from (1,2,3) to (a,b,c,d) is the 20 elements:
#
#      aaa, abb, acc, add, aab, abc, acd, aac, abd, aad
#      bbb, bcc, bdd, bbc, bcd, bbd, ccc, cdd, ccd, ddd.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X, the argument of the rising factorial function.
#
#    integer N, the order of the rising factorial function.
#    If N = 0, RISE = 1, if N = 1, RISE = X.  Note that if N is
#    negative, a "falling" factorial will be computed.
#
#  Output:
#
#    integer VALUE, the value of the rising factorial function.
#
  value = 1

  arg = x

  if ( 0 < n ):

    for i in range ( 0, n ):
      value = value * arg
      arg = arg + 1

  elif ( n < 0 ):

    for i in range ( n, 0 ):
      value = value * arg
      arg = arg - 1

  return value

def i4_rise_test ( ):

#*****************************************************************************80
#
## i4_rise_test() tests i4_rise().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_rise_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_rise evaluates the rising factorial Fall(I,N).' )
  print ( '' )
  print ( '         M         N      Exact         i4_rise(M,N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, m, n, f1 = i4_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = i4_rise ( m, n )

    print ( '  %8d  %8d  %12d  %12d' % ( m, n, f1, f2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_rise_test' )
  print ( '  Normal end of execution.' )
  return

def i4_rise_values ( n_data ):

#*****************************************************************************80
#
## i4_rise_values() returns values of the integer rising factorial function.
#
#  Discussion:
#
#    The integer rising factorial function is sometimes symbolized by (m)_n.
#
#    The definition is
#
#      (m)_n = (m-1+n)! / (m-1)!
#            = ( m ) * ( m + 1 ) * ( m + 2 ) ... * ( m - 1 + n )
#            = Gamma ( m + n ) / Gamma ( m )
#
#    We assume 0 <= N <= M.
#
#    In Mathematica, the function can be evaluated by:
#
#      Pochhammer[m,n]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.
#
#  Output:
#
#    integer N_DATA.  The routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer M, N, the arguments of the function.
#
#    integer FMN, the value of the function.
#
  import numpy as np

  n_max = 15

  fmn_vec = np.array ( [ 
     1, 5, 30, 210, 1680, \
     15120, 151200, 1, 10, 4000, \
     110, 6840, 840, 970200, 5040 ] )
  m_vec = np.array ( [ 
    5, 5, 5, 5, 5, \
    5, 5, 50, 10, 4000, \
    10, 18, 4, 98, 1 ] )
  n_vec = np.array ( [ 
     0, 1, 2, 3, 4, \
    5, 6, 0, 1, 1, \
    2, 3, 4, 3, 7 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    m = 0
    n = 0
    fmn = 0
  else:
    m = m_vec[n_data]
    n = n_vec[n_data]
    fmn = fmn_vec[n_data]
    n_data = n_data + 1

  return n_data, m, n, fmn

def i4_rise_values_test ( ):

#*****************************************************************************80
#
## i4_rise_values_test() tests i4_rise_values().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_rise_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_rise_values returns values of the integer rising factorial.' )
  print ( '' )
  print ( '          M         N          i4_rise(M,N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, m, n, fmn = i4_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %8d  %8d' % ( m, n, fmn ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_rise_values_test:' )
  print ( '  Normal end of execution.' )
  return

def i4_sign ( i ):

#*****************************************************************************80
#
## i4_sign() returns the sign of an integer.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose sign is desired.
#
#  Output:
#
#    integer VALUE, the sign of I.
#
  if ( i < 0 ):
    value = -1
  else:
    value = +1

  return value

def i4_sign_test ( ):

#*****************************************************************************80
#
## i4_sign_test() tests i4_sign().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 5

  i4_vec = np.array ( ( -10, -7, 0, 5, 9 ) )

  print ( '' )
  print ( 'i4_sign_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_sign returns the sign of an I4.' )
  print ( '' )
  print ( '    I4  i4_sign(I4)' )
  print ( '' )

  for test in range ( 0, test_num ):
    i4 = i4_vec[test]
    s = i4_sign ( i4 )
    print ( '  %4d  %11d' % ( i4, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_sign_test' )
  print ( '  Normal end of execution.' )
  return

def i4vec_indicator0 ( n ):

#*****************************************************************************80
#
## i4vec_indicator0() sets an I4VEC to the indicator vector ( 0, 1, 2, ... ).
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    integer A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    a[i] = i

  return a

def i4vec_indicator0_test ( ):

#*****************************************************************************80
#
## i4vec_indicator0_test() tests i4vec_indicator0().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4vec_indicator0_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_indicator0 returns an indicator vector.' )

  n = 10
  a = i4vec_indicator0 ( n )
  i4vec_print ( n, a, '  The indicator0 vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_indicator0_test' )
  print ( '  Normal end of execution.' )
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

def i4_wrap ( value, lo, hi ):

#*****************************************************************************80
#
## i4_wrap() forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    LO = 4, HI = 8
#
#    In   Out
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer VALUE, an integer value.
#
#    integer LO, HI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of VALUE.
#
  value = lo + ( ( value - lo ) % ( hi - lo + 1 ) )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## i4_wrap_test() tests i4_wrap().
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
  import platform

  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'i4_wrap_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_wrap forces an integer to lie within given limits.' )
  print ( '' )
  print ( '  ILO = %d' % ( ilo ) )
  print ( '  IHI = %d' % ( ihi ) )
  print ( '' )
  print ( '     I  i4_wrap(I)' )
  print ( '' )

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print ( '  %6d  %6d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_wrap_test' )
  print ( '  Normal end of execution.' )
  return

def idempotent_random_matrix ( n, rank, key ):

#*****************************************************************************80
#
## idempotent_random_matrix() returns the IDEMPOTENT_RANDOM matrix of rank K.
#
#  Properties:
#
#    A is idempotent: A * A = A
#
#    If A is invertible, then A must be the identity matrix.
#    In other words, unless A is the identity matrix, it is singular.
#
#    I - A is also idempotent.
#
#    All eigenvalues of A are either 0 or 1.
#
#    rank(A) = trace(A)
#
#    A is a projector matrix.
#
#    The matrix I - 2A is involutory, that is ( I - 2A ) * ( I - 2A ) = I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alston Householder, John Carpenter,
#    The singular values of involutory and of idempotent matrices,
#    Numerische Mathematik,
#    Volume 5, 1963, pages 234-237.
#
#  Input:
#
#    integer N, the order of A.
#
#    integer RANK, the rank of A.
#    0 <= RANK <= N.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( rank < 0 or n < rank ):
    print ( '' )
    print ( 'idempotent_random_matrix - Fatal error!' )
    print ( '  RANK must be between 0 and N.' )
    print ( '  Input value = %d' % ( rank ) )
    raise Exception ( 'idempotent_random - Fatal error!' )
#
#  Get a random orthogonal matrix Q.
#
  q = orthogonal_random_matrix ( n, key )
#
#  Compute Q' * D * Q, where D is the diagonal eigenvalue matrix
#  of RANK 1's followed by N-RANK 0's.
#
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      t = 0.0
      for k in range ( 0, rank ):
        t = t + q[k,i] * q[k,j]
      a[i,j] =  t

  return a

def idempotent_random_determinant ( n, rank, key ):

#*****************************************************************************80
#
## idempotent_random_determinant(): determinant of the idempotent_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer RANK, the rank.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real VALUE, the determinant.
#
  if ( rank == n ):
    value = 1.0
  else:
    value = 0.0

  return value

def idempotent_random_eigen_right ( n, rank, key ):

#*****************************************************************************80
#
## idempotent_random_eigen_right(): right eigenvectors of the idempotent_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alston Householder, John Carpenter,
#    The singular values of involutory and of idempotent matrices,
#    Numerische Mathematik,
#    Volume 5, 1963, pages 234-237.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer RANK, the rank of A.
#    0 <= RANK <= N.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real X(N,N), the matrix.
#
  import numpy as np

  x = orthogonal_random_matrix ( n, key )

  x = np.transpose ( x )

  return x

def idempotent_random_eigenvalues ( n, rank, key ):

#*****************************************************************************80
#
## idempotent_random_eigenvalues(): eigenvalues of the idempotent_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer RANK, the rank of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, rank ):
    lam[i] = 1.0

  return lam

def idempotent_random_test ( ):

#*****************************************************************************80
#
## idempotent_random_test() tests idempotent_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  i4_lo = 0
  i4_hi = n

  print ( '' )
  print ( 'idempotent_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  idempotent_random_matrix() returns a random idempotent matrix.' )

  rank = np.random.randint ( 0, n + 1 )

  print ( '' )
  print ( '  Randomly chosen rank will be %d' % ( rank ) )

  key = 123456789

  a = idempotent_random_matrix ( n, rank, key )

  m = n
  r8mat_print ( m, n, a, '  idempotent_random matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'idempotent_random_test:' )
  print ( '  Normal end of execution.' )
  return

def identity_matrix ( m, n ):

#*****************************************************************************80
#
## identity_matrix() returns the IDENTITY matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 4, N = 5
#
#    1 0 0 0 0
#    0 1 0 0 0
#    0 0 1 0 0
#    0 0 0 1 0
#
#  Rectangular properties:
#
#    A is integral: int ( A ) = A.
#
#    A is a zero/one matrix.
#
#  Square Properties:
#
#    A is nonsingular.
#
#    A is involutional: A * A = I.
#
#    A is diagonal.
#
#    Because A is diagonal, it has property A.
#
#    A is symmetric: A' = A.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    LAMBDA(1:N) = 1
#
#    The matrix of eigenvectors of A is A.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    For any vector v, A*v = v.
#
#    For any matrix B, A*B = B*A=B.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of 
#    the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 1.0

  return a

def identity_condition ( n ):

#*****************************************************************************80
#
## identity_condition() returns the L1 condition of the IDENTITY matrix.
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
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = 1.0
  b_norm = 1.0
  value = a_norm * b_norm

  return value

def identity_determinant ( n ):

#*****************************************************************************80
#
## identity_determinant() returns the determinant of the IDENTITY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def identity_eigen_right ( n ):

#*****************************************************************************80
#
## identity_eigen_right() returns the right eigenvectors of the IDENTITY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  return a

def identity_eigenvalues ( n ):

#*****************************************************************************80
#
## identity_eigenvalues() returns the eigenvalues of the IDENTITY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.ones ( n )

  return lam

def identity_inverse ( n ):

#*****************************************************************************80
#
## identity_inverse() returns the inverse of the IDENTITY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 1.0

  return a

def identity_test ( ):

#*****************************************************************************80
#
## identity_test() tests identity_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'identity_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  identity_matrix() returns the IDENTITY matrix.' )

  m = 4
  n = m

  a = identity_matrix ( m, n )
  r8mat_print ( m, n, a, '  IDENTITY matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'identity_test' )
  print ( '  Normal end of execution.' )
  return

def ijfact1_matrix ( n ):

#*****************************************************************************80
#
## ijfact1_matrix() returns the IJFACT1 matrix.
#
#  Formula:
#
#    A(I,J) = (I+J)!
#
#  Example:
#
#    N = 4
#
#     2   6   24   120
#     6  24  120   720
#    24 120  720  5040
#   120 720 5040 40320
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    A is integral: int ( A ) = A.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    MJC Gover,
#    The explicit inverse of factorial Hankel matrices,
#    Department of Mathematics, University of Bradford, 1993.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from scipy.special import factorial
  import numpy as np

  a = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = factorial ( i + j + 2 )

  return a

def ijfact1_determinant ( n ):

#*****************************************************************************80
#
## ijfact1_determinant() returns the determinant of the IJFACT1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  from scipy.special import factorial

  value = 1.0

  for i in range ( 1, n ):
    value = value * factorial ( i + 1 ) * factorial ( n - i )

  value = value * factorial ( n + 1 )

  return value

def ijfact1_test ( ):

#*****************************************************************************80
#
## ijfact1_test() tests ijfact1_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ijfact1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ijfact1_matrix() returns the IJFACT1 matrix.' )

  m = 5
  n = m

  a = ijfact1_matrix ( n )
 
  r8mat_print ( m, n, a, '  IJFACT1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ijfact1_test' )
  print ( '  Normal end of execution.' )
  return

def ijfact2_matrix ( n ):

#*****************************************************************************80
#
## ijfact2_matrix() returns the IJFACT2 matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( (I+J)! )
#
#  Example:
#
#    N = 4
#
#   1/2   1/6   1/24   1/120
#   1/6   1/24  1/120  1/720
#   1/24  1/120 1/720  1/5040
#   1/120 1/720 1/5040 1/40320
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    A is integral: int ( A ) = A.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    MJC Gover,
#    The explicit inverse of factorial Hankel matrices,
#    Department of Mathematics, University of Bradford, 1993.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from scipy.special import factorial
  import numpy as np

  a = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / factorial ( i + j + 2 )

  return a

def ijfact2_determinant ( n ):

#*****************************************************************************80
#
## ijfact2_determinant() returns the determinant of the IJFACT2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  from scipy.special import factorial

  value = 1.0

  for i in range ( 0, n ):
    value = value * factorial ( i ) / factorial ( n + 1 + i )

  test = ( n * ( n - 1 ) ) // 2

  if ( test % 2 != 0 ):
    value = - value

  return value

def ijfact2_test ( ):

#*****************************************************************************80
#
## ijfact2_test() tests ijfact2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ijfact2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ijfact2_matrix() returns the IJFACT2 matrix.' )

  m = 5
  n = m

  a = ijfact2_matrix ( n )
 
  r8mat_print ( m, n, a, '  IJFACT2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ijfact2_test' )
  print ( '  Normal end of execution.' )
  return

def ill3_matrix ( ):

#*****************************************************************************80
#
## ill3_matrix() returns the ILL3 matrix.
#
#  Discussion:
#
#    This is an ill conditioned 3 by 3 matrix.
#
#  Formula:
#
#    -149  -50 -154
#     537  180  546
#     -27   -9  -25
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    The eigenvalues are ( 1, 2, 3 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Output:
#
#    real A(3,3), the matrix.
#
  import numpy as np

  a = np.array ( [ 
   [ -149.0, -50.0, -154.0 ], \
   [  537.0, 180.0,  546.0 ], \
   [  -27.0,  -9.0,  -25.0 ] ] )

  return a

def ill3_condition ( ):

#*****************************************************************************80
#
## ill3_condition() returns the L1 condition of the ILL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the L1 condition number.
#
  value = 725 * 299

  return value

def ill3_determinant ( ):

#*****************************************************************************80
#
## ill3_determinant() returns the determinant of the ILL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant number.
#
  value = 6.0

  return value

def ill3_eigen_right ( ):

#*****************************************************************************80
#
## ill3_eigen_right() returns the right eigenvectors of the ILL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Output:
#
#    real A(3,3), the right eigenvector matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
  [ -0.139139989879567,   \
    -0.404061017818396,   \
     0.316227766017190 ], \
  [  0.973979929161820,   \
     0.909137290098421,   \
    -0.948683298050396 ], \
  [ -0.178894272703878,   \
     0.101015254452291,   \
    -0.000000000000407 ] ] )

  return a

def ill3_eigenvalues ( ):

#*****************************************************************************80
#
## ill3_eigenvalues() returns the eigenvalues of the ILL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Output:
#
#    real LAMBDA(3), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ 3.0, 2.0, 1.0 ] )

  return lam

def ill3_inverse ( ):

#*****************************************************************************80
#
## ill3_inverse() returns the inverse of the ILL3 matrix.
#
#  Formula:
#
#      69     68/3   70
#    -439/2 -433/6 -224
#       9/2    3/2    5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(3,3), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
      [   69.0,         68.0 / 3.0,   70.0 ], \
      [ -439.0 / 2.0, -433.0 / 6.0, -224.0 ], \
      [    4.5,          1.5,          5.0 ] ] )

  return a

def ill3_test ( ):

#*****************************************************************************80
#
## ill3_test() tests ill3_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ill3_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ill3_matrix() returns the ILL3 matrix.' )

  m = 3
  n = m
  a = ill3_matrix (  )
  r8mat_print ( m, n, a, '  ILL3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ill3_test' )
  print ( '  Normal end of execution.' )
  return

def integration_matrix ( alpha, n ):

#*****************************************************************************80
#
## integration_matrix() returns the INTEGRATION matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1
#    else if ( J = I + 1 )
#      A(I,J) = ALPHA / I
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#    1  2   0   0   0
#    0  1  2/2  0   0
#    0  0   1  2/3  0
#    0  0   0   1  2/4
#    0  0   0   0   1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is unit upper triangular.
#
#    A is bidiagonal.
#
#    Because A is bidiagonal, it has property A (bipartite).
#
#    A is nonsingular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar which defines the first 
#    superdiagonal of the matrix.
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):

      if ( j == i ):
        a[i,j] = 1.0
      elif ( j == i + 1 ):
        a[i,j] = alpha / float ( i + 1 )

  return a

def integration_determinant ( alpha, n ):

#*****************************************************************************80
#
## integration_determinant() returns the determinant of the INTEGRATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#    A common value is -1.
#
#    integer N, the order of the matrix.  N must be even.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def integration_inverse ( alpha, n ):

#*****************************************************************************80
#
## integration_inverse() returns the inverse of the INTEGRATION matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1
#    else if ( I < J )
#      A(I,J) = (-ALPHA)^(J-I) / (I*...*J-1)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#    1 -2   2  -4/3   2/3
#    0  1  -1   2/3  -1/3
#    0  0   1  -2/3   1/3
#    0  0   0    1   -1/2
#    0  0   0    0     1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is unit upper triangular.
#
#    A is nonsingular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar which defines the first
#    superdiagonal of the matrix.
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i ):
        a[i,j] = 1.0
      elif ( i < j ):
        a[i,j] = ( - alpha ) ** ( j - i ) / r8_rise ( i + 1, j - i )

  return a

def integration_test ( ):

#*****************************************************************************80
#
## integration_test() tests integration_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'integration_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  integration_matrix() returns the INTEGRATION matrix.' )

  m = 6
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )

  a = integration_matrix ( alpha, n )
  r8mat_print ( m, n, a, '  INTEGRATION matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'integration_test' )
  print ( '  Normal end of execution.' )
  return

def involutory_matrix ( n ):

#*****************************************************************************80
#
## involutory_matrix() returns the involutory matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( I + J - 1 )
#
#    Set D = -N
#
#    Multiply column 1 of A by D.
#
#    For I = 1 to N-1
#      D = -(N+I)*(N-I)*D/(I*I)
#      Multiply row I + 1 by D.
#    End
#
#  Example:
#
#    N = 5
#
#       -5     0.5     0.33     0.25    0.2
#     -300    40.0    30.00    24.00   20.0
#     1050  -157.5  -126.00  -105.00  -90.0
#    -1400   224.0   186.66   160.00  140.0
#      630  -105.0   -90.00   -78.75  -70.0
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is involutory: A * A = I.
#
#    det ( A ) = +1 or -1.
#
#    A is unimodular.
#
#    The matrices:
#      B = 1/2 ( I - A )
#    and
#      C = 1/2 ( I + A )
#    are idempotent, that is, B * B = B, and C * C = C.
#
#    A is ill-conditioned.
#
#    A is a diagonally scaled version of the Hilbert matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alston Householder, John Carpenter,
#    The singular values of involutory and of idempotent matrices,
#    Numerische Mathematik,
#    Volume 5, 1963, pages 234-237.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / float ( i + j + 1 )
 
  for i in range ( 0, n ):
    a[i,0] = - n * a[i,0]

  d = - float ( n )
  for i in range ( 1, n ):
    d = - float ( n + i ) * float ( n - i ) * d  / float ( i * i )
    for j in range ( 0, n ):
      a[i,j] = d * a[i,j]

  return a

def involutory_determinant ( n ):

#*****************************************************************************80
#
## involutory_determinant() returns the determinant of the involutory matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 4 ) == 0 or ( n % 4 ) == 3 ):
    value = 1.0
  else:
    value = - 1.0

  return value

def involutory_inverse ( n ):

#*****************************************************************************80
#
## involutory_inverse() returns the inverse of the involutory matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  a = involutory_matrix ( n )

  return a

def involutory_test ( ):

#*****************************************************************************80
#
## involutory_test() tests involutory_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'involutory_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  involutory_matrix() computes the involutory matrix.' )

  m = 5
  n = m

  a = involutory_matrix ( n )
 
  r8mat_print ( m, n, a, '  involutory matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'involutory_test' )
  print ( '  Normal end of execution.' )
  return

def involutory_random_matrix ( n, rank, key ):

#*****************************************************************************80
#
## involutory_random_matrix() returns the INVOLUTORY_RANDOM matrix.
#
#  Example:
#
#    N = 5, RANK = 4, KEY = 123456789
#
#   -0.3830    0.0175   -0.7432    0.2818    0.4704
#    0.0175   -0.9995   -0.0211    0.0080    0.0133
#   -0.7432   -0.0211   -0.1049   -0.3395   -0.5666
#    0.2818    0.0080   -0.3395   -0.8713    0.2149
#    0.4704    0.0133   -0.5666    0.2149   -0.6413
#
#  Properties:
#
#    A is nonsingular.
#
#    A is involutory: A * A = I
#
#    det ( A ) = +1 or -1.
#
#    A is unimodular.
#
#    A is not diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alston Householder, John Carpenter,
#    The singular values of involutory and of idempotent matrices,
#    Numerische Mathematik,
#    Volume 5, 1963, pages 234-237.
#
#  Input:
#
#    integer N, the order of A.
#
#    integer RANK, the rank of the idempotent matrix
#    used to generate A.  Setting RANK = 0 or N will yield
#    a multiple of the identity.  Intermediate values will give
#    more interesting results.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  a = idempotent_random_matrix ( n, rank, key )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 1.0 - 2.0 * a[i,j]
      else:
        a[i,j] =     - 2.0 * a[i,j]

  return a

def involutory_random_test ( ):

#*****************************************************************************80
#
## involutory_random_test() tests involutory_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'involutory_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  involutory_random_matrix() computes the involutory_random matrix.' )

  m = 5
  n = 5
  k = 2
  a = involutory_random_matrix ( m, n, k )
  r8mat_print ( m, n, a, '  involutory_random matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'involutory_random_test' )
  print ( '  Normal end of execution.' )
  return

def jacobi_matrix ( m, n ):

#*****************************************************************************80
#
## jacobi_matrix() returns the JACOBI matrix.
#
#  Formula:
#
#    if ( J = I - 1 )
#      A(I,J) = 0.5 * sqrt ( ( 4 * J^2 ) / ( 4 * J^2 - 1 ) )
#    else if ( J = I + 1 )
#      A(I,J) = 0.5 * sqrt ( ( 4 * (J-1)^2 ) / ( 4 * (J-1)^2 - 1 ) )
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 4, N = 4
#
#    0            0.577350269  0            0
#    0.577350269  0            0.516397779  0
#    0            0.516397779  0            0.507092553
#    0            0            0.507092553  0
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A has a zero diagonal.
#
#    The eigenvalues of A are the zeros of the Legendre polynomial
#    of degree N.  They lie symmetrically in [-1,1], and are also
#    the nodes of Gauss-Legendre quadrature.  For the case of N = 4,
#    these eigenvalues are
#
#      [ -0.861136312, -0.339981044, +0.339981044, +0.861136312 ].
#
#    It follows that A is singular when N is odd.
#
#    The J-th Gauss-Legendre weight is twice the square of the first
#    component of the J-th eigenvector of A.  For the case of N = 4,
#    the eigenvector matrix is:
#
#      -0.417046     -0.571028     -0.571028    0.417046
#       0.622037      0.336258     -0.336258    0.622038
#      -0.571028      0.417046      0.417046    0.571028
#       0.336258     -0.622037      0.622038    0.336258
#
#    and the corresponding weights are
#
#      [ 0.347854845, 0.652145155, 0.652145155, 0.347854845 ]
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Lloyd Trefethen, David Bau,
#    Numerical Linear Algebra,
#    SIAM, 1997, pages 287-292.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( j == i - 1 ):
        a[i,j] = 0.5 * np.sqrt ( float ( 4 * ( j + 1 ) ** 2 ) \
                               / float ( 4 * ( j + 1 ) ** 2 - 1 ) )
      elif ( j == i + 1 ):
        a[i,j] = 0.5 * np.sqrt ( float ( 4 * j ** 2 ) \
                               / float ( 4 * j ** 2 - 1 ) )

  return a

def jacobi_determinant ( n ):

#*****************************************************************************80
#
## jacobi_determinant() returns the determinant of the JACOBI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  if ( ( n % 2 ) == 1 ):
  
    value = 0.0
    
  else:
  
    lam = legendre_zeros ( n )
  
    value = np.prod ( lam )

  return value

def jacobi_inverse ( n ):

#*****************************************************************************80
#
## jacobi_inverse() returns the inverse of the JACOBI matrix.
#
#  Discussion:
#
#    This inverse is related to that of the CLEMENT2 matrix.
#
#  Example:
#
#    N = 6
#
#         0    1.7321         0   -1.7638         0    1.7689
#    1.7321         0         0         0         0         0
#         0         0         0    1.9720         0   -1.9777
#   -1.7638         0    1.9720         0         0         0
#         0         0         0         0         0    1.9900
#    1.7689         0   -1.9777         0    1.9900         0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be even.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np
 
  if ( ( n % 2 ) == 1 ):
    print ( '' )
    print ( 'jacobi_inverse - Fatal error!' )
    print ( '  The Jacobi matrix is singular for odd N.' )
    raise Exception ( 'jacobi_inverse - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):

      p = 1.0

      for j in range ( i, n - 1, 2 ):

        a1 = 0.5 * np.sqrt ( float ( 4 * ( j + 1 ) * ( j + 1 ) ) \
          / float ( 4 * ( j + 1 ) * ( j + 1 ) - 1 ) )
        a2 = 0.5 * np.sqrt ( float ( 4 * j * j ) \
          / float ( 4 * j * j - 1 ) )

        if ( j == i ):
          p = p / a1
        else:
          p = - p * a2 / a1
 
        a[i,j+1] = p
        a[j+1,i] = p

  return a

def jacobi_test ( ):

#*****************************************************************************80
#
## jacobi_test() tests jacobi_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'jacobi_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  jacobi_matrix() computes the JACOBI matrix.' )

  m = 4
  n = m

  a = jacobi_matrix ( m, n )
  r8mat_print ( m, n, a, '  JACOBI matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'jacobi_test' )
  print ( '  Normal end of execution.' )
  return

def jordan_matrix ( m, n, alpha ):

#*****************************************************************************80
#
## jordan_matrix() returns the JORDAN matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = ALPHA
#    else if ( I = J-1 )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, M = 5, N = 5
#
#    2  1  0  0  0
#    0  2  1  0  0
#    0  0  2  1  0
#    0  0  0  2  1
#    0  0  0  0  2
#
#  Properties:
#
#    A is upper triangular.
#
#    A is lower Hessenberg.
#
#    A is bidiagonal.
#
#    Because A is bidiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 2.
#
#    A is generally not symmetric: A' /= A.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is nonsingular if and only if ALPHA is nonzero.
#
#    det ( A ) = ALPHA^N.
#
#    LAMBDA(I) = ALPHA.
#
#    A is defective, having only one eigenvector, namely (1,0,0,...,0).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#    real ALPHA, the eigenvalue of the Jordan matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = alpha
      elif ( j == i + 1 ):
        a[i,j] = 1.0

  return a

def jordan_condition ( n, alpha ):

#*****************************************************************************80
#
## jordan_condition() returns the L1 condition of the JORDAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, the eigenvalue of the Jordan matrix.
#
#  Output:
#
#    real VALUE, the L1 condition number.
#
  a2 = abs ( alpha )

  if ( n == 1 ):
    a_norm = a2
  else:
    a_norm = a2 + 1.0

  if ( a2 == 1.0 ):
    b_norm = float ( n ) * a2
  else:
    b_norm = ( a2 ** n - 1.0 ) / ( a2 - 1.0 ) / a2 ** n

  value = a_norm * b_norm

  return value

def jordan_determinant ( n, alpha ):

#*****************************************************************************80
#
## jordan_determinant() returns the determinant of the JORDAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, the eigenvalue of the Jordan matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = alpha ** n

  return value

def jordan_eigenvalues ( n, alpha ):

#*****************************************************************************80
#
## jordan_eigenvalues() returns the eigenvalues of the JORDAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, the eigenvalue of the Jordan matrix.
#
#  Output:
#
#    real LAM[N], the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    lam[i] = alpha

  return value

def jordan_inverse ( n, alpha ):

#*****************************************************************************80
#
## jordan_inverse() returns the inverse of the Jordan block matrix.
#
#  Formula:
#
#    if ( I <= J )
#      A(I,J) =  -1 * (-1/ALPHA)^(J+1-I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, N = 4
#
#    1/2 -1/4  1/8 -1/16
#    0    1/2 -1/4  1/8
#    0    0    1/2 -1/4
#    0    0    0    1/2
#
#  Properties:
#
#    A is upper triangular.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is generally not symmetric: A' /= A.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The inverse of A is the Jordan block matrix, whose diagonal
#    entries are ALPHA, whose first superdiagonal entries are 1,
#    with all other entries zero.
#
#    det ( A ) = (1/ALPHA)^N.
#
#    LAMBDA(1:N) = 1 / ALPHA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real ALPHA, the eigenvalue of the Jordan matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  if ( alpha == 0.0 ):
    print ( '' )
    print ( 'jordan_inverse - Fatal error!' )
    print ( '  The input parameter ALPHA was 0.' )
    raise Exception ( 'jordan_inverse - Fatal error!' )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] =  - ( - 1.0 / alpha ) ** ( j + 1 - i )

  return a

def jordan_test ( ):

#*****************************************************************************80
#
## jordan_test() tests jordan_matrix().
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
  import platform

  print ( '' )
  print ( 'jordan_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  jordan_matrix() computes the JORDAN matrix.' )

  m = 6
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )

  a = jordan_matrix ( m, n, alpha )
  r8mat_print ( m, n, a, '  JORDAN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'jordan_test' )
  print ( '  Normal end of execution.' )
  return

def kahan_matrix ( alpha, m, n ):

#*****************************************************************************80
#
## kahan_matrix() returns the KAHAN matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,I) =  sin(ALPHA)^(I)
#    elseif ( I < J )
#      A(I,J) = - sin(ALPHA)^(I) * cos(ALPHA)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 0.25, N = 4
#
#    S  -C*S    -C*S      -C*S
#    0     S^2  -C*S^2    -C*S^2
#    0     0       S^3    -C*S^3
#    0     0       0         S^4
#
#    where
#
#      S = sin(ALPHA), C=COS(ALPHA)
#
#  Properties:
#
#    A is upper triangular.
#
#    A = B * C, where B is a diagonal matrix and C is unit upper triangular.
#    For instance, for the case M = 3, N = 4:
#
#    A = | S 0    0    |  * | 1 -C -C  -C |
#        | 0 S^2  0    |    | 0  1 -C  -C |
#        | 0 0    S^3  |    | 0  0  1  -C |
#
#    A is generally not symmetric: A' /= A.
#
#    A has some interesting properties regarding estimation of
#    condition and rank.
#
#    det ( A ) = sin(ALPHA)^(N*(N+1)/2).
#
#    LAMBDA(I) = sin ( ALPHA )^I
#
#    A is nonsingular if and only if sin ( ALPHA ) =/= 0.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    A survey of condition number estimation for triangular matrices,
#    SIAM Review,
#    Volume 9, 1987, pages 575-596.
#
#    W Kahan,
#    Numerical Linear Algebra,
#    Canadian Mathematical Bulletin,
#    Volume 9, 1966, pages 757-801.
#
#  Input:
#
#    real ALPHA, the scalar that defines A.  A typical
#    value is 1.2.  The "interesting" range of ALPHA is 0 < ALPHA < PI.
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):

    si = np.sin ( alpha ) ** ( i + 1 )
    csi = - np.cos ( alpha ) * si

    for j in range ( 0, n ):

      if ( j == i ):
        a[i,j] = si
      elif ( i < j ):
        a[i,j] = csi

  return a

def kahan_determinant ( alpha, n ):

#*****************************************************************************80
#
## kahan_determinant() returns the determinant of the KAHAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the parameter.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  power = ( n * ( n + 1 ) ) // 2
  value = ( np.sin ( alpha ) ) ** power

  return value

def kahan_inverse ( alpha, n ):

#*****************************************************************************80
#
## kahan_inverse() returns the inverse of the KAHAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar that defines A.  A typical 
#    value is 1.2.  The "interesting" range of ALPHA is 0 < ALPHA < PI.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  ci = np.cos ( alpha )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = 1.0
      elif ( i == j - 1 ):
        a[i,j] = ci
      elif ( i < j ):
        a[i,j] = ci * ( 1.0 + ci ) ** ( j - i - 1 )
#
#  Scale the columns.
#
  for j in range ( 0, n):
    si = np.sin ( alpha ) ** ( j + 1 )
    for i in range ( 0, n ):
      a[i,j] = a[i,j] / si

  return a

def kahan_test ( ):

#*****************************************************************************80
#
## kahan_test() tests kahan_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'kahan_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  kahan_matrix() computes the KAHAN matrix.' )

  m = 5
  n = 5
  alpha = np.random.rand ( )
  a = kahan_matrix ( alpha, m, n )
  r8mat_print ( m, n, a, '  KAHAN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'kahan_test' )
  print ( '  Normal end of execution.' )
  return

def kershaw_matrix ( ):

#*****************************************************************************80
#
## kershaw_matrix() returns the KERSHAW matrix.
#
#  Discussion:
#
#    The Kershaw matrix is a simple example of a symmetric
#    positive definite matrix for which the incomplete Cholesky
#    factorization fails, because of a negative pivot.
#
#  Example:
#
#     3 -2  0  2
#    -2  3 -2  0
#     0 -2  3 -2
#     2  0 -2  3
#
#  Properties:
#
#    A is symmetric.
#
#    A is positive definite.
#
#    det ( A ) = 1.
#
#    LAMBDA(A) = [ 
#      5.828427124746192
#      5.828427124746188
#      0.171572875253810
#      0.171572875253810 ].
#
#    A does not have an incompete Cholesky factorization.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [  3.0, -2.0,  0.0,  2.0 ], \
    [ -2.0,  3.0, -2.0,  0.0 ], \
    [  0.0, -2.0,  3.0, -2.0 ], \
    [  2.0,  0.0, -2.0,  3.0 ] ] )

  return a

def kershaw_condition ( ):

#*****************************************************************************80
#
## kershaw_condition() returns the L1 condition of the KERSHAW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the condition.
#
  a_norm = 7.0
  b_norm = 7.0
  value = a_norm * b_norm

  return value

def kershaw_determinant ( ):

#*****************************************************************************80
#
## kershaw_determinant() returns the determinant of the KERSHAW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def kershaw_eigen_right ( ):

#*****************************************************************************80
#
## kershaw_eigen_right() returns the right eigenvectors of the KERSHAW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(4,4), the eigenvectors.
#
  import numpy as np

  x = np.array ( [ \
   [  0.500000000000000,  0.500000000000000,   \
     -0.548490135760211,  0.446271857698584 ], \
   [ -0.707106781186548, -0.000000000000000,   \
     -0.703402951241362, -0.072279237578588 ], \
   [  0.500000000000000, -0.500000000000000,   \
     -0.446271857698584, -0.548490135760211 ], \
   [ -0.000000000000000,  0.707106781186548,   \
      0.072279237578588, -0.703402951241362 ] ] )

  return x

def kershaw_eigenvalues ( ):

#*****************************************************************************80
#
## kershaw_eigenvalues() returns the eigenvalues of the KERSHAW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kershaw,
#    The Incomplete Cholesky-Conjugate Gradient Method for the Iterative
#    Solution of Systems of Linear Equations,
#    Journal of Computational Physics,
#    Volume 26, Number 1, January 1978, pages 43-65.
#
#  Output:
#
#    real LAM(4), the eigenvalues of the matrix.
#
  import numpy as np

  lam = np.array ( [ \
    [ 5.828427124746192 ], \
    [ 5.828427124746188 ], \
    [ 0.171572875253810 ], \
    [ 0.171572875253810 ] ] )

  return lam

def kershaw_inverse ( ):

#*****************************************************************************80
#
## kershaw_inverse() returns the inverse of the KERSHAW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
    [  3.0,  2.0,  0.0, -2.0 ], \
    [  2.0,  3.0,  2.0,  0.0 ], \
    [  0.0,  2.0,  3.0,  2.0 ], \
    [ -2.0,  0.0,  2.0,  3.0 ] ] )

  return a

def kershaw_llt ( ):

#*****************************************************************************80
#
## kershaw_llt() returns the Cholesky factor of the KERSHAW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
  [  1.732050807568877,  0.0,               \
     0.0,                0.0 ],             \
  [ -1.154700538379252,  1.290994448735805, \
     0.0,                0.0 ],             \
  [                0.0, -1.549193338482967, \
     0.774596669241483,  0.0 ],             \
  [  1.154700538379252,  1.032795558988645, \
    -0.516397779494321,  0.577350269189626 ] ] )

  return a

def kershaw_test ( ):

#*****************************************************************************80
#
## kershaw_test() tests kershaw_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'kershaw_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  kershaw_matrix() computes the KERSHAW matrix.' )

  n = 4
  a = kershaw_matrix ( )
  r8mat_print ( n, n, a, '  KERSHAW matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'kershaw_test' )
  print ( '  Normal end of execution.' )
  return

def kershawtri_matrix ( n, x ):

#*****************************************************************************80
#
## kershawtri_matrix() returns the KERSHAWTRI matrix.
#
#  Discussion:
#
#    A(I,I) = X(I)     for I <= (N+1)/2
#    A(I,I) = X(N+1-I) for (N+1)/2 < I
#    A(I,J) = 1        for I = J + 1 or I = J - 1.
#    A(I,J) = 0        otherwise.
#
#  Example:
#
#    N = 5,
#    X = ( 10, 20, 30 )
#    A = 
#      10   1   0   0   0
#       1  20   1   0   0
#       0   1  30   1   0
#       0   0   1  20   1
#       0   0   0   1  10
#
#  Properties:
#
#    A is tridiagonal.
#
#    A is symmetric.
#
#    If the entries in X are integers, then det(A) is an integer.
#
#    If det(A) is an integer, then det(A) * inv(A) is an integer matrix.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    P Schlegel,
#    The Explicit Inverse of a Tridiagonal Matrix,
#    Mathematics of Computation,
#    Volume 24, Number 111, July 1970, page 665.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X((N+1)/2), defines the diagonal of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  nh = ( n // 2 )

  for i in range ( 0, nh ):
    a[i,i]         = x[i]
    a[n-1-i,n-1-i] = x[i]

  if ( ( n % 2 ) == 1 ):
    a[nh,nh] = x[nh]

  for i in range ( 0, n - 1 ):  
    a[i,i+1] = 1.0
    a[i+1,i] = 1.0

  return a

def kershawtri_determinant ( n, x ):

#*****************************************************************************80
#
## kershawtri_determinant() returns the determinant of the KERSHAWTRI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X((N+1)/2), defines the diagonal of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  nh = ( n // 2 )

  r = np.zeros ( n + 1 )

  r[0] = 1.0
  r[1] = - x[0]
  for i in range ( 3, n + 1 ):
    if ( i - 1 <= nh ):
      xim1 = x[i-2]
    else:
      xim1 = x[n+1-i]
    r[i-1] = - ( xim1 * r[i-2] + r[i-3] )

  value = x[0] * r[n-1] + r[n-2]
 
  return value

def kershawtri_inverse ( n, x ):

#*****************************************************************************80
#
## kershawtri_inverse() returns the inverse of the KERSHAWTRI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X((N+1)/2), defines the diagonal of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  nh = ( n // 2 )

  r = np.zeros ( n + 1 )
 
  r[0] = 1.0
  r[1] = - x[0]
  for i in range ( 2, n ):
    if ( i <= nh ):
      xim1 = x[i-1]
    else:
      xim1 = x[n-i]
    r[i] = - ( xim1 * r[i-1] + r[i-2] )
  r[n] = x[0] * r[n-1] + r[n-2]

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      a[i,j] = r[j] * r[n-1-i] / r[n]
    a[i,i] = r[i] * r[n-1-i] / r[n]
    for j in range ( i + 1, n ):
      a[i,j] = r[i] * r[n-1-j] / r[n]

  return a

def kershawtri_test ( ):

#*****************************************************************************80
#
## kershawtri_test() tests kershawtri_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'kershawtri_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  kershawtri_matrix computes the KERSHAWTRI matrix.' )

  n = 5
  x_n = ( ( n + 1 ) // 2 )
  r8_lo = -5.0
  r8_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( x_n )

  a = kershawtri_matrix ( n, x )
  m = n
  r8mat_print ( m, n, a, '  KERSHAWTRI matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'kershawtri_test' )
  print ( '  Normal end of execution.' )
  return

def kms_matrix ( alpha, m, n ):

#*****************************************************************************80
#
## kms_matrix() returns the KMS matrix.
#
#  Formula:
#
#    A(I,J) = ALPHA^abs ( I - J )
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#     1  2  4  8  16
#     2  1  2  4   8
#     4  2  1  2   4
#     8  4  2  1   2
#    16  8  4  2   1
#
#    ALPHA = 1/2, N = 5
#
#     1   1/2  1/4  1/8  1/16
#    1/2   1   1/2  1/4  1/8
#    1/4  1/2   1   1/2  1/4
#    1/8  1/4  1/2   1   1/2
#    1/16 1/8  1/4  1/2   1
#
#  Properties:
#
#    A is Toeplitz: constant along diagonals.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    A has an L*D*L' factorization, with L being the inverse
#    of the transpose of the matrix with 1's on the diagonal and
#    -ALPHA on the superdiagonal and zero elsewhere, and
#    D(I,I) = (1-ALPHA^2) except that D(1,1)=1.
#
#    det ( A ) = ( 1 - ALPHA^2 )^(N-1).
#
#    The inverse of A is tridiagonal.
#
#    A is positive definite if and only if 0 < abs ( ALPHA ) < 1.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Numerical solution of the eigenvalue problem for Hermitian
#    Toeplitz matrices,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, Number 2, April 1989, pages 135-146.
#
#  Input:
#
#    real ALPHA, the scalar that defines A.  
#    A typical value is 0.5.
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( alpha == 0.0 and i == j ):
        a[i,j] = 1.0
      else:
        a[i,j] = alpha ** ( abs ( i - j ) )

  return a

def kms_determinant ( alpha, n ):

#*****************************************************************************80
#
## kms_determinant() returns the determinant of the KMS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the parameter.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  if ( n == 1 ):
    value = 1.0
  else:
    value = ( 1.0 - alpha * alpha ) ** ( n - 1 )

  return value

def kms_eigen_right ( alpha, n ):

#*****************************************************************************80
#
## kms_eigen_right() returns the right eigenvectors of the KMS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Spectral decomposition of Kac-Murdock-Szego matrices,
#    Unpublished technical report.
#
#  Input:
#
#    real ALPHA, the parameter.
#    Eigenvalue computations require 0 <= ALPHA <= 1.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the right eigenvector matrix.
#
  import numpy as np
 
  t = kms_eigenvalues_theta ( alpha, n )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = np.sin ( ( float ) ( i + 1 ) * t[j] ) \
        - alpha * np.sin ( float ( i ) * t[j] )

  return a

def kms_eigenvalues ( alpha, n ):

#*****************************************************************************80
#
## kms_eigenvalues() returns the eigenvalues of the KMS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Spectral decomposition of Kac-Murdock-Szego matrices,
#    Unpublished technical document.
#
#  Input:
#
#    real ALPHA, the scalar that defines A.  
#    Eigenvalue computations require 0 <= ALPHA <= 1.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  theta = kms_eigenvalues_theta ( alpha, n )

  lam = np.zeros ( n )
 
  for i in range ( 0, n ):
    lam[i] = ( 1.0 + alpha ) * ( 1.0 - alpha ) \
      / ( 1.0 - 2.0 * alpha * np.cos ( theta[i] ) + alpha * alpha )

  return lam

def kms_eigenvalues_theta ( alpha, n ):

#*****************************************************************************80
#
## kms_eigenvalues_theta() returns data needed to compute KMS eigenvalues.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Spectral decomposition of Kac-Murdock-Szego matrices,
#    Unpublished technical document.
#
#  Input:
#
#    real ALPHA, the scalar that defines A.  
#    Eigenvalue computations require 0 <= ALPHA <= 1.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real T(N), the angles associated with
#    the eigenvalues.
#
  import numpy as np

  step_max = 100

  t = np.zeros ( n )

  for i in range ( 0, n ):
#
#  Avoid confusion in first subinterval, where f(0) = 0.
#
    if ( i == 0 ):
      xa = 0.0001
    else:
      xa = float ( i ) * np.pi / float ( n + 1 )

    fxa = kms_eigenvalues_theta_f ( alpha, n, xa )
    xb = float ( i + 1 ) * np.pi / float ( n + 1 )
    fxb = kms_eigenvalues_theta_f ( alpha, n, xb )

    if ( 0.0 < fxa ):
      temp = xa
      xa = xb
      xb = temp
      temp = fxa
      fxa = fxb
      fxb = temp

    for step in range ( 0, step_max ):

      xc = 0.5 * ( xa + xb )
      fxc = kms_eigenvalues_theta_f ( alpha, n, xc )
#
#  Return if residual is small.
#
      if ( abs ( fxc ) <= 0.0000001 ):
        break
#
#  Return if interval is small.
#
      if ( abs ( xb - xa ) <= 0.0000001 ):
        break

      if ( fxc < 0.0 ):
        xa = xc
        fxa = fxc
      else:
        xb = xc
        fxb = fxc

    t[i] = xc

  return t

def kms_eigenvalues_theta_f ( alpha, n, t ):

#*****************************************************************************80
#
## kms_eigenvalues_theta_f() evaluates a function for KMS eigenvalues.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Spectral decomposition of Kac-Murdock-Szego matrices,
#    Unpublished technical document.
#
#  Input:
#
#    real ALPHA, the scalar that defines A.  
#    Eigenvalue computations require 0 <= ALPHA <= 1.
#
#    integer N, the order of the matrix.
#
#    real T, an angle associated with the eigenvalue.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  n_r8 = float ( n ) 

  value = np.sin ( ( n_r8 + 1.0 ) * t ) \
    - 2.0 * alpha * np.sin ( n_r8 * t ) \
    + alpha * alpha * np.sin ( ( n_r8 - 1.0 ) * t )

  return value

def kms_inverse ( alpha, n ):

#*****************************************************************************80
#
## kms_inverse() returns the inverse of the KMS matrix.
#
#  Formula:
#
#    if ( I = J )
#      if ( I = 1 )
#        A(I,J) = -1/(ALPHA^2-1)
#      elseif ( I < N )
#        A(I,J) = -(ALPHA^2+1)/(ALPHA^2-1)
#      elseif ( I = N )
#        A(I,J) = -1/(ALPHA^2-1)
#    elseif ( J = I + 1 or I = J + 1 )
#      A(I,J) = ALPHA/(ALPHA^2-1)
#    else
#      A(I,J) = 0 otherwise
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#         -1  2  0  0  0
#          2 -5  2  0  0
#    1/3 * 0  2 -5  2  0
#          0  0  2 -5  2
#          0  0  0  2 -1
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Numerical solution of the eigenvalue problem for Hermitian
#    Toeplitz matrices,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, Number 2, April 1989, pages 135-146.
#
#  Input:
#
#    real ALPHA, the scalar that defines A.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  bot = alpha * alpha - 1.0

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        if ( j == 0 ):
          a[i,j] = - 1.0 / bot
        elif ( j < n - 1 ):
          a[i,j] = - ( alpha * alpha + 1.0 ) / bot
        elif ( j == n - 1 ):
          a[i,j] = -1.0 / bot
      elif ( i == j + 1 or j == i + 1 ):
        a[i,j] = alpha / bot

  return a

def kms_lu ( alpha, n ):

#*****************************************************************************80
#
## kms_lu() returns the LU factors of the KMS matrix.
#
#  Example:
#
#    ALPHA = 0.5, N = 5
#
#    L =
#
#       1    0   0   0   0
#      1/2   1   0   0   0
#      1/4  1/2  1   0   0
#      1/8  1/4 1/2  1   0
#      1/16 1/8 1/4 1/2  1
#
#    U =
#
#       1   1/2  1/4  1/8  1/16
#       0   3/4  3/8  3/16 3/32
#       0    0   3/4  3/8  3/16
#       0    0    0   3/4  3/8
#       0    0    0    0   3/4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Numerical solution of the eigenvalue problem for Hermitian
#    Toeplitz matrices,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, Number 2, April 1989, pages 135-146.
#
#  Input:
#
#    real ALPHA, the scalar that defines A.  
#    A typical value is 0.5.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real L(N,N), U(N,N), the factors.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )

  l[0,0] = 1.0
  for i in range ( 1, n ):
    l[i,0] = alpha * l[i-1,0]

  for j in range ( 1, n ):
    for i in range ( j, n ):
      l[i,j] = l[i-j,0]

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    u[0,j] = l[j,0]
    for i in range ( 1, n ):
      u[i,j] = l[j,i] * ( 1.0 - alpha * alpha )

  return l, u

def kms_plu ( alpha, n ):

#*****************************************************************************80
#
## kms_plu() returns the PLU factors of the KMS matrix.
#
#  Example:
#
#    ALPHA = 0.5, N = 5
#
#    P = Identity matrix
#
#    L =
#
#       1    0   0   0   0
#      1/2   1   0   0   0
#      1/4  1/2  1   0   0
#      1/8  1/4 1/2  1   0
#      1/16 1/8 1/4 1/2  1
#
#    U =
#
#       1   1/2  1/4  1/8  1/16
#       0   3/4  3/8  3/16 3/32
#       0    0   3/4  3/8  3/16
#       0    0    0   3/4  3/8
#       0    0    0    0   3/4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Trench,
#    Numerical solution of the eigenvalue problem for Hermitian
#    Toeplitz matrices,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, Number 2, April 1989, pages 135-146.
#
#  Input:
#
#    real ALPHA, the scalar that defines A.  
#    A typical value is 0.5.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )

  l[0,0] = 1.0
  for i in range ( 1, n ):
    l[i,0] = alpha * l[i-1,0]

  for j in range ( 1, n ):
    for i in range ( j, n ):
      l[i,j] = l[i-j,0]

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    u[0,j] = l[j,0]
    for i in range ( 1, n ):
      u[i,j] = l[j,i] * ( 1.0 - alpha * alpha )

  return p, l, u

def kms_test ( ):

#*****************************************************************************80
#
## kms_test() tests kms_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'kms_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  kms_matrix computes the KMS matrix.' )

  m = 5
  n = 5
  r8_lo = 0.0
  r8_hi = 1.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  a = kms_matrix ( alpha, m, n )
  r8mat_print ( m, n, a, '  KMS matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'kms_test' )
  print ( '  Normal end of execution.' )
  return

def laguerre_matrix ( n ):

#*****************************************************************************80
#
## laguerre_matrix() returns the LAGUERRE matrix.
#
#  Example:
#
#    N = 8
#
#      1      .     .      .    .    .    .    .
#      1     -1     .      .    .    .    .    .
#      2     -4     1      .    .    .    .    .   /    2
#      6    -18     9     -1    .    .    .    .   /    6
#     24    -96    72    -16    1    .    .    .   /   24
#    120   -600   600   -200   25   -1    .    .   /  120
#    720  -4320  5400  -2400  450  -36    1    .   /  720
#   5040 -35280 52920 -29400 7350 -882   49   -1   / 5040
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is lower triangular.
#
#    The columns of A alternate in sign.
#
#    A(I,1) = 1
#    A(I,I) = (-1)^(I-1) / (I-1)!.
#
#    LAMBDA(I) = (-1)^(I-1) / (I-1)!.
#
#    det ( A ) = product ( 1 <= I <= N ) (-1)^(I-1) / (I-1)!
#
#    The I-th row contains the coefficients of the Laguerre
#    polynomial of degree I-1.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,0] = 1.0
    a[1,1] = -1.0

    if ( 2 < n ):

      for i in range ( 3, n + 1 ):
        for j in range ( 0, n ):
          if ( j == 0 ):
            a[i-1,j] = ( float ( 2 * i - 3 ) * a[i-2,j] \
                      +  float (   - i + 2 ) * a[i-3,j] ) \
                      /  float (     i - 1 )
          else:
            a[i-1,j] = ( float ( 2 * i - 3 ) * a[i-2,j] \
                      -  float (         1 ) * a[i-2,j-1] \
                      +  float (   - i + 2 ) * a[i-3,j] ) \
                      /  float (     i - 1 )

  return a

def laguerre_determinant ( n ):

#*****************************************************************************80
#
## laguerre_determinant() returns the determinant of the LAGUERRE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  from scipy.special import factorial

  value = 1.0
  p = + 1.0
  for i in range ( 0, n ):
    value = value * p / factorial ( i )
    p = - p

  return value

def laguerre_inverse ( n ):

#*****************************************************************************80
#
## laguerre_inverse() returns the inverse of the LAGUERRE matrix.
#
#  Example:
#
#    N = 9
#
#        1        .       .        .       .        .       .       .     .
#        1       -1       .        .       .        .       .       .     .
#        2       -4       2        .       .        .       .       .     .
#        6      -18      18       -6       .        .       .       .     .
#       24      -96     144      -96      24        .       .       .     .
#      120     -600    1200    -1200     600     -120       .       .     .
#      720    -4320   10800   -14400   10800    -4320     720       .     .
#     5040   -35280  105840  -176400  176400  -105840   35280   -5040     .
#     40320 -322560 1128960 -2257920 2822400 -2257920 1128960 -322560 40320
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is lower triangular.
#
#    The columns of A alternate in sign.
#
#    A(I,1) = (I-1)!
#    A(I,I) = (I-1)! * ( -1 ) ^ (N+1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,0] = 1.0
    a[1,1] = -1.0

    if ( 2 < n ):
      
      for i in range ( 2, n ):
        for j in range ( 0, n ):

          if ( j == 0 ):
            a[i,j] = float ( i ) * ( a[i-1,j]              )
          else:
            a[i,j] = float ( i ) * ( a[i-1,j] - a[i-1,j-1] )

  return a

def laguerre_test ( ):

#*****************************************************************************80
#
## laguerre_test() tests laguerre_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'laguerre_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  laguerre_matrix() computes the LAGUERRE matrix.' )

  m = 5
  n = m

  a = laguerre_matrix ( n )
 
  r8mat_print ( m, n, a, '  LAGUERRE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'laguerre_test' )
  print ( '  Normal end of execution.' )
  return

def lauchli_matrix ( alpha, m, n ):

#*****************************************************************************80
#
## lauchli_matrix() returns the LAUCHLI matrix.
#
#  Discussion:
#
#    The Lauchli matrix is of order M by N, with M = N + 1.
#
#    This matrix is a well-known example in least squares that indicates
#    the danger of forming the matrix of the normal equations,  A' * A.
#
#    A common value for ALPHA is sqrt(EPS) where EPS is the machine epsilon.
#
#  Formula:
#
#    if ( I = 1 )
#      A(I,J) = 1
#    else if ( I-1 = J )
#      A(I,J) = ALPHA
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 5, N = 4
#    ALPHA = 2
#
#    1  1  1  1
#    2  0  0  0
#    0  2  0  0
#    0  0  2  0
#    0  0  0  2
#
#  Properties:
#
#    The matrix is singular in a simple way.  The first row is
#    equal to the sum of the other rows, divided by ALPHA.
#
#    if ( ALPHA /= 0 )
#      rank ( A ) = N - 1
#    else if ( ALPHA == 0 )
#      rank ( A ) = 1
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Peter Lauchli,
#    Jordan-Elimination und Ausgleichung nach kleinsten Quadraten,
#    (Jordan elimination and smoothing by least squares),
#    Numerische Mathematik,
#    Volume 3, Number 1, December 1961, pages 226-240.
#
#  Input:
#
#    real ALPHA, the scalar defining the matrix.
#
#    integer M, N, the order of A.  It should be the case
#    that M = N + 1.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
 
      if ( i == 0 ):
        a[i,j] = 1.0
      elif ( i == j + 1 ):
        a[i,j] = alpha

  return a

def lauchli_null_left ( alpha, m, n ):

#*****************************************************************************80
#
## lauchli_null_left() returns a left null vector of the LAUCHLI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining the matrix.
#
#    integer M, N, the order of A.
#    It should be the case that M = N + 1.
#
#  Output:
#
#    real X(M), the vector.
#
  import numpy as np

  x = np.zeros ( m )

  x[0] = - alpha
  for i in range ( 1, m ):
    x[i] = 1.0

  return x

def lauchli_test ( ):

#*****************************************************************************80
#
## lauchli_test() tests lauchli_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'lauchli_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  lauchli_matrix() computes the LAUCHLI matrix.' )

  m = 5
  n = m - 1
  alpha = np.random.rand ( )
  a = lauchli_matrix ( alpha, m, n )
  r8mat_print ( m, n, a, '  LAUCHLI matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'lauchli_test' )
  print ( '  Normal end of execution.' )
  return

def legendre_matrix ( n ):

#*****************************************************************************80
#
## legendre_matrix() returns the LEGENDRE matrix.
#
#  Example:
#
#    N = 11
#
#     1    .     .     .      .     .      .      .       .     .     . / 1
#     .    1     .     .      .     .      .      .       .     .     . / 1
#    -1    .     3     .      .     .      .      .       .     .     . / 2
#     .   -3     .     5      .     .      .      .       .     .     . / 2
#     3    .   -30     .     35     .      .      .       .     .     . / 8
#     .   15     .   -70      .    63      .      .       .     .     . / 8
#    -5    .   105     .   -315     .    231      .       .     .     . / 16
#     .  -35     .   315      .  -693      .    429       .     .     . / 16
#    35    . -1260     .   6930     . -12012      .    6435     .     . / 128
#     .  315     . -4620      . 18018      . -25740       . 12155     . / 128
#   -63    .  3465     . -30030     .  90090      . -109395     . 46189 / 256
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is lower triangular.
#
#    The elements of each row sum to 1.
#
#    Because it has a constant row sum of 1,
#    A has an eigenvalue of 1, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A is reducible.
#
#    The diagonals form a pattern of zero, positive, zero, negative.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,1] = 1.0

    if ( 2 < n ):

      for i in range ( 2, n ):
        for j in range ( 0, n ):
          if ( j == 0 ):
            a[i,j] = - ( i - 1 ) * a[i-2,j] \
                     / float ( i )
          else:
            a[i,j] = ( ( 2 * i - 1 ) * a[i-1,j-1] \
                     + (   - i + 1 ) * a[i-2,j] ) \
                     / float (     i     )

  return a

def legendre_determinant ( n ):

#*****************************************************************************80
#
## legendre_determinant() returns the determinant of the LEGENDRE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0
  t = 1.0

  for i in range ( 3, n + 1 ):
    t = t * float ( 2 * i - 3 ) / float (  i - 1 )
    value = value * t

  return value

def legendre_inverse ( n ):

#*****************************************************************************80
#
## legendre_inverse() returns the inverse of the LEGENDRE matrix.
#
#  Example:
#
#    N = 11
#
#       1    .     .    .     .    .    .   .    .   .   .
#       .    1     .    .     .    .    .   .    .   .   .
#       1    .     2    .     .    .    .   .    .   .   . /     3
#       .    3     .    2     .    .    .   .    .   .   . /     5
#       7    .    20    .     8    .    .   .    .   .   . /    35
#       .   27     .   28     .    8    .   .    .   .   . /    63
#      33    .   110    .    72    .   16   .    .   .   . /   231
#       .  143     .  182     .   88    .  16    .   .   . /   429
#     715    .  2600    .  2160    .  832   .  128   .   . /  6435
#       . 3315     . 4760     . 2992    . 960    . 128   . / 12155
#    4199    . 16150    . 15504    . 7904   . 2176   . 256 / 46189
#
#  Properties:
#
#    A is nonnegative.
#
#    The elements of each row sum to 1.
#
#    Because it has a constant row sum of 1,
#    A has an eigenvalue of 1, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A is lower triangular.
#
#    A is reducible.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,1] = 1.0

    if ( 2 < n ):

      for i in range ( 2, n ):
        for j in range ( 0, n ):

          if ( j == 0 ):

            a[i,j] = (     j + 1 ) * a[i-1,j+1] / float ( 2 * j + 3 )

          elif ( j < n - 1 ):

            a[i,j] = (     j     ) * a[i-1,j-1] / float ( 2 * j - 1 ) \
                   + (     j + 1 ) * a[i-1,j+1] / float ( 2 * j + 3 )

          else:

            a[i,j] = (     j     ) * a[i-1,j-1] / float ( 2 * j - 1 )

  return a

def legendre_test ( ):

#*****************************************************************************80
#
## legendre_test() tests legendre_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'legendre_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  legendre_matrix() computes the LEGENDRE matrix.' )

  m = 5
  n = m

  a = legendre_matrix ( n )
 
  r8mat_print ( m, n, a, '  LEGENDRE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'legendre_test' )
  print ( '  Normal end of execution.' )
  return

def legendre_symbol ( q, p ):

#*****************************************************************************80
#
## legendre_symbol() evaluates the Legendre symbol (Q/P).
#
#  Definition:
#
#    Let P be an odd prime.  Q is a QUADRATIC RESIDUE modulo P
#    if there is an integer R such that R^2 = Q ( mod P ).
#    The Legendre symbol ( Q / P ) is defined to be:
#
#      + 1 if Q ( mod P ) /= 0 and Q is a quadratic residue modulo P,
#      - 1 if Q ( mod P ) /= 0 and Q is not a quadratic residue modulo P,
#        0 if Q ( mod P ) == 0.
#
#    We can also define ( Q / P ) for P = 2 by:
#
#      + 1 if Q ( mod P ) /= 0
#        0 if Q ( mod P ) == 0
#
#  Example:
#
#    (0/7) =   0
#    (1/7) = + 1  ( 1^2 = 1 mod 7 )
#    (2/7) = + 1  ( 3^2 = 2 mod 7 )
#    (3/7) = - 1
#    (4/7) = + 1  ( 2^2 = 4 mod 7 )
#    (5/7) = - 1
#    (6/7) = - 1
#
#  Note:
#
#    For any prime P, exactly half of the integers from 1 to P-1
#    are quadratic residues.
#
#    ( 0 / P ) = 0.
#
#    ( Q / P ) = ( mod ( Q, P ) / P ).
#
#    ( Q / P ) = ( Q1 / P ) * ( Q2 / P ) if Q = Q1 * Q2.
#
#    If Q is prime, and P is prime and greater than 2, then:
#
#      if ( Q == 1 ) then
#
#        ( Q / P ) = 1
#
#      else if ( Q == 2 ) then
#
#        ( Q / P ) = + 1 if mod ( P, 8 ) = 1 or mod ( P, 8 ) = 7,
#        ( Q / P ) = - 1 if mod ( P, 8 ) = 3 or mod ( P, 8 ) = 5.
#
#      else
#
#        ( Q / P ) = - ( P / Q ) if Q = 3 ( mod 4 ) and P = 3 ( mod 4 ),
#                  =   ( P / Q ) otherwise.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Pinter,
#    A Book of Abstract Algebra,
#    McGraw Hill, 1982, pages 236-237.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, pages 86-87.
#
#  Input:
#
#    integer Q, an integer whose Legendre symbol with
#    respect to P is desired.
#
#    integer P, a prime number, greater than 1, with respect
#    to which the Legendre symbol of Q is desired.
#
#  Output:
#
#    integer L, the Legendre symbol (Q/P).
#    Ordinarily, L will be -1, 0 or 1.
#    L = -2, P is less than or equal to 1.
#    L = -3, P is not prime.
#    L = -4, the internal stack of factors overflowed.
#    L = -5, not enough factorization space.
#
  import numpy as np

  l = 0
#
#  P must be greater than 1.
#
  if ( p <= 1 ):
    print ( '' )
    print ( 'legendre_symbol - Fatal error!' )
    print ( '  P must be greater than 1.' )
    l = -2
    raise Exception ( 'legendre_symbol - Fatal error!' )
#
#  P must be prime.
#
  if ( not ( i4_is_prime ( p ) ) ):
    print ( '' )
    print ( 'legendre_symbol - Fatal error!' )
    print ( '  P is not prime.' )
    l = -3
    raise Exception ( 'legendre_symbol - Fatal error!' )
#
#  ( k*P / P ) = 0.
#
  if ( ( q % p ) == 0 ):
    l = 0
    return l
#
#  For the special case P = 2, (Q/P) = 1 for all odd numbers.
#
  if ( p == 2 ):
    l = 1
    return l

#
#  Make a copy of Q, and force it to be nonnegative.
#
  qq = q

  while ( qq < 0 ):
    qq = qq + p

  nstack = 0
  pstack = np.zeros ( 100 )
  qstack = np.zeros ( 100 )
  pp = p
  l = 1

  while ( True ):

    qq = ( qq % pp )
#
#  Decompose QQ into factors of prime powers.
#
    nfactor, factor, power, nleft = i4_factor ( qq )

    if ( nleft != 1 ):
      print ( '' )
      print ( 'legendre_symbol - Fatal error!' )
      print ( '  Not enough factorization space.' )
      raise Exception ( 'legendre_symbol - Fatal error!' )
#
#  Each factor which is an odd power is added to the stack.
#
    nmore = 0

    for i in range ( 0, nfactor ):

      if ( ( power[i] % 2 ) == 1 ):

        nmore = nmore + 1
        pstack[nstack] = pp
        qstack[nstack] = factor[i]
        nstack = nstack + 1

    hop = False

    if ( nmore != 0 ):

      nstack = nstack - 1
      qq = qstack[nstack]
#
#  Check for a QQ of 1 or 2.
#
      if ( qq == 1 ):

        l = + 1 * l

      elif ( qq == 2 and ( ( pp % 8 ) == 1 or ( pp % 8 ) == 7 ) ):

        l = + 1 * l

      elif ( qq == 2 and ( ( pp % 8 ) == 3 or ( pp % 8 ) == 5 ) ):

        l = - 1 * l

      else:

        if ( ( pp % 4 ) == 3 and ( qq % 4 ) == 3 ):
          l = - 1 * l

        rr = pp
        pp = qq
        qq = rr

        hop = True
#
#  If the stack is empty, we're done.
#
    if ( not hop ):

      if ( nstack == 0 ):
        break
#
#  Otherwise, get the last P and Q from the stack, and process them.
#
      nstack = nstack - 1
      pp = pstack[nstack]
      qq = qstack[nstack]

  return l

def legendre_symbol_test ( ):

#*****************************************************************************80
#
## legendre_symbol_test() tests legendre_symbol().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  ntest = 4
  ptest = [ 7, 11, 13, 17 ]

  print ( '' )
  print ( 'legendre_symbol_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  legendre_symbol computes the Legendre' )
  print ( '  symbol (Q/P) which records whether Q is' )
  print ( '  a quadratic residue modulo the prime P.' )

  for i in range ( 0, ntest ):
    p = ptest[i]
    print ( '' )
    print ( '  Legendre Symbols for P = %d' % ( p ) )
    print ( '' )
    for q in range ( 0, p + 1 ):
      l = legendre_symbol ( q, p )
      print ( '  %6d  %6d  %6d' % ( p, q, l ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'legendre_symbol_test():' )
  print ( '  Normal end of execution.' )
  return

def legendre_zeros ( n ):

#*****************************************************************************80
#
## legendre_zeros() returns the zeros of the Legendre polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the degree of the polynomial.
#
#  Output:
#
#    real X(N), the zeros of the polynomial.
#
  import numpy as np

  x = np.zeros ( n )

  e1 = float ( n * ( n + 1 ) )

  m = ( n + 1 ) // 2

  for i in range ( 1, m + 1 ):

    t = float ( 4 * i - 1 ) * np.pi / float ( 4 * n + 2 )
    x0 = np.cos ( t ) * ( 1.0 - ( 1.0 - 1.0 / float ( n ) ) / float ( 8 * n * n ) )

    pkm1 = 1.0
    pk = x0

    for k in range ( 2, n + 1 ):
      pkp1 = 2.0 * x0 * pk - pkm1 - ( x0 * pk - pkm1 ) / float ( k )
      pkm1 = pk
      pk = pkp1

    d1 = float ( n ) * ( pkm1 - x0 * pk )

    dpn = d1 / ( 1.0 - x0 * x0 )

    d2pn = ( 2.0 * x0 * dpn - e1 * pk ) / ( 1.0 - x0 * x0 )

    d3pn = ( 4.0 * x0 * d2pn + ( 2.0 - e1 ) * dpn ) / ( 1.0 - x0 * x0 )

    d4pn = ( 6.0 * x0 * d3pn + ( 6.0 - e1 ) * d2pn ) / ( 1.0 - x0 * x0 )

    u = pk / dpn
    v = d2pn / dpn
#
#  Initial approximation H:
#
    h = - u * ( 1.0 + 0.5 * u * ( v + u * ( v * v - d3pn / ( 3.0 * dpn ) ) ) )
#
#  Refine H using one step of Newton's method:
#
    p = pk + h * ( dpn + 0.5 * h * ( d2pn + h / 3.0 \
      * ( d3pn + 0.25 * h * d4pn ) ) )

    dp = dpn + h * ( d2pn + 0.5 * h * ( d3pn + h * d4pn / 3.0 ) )

    h = h - p / dp

    xtemp = x0 + h

    x[n-i] =   xtemp
    x[i-1] = - xtemp

    fx = d1 - h * e1 * ( pk + 0.5 * h * ( dpn + h / 3.0 \
      * ( d2pn + 0.25 * h * ( d3pn + 0.2 * h * d4pn ) ) ) )

  if ( ( n % 2 ) == 1 ):
    x[m-1] = 0.0

  return x

def legendre_zeros_test ( ):

#*****************************************************************************80
#
## legendre_zeros_test() tests legendre_zeros().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'legendre_zeros_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  legendre_zeros computes the zeros of the N-th Legendre polynomial.' )

  for n in range ( 1, 8 ):
    l = legendre_zeros ( n )
    r8vec_print ( n, l, '  Legendre zeros:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'legendre_zeros_test' )
  print ( '  Normal end of execution.' )
  return

def lehmer_matrix ( m, n ):

#*****************************************************************************80
#
## lehmer_matrix() returns the LEHMER matrix.
#
#  Discussion:
#
#    This matrix is also known as the "Westlake" matrix.
#
#  Formula:
#
#    A(I,J) = min ( I, J ) / max ( I, J )
#
#  Example:
#
#    N = 5
#
#    1/1  1/2  1/3  1/4  1/5
#    1/2  2/2  2/3  2/4  2/5
#    1/3  2/3  3/3  3/4  3/5
#    1/4  2/4  3/4  4/4  4/5
#    1/5  2/5  3/5  4/5  5/5
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is positive definite.
#
#    A is totally nonnegative.
#
#    The inverse of A is tridiagonal.
#
#    The condition number of A lies between N and 4*N*N.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Morris Newman, John Todd,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, 1958, pages 466-476.
#
#    Solutions to problem E710, proposed by DH Lehmer: The inverse of
#    a matrix.
#    American Mathematical Monthly,
#    Volume 53, Number 9, November 1946, pages 534-535.
#
#    John Todd,
#    Basic Numerical Mathematics, Volume 2: Numerical Algebra,
#    Academic Press, 1977, page 154.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = float ( min ( i + 1, j + 1 ) ) / float ( max ( i + 1, j + 1 ) )

  return a

def lehmer_determinant ( n ):

#*****************************************************************************80
#
## lehmer_determinant() returns the determinant of the LEHMER matrix.
#
#  Formula:
#
#    determinant = (2n)! / 2^n / (n!)^3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Emrah Kilic, Pantelimon Stanica,
#    The Lehmer matrix and its recursive analogue,
#    Journal of Combinatorial Mathematics and Combinatorial Computing,
#    Volume 74, August 2010, pages 193-205.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0
  for i in range ( 0, n ):
    value = value * float ( n + i + 1 ) / float ( 2 * ( i + 1 ) ** 2 )

  return value

def lehmer_inverse ( n ):

#*****************************************************************************80
#
## lehmer_inverse() returns the inverse of the LEHMER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n - 1 ):
    ip1 = float ( i + 1 )
    a[i,i] = ( 4.0 * ip1 * ip1 * ip1 ) / ( 4.0 * ip1 * ip1 - 1.0 )

  a[n-1,n-1] = float ( n * n ) / float ( 2 * n - 1 )

  for i in range ( 0, n - 1 ):
    ip1 = float ( i + 1 )
    a[i,i+1] = - ( ip1 * ( ip1 + 1.0 ) ) / ( 2.0 * ip1 + 1.0 )
    a[i+1,i] = - ( ip1 * ( ip1 + 1.0 ) ) / ( 2.0 * ip1 + 1.0 )

  return a

def lehmer_llt ( n ):

#*****************************************************************************80
#
## lehmer_llt() returns the Cholesky factor of the LEHMER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Emrah Kilic, Pantelimon Stanica,
#    The Lehmer matrix and its recursive analogue,
#    Journal of Combinatorial Mathematics and Combinatorial Computing,
#    Volume 74, August 2010, pages 193-205.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( j, n ):
      a[i,j] = np.sqrt ( float ( 2 * j + 1 ) ) / float ( i + 1 )

  return a

def lehmer_lu ( n ):

#*****************************************************************************80
#
## lehmer_lu() returns the LU factors of the LEHMER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Emrah Kilic, Pantelimon Stanica,
#    The Lehmer matrix and its recursive analogue,
#    Journal of Combinatorial Mathematics and Combinatorial Computing,
#    Volume 74, August 2010, pages 193-205.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real L(N,N), U(N,N), the factors.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    l[j,j] = 1.0
    for i in range ( j + 1, n ):
      l[i,j] = float ( j + 1 ) / float  ( i + 1 )

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      u[i,j] = float ( 2 * i + 1 ) / float  ( ( i + 1 ) * ( j + 1 ) )

  return l, u

def lehmer_plu ( n ):

#*****************************************************************************80
#
## lehmer_plu() returns the PLU factors of the LEHMER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Emrah Kilic, Pantelimon Stanica,
#    The Lehmer matrix and its recursive analogue,
#    Journal of Combinatorial Mathematics and Combinatorial Computing,
#    Volume 74, August 2010, pages 193-205.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    l[j,j] = 1.0
    for i in range ( j + 1, n ):
      l[i,j] = float ( j + 1 ) / float  ( i + 1 )

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      u[i,j] = float ( 2 * i + 1 ) / float  ( ( i + 1 ) * ( j + 1 ) )

  return p, l, u

def lehmer_test ( ):

#*****************************************************************************80
#
## lehmer_test() tests lehmer_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'lehmer_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  lehmer_matrix() computes the LEHMER matrix.' )

  m = 5
  n = 5
  a = lehmer_matrix ( m, n )
  r8mat_print ( m, n, a, '  LEHMER matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'lehmer_test' )
  print ( '  Normal end of execution.' )
  return

def leslie_matrix ( b, di, da ):

#*****************************************************************************80
#
## leslie_matrix() returns the LESLIE matrix.
#
#  Formula:
#
#    5/6 * ( 1.0 - DI )    0      B         0
#    1/6 * ( 1.0 - DI )  13/14    0         0
#        0                1/14  39/40       0
#        0                 0     1/40  9/10 * ( 1 - DA )
#
#  Discussion:
#
#    A human population is assumed to be grouped into the categories:
#
#      X(1) = between  0 and  5+
#      X(2) = between  6 and 19+
#      X(3) = between 20 and 59+
#      X(4) = between 60 and 69+
#
#    Humans older than 69 are ignored.  Deaths occur in the 60 to 69
#    year bracket at a relative rate of DA per year, and in the 0 to 5
#    year bracket at a relative rate of DI per year.  Deaths do not occurr
#    in the other two brackets.
#
#    Births occur at a rate of B relative to the population in the
#    20 to 59 year bracket.
#
#    Thus, given the population vector X in a given year, the population
#    in the next year will be A * X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ke Chen, Peter Giblin, Alan Irving,
#    Mathematical Explorations with MATLAB,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-63920-4.
#
#  Input:
#
#    real B, DI, DA, the birth rate, infant mortality rate,
#    and aged mortality rate.  These should be positive values.
#    The mortality rates must be between 0.0 and 1.0.  Reasonable
#    values might be B = 0.025, DI = 0.010, and DA = 0.100
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  if ( b < 0.0 ):
    print ( '' )
    print ( 'leslie_matrix - Fatal error!' )
    print ( '  0 <= B is required.' )
 
  if ( da < 0.0 or 1.0 < da ):
    print ( '' )
    print ( 'leslie_matrix - Fatal error!' )
    print ( '  0 <= DA <= 1.0 is required.' )

  if ( di < 0.0 or 1.0 < di ):
    print ( '' )
    print ( 'leslie_matrix - Fatal error!' )
    print ( '  0 <= DI <= 1.0 is required.' )

  a = np.zeros ( ( 4, 4, ) )

  a[0,0] = 5.0 * ( 1.0 - di ) / 6.0
  a[0,1] = 0.0
  a[0,2] = b
  a[0,3] = 0.0

  a[1,0] = ( 1.0 - di ) / 6.0
  a[1,1] = 13.0 / 14.0
  a[1,2] = 0.0
  a[1,3] = 0.0

  a[2,0] = 0.0
  a[2,1] = 1.0 / 14.0
  a[2,2] = 39.0 / 40.0
  a[2,3] = 0.0

  a[3,0] = 0.0
  a[3,1] = 0.0
  a[3,2] = 1.0 / 40.0
  a[3,3] = 9.0 * ( 1.0 - da ) / 10.0

  return a

def leslie_determinant ( b, di, da ):

#*****************************************************************************80
#
## leslie_determinant() returns the determinant of the LESLIE matrix.
#
#  Discussion:
#
#    DETERM = a(4,4) * ( 
#        a(1,1) * a(2,2) * a(3,3)
#      + a(1,3) * a(2,1) * a(3,2) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real B, DI, DA, the birth rate, infant mortality rate,
#    and aged mortality rate.  These should be positive values.
#    The mortality rates must be between 0.0 and 1.0.  Reasonable
#    values might be B = 0.025, DI = 0.010, and DA = 0.100
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 9.0 * ( 1.0 - da ) / 10.0 * \
  ( \
      5.0 * ( 1.0 - di ) / 6.0 \
    * 13.0 / 14.0 \
    * 39.0 / 40.0 \
  +   b \
    * ( 1.0 - di ) / 6.0 \
    * 1.0 / 14.0 \
   )

  return value

def leslie_test ( ):

#*****************************************************************************80
#
## leslie_test() tests leslie_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'leslie_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  leslie_matrix() computes the LESLIE matrix.' )

  m = 4
  n = m

  b =  0.025
  di = 0.010
  da = 0.100

  a = leslie_matrix ( b, di, da )
 
  r8mat_print ( m, n, a, '  LESLIE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'leslie_test' )
  print ( '  Normal end of execution.' )
  return

def lesp_matrix ( m, n ):

#*****************************************************************************80
#
## lesp_matrix() returns the LESP matrix.
#
#  Formula:
#
#    if ( I - J == 1 )
#      A(I,J) = 1 / I
#    else if ( I - J == 0 )
#      A(I,J) = - ( 2*I+3 )
#    else if ( I - J == 1 )
#      A(I,J) = J
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    M = 5, N = 5
#
#     -5    2    .    .     .
#     1/2  -7    3    .     .
#      .   1/3  -9    4     .
#      .    .   1/4 -11     5
#      .    .    .   1/5  -13
#
#
#  Properties:
#
#    The matrix is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is generally not symmetric: A' /= A.
#
#    The eigenvalues are real, and smoothly distributed in [-2*N-3.5, -4.5].
#
#    The eigenvalues are sensitive.
#
#    The matrix is similar to the symmetric tridiagonal matrix with
#    the same diagonal entries and with off-diagonal entries 1,
#    via a similarity transformation using the diagonal matrix
#    D = diagonal ( 1!, 2!, ..., N! ).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Wim Lenferink, MN Spijker,
#    On the use of stability regions in the numerical analysis of initial
#    value problems,
#    Mathematics of Computation,
#    Volume 57, 1991, pages 221-237.
#
#    Lloyd Trefethen,
#    Pseudospectra of matrices,
#    in Numerical Analysis 1991,
#    Proceedings of the 14th Dundee Conference,
#    D F Griffiths and G A Watson, editors,
#    Pitman Research Notes in Mathematics, volume 260,
#    Longman Scientific and Technical, Essex, UK, 1992, pages 234-266.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( i - j == 1 ):
        a[i,j] = 1.0 / float ( i + 1 )
      elif ( i - j == 0 ):
        a[i,j] = - float ( 2 * i + 5 )
      elif ( i - j == -1 ):
        a[i,j] = float ( j + 1 )

  return a

def lesp_determinant ( n ):

#*****************************************************************************80
#
## lesp_determinant() returns the determinant of the LESP matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  determ_nm1 = - float ( 2 * n + 3 )
  value = determ_nm1

  if ( 1 < n ):
 
    determ_nm2 = determ_nm1
    determ_nm1 = float ( ( 2 * n + 1 ) * ( 2 * n + 3 ) - 1 )
    value = determ_nm1

    if ( 2 < n ):
 
      for i in range ( n - 2, 0, -1 ):

        determ = - float ( 2 * i + 3 ) * determ_nm1 - determ_nm2
  
        determ_nm2 = determ_nm1
        determ_nm1 = determ

      value = determ

  return value

def lesp_inverse ( n ):

#*****************************************************************************80
#
## lesp_inverse() returns the inverse of the LESP matrix.
#
#  Discussion:
#
#    This computation is an application of the triv_inverse function.
#
#  Example:
#
#    N = 5
#   -0.2060   -0.0598   -0.0201   -0.0074   -0.0028
#   -0.0150   -0.1495   -0.0504   -0.0184   -0.0071
#   -0.0006   -0.0056   -0.1141   -0.0418   -0.0161
#   -0.0000   -0.0001   -0.0026   -0.0925   -0.0356
#   -0.0000   -0.0000   -0.0000   -0.0014   -0.0775
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    CM daFonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the inverse of the matrix.
#
  import numpy as np

  x = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    x[i] = 1.0 / float ( i + 2 )
 
  y = np.zeros ( n )
  for i in range ( 0, n ):
    y[i] = float ( - 2 * i - 5 )

  z = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    z[i] = float ( i + 2 )

  a = triv_inverse ( n, x, y, z )

  return a

def lesp_test ( ):

#*****************************************************************************80
#
## lesp_test() tests lesp_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'lesp_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  lesp_matrix() computes the LESP matrix.' )

  m = 5
  n = m

  a = lesp_matrix ( m, n )
  r8mat_print ( m, n, a, '  LESP matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'lesp_test' )
  print ( '  Normal end of execution.' )
  return

def lietzke_matrix ( n ):

#*****************************************************************************80
#
## lietzke_matrix() returns the LIETZKE matrix.
#
#  Formula:
#
#    A(I,J) = N - abs ( I - J )
#
#  Example:
#
#    N = 5
#
#     5  4  3  2  1
#     4  5  4  3  2
#     3  4  5  4  3
#     2  3  4  5  4
#     1  2  3  4  5
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    M Lietzke, R Stoughton, Marjorie Lietzke,
#    A Comparison of Several Methods for Inverting Large Symmetric
#    Positive Definite Matrices,
#    Mathematics of Computation,
#    Volume 18, Number 87, pages 449-456.
#
#  Input:
#
#    integer N, the number of rows and columns.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = float ( n - abs ( i - j ) )

  return a

def lietzke_condition ( n ):

#*****************************************************************************80
#
## lietzke_condition() returns the L1 condition of the LIETZKE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  s = 0
  k = n
  for i in range ( 0, n ):
    s = s + k
    if ( ( i % 2 ) == 0 ):
      k = k - 1
  a_norm = float ( s )
  if ( n == 1 ):
    b_norm = 0.25
  elif ( n == 2 ):
    b_norm = 5.0 / 6.0
  else:
    b_norm = 2.0

  value = a_norm * b_norm
    
  return value

def lietzke_determinant ( n ):

#*****************************************************************************80
#
## lietzke_determinant() returns the determinant of the LIETZKE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = float ( n + 1 ) * 2.0 ** ( n - 2 )

  return value

def lietzke_inverse ( n ):

#*****************************************************************************80
#
## lietzke_inverse() returns the inverse of the LIETZKE matrix.
#
#  Example:
#
#    N = 5
#
#   0.5833   -0.5000         0         0    0.0833
#  -0.5000    1.0000   -0.5000         0         0
#        0   -0.5000    1.0000   -0.5000         0
#        0         0   -0.5000    1.0000   -0.5000
#   0.0833         0         0   -0.5000    0.5833
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns 
#    of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = float ( n + 2 ) / float ( 2 * n + 2 )
  for i in range ( 1, n - 1 ):
    a[i,i] = 1.0
  a[n-1,n-1] = float ( n + 2 ) / float ( 2 * n + 2 )

  if ( n == 2 ):

    for i in range ( 0, n - 1 ):
      a[i,i+1] = - 1.0 / 3.0

    for i in range ( 1, n ):
      a[i,i-1] = - 1.0 / 3.0

  else:

    for i in range ( 0, n - 1 ):
      a[i,i+1] = - 0.5

    for i in range ( 1, n ):
      a[i,i-1] = - 0.5

  a[0,n-1] = 1.0 / float ( 2 * n + 2 )
  a[n-1,0] = 1.0 / float ( 2 * n + 2 )

  return a

def lietzke_test ( ):

#*****************************************************************************80
#
## lietzke_test() tests lietzke_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'lietzke_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  lietzke_matrix() computes the LIETZKE matrix.' )

  m = 5
  n = m

  a = lietzke_matrix ( n )
 
  r8mat_print ( m, n, a, '  LIETZKE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'lietzke_test' )
  print ( '  Normal end of execution.' )
  return

def line_adj_matrix ( n ):

#*****************************************************************************80
#
## line_adj_matrix() returns the LINE_adj matrix.
#
#  Discussion:
#
#    This is the adjacency matrix for a line of points.
#
#  Example:
#
#    N = 5
#
#    0  1  0  0  0
#    1  0  1  0  0
#    0  1  0  1  0
#    0  0  1  0  1
#    0  0  0  1  0
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is an adjacency matrix for a set of points arranged in a line.
#
#    A has a zero diagonal.
#
#    A is a zero/one matrix.
#
#    The row and column sums are all 2, except for the first and last
#    rows and columns which have a sum of 1.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( j == i - 1 ):
        a[i,j] = 1.0
      elif ( j == i + 1 ):
        a[i,j] = 1.0

  return a

def line_adj_determinant ( n ):

#*****************************************************************************80
#
## line_adj_determinant() returns the determinant of the LINE_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  if ( ( n % 4 ) == 1 ):
    value =   0.0
  elif ( ( n % 4 ) == 2 ):
    value = - 1.0
  elif ( ( n % 4 ) == 3 ):
    value =   0.0
  elif ( ( n % 4 ) == 0 ):
    value = + 1.0

  return value

def line_adj_eigen_right ( n ):

#*****************************************************************************80
#
## line_adj_eigen_right() returns the right eigenvectors of the LINE_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the right eigenvector matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( ( i + 1 ) *  ( j + 1 ) ) * np.pi / float ( n + 1 )
      a[i,j] = np.sqrt ( 2.0 / float ( n + 1 ) ) * np.sin ( angle )

  return a

def line_adj_eigenvalues ( n ):

#*****************************************************************************80
#
## line_adj_eigenvalues() returns the eigenvalues of the LINE_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    lam[i] = 2.0 * np.cos ( angle )

  return lam

def line_adj_inverse ( n ):

#*****************************************************************************80
#
## line_adj_inverse() returns the inverse of the LINE_adj matrix.
#
#  Example:
#
#    N = 6:
#
#     0     1     0    -1     0     1
#     1     0     0     0     0     0
#     0     0     0     1     0    -1
#    -1     0     1     0     0     0
#     0     0     0     0     0     1
#     1     0    -1     0     1     0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( ( n % 2 ) == 1 ):
    print ( '' )
    print ( 'line_adj_inverse - Fatal error!' )
    print ( '  The matrix is singular for odd N.' )
    raise Exception ( 'line_adj_inverse - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):

      for j in range ( i, n - 1, 2 ):

        if ( j == i ):
          p = 1.0
        else:
          p = - p

        a[i,j+1] = p
        a[j+1,i] = p

  return a

def line_adj_null_left ( m, n ):

#*****************************************************************************80
#
## line_adj_null_left() returns a left null vector of the LINE_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(M), the vector
#
  import numpy as np

  if ( ( m % 2 ) == 0 ):
    print ( '' )
    print ( 'line_adj_null_left - Fatal error!' )
    print ( '  For M even, there is no null vector.' )
    raise Exception ( 'line_adj_null_left - Fatal error!' )

  x = np.zeros ( m )
  s = 1.0

  for i in range ( 0, m, 2 ):
    x[i] = s
    s = -s

  return x

def line_adj_null_right ( m, n ):

#*****************************************************************************80
#
## line_adj_null_right() returns a right null vector of the LINE_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(N), the vector
#
  import numpy as np

  if ( ( n % 2 ) == 0 ):
    print ( '' )
    print ( 'line_adj_null_right - Fatal error!' )
    print ( '  For N even, there is no null vector.' )
    raise Exception ( 'line_adj_null_right - Fatal error!' )

  x = np.zeros ( n )
  s = 1.0

  for i in range ( 0, n, 2 ):
    x[i] = s
    s = -s

  return x

def line_adj_test ( ):

#*****************************************************************************80
#
## line_adj_test() tests line_adj_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'line_adj_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  line_adj_matrix() computes the LINE_adj matrix.' )

  m = 5
  n = m

  a = line_adj_matrix ( n )
 
  r8mat_print ( m, n, a, '  LINE_adj matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'line_adj_test' )
  print ( '  Normal end of execution.' )
  return

def line_loop_adj_matrix ( n ):

#*****************************************************************************80
#
## line_loop_adj_matrix() returns the LINE_lOOP_adj matrix.
#
#  Discussion:
#
#    LINE_lOOP_adj is the line loop adjacency matrix.
#
#  Example:
#
#    N = 5
#
#    1  1  0  0  0
#    1  1  1  0  0
#    0  1  1  1  0
#    0  0  1  1  1
#    0  0  0  1  1
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is an adjacency matrix for a set of points arranged in a line.
#
#    A is a zero/one matrix.
#
#    The row and column sums are all 3, except for the first and last
#    rows and columns which have a sum of 2.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( j == i - 1 ):
        a[i,j] = 1.0
      elif ( j == i ):
        a[i,j] = 1.0
      elif ( j == i + 1 ):
        a[i,j] = 1.0

  return a

def line_loop_adj_determinant ( n ):

#*****************************************************************************80
#
## line_loop_adj_determinant() returns the determinant of the LINE_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  if ( ( n % 2 ) == 1 ):

    value = 0.0

  else:

    value = 1.0

    for i in range ( 1, n + 1 ):
      angle = float ( i ) * np.pi / float ( n + 1 )
      value = value * ( 1.0 + 2.0 * np.cos ( angle ) )

  return value

def line_loop_adj_eigen_right ( n ):

#*****************************************************************************80
#
## line_loop_adj_eigen_right(): right eigenvectors of the LINE_lOOP_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the right eigenvector matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( ( i + 1 ) *  ( j + 1 ) ) * np.pi / float ( n + 1 )
      a[i,j] = np.sqrt ( 2.0 / float ( n + 1 ) ) * np.sin ( angle )

  return a

def line_loop_adj_eigenvalues ( n ):

#*****************************************************************************80
#
## line_loop_adj_eigenvalues(): the eigenvalues of the LINE_lOOP_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    lam[i] = 1.0 + 2.0 * np.cos ( angle )

  return lam

def line_loop_adj_test ( ):

#*****************************************************************************80
#
## line_loop_adj_test() tests line_loop_adj_matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'line_loop_adj_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  line_loop_adj_matrix() computes the LINE_lOOP_adj matrix.' )

  m = 5
  n = m

  a = line_loop_adj_matrix ( n )
 
  r8mat_print ( m, n, a, '  LINE_lOOP_adj matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'line_loop_adj_test' )
  print ( '  Normal end of execution.' )
  return

def lotkin_matrix ( m, n ):

#*****************************************************************************80
#
## lotkin_matrix() returns the LOTKIN matrix.
#
#  Formula:
#
#    if ( I = 1 )
#      A(I,J) = 1
#    else
#      A(I,J) = 1 / ( I + J - 1 )
#
#  Example:
#
#    N = 5
#
#     1   1   1   1   1
#    1/2 1/3 1/4 1/5 1/6
#    1/3 1/4 1/5 1/6 1/7
#    1/4 1/5 1/6 1/7 1/8
#    1/5 1/6 1/7 1/8 1/9
#
#  Properties:
#
#    A is the Hilbert matrix with the first row set to all 1's.
#
#    A is generally not symmetric: A' /= A.
#
#    A is ill-conditioned.
#
#    A has many negative eigenvalues of small magnitude.
#
#    The inverse of A has all integer elements, and is known explicitly.
#
#    For N = 6, the eigenvalues are:
#       2.132376,
#      -0.2214068,
#      -0.3184330 D-1,
#      -0.8983233 D-3,
#      -0.1706278 D-4,
#      -0.1394499 D-6.
#
#    det ( A(N) ) = ( -1 )^(N-1) / DELTA(N)
#
#    where
#
#      DELTA(N) = COMB ( 2*N-2, N-2 ) * COMB ( 2*N-2, N-1 )
#        * ( 2*N-1) * DELTA(N-1),
#      DELTA(1) = 1.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.9,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 38,
#    LC: QA263.G68.
#
#    Max Lotkin,
#    A set of test matrices,
#    Mathematics Tables and Other Aids to Computation,
#    Volume 9, 1955, pages 153-161.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( i == 0 ):
        a[i,j] = 1.0
      else:
        a[i,j] = 1.0 / float ( i + j + 1 )

  return a

def lotkin_determinant ( n ):

#*****************************************************************************80
#
## lotkin_determinant() returns the determinant of the LOTKIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  from scipy.special import comb

  delta = 1.0

  for i in range ( 2, n + 1 ):
    delta = - comb ( 2 * i - 2, i - 2 ) * comb ( 2 * i - 2, i - 1 ) \
      * float ( 2 * i - 1 ) * delta

  value = 1.0 / delta

  return value

def lotkin_inverse ( n ):

#*****************************************************************************80
#
## lotkin_inverse() returns the inverse of the LOTKIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from scipy.special import comb
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == 0 ):

        a[i,j] = r8_mop ( n - i - 1 ) \
          * comb ( n + i, i ) \
          * comb ( n, i + 1 )

      else:

        a[i,j] = r8_mop ( i - j + 1 ) * float ( i + 1 ) \
          * comb ( i + j + 1, j ) \
          * comb ( i + j, j - 1 ) \
          * comb ( n + i, i + j + 1 ) \
          * comb ( n + j, i + j + 1 )

  return a

def magic_matrix ( n ):

#*****************************************************************************80
#
## magic_matrix() returns the magic matrix.
#
#  Example:
#
#    N = 5
#
#    17    24     1     8    15
#    23     5     7    14    16
#     4     6    13    20    22
#    10    12    19    21     3
#    11    18    25     2     9
#
#  Properties:
#
#    A is not symmetric.
#
#    The row sums and column sums and diagonal sums of A are n*(n^2+1)/2.
#
#    A has an eigenvalue of n*(n^2+1)/2, with left and right eigenvectors
#    of ( 1, 1, 1, ..., 1 ).
#
#    A is not diagonally dominant.
#
#    A is singular when N is even.  This is because A is a "regular"
#    magic square, for which A(i,j) + A(n-i+1,n-j+1) = n^2+1.
#
#  Modified:
#
#    25 October 2021
#
#  Input:
#
#    integer N: the number of rows and columns of A.  3 <= N.
#
#  Output:
#
#    real A[N,N]: the matrix.
#
  import numpy as np

  n = int ( n )

  if ( n < 3 ):
    raise Exception ( "magic_matrix(): Size n must be at least 3!" )

  if ( n % 2 == 1 ):
    p = np.arange ( 1, n + 1 )
    A = n*np.mod(p[:, None] + p - (n+3)//2, n) + np.mod(p[:, None] + 2*p-2, n) + 1
  elif ( n % 4 == 0 ):
    J = np.mod(np.arange(1, n+1), 4) // 2
    K = J[:, None] == J
    A = np.arange(1, n*n+1, n)[:, None] + np.arange(n)
    A[K] = n*n + 1 - A[K]
  else:
    p = n // 2
    A = magic_matrix ( p )
    A = np.block([[A, A+2*p*p], [A+3*p*p, A+p*p]])
    i = np.arange(p)
    k = (n-2)//4
    j = np.concatenate((np.arange(k), np.arange(n-k+1, n)))
    A[np.ix_(np.concatenate((i, i+p)), j)] = A[np.ix_(np.concatenate((i+p, i)), j)]
    A[np.ix_([k, k+p], [0, k])] = A[np.ix_([k+p, k], [0, k])]

  return A 

def markov_random_matrix ( n, key ):

#*****************************************************************************80
#
## markov_random_matrix() returns a random Markov matrix.
#
#  Discussion:
#
#    A Markov matrix, also called a "stochastic" matrix, is distinguished
#    by two properties:
#
#    * All matrix entries are nonnegative;
#    * The sum of the entries in each row is 1.
#
#    A "transition matrix" is the transpose of a Markov matrix, and
#    has column sums equal to 1.
#
#  Example:
#
#    N = 4
#
#    1/10  2/10  3/10  4/10
#    1     0     0     0
#    5/10  2/10  3/10  0
#    2/10  2/10  2/10  4/10
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    0 <= A(I,J) <= 1.0 for every I and J.
#
#    The sum of the entries in each row of A is 1.
#
#    Because it has a constant row sum of 1,
#    A has an eigenvalue of 1, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    All the eigenvalues of A have modulus no greater than 1.
#
#    The eigenvalue 1 lies on the boundary of all the Gerschgorin rowsum disks.
#
#    A is not diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  np.random.seed ( key )

  a = np.random.rand ( n, n )

  for i in range ( 0, n ):

    row_sum = np.sum ( a[i,0:n] )

    a[i,0:n] = a[i,0:n] / row_sum

  return a

def markov_random_test ( ):

#*****************************************************************************80
#
## markov_random_test() tests markov_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'markov_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  markov_random_matrix() computes the markov_random matrix.' )

  n = 3
  key = 123456789
  a = markov_random_matrix ( n, key )
  r8mat_print ( n, n, a, '  markov_random matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'markov_random_test' )
  print ( '  Normal end of execution.' )
  return

def maxij_matrix ( m, n ):

#*****************************************************************************80
#
## maxij_matrix() returns the MAXIJ matrix.
#
#  Discussion:
#
#    This matrix is occasionally known as the "Boothroyd MAX" matrix.
#
#  Formula:
#
#    A(I,J) = max(I,J)
#
#  Example:
#
#    N = 5
#
#    1 2 3 4 5
#    2 2 3 4 5
#    3 3 3 4 5
#    4 4 4 4 5
#    5 5 5 5 5
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The inverse of A is tridiagonal.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.13,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 42,
#    LC: QA263.G68.
#
#  Input:
#
#    integer M, N, the number of rows and columns 
#    of the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      a[i,j] = float ( max ( i, j ) + 1 )

  return a

def maxij_condition ( n ):

#*****************************************************************************80
#
## maxij_condition() returns the L1 condition of the MAXIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = n * n

  if ( n == 1 ):
    b_norm = 1.0
  elif ( n == 2 ):
    b_norm = 2.0
  else:
    b_norm = 4.0

  value = a_norm * b_norm

  return value

def maxij_determinant ( n ):

#*****************************************************************************80
#
## maxij_determinant() returns the determinant of the MAXIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = float ( n )

  return value

def maxij_inverse ( n ):

#*****************************************************************************80
#
## maxij_inverse() returns the inverse of the MAXIJ matrix.
#
#  Formula:
#
#    if ( I = 1 and J = 1 )
#      A(I,J) = -1
#    else if ( I = N and J = N )
#      A(I,J) = -(N-1)/N
#    else if ( I = J )
#      A(I,J) = -2
#    else if ( J = I-1 or J = I + 1 )
#      A(I,J) =  1
#    else
#      A(I,J) =  0
#
#  Example:
#
#    N = 5
#
#    -1  1  0  0   0
#     1 -2  1  0   0
#     0  1 -2  1   0
#     0  0  1 -2   1
#     0  0  0  1 -4/5
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is "almost" equal to the second difference matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
 
      if ( j == i ):

        if ( i == 0 ):
          a[i,j] = - 1.0
        elif ( i < n - 1 ):
          a[i,j] = - 2.0
        else:
          a[i,j] = - float ( n - 1 ) / float ( n )

      elif ( j == i - 1 or j == i + 1 ):

        a[i,j] = 1.0

  return a

def maxij_plu ( n ):

#*****************************************************************************80
#
## maxij_plu() returns the PLU factors of the MAXIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i4_wrap ( j - i, 1, n ) == 1 ):
        p[i,j] = 1.0

  l = np.zeros ( ( n, n ) )

  l[0,0] = 1.0

  j = 0
  for i in range ( 1, n ):
    l[i,j] = float ( i ) / float ( n )

  for j in range ( 1, n ):
    l[j,j] = 1.0

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    u[0,j] = float ( n )

  for i in range ( 1, n ):
    for j in range ( i, n ):
      u[i,j] = float ( j + 1 - i )

  return p, l, u

def maxij_test ( ):

#*****************************************************************************80
#
## maxij_test() tests maxij_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'maxij_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  maxij_matrix() computes the MAXIJ matrix.' )

  m = 5
  n = 5
  a = maxij_matrix ( m, n )
  r8mat_print ( m, n, a, '  MAXIJ matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'maxij_test' )
  print ( '  Normal end of execution.' )
  return

def mertens ( n ):

#*****************************************************************************80
#
## mertens() evaluates the Mertens function.
#
#  Discussion:
#
#    The Mertens function M(N) is the sum from 1 to N of the Moebius
#    function MU.  That is,
#
#    M(N) = sum ( 1 <= I <= N ) MU(I)
#
#        N   M(N)
#        --  ----
#         1     1
#         2     0
#         3    -1
#         4    -1
#         5    -2
#         6    -1
#         7    -2
#         8    -2
#         9    -2
#        10    -1
#        11    -2
#        12    -2
#       100     1
#      1000     2
#     10000   -23
#    100000   -48
#
#    The determinant of the Redheffer matrix of order N is equal
#    to the Mertens function M(N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    M Deleglise, J Rivat,
#    Computing the Summation of the Moebius Function,
#    Experimental Mathematics,
#    Volume 5, 1996, pages 291-295.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 2002,
#    Second edition,
#    ISBN: 1584883472,
#    LC: QA5.W45
#
#  Input:
#
#    integer N, the argument.
#
#  Output:
#
#    integer VALUE, the value.
#
  value = 0

  for i in range ( 1, n + 1 ):
    value = value + moebius ( i )

  return value

def mertens_test ( ):

#*****************************************************************************80
#
## mertens_test() tests mertens().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'mertens_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  mertens computes the Mertens function.' )
  print ( '' )
  print ( '    N   Exact   MERTENS(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = mertens_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = mertens ( n )

    print ( '  %4d  %8d  %8d' % ( n, c, c2 ) )
#
#  Terminate.
# 
  print ( '' )
  print ( 'mertens_test' )
  print ( '  Normal end of execution.' )
  return

def mertens_values ( n_data ):

#*****************************************************************************80
#
## mertens_values() returns some values of the Mertens function.
#
#  Discussion:
#
#    The Mertens function M(N) is the sum from 1 to N of the Moebius
#    function MU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    M Deleglise, J Rivat,
#    Computing the Summation of the Moebius Function,
#    Experimental Mathematics,
#    Volume 5, 1996, pages 291-295.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 2002,
#    Second edition,
#    ISBN: 1584883472,
#    LC: QA5.W45.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, 
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the Mertens function.
#
#    integer C, the value of the Mertens function.
#
  import numpy as np

  n_max = 15

  c_vec = np.array ( ( \
      1,   0,  -1,   -1,  -2,  -1,  -2,  -2,   -2,  -1, \
     -2,  -2,   1,    2, -23 ))

  n_vec = np.array ( ( \
      1,   2,   3,   4,   5,   6,   7,   8,   9,  10, \
     11,  12,  100, 1000, 10000 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def mertens_values_test ( ):

#*****************************************************************************80
#
## mertens_values_test() tests mertens_values().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'mertens_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  mertens_values stores values of the MERTENS function.' )
  print ( '' )
  print ( '             N    MERTENS(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = mertens_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'mertens_values_test:' )
  print ( '  Normal end of execution.' )
  return

def milnes_matrix ( m, n, x ):

#*****************************************************************************80
#
## milnes_matrix() returns the MILNES matrix.
#
#  Formula:
#
#    If ( I <= J )
#      A(I,J) = 1
#    else
#      A(I,J) = X(J)
#
#  Example:
#
#    M = 5, N = 5, X = ( 4, 7, 3, 8 )
#
#    1 1 1 1 1
#    4 1 1 1 1
#    4 7 1 1 1
#    4 7 3 1 1
#    4 7 3 8 1
#
#    M = 3, N = 6, X = ( 5, 7 )
#
#    1 1 1 1 1
#    5 1 1 1 1
#    5 7 1 1 1
#
#    M = 5, N = 3, X = ( 5, 7, 8 )
#
#    1 1 1
#    5 1 1
#    5 7 1
#    5 7 8
#    5 7 8
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    det ( A ) = ( 1 - X(1) ) * ( 1 - X(2) ) * ... * ( 1 - X(N-1) ).
#
#    A is singular if and only if X(I) = 1 for any I.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.14, Example 5.24,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 52, page 105,
#    LC: QA263.G68.
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#    real X(*), the lower column values.
#    If M <= N, then X should be dimensioned M-1.
#    If N < M, X should be dimensioned N.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = 1.0
      else:
        a[i,j] = x[j]

  return a

def milnes_determinant ( n, x ):

#*****************************************************************************80
#
## milnes_determinant() returns the determinant of the MILNES matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N), the parameter vector.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  if ( 1 < n ):
    for i in range ( 0, n - 1 ):
      value = value * ( 1.0 - x[i] )

  return value

def milnes_inverse ( n, x ):

#*****************************************************************************80
#
## milnes_inverse() returns the inverse of the MILNES matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.24,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 52, 
#    LC: QA263.G68.
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N-1), the lower column values.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j and i != n - 1 ):
        a[i,j] = 1.0 / ( 1.0 - x[i] )
      elif ( j == i + 1 and i != n - 1 ):
        a[i,j] = -1.0 / ( 1.0 - x[i] )
      elif ( i == n - 1 and j != 0 and j != n - 1 ):
        a[i,j] = ( x[j-1] - x[j] ) / ( ( 1.0 - x[j] ) * ( 1.0 - x[j-1] ) )
      elif ( i == n - 1 and j == 0 ):
        a[i,j] = - x[0] / ( 1.0 - x[0] )
      elif ( i == n - 1 and j == n - 1 ):
        a[i,j] = 1.0 / ( 1.0 - x[n-2] )

  return a

def milnes_test ( ):

#*****************************************************************************80
#
## milnes_test() tests milnes_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'milnes_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  milnes_matrix() computes the MILNES matrix.' )

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )

  a = milnes_matrix ( m, n, x )
 
  r8mat_print ( m, n, a, '  MILNES matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'milnes_test' )
  print ( '  Normal end of execution.' )
  return

def minij_matrix ( m, n ):

#*****************************************************************************80
#
## minij_matrix() returns the MINIJ matrix.
#
#  Formula:
#
#    A(I,J) = min ( I, J )
#
#  Example:
#
#    N = 5
#
#    1 1 1 1 1
#    1 2 2 2 2
#    1 2 3 3 3
#    1 2 3 4 4
#    1 2 3 4 5
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The inverse of A is tridiagonal.
#
#    The eigenvalues of A are
#
#      LAMBDA(I) = 0.5 / ( 1 - cos ( ( 2 * I - 1 ) * pi / ( 2 * N + 1 ) ) ),
#
#    For N = 12, the characteristic polynomial is
#      P(X) = X^12 - 78 X^11 + 1001 X^10 - 5005 X^9 + 12870 X^8
#        - 19448 X^7 + 18564 X^6 - 11628 X^5 + 4845 X^4 - 1330 X^3
#        + 231 X^2 - 23 X + 1.
#
#    (N+1)*ONES(N) - A also has a tridiagonal inverse.
#
#    Gregory and Karney consider the matrix defined by
#
#      B(I,J) = N + 1 - MAX(I,J)
#
#    which is equal to the MINIJ matrix, but with the rows and
#    columns reversed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.12, Example 4.14,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 41, page 74, 
#    LC: QA263.G68.
#
#    Daniel Rutherford,
#    Some continuant determinants arising in physics and chemistry II,
#    Proceedings of the Royal Society Edinburgh,
#    Volume 63, A, 1952, pages 232-241.
#
#    John Todd,
#    Basic Numerical Mathematics, Vol. 2: Numerical Algebra,
#    Academic Press, 1977, page 158.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer M, N, the number of rows and columns 
#    of the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      a[i,j] = min ( i, j ) + 1

  return a

def minij_condition ( n ):

#*****************************************************************************80
#
## minij_condition() returns the L1 condition of the MINIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = float ( n * ( n + 1 ) ) / 2.0
  if ( n == 1 ):
    b_norm = 1.0
  elif ( n == 2 ):
    b_norm = 3.0
  else:
    b_norm = 4.0

  value = a_norm * b_norm

  return value

def minij_determinant ( n ):

#*****************************************************************************80
#
## minij_determinant() returns the determinant of the MINIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  value = 1.0

  for i in range ( 0, n ):
    angle = float ( 2 * i + 1 ) * np.pi / float ( 2 * n + 1 )
    value = value * 0.5 / ( 1.0 - np.cos ( angle ) )

  return value

def minij_eigenvalues ( n ):

#*****************************************************************************80
#
## minij_eigenvalues() returns the eigenvalues of the MINIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = zeros ( n, 1 )

  for i in range ( 0, n ):
    angle = float ( 2 * i + 1 ) * np.pi / float ( 2 * n + 1 )
    lam[i] = 0.5 / ( 1.0 - np.cos ( angle ) )

  return lam

def minij_inverse ( n ):

#*****************************************************************************80
#
## minij_inverse() returns the inverse of the MINIJ matrix.
#
#  Formula:
#
#    A(I,J) =  -1  if J=I-1 or J=I+1
#    A(I,J) =   2  if J=I and J is not N.
#    A(I,J) =   1  if J=I and J=N.
#    A(I,J) =   0  otherwise
#
#  Example:
#
#    N = 5
#
#     2 -1  0  0  0
#    -1  2 -1  0  0
#     0 -1  2 -1  0
#     0  0 -1  2 -1
#     0  0  0 -1  1
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is "almost" equal to the second difference matrix,
#    as computed by DIF.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        if ( i < n - 1 ):
          a[i,j] = 2.0
        else:
          a[i,j] = 1.0
      elif ( i == j + 1 or i == j - 1 ):
        a[i,j] = -1.0
 
  return a

def minij_llt ( n ):

#*****************************************************************************80
#
## minij_llt() returns the Cholesky factor of the MINIJ matrix.
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  0
#    1  1  0  0  0
#    1  1  1  0  0
#    1  1  1  1  0
#    1  1  1  1  1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      a[i,j] = 1.0

  return a

def minij_lu ( n ):

#*****************************************************************************80
#
## minij_lu() returns the LU factors of the MINIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real L(N,N), U(N,N) the factors.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( j, n ):
      l[i,j] = 1.0

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      u[i,j] = 1.0

  return l, u

def minij_plu ( n ):

#*****************************************************************************80
#
## minij_plu() returns the PLU factors of the MINIJ matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 June 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N) the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == j ):
        p[i,j] = 1.0

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( j, n ):
      l[i,j] = 1.0

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      u[i,j] = 1.0

  return p, l, u

def minij_test ( ):

#*****************************************************************************80
#
## minij_test() tests minij_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'minij_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  minij_matrix() computes the MINIJ matrix.' )

  m = 5
  n = 5
  a = minij_matrix ( m, n )
  r8mat_print ( m, n, a, '  MINIJ matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'minij_test' )
  print ( '  Normal end of execution.' )
  return

def moebius ( n ):

#*****************************************************************************80
#
## moebius() returns the value of MU(N), the Moebius function of N.
#
#  Definition:
#
#    MU(N) is defined as follows:
#
#      MU(N) = 1 if N = 1;
#              0 if N is divisible by the square of a prime;
#              (-1)^K, if N is the product of K distinct primes.
#
#  First values:
#
#     N  MU(N)
#
#     1    1
#     2   -1
#     3   -1
#     4    0
#     5   -1
#     6    1
#     7   -1
#     8    0
#     9    0
#    10    1
#    11   -1
#    12    0
#    13   -1
#    14    1
#    15    1
#    16    0
#    17   -1
#    18    0
#    19   -1
#    20    0
#
#    As special cases, MU(N) is -1 if N is a prime, and MU(N) is 0
#    if N is a square, cube, etc.
#
#    The Moebius function is related to Euler's totient function:
#
#      PHI(N) = Sum ( D divides N ) MU(D) * ( N / D ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the value to be analyzed.
#
#  Output:
#
#    integer VALUE, the value of MU(N).
#    If N is less than or equal to 0, MU will be returned as -2.
#    If there was not enough internal space for factoring, MU
#    is returned as -3.
#
  if ( n <= 0 ):
    value = -2
    return value

  if ( n == 1 ):
    value = 1
    return value
#
#  Factor N.
#
  nfactor, factor, power, nleft = i4_factor ( n )

  if ( nleft != 1 ):
    print ( '' )
    print ( 'moebius - Fatal error!' )
    print ( '  Incomplete factorization.' )
    value = -3

  value = 1

  for i in range ( 0, nfactor ):
 
    value = - value

    if ( 1 < power[i] ):
      value = 0
      return value

  return value

def moebius_test ( ):

#*****************************************************************************80
#
## moebius_test() tests moebius().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'moebius_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  moebius() computes the Moebius function.' )
  print ( '' )
  print ( '    N   Exact   MOEBIUS(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = moebius_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = moebius ( n )

    print ( '  %4d  %8d  %8d' % ( n, c, c2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'moebius_test' )
  print ( '  Normal end of execution.' )
  return

def moebius_values ( n_data ):

#*****************************************************************************80
#
## moebius_values() returns some values of the Moebius function.
#
#  Discussion:
#
#    MU(N) is defined as follows:
#
#      MU(N) = 1 if N = 1;
#              0 if N is divisible by the square of a prime;
#              (-1)^K, if N is the product of K distinct primes.
#
#    In Mathematica, the function can be evaluated by:
#
#      MoebiusMu[n]
#
#  First values:
#
#     N  MU(N)
#
#     1    1
#     2   -1
#     3   -1
#     4    0
#     5   -1
#     6    1
#     7   -1
#     8    0
#     9    0
#    10    1
#    11   -1
#    12    0
#    13   -1
#    14    1
#    15    1
#    16    0
#    17   -1
#    18    0
#    19   -1
#    20    0
#
#    As special cases, MU(N) is -1 if N is a prime, and MU(N) is 0
#    if N is a square, cube, etc.
#
#  Formula:
#
#    The Moebius function is related to Euler's totient function:
#
#      PHI(N) = Sum ( D divides N ) MU(D) * ( N / D ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, 
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the Moebius function.
#
#    integer C, the value of the Moebius function.
#
  import numpy as np

  n_max = 20

  c_vec = np.array ( ( \
      1,  -1,  -1,   0,  -1,   1,  -1,   0,   0,   1, \
     -1,   0,  -1,   1,   1,   0,  -1,   0,  -1,   0 ))

  n_vec = np.array ( ( \
      1,   2,   3,   4,   5,   6,   7,   8,   9,  10, \
     11,  12,  13,  14,  15,  16,  17,  18,  19,  20 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def moebius_values_test ( ):

#*****************************************************************************80
#
## moebius_values_test() tests moebius_values().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'moebius_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  moebius_values stores values of the MOEBIUS function.' )
  print ( '' )
  print ( '             N    MOEBIUS(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = moebius_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'moebius_values_test:' )
  print ( '  Normal end of execution.' )
  return

def moler1_matrix ( alpha, m, n ):

#*****************************************************************************80
#
## moler1_matrix() returns the MOLER1 matrix.
#
#  Formula:
#
#    If ( I = J )
#      A(I,J) = min ( I-1, J-1 ) * ALPHA^2 + 1
#    else
#      A(I,J) = min ( I-1, J-1 ) * ALPHA^2 + ALPHA
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#    1 2  2  2  2
#    2 5  6  6  6
#    2 6  9 10 10
#    2 6 10 13 14
#    2 6 10 14 17
#
#  Properties:
#
#    Successive elements of each diagonal increase by an increment of ALPHA^2.
#
#    A is the product of B' * B, where B is the matrix returned by
#
#      B = TRIW ( ALPHA, N-1, N ).
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is positive definite.
#
#    If ALPHA = -1, A(I,J) = min ( I, J ) - 2, A(I,I)=I.
#
#    A has one small eigenvalue.
#
#    If ALPHA is integral, then A is integral.
#    If A is integral, then det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Nash,
#    Compact Numerical Methods for Computers: Linear Algebra and
#    Function Minimisation,
#    John Wiley, 1979,
#    pages 76 and 210.
#
#  Input:
#
#    real ALPHA, the scalar that defines the Moler matrix.
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = min ( i, j ) * alpha * alpha + 1.0
      else:
        a[i,j] = min ( i, j ) * alpha * alpha + alpha

  return a

def moler1_determinant ( alpha, n ):

#*****************************************************************************80
#
## moler1_determinant() returns the determinant of the MOLER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def moler1_inverse ( alpha, n ):

#*****************************************************************************80
#
## moler1_inverse() returns the inverse of the MOLER1 matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) =              min ( N-I, N-J ) * ALPHA^2 + 1
#    else
#      A(I,J) = (-1)^(I+J) * min ( N-I, N-J ) * ALPHA^2 + ALPHA
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#     17 -14  10 -6  2
#    -14  13 -10  6 -2
#     10 -10   9 -6  2
#     -6   6  -6  5 -2
#      2  -2   2 -2  1
#
#  Properties:
#
#    The matrix is symmetric.
#
#    Successive elements of each diagonal decrease by ALPHA**2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar that defines the inverse 
#    Moler matrix.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  v = np.zeros ( n )

  v[0] = 1.0
  v[1] = - alpha
  for i in range ( 2, n ):
    v[i] = - ( alpha - 1.0 ) * v[i-1]

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        t = 0.0
        for k in range ( 0, n - j ):
          t = t + v[j-i+k] * v[k]
        a[i,j] = t
      else:
        t = 0.0
        for k in range ( 0, n - i ):
          t = t + v[k] * v[i-j+k]
        a[i,j] = t

  return a

def moler1_llt ( alpha, n ):

#*****************************************************************************80
#
## moler1_llt() returns the Cholesky factor of the MOLER1 matrix.
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#    1  0  0  0  0
#    2  1  0  0  0
#    2  2  1  0  0
#    2  2  2  1  0
#    2  2  2  2  1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    a[j,j] = 1.0
    for i in range ( j + 1, n ):
      a[i,j] = alpha
 
  return a

def moler1_lu ( alpha, n ):

#*****************************************************************************80
#
## moler1_lu() returns the LU factors of the MOLER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Nash,
#    Compact Numerical Methods for Computers: Linear Algebra and
#    Function Minimisation,
#    Second Edition,
#    Taylor & Francis, 1990,
#    ISBN: 085274319X,
#    LC: QA184.N37.
#
#  Input:
#
#    real ALPHA, the parameter.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real L(N,N), U(N,N), the factors.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == j ):
        l[i,j] = 1.0
      elif ( j < i ):
        l[i,j] = alpha

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, j ):
      u[i,j] = alpha
    u[j,j] = 1.0

  return l, u

def moler1_plu ( alpha, n ):

#*****************************************************************************80
#
## moler1_plu() returns the PLU factors of the MOLER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Nash,
#    Compact Numerical Methods for Computers: Linear Algebra and
#    Function Minimisation,
#    Second Edition,
#    Taylor & Francis, 1990,
#    ISBN: 085274319X,
#    LC: QA184.N37.
#
#  Input:
#
#    real ALPHA, the parameter.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == j ):
        l[i,j] = 1.0
      elif ( j < i ):
        l[i,j] = alpha

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, j ):
      u[i,j] = alpha
    u[j,j] = 1.0

  return p, l, u

def moler1_test ( ):

#*****************************************************************************80
#
## moler1_test() tests moler1_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'moler1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  moler1_matrix() computes the MOLER1 matrix.' )

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )

  a = moler1_matrix ( alpha, m, n )
  r8mat_print ( m, n, a, '  MOLER1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'moler1_test' )
  print ( '  Normal end of execution.' )
  return

def moler2_matrix ( ):

#*****************************************************************************80
#
## moler2_matrix() returns the MOLER2 matrix.
#
#  Discussion:
#
#    This is a 5 by 5 matrix for which the challenge is to find the EXACT
#    eigenvalues and eigenvectors.
#
#  Formula:
#
#       -9     11    -21     63    -252
#       70    -69    141   -421    1684
#     -575    575  -1149   3451  -13801
#     3891  -3891   7782 -23345   93365
#     1024  -1024   2048  -6144   24572
#
#  Properties:
#
#    A is defective.
#
#    The Jordan normal form of A has just one block, with eigenvalue
#    zero, because A^k is nonzero for K = 0, 1, 2, 3, 4, but A^5=0.
#
#    det ( A ) = 0.
#
#    TRACE(A) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(5,5), the matrix.
#
  import numpy as np

  a = np.array ( [ \
      [     -9.0,     11.0,    -21.0,     63.0,   -252.0 ], \
      [     70.0,    -69.0,    141.0,   -421.0,   1684.0 ], \
      [   -575.0,    575.0,  -1149.0,   3451.0, -13801.0 ], \
      [   3891.0,  -3891.0,   7782.0, -23345.0,  93365.0 ], \
      [   1024.0,  -1024.0,   2048.0,  -6144.0,  24572.0 ] ] )

  return a

def moler2_determinant ( ):

#*****************************************************************************80
#
## moler2_determinant() returns the determinant of the MOLER2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 0.0

  return value

def moler2_null_left ( ):

#*****************************************************************************80
#
## moler2_null_left() returns a left null vector of the MOLER2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(M), the left null vector.
#
  import numpy as np

  x = np.array ( [ [ 4.0 ], [ -8.0 ], [ 20.0 ], [ -64.0 ], [ 255.0 ] ] )

  return x

def moler2_null_right ( ):

#*****************************************************************************80
#
## moler2_null_right() returns a right null vector for the MOLER2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(5), the null vector.
#
  import numpy as np

  x = np.array ( [ [ 0.0 ], [ -21.0 ], [ 142.0 ], [ -973.0 ], [ -256.0 ] ] )

  return x

def moler2_test ( ):

#*****************************************************************************80
#
## moler2_test() tests moler2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'moler2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  moler2_matrix() computes the MOLER2 matrix.' )

  m = 5
  n = m

  a = moler2_matrix ( )
  r8mat_print ( m, n, a, '  MOLER2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'moler2_test' )
  print ( '  Normal end of execution.' )
  return

def moler3_matrix ( m, n ):

#*****************************************************************************80
#
## moler3_matrix() returns the MOLER3 matrix.
#
#  Formula:
#
#    if ( I == J )
#      A(I,J) = I
#    else
#      A(I,J) = min(I,J) - 2
#
#  Example:
#
#    N = 5
#
#     1 -1 -1 -1 -1
#    -1  2  0  0  0
#    -1  0  3  1  1
#    -1  0  1  4  2
#    -1  0  1  2  5
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A has a simple Cholesky factorization.
#
#    A has one small eigenvalue.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  A = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i == j ):
        A[i,j] = float ( i + 1 )
      else:
        A[i,j] = float ( min ( i, j ) - 1 )

  return A

def moler3_determinant ( n ):

#*****************************************************************************80
#
## moler3_determinant() returns the determinant of the MOLER3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def moler3_inverse ( n ):

#*****************************************************************************80
#
## moler3_inverse() returns the inverse of the MOLER3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    l[j,j] = 1.0
    value = 1.0
    for i in range ( j + 1, n ):
      l[i,j] = value
      value = value * 2.0

  a = r8mat_mtm ( n, n, n, l, l )

  return a

def moler3_llt ( n ):

#*****************************************************************************80
#
## moler3_llt() returns the Cholesky factor of the MOLER3 matrix.
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  0
#   -1  1  0  0  0
#   -1 -1  1  0  0
#   -1 -1 -1  1  0
#   -1 -1 -1 -1  1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      a[i,j] = -1.0
    a[i,i] =  1.0
 
  return a

def moler3_lu ( n ):

#*****************************************************************************80
#
## moler3_lu() returns the LU factors of the MOLER3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real L(N,N), U(N,N) the LU factors.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      l[i,j] = -1.0
    l[i,i] =  1.0

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, j ):
      u[i,j] = -1.0
    u[j,j] =  1.0

  return l, u

def moler3_plu ( n ):

#*****************************************************************************80
#
## moler3_plu() returns the PLU factors of the MOLER3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N) the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      l[i,j] = -1.0
    l[i,i] =  1.0

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, j ):
      u[i,j] = -1.0
    u[j,j] =  1.0

  return p, l, u

def moler3_test ( ):

#*****************************************************************************80
#
## moler3_test() tests moler3_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'moler3_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  moler3_matrix() computes the MOLER3 matrix.' )

  m = 5
  n = m

  a = moler3_matrix ( m, n )
  r8mat_print ( m, n, a, '  MOLER3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'moler3_test' )
  print ( '  Normal end of execution.' )
  return

def moler4_matrix ( ):

#*****************************************************************************80
#
## moler4_matrix() returns the MOLER4 matrix.
#
#  Example:
#
#    0  2  0 -1
#    1  0  0  0
#    0  1  0  0
#    0  0  1  0
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is the companion matrix of the polynomial X^4-2X^2+1=0.
#
#    A has eigenvalues -1, -1, +1, +1.
#
#    A can cause problems to a standard QR algorithm, which
#    can fail to converge.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 0.0,  2.0,  0.0, -1.0 ], \
    [ 1.0,  0.0,  0.0,  0.0 ], \
    [ 0.0,  1.0,  0.0,  0.0 ], \
    [ 0.0,  0.0,  1.0,  0.0 ] ] )

  return a

def moler4_determinant ( ):

#*****************************************************************************80
#
## moler4_determinant() returns the determinant of the MOLER4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def moler4_test ( ):

#*****************************************************************************80
#
## moler4_test() tests moler4_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'moler4_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  moler4_matrix() computes the MOLER4 matrix.' )

  m = 4
  n = m

  a = moler4_matrix ( )
  r8mat_print ( m, n, a, '  MOLER4 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'moler4_test' )
  print ( '  Normal end of execution.' )
  return

def neumann_matrix ( nrow, ncol ):

#*****************************************************************************80
#
## neumann_matrix() returns the NEUMANN matrix.
#
#  Formula:
#
#    I1 = 1 + ( I - 1 ) / NROW
#    I2 = I - ( I1 - 1 ) * NROW
#    J1 = 1 + ( J - 1 ) / NROW
#
#    if ( I = J )
#      A(I,J) = 4
#    elseif ( I = J-1 )
#      If ( I2 = 1 )
#        A(I,J) = -2
#      else
#        A(I,J) = -1
#    elseif ( I = J+1 )
#      If ( I2 = NROW )
#        A(I,J) = -2
#      else
#        A(I,J) = -1
#    elseif ( I = J - NROW )
#      if ( J1 = 2 )
#        A(I,J) = -2
#      else
#        A(I,J) = -1
#    elseif ( I = J + NROW )
#      if ( J1 = NCOL-1 )
#        A(I,J) = -2
#      else
#        A(I,J) = -1
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    NROW = NCOL = 3
#
#     4 -2  0 | -2  0  0 |  0  0  0
#    -1  4 -1 |  0 -2  0 |  0  0  0
#     0 -2  4 |  0  0 -2 |  0  0  0
#     ----------------------------
#    -1  0  0 |  4 -1  0 | -1  0  0
#     0 -1  0 | -1  4 -1 |  0 -1  0
#     0  0 -1 |  0 -1  4 |  0  0 -1
#     ----------------------------
#     0  0  0 | -2  0  0 |  4 -2  0
#     0  0  0 |  0 -2  0 | -1  4 -1
#     0  0  0 |  0  0 -2 |  0 -2  4
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is block tridiagonal.
#
#    A results from discretizing Neumann's equation with the
#    5 point operator on a mesh of NROW by NCOL points.
#
#    A is singular.
#
#    A has the null vector ( 1, 1, ..., 1 ).
#
#    det ( A ) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989
#    (Section 4.5.4).
#
#  Input:
#
#    integer NROW, NCOL, the number of rows and columns
#    in the grid.
#
#  Output:
#
#    integer N, the order of the matrix, which 
#    is NROW*NCOL.
#
#    real A(NROW*NCOL,NROW*NCOL), the NROW*NCOL 
#    by NROW*NCOL matrix.
#
  import numpy as np

  n = nrow * ncol

  a = np.zeros ( ( n, n ) )

  i = 0

  for i1 in range ( 0, nrow ):
    for j1 in range ( 0, ncol ):

      if ( 0 < i1 ):
        j = i - nrow
      else:
        j = i + nrow

      a[i,j] = a[i,j] - 1.0

      if ( 0 < j1 ):
        j = i - 1
      else:
        j = i + 1

      a[i,j] = a[i,j] - 1.0

      j = i
      a[i,j] = 4.0

      if ( j1 < ncol - 1 ):
        j = i + 1
      else:
        j = i - 1

      a[i,j] = a[i,j] - 1.0

      if ( i1 < nrow - 1 ):
        j = i + nrow
      else:
        j = i - nrow

      a[i,j] = a[i,j] - 1.0

      i = i + 1

  return a

def neumann_determinant ( row_num, col_num ):

#*****************************************************************************80
#
## neumann_determinant() returns the determinant of the NEUMANN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ROW_NUM, COL_NUM, the number of rows and columns 
#    in the grid.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 0.0

  return value

def neumann_null_right ( nrow, ncol ):

#*****************************************************************************80
#
## neumann_null_right() returns a right null vector of the NEUMANN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NROW, NCOL, the number of rows and columns 
#    in the grid.
#
#  Output:
#
#    real X(NROW*NCOL), the null vector.
#
  import numpy as np

  x = np.ones ( nrow * ncol )
 
  return x

def neumann_test ( ):

#*****************************************************************************80
#
## neumann_test() tests neumann_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'neumann_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  neumann_matrix() computes the NEUMANN matrix.' )

  row_num = 3
  col_num = 3

  m = row_num * col_num
  n = m

  a = neumann_matrix ( row_num, col_num )
  r8mat_print ( m, n, a, '  NEUMANN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'neumann_test' )
  print ( '  Normal end of execution.' )
  return

def one_matrix ( m, n ):

#*****************************************************************************80
#
## one_matrix() returns the ONE matrix.
#
#  Discussion:
#
#    The matrix is sometimes symbolized by "J".
#
#  Example:
#
#    N = 5
#
#    1 1 1 1 1
#    1 1 1 1 1
#    1 1 1 1 1
#    1 1 1 1 1
#    1 1 1 1 1
#
#  Properties:
#
#    Every entry of A is 1.
#
#    A is symmetric.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is Hankel: constant along antidiagonals.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A has constant row sums.
#
#    A has constant column sums.
#
#    If 1 < N, A is singular.
#
#    If 1 < N, det ( A ) = 0.
#
#    LAMBDA(1:N-1) = 0
#    LAMBDA(N) = N
#
#    The eigenvector associated with LAMBDA = N is ( 1, 1, ..., 1 ).
#
#    A * A = N * A
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.ones ( ( m, n ) )
 
  return a

def one_determinant ( n ):

#*****************************************************************************80
#
## one_determinant() returns the determinant of the ONE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  if ( n == 1 ):
    value = 1.0
  else:
    value = 0.0

  return value

def one_eigen_right ( n ):

#*****************************************************************************80
#
## one_eigen_right() returns the right eigenvectors of the ONE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real X(N,N), the right eigenvectors.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n - 1 ):
    x[  0,j] = +1.0
    x[j+1,j] = -1.0

  for i in range ( 0, n ):
    x[i,n-1] = 1.0

  return x

def one_eigenvalues ( n ):

#*****************************************************************************80
#
## one_eigenvalues() returns the eigenvalues of the ONE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  lam[n-1] = float ( n )

  return lam

def one_null_left ( m, n ):

#*****************************************************************************80
#
## one_null_left() returns a left null vector for the ONE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(M), a left null vector.
#
  import numpy as np

  x = np.zeros ( m )

  x[0] = 1
  x[m-1] = -1

  return x

def one_null_right ( m, n ):

#*****************************************************************************80
#
## one_null_right() returns a right null vector for the ONE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(N), a right null vector.
#
  import numpy as np

  x = np.zeros ( n )

  x[0] = 1.0
  x[n-1] = -1.0

  return x

def one_test ( ):

#*****************************************************************************80
#
## one_test() tests one_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'one_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  one_matrix() computes the ONE matrix.' )

  m = 4
  n = m

  a = one_matrix ( m, n )
  r8mat_print ( m, n, a, '  ONE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'one_test' )
  print ( '  Normal end of execution.' )
  return

def ortega_matrix ( n, u, v, d ):

#*****************************************************************************80
#
## ortega_matrix() returns the ORTEGA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Ortega,
#    Generation of Test Matrices by Similarity Transformations,
#    Communications of the ACM,
#    Volume 7, 1964, pages 377-378.
#
#  Input:
#
#    integer N, the order of the matrix.
#    2 <= N.
#
#    real U(N), V(N), vectors which define the matrix.
#    U'V must not equal -1.0.  If, in fact, U'V = 0, and U, V and D are
#    integers, then the matrix, inverse, eigenvalues, and eigenvectors 
#    will be integers.
#
#    real D(N), the desired eigenvalues.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np
  
  vtu = np.dot ( v, u )

  beta = 1.0 / ( 1.0 + vtu )

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      for k in range ( 0, n ):

        if ( i == k ):
          bik = 1.0 + u[i] * v[k]
        else:
          bik =       u[i] * v[k]

        if ( k == j ):
          ckj = 1.0 - beta * u[k] * v[j]
        else:
          ckj =     - beta * u[k] * v[j]

        a[i,j] = a[i,j] + bik * d[k] * ckj
 
  return a

def ortega_determinant ( n, u, v, d ):

#*****************************************************************************80
#
## ortega_determinant() returns the determinant of the ORTEGA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real U(N), V(N), vectors which define the matrix.
#    U'V must not equal -1.0.  If, in fact, U'V = 0, and U, V and D are
#    integers, then the matrix, inverse, eigenvalues, and eigenvectors 
#    will be integers.
#
#    real D(N), the desired eigenvalues
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as  np

  value = np.prod ( d )

  return value

def ortega_eigen_right ( n, u, v, d ):

#*****************************************************************************80
#
## ortega_eigen_right() returns the right eigenvectors of the ORTEGA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Ortega,
#    Generation of Test Matrices by Similarity Transformations,
#    Communications of the ACM,
#    Volume 7, 1964, pages 377-378.
#
#  Input:
#
#    integer N, the order of the matrix.
#    2 <= N.
#
#    real U(N), V(N), vectors which define the matrix.
#    U'V must not equal -1.0.  If, in fact, U'V = 0, and U, V and D are
#    integers, then the matrix, inverse, eigenvalues, and eigenvectors 
#    will be integers.
#
#    real D(N), the desired eigenvalues.
#
#  Output:
#
#    real X(N,N), the determinant.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n ):
    for i in range ( 0, n ):

      if ( i == j ):
        x[i,j] = 1.0 + u[i] * v[j]
      else:
        x[i,j] =       u[i] * v[j]

  return x

def ortega_eigenvalues ( n, u, v, d ):

#*****************************************************************************80
#
## ortega_eigenvalues() returns the eigenvalues of the ORTEGA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Ortega,
#    Generation of Test Matrices by Similarity Transformations,
#    Communications of the ACM,
#    Volume 7, 1964, pages 377-378.
#
#  Input:
#
#    integer N, the order of the matrix.
#    2 <= N.
#
#    real U(N), V(N), vectors which define the matrix.
#    U'V must not equal -1.0.  If, in fact, U'V = 0, and U, V and D are
#    integers, then the matrix, inverse, eigenvalues, and eigenvectors 
#    will be integers.
#
#    real D(N), the desired eigenvalues.
#
#  Output:
#
#    real LAM(N), the determinant.
#
  import numpy as np

  lam = np.copy ( d )

  return lam

def ortega_inverse ( n, u, v, d ):

#*****************************************************************************80
#
## ortega_inverse() returns the inverse of the ORTEGA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Ortega,
#    Generation of Test Matrices by Similarity Transformations,
#    Communications of the ACM,
#    Volume 7, 1964, pages 377-378.
#
#  Input:
#
#    integer N, the order of the matrix.
#    2 <= N.
#
#    real U(N), V(N), vectors which define the matrix.
#    U'V must not equal -1.0.  If, in fact, U'V = 0, and U, V and D are
#    integers, then the matrix, inverse, eigenvalues, and eigenvectors 
#    will be integers.
#
#    real D(N), the desired eigenvalues.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  vtu = 0.0
  for i in range ( 0, n):
    vtu = vtu + v[i] * u[i]

  beta = 1.0 / ( 1.0 + vtu )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      for k in range ( 0, n ):

        if ( i == k ):
          bik = 1.0 + u[i] * v[k]
        else:
          bik =     + u[i] * v[k]

        if ( k == j ):
          ckj = 1.0 - beta * u[k] * v[j]
        else:
          ckj =     - beta * u[k] * v[j]

        a[i,j] = a[i,j] + ( bik / d[k] ) * ckj

  return a

def ortega_test ( ):

#*****************************************************************************80
#
## ortega_test() tests ortega_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ortega_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ortega_matrix() computes the ORTEGA matrix.' )

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  v1 = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )
  v2 = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )
  v3 = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )

  a = ortega_matrix ( n, v1, v2, v3 )

  r8mat_print ( m, n, a, '  ORTEGA matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ortega_test' )
  print ( '  Normal end of execution.' )
  return

def orthogonal_random_matrix ( n, key ):

#*****************************************************************************80
#
## orthogonal_random_matrix() returns an orthogonal_random matrix.
#
#  Properties:
#
#    The inverse of A is equal to A'.
#
#    A is orthogonal: A * A'  = A' * A = I.
#
#    Because A is orthogonal, it is normal: A' * A = A * A'.
#
#    Columns and rows of A have unit Euclidean norm.
#
#    Distinct pairs of columns of A are orthogonal.
#
#    Distinct pairs of rows of A are orthogonal.
#
#    The L2 vector norm of A*x = the L2 vector norm of x for any vector x.
#
#    The L2 matrix norm of A*B = the L2 matrix norm of B for any matrix B.
#
#    det ( A ) = +1 or -1.
#
#    A is unimodular.
#
#    All the eigenvalues of A have modulus 1.
#
#    All singular values of A are 1.
#
#    All entries of A are between -1 and 1.
#
#  Discussion:
#
#    Thanks to Eugene Petrov, B I Stepanov Institute of Physics,
#    National Academy of Sciences of Belarus, for convincingly
#    pointing out the severe deficiencies of an earlier version of
#    this routine.
#
#    Essentially, the computation involves saving the Q factor of the
#    QR factorization of a matrix whose entries are normally distributed.
#    However, it is only necessary to generate this matrix a column at
#    a time, since it can be shown that when it comes time to annihilate
#    the subdiagonal elements of column K, these (transformed) elements of
#    column K are still normally distributed random values.  Hence, there
#    is no need to generate them at the beginning of the process and
#    transform them K-1 times.
#
#    For computational efficiency, the individual Householder transformations
#    could be saved, as recommended in the reference, instead of being
#    accumulated into an explicit matrix format.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pete Stewart,
#    Efficient Generation of Random Orthogonal Matrices With an Application
#    to Condition Estimators,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 3, June 1980, pages 403-409.
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np
#
#  Start with A = the identity matrix.
#
  a = np.identity ( n )
#
#  Now behave as though we were computing the QR factorization of
#  some other random matrix.  Generate the N elements of the first column,
#  compute the Householder matrix H1 that annihilates the subdiagonal elements,
#  and set A := A * H1' = A * H.
#
#  On the second step, generate the lower N-1 elements of the second column,
#  compute the Householder matrix H2 that annihilates them,
#  and set A := A * H2' = A * H2 = H1 * H2.
#
#  On the N-1 step, generate the lower 2 elements of column N-1,
#  compute the Householder matrix HN-1 that annihilates them, and
#  and set A := A * H(N-1)' = A * H(N-1) = H1 * H2 * ... * H(N-1).
#  This is our random orthogonal matrix.
#
  x_col = np.zeros ( n )
 
  np.random.seed ( key )
 
  for j in range ( 0, n - 1 ):

    for i in range ( 0, j ):
      x_col[i] = 0.0

    for i in range ( j, n ):
      x_col[i] = np.random.normal ( 0.0, 1.0 )
#
#  Compute the vector V that defines a Householder transformation matrix
#  H(V) that annihilates the subdiagonal elements of X.
#
    v = r8vec_house_column ( n, x_col, j )
#
#  Postmultiply the matrix A by H'(V) = H(V).
#
    a = r8mat_house_axh ( n, a, v )
#
#  Randomly insert reflections.
#
    r = np.random.rand ( )
    if ( 0.5 < r ):
      k = np.random.randint ( 0, n )
      a[k,0:n] = - a[k,0:n]

  return a

def orthogonal_random_determinant ( n, key ):

#*****************************************************************************80
#
## orthogonal_random_determinant(): determinant of the orthogonal_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def orthogonal_random_inverse ( n, key ):

#*****************************************************************************80
#
## orthogonal_random_inverse(): inverse of the orthogonal_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real B[N,N], the inverse.
#
  import numpy as np

  b = orthogonal_random_matrix ( n, key )

  b = np.transpose ( b )

  return b

def orthogonal_random_test ( ):

#*****************************************************************************80
#
## orthogonal_random_test() tests orthogonal_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'orthogonal_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  orthogonal_random_matrix computes a random orthogonal matrix.' )

  m = 5
  n = m
  key = 123456789

  a = orthogonal_random_matrix ( n, key )

  r8mat_print ( m, n, a, '  orthogonal_random matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'orthogonal_random_test:' )
  print ( '  Normal end of execution.' )
  return

def orthogonal_symmetric_matrix ( n ):

#*****************************************************************************80
#
## orthogonal_symmetric_matrix() returns an orthogonal symmetric matrix.
#
#  Formula:
#
#    A(I,J) = sqrt ( 2 ) * sin ( I * J * pi / ( N + 1 ) ) / sqrt ( N + 1 )
#
#  Example:
#
#    N = 5
#
#    0.326019   0.548529   0.596885   0.455734   0.169891
#    0.548529   0.455734  -0.169891  -0.596885  -0.326019
#    0.596885  -0.169891  -0.548529   0.326019   0.455734
#    0.455734  -0.596885   0.326019   0.169891  -0.548528
#    0.169891  -0.326019   0.455734  -0.548528   0.596885
#
#  Properties:
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    A is symmetric: A' = A.
#
#    A is not positive definite (unless N = 1 ).
#
#    Because A is symmetric, it is normal.
#
#    Because A is symmetric, its eigenvalues are real.
#
#    Because A is orthogonal, its eigenvalues have unit norm.
#
#    Only +1 and -1 can be eigenvalues of A.
#
#    Because A is normal, it is diagonalizable.
#
#    A is involutional: A * A = I.
#
#    If N is even, trace ( A ) = 0; if N is odd, trace ( A ) = 1.
#
#    LAMBDA(1:(N+1)/2) = 1; LAMBDA((N+1)/2+1:N) = -1.
#
#    A is the left and right eigenvector matrix for the
#    second difference matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Morris Newman, John Todd,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = 2.0 * float ( i + 1 ) * float ( j + 1 ) * np.pi / float ( 2 * n + 1 )
      a[i,j] = 2.0 * np.sin ( angle ) / np.sqrt ( float ( 2 * n + 1 ) )

  return a

def orthogonal_symmetric_condition ( n ):

#*****************************************************************************80
#
## orthogonal_symmetric_condition(): L1 condition of the orthogonal_symmetric matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  import numpy as np

  a_norm = 0.0
  j = 0
  for i in range ( 0, n ): 
    angle = 2.0 * float ( i + 1 ) * float ( j + 1 ) * np.pi / float ( 2 * n + 1 )
    a_norm = a_norm + 2.0 * abs ( np.sin ( angle ) ) / np.sqrt ( 2 * n + 1 )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def orthogonal_symmetric_determinant ( n ):

#*****************************************************************************80
#
## orthogonal_symmetric_determinant(): determinant of the orthogonal_symmetric matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def orthogonal_symmetric_inverse ( n ):

#*****************************************************************************80
#
## orthogonal_symmetric_inverse(): inverse of the orthogonal_symmetric matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  a = orthogonal_symmetric_matrix ( n )

  return a

def orthogonal_symmetric_test ( ):

#*****************************************************************************80
#
## orthogonal_symmetric_test() tests orthogonal_symmetric_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'orthogonal_symmetric_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  orthogonal_symmetric_matrix() computes the orthogonal_symmetric matrix.' )

  m = 5
  n = 5
  a = orthogonal_symmetric_matrix ( n )
  r8mat_print ( m, n, a, '  orthogonal_symmetric matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'orthogonal_symmetric_test' )
  print ( '  Normal end of execution.' )
  return

def oto_matrix ( m, n ):

#*****************************************************************************80
#
## oto_matrix() returns the OTO matrix.
#
#  Example:
#
#    N = 5
#
#    2  1  .  .  .
#    1  2  1  .  .
#    .  1  2  1  .
#    .  .  1  2  1
#    .  .  .  1  2
#
#  Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is integral: int ( A ) = A.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is weakly diagonally dominant, but not strictly diagonally dominant.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( j == i - 1 ):
        a[i,j] = 1.0
      elif ( j == i ):
        a[i,j] = 2.0
      elif ( j == i + 1 ):
        a[i,j] = 1.0
      else:
        a[i,j] = 0.0

  return a

def oto_condition ( n ):

#*****************************************************************************80
#
## oto_condition() returns the L1 condition of the OTO matrix.
#
#  Discussion:
#
#    I knew it had to be possible to work out this condition number!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  if ( n == 1 ):
    a_norm = 2.0
  elif ( n == 2 ):
    a_norm = 3.0
  else:
    a_norm = 4.0

  n1 = ( n + 1 ) // 2
  n2 = ( n + 2 ) // 2

  s = 0
  i1 = n1
  i2 = 0

  while ( i2 < n2 ):
    i2 = i2 + 1
    s = s + i1 * i2

  while ( 1 < i1 ):
    i1 = i1 - 1
    s = s + i1 * i2

  b_norm = ( float ) ( s ) / ( float ) ( n + 1 )

  value = a_norm * b_norm

  return value

def oto_determinant ( n ):

#*****************************************************************************80
#
## oto_determinant() returns the determinant of the OTO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = float ( n + 1 )

  return value

def oto_eigen_right ( n ):

#*****************************************************************************80
#
## oto_eigen_right() returns the right eigenvectors of the OTO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the right eigenvector matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( ( i + 1 ) * ( j + 1 ) ) * np.pi / float ( n + 1 )
      a[i,j] = r8_mop ( i + j ) * np.sqrt ( 2.0 / float ( n + 1 ) ) \
        * np.sin ( angle )

  return a

def oto_eigenvalues ( n ):

#*****************************************************************************80
#
## oto_eigenvalues() returns the eigenvalues of the OTO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    lam[i] = 4.0 * ( np.sin ( angle ) ) ** 2

  return lam

def oto_inverse ( n ):

#*****************************************************************************80
#
## oto_inverse() returns the inverse of the OTO matrix.
#
#  Formula:
#
#    if ( I <= J )
#      A(I,J) = (-1)^(I+J) * I * (N-J+1) / (N+1)
#    else
#      A(I,J) = (-1)^(I+J) * J * (N-I+1) / (N+1)
#
#  Example:
#
#    N = 4
#
#             4 -3  2 -1
#    (1/5) * -3  6 -4  2
#             2 -4  6 -3
#            -1  2 -3  4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = r8_mop ( i + j ) * float ( ( i + 1 ) * ( n - j ) ) / float ( n + 1 )
      else:
        a[i,j] = r8_mop ( i + j ) * float ( ( j + 1 ) * ( n - i ) ) \
          / float ( n + 1 )


  return a

def oto_llt ( n ):

#*****************************************************************************80
#
## oto_llt() returns the Cholesky factor of the OTO matrix.
#
#  Example:
#
#    N = 5
#
#   1.4142         0         0         0         0
#   0.7071    1.2247         0         0         0
#        0    0.8165    1.1547         0         0
#        0         0    0.8660    1.1180         0
#        0         0         0    0.8944    1.0954
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np
  
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = np.sqrt ( float ( i + 2 ) / float ( i + 1 ) )

  for i in range ( 1, n ):
    a[i,i-1] = np.sqrt ( float ( i ) / float ( i + 1 ) )

  return a

def oto_lu ( n ):

#*****************************************************************************80
#
## oto_lu() returns the LU factors of the OTO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real L(N,N), U(N,N), the factors.
#
  import numpy as np

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    l[j,j] = 1.0
  for j in range ( 0, n - 1 ):
    l[j+1,j] = float ( j + 1 ) / float ( j + 2 )

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    u[j,j] = float ( j + 2 ) / float ( j + 1 )
  for j in range ( 1, n ):
    u[j-1,j] = 1.0

  return l, u

def oto_plu ( n ):

#*****************************************************************************80
#
## oto_plu() returns the PLU factors of the OTO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    l[j,j] = 1.0
  for j in range ( 0, n - 1 ):
    l[j+1,j] = float ( j + 1 ) / float ( j + 2 )

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    u[j,j] = float ( j + 2 ) / float ( j + 1 )
  for j in range ( 1, n ):
    u[j-1,j] = 1.0

  return p, l, u

def oto_test ( ):

#*****************************************************************************80
#
## oto_test() tests oto_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'oto_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  oto_matrix() computes the OTO matrix.' )

  m = 5
  n = m
  a = oto_matrix ( m, n )
  r8mat_print ( m, n, a, '  OTO matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'oto_test' )
  print ( '  Normal end of execution.' )
  return

def parter_matrix ( m, n ):

#*****************************************************************************80
#
## parter_matrix() returns the PARTER matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( i - j + 0.5 )
#
#  Example:
#
#    N = 5
#
#     2   -2  -2/3 -2/5 -2/7
#    2/3   2   -2  -2/3 -2/5
#    2/5  2/3   2   -2  -2/3
#    2/7  2/5  2/3   2   -2
#    2/9  2/7  2/5  2/3   2
#
#  Properties:
#
#    The diagonal entries are all 2, the first superdiagonals all -2.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is generally not symmetric: A' ~= A.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is a special case of the Cauchy matrix.
#
#    Most of the singular values are very close to Pi.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Seymour Parter,
#    On the distribution of the singular values of Toeplitz matrices,
#    Linear Algebra and Applications,
#    Volume 80, August 1986, pages 115-130.
#
#    Evgeny Tyrtyshnikov,
#    Cauchy-Toeplitz matrices and some applications,
#    Linear Algebra and Applications,
#    Volume 149, 15 April 1991, pages 1-18.
#
#  Input:
#
#    integer M, N, the order of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / ( float ( i - j ) + 0.5 )

  return a

def parter_determinant ( n ):

#*****************************************************************************80
#
## parter_determinant() returns the determinant of the PARTER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  top = 1.0
  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      top = top * float ( j - i ) * float ( i - j )

  bottom = 1.0
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      bottom = bottom * ( float ( i - j ) + 0.5 )

  value = top / bottom

  return value

def parter_inverse ( n ):

#*****************************************************************************80
#
## parter_inverse() returns the inverse of the PARTER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n):
    for j in range ( 0, n ):

      top = 1.0
      bot1 = 1.0
      bot2 = 1.0

      for k in range ( 0, n ):

        top = top * ( 0.5 + float ( j - k ) ) * ( 0.5 + float ( k - i ) )

        if ( k != j ):
          bot1 = bot1 * float ( j - k )

        if ( k != i ):
          bot2 = bot2 * float ( k - i )

      a[i,j] = top / ( ( 0.5 + float ( j - i ) ) * bot1 * bot2 )

  return a

def parter_test ( ):

#*****************************************************************************80
#
## parter_test() tests parter_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'parter_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  parter_matrix() computes the PARTER matrix.' )

  m = 4
  n = m

  a = parter_matrix ( m, n )
  r8mat_print ( m, n, a, '  PARTER matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'parter_test' )
  print ( '  Normal end of execution.' )
  return

def pascal1_matrix ( n ):

#*****************************************************************************80
#
## pascal1_matrix() returns the PASCAL1 matrix.
#
#  Formula:
#
#    if ( J = 1 )
#      A(I,J) = 1
#    elseif ( I = 0 )
#      A(1,J) = 0
#    else
#      A(I,J) = A(I-1,J) + A(I-1,J-1)
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  0
#    1  1  0  0  0
#    1  2  1  0  0
#    1  3  3  1  0
#    1  4  6  4  1
#
#  Properties:
#
#    A is a "chunk" of the Pascal binomial combinatorial triangle.
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular.
#
#    A is lower triangular.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    (0, 0, ..., 0, 1) is an eigenvector.
#
#    The inverse of A is the same as A, except that entries in "odd"
#    positions have changed sign:
#
#      B(I,J) = (-1)^(I+J) * A(I,J)
#
#    The product A*A' is a Pascal matrix
#    of the sort created by subroutine PASCAL2.
#
#    Let the matrix C have the same entries as A, except that
#    the even columns are negated.  Then Inverse(C) = C, and
#    C' * C = the Pascal matrix created by PASCAL2.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.15,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 43, 
#    LC: QA263.G68.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  return a

def pascal1_condition ( n ):

#*****************************************************************************80
#
## pascal1_condition() returns the L1 condition of the PASCAL1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  from scipy.special import comb

  nhalf = ( ( n + 1 ) // 2 )
  a_norm = comb ( n, nhalf )
  b_norm = comb ( n, nhalf )
  value = a_norm * b_norm

  return value

def pascal1_determinant ( n ):

#*****************************************************************************80
#
## pascal1_determinant() returns the determinant of the PASCAL1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def pascal1_inverse ( n ):

#*****************************************************************************80
#
## pascal1_inverse() returns the inverse of the PASCAL1 matrix.
#
#  Formula:
#
#    if ( J = 1 )
#      A(I,J) = (-1)^(I+J)
#    elseif ( I = 1 )
#      A(I,J) = 0
#    else
#      A(I,J) = A(I-1,J) - A(I,J-1)
#
#  Example:
#
#    N = 5
#
#     1  0  0  0  0
#    -1  1  0  0  0
#     1 -2  1  0  0
#    -1  3 -3  1  0
#     1 -4  6 -4  1
#
#  Properties:
#
#    A is nonsingular.
#
#    A is lower triangular.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    (0, 0, ..., 0, 1) is an eigenvector.
#
#    The inverse of A is the same as A, except that entries in "odd"
#    positions have changed sign:
#
#      B(I,J) = (-1)^(I+J) * A(I,J)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == 0 ):
        a[i,j] = r8_mop ( i + j )
      elif ( 0 < i ):
        a[i,j] = a[i-1,j-1] - a[i-1,j]

  return a

def pascal1_test ( ):

#*****************************************************************************80
#
## pascal1_test() tests pascal1_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pascal1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pascal1_matrix() computes the PASCAL1 matrix.' )

  m = 5
  n = m

  a = pascal1_matrix ( n )
 
  r8mat_print ( m, n, a, '  PASCAL1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'pascal1_test' )
  print ( '  Normal end of execution.' )
  return

def pascal2_matrix ( n ):

#*****************************************************************************80
#
## pascal2_matrix() returns the PASCAL2 matrix.
#
#  Formula:
#
#    If ( I = 1 or J = 1 )
#      A(I,J) = 1
#    else
#      A(I,J) = A(I-1,J) + A(I,J-1)
#
#  Example:
#
#    N = 5
#
#    1 1  1  1  1
#    1 2  3  4  5
#    1 3  6 10 15
#    1 4 10 20 35
#    1 5 15 35 70
#
#  Properties:
#
#    A is a "chunk" of the Pascal binomial combinatorial triangle.
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is nonsingular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    Eigenvalues of A occur in reciprocal pairs.
#
#    The condition number of A is approximately 16^N / ( N*PI ).
#
#    The elements of the inverse of A are integers.
#
#    A(I,J) = (I+J-2)! / ( (I-1)! * (J-1)! )
#
#    The Cholesky factor of A is a lower triangular matrix R,
#    such that A = R * R'.  The matrix R is a Pascal
#    matrix of the type generated by subroutine PASCAL.  In other
#    words, PASCAL2 = PASCAL * PASCAL'.
#
#    If the (N,N) entry of A is decreased by 1, the matrix is singular.
#
#    Gregory and Karney consider a generalization of this matrix as
#    their test matrix 3.7, in which every element is multiplied by a
#    nonzero constant K.  They point out that if K is the reciprocal of
#    an integer, then the inverse matrix has all integer entries.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Brawer, Magnus Pirovino,
#    The linear algebra of the Pascal matrix,
#    Linear Algebra and Applications,
#    Volume 174, 1992, pages 13-23.
#
#    Robert Gregory, David Karney,
#    Example 3.7,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 32, 
#    LC: QA263.G68.
#
#    Nicholas Higham,
#    Accuracy and Stability of Numerical Algorithms,
#    Society for Industrial and Applied Mathematics,
#    Philadelphia, PA, USA, 1996; section 26.4.
#
#    Sam Karlin,
#    Total Positivity, Volume 1,
#    Stanford University Press, 1968.
#
#    Morris Newman, John Todd,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    Heinz Rutishauser,
#    On test matrices,
#    Programmation en Mathematiques Numeriques,
#    Centre National de la Recherche Scientifique,
#    1966, pages 349-365.
#
#    John Todd,
#    Basic Numerical Mathematics, Vol. 2: Numerical Algebra,
#    Academic Press, 1977, page 172.
#
#    HW Turnbull,
#    The Theory of Determinants, Matrices, and Invariants,
#    Blackie, 1929.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):
        a[i,j] = 1.0
      elif ( j == 0 ):
        a[i,j] = 1.0
      else:
        a[i,j] = a[i,j-1] + a[i-1,j]

  return a

def pascal2_determinant ( n ):

#*****************************************************************************80
#
## pascal2_determinant() returns the determinant of the PASCAL2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def pascal2_inverse ( n ):

#*****************************************************************************80
#
## pascal2_inverse() returns the inverse of the PASCAL2 matrix.
#
#  Formula:
#
#    A(I,J) = sum ( max(I,J) <= K <= N )
#      (-1)^(J+I) * COMB(K-1,I-1) * COMB(K-1,J-1)
#
#  Example:
#
#    N = 5
#
#      5 -10  10  -5   1
#    -10  30 -35  19  -4
#     10 -35  46 -27   6
#     -5  19 -27  17  -4
#      1  -4   6  -4   1
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    The first row sums to 1, the others to 0.
#
#    The first column sums to 1, the others to 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  from scipy.special import comb
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      klo = max ( i + 1, j + 1 )
      for k in range ( klo, n + 1 ):
        a[i,j] = a[i,j] + r8_mop ( i + j ) * comb ( k - 1, i ) \
          * comb ( k - 1, j )

  return a

def pascal2_llt ( n ):

#*****************************************************************************80
#
## pascal2_llt() returns the Cholesky factor of the PASCAL2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  a = pascal1_matrix ( n )

  return a

def pascal2_lu ( n ):

#*****************************************************************************80
#
## pascal2_lu() returns the LU factors of the PASCAL2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real L(N,N), U(N,N), the factors.
#
  import numpy as np

  l = pascal1_matrix ( n )

  u = np.transpose ( l )

  return l, u

def pascal2_plu ( n ):

#*****************************************************************************80
#
## pascal2_plu() returns the PLU factors of the PASCAL2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = pascal1_matrix ( n )

  u = np.transpose ( l )

  return p, l, u

def pascal2_test ( ):

#*****************************************************************************80
#
## pascal2_test() tests pascal2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pascal2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pascal2_matrix() computes the PASCAL2 matrix.' )

  m = 5
  n = m

  a = pascal2_matrix ( n )
 
  r8mat_print ( m, n, a, '  PASCAL2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'pascal2_test' )
  print ( '  Normal end of execution.' )
  return

def pascal3_matrix ( n, alpha ):

#*****************************************************************************80
#
## pascal3_matrix() returns the PASCAL3 matrix.
#
#  Formula:
#
#    if ( J = 1 )
#      A(I,J) = 1
#    elseif ( I = 0 )
#      A(1,J) = 0
#    else
#      A(I,J) =  ALPHA * A(I-1,J) + A(I-1,J-1) )
#
#  Example:
#
#    N = 5, ALPHA = 2
#
#     1   0   0   0   0
#     2   1   0   0   0
#     4   4   1   0   0
#     8  12   6   1   0
#    16  32  24   8   1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A[0] is the identity matrix.
#
#    A[1] is the usual (lower triangular) Pascal matrix.
#
#    A is nonsingular.
#
#    A is lower triangular.
#
#    If ALPHA is integral, then A is integral.
#    If A is integral, then det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    (0, 0, ..., 0, 1) is an eigenvector.
#
#    The inverse of A[ALPHA] is A[-ALPHA].
#
#    A[ALPHA] * A[BETA] = A[ALPHA*BETA].
#
#    A[1/2] is the "square root" of A[1], and so on.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gregory Call, Daniel Velleman,
#    Pascal's Matrices,
#    American Mathematical Monthly,
#    Volume 100, Number 4, April 1993, pages 372-376.
#
#  Input:
#
#    integer N, the order of A.
#
#    real ALPHA, the parameter.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):

        if ( j == 0 ):
          a[i,j] = 1.0
        else:
          a[i,j] = 0.0

      elif ( j == 0 ):

        a[i,j] = alpha * a[i-1,j]

      else:

        a[i,j] = a[i-1,j-1] + alpha * a[i-1,j]

  return a

def pascal3_condition ( n, alpha ):

#*****************************************************************************80
#
## pascal3_condition() returns the L1 condition of the PASCAL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, the scalar defining A.  
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a = pascal3_matrix ( n, alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def pascal3_determinant ( n, alpha ):

#*****************************************************************************80
#
## pascal3_determinant() returns the determinant of the PASCAL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, the scalar defining A.  
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def pascal3_inverse ( n, alpha ):

#*****************************************************************************80
#
## pascal3_inverse() returns the inverse of the PASCAL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real ALPHA, the parameter.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):

        if ( j == 0 ):
          a[i,j] = 1.0

      elif ( j == 0 ):

        a[i,j] = - alpha * a[i-1,j]

      else:

        a[i,j] = a[i-1,j-1] - alpha * a[i-1,j]

  return a

def pascal3_test ( ):

#*****************************************************************************80
#
## pascal3_test() tests pascal3_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pascal3_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pascal3_matrix() computes the PASCAL3 matrix.' )

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )

  a = pascal3_matrix ( n, alpha )
  r8mat_print ( m, n, a, '  PASCAL3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'pascal3_test' )
  print ( '  Normal end of execution.' )
  return

def pei_matrix ( alpha, n ):

#*****************************************************************************80
#
## pei_matrix() returns the PEI matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1.0 + ALPHA
#    else
#      A(I,J) = 1.0
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#    3 1 1 1 1
#    1 3 1 1 1
#    1 1 3 1 1
#    1 1 1 3 1
#    1 1 1 1 3
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is positive definite for 0 < ALPHA.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A is singular if and only if ALPHA = 0 or ALPHA = -N.
#
#    A becomes more ill-conditioned as ALPHA approaches 0.
#
#    The condition number under the spectral norm is 
#      abs ( ( ALPHA + N ) / ALPHA )
#
#    The eigenvalues of A are
#
#      LAMBDA(1:N-1) = ALPHA
#      LAMBDA(N) = ALPHA + N
#
#    A has constant row sum of ALPHA + N.
#
#    Because it has a constant row sum of ALPHA + N,
#    A has an eigenvalue of ALPHA + N, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A has constant column sum of ALPHA + N.
#
#    Because it has a constant column sum of ALPHA + N,
#    A has an eigenvalue of ALPHA + N, and
#    a (left) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    The eigenvectors are:
#
#      V1 = 1 / sqrt ( N )       * ( 1, 1, 1, ... , 1 )
#      VR = 1 / sqrt ( R * (R-1) ) * ( 1, 1, 1, ... 1, -R+1, 0, 0, 0, ... 0 )
#
#    where the "-R+1" occurs at index R.
#
#    det ( A ) = ALPHA^(N-1) * ( N + ALPHA ).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Morris Newman, John Todd,
#    Example A3,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    ML Pei,
#    A test matrix for inversion procedures,
#    Communications of the ACM,
#    Volume 5, 1962, page 508.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    real ALPHA, the scalar that defines the Pei matrix.  A
#    typical value of ALPHA is 1.0.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = 1.0 + alpha
      else:
        a[i,j] = 1.0

  return a

def pei_condition ( alpha, n ):

#*****************************************************************************80
#
## pei_condition() returns the L1 condition of the PEI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#
#    integer N, the order of A.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = abs ( alpha + 1.0 ) + n - 1
  b_norm = ( abs ( alpha + n - 1.0 ) + n - 1.0 ) \
    / abs ( alpha * ( alpha + n ) )
  value = a_norm * b_norm

  return value

def pei_determinant ( alpha, n ):

#*****************************************************************************80
#
## pei_determinant() returns the determinant of the PEI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar defining A.  
#
#    integer N, the order of A.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = alpha ** ( n - 1 ) * ( alpha + n )

  return value

def pei_eigen_right ( alpha, n ):

#*****************************************************************************80
#
## pei_eigen_right() returns the right eigenvectors of the PEI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar that defines A.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real X(N,N), the right eigenvectors.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )

  for j in range ( 0, n - 1 ):
    x[  0,j] = +1.0
    x[j+1,j] = -1.0

  for i in range ( 0, n ):
    x[i,n-1] = 1.0

  return x

def pei_eigenvalues ( alpha, n ):

#*****************************************************************************80
#
## pei_eigenvalues() returns the eigenvalues of the Pei matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the scalar that defines the Pei matrix.  A
#    typical value of ALPHA is 1.0.
#
#    integer N, the order of A.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n - 1 ):
    lam[i] = alpha

  lam[n-1] = alpha + float ( n )

  return lam

def pei_inverse ( alpha, n ):

#*****************************************************************************80
#
## pei_inverse() returns the inverse of the Pei matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = (ALPHA+N-1) / ( (ALPHA+1)*(ALPHA+N-1)-(N-1) )
#    else
#      A(I,J) =          -1 / ( (ALPHA+1)*(ALPHA+N-1)-(N-1) )
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#            6 -1 -1 -1 -1
#           -1  6 -1 -1 -1
#    1/14 * -1 -1  6 -1 -1
#           -1 -1 -1  6 -1
#           -1 -1 -1 -1  6
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is a "combinatorial" matrix.  See routine COMBIN.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A has constant row sum.
#
#    Because it has a constant row sum of 1 / ( ALPHA + N ),
#    A has an eigenvalue of 1 / ( ALPHA + N ), and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A has constant column sum.
#
#    Because it has constant column sum of 1 / ( ALPHA + N ),
#    A has an eigenvalue of 1 / ( ALPHA + N ), and
#    a (left) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    The eigenvalues of A are
#      LAMBDA(1:N-1) = 1 / ALPHA
#      LAMBDA(N) = 1 / ( ALPHA + N )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    ML Pei,
#    A test matrix for inversion procedures,
#    Communications of the ACM,
#    Volume 5, 1962, page 508.
#
#  Input:
#
#    real ALPHA, the scalar that defines the inverse 
#    of the Pei matrix.
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  bottom = ( alpha + 1.0 ) * ( alpha + n - 1.0 ) - n + 1.0

  if ( bottom == 0.0 ):
    print ( '' )
    print ( 'pei_inverse - Fatal error!' )
    print ( '  The matrix is not invertible.' )
    print ( '  (ALPHA+1)*(ALPHA+N-1)-N+1 is zero.' )
    raise Exception ( 'pei_inverse - Fatal error!' )

  alpha1 = ( alpha + ( n ) - 1.0 ) / bottom
  beta1 = - 1.0 / bottom

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = alpha1
      else:
        a[i,j] = beta1

  return a

def pei_test ( ):

#*****************************************************************************80
#
## pei_test() tests pei_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pei_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pei_matrix() computes the PEI matrix.' )

  m = 5
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  alpha = alpha_lo + ( alpha_hi - alpha_lo ) * np.random.rand ( )

  a = pei_matrix ( alpha, n )
  r8mat_print ( m, n, a, '  PEI matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'pei_test' )
  print ( '  Normal end of execution.' )
  return

def permutation_random_matrix ( n, key ):

#*****************************************************************************80
#
## permutation_random_matrix() returns the permutation_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = identity_matrix ( n, n )

  np.random.seed ( key )

  for i in range ( 0, n ):
    i4_lo = i
    i4_hi = n - 1
    i2 = np.random.randint ( i, n )
    if ( i2 != i ):
      for j in range ( 0, n ):
        t = a[i,j]
        a[i,j] = a[i2,j]
        a[i2,j] = t

  return a

def permutation_random_determinant ( n, key ):

#*****************************************************************************80
#
## permutation_random_determinant(): determinant of permutation_random matrix.
#
#  Discussion:
#
#    This routine will only work properly if it is given as input the
#    same value of SEED that was given to permutation_random.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real VALUE, the determinant.
#
  a = permutation_random_matrix ( n, key )

  value = 1.0

  for i in range ( 0, n ):

    found = False

    for i2 in range ( i, n ):

      if ( a[i2,i] == 1.0 ):
        found = True
        if ( i2 != i ):
          for j in range ( 0, n ):
            t       = a[i2,j]
            a[i2,j] = a[i,j]
            a[i,j]  = t
          value = - value

    if ( not found ):
      print ( '' )
      print ( 'permutation_random_determinant - Fatal error!' )
      print ( '  Permutation matrix is illegal.' )
      raise Exception ( 'permutation_random_determinant - Fatal error!' )

  return value

def permutation_random_inverse ( n, key ):

#*****************************************************************************80
#
## permutation_random_inverse(): inverse of permutation_random matrix.
#
#  Discussion:
#
#    This routine will only work properly if it is given as input the
#    same value of SEED that was given to permutation_random.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the inverse matrix.
#
  import numpy as np

  a = permutation_random_matrix ( n, key )
 
  a = np.transpose ( a )

  return a

def permutation_random_test ( ):

#*****************************************************************************80
#
## permutation_random_test() tests permutation_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'permutation_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  permutation_random_matrix() computes the permutation_random matrix.' )

  n = 5

  key = 123456789
  a = permutation_random_matrix ( n, key )
  r8mat_print ( n, n, a, '  permutation_random matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'permutation_random_test' )
  print ( '  Normal end of execution.' )
  return

def householder_real ( x ):

#*****************************************************************************80
#
## householder_real(): computes a Householder transformation for a real vector.
#
    """(v, tau, alpha) = householder_real(x)

    Compute a Householder transformation such that
    (1-tau v v^T) x = alpha e_1
    where x and v a real vectors, tau is 0 or 2, and
    alpha a real number (e_1 is the first unit vector)
    """
    import numpy as np
    import scipy.linalg as la
    import scipy.sparse as sp
    import math
    import cmath
    import numpy.linalg
    import numpy.matlib

    assert x.shape[0]>0

    sigma = np.dot(x[1:],x[1:])

    if sigma == 0:
        return (np.zeros(x.shape[0]), 0, x[0])
    else:
        norm_x=math.sqrt(x[0]**2+sigma)

        v=x.copy()

        #depending on whether x[0] is positive or negatvie
        #choose the sign
        if x[0]<=0:
            v[0]-=norm_x
            alpha=+norm_x
        else:
            v[0]+=norm_x
            alpha=-norm_x

        v/=np.linalg.norm(v)

        return (v, 2, alpha)

def householder_complex(x):

#*****************************************************************************80
#
## householder_complex(): Householder transformation for a complex vector.
#
    """(v, tau, alpha) = householder_real(x)

    Compute a Householder transformation such that
    (1-tau v v^T) x = alpha e_1
    where x and v a complex vectors, tau is 0 or 2, and
    alpha a complex number (e_1 is the first unit vector)
    """

    import numpy as np
    import scipy.linalg as la
    import scipy.sparse as sp
    import math
    import cmath
    import numpy.linalg
    import numpy.matlib

    assert x.shape[0]>0

    sigma=np.dot(np.conj(x[1:]), x[1:])

    if sigma==0:
        return (np.zeros(x.shape[0]), 0, x[0])
    else:
        norm_x=cmath.sqrt(x[0].conjugate()*x[0]+sigma)

        v=x.copy()

        phase=cmath.exp(1j*math.atan2(x[0].imag, x[0].real))

        v[0]+=phase*norm_x

        v/=np.linalg.norm(v)

    return (v, 2, -phase*norm_x)

def skew_tridiagonalize ( A, overwrite_a = False, calc_q = True ):

#*****************************************************************************80
#
## skew_tridiagonalize() tridiagonalizes a skew-symmetric matrix.
#
    """ T, Q = skew_tridiagonalize(A, overwrite_a, calc_q=True)

    or

    T = skew_tridiagonalize(A, overwrite_a, calc_q=False)

    Bring a real or complex skew-symmetric matrix (A=-A^T) into
    tridiagonal form T (with zero diagonal) with a orthogonal
    (real case) or unitary (complex case) matrix U such that
    A = Q T Q^T
    (Note that Q^T and *not* Q^dagger also in the complex case)

    A is overwritten if overwrite_a=True (default: False), and
    Q only calculated if calc_q=True (default: True)
    """

    import numpy as np
    import scipy.linalg as la
    import scipy.sparse as sp
    import math
    import cmath
    import numpy.linalg
    import numpy.matlib

    #Check if matrix is square
    assert A.shape[0] == A.shape[1] > 0
    #Check if it's skew-symmetric
    assert abs((A+A.T).max())<1e-14

    n = A.shape[0]
    A = np.asarray(A)  #the slice views work only properly for arrays

    #Check if we have a complex data type
    if np.issubdtype(A.dtype, np.complexfloating):
        householder = householder_complex
    elif not np.issubdtype(A.dtype, np.number):
        raise TypeError("pfaffian() can only work on numeric input")
    else:
        householder = householder_real

    if not overwrite_a:
        A = A.copy()

    if calc_q:
        Q = np.eye(A.shape[0], dtype=A.dtype)

    for i in range(A.shape[0]-2):
        #Find a Householder vector to eliminate the i-th column
        v, tau, alpha = householder(A[i+1:,i])
        A[i+1, i] = alpha
        A[i, i+1] = -alpha
        A[i+2:, i] = 0
        A[i, i+2:] = 0

        #Update the matrix block A(i+1:N,i+1:N)
        w = tau*np.dot(A[i+1:, i+1:], v.conj())
        A[i+1:,i+1:]+=np.outer(v,w)-np.outer(w,v)

        if calc_q:
            #Accumulate the individual Householder reflections
            #Accumulate them in the form P_1*P_2*..., which is
            # (..*P_2*P_1)^dagger
            y = tau*np.dot(Q[:, i+1:], v)
            Q[:, i+1:]-=np.outer(y,v.conj())

    if calc_q:
        return (np.asmatrix(A), np.asmatrix(Q))
    else:
        return np.asmatrix(A)

def skew_ltl ( A, overwrite_a = False, calc_l = True, calc_P = True ):

#*****************************************************************************80
#
## skew_ltl tridiagonalizes a skew-symmetric matrix.
#
    """ T, L, P = skew_ltl(A, overwrite_a, calc_q=True)

    Bring a real or complex skew-symmetric matrix (A=-A^T) into
    tridiagonal form T (with zero diagonal) with a lower unit
    triangular matrix L such that
    P A P^T= L T L^T

    A is overwritten if overwrite_a=True (default: False),
    L and P only calculated if calc_l=True or calc_P=True,
    respectively (default: True).
    """

    import numpy as np
    import scipy.linalg as la
    import scipy.sparse as sp
    import math
    import cmath
    import numpy.linalg
    import numpy.matlib

    #Check if matrix is square
    assert A.shape[0] == A.shape[1] > 0
    #Check if it's skew-symmetric
    assert abs((A+A.T).max())<1e-14

    n = A.shape[0]
    A = np.asarray(A)  #the slice views work only properly for arrays

    if not overwrite_a:
        A = A.copy()

    if calc_l:
        L = np.eye(n, dtype=A.dtype)

    if calc_P:
        Pv = np.arange(n)

    for k in range(n-2):
        #First, find the largest entry in A[k+1:,k] and
        #permute it to A[k+1,k]
        kp = k+1+np.abs(A[k+1:,k]).argmax()

        #Check if we need to pivot
        if kp != k+1:
            #interchange rows k+1 and kp
            temp = A[k+1,k:].copy()
            A[k+1,k:] = A[kp,k:]
            A[kp,k:] = temp

            #Then interchange columns k+1 and kp
            temp = A[k:,k+1].copy()
            A[k:,k+1] = A[k:,kp]
            A[k:,kp] = temp

            if calc_l:
                #permute L accordingly
                temp = L[k+1,1:k+1].copy()
                L[k+1,1:k+1] = L[kp,1:k+1]
                L[kp,1:k+1] = temp

            if calc_P:
                #accumulate the permutation matrix
                temp = Pv[k+1]
                Pv[k+1] = Pv[kp]
                Pv[kp] = temp

        #Now form the Gauss vector
        if A[k+1,k] != 0.0:
            tau = A[k+2:,k].copy()
            tau /= A[k+1,k]

            #clear eliminated row and column
            A[k+2:,k] = 0.0
            A[k,k+2:] = 0.0

            #Update the matrix block A(k+2:,k+2)
            A[k+2:,k+2:] += np.outer(tau, A[k+2:,k+1])
            A[k+2:,k+2:] -= np.outer(A[k+2:,k+1], tau)

            if calc_l:
                L[k+2:,k+1] = tau

    if calc_P:
        #form the permutation matrix as a sparse matrix
        P = sp.csr_matrix( (np.ones(n), (np.arange(n), Pv)) )

    if calc_l:
        if calc_P:
            return (np.asmatrix(A), np.asmatrix(L), P)
        else:
            return (np.asmatrix(A), np.asmatrix(L))
    else:
        if calc_P:
            return (np.asmatrix(A), P)
        else:
            return np.asmatrix(A)

def pfaffian ( A, overwrite_a = False, method = 'P' ):

#*****************************************************************************80
#
## pfaffian() computes the Pfaffian of a skew-symmetric matrix.
#
    """ pfaffian(A, overwrite_a=False, method='P')

    Compute the Pfaffian of a real or complex skew-symmetric
    matrix A (A=-A^T). If overwrite_a=True, the matrix A
    is overwritten in the process. This function uses
    either the Parlett-Reid algorithm (method='P', default),
    or the Householder tridiagonalization (method='H')
    """

    import numpy as np
    import scipy.linalg as la
    import scipy.sparse as sp
    import math
    import cmath
    import numpy.linalg
    import numpy.matlib

    #Check if matrix is square
    assert A.shape[0] == A.shape[1] > 0
    #Check if it's skew-symmetric
    assert abs((A+A.T).max())<1e-14
    #Check that the method variable is appropriately set
    assert method == 'P' or method == 'H'

    if method == 'P':
        return pfaffian_ltl(A, overwrite_a)
    else:
        return pfaffian_householder(A, overwrite_a)

def pfaffian_ltl ( A, overwrite_a = False ):

#*****************************************************************************80
#
## pfaffian_ltl() computes the Pfaffian of a skew-symmetric matrix.
#
    """ pfaffian_ltl(A, overwrite_a=False)

    Compute the Pfaffian of a real or complex skew-symmetric
    matrix A (A=-A^T). If overwrite_a=True, the matrix A
    is overwritten in the process. This function uses
    the Parlett-Reid algorithm.
    """

    import numpy as np
    import scipy.linalg as la
    import scipy.sparse as sp
    import math
    import cmath
    import numpy.linalg
    import numpy.matlib

    #Check if matrix is square
    assert A.shape[0] == A.shape[1] > 0
    #Check if it's skew-symmetric
    assert abs((A+A.T).max())<1e-14

    n = A.shape[0]
    A = np.asarray(A)  #the slice views work only properly for arrays

    #Quick return if possible
    if n%2==1:
        return 0

    if not overwrite_a:
        A = A.copy()

    pfaffian_val = 1.0

    for k in range(0, n-1, 2):
        #First, find the largest entry in A[k+1:,k] and
        #permute it to A[k+1,k]
        kp = k+1+np.abs(A[k+1:,k]).argmax()

        #Check if we need to pivot
        if kp != k+1:
            #interchange rows k+1 and kp
            temp = A[k+1,k:].copy()
            A[k+1,k:] = A[kp,k:]
            A[kp,k:] = temp

            #Then interchange columns k+1 and kp
            temp = A[k:,k+1].copy()
            A[k:,k+1] = A[k:,kp]
            A[k:,kp] = temp

            #every interchange corresponds to a "-" in det(P)
            pfaffian_val *= -1

        #Now form the Gauss vector
        if A[k+1,k] != 0.0:
            tau = A[k,k+2:].copy()
            tau /= A[k,k+1]

            pfaffian_val *= A[k,k+1]

            if k+2<n:
                #Update the matrix block A(k+2:,k+2)
                A[k+2:,k+2:] += np.outer(tau, A[k+2:,k+1])
                A[k+2:,k+2:] -= np.outer(A[k+2:,k+1], tau)
        else:
            #if we encounter a zero on the super/subdiagonal, the
            #Pfaffian is 0
            return 0.0

    return pfaffian_val

def pfaffian_householder ( A, overwrite_a = False ):

#*****************************************************************************80
#
## pfaffian_householder() computes the Pfaffian of a skew-symmetric matrix.
#
    """ pfaffian(A, overwrite_a=False)

    Compute the Pfaffian of a real or complex skew-symmetric
    matrix A (A=-A^T). If overwrite_a=True, the matrix A
    is overwritten in the process. This function uses the
    Householder tridiagonalization.

    Note that the function pfaffian_schur() can also be used in the
    real case. That function does not make use of the skew-symmetry
    and is only slightly slower than pfaffian_householder().
    """

    import numpy as np
    import scipy.linalg as la
    import scipy.sparse as sp
    import math
    import cmath
    import numpy.linalg
    import numpy.matlib

    #Check if matrix is square
    assert A.shape[0] == A.shape[1] > 0
    #Check if it's skew-symmetric
    assert abs((A+A.T).max())<1e-14

    n = A.shape[0]

    #Quick return if possible
    if n%2==1:
        return 0

    #Check if we have a complex data type
    if np.issubdtype(A.dtype, np.complexfloating):
        householder=householder_complex
    elif not np.issubdtype(A.dtype, np.number):
        raise TypeError("pfaffian() can only work on numeric input")
    else:
        householder=householder_real

    A = np.asarray(A)  #the slice views work only properly for arrays

    if not overwrite_a:
        A = A.copy()

    pfaffian_val = 1.

    for i in range(A.shape[0]-2):
        #Find a Householder vector to eliminate the i-th column
        v, tau, alpha = householder(A[i+1:,i])
        A[i+1, i] = alpha
        A[i, i+1] = -alpha
        A[i+2:, i] = 0
        A[i, i+2:] = 0

        #Update the matrix block A(i+1:N,i+1:N)
        w = tau*np.dot(A[i+1:, i+1:], v.conj())
        A[i+1:,i+1:]+=np.outer(v,w)-np.outer(w,v)

        if tau!=0:
            pfaffian_val *= 1-tau
        if i%2==0:
            pfaffian_val *= -alpha

    pfaffian_val *= A[n-2,n-1]

    return pfaffian_val

def pfaffian_schur ( A, overwrite_a = False ):

#*****************************************************************************80
#
## pfaffian_schur() computes the Pfaffian of a real antisymmetric matrix.
#
    """Calculate Pfaffian of a real antisymmetric matrix using
    the Schur decomposition. (Hessenberg would in principle be faster,
    but scipy-0.8 messed up the performance for scipy.linalg.hessenberg()).

    This function does not make use of the skew-symmetry of the matrix A,
    but uses a LAPACK routine that is coded in FORTRAN and hence faster
    than python. As a consequence, pfaffian_schur is only slightly slower
    than pfaffian().
    """

    import numpy as np
    import scipy.linalg as la
    import scipy.sparse as sp
    import math
    import cmath
    import numpy.linalg
    import numpy.matlib

    assert np.issubdtype(A.dtype, np.number) and not np.issubdtype(A.dtype, np.complexfloating)

    assert A.shape[0] == A.shape[1] > 0

    assert abs(A + A.T).max() < 1e-14

    #Quick return if possible
    if A.shape[0]%2 == 1:
        return 0

    (t, z) = la.schur(A, output='real', overwrite_a=overwrite_a)
    l = np.diag(t, 1)
    return np.prod(l[::2]) * la.det(z)

def test_pfaffian ( ):

#*****************************************************************************80
#
## test_pfaffian() compares the output of Pfaffian routines and determinant.
#
  import numpy as np
  import scipy.linalg as la
  import scipy.sparse as sp
  import math
  import cmath
  import numpy.linalg
  import numpy.matlib

  print ( '' )
  print ( 'test_pfaffian():' )
  print ( '  Compare the output of Pfaffian routines and determinant.' )
#
#  A is a real antisymmetric matrix.
#
  A = numpy.matlib.rand ( 100, 100 )
  A = A - A.T

  pfa1 = pfaffian ( A )
  pfa2 = pfaffian ( A, method='H' )
  pfa3 = pfaffian_schur ( A )
  deta = numpy.linalg.det ( A )

  print ( '' )
  print ( '  Real matrix:' )
  print ( '    pfaffian(A) =           ', pfa1 )
  print ( '    pfaffian(A,method=H) =  ', pfa2 )
  print ( '    pfaffian_schur(A) =     ', pfa3 )
  print ( '' )
  print ( '    pfaffian(A)^2 =         ', pfa1**2 )
  print ( '    pfaffian(A,method=H)^2 =', pfa2**2 )
  print ( '    pfaffian_schur(A)^2 =   ', pfa3**2 )
  print ( '    numpy.linalg.det(A) =   ', deta )

  assert abs((pfa1-pfa2)/pfa1) < 1e-13
  assert abs((pfa1-pfa3)/pfa1) < 1e-13
  assert abs((pfa1**2-deta)/deta) < 1e-13
#
#  A is a complex skew-symmetric matrix.
#
  A = numpy.matlib.rand(100,100)+1.j*numpy.matlib.rand(100,100)
  A = A-A.T

  pfa1 = pfaffian(A)
  pfa2 = pfaffian(A, method='H')
  deta = numpy.linalg.det(A)

  print ( '' )
  print ( '  Complex matrix:' )
  print ( '    pfaffian(A) =            ', pfa1 )
  print ( '    pfaffian(A,method=H) =   ', pfa2 )
  print ( '' )
  print ( '    pfaffian(A)^2 =          ', pfa1**2 )
  print ( '    pfaffian(A,method=H)^2 = ', pfa2**2 )
  print ( '    numpy.linalg.det(A) =    ', deta )

  assert abs((pfa1-pfa2)/pfa1) < 1e-13
  assert abs((pfa1**2-deta)/deta) < 1e-13

  return

def test_decompositions ( ):

#*****************************************************************************80
#
## test_decompositions() tests the LTL^T and Householder decompositions
#
  import numpy as np
  import scipy.linalg as la
  import scipy.sparse as sp
  import math
  import cmath
  import numpy.linalg
  import numpy.matlib

  print ( '' )
  print ( 'test_decompositions():' )
  print ( '  Test the LTL^T and Householder decompositions.' )
#
#  Real matrices
#
  A = numpy.matlib.rand(100,100)
  A = A-A.T

  T, L, P = skew_ltl(A)

  assert numpy.linalg.norm(P*A*P.T-L*T*L.T)/numpy.linalg.norm(A) < 1e-13

  T, Q = skew_tridiagonalize(A)

  assert numpy.linalg.norm(A-Q*T*Q.T)/numpy.linalg.norm(A) < 1e-13
#
#  Complex matrices
#
  A = numpy.matlib.rand(100,100)+1.0j*numpy.matlib.rand(100,100)
  A = A-A.T

  T, L, P = skew_ltl(A)

  assert numpy.linalg.norm(P*A*P.T-L*T*L.T)/numpy.linalg.norm(A) < 1e-13

  T, Q = skew_tridiagonalize(A)

  assert numpy.linalg.norm(A-Q*T*Q.T)/numpy.linalg.norm(A) < 1e-13

  return

def pfaffian_test ( ):

#*****************************************************************************80
#
## pfaffian_test() tests pfaffian().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pfaffian_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test pfaffian.' )

  test_pfaffian ( )
  test_decompositions ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pfaffian_test:' )
  print ( '  Normal end of execution.' )
  return

def plu_matrix ( n, pivot ):

#*****************************************************************************80
#
## plu_matrix() returns a matrix with known P, L and U factors.
#
#  Example:
#
#    Input:
#
#      N = 5
#      PIVOT = ( 1, 3, 3, 5, 5 )
#
#    Output:
#
#      A:
#
#         11            12           13            14           15
#          1.375         9.75        43.25         44.75        46.25
#          2.75         25           26.25         27.5         28.75
#          0.34375       2.4375       7.71875      17.625       73.125
#          0.6875        4.875       15.4375       60           61.5625
#
#      P:
#
#          1             0            0             0            0
#          0             0            1             0            0
#          0             1            0             0            0
#          0             0            0             0            1
#          0             0            0             1            0
#
#      L:
#
#         1              0            0             0            0
#         0.25           1            0             0            0
#         0.125          0.375        1             0            0
#         0.0625         0.1875       0.3125        1            0
#         0.03125        0.09375      0.15625       0.21875      1
#
#      U:
#
#        11             12           13            14           15
#         0             22           23            24           25
#         0              0           33            34           35
#         0              0            0            44           45
#         0              0            0             0           55
#
#  Note:
#
#    The LINPACK routine DGEFA will factor the above A as:
#
#       11             12             13             14             15
#      -0.125          22             23             24             25
#      -0.25           -0.375         33             34             35
#      -0.03125        -0.09375       -0.15625       44             45
#      -0.0625         -0.1875        -0.3125        -0.21875       55
#
#    and the pivot information in the vector IPVT as:
#
#      ( 1, 3, 3, 5, 5 ).
#
#    The LAPACK routine DGETRF will factor the above A as:
#
#      11              12             13             14             15
#      0.25            22             23             24             25
#      0.125            0.375         33             34             35
#      0.0625           0.1875         0.3125        44             45
#      0.03125          0.09375        0.15625        0.21875       55
#
#   and the pivot information in the vector IPIV as:
#
#     ( 1, 3, 3, 5, 5 ).
#
#  Method:
#
#    The L factor will have unit diagonal, and subdiagonal entries
#    L(I,J) = ( 2 * J - 1 ) / 2^I, which should result in a unique
#    value for every entry.
#
#    The U factor of A will have entries
#    U(I,J) = 10 * I + J, which should result in "nice" entries as long
#    as N < 10.
#
#    The P factor can be deduced by applying the pivoting operations
#    specified by PIVOT in reverse order to the rows of the identity.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer PIVOT(N), the list of pivot rows.  PIVOT(I)
#    must be a value between I and N, reflecting the choice of
#    pivot row on the I-th step.  For no pivoting, set PIVOT(I) = I.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the P, L and U factors
#    of A, as defined by Gaussian elimination with partial pivoting.
#    P is a permutation matrix, L is unit lower triangular, and U
#    is upper trianguler.
#
#    real A(N,N), the matrix.
#
  p, l, u = plu_plu ( n, pivot )

  lu = r8mat_mm ( n, n, n, l, u )
  a = r8mat_mm ( n, n, n, p, lu )

  return a

def plu_determinant ( n, pivot ):

#*****************************************************************************80
#
## plu_determinant() returns the determinant of the PLU matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer PIVOT(N), the list of pivot rows.  PIVOT(I)
#    must be a value between I and N, reflecting the choice of
#    pivot row on the I-th step.  For no pivoting, set PIVOT(I) = I.
#
#  Output:
#
#    real VALUE, the determinant.
#
  p, l, u = plu_plu ( n, pivot )

  value = 1.0
  for i in range ( 0, n ):
    value = value * u[i,i]

  for i in range ( 0, n ):

    found = False
    for i2 in range ( i, n ):

      if ( p[i2,i] == 1.0 ):
        found = True
        if ( i2 != i ):
          for j in range ( 0, n ):
            t       = p[i2,j]
            p[i2,j] = p[i,j]
            p[i,j]  = t
          value = - value

    if ( not found ):
      print ( '' )
      print ( 'plu_determinant - Fatal error!' )
      print ( '  Permutation matrix is illegal.' )
      raise Exception ( 'plu_determinant - Fatal error!' )

  return value

def plu_inverse ( n, pivot ):

#*****************************************************************************80
#
## plu_inverse() returns the inverse of a PLU matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer PIVOT(N), the list of pivot rows.  PIVOT(I)
#    must be a value between I and N, reflecting the choice of
#    pivot row on the I-th step.  For no pivoting, set PIVOT(I) = I.
#
#  Output:
#
#    real A(N,N), the inverse matrix.
#
  import numpy as np

  p, l, u = plu_plu ( n, pivot )

  p_inverse = np.transpose ( p )

  l_inverse = tri_l1_inverse ( n, l )

  u_inverse = tri_u_inverse ( n, u )

  lipi = r8mat_mm ( n, n, n, l_inverse, p_inverse )
  
  a = r8mat_mm ( n, n, n, u_inverse, lipi )

  return a

def plu_plu ( n, pivot ):

#*****************************************************************************80
#
## plu_plu() returns the PLU factors of the PLU matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer PIVOT(N), the list of pivot rows.  PIVOT(I)
#    must be a value between I and N, reflecting the choice of
#    pivot row on the I-th step.  For no pivoting, set PIVOT(I) = I.
#
#  Output:
#
#    real P(N,N), L(N,N), U(N,N), the P, L and U factors.
#
  import numpy as np
#
#  Check that the pivot vector is legal.
#
  for i in range ( 0, n ):

    if ( pivot[i] < i or n - 1 < pivot[i] ):
      print ( '' )
      print ( 'PLU - Fatal error!' )
      print ( '  PIVOT[%d] = %d' % ( i, pivot[i] ) )
      print ( '  but must be between %d and %d.' % ( i, n - 1 ) )
      raise Exception ( 'PLU - Fatal error!' )
#
#  Compute U.
#
  u = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        u[i,j] = float ( 10 * (  i + 1 ) + ( j + 1 ) )
#
#  Compute L.
#
  l = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      l[i,j] = float ( 2 * j + 1 ) / float ( 2 ** ( i + 1 ) )
    l[i,i] = 1.0
#
#  Compute P.
#
  p = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    p[i,i] = 1.0

  for i in range ( n - 1, -1, -1 ):
    k = pivot[i]
    if ( k != i ):
      for j in range ( 0, n ):
        t      = p[i,j]
        p[i,j] = p[k,j]
        p[k,j] = t

  return p, l, u

def plu_test ( ):

#*****************************************************************************80
#
## plu_test() tests plu_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'plu_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  plu_matrix() computes the PLU matrix.' )

  m = 5
  n = m

  pivot = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    i4_lo = i
    i4_hi = n - 1
    pivot[i] = np.random.randint ( i, n )

  a = plu_matrix ( n, pivot )

  r8mat_print ( m, n, a, '  PLU matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'plu_test' )
  print ( '  Normal end of execution.' )
  return

def poisson_matrix ( nrow, ncol ):

#*****************************************************************************80
#
## poisson_matrix() returns the POISSON matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 4.0
#    elseif ( I = J+1 or I = J-1 or I = J+NROW or I = J-NROW )
#      A(I,J) = -1.0
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    NROW = NCOL = 3
#
#     4 -1  0 | -1  0  0 |  0  0  0
#    -1  4 -1 |  0 -1  0 |  0  0  0
#     0 -1  4 |  0  0 -1 |  0  0  0
#     ----------------------------
#    -1  0  0 |  4 -1  0 | -1  0  0
#     0 -1  0 | -1  4 -1 |  0 -1  0
#     0  0 -1 |  0 -1  4 |  0  0 -1
#     ----------------------------
#     0  0  0 | -1  0  0 |  4 -1  0
#     0  0  0 |  0 -1  0 | -1  4 -1
#     0  0  0 |  0  0 -1 |  0 -1  4
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A results from discretizing Poisson's equation with the
#    5 point operator on a square mesh of N points.
#
#    A has eigenvalues
#
#      LAMBDA(I,J) = 4 - 2 * COS(I*PI/(N+1))
#                      - 2 * COS(J*PI/(M+1)), I = 1 to N, J = 1 to M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989
#    (Section 4.5.4).
#
#  Input:
#
#    integer NROW, NCOL, the number of rows and columns 
#    in the grid.
#
#  Output:
#
#    real A(NROW*NCOL,NROW*NCOL), the matrix.
#
  import numpy as np

  n = nrow * ncol

  a = np.zeros ( ( n, n ) )

  i = 0

  for i1 in range ( 0, nrow ):
    for j1 in range ( 0, ncol ):

      if ( 0 < i1 ):
        j = i - ncol
        a[i,j] = -1.0

      if ( 0 < j1 ):
        j = i - 1
        a[i,j] = -1.0

      j = i
      a[i,j] = 4.0

      if ( j1 < ncol - 1 ):
        j = i + 1
        a[i,j] = -1.0

      if ( i1 < nrow - 1 ):
        j = i + ncol
        a[i,j] = -1.0

      i = i + 1

  return a

def poisson_test ( ):

#*****************************************************************************80
#
## poisson_test() tests poisson_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'poisson_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  poisson_matrix() computes the POISSON matrix.' )

  row_num = 3
  col_num = 3

  m = row_num * col_num
  n = m

  a = poisson_matrix ( row_num, col_num )
  r8mat_print ( m, n, a, '  POISSON matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'poisson_test' )
  print ( '  Normal end of execution.' )
  return

def poisson_determinant ( nrow, ncol ):

#*****************************************************************************80
#
## poisson_determinant() returns the determinant of the Poisson matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NROW, NCOL, the number of rows and columns 
#    in the grid.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  cr = np.zeros ( nrow )

  for i in range ( 0, nrow ):
    angle = float ( i + 1 ) * np.pi / float ( nrow + 1 )
    cr[i] = np.cos ( angle )

  cc = np.zeros ( ncol )

  for j in range ( 0, ncol ):
    angle = float ( j + 1 ) * np.pi / float ( ncol + 1 )
    cc[j] = np.cos ( angle )

  value = 1.0

  for i in range ( 0, nrow ):
    for j in range ( 0, ncol):
      value = value * ( 4.0 - 2.0 * cr[i] - 2.0 * cc[j] )

  return value

def poisson_rhs ( nrow, ncol, rhs_num ):

#*****************************************************************************80
#
## poisson_rhs() returns the right hand side of a Poisson linear system.
#
#  Discussion:
#
#    The Poisson matrix is associated with an NROW by NCOL rectangular
#    grid of points.
#
#    Assume that the points are numbered from left to right, bottom to top.
#
#    If the K-th point is in row I and column J, set X = I + J.
#
#    This will be the solution to the linear system.
#
#    The right hand side is easily determined from X.  It is 0 for every
#    interior point.
#
#  Example:
#
#    NROW = 3, NCOL = 3
#
#    ^
#    |  7  8  9
#    J  4  5  6
#    |  1  2  3
#    |
#    +-----I---->
#
#    Solution vector X = ( 2, 3, 4, 3, 4, 5, 4, 5, 6 )
#
#    Right hand side B = ( 2, 2, 8, 2, 0, 6, 8, 6, 14 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989
#    (Section 4.5.4).
#
#  Input:
#
#    integer NROW, NCOL, the number of rows and columns
#    in the grid.
#
#    integer RHS_NUM, the number of right hand sides.
#
#  Output:
#
#    real B(NROW*NCOL,RHS_NUM), the right hand side.
#
  import numpy as np

  n = nrow * ncol

  b = np.zeros ( ( n, 1 ) )

  k = 0

  for i in range ( 0, nrow ):
    for j in range ( 0, ncol ):

      if ( i == 0 ):
        b[k,0] = b[k,0] + i + j + 1

      if ( j == 0 ):
        b[k,0] = b[k,0] + i + j + 1

      if ( j == ncol - 1 ):
        b[k,0] = b[k,0] + i + j + 3

      if ( i == nrow - 1 ):
        b[k,0] = b[k,0] + i + j + 3

      k = k + 1

  return b

def poisson_solution ( nrow, ncol, rhs_num ):

#*****************************************************************************80
#
## poisson_solution() returns the solution of a Poisson linear system.
#
#  Discussion:
#
#    The Poisson matrix is associated with an NROW by NCOL rectangular
#    grid of points.
#
#    Assume that the points are numbered from left to right, bottom to top.
#
#    If the K-th point is in row I and column J, set X = I + J.
#
#    This will be the solution to the linear system.
#
#  Example:
#
#    NROW = 3, NCOL = 3
#
#    ^
#    |  7  8  9
#    J  4  5  6
#    |  1  2  3
#    |
#    +-----I---->
#
#    Solution vector X = ( 2, 3, 4, 3, 4, 5, 4, 5, 6 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989
#    (Section 4.5.4).
#
#  Input:
#
#    integer NROW, NCOL, the number of rows and columns
#    in the grid.
#
#    integer RHS_NUM, the number of right hand sides.
#
#  Output:
#
#    real X(NROW*NCOL,RHS_NUM), the solution.
#
  import numpy as np

  n = nrow * ncol

  x = np.zeros ( ( n, rhs_num ) )

  k = 0
  for i in range ( 0, nrow ):
    for j in range ( 0, ncol ):
      x[k,0] = i + j + 2
      k = k + 1

  return x

def prime ( n ):

#*****************************************************************************80
#
## prime() returns returns any of the first prime_MAX prime numbers.
#
#  Discussion:
#
#    prime_MAX is 1600, and the largest prime stored is 13499.
#
#    Thanks to Bart Vandewoestyne for pointing out a typo, 18 February 2005.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964, pages 870-873.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, pages 95-98.
#
#  Input:
#
#    integer N, the index of the desired prime number.
#    In general, is should be true that 0 <= N <= prime_MAX.
#    N = -1 returns prime_MAX, the index of the largest prime available.
#    N = 0 is legal, returning PRIME = 1.
#
#  Output:
#
#    integer P, the N-th prime.  If N is out of range, P
#    is returned as -1.
#
  prime_max = 1600

  prime_vector = ( (
        2,    3,    5,    7,   11,   13,   17,   19,   23,   29, \
       31,   37,   41,   43,   47,   53,   59,   61,   67,   71, \
       73,   79,   83,   89,   97,  101,  103,  107,  109,  113, \
      127,  131,  137,  139,  149,  151,  157,  163,  167,  173, \
      179,  181,  191,  193,  197,  199,  211,  223,  227,  229, \
      233,  239,  241,  251,  257,  263,  269,  271,  277,  281, \
      283,  293,  307,  311,  313,  317,  331,  337,  347,  349, \
      353,  359,  367,  373,  379,  383,  389,  397,  401,  409, \
      419,  421,  431,  433,  439,  443,  449,  457,  461,  463, \
      467,  479,  487,  491,  499,  503,  509,  521,  523,  541, \
      547,  557,  563,  569,  571,  577,  587,  593,  599,  601, \
      607,  613,  617,  619,  631,  641,  643,  647,  653,  659, \
      661,  673,  677,  683,  691,  701,  709,  719,  727,  733, \
      739,  743,  751,  757,  761,  769,  773,  787,  797,  809, \
      811,  821,  823,  827,  829,  839,  853,  857,  859,  863, \
      877,  881,  883,  887,  907,  911,  919,  929,  937,  941, \
      947,  953,  967,  971,  977,  983,  991,  997, 1009, 1013, \
     1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, \
     1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, \
     1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, \
     1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, \
     1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, \
     1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, \
     1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, \
     1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, \
     1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, \
     1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, \
     1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, \
     1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, \
     1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, \
     1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, \
     2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, \
     2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, \
     2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, \
     2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, \
     2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, \
     2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, \
     2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, \
     2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, \
     2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, \
     2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, \
     2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, \
     2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, \
     3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, \
     3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, \
     3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, \
     3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, \
     3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, \
     3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, \
     3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, \
     3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, \
     3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, \
     3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, \
     3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, \
     3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, \
     4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, \
     4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, \
     4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, \
     4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, \
     4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, \
     4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, \
     4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, \
     4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, \
     4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, \
     4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, \
     4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, \
     4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999, 5003, \
     5009, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, \
     5099, 5101, 5107, 5113, 5119, 5147, 5153, 5167, 5171, 5179, \
     5189, 5197, 5209, 5227, 5231, 5233, 5237, 5261, 5273, 5279, \
     5281, 5297, 5303, 5309, 5323, 5333, 5347, 5351, 5381, 5387, \
     5393, 5399, 5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443, \
     5449, 5471, 5477, 5479, 5483, 5501, 5503, 5507, 5519, 5521, \
     5527, 5531, 5557, 5563, 5569, 5573, 5581, 5591, 5623, 5639, \
     5641, 5647, 5651, 5653, 5657, 5659, 5669, 5683, 5689, 5693, \
     5701, 5711, 5717, 5737, 5741, 5743, 5749, 5779, 5783, 5791, \
     5801, 5807, 5813, 5821, 5827, 5839, 5843, 5849, 5851, 5857, \
     5861, 5867, 5869, 5879, 5881, 5897, 5903, 5923, 5927, 5939, \
     5953, 5981, 5987, 6007, 6011, 6029, 6037, 6043, 6047, 6053, \
     6067, 6073, 6079, 6089, 6091, 6101, 6113, 6121, 6131, 6133, \
     6143, 6151, 6163, 6173, 6197, 6199, 6203, 6211, 6217, 6221, \
     6229, 6247, 6257, 6263, 6269, 6271, 6277, 6287, 6299, 6301, \
     6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359, 6361, 6367, \
     6373, 6379, 6389, 6397, 6421, 6427, 6449, 6451, 6469, 6473, \
     6481, 6491, 6521, 6529, 6547, 6551, 6553, 6563, 6569, 6571, \
     6577, 6581, 6599, 6607, 6619, 6637, 6653, 6659, 6661, 6673, \
     6679, 6689, 6691, 6701, 6703, 6709, 6719, 6733, 6737, 6761, \
     6763, 6779, 6781, 6791, 6793, 6803, 6823, 6827, 6829, 6833, \
     6841, 6857, 6863, 6869, 6871, 6883, 6899, 6907, 6911, 6917, \
     6947, 6949, 6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997, \
     7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, \
     7109, 7121, 7127, 7129, 7151, 7159, 7177, 7187, 7193, 7207, \
     7211, 7213, 7219, 7229, 7237, 7243, 7247, 7253, 7283, 7297, \
     7307, 7309, 7321, 7331, 7333, 7349, 7351, 7369, 7393, 7411, \
     7417, 7433, 7451, 7457, 7459, 7477, 7481, 7487, 7489, 7499, \
     7507, 7517, 7523, 7529, 7537, 7541, 7547, 7549, 7559, 7561, \
     7573, 7577, 7583, 7589, 7591, 7603, 7607, 7621, 7639, 7643, \
     7649, 7669, 7673, 7681, 7687, 7691, 7699, 7703, 7717, 7723, \
     7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829, \
     7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919, \
     7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017, \
     8039, 8053, 8059, 8069, 8081, 8087, 8089, 8093, 8101, 8111, \
     8117, 8123, 8147, 8161, 8167, 8171, 8179, 8191, 8209, 8219, \
     8221, 8231, 8233, 8237, 8243, 8263, 8269, 8273, 8287, 8291, \
     8293, 8297, 8311, 8317, 8329, 8353, 8363, 8369, 8377, 8387, \
     8389, 8419, 8423, 8429, 8431, 8443, 8447, 8461, 8467, 8501, \
     8513, 8521, 8527, 8537, 8539, 8543, 8563, 8573, 8581, 8597, \
     8599, 8609, 8623, 8627, 8629, 8641, 8647, 8663, 8669, 8677, \
     8681, 8689, 8693, 8699, 8707, 8713, 8719, 8731, 8737, 8741, \
     8747, 8753, 8761, 8779, 8783, 8803, 8807, 8819, 8821, 8831, \
     8837, 8839, 8849, 8861, 8863, 8867, 8887, 8893, 8923, 8929, \
     8933, 8941, 8951, 8963, 8969, 8971, 8999, 9001, 9007, 9011, \
     9013, 9029, 9041, 9043, 9049, 9059, 9067, 9091, 9103, 9109, \
     9127, 9133, 9137, 9151, 9157, 9161, 9173, 9181, 9187, 9199, \
     9203, 9209, 9221, 9227, 9239, 9241, 9257, 9277, 9281, 9283, \
     9293, 9311, 9319, 9323, 9337, 9341, 9343, 9349, 9371, 9377, \
     9391, 9397, 9403, 9413, 9419, 9421, 9431, 9433, 9437, 9439, \
     9461, 9463, 9467, 9473, 9479, 9491, 9497, 9511, 9521, 9533, \
     9539, 9547, 9551, 9587, 9601, 9613, 9619, 9623, 9629, 9631, \
     9643, 9649, 9661, 9677, 9679, 9689, 9697, 9719, 9721, 9733, \
     9739, 9743, 9749, 9767, 9769, 9781, 9787, 9791, 9803, 9811, \
     9817, 9829, 9833, 9839, 9851, 9857, 9859, 9871, 9883, 9887, \
     9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973,10007, \
    10009,10037,10039,10061,10067,10069,10079,10091,10093,10099, \
    10103,10111,10133,10139,10141,10151,10159,10163,10169,10177, \
    10181,10193,10211,10223,10243,10247,10253,10259,10267,10271, \
    10273,10289,10301,10303,10313,10321,10331,10333,10337,10343, \
    10357,10369,10391,10399,10427,10429,10433,10453,10457,10459, \
    10463,10477,10487,10499,10501,10513,10529,10531,10559,10567, \
    10589,10597,10601,10607,10613,10627,10631,10639,10651,10657, \
    10663,10667,10687,10691,10709,10711,10723,10729,10733,10739, \
    10753,10771,10781,10789,10799,10831,10837,10847,10853,10859, \
    10861,10867,10883,10889,10891,10903,10909,10937,10939,10949, \
    10957,10973,10979,10987,10993,11003,11027,11047,11057,11059, \
    11069,11071,11083,11087,11093,11113,11117,11119,11131,11149, \
    11159,11161,11171,11173,11177,11197,11213,11239,11243,11251, \
    11257,11261,11273,11279,11287,11299,11311,11317,11321,11329, \
    11351,11353,11369,11383,11393,11399,11411,11423,11437,11443, \
    11447,11467,11471,11483,11489,11491,11497,11503,11519,11527, \
    11549,11551,11579,11587,11593,11597,11617,11621,11633,11657, \
    11677,11681,11689,11699,11701,11717,11719,11731,11743,11777, \
    11779,11783,11789,11801,11807,11813,11821,11827,11831,11833, \
    11839,11863,11867,11887,11897,11903,11909,11923,11927,11933, \
    11939,11941,11953,11959,11969,11971,11981,11987,12007,12011, \
    12037,12041,12043,12049,12071,12073,12097,12101,12107,12109, \
    12113,12119,12143,12149,12157,12161,12163,12197,12203,12211, \
    12227,12239,12241,12251,12253,12263,12269,12277,12281,12289, \
    12301,12323,12329,12343,12347,12373,12377,12379,12391,12401, \
    12409,12413,12421,12433,12437,12451,12457,12473,12479,12487, \
    12491,12497,12503,12511,12517,12527,12539,12541,12547,12553, \
    12569,12577,12583,12589,12601,12611,12613,12619,12637,12641, \
    12647,12653,12659,12671,12689,12697,12703,12713,12721,12739, \
    12743,12757,12763,12781,12791,12799,12809,12821,12823,12829, \
    12841,12853,12889,12893,12899,12907,12911,12917,12919,12923, \
    12941,12953,12959,12967,12973,12979,12983,13001,13003,13007, \
    13009,13033,13037,13043,13049,13063,13093,13099,13103,13109, \
    13121,13127,13147,13151,13159,13163,13171,13177,13183,13187, \
    13217,13219,13229,13241,13249,13259,13267,13291,13297,13309, \
    13313,13327,13331,13337,13339,13367,13381,13397,13399,13411, \
    13417,13421,13441,13451,13457,13463,13469,13477,13487,13499 ) )

  if ( n == -1 ):
    p = prime_max
  elif ( n == 0 ):
    p = 1
  elif ( n <= prime_max ):
    p = prime_vector[n-1]
  else:
    p = -1

  return p

def prime_test ( ):

#*****************************************************************************80
#
## prime_test() tests prime().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'prime_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  prime() returns primes from a table.' )

  n = -1
  prime_max = prime ( n )
  print ( '' )
  print ( '  Number of primes stored is %d' % ( prime_max ) )
  print ( '' )
  print ( '     I    Prime(I)' )
  print ( '' )
  for i in range ( 1, 11 ):
    print ( '    %4d  %6d' % ( i, prime(i) ) )
  print ( '' )
  for i in range ( prime_max - 10, prime_max + 1 ):
    print ( '    %4d  %6d' % ( i, prime(i) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'prime_test' )
  print ( '  Normal end of execution.' )
  return

def projection_random_determinant ( n, k, key ):

#*****************************************************************************80
#
## projection_random_determinant(): determinant of a random projection matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of A.
#
#    integer K: the rank of the matrix.
#    0 <= k <= n.
#
#    integer KEY: a positive integer that selects the data.
#
#  Output:
#
#    real VALUE: the determinant.
#
  if ( k == n ):
    value = 1.0
  else:
    value = 0.0

  return value

def projection_random_matrix ( n, k, key ):

#*****************************************************************************80
#
## projection_random_matrix() returns a random projection matrix.
#
#  Properties:
#
#    If k == n, det(A) = 1;  Otherwise det(A) = 0.
#
#    The only eigenvalues of A are 0 and 1.
#
#    A*A=A.
#
#    A is symmetric.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of A.
#
#    integer K: the rank of the matrix.
#    0 <= k <= n.
#
#    integer KEY: a positive integer that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  np.random.seed ( key )

  V = np.random.rand ( n, k )

  VT = np.transpose ( V )
  VTV = np.matmul ( VT, V )
  VTVinv = np.linalg.inv ( VTV )

  A = np.matmul ( np.matmul ( V, VTVinv ), VT )

  return A

def projection_random_test ( ):

#*****************************************************************************80
#
## projection_random_test() tests projection_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'projection_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  projection_random_matrix() computes the projection_random matrix.' )

  n = 5
  k = 4
  key = 123456789
  a = projection_random_matrix ( n, k, key )
  r8mat_print ( n, n, a, '  projection_random matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'projection_random_test' )
  print ( '  Normal end of execution.' )
  return

def r8col_swap ( m, n, a, j1, j2 ):

#*****************************************************************************80
#
## r8col_swap() swaps two columns of an R8COL.
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
## r8col_swap_test() tests r8col_swap().
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

  a = r8mat_indicator ( m, n )

  r8mat_print ( m, n, a, '  The array:' )

  icol1 = 0
  icol2 = 2

  print ( '' )
  print ( '  Swap columns %d and %d' % ( icol1, icol2 ) )

  a = r8col_swap ( m, n, a, icol1, icol2 )

  r8mat_print ( m, n, a, '  The updated matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_swap_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_house_axh ( n, a, v ):

#*****************************************************************************80
#
## r8mat_house_axh() computes A*H where H is a compact Householder matrix.
#
#  Discussion:
#
#    The Householder matrix H(V) is defined by
#
#      H(V) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real A(N,N), the matrix to be postmultiplied.
#
#    real V(N), a vector defining a Householder matrix.
#
#  Output:
#
#    real AH(N,N), the product A*H.
#
  import numpy as np

  vtv = 0.0
  for i in range ( 0, n ):
    vtv = vtv + v[i] ** 2

  ah = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      ah[i,j] = a[i,j]
      for k in range ( 0, n ):
        ah[i,j] = ah[i,j] - 2.0 * a[i,k] * v[k] * v[j] / vtv
            
  return ah

def r8mat_house_axh_test ( ):

#*****************************************************************************80
#
## r8mat_house_axh_test() tests r8mat_house_axh().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8mat_house_axh_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_house_axh multiplies a matrix A times a' )
  print ( '  compact Householder matrix.' )

  r8_lo = -5.0
  r8_hi = +5.0

  a = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n, n )

  r8mat_print ( n, n, a, '  Matrix A:' )
#
#  Request V, the compact form of the Householder matrix H
#  such that H*A packs column 3 of A.
#
  k = 3
  km1 = k - 1
  a_col = np.zeros ( n )
  for i in range ( 0, n ):
    a_col[i] = a[i,km1]

  v = r8vec_house_column ( n, a_col, km1 )

  r8vec_print ( n, v, '  Compact vector V so column 3 of H*A is packed:' )

  h = r8mat_house_form ( n, v )

  r8mat_print ( n, n, h, '  Householder matrix H:' )
#
#  Compute A*H.
#
  ah = r8mat_house_axh ( n, a, v )

  r8mat_print ( n, n, ah, '  Indirect product A*H:' )
#
#  Compare with a direct calculation.
#
  ah = r8mat_mm ( n, n, n, a, h )

  r8mat_print ( n, n, ah, '  Direct product A*H:' )
#
#  Compute H*A to demonstrate packed column 3:
#
  ha = r8mat_mm ( n, n, n, h, a )

  r8mat_print ( n, n, ha, '  H*A should pack column 3:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_house_axh_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_house_form ( n, v ):

#*****************************************************************************80
#
## r8mat_house_form() constructs a Householder matrix from its compact form.
#
#  Discussion:
#
#    H(v) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real V(N,1), the vector defining the Householder matrix.
#
#  Output:
#
#    real H(N,N), the Householder matrix.
#
  import numpy as np

  v_dot_v = 0.0
  for i in range ( 0, n ):
    v_dot_v = v_dot_v + v[i] * v[i]

  c = - 2.0 / v_dot_v

  h = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    h[j,j] = 1.0
    for i in range ( 0, n ):
      h[i,j] = h[i,j] + c * v[i] * v[j]
            
  return h

def r8mat_house_form_test ( ):

#*****************************************************************************80
#
## r8mat_house_form_test() tests r8mat_house_form().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  v = np.array ( ( 0.0, 0.0, 1.0, 2.0, 3.0 ) )

  print ( '' )
  print ( 'r8mat_house_form_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_house_form forms a Householder' )
  print ( '  matrix from its compact form.' )

  r8vec_print ( n, v, '  Compact vector form V:' )

  h = r8mat_house_form ( n, v )
 
  r8mat_print ( n, n, h, '  Householder matrix H:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_house_form_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_indicator ( m, n ):

#*****************************************************************************80
#
## r8mat_indicator() sets up an indicator R8MAT.
#
#  Discussion:
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
#    03 December 2014
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

def r8mat_indicator_test ( ):

#*****************************************************************************80
#
## r8mat_indicator_test() tests r8mat_indicator().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8mat_indicator_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_indicator creates an "indicator" R8MAT.' )

  m = 5
  n = 4
  a = r8mat_indicator ( m, n )
  r8mat_print ( m, n, a, '  The indicator matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_indicator_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_adjacency ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_adjacency() checks whether A is an adjacency matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    bool VALUE, is True if the matrix is an
#    adjacency matrix.
#
  value = True

  if ( not r8mat_is_square ( m, n, a ) ):
    value = False
    return value

  if ( not r8mat_is_symmetric ( m, n, a ) ):
    value = False
    return value

  if ( not r8mat_is_zero_one ( m, n, a ) ):
    value = False
    return value

  value = True
  return value

def r8mat_is_adjacency_test ( ):

#*****************************************************************************80
#
## r8mat_is_adjacency_test() tests r8mat_is_adjacency().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_adjacency_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_adjacency reports whether a matrix' )
  print ( '  is an adjacency matrix.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_adjacency ( m, n, a )
  print ( '' )
  print ( '  Adjacency = %s' % ( value ) )
#
#  Square, but not symmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 1, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 1, 0, 1, 0 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Not symmetric matrix:' )
  value = r8mat_is_adjacency ( m, n, a )
  print ( '' )
  print ( '  Adjacency = %s' % ( value ) )
#
#  Square, symmetric, but not zero/one.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 2, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 2, 0, 1, 1 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Not zero/one matrix:' )
  value = r8mat_is_adjacency ( m, n, a )
  print ( '' )
  print ( '  Adjacency = %s' % ( value ) )
#
#  Square, symmetric, zero/one.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 1, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 1, 0, 1, 1 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Adjacency matrix:' )
  value = r8mat_is_adjacency ( m, n, a )
  print ( '' )
  print ( '  Adjacency = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_adjacency_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_anticirculant ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_anticirculant() checks whether A is an anticirculant matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the row and column dimensions of 
#    the matrix.  M and N must be positive.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    bool VALUE, is True if the matrix is an
#    anticirculant matrix.
#
  value = True

  for i in range ( 1, m ):
    for j in range ( 0, n ):

      k = ( ( j + i ) % n )

      if ( a[i,j] != a[0,k] ):
        value = False
        return value

  return value

def r8mat_is_anticirculant_test ( ):

#*****************************************************************************80
#
## r8mat_is_anticirculant_test() tests r8mat_is_anticirculant().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_anticirculant_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_anticirculant reports whether a matrix' )
  print ( '  is an anticirculant matrix.' )
#
#  Circulant
#
  m = 4
  n = 5
  a = np.array ( [ \
    [ 0, 1, 2, 3, 4 ], \
    [ 4, 0, 1, 2, 3 ], \
    [ 3, 4, 0, 1, 2 ], \
    [ 2, 3, 4, 0, 1 ] ] )
  r8mat_print ( m, n, a, '  Circulant matrix:' )
  value = r8mat_is_anticirculant ( m, n, a )
  print ( '' )
  print ( '  Anticirculant = %s' % ( value ) )
#
#  Anticirculant.
#
  m = 4
  n = 5
  a = np.array ( [ \
    [ 0, 1, 2, 3, 4 ], \
    [ 1, 2, 3, 4, 0 ], \
    [ 2, 3, 4, 0, 1 ], \
    [ 3, 4, 0, 1, 2 ] ] )
  r8mat_print ( m, n, a, '  Anticirculant matrix:' )
  value = r8mat_is_anticirculant ( m, n, a )
  print ( '' )
  print ( '  Anticirculant = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_anticirculant_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_antipersymmetric ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_antipersymmetric() checks an R8MAT for antipersymmetry.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    A is persymmetric if A(I,J) = -A(N+1-J,N+1-I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    real ERROR_fROBENIUS, the Frobenius error
#    in antipersymmetry, which will be 0 if the matrix is exactly
#    antipersymmetric.
#
  import numpy as np

  if ( not r8mat_is_square ( m, n, a ) ):
    error_frobenius = float ( 'Inf' )
    return error_frobenius

  error_frobenius = 0.0
  for i in range ( 0, m ):
    for j in range ( n - 1, -1, -1 ):
      error_frobenius = error_frobenius + ( a[i,j] + a[n-1-j,m-1-i] ) ** 2

  error_frobenius = np.sqrt ( error_frobenius )

  return error_frobenius

def r8mat_is_antipersymmetric_test ( ):

#*****************************************************************************80
#
## r8mat_is_antipersymmetric_test() tests r8mat_is_antipersymmetric().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_antipersymmetric_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_antipersymmetric reports whether a matrix' )
  print ( '  is antipersymmetric.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_antipersymmetric ( m, n, a )
  print ( '' )
  print ( '  Antipersymmetric = %g' % ( value ) )
#
#  Square, but not antipersymmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 4, 3,-2, 0 ], \
    [-7,-6, 0, 3 ], \
    [ 9, 8, 6,-3 ], \
    [ 0,-7, 7,-4 ] ] )
  r8mat_print ( m, n, a, '  Not antipersymmetric matrix:' )
  value = r8mat_is_antipersymmetric ( m, n, a )
  print ( '' )
  print ( '  Antipersymmetric = %g' % ( value ) )
#
#  Antipersymmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [  4,  3, -2,  0 ], \
    [ -7, -6,  0,  2 ], \
    [  9,  0,  6, -3 ], \
    [  0, -9,  7, -4 ] ] )
  r8mat_print ( m, n, a, '  Antipersymmetric matrix:' )
  value = r8mat_is_antipersymmetric ( m, n, a )
  print ( '' )
  print ( '  Antipersymmetric = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_antipersymmetric_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_antisymmetric ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_antisymmetric() checks whether A is an antisymmetric matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    bool r8mat_is_antisymmetric, True if the matrix is antisymmetric.
#
  import numpy as np

  if ( not r8mat_is_square ( m, n, a ) ):
    return False

  t = 0.0
  for i in range ( 0, m ):
    t = t + a[i,i] ** 2
    for j in range ( i + 1, n ):
      t = t + ( a[i,j] + a[j,i] ) ** 2

  tol = 0.00001

  if ( t < tol ):
    value = True
  else:
    value = False

  return value

def r8mat_is_antisymmetric_test ( ):

#*****************************************************************************80
#
## r8mat_is_antisymmetric_test() tests r8mat_is_antisymmetric().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
 
  print ( '' )
  print ( 'r8mat_is_antisymmetric_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_antisymmetric reports whether a matrix' )
  print ( '  is antisymmetric.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_antisymmetric ( m, n, a )
  print ( '' )
  print ( '  Antisymmetric = %s' % ( value ) )
#
#  Square, but not antisymmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [  0,  5,  1, -2 ], \
    [ -5,  0,  3,  0 ], \
    [  1, -3,  6,  4 ], \
    [  2,  0, -4,  0 ] ] )
  r8mat_print ( m, n, a, '  Not antisymmetric matrix:' )
  value = r8mat_is_antisymmetric ( m, n, a )
  print ( '' )
  print ( '  Antisymmetric = %s' % ( value ) )
#
#  Antisymmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [  0,  5, -1, -2 ], \
    [ -5,  0,  3,  0 ], \
    [  1, -3,  0,  4 ], \
    [  2,  0, -4,  0 ] ] )
  r8mat_print ( m, n, a, '  Antisymmetric matrix:' )
  value = r8mat_is_antisymmetric ( m, n, a )
  print ( '' )
  print ( '  Antisymmetric = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_antisymmetric_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_eigen_left ( n, k, a, x, lam ):

#*****************************************************************************80
#
## r8mat_is_eigen_left() determines the error in a left eigensystem.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    This routine computes the Frobenius norm of
#
#      X * A - LAMBDA * X
#
#    where
#
#      A is an N by N matrix,
#      X is an K by N matrix (each of K columns is an eigenvector)
#      LAMBDA is a K by K diagonal matrix of eigenvalues.
#
#    This routine assumes that A, X and LAMBDA are all real.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer K, the number of eigenvectors.
#    K is usually 1 or N.
#
#    real A(N,N), the matrix.
#
#    real X(K,N), the K eigenvectors.
#
#    real LAM(K), the K eigenvalues.
#
#  Output:
#
#    real VALUE, the Frobenius norm of X * A - LAM * X.
#
  c = r8mat_mm ( k, n, n, x, a )

  for i in range ( 0, k ):
    for j in range ( 0, n ):
      c[i,j] = c[i,j] - lam[i] * x[i,j]

  value = r8mat_norm_fro ( k, n, c )

  return value

def r8mat_is_eigen_left_test ( ):

#*****************************************************************************80
#
## r8mat_is_eigen_left_test() tests r8mat_is_eigen_left().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
#
#  This is the CARRY ( 4.0, 4 ) matrix.
#
  m = 4
  n = m
  a = np.array ( [ \
   [ 0.13671875,   0.60546875,   0.25390625,   0.00390625 ], \
   [ 0.05859375,   0.52734375,   0.39453125,   0.01953125 ], \
   [ 0.01953125,   0.39453125,   0.52734375,   0.05859375 ], \
   [ 0.00390625,   0.25390625,   0.60546875,   0.13671875 ] ] )

  k = 4
  x = np.array ( [ \
    [  1.0,     1.0,     1.0,     1.0 ], \
    [ 11.0,     3.0,    -1.0,    -3.0 ], \
    [ 11.0,    -3.0,    -1.0,     3.0 ], \
    [  1.0,    -1.0,     1.0,    -1.0 ] ] )

  lam = np.array ( [ \
     1.000000000000000, \
     0.250000000000000, \
     0.062500000000000, \
     0.015625000000000 ] )

  print ( '' )
  print ( 'r8mat_is_eigen_left_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_eigen_left tests the error in the left eigensystem' )
  print ( '    A\' * X - X * LAMBDA = 0' )

  r8mat_print ( n, n, a, '  Matrix A:' )
  r8mat_print ( n, k, x, '  Eigenmatrix X:' )
  r8vec_print ( n, lam, '  Eigenvalues LAM:' )

  value = r8mat_is_eigen_left ( n, k, a, x, lam )

  print ( '' )
  print ( '  Frobenius norm of A\'*X-X*LAMBDA is %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_eigen_left_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_eigen_right ( n, k, a, x, lam ):

#*****************************************************************************80
#
## r8mat_is_eigen_right() determines the error in a right eigensystem.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    This routine computes the Frobenius norm of
#
#      A * X - X * LAMBDA
#
#    where
#
#      A is an N by N matrix,
#      X is an N by K matrix (each of K columns is an eigenvector)
#      LAMBDA is a K by K diagonal matrix of eigenvalues.
#
#    This routine assumes that A, X and LAMBDA are all real.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer K, the number of eigenvectors.
#    K is usually 1 or N.
#
#    real A(N,N), the matrix.
#
#    real X(N,K), the K eigenvectors.
#
#    real LAM(K), the K eigenvalues.
#
#  Output:
#
#    real VALUE, the Frobenius norm
#    of the difference matrix A * X - X * LAM, which would be exactly zero
#    if X and LAM were exact eigenvectors and eigenvalues of A.
#
  c = r8mat_mm ( n, n, k, a, x )

  for j in range ( 0, k ):
    for i in range ( 0, n ):
      c[i,j] = c[i,j] - lam[j] * x[i,j]

  value = r8mat_norm_fro ( n, k, c )

  return value

def r8mat_is_eigen_right_test ( ):

#*****************************************************************************80
#
## r8mat_is_eigen_right_test() tests r8mat_is_eigen_right().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
#
#  This is the CARRY ( 4.0, 4 ) matrix.
#
  m = 4
  n = m
  a = np.array ( [ \
   [ 0.13671875,   0.60546875,   0.25390625,   0.00390625 ], \
   [ 0.05859375,   0.52734375,   0.39453125,   0.01953125 ], \
   [ 0.01953125,   0.39453125,   0.52734375,   0.05859375 ], \
   [ 0.00390625,   0.25390625,   0.60546875,   0.13671875 ] ] )

  k = 4
  x = np.array ( [ \
    [ 1.0,     6.0,    11.0,     6.0 ], \
    [ 1.0,     2.0,    -1.0,    -2.0 ], \
    [ 1.0,    -2.0,    -1.0,     2.0 ], \
    [ 1.0,    -6.0,    11.0,    -6.0 ] ] )

  lam = np.array ( [ \
     1.000000000000000, \
     0.250000000000000, \
     0.062500000000000, \
     0.015625000000000 ] )

  print ( '' )
  print ( 'r8mat_is_eigen_right_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_eigen_right tests the error in the right eigensystem' )
  print ( '    A * X - X * LAMBDA = 0' )

  r8mat_print ( n, n, a, '  Matrix A:' )
  r8mat_print ( n, k, x, '  Eigenmatrix X:' )
  r8vec_print ( n, lam, '  Eigenvalues LAM:' )

  value = r8mat_is_eigen_right ( n, k, a, x, lam )

  print ( '' )
  print ( '  Frobenius norm of A*X-X*LAMBDA is %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_eigen_right_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_identity ( n, a ):

#*****************************************************************************80
#
## r8mat_is_identity() determines if a matrix is the identity.
#
#  Discussion:
#
#    The routine returns the Frobenius norm of A - I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix.
#
#  Output:
#
#    real ERROR_fROBENIUS, the Frobenius norm
#    of the difference matrix A - I, which would be exactly zero
#    if A were the identity matrix.
#
  import numpy as np

  error_frobenius = 0.0

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        error_frobenius = error_frobenius + ( a[i,j] - 1.0 ) ** 2
      else:
        error_frobenius = error_frobenius + a[i,j] ** 2

  error_frobenius = np.sqrt ( error_frobenius )

  return error_frobenius

def r8mat_is_identity_test ( ):

#*****************************************************************************80
#
## r8mat_is_identity_test() tests r8mat_is_identity().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_identity_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_identity reports the Frobenius norm difference' )
  print ( '  between a given matrix A and the identity matrix.' )

  n = 4
  a = np.zeros ( [ n, n ] )
  r8mat_print ( n, n, a, '  Zero matrix:' )
  e = r8mat_is_identity ( n, a )
  print ( '' )
  print ( '  Difference is %g' % ( e ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0
  r8mat_print ( n, n, a, '  Identity matrix:' )
  e = r8mat_is_identity ( n, a )
  print ( '' )
  print ( '  Difference is %g' % ( e ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = a[i,j] + float ( i * j ) / 1000
  r8mat_print ( n, n, a, '  Almost identity matrix:' )
  e = r8mat_is_identity ( n, a )
  print ( '' )
  print ( '  Difference is %g' % ( e ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_identity_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_integer ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_integer() checks whether A has only integer entries.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    real ERROR_fROBENIUS, the Frobenius norm of the
#    difference between A and the nearest integer matrix.
#
  import numpy as np

  error_frobenius = 0.0

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      t = a[i,j] - np.round ( a[i,j] )
      error_frobenius = error_frobenius + t * t

  error_frobenius = np.sqrt ( error_frobenius )

  return error_frobenius

def r8mat_is_integer_test ( ):

#*****************************************************************************80
#
## r8mat_is_integer_test() tests r8mat_is_integer().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_integer_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_integer reports the Frobenius norm of the' )
  print ( '  distance between a matrix A and the nearest integer matrix.' )

  m = 5
  n = 4
  a = maxij_matrix ( m, n )
  r8mat_print ( m, n, a, '  MAXIJ matrix:' )
  value = r8mat_is_integer ( m, n, a )
  print ( '' )
  print ( '  Frobenius norm = %g' % ( value ) )

  n = 4
  a = involutory_matrix ( n )
  r8mat_print ( n, n, a, '  INVOLUTORY matrix:' )
  value = r8mat_is_integer ( n, n, a )
  print ( '' )
  print ( '  Frobenius norm = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_integer_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_inverse ( n, a, b ):

#*****************************************************************************80
#
## r8mat_is_inverse() measures the error in a matrix inverse.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    This routine returns the sum of the Frobenius norms of
#      A * B - I and B * A - I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix.
#
#    real B(M,N), the inverse matrix.
#
#  Output:
#
#    real VALUE, the Frobenius norm
#    of the difference matrices A * B - I and B * A - I.
#
  ab = r8mat_mm ( n, n, n, a, b )
  ba = r8mat_mm ( n, n, n, b, a )
  id = identity_matrix ( n, n )
  d1 = r8mat_sub ( n, n, ab, id )
  d2 = r8mat_sub ( n, n, ba, id )
 
  value = r8mat_norm_fro ( n, n, d1 ) \
        + r8mat_norm_fro ( n, n, d2 )

  return value

def r8mat_is_inverse_test ( ):

#*****************************************************************************80
#
## r8mat_is_inverse_test() tests r8mat_is_inverse().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
#
#  This is the BODEWIG matrix.
#
  m = 4
  n = m

  a = np.array ( [ \
    [ 2.0,  1.0,  3.0,  4.0 ], \
    [ 1.0, -3.0,  1.0,  5.0 ], \
    [ 3.0,  1.0,  6.0, -2.0 ], \
    [ 4.0,  5.0, -2.0, -1.0 ] ] )

  b  = np.array ( [ \
    [ -139.0 / 568.0,  165.0 / 568.0,  79.0 / 568.0,  111.0 / 568.0 ], \
    [  165.0 / 568.0, -155.0 / 568.0, -57.0 / 568.0,   -1.0 / 568.0 ], \
    [   79.0 / 568.0,  -57.0 / 568.0,  45.0 / 568.0,  -59.0 / 568.0 ], \
    [  111.0 / 568.0,   -1.0 / 568.0, -59.0 / 568.0,  -11.0 / 568.0 ] ] )

  print ( '' )
  print ( 'r8mat_is_inverse_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_inverse tests the error in a matrix inverse:' )
  print ( '    A * B - I = 0' )
  print ( '    B * A - I = 0' )

  r8mat_print ( m, n, a, '  Matrix A:' )
  r8mat_print ( m, n, b, '  Inverse matrix B:' )

  value = r8mat_is_inverse ( n, a, b  )

  print ( '' )
  print ( '  Frobenius norm of error is %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_inverse_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_llt ( m, n, a, l ):

#*****************************************************************************80
#
## r8mat_is_llt() measures the error in a lower triangular Cholesky factorization.
#
#  Discussion:
#
#    This routine simply returns the Frobenius norm of the M x M matrix:
#      A - L * L' 
#    where L is an M by N lower triangular matrix presumed to be the
#    Cholesky factor of A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the matrix dimensions.
#
#    real A(M,M), the matrix.
#
#    real L(M,N), the Cholesky factor.
#
#  Output:
#
#    real VALUE, the Frobenius norm of A-L*L'.
#

#
#  D = L * L'.
#
  d = r8mat_mmt ( m, n, m, l, l )
#
#  D = A - L * L'
#
  d = r8mat_sub ( m, m, a, d )
#
#  Take the norm
#
  value = r8mat_norm_fro ( m, m, d )

  return value

def r8mat_is_llt_test ( ):

#*****************************************************************************80
#
## r8mat_is_llt_test() tests r8mat_is_llt().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 4
  n = 4
  a = np.array ( [ \
    [ 2.0, 1.0, 0.0, 0.0 ], \
    [ 1.0, 2.0, 1.0, 0.0 ], \
    [ 0.0, 1.0, 2.0, 1.0 ], \
    [ 0.0, 0.0, 1.0, 2.0 ] ] )

  l = np.array ( [ \
    [ 1.414213562373095, 0.0,               0.0,               0.0 ], \
    [ 0.707106781186547, 1.224744871391589, 0.0,               0.0 ], \
    [ 0.0,               0.816496580927726, 1.154700538379251, 0.0 ], \
    [ 0.0,               0.0,               0.866025403784439, 1.118033988749895 ] ] )

  print ( '' )
  print ( 'r8mat_is_llt_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_llt tests the error in a lower triangular Cholesky' )
  print ( '  factorization ||A-L*L\'||.' )

  r8mat_print ( m, m, a, '  Matrix A:' )
  r8mat_print ( m, n, l, '  Factor L:' )

  value = r8mat_is_llt ( m, n, a, l )

  print ( '' )
  print ( '  Frobenius norm of A-L*L\' is %g' % (value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_llt_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_lu ( m, n, a, l, u ):

#*****************************************************************************80
#
## r8mat_is_lu() measures the error in an LU factorization.
#
#  Discussion:
#
#    This routine computes the Frobenius norm of
#
#      A - L * U
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#    real L(M,M), U(M,N), the LU factors.
#
#  Output:
#
#    real VALUE, the Frobenius norm of A - L * U.
#
  import numpy as np

  lu = np.dot ( l, u )
  value = np.linalg.norm ( a - lu )

  return value

def r8mat_is_null_left ( m, n, a, x ):

#*****************************************************************************80
#
## r8mat_is_null_left() determines if x is a left null vector of matrix A.
#
#  Discussion:
#
#    The nonzero M vector x is a left null vector of the MxN matrix A if
#
#      x'*A = A'*x = 0
#
#    If A is a square matrix, then this implies that A is singular.
#
#    If A is a square matrix, this implies that 0 is an eigenvalue of A,
#    and that x is an associated eigenvector.
#
#    This routine returns 0 if x is exactly a left null vector of A.
#
#    It returns a "huge" value if x is the zero vector.
#
#    Otherwise, it returns the L2 norm of A' * x divided by the L2 norm of x:
#
#      ERROR_l2 = NORM_l2 ( A' * x ) / NORM_l2 ( x )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the row and column dimensions of 
#    the matrix.  M and N must be positive.
#
#    real A(M,N), the matrix.
#
#    real X(M), the vector.
#
#  Output:
#
#    real VALUE, the result.
#    0.0 indicates that X is exactly a left null vector.
#    A "huge" value indicates that ||x|| = 0;
#    Otherwise, the value returned is a relative error ||A'*x||/||x||.
#
  import numpy as np
#
#  X_norm
#
  x_norm = np.linalg.norm ( x )
#
#  ATX = A'*X
#
  atx = r8mat_mtv ( m, n, a, x )
#
#  ATX_norm
#
  atx_norm = np.linalg.norm ( atx )
#
#  Value
#
  value = atx_norm / x_norm

  return value

def r8mat_is_null_left_test ( ):

#*****************************************************************************80
#
## r8mat_is_null_left_test() tests r8mat_is_null_left().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 3
  n = 3
  a = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ], \
    [ 7.0, 8.0, 9.0 ] ])
  x = np.array ( [ 1.0, -2.0, 1.0 ] )

  print ( '' )
  print ( 'r8mat_is_null_left_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_null_left tests whether the M vector X' )
  print ( '  is a left null vector of A, that is, A\'*x=0.' )

  r8mat_print ( m, n, a, '  Matrix A:' )
  r8vec_print ( m, x, '  Vector X:' )

  enorm = r8mat_is_null_left ( m, n, a, x )

  print ( '' )
  print ( '  Frobenius norm of A\'*x is %g' % ( enorm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_null_left_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_null_right ( m, n, a, x ):

#*****************************************************************************80
#
## r8mat_is_null_right() determines if x is a right null vector of matrix A.
#
#  Discussion:
#
#    The nonzero N vector x is a right null vector of the MxN matrix A if
#
#      A * x = 0
#
#    If A is a square matrix, then this implies that A is singular.
#
#    If A is a square matrix, this implies that 0 is an eigenvalue of A,
#    and that x is an associated eigenvector.
#
#    This routine returns 0 if x is exactly a right null vector of A.
#
#    It returns a "huge" value if x is the zero vector.
#
#    Otherwise, it returns the L2 norm of A * x divided by the L2 norm of x:
#
#      ERROR_l2 = NORM_l2 ( A * x ) / NORM_l2 ( x )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the row and column dimensions of 
#    the matrix.  M and N must be positive.
#
#    real A(M,N), the matrix.
#
#    real X(N), the vector.
#
#  Output:
#
#    real VALUE, the result.
#    0.0 indicates that X is exactly a null vector.
#    A "huge" value indicates that ||x|| = 0;
#    Otherwise, the value returned is a relative error ||A*x||/||x||.
#
  import numpy as np
#
#  X_norm
#
  x_norm = np.linalg.norm ( x )
#
#  AX = A*X
#
  ax = r8mat_mv ( m, n, a, x )
#
#  AX_norm
#
  ax_norm = np.linalg.norm ( ax )
#
#  Value
#
  value = ax_norm / x_norm

  return value

def r8mat_is_null_right_test ( ):

#*****************************************************************************80
#
## r8mat_is_null_right_test() tests r8mat_is_null_right().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 3
  n = 3
  a = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ], \
    [ 7.0, 8.0, 9.0 ] ])
  x = np.array ( [ 1.0, -2.0, 1.0 ] )

  print ( '' )
  print ( 'r8mat_is_null_right_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_null_right tests whether the N vector X' )
  print ( '  is a right null vector of A, that is, A*x=0.' )

  r8mat_print ( m, n, a, '  Matrix A:' )
  r8vec_print ( n, x, '  Vector X:' )

  enorm = r8mat_is_null_right ( m, n, a, x )

  print ( '' )
  print ( '  Frobenius norm of A*x is %g' % ( enorm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_null_right_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_orthogonal_column ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_orthogonal_column() checks whether an R8MAT is column orthogonal.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the row and column dimensions of 
#    the matrix.  M and N must be positive.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    real ERROR_fROBENIUS, the sum of the errors.
#
  import numpy as np

  b = np.dot ( a.transpose ( ), a )

  error_frobenius = r8mat_is_identity ( n, b )

  return error_frobenius

def r8mat_is_orthogonal_column_test ( ):

#*****************************************************************************80
#
## r8mat_is_orthogonal_column_test() tests r8mat_is_orthogonal_column().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_orthogonal_column_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_orthogonal_column reports the Frobenius norm difference' )
  print ( '  between A\'*A and the MxM identity matrix.' )

  nb = 4
  key = 123456789
  b = orthogonal_random_matrix ( nb, key )

  m = 4
  n = 4
  a = b.copy ( )
  r8mat_print ( m, n, a, '  Random 4x4 orthogonal matrix:' )
  e = r8mat_is_orthogonal_column ( m, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )

  m = 4
  n = 3
  a = b[0:m,0:n]
  r8mat_print ( m, n, a, '  3 columns of random 4x4 orthogonal matrix:' )
  e = r8mat_is_orthogonal_column ( m, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )

  m = 3
  n = 4
  a = b[0:m,0:n]
  r8mat_print ( m, n, a, '  3 rows of random 4x4 orthogonal matrix:' )
  e = r8mat_is_orthogonal_column ( m, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_orthogonal_column_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_orthogonal ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_orthogonal() determines if a matrix is orthogonal.
#
#  Discussion:
#
#    The routine returns the Frobenius norm of A'*A - I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    real ERROR_fROBENIUS, the Frobenius orthogonality
#    error, which is zero if the matrix is exactly orthogonal.
#
  import numpy as np

  if ( m != n ):
    error_frobenius = float ( 'Inf' )
    return error_frobenius

  b = np.dot ( a.transpose ( ), a )

  error_frobenius = r8mat_is_identity ( n, b )

  return error_frobenius

def r8mat_is_orthogonal_test ( ):

#*****************************************************************************80
#
## r8mat_is_orthogonal_test() tests r8mat_is_orthogonal().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_orthogonal_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_orthogonal reports the Frobenius norm difference' )
  print ( '  between A\'*A and the identity matrix.' )

  n = 4
  key = 123456789
  a = orthogonal_random_matrix ( n, key )
  r8mat_print ( n, n, a, '  Random orthogonal matrix:' )
  e = r8mat_is_orthogonal ( n, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )

  n = 4
  a = summation_matrix ( n, n )
  r8mat_print ( n, n, a, '  Summation matrix:' )
  e = r8mat_is_orthogonal ( n, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_orthogonal_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_orthogonal_row ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_orthogonal_row() checks whether an R8MAT is row orthogonal.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the row and column dimensions of 
#    the matrix.  M and N must be positive.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    real ERROR_fROBENIUS, the sum of the errors.
#
  import numpy as np

  b = np.dot ( a, a.transpose ( ) )

  error_frobenius = r8mat_is_identity ( m, b )

  return error_frobenius

def r8mat_is_orthogonal_row_test ( ):

#*****************************************************************************80
#
## r8mat_is_orthogonal_row_test() tests r8mat_is_orthogonal_row().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_orthogonal_row_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_orthogonal_row reports the Frobenius norm difference' )
  print ( '  between A*A\' and the NxN identity matrix.' )

  nb = 4
  key = 123456789
  b = orthogonal_random_matrix ( nb, key )

  m = 4
  n = 4
  a = b.copy ( )
  r8mat_print ( m, n, a, '  Random 4x4 orthogonal matrix:' )
  e = r8mat_is_orthogonal_row ( m, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )

  m = 4
  n = 3
  a = b[0:m,0:n]
  r8mat_print ( m, n, a, '  3 columns of random 4x4 orthogonal matrix:' )
  e = r8mat_is_orthogonal_row ( m, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )

  m = 3
  n = 4
  a = b[0:m,0:n]
  r8mat_print ( m, n, a, '  3 rows of random 4x4 orthogonal matrix:' )
  e = r8mat_is_orthogonal_row ( m, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_orthogonal_row_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_permutation ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_permutation() checks whether A is a permutation matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    integer IVAL:
#    -1, the matrix is not square;
#    -2, the matrix is not a zero-one matrix.
#    -3, there is a row that does not sum to 1.
#    -4, there is a column that does not sum to 1.
#    1, the matrix is a permutation matrix,
#
  if ( m != n ):
    ival = -1
    return ival

  jval = r8mat_is_zero_one ( m, n, a )

  if ( jval != 1 ):
    ival = -2
    return ival

  for i in range ( 0, m ):
    s = 0
    for j in range ( 0, n ):
      if ( a[i,j] == 1 ):
        s = s + 1
    if ( s != 1 ):
      ival = -3
      return ival

  for j in range ( 0, n ):
    s = 0
    for i in range ( 0, m ):
      if ( a[i,j] == 1 ):
        s = s + 1
    if ( s != 1 ):
      ival = -4
      return ival

  ival = 1
  return ival

def r8mat_is_permutation_test ( ):

#*****************************************************************************80
#
## r8mat_is_permutation_test() tests r8mat_is_permutation().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_permutation_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_permutation reports whether A is a permutation matrix.' )

  m = 4
  n = 4
  a = np.zeros ( [ m, n ] )
  title = 'Zero matrix'
  r8mat_print ( m, n, a, title )
  ival = r8mat_is_permutation ( m, n, a )
  if ( ival == 1 ):
    print ( '%s is a permutation matrix.' % ( title ) )
  else:
    print ( '%s is NOT a permutation matrix.' % ( title ) )

  m = 4
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, m ):
    a[i,i] = 1.0
  title = 'Identity matrix'
  r8mat_print ( m, n, a, title )
  ival = r8mat_is_permutation ( m, n, a )
  if ( ival == 1 ):
    print ( '%s is a permutation matrix.' % ( title ) )
  else:
    print ( '%s is NOT a permutation matrix.' % ( title ) )

  m = 4
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, m ):
    a[i,i] = 2.0
  title = '2 * Identity matrix'
  r8mat_print ( m, n, a, title )
  ival = r8mat_is_permutation ( m, n, a )
  if ( ival == 1 ):
    print ( '%s is a permutation matrix.' % ( title ) )
  else:
    print ( '%s is NOT a permutation matrix.' % ( title ) )

  m = 4
  n = 4
  a = np.array ( [\
    [0,0,1,0],\
    [0,0,0,1],\
    [1,0,0,0],\
    [0,1,0,0] ])
  title = 'M1'
  r8mat_print ( m, n, a, title )
  ival = r8mat_is_permutation ( m, n, a )
  if ( ival == 1 ):
    print ( '%s is a permutation matrix.' % ( title ) )
  else:
    print ( '%s is NOT a permutation matrix.' % ( title ) )

  m = 4
  n = 4
  a = np.array ( [\
    [0,0,1,0],\
    [0,1,0,1],\
    [1,0,0,0],\
    [0,0,0,0] ])
  title = 'M2'
  r8mat_print ( m, n, a, title )
  ival = r8mat_is_permutation ( m, n, a )
  if ( ival == 1 ):
    print ( '%s is a permutation matrix.' % ( title ) )
  else:
    print ( '%s is NOT a permutation matrix.' % ( title ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_permutation_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_persymmetric ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_persymmetric() checks an R8MAT for persymmetry.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    A is persymmetric if A(I,J) = A(N+1-J,N+1-I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    real ERROR_fROBENIUS, the Frobenius error
#    in persymmetry, which will be 0 if the matrix is exactly
#    persymmetric.
#
  import numpy as np

  if ( not r8mat_is_square ( m, n, a ) ):
    error_frobenius = float ( 'Inf' )
    return error_frobenius

  error_frobenius = 0.0
  for i in range ( 0, m ):
    for j in range ( n - 1, -1, -1 ):
      error_frobenius = error_frobenius + ( a[i,j] - a[n-1-j,m-1-i] ) ** 2

  error_frobenius = np.sqrt ( error_frobenius )

  return error_frobenius

def r8mat_is_persymmetric_test ( ):

#*****************************************************************************80
#
## r8mat_is_persymmetric_test() tests r8mat_is_persymmetric().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_persymmetric_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_persymmetric reports whether a matrix' )
  print ( '  is persymmetric.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_persymmetric ( m, n, a )
  print ( '' )
  print ( '  Persymmetric = %g' % ( value ) )
#
#  Square, but not persymmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 4, 3, 2, 1 ], \
    [ 7, 6, 5, 3 ], \
    [ 9, 8, 6, 3 ], \
    [10, 7, 7, 4 ] ] )
  r8mat_print ( m, n, a, '  Not persymmetric matrix:' )
  value = r8mat_is_persymmetric ( m, n, a )
  print ( '' )
  print ( '  Persymmetric = %g' % ( value ) )
#
#  Persymmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 4, 3, 2, 1 ], \
    [ 7, 6, 5, 2 ], \
    [ 9, 8, 6, 3 ], \
    [10, 9, 7, 4 ] ] )
  r8mat_print ( m, n, a, '  Persymmetric matrix:' )
  value = r8mat_is_persymmetric ( m, n, a )
  print ( '' )
  print ( '  Persymmetric = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_persymmetric_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_plu ( m, n, a, p, l, u ):

#*****************************************************************************80
#
## r8mat_is_plu() measures the error in a PLU factorization.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    This routine computes the Frobenius norm of
#
#      A - P * L * U
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#    real P(M,M), L(M,M), U(M,N), the PLU factors.
#
#  Output:
#
#    real VALUE, the Frobenius norm
#    of the difference matrix A - P * L * U.
#
  lu = r8mat_mm ( m, m, n, l, u )
  plu = r8mat_mm ( m, m, n, p, lu )

  d = r8mat_sub ( m, n, a, plu )
 
  value = r8mat_norm_fro ( m, n, d )

  return value

def r8mat_is_plu_test ( ):

#*****************************************************************************80
#
## r8mat_is_plu_test() tests r8mat_is_plu().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
#
#  This is the CARRY ( 4.0, 4 ) matrix.
#
  m = 4
  n = m

  a = np.array ( [ \
    [ 5.0,  7.0,  6.0,  5.0 ], \
    [ 7.0, 10.0,  8.0,  7.0 ], \
    [ 6.0,  8.0, 10.0,  9.0 ], \
    [ 5.0,  7.0,  9.0, 10.0 ] ] )

  p = np.array ( [ \
    [ 0.0,  0.0,  0.0,  1.0 ], \
    [ 1.0,  0.0,  0.0,  0.0 ], \
    [ 0.0,  1.0,  0.0,  0.0 ], \
    [ 0.0,  0.0,  1.0,  0.0 ] ] )

  l = np.array ( [ \
   [ 1.0,                0.00,  0.00,  0.00 ], \
   [ 0.857142857142857,  1.00,  0.00,  0.00 ], \
   [ 0.714285714285714,  0.25,  1.00,  0.00 ], \
   [ 0.714285714285714,  0.25, -0.20,  1.00 ] ] )

  u = np.array ( [ \
    [ 7.00, 10.0,               8.0,               7.00 ], \
    [ 0.00, -0.571428571428571, 3.142857142857143, 3.00 ], \
    [ 0.00,  0.0,               2.50,              4.25 ], \
    [ 0.00,  0.0,               0.0,               0.10 ] ] )

  print ( '' )
  print ( 'r8mat_is_plu_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_plu tests the error in the P*L*U factorization:' )
  print ( '    A - P * L * U = 0' )

  r8mat_print ( m, n, a, '  Matrix A:' )
  r8mat_print ( m, m, p, '  Permutation P:' )
  r8mat_print ( m, m, l, '  Lower triangular L:' )
  r8mat_print ( m, n, u, '  Upper triangular U:' )

  value = r8mat_is_plu ( m, n, a, p, l, u  )

  print ( '' )
  print ( '  Frobenius norm of A-P*L*U is %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_plu_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_solution ( m, n, k, a, x, b ):

#*****************************************************************************80
#
## r8mat_is_solution() measures the error in a linear system solution.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    The system matrix A is an M x N matrix.
#    It is not required that A be invertible.
#
#    The solution vector X is actually allowed to be an N x K matrix.
#
#    The right hand side "vector" B is actually allowed to be an M x K matrix.
#
#    This routine simply returns the Frobenius norm of the M x K matrix:
#    A * X - B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, K, the order of the matrices.
#
#    real A(M,N), X(N,K), B(M,K), the matrices.
#
#  Output:
#
#    real VALUE, the Frobenius norm
#    of the difference matrix A * X - B, which would be exactly zero
#    if X was the "solution" of the linear system.
#

#
#  AX = A*X
#
  ax = r8mat_mm ( m, n, k, a, x )
#
#  AXMB = AX-B.
#
  axmb = r8mat_sub ( m, k, ax, b )
#
#  Value = ||AX-B|\
#
  value = r8mat_norm_fro ( m, k, axmb )

  return value

def r8mat_is_solution_test ( ):

#*****************************************************************************80
#
## r8mat_is_solution_test() tests r8mat_is_solution().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_solution_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_solution tests whether X is the solution of' )
  print ( '  A*X=B by computing the Frobenius norm of the residual.' )
#
#  Get random shapes.
#
  m = np.random.randint ( 1, 11 )
  n = np.random.randint ( 1, 11 )
  k = np.random.randint ( 1, 11 )
#
#  Get a random A.
#
  r8_lo = -5.0
  r8_hi = +5.0
  a = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( m, n )
#
#  Get a random X.
#
  r8_lo = -5.0
  r8_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n, k )
#
#  Compute B = A * X.
#
  b = r8mat_mm ( m, n, k, a, x )
#
#  Compute || A*X-B||
#
  enorm = r8mat_is_solution ( m, n, k, a, x, b )
  
  print ( '' )
  print ( '  A is %d by %d' % ( m, n ) )
  print ( '  X is %d by %d' % ( n, k ) )
  print ( '  B is %d by %d' % ( m, k ) )
  print ( '  Frobenius error in A*X-B is %g' % ( enorm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_solution_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_sparse ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_sparse() checks whether a matrix is sparse.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    real FNORM, the number of nonzero entries divided by M * N.
#
  ival = 0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( a[i,j] != 0.0 ):
        ival = ival + 1

  fnorm = float ( ival ) / float ( m ) / float ( n )

  return fnorm

def r8mat_is_sparse_test ( ):

#*****************************************************************************80
#
## r8mat_is_sparse_test() tests r8mat_is_sparse().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_sparse_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_sparse reports whether a matrix' )
  print ( '  is sparse.' )
#
#  Maximal sparse
#
  m = 3
  n = 4
  a = np.zeros ( [ m, n ] )

  r8mat_print ( m, n, a, '  Zero matrix:' )
  value = r8mat_is_sparse ( m, n, a )
  print ( '' )
  print ( '  Sparseness = %g' % ( value ) )
#
#  Rather sparse
#
  m = 3
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0
  r8mat_print ( m, n, a, '  Identity-like matrix:' )
  value = r8mat_is_sparse ( m, n, a )
  print ( '' )
  print ( '  Sparseness = %g' % ( value ) )
#
#  Hardly sparse
#
  m = 4
  n = 4
  a = np.array ( [ \
    [  0,  1,  2,  3 ], \
    [  4,  5,  6,  7 ], \
    [  8,  9, 10, 11 ], \
    [ 12, 13, 14, 15 ] ] )
  r8mat_print ( m, n, a, '  Hardly sparse:' )
  value = r8mat_is_sparse ( m, n, a )
  print ( '' )
  print ( '  Sparseness = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_sparse_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_square ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_square() checks whether A is square.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    bool r8mat_is_square, is True if the matrix is square.
#
  if ( m == n ):
    value = True
  else:
    value = False

  return value

def r8mat_is_square_test ( ):

#*****************************************************************************80
#
## r8mat_is_square_test() tests r8mat_is_square().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_square_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_square reports whether a matrix' )
  print ( '  is square.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_square ( m, n, a )
  print ( '' )
  print ( '  Square = %s' % ( value ) )
#
#  Square.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 1, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 1, 0, 1, 0 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Square matrix:' )
  value = r8mat_is_square ( m, n, a )
  print ( '' )
  print ( '  Square = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_square_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_symmetric ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_symmetric() checks whether A is a symmetric matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    bool r8mat_is_symmetric, is True if the matrix is symmetric.
#
  import numpy as np

  if ( not r8mat_is_square ( m, n, a ) ):
    return False

  t = 0.0
  for i in range ( 0, m ):
    for j in range ( i + 1, n ):
      t = t + ( a[i,j] - a[j,i] ) ** 2

  print ( 'T = %g' % ( t ) )
  tol = 0.00001

  if ( t < tol ):
    value = True
  else:
    value = False

  return value

def r8mat_is_symmetric_test ( ):

#*****************************************************************************80
#
## r8mat_is_symmetric_test() tests r8mat_is_symmetric().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_symmetric_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_symmetric reports whether a matrix' )
  print ( '  is symmetric.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_symmetric ( m, n, a )
  print ( '' )
  print ( '  Symmetric = %s' % ( value ) )
#
#  Square, but not symmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 1, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 1, 0, 1, 0 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Not symmetric matrix:' )
  value = r8mat_is_symmetric ( m, n, a )
  print ( '' )
  print ( '  Symmetric = %s' % ( value ) )
#
#  Symmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 2, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 2, 0, 1, 1 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Symmetric matrix:' )
  value = r8mat_is_symmetric ( m, n, a )
  print ( '' )
  print ( '  Symmetric = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_symmetric_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_zero_one ( m, n, a ):

#*****************************************************************************80
#
## r8mat_is_zero_one() checks for a zero-one matrix.
#
#  Discussion:
#
#    The routine returns the Frobenius norm of A - I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    bool r8mat_is_zero_one, is True if the matrix is a
#    zero-one matrix, and False otherwise.
#
  value = True

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( a[i,j] != 0.0 and a[i,j] != 1.0 ):
        value = False
        return value

  return value

def r8mat_is_zero_one_test ( ):

#*****************************************************************************80
#
## r8mat_is_zero_one_test() tests r8mat_is_zero_one().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_is_zero_one_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_is_zero_one reports whether a matrix' )
  print ( '  only has entries of 0 and 1.' )

  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  r8mat_print ( m, n, a, '  Zero matrix:' )
  value = r8mat_is_zero_one ( m, n, a )
  print ( '' )
  print ( '  Zero/one = %s' % ( value ) )

  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0
  r8mat_print ( m, n, a, '  Identity matrix:' )
  value = r8mat_is_zero_one ( m, n, a )
  print ( '' )
  print ( '  Zero/one = %s' % ( value ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = a[i,j] + float ( i * j ) / 1000
  r8mat_print ( m, n, a, '  Almost identity matrix:' )
  value = r8mat_is_zero_one ( m, n, a )
  print ( '' )
  print ( '  Zero/one = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_is_zero_one_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_l1_inverse ( A ):

#*****************************************************************************80
#
## r8mat_l1_inverse() inverts a unit lower triangular R8MAT.
#
#  Discussion:
#
#    A unit lower triangular matrix is a matrix with only 1's on the main
#    diagonal, and only 0's above the main diagonal.
#
#    The inverse of a unit lower triangular matrix is also
#    a unit lower triangular matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    real A(N,N), the unit lower triangular matrix.
#
#  Output:
#
#    real B(N,N), the inverse matrix.
#
  import numpy as np

  n = np.size ( A, 0 )
  
  B = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i < j ):
        B[i,j] = 0.0
      elif ( j == i ):
        B[i,j] = 1.0
      else:
        B[i,j] = - np.sum ( A[i,0:i] * B[0:i,j] )

  return B

def r8mat_l1_inverse_test ( ):

#*****************************************************************************80
#
## r8mat_l1_inverse_test() tests r8mat_l1_inverse().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6
#
#  Each row of this definition is a COLUMN of the matrix.
#
  A = np.array ( [ \
    [  1.0, 0.0, 0.0, 0.0, 0.0, 0.0 ], \
    [  2.0, 1.0, 0.0, 0.0, 0.0, 0.0 ], \
    [  0.0, 0.0, 1.0, 0.0, 0.0, 0.0 ], \
    [  5.0, 0.0, 3.0, 1.0, 0.0, 0.0 ], \
    [  0.0, 0.0, 0.0, 0.0, 1.0, 0.0 ], \
    [ 75.0, 0.0, 0.0, 6.0, 4.0, 1.0 ] ] )

  print ( '' )
  print ( 'r8mat_l1_inverse_test' )
  print ( '  r8mat_l1_inverse inverts a unit lower triangular matrix.' )

  r8mat_print ( n, n, A, '  Matrix A to be inverted:' )
 
  B = r8mat_l1_inverse ( A )
 
  r8mat_print ( n, n, B, '  Inverse matrix B:' )
 
  C = np.matmul ( A, B )

  r8mat_print ( n, n, C, '  Product C = A * B:' )

  return

def r8mat_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## r8mat_mm() multiplies two R8MAT's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    real A(N1,N2), B(N2,N3), the matrices to multiply.
#
#  Output:
#
#    real C(N1,N3), the product matrix C = A * B.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ) )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def r8mat_mm_test ( ):

#*****************************************************************************80
#
## r8mat_mm_test() tests r8mat_mm().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'r8mat_mm_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_mm computes a matrix-matrix product C = A * B;' )

  a = np.zeros ( ( n1, n2 ) )

  for i in range ( 0, n1 ): 
    for j in range ( 0, n2 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = np.transpose ( a )

  c = r8mat_mm ( n1, n2, n3, a, b )

  r8mat_print ( n1, n2, a, '  A:' )
  r8mat_print ( n2, n3, b, '  B:' )
  r8mat_print ( n1, n3, c, '  C = A*B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_mm_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_mmt ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## r8mat_mmt() multiplies an R8MAT times a transposed R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    real A(N1,N2), B(N3,N2), the matrices to multiply.
#
#  Output:
#
#    real C(N1,N3), the product matrix C = A * B'.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ) )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[j,k]

  return c

def r8mat_mmt_test ( ):

#*****************************************************************************80
#
## r8mat_mmt_test() tests r8mat_mmt().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'r8mat_mmt_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_mmt computes a matrix-matrix product C = A * B\';' )

  a = np.zeros ( ( n1, n2 ) )

  for i in range ( 0, n1 ): 
    for j in range ( 0, n2 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = np.copy ( a )

  c = r8mat_mmt ( n1, n2, n3, a, b )

  r8mat_print ( n1, n2, a, '  A:' )
  r8mat_print ( n3, n2, b, '  B:' )
  r8mat_print ( n1, n3, c, '  C = A*B\':' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_mmt_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_mtm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## r8mat_mtm() computes A' * B for two R8MAT's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, the order of the matrices.
#
#    real A(N2,N1), B(N2,N3), the matrices to multiply.
#
#  Output:
#
#    real C(N1,N3), the product matrix C = A' * B.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ) )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[k,i] * b[k,j]

  return c

def r8mat_mtm_test ( ):

#*****************************************************************************80
#
## r8mat_mtm_test() tests r8mat_mtm().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'r8mat_mtm_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_mtm computes a matrix-matrix product C = A\' * B;' )

  a = np.zeros ( ( n2, n1 ) )

  for i in range ( 0, n2 ): 
    for j in range ( 0, n1 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = a

  c = r8mat_mtm ( n1, n2, n3, a, b )

  r8mat_print ( n2, n1, a, '  A:' )
  r8mat_print ( n2, n3, b, '  B:' )
  r8mat_print ( n1, n3, c, '  C = A\'*B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_mtm_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r8mat_mtv() multiplies a tranposed matrix times a vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), the M by N matrix.
#
#    real X(M), the vector to be multiplied by A'.
#
#  Output:
#
#    real Y(N), the product A'*X.
#
  import numpy as np

  y = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      y[j] = y[j] + x[i] * a[i,j]

  return y

def r8mat_mtv_test ( ):

#*****************************************************************************80
#
## r8mat_mtv_test() tests r8mat_mtv().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 4
  n = 2

  a = np.array \
  ( \
    ( ( 1.0, 1.0 ), \
    ( 2.0, 1.0 ), \
    ( 3.0, 1.0 ), \
    ( 4.0, 1.0 ) ) \
  )
 
  x = np.array ( ( 1.0, 2.0, 3.0, 4.0 ) )

  print ( '' )
  print ( 'r8mat_mtv_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_mtv computes a matrix-vector product b = A\' * x;' )

  b = r8mat_mtv ( m, n, a, x )

  r8mat_print ( m, n, a, '  A:' )
  r8vec_print ( m, x, '  X:' )
  r8vec_print ( n, b, '  B = A\'*X:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_mtv_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r8mat_mv() multiplies a matrix times a vector.
#
#  Discussion:
#
#    In FORTRAN90, this operation can be more efficiently carried
#    out by the command
#
#      Y(1:M) = MATMUL ( A(1:M,1:N), X(1:N) )
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
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), the M by N matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real Y(M), the product A*X.
#
  import numpy as np

  y = np.zeros ( m )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      y[i] = y[i] + a[i,j] * x[j]

  return y

def r8mat_mv_test ( ):

#*****************************************************************************80
#
## r8mat_mv_test() tests r8mat_mv().
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
  import numpy as np
  import platform

  m = 4
  n = 2

  a = np.array \
  ( \
    ( ( 1.0, 1.0 ), \
    ( 2.0, 1.0 ), \
    ( 3.0, 1.0 ), \
    ( 4.0, 1.0 ) ) \
  )
 
  x = np.array ( ( 1.0, 2.0 ) )

  print ( '' )
  print ( 'r8mat_mv_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_mv computes a matrix-vector product b = A * x;' )

  b = r8mat_mv ( m, n, a, x )

  r8mat_print ( m, n, a, '  A:' )
  r8vec_print ( n, x, '  X:' )
  r8vec_print ( m, b, '  B = A*X:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_mv_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_norm_fro ( m, n, a ):

#*****************************************************************************80
#
## r8mat_norm_fro() returns the Frobenius norm of an R8MAT.
#
#  Discussion:
#
#    The Frobenius norm is defined as
#
#      value = sqrt ( sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J)^2 )
#
#    The matrix Frobenius norm is not derived from a vector norm, but
#    is compatible with the vector L2 norm, so that:
#
#      vec_norm_l2 ( A * x ) <= mat_norm_fro ( A ) * vec_norm_l2 ( x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
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
#    real A(M,N), the matrix whose Frobenius
#    norm is desired.
#
#  Output:
#
#    real VALUE, the Frobenius norm of A.
#
  import numpy as np
 
  value = np.sqrt ( sum ( sum ( a ** 2 ) ) )

  return value

def r8mat_norm_fro_test ( ):

#*****************************************************************************80
#
## r8mat_norm_fro_test() tests r8mat_norm_fro().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4

  a = np.zeros ( ( m, n ) )

  k = 0
  t1 = 0.0

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k
      t1 = t1 + k * k

  t1 = np.sqrt ( t1 )

  print ( '' )
  print ( 'r8mat_norm_fro_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_norm_fro computes the Frobenius norm of an R8MAT;' )

  t2 = r8mat_norm_fro ( m, n, a )

  r8mat_print ( m, n, a, '  A:' )
  print ( '' )
  print ( '  Expected Frobenius norm = %g' % ( t1 ) )
  print ( '  Computed Frobenius norm = %g' % ( t2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_norm_fro_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_norm_l1 ( m, n, a ):

#*****************************************************************************80
#
## r8mat_norm_l1() returns the matrix L1 norm of an R8MAT.
#
#  Discussion:
#
#    The matrix L1 norm is defined as:
#
#      value = max ( 1 <= J <= N ) sum ( 1 <= I <= M ) abs ( A(I,J) ).
#
#    The matrix L1 norm is derived from the vector L1 norm, and
#    satisifies:
#
#      vec_norm_l1 ( A * x ) <= mat_norm_l1 ( A ) * vec_norm_l1 ( x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
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
#    real A(M,N), the matrix whose norm is desired.
#
#  Output:
#
#    real VALUE, the norm of A.
#
  value = 0.0

  for j in range ( 0, n ):
    row_sum = 0.0
    for i in range ( 0, m ):
      row_sum = row_sum + abs ( a[i,j] )
    value = max ( value, row_sum )

  return value

def r8mat_norm_l1_test ( ):

#*****************************************************************************80
#
## r8mat_norm_l1_test() tests r8mat_norm_l1().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4
  x1 = -5.0
  x2 = +5.0

  a = x1 + ( x2 - x1 ) * np.random.rand ( m, n )
  
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = round ( a[i,j] )

  print ( '' )
  print ( 'r8mat_norm_l1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_norm_l1 computes the L1 norm of an R8MAT;' )

  t = r8mat_norm_l1 ( m, n, a )

  r8mat_print ( m, n, a, '  A:' )
  print ( '' )
  print ( '  Computed L1 norm = %g' % ( t ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_norm_l1_test' )
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
#    08 May 2020
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
#    08 May 2020
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

def r8mat_sub ( m, n, a, b ):

#*****************************************************************************80
#
## r8mat_sub() computes the difference of two matrices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrices.
#
#    real A(M,N), B(M,N), the matrices.
#
#  Output:
#
#    real C(M,N), the difference C = A - B.
#
  import numpy as np

  c = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m):
      c[i,j] = a[i,j] - b[i,j]

  return c

def r8mat_sub_test ( ):

#*****************************************************************************80
#
## r8mat_sub_test() tests r8mat_sub().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 4
  n = 4

  print ( '' )
  print ( 'r8mat_sub_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_sub computes C = A - B;' )

  a = r8mat_indicator ( m, n )

  b = np.transpose ( a )

  c = r8mat_sub ( m, n, a, b )

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )
  r8mat_print ( m, n, c, '  C = A - B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_sub_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_u1_inverse ( A ):

#*****************************************************************************80
#
## r8mat_u1_inverse() inverts a unit upper triangular R8MAT.
#
#  Discussion:
#
#    A unit upper triangular matrix is a matrix with only 1's on the main
#    diagonal, and only 0's below the main diagonal.
#
#    The inverse of a unit upper triangular matrix is also
#    a unit upper triangular matrix.
#
#    This routine can invert a matrix in place, that is, with no extra
#    storage.  If the matrix is stored in A, then the call
#
#      call r8mat_u1_inverse ( n, a, a )
#
#    will result in A being overwritten by its inverse.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    real A(N,N), the unit upper triangular matrix.
#
#  Output:
#
#    real B(N,N), the inverse matrix.
#
  import numpy as np

  n = np.size ( A, 0 )

  B = np.zeros ( [ n, n ] )

  for j in range ( n - 1, -1, -1 ):

    for i in range ( n - 1, -1, -1 ):

      if ( j < i ):
        B[i,j] = 0.0
      elif ( i == j ):
        B[i,j] = 1.0
      else:
        B[i,j] = - np.sum ( A[i,i+1:j+1] * B[i+1:j+1,j] )


  return B

def r8mat_u1_inverse_test ( ):

#*****************************************************************************80
#
## r8mat_u1_inverse_test() tests r8mat_u1_inverse().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 6
#
#  Each row of this definition is a COLUMN of the matrix.
#
  A = np.array ( [ \
    [ 1.0, 2.0, 0.0, 5.0, 0.0, 75.0 ], \
    [ 0.0, 1.0, 0.0, 0.0, 0.0,  0.0 ], \
    [ 0.0, 0.0, 1.0, 3.0, 0.0,  0.0 ], \
    [ 0.0, 0.0, 0.0, 1.0, 0.0,  6.0 ], \
    [ 0.0, 0.0, 0.0, 0.0, 1.0,  4.0 ], \
    [ 0.0, 0.0, 0.0, 0.0, 0.0,  1.0 ] ] )

  print ( '' )
  print ( 'r8mat_u1_inverse_test' )
  print ( '  r8mat_u1_inverse inverts a unit upper triangular matrix.' )

  r8mat_print ( n, n, A, '  Input matrix A' )
 
  B = r8mat_u1_inverse ( A )
 
  r8mat_print ( n, n, B, '  Inverse matrix B:' )

  C = np.matmul ( A, B )

  r8mat_print ( n, n, C, '  Product C = A * B:' )

  return

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop() returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real r8_mop, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## r8_mop_test() tests r8_mop().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8_mop_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_mop evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_mop(I4)' )
  print ( '' )

  for test in range ( 0, 10 ):
    i4 = np.random.randint ( -100, +101 )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_mop_test' )
  print ( '  Normal end of execution.' )
  return

def r8poly_degree ( m, a ):

#*****************************************************************************80
#
## r8poly_degree() returns the degree of a polynomial.
#
#  Discussion:
#
#    The degree of a polynomial is the index of the highest power
#    of X with a nonzero coefficient.
#
#    The degree of a constant polynomial is 0.  The degree of the
#    zero polynomial is debatable, but this routine returns the
#    degree as 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the nominal degree of A.
#
#    real A(M+1), the coefficients of the polynomials.
#
#  Output:
#
#    integer VALUE, the degree of A.
#
  value = m

  while ( 0 < value ):
    if ( a[value] != 0.0 ):
      break
    value = value - 1

  return value

def r8poly_degree_test ( ):

#*****************************************************************************80
#
## r8poly_degree_test() tests r8poly_degree().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  c1 = np.array ( [ 1.0, 2.0, 3.0, 4.0 ] )
  c2 = np.array ( [ 1.0, 2.0, 3.0, 0.0 ] )
  c3 = np.array ( [ 1.0, 2.0, 0.0, 4.0 ] )
  c4 = np.array ( [ 1.0, 0.0, 0.0, 0.0 ] )
  c5 = np.array ( [ 0.0, 0.0, 0.0, 0.0 ] )

  print ( '' )
  print ( 'r8poly_degree_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8poly_degree determines the degree of an R8POLY.' )

  m = 3

  r8poly_print ( m, c1, '  The R8POLY:' )
  d = r8poly_degree ( m, c1 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( m, c2, '  The R8POLY:' )
  d = r8poly_degree ( m, c2 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( m, c3, '  The R8POLY:' )
  d = r8poly_degree ( m, c3 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( m, c4, '  The R8POLY:' )
  d = r8poly_degree ( m, c4 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( m, c5, '  The R8POLY:' )
  d = r8poly_degree ( m, c5 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  print ( '' )
  print ( 'r8poly_degree_test:' )
  print ( '  Normal end of execution.' )
  return

def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## r8poly_print() prints out a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the nominal degree of the polynomial.
#
#    real A[0:M], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( a[m] < 0.0 ):
    plus_minus = '-'
  else:
    plus_minus = ' '

  mag = abs ( a[m] )

  if ( 2 <= m ):
    print ( '  p(x) = %c %g * x^%d' % ( plus_minus, mag, m ) )
  elif ( m == 1 ):
    print ( '  p(x) = %c %g * x' % ( plus_minus, mag ) )
  elif ( m == 0 ):
    print ( '  p(x) = %c %g' % ( plus_minus, mag ) )

  for i in range ( m - 1, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( 2 <= i ):
        print ( '         %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '         %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '         %c %g' % ( plus_minus, mag ) )

def r8poly_print_test ( ):

#*****************************************************************************80
#
## r8poly_print_test() tests r8poly_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8poly_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8poly_print prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )

  r8poly_print ( m, c, '  The R8POLY:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8poly_print_test:' )
  print ( '  Normal end of execution.' )

  return

def r8_rise ( x, n ):

#*****************************************************************************80
#
## r8_rise() computes the rising factorial function [X]^N.
#
#  Discussion:
#
#    [X]^N = X * ( X + 1 ) * ( X + 2 ) * ... * ( X + N - 1 ).
#
#    Note that the number of ways of arranging N objects in M ordered
#    boxes is [M]^N.  (Here, the ordering of the objects in each box matters).
#    Thus, 2 objects in 2 boxes have the following 6 possible arrangements:
#
#      -|12, 1|2, 12|-, -|21, 2|1, 21|-.
#
#    Moreover, the number of non-decreasing maps from a set of
#    N to a set of M ordered elements is [M]^N / N!.  Thus the set of
#    nondecreasing maps from (1,2,3) to (a,b,c,d) is the 20 elements:
#
#      aaa, abb, acc, add, aab, abc, acd, aac, abd, aad
#      bbb, bcc, bdd, bbc, bcd, bbd, ccc, cdd, ccd, ddd.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the rising factorial function.
#
#    integer N, the order of the rising factorial function.
#    If N = 0, RISE = 1, if N = 1, RISE = X.  Note that if N is
#    negative, a "falling" factorial will be computed.
#
#  Output:
#
#    real VALUE, the value of the rising factorial function.
#
  value = 1.0

  arg = x

  if ( 0 < n ):

    for i in range ( 0, n ):
      value = value * arg
      arg = arg + 1.0

  elif ( n < 0 ):

    for i in range ( n, 0 ):
      value = value * arg
      arg = arg - 1.0

  return value

def r8_rise_test ( ):

#*****************************************************************************80
#
## r8_rise_test() tests r8_rise().
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
  import platform

  print ( '' )
  print ( 'r8_rise_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_rise evaluates the rising factorial Rise(X,N).' )
  print ( '' )
  print ( '      X        N                     Exact                  Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, n, f1 = r8_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_rise ( x, n )

    print ( '  %8.4g  %4d  %24.16g  %24.16g' % ( x, n, f1, f2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_rise_test' )
  print ( '  Normal end of execution.' )
  return

def r8_rise_values ( n_data ):

#*****************************************************************************80
#
## r8_rise_values() returns values of the rising factorial function.
#
#  Discussion:
#
#    The rising factorial function is sometimes symbolized by (m)_n.
#
#    The definition is
#
#      (m)_n = (m-1+n)! / (m-1)!
#            = ( m ) * ( m + 1 ) * ( m + 2 ) \ * ( m - 1 + n )
#            = Gamma ( m + n ) / Gamma ( m )
#
#    We assume 0 <= N <= M.
#
#    In Mathematica, the function can be evaluated by:
#
#      Pochhammer[m,n]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, integer N, the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 15

  f_vec = np.array ( [ 
       1680.000000000000, \
       1962.597656250000, \
       2279.062500000000, \
       2631.972656250000, \
       3024.000000000000, \
       1.000000000000000, \
       7.500000000000000, \
       63.75000000000000, \
       605.6250000000000, \
       6359.062500000000, \
       73129.21875000000, \
       914115.2343750000, \
       1.234055566406250E+07, \
       1.789380571289063E+08, \
       2.773539885498047E+09 ] )

  n_vec = np.array ( [ 
       4, \
       4, \
       4, \
       4, \
       4, \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9 ] )

  x_vec = np.array ( [ 
       5.00, \
       5.25, \
       5.50, \
       5.75, \
       6.00, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    n = 0
    f = 0.0
  else:
    x = x_vec[n_data]
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, n, f

def r8_rise_values_test ( ):

#*****************************************************************************80
#
## r8_rise_values_test() tests r8_rise_values().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_rise_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_rise_values returns values of the rising factorial.' )
  print ( '' )
  print ( '          X         N          r8_rise(X,N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, n, f = r8_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8.4f  %8d  %24.16g' % ( x, n, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_rise_values_test:' )
  print ( '  Normal end of execution.' )
  return

def r8_sign ( x ):

#*****************************************************************************80
#
## r8_sign() returns the sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose sign is desired.
#
#  Output:
#
#    real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  else:
    value = +1.0
 
  return value

def r8_sign_test ( ):

#*****************************************************************************80
#
## r8_sign_test() tests r8_sign().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 5

  r8_test = np.array ( [ -1.25, -0.25, 0.0, +0.5, +9.0 ] )

  print ( '' )
  print ( 'r8_sign_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sign returns the sign of an R8.' )
  print ( '' )
  print ( '     R8     r8_sign(R8)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_test[test]
    s = r8_sign ( r8 )
    print ( '  %8.4f  %8.0f' % ( r8, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_sign_test' )
  print ( '  Normal end of execution.' )
  return

def r8vec_asum ( n, a ):

#*****************************************************************************80
#
## r8vec_asum() sums the absolute values of the entries of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the sum of the absolute values of the entries.
#
  value = 0.0
  for i in range ( 0, n ):
    value = value + abs ( a[i] )

  return value

def r8vec_asum_test ( ):

#*****************************************************************************80
#
## r8vec_asum_test() tests r8vec_asum().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8vec_asum_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_asum sums the absolute values of the entries in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0

  a = a_lo + ( a_hi - a_lo ) * np.random.rand ( n )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_asum ( n, a )

  print ( '' )
  print ( '  Sum of absolute values of entries = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_asum_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_house_column ( n, a_vec, k ):

#*****************************************************************************80
#
## r8vec_house_column() defines a Householder premultiplier that "packs" a column.
#
#  Discussion:
#
#    The routine returns a vector V that defines a Householder
#    premultiplier matrix H(V) that zeros out the subdiagonal entries of
#    column K of the matrix A.
#
#       H(V) = I - 2 * v * v'
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix A.
#
#    real A_VEC(N), a row or column of the matrix A.
#
#    integer K, the "special" entry in A_VEC.
#    The Householder matrix will zero out the entries after this.
#
#  Output:
#
#    real V(N), a vector of unit L2 norm which defines an
#    orthogonal Householder premultiplier matrix H with the property
#    that the K-th column of H*A is zero below the diagonal.
#
  import numpy as np

  v = np.zeros ( n )

  if ( k < 0 or n - 1 <= k ):
    return v

  s = 0.0
  for i in range ( k, n ):
    s = s + a_vec[i] ** 2
  s = np.sqrt ( s )

  if ( s == 0.0 ):
    return v

  if ( a_vec[k] < 0.0 ):
    v[k] = a_vec[k] - abs ( s )
  else:
    v[k] = a_vec[k] + abs ( s )

  for i in range ( k + 1, n ):
    v[i] = a_vec[i]

  s = 0.0
  for i in range ( k, n ):
    s = s + v[i] ** 2
  s = np.sqrt ( s )

  for i in range ( k, n ):
    v[i] = v[i] / s

  return v

def r8vec_house_column_test ( ):

#*****************************************************************************80
#
## r8vec_house_column_test() tests r8vec_house_column().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_house_column_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_house_column returns the compact form of' )
  print ( '  a Householder matrix that "packs" a column' )
  print ( '  of a matrix.' )
#
#  Get a random matrix.
#
  n = 4
  r8_lo = 0.0
  r8_hi = 5.0

  a = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n, n )

  r8mat_print ( n, n, a, '  Matrix A:' )

  a_col = np.zeros ( n )

  for k in range ( 0, n - 1 ):

    print ( '' )
    print ( '  Working on column K = %d' % ( k ) )

    for i in range ( 0, n ):
      a_col[i] = a[i,k]

    v = r8vec_house_column ( n, a_col, k )

    h = r8mat_house_form ( n, v )

    r8mat_print ( n, n, h, '  Householder matrix H:' )

    ha = r8mat_mm ( n, n, n, h, a )

    r8mat_print ( n, n, ha, '  Product H*A:' )
#
#  If we set A := HA, then we can successively convert A to upper
#  triangular form.
#
    a = ha
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_house_column_test' )
  print ( '  Normal end of execution.' )
  return

def r8vec_nint ( n, a ):

#*****************************************************************************80
#
## r8vec_nint() rounds entries of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector to be rounded.
#
#  Output:
#
#    real A(N), the rounded vector.
#
  for i in range ( 0, n ):
    a[i] = round ( a[i] )

  return a

def r8vec_nint_test ( ):

#*****************************************************************************80
#
## r8vec_nint_test() tests r8vec_nint().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_nint_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_nint rounds an R8VEC.' )

  n = 5
  x1 = -5.0
  x2 = +5.0
  a = x1 + ( x2 - x1 ) * np.random.rand ( n )
  r8vec_print ( n, a, '  Vector A:' )
  a = r8vec_nint ( n, a )
  r8vec_print ( n, a, '  Rounded vector A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_nint_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
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

  return

def redheffer_matrix ( n ):

#*****************************************************************************80
#
## redheffer_matrix() returns the REDHEFFER matrix.
#
#  Formula:
#
#    if ( J = 1 or mod ( J, I ) == 0 )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#     1  1  1  1  1
#     1  1  0  1  0
#     1  0  1  0  0
#     1  0  0  1  0
#     1  0  0  0  1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    The diagonal entries of A are all 1.
#
#    A is a zero/one matrix.
#
#    N - int ( log2 ( N ) ) - 1 eigenvalues are equal to 1.
#
#    There is a real eigenvalue of magnitude approximately sqrt ( N ),
#    which is the spectral radius of the matrix.
#
#    There is a negative eigenvalue of value approximately -sqrt ( N ).
#
#    The remaining eigenvalues are "small", and there is a conjecture
#    that they lie inside the unit circle in the complex plane.
#
#    The determinant is equal to the Mertens function M(N).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Wayne Barrett, Tyler Jarvis,
#    Spectral Properties of a Matrix of Redheffer,
#    Linear Algebra and Applications,
#    Volume 162, 1992, pages 673-683.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == 0 or ( ( j + 1 ) % ( i + 1 ) ) == 0 ):
        a[i,j] = 1.0

  return a

def redheffer_determinant ( n ):

#*****************************************************************************80
#
## redheffer_determinant() returns the determinant of the REDHEFFER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = mertens ( n )

  return value

def redheffer_test ( ):

#*****************************************************************************80
#
## redheffer_test() tests redheffer_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'redheffer_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  redheffer_matrix() computes the REDHEFFER matrix.' )

  m = 5
  n = m

  a = redheffer_matrix ( n )
 
  r8mat_print ( m, n, a, '  REDHEFFER matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'redheffer_test' )
  print ( '  Normal end of execution.' )
  return

def reflection_random_determinant ( n, key ):

#*****************************************************************************80
#
## reflection_random_determinant(): determinant of the REFLECTION_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real DET: the determinant.
#
  det = - 1.0

  return det

def reflection_random_eigen_right ( n, key ):

#*****************************************************************************80
#
## reflection_random_eigen_right(): right eigenvectors of REFLECTION_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real Q(N,N), the eigenvector matrix.
#
  import numpy as np

  np.random.seed ( key )
#
#  Get a random vector v.
#
  v = np.random.normal ( 0.0, 1.0, size = n )

  v = v.reshape ( n, 1 )
#
#  Get the QR factorization.
#
  Q, R = np.linalg.qr ( v, mode = 'complete' )

  return Q

def reflection_random_eigenvalues ( n, key ):

#*****************************************************************************80
#
## reflection_random_eigenvalues(): eigenvalues of the REFLECTION_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real LAMDA(N), the eigenvalues.
#
  import numpy as np

  lamda = np.ones ( n )
  lamda[0] = -1.0

  return lamda

def reflection_random_inverse ( n, key ):

#*****************************************************************************80
#
## reflection_random_inverse(): inverse of the REFLECTION_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real A(N,N), the inverse matrix.
#
  import numpy as np

  np.random.seed ( key )
#
#  Get a random vector v.
#
  v = np.random.normal ( 0.0, 1.0, size = n )
#
#  Normalize.
#
  v = v / np.linalg.norm ( v )
#
#  A = I - 2 * v v'
#
  A = np.identity ( n ) - 2.0 * np.outer ( v, v )
#
#  Inverse is transpose.
#
  A = np.transpose ( A )

  return A

def reflection_random_matrix ( n, key ):

#*****************************************************************************80
#
## reflection_random_matrix() returns the REFLECTION_RANDOM matrix.
#
#  Properties:
#
#    A has determinant -1.
#
#    A will have a single eigenvalue of -1.   All other eigenvalues
#    will be +1.
#
#    A is an orthogonal matrix.
#
#    A*v = -v.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
#    real V(N): the vector that is exactly reflected by A.
#
  import numpy as np

  np.random.seed ( key )
#
#  Get a random vector v.
#
  v = np.random.normal ( 0.0, 1.0, size = n )
#
#  Normalize.
#
  v = v / np.linalg.norm ( v )
#
#  A = I - 2 * v v'
#
  A = np.identity ( n ) - 2.0 * np.outer ( v, v )

  return A, v

def reflection_random_test ( ):

#*****************************************************************************80
#
## reflection_random_test() tests reflection_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'reflection_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  reflection_random_matrix() computes the reflection_random matrix.' )

  n = 5
  key = 123456789
  A, v = reflection_random_matrix ( n, key )
  r8mat_print ( n, n, A, '  reflection_random matrix:' )
  r8vec_print ( n, v, '  vector v:' )
  Av = np.matmul ( A, v )
  r8vec_print ( n, Av, '  vector A*v' )
#
#  Terminate.
#
  print ( '' )
  print ( 'reflection_random_test' )
  print ( '  Normal end of execution.' )
  return

def ring_adj_matrix ( m, n ):

#*****************************************************************************80
#
## ring_adj_matrix() returns the ring_adj matrix.
#
#  Discussion:
#
#    This is the adjacency matrix for a set of points on a circle.
#
#  Example:
#
#    N = 5
#
#    0  1  0  0  1
#    1  0  1  0  0
#    0  1  0  1  0
#    0  0  1  0  1
#    1  0  0  1  0
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The determinant for N = 1 is 1, for N = 2 is -1, and for 2 < N,
#      mod ( N, 4 ) = 1 ==> det ( A ) =  2
#      mod ( N, 4 ) = 2 ==> det ( A ) = -4
#      mod ( N, 4 ) = 3 ==> det ( A ) =  2
#      mod ( N, 4 ) = 0 ==> det ( A ) =  0
#
#    A is a zero/one matrix.
#
#    A is an adjacency matrix.
#
#    A has a zero diagonal.
#
#    A is cyclic tridiagonal.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A has a constant row sum of 2.
#
#    Because it has a constant row sum of 2,
#    A has an eigenvalue of 2, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A has a constant column sum of 2.
#
#    Because it has a constant column sum of 2,
#    A has an eigenvalue of 2, and
#    a (left) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    A has an eigenvector of ( 1, 1, 1, ..., 1 ) with eigenvalue of 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( j == i + 1 or j == i - 1 or j == i + 1 - n or j == i - 1 + n ):
        a[i,j] = 1.0

  return a

def ring_adj_determinant ( n ):

#*****************************************************************************80
#
## ring_adj_determinant() returns the determinant of the ring_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  if ( n == 1 ):
    value = 1.0
  elif ( n == 2 ):
    value = -1.0
  elif ( ( n % 4 ) == 0 ):
    value = 0.0
  elif ( ( n % 4 ) == 1 ):
    value = 2.0
  elif ( ( n % 4 ) == 2 ):
    value = -4.0
  elif ( ( n % 4 ) == 3 ):
    value = 2.0

  return value

def ring_adj_null_left ( m, n ):

#*****************************************************************************80
#
## ring_adj_null_left() returns a left null vector of the ring_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(N), the null vector.
#
  import numpy as np

  if ( ( m % 4 ) != 0 ):
    print ( '' )
    print ( 'ring_adj_null_left - Fatal error!' )
    print ( '  M must be a multiple of 4.' )
    raise Exception ( 'ring_adj_null_left - Fatal error!' )

  x = np.zeros ( m )

  for i in range ( 0, m, 4 ):
    x[i]   = + 1.0
    x[i+1] = + 1.0
    x[i+2] = - 1.0
    x[i+3] = - 1.0

  return x

def ring_adj_null_right ( m, n ):

#*****************************************************************************80
#
## ring_adj_null_right() returns a right null vector of the ring_adj matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real X(N), the null vector.
#
  import numpy as np

  if ( ( n % 4 ) != 0 ):
    print ( '' )
    print ( 'ring_adj_null_right - Fatal error!' )
    print ( '  N must be a multiple of 4.' )
    raise Exception ( 'ring_adj_null_right - Fatal error!' )

  x = np.zeros ( n )

  for i in range ( 0, n, 4 ):
    x[i]   = + 1.0
    x[i+1] = + 1.0
    x[i+2] = - 1.0
    x[i+3] = - 1.0

  return x

def ring_adj_test ( ):

#*****************************************************************************80
#
## ring_adj_test() tests ring_adj_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ring_adj_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ring_adj_matrix() computes the ring_adj matrix.' )

  m = 6
  n = m

  a = ring_adj_matrix ( m, n )
  r8mat_print ( m, n, a, '  ring_adj matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ring_adj_test' )
  print ( '  Normal end of execution.' )
  return

def ris_matrix ( n ):

#*****************************************************************************80
#
## ris_matrix() returns the RIS matrix.
#
#  Discussion:
#
#    This is sometimes called the "dingdong" matrix, invented by F N Ris.
#
#  Formula:
#
#    A(I,J) = 1 / ( 3 + 2 * N - 2 * I - 2 * J )
#
#  Example:
#
#    N = 5
#
#    1/9  1/7  1/5  1/3   1
#    1/7  1/5  1/3   1   -1
#    1/5  1/3   1   -1  -1/3
#    1/3   1   -1  -1/3 -1/5
#     1   -1  -1/3 -1/5 -1/7
#
#  Properties:
#
#    A is a Cauchy matrix.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The eigenvalues of A cluster around PI/2 and -PI/2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Nash,
#    Compact Numerical Methods for Computers: Linear Algebra and
#    Function Minimisation,
#    John Wiley, 1979, page 210.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / float ( 2 * n - 2 * i - 2 * j - 1 )

  return a

def ris_determinant ( n ):

#*****************************************************************************80
#
## ris_determinant() returns the determinant of the RIS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  top = 1.0
  for i in range ( 1, n + 1 ):
    for j in range ( i + 1, n + 1 ):
      top = top * float ( 4 * ( i - j ) * ( i - j ) )

  bottom = 1.0
  for i in range ( 1, n + 1 ):
    for j in range ( 1, n + 1 ):
      bottom = bottom * float ( 3 + 2 * n - 2 * i - 2 * j )

  value = top / bottom

  return value

def ris_inverse ( n ):

#*****************************************************************************80
#
## ris_inverse() returns the inverse of the RIS matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      top = 1.0
      bot1 = 1.0
      bot2 = 1.0

      for k in range ( 0, n ):

        top = top * float ( 3 + 2 * n - 2 * ( j + 1 ) - 2 * ( k + 1 ) ) \
          * ( 3 + 2 * n - 2 * ( k + 1 ) - 2 * ( i + 1 ) )

        if ( k != j ):
          bot1 = bot1 * float ( 2 * ( k - j ) )

        if ( k != i ):
          bot2 = bot2 * float ( 2 * ( k - i ) )

      a[i,j] = top / ( float ( 3 + 2 * n - 2 * ( j + 1 ) - 2 * ( i + 1 ) ) \
        * bot1 * bot2 )

  return a

def ris_test ( ):

#*****************************************************************************80
#
## ris_test() tests ris_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ris_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ris_matrix() computes the RIS matrix.' )

  m = 5
  n = m

  a = ris_matrix ( n )
 
  r8mat_print ( m, n, a, '  RIS matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ris_test' )
  print ( '  Normal end of execution.' )
  return

def rodman_matrix ( m, n, alpha ):

#*****************************************************************************80
#
## rodman_matrix() returns the RODMAN matrix.
#
#  Formula:
#
#    If ( I = J )
#      A(I,J) = 1
#    else
#      A(I,J) = ALPHA
#
#  Example:
#
#    M = 5, N = 5, ALPHA = 2
#
#    1 2 2 2 2
#    2 1 2 2 2
#    2 2 1 2 2
#    2 2 2 1 2
#    2 2 2 2 1
#
#  Properties:
#
#    A is a special case of the combinatorial matrix.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is a circulant matrix: each row is shifted once to get the next row.
#
#    A has constant row sum.
#
#    Because it has a constant row sum of 1+(N-1)*ALPHA,
#    A has an eigenvalue of 1+(N-1)*ALPHA, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A has constant column sum.
#
#    Because it has a constant column sum of 1+(N-1)*ALPHA,
#    A has an eigenvalue of 1+(N-1)*ALPHA, and
#    a (left) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    A is positive definite for ALPHA < 1.
#
#    The eigenvalues and eigenvectors of A are:
#
#      For I = 1 to N-1:
#
#        LAMBDA(I) = 1 - ALPHA
#        V(I) = ( - sum ( 2 <= J <= N ) X(J), X(2), X(3), ..., X(N) )
#
#      For I = N:
#
#        LAMBDA(I) = 1 + ALPHA * ( N - 1 )
#        V(I) = ( 1, 1, 1, ..., 1 )
#
#    det ( A ) = ( 1 - ALPHA )^(N-1) * ( 1 + ALPHA * ( N - 1 ) ).
#
#    A is nonsingular if ALPHA is not 1, and ALPHA is not -1/(N-1).
#
#    The inverse of A is known.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real ALPHA, the parameter.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 1.0
      else:
        a[i,j] = alpha

  return a

def rodman_condition ( n, alpha ):

#*****************************************************************************80
#
## rodman_condition() computes the L1 condition of the RODMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, the parameter.
#
#  Output:
#
#    real VALUE, the L1 condition.
#
  a_norm = 1.0 + float ( n - 1 ) * abs ( alpha )

  top = abs ( 1.0 + alpha * float ( n - 2 ) ) \
    + float ( n - 1 ) * abs ( alpha )

  bot = abs ( 1.0 + alpha * float ( n - 2 ) \
    - alpha * alpha * float ( n - 1 ) )

  b_norm = top / bot

  value = a_norm * b_norm

  return value

def rodman_determinant ( n, alpha ):

#*****************************************************************************80
#
## rodman_determinant() returns the determinant of the RODMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, the parameter.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = ( 1.0 - alpha ) ** ( n - 1 ) * ( 1.0 + alpha * float ( n - 1 ) )

  return value

def rodman_eigen_right ( n, alpha ):

#*****************************************************************************80
#
## rodman_eigen_right() returns the right eigenvectors of the RODMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, the parameter.
#
#  Output:
#
#    real X(N,N), the right eigenvectors.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )

  for j in range ( 0, n - 1 ):
    x[  0,j] = +1.0
    x[j+1,j] = -1.0

  for i in range ( 0, n ):
    x[i,n-1] = 1.0

  return x

def rodman_eigenvalues ( n, alpha ):

#*****************************************************************************80
#
## rodman_eigenvalues() returns the eigenvalues of the RODMAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real ALPHA, the parameter.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n - 1 ):
    lam[i] = 1.0 - alpha

  lam[n-1] = 1.0 + alpha * float ( n - 1 )

  return lam

def rodman_inverse ( n, alpha ):

#*****************************************************************************80
#
## rodman_inverse() returns the inverse of the RODMAN matrix.
#
#  Formula:
#
#    If ( I = J )
#      A(I,J) = ( 1 + ALPHA * ( N - 2 ) ) /
#        ( 1 + ALPHA * ( N - 2 ) - ALPHA^2 * ( N - 1 ) )
#    else
#      A(I,J) = - ALPHA /
#        ( 1 + ALPHA * ( N - 2 ) - ALPHA^2 * ( N - 1 ) )
#
#  Example:
#
#    N = 5, ALPHA = 2.0
#
#   -0.7778    0.2222    0.2222    0.2222    0.2222
#    0.2222   -0.7778    0.2222    0.2222    0.2222
#    0.2222    0.2222   -0.7778    0.2222    0.2222
#    0.2222    0.2222    0.2222   -0.7778    0.2222
#    0.2222    0.2222    0.2222    0.2222   -0.7778
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real ALPHA, the parameter.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  bot = 1.0 + alpha * float ( n - 2 ) - alpha * alpha * float ( n - 1 )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = ( 1.0 + alpha * float ( n - 2 ) ) / bot
      else:
        a[i,j] = - alpha / bot

  return a

def rodman_test ( ):

#*****************************************************************************80
#
## rodman_test() tests rodman_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rodman_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rodman_matrix() computes the RODMAN matrix.' )

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )

  a = rodman_matrix ( m, n, alpha )
 
  r8mat_print ( m, n, a, '  RODMAN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rodman_test' )
  print ( '  Normal end of execution.' )
  return

def rosser1_matrix ( ):

#*****************************************************************************80
#
## rosser1_matrix() returns the ROSSER1 matrix.
#
#  Formula:
#
#    611  196 -192  407   -8  -52  -49   29
#    196  899  113 -192  -71  -43   -8  -44
#   -192  113  899  196   61   49    8   52
#    407 -192  196  611    8   44   59  -23
#     -8  -71   61    8  411 -599  208  208
#    -52  -43   49   44 -599  411  208  208
#    -49   -8    8   59  208  208   99 -911
#     29  -44   52  -23  208  208 -911   99
#
#  Properties:
#
#    A is singular.
#
#    det ( A ) = 0.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    The eigenvalues of A are:
#
#      a = sqrt(10405), b = sqrt(26),
#
#      LAMBDA = (-10*a, 0, 510-100*b, 1000, 1000, 510+100*b, 1020, 10*a)
#
#      ( 10*a = 1020.04901843, 510-100*b = 0.09804864072 )
#
#    The eigenvectors are
#
#      ( 2,  1,   1,  2, 102+a, 102+a, -204-2a, -204-2a )
#      ( 1,  2,  -2, -1,    14,    14,       7,       7 )
#      ( 2, -1,   1, -2,   5-b,  -5+b,  -10+2b,   10-2b )
#      ( 7, 14, -14, -7,    -2,    -2,      -1,      -1 )
#      ( 1, -2,  -2,  1,    -2,     2,      -1,       1 )
#      ( 2, -1,   1, -2,   5+b,  -5-b,  -10-2b,   10+2b )
#      ( 1, -2,  -2,  1,     2,    -2,       1,      -1 )
#      ( 2,  1,   1,  2, 102-a, 102-a, -204+2a, -204+2a )
#
#    trace ( A ) = 4040.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 4.10,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 61, 
#    LC: QA263.G68.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Output:
#
#    real A(8,8), the matrix.
#
  import numpy as np

  a = np.array ( [ \
      [  611.0,  196.0, -192.0,  407.0,   -8.0,  -52.0,  -49.0,   29.0 ], \
      [  196.0,  899.0,  113.0, -192.0,  -71.0,  -43.0,   -8.0,  -44.0 ], \
      [ -192.0,  113.0,  899.0,  196.0,   61.0,   49.0,    8.0,   52.0 ], \
      [  407.0, -192.0,  196.0,  611.0,    8.0,   44.0,   59.0,  -23.0 ], \
      [   -8.0,  -71.0,   61.0,    8.0,  411.0, -599.0,  208.0,  208.0 ], \
      [  -52.0,  -43.0,   49.0,   44.0, -599.0,  411.0,  208.0,  208.0 ], \
      [  -49.0,   -8.0,    8.0,   59.0,  208.0,  208.0,   99.0, -911.0 ], \
      [   29.0,  -44.0,   52.0,  -23.0,  208.0,  208.0, -911.0,   99.0 ] ] )

  return a

def rosser1_determinant ( ):

#*****************************************************************************80
#
## rosser1_determinant() returns the determinant of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 0.0

  return value

def rosser1_eigen_left ( ):

#*****************************************************************************80
#
## rosser1_eigen_left() returns left eigenvectors of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(8,8), the eigenvector matrix.
#
  import numpy as np

  a = np.sqrt ( 10405.0 )
  b = np.sqrt ( 26.0 )

  x = np.zeros ( ( 8, 8 ) )
#
#  Note that the matrix entries are listed by ROW
#
  x = np.array ( [ \
    [ 2.0, 1.0, 1.0, 2.0, 102.0 + a, 102.0 + a, -204.0 - 2.0 * a, -204.0 - 2.0 * a ], \
    [ 1.0, 2.0, -2.0, -1.0, 14.0, 14.0,       7.0,       7.0 ], \
    [ 2.0, -1.0, 1.0, -2.0, 5.0 - b, -5.0 + b, -10.0 + 2.0 * b, 10.0 - 2.0 * b ], \
    [ 7.0, 14.0, -14.0, -7.0,  -2.0, -2.0,      -1.0,      -1.0 ], \
    [ 1.0, -2.0,  -2.0,  1.0,  -2.0, 2.0,      -1.0,       1.0 ], \
    [ 2.0, -1.0, 1.0, -2.0, 5.0 + b, -5.0 - b, -10.0 - 2.0 * b, 10.0 + 2.0 * b ], \
    [ 1.0, -2.0,  -2.0,  1.0,   2.0, -2.0,       1.0,      -1.0 ], \
    [ 2.0, 1.0, 1.0, 2.0, 102.0 - a, 102.0 - a, -204.0 + 2.0 * a, -204.0 + 2.0 * a ] ] )

  return x

def rosser1_eigen_right ( ):

#*****************************************************************************80
#
## rosser1_eigen_right() returns right eigenvectors of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(8,8), the eigenvector matrix.
#
  import numpy as np

  a = np.sqrt ( 10405.0 )
  b = np.sqrt ( 26.0 )

  x = np.zeros ( ( 8, 8 ) )
#
#  Note that the matrix entries are listed by ROW
#
  x = np.array ( [ \
    [ 2.0, 1.0, 1.0, 2.0, 102.0 + a, 102.0 + a, -204.0 - 2.0 * a, -204.0 - 2.0 * a ], \
    [ 1.0, 2.0, -2.0, -1.0, 14.0, 14.0,       7.0,       7.0 ], \
    [ 2.0, -1.0, 1.0, -2.0, 5.0 - b, -5.0 + b, -10.0 + 2.0 * b, 10.0 - 2.0 * b ], \
    [ 7.0, 14.0, -14.0, -7.0,  -2.0, -2.0,      -1.0,      -1.0 ], \
    [ 1.0, -2.0,  -2.0,  1.0,  -2.0, 2.0,      -1.0,       1.0 ], \
    [ 2.0, -1.0, 1.0, -2.0, 5.0 + b, -5.0 - b, -10.0 - 2.0 * b, 10.0 + 2.0 * b ], \
    [ 1.0, -2.0,  -2.0,  1.0,   2.0, -2.0,       1.0,      -1.0 ], \
    [ 2.0, 1.0, 1.0, 2.0, 102.0 - a, 102.0 - a, -204.0 + 2.0 * a, -204.0 + 2.0 * a ] ] )

  x = np.transpose ( x )

  return x

def rosser1_eigenvalues ( ):

#*****************************************************************************80
#
## rosser1_eigenvalues() returns the eigenvalues of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real LAMBDA(8,1), the eigenvalues.
#
  import numpy as np

  a = np.sqrt ( 10405.0 )
  b = np.sqrt ( 26.0 )

  lam = np.array ( [ \
    [  -10.0 * a ], \
    [    0.0 ], \
    [  510.0 - 100.0 * b ], \
    [ 1000.0 ], \
    [ 1000.0 ], \
    [  510.0 + 100.0 * b ], \
    [ 1020.0 ], \
    [ 10.0 * a ] ] )

  return lam

def rosser1_null_left ( ):

#*****************************************************************************80
#
## rosser1_null_left() returns a left null vector of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(8), the null vector.
#
  import numpy as np

  x = np.array ( [ \
    [  1.0 ], \
    [  2.0 ], \
    [ -2.0 ], \
    [ -1.0 ], \
    [ 14.0 ], \
    [ 14.0 ], \
    [  7.0 ], \
    [  7.0 ] ] )

  return x

def rosser1_eigenvalues ( ):

#*****************************************************************************80
#
## rosser1_eigenvalues() returns the eigenvalues of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real LAM(8), the eigenvalues.
#
  import numpy as np

  a = np.sqrt ( 10405.0 )
  b = np.sqrt ( 26.0 )

  lam = np.array ( [ \
    [  -10.0 * a ], \
    [    0.0 ], \
    [  510.0 - 100.0 * b ], \
    [ 1000.0 ], \
    [ 1000.0 ], \
    [  510.0 + 100.0 * b ], \
    [ 1020.0 ], \
    [ 10.0 * a ] ] )

  return lam

def rosser1_null_right ( ):

#*****************************************************************************80
#
## rosser1_null_right() returns a right null vector of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X(8), the null vector.
#
  import numpy as np

  x = np.array ( [ \
    [  1.0 ], \
    [  2.0 ], \
    [ -2.0 ], \
    [ -1.0 ], \
    [ 14.0 ], \
    [ 14.0 ], \
    [  7.0 ], \
    [  7.0 ] ] )

  return x

def rosser1_test ( ):

#*****************************************************************************80
#
## rosser1_test() tests rosser1_matrix().
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
  import platform

  print ( '' )
  print ( 'rosser1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rosser1_matrix() computes the ROSSER1 matrix.' )

  n = 8
  a = rosser1_matrix ( )
  r8mat_print ( n, n, a, '  ROSSER1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rosser1_test' )
  print ( '  Normal end of execution.' )
  return

def routh_matrix ( n, x ):

#*****************************************************************************80
#
## routh_matrix() returns the ROUTH matrix.
#
#  Formula:
#
#    A is tridiagonal.
#    A(1,1)   =          X(1).
#    A(I-1,I) =   sqrt ( X(I) ), for I = 2 to N.
#    A(I,I-1) = - sqrt ( X(I) ), for I = 2 to N.
#
#  Example:
#
#    N = 5, X = ( 1, 4, 9, 16, 25 )
#
#    1 -2  0  0  0
#    2  0 -3  0  0
#    0  3  0 -4  0
#    0  0  4  0 -5
#    0  0  0  5  0
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    det ( A ) = product ( X(N) * X(N-2) * X(N-4) * ... * X(N+1-2*(N/2)) )
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N), the data that defines the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 and j == 0 ):
        a[i,j] = abs ( x[0] )
      elif ( i == j + 1 ):
        a[i,j] = np.sqrt ( abs ( x[i] ) )
      elif ( i == j - 1 ):
        a[i,j] = - np.sqrt ( abs ( x[i+1] ) )

  return a

def routh_determinant ( n, x ):

#*****************************************************************************80
#
## routh_determinant() returns the determinant of the ROUTH matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N-1), the elements.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0
  for i in range ( n - 1, -1, -2 ):
    value = value * x[i]

  return value

def routh_test ( ):

#*****************************************************************************80
#
## routh_test() tests routh_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'routh_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  routh_matrix() computes the ROUTH matrix.' )

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )

  a = routh_matrix ( n, x )
 
  r8mat_print ( m, n, a, '  ROUTH matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'routh_test' )
  print ( '  Normal end of execution.' )
  return

def rutis1_matrix ( ):

#*****************************************************************************80
#
## rutis1_matrix() returns the RUTIS1 matrix.
#
#  Example:
#
#    6 4 4 1
#    4 6 1 4
#    4 1 6 4
#    1 4 4 6
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A has constant row sums.
#
#    Because it has a constant row sum of 15,
#    A has an eigenvalue of 15, and
#    a (right) eigenvector of ( 1, 1, 1, 1 ).
#
#    A has constant column sums.
#
#    Because it has a constant column sum of 15,
#    A has an eigenvalue of 15, and
#    a (left) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A has a repeated eigenvalue.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
   [  6.0,  4.0,  4.0,  1.0 ], \
   [  4.0,  6.0,  1.0,  4.0 ], \
   [  4.0,  1.0,  6.0,  4.0 ], \
   [  1.0,  4.0,  4.0,  6.0 ] ] )

  return a

def rutis1_condition ( ):

#*****************************************************************************80
#
## rutis1_condition() returns the L1 condition of the RUTIS1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the condition.
#
  a_norm = 15.0
  b_norm = 1.0
  value = a_norm * b_norm

  return value

def rutis1_determinant ( ):

#*****************************************************************************80
#
## rutis1_determinant() returns the determinant of the RUTIS1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = - 375.0

  return value

def rutis1_eigen_right ( ):

#*****************************************************************************80
#
## rutis1_eigen_right() returns the right eigenvectors of the RUTIS1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 1.0,  1.0,  0.0,  1.0 ], \
    [ 1.0,  0.0,  1.0, -1.0 ], \
    [ 1.0,  0.0, -1.0, -1.0 ], \
    [ 1.0, -1.0,  0.0,  1.0 ] ] )

  return a

def rutis1_eigenvalues ( ):

#*****************************************************************************80
#
## rutis1_eigenvalues() returns the eigenvalues of the RUTIS1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real LAM(4), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
    [ 15.0 ], \
    [  5.0 ], \
    [  5.0 ], \
    [ -1.0 ] ] )

  return lam

def rutis1_inverse ( ):

#*****************************************************************************80
#
## rutis1_inverse() returns the inverse of the RUTIS1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
    [ -2.0,  4.0,  4.0, -5.0 ], \
    [  4.0, -2.0, -5.0,  4.0 ], \
    [  4.0, -5.0, -2.0,  4.0 ], \
    [ -5.0,  4.0,  4.0, -2.0 ] ] )

  for i in range ( 0, 4 ):
    for j in range ( 0, 4 ):
      a[i,j] = a[i,j] / 15.0

  return a

def rutis1_test ( ):

#*****************************************************************************80
#
## rutis1_test() tests rutis1_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rutis1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rutis1_matrix() computes the RUTIS1 matrix.' )

  n = 4
  a = rutis1_matrix ( )
  r8mat_print ( n, n, a, '  RUTIS1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rutis1_test' )
  print ( '  Normal end of execution.' )
  return

def rutis2_matrix ( ):

#*****************************************************************************80
#
## rutis2_matrix() returns the RUTIS2 matrix.
#
#  Example:
#
#    5 4 1 1
#    4 5 1 1
#    1 1 4 2
#    1 1 2 4
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A has distinct eigenvalues.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
   [  5.0,  4.0,  1.0,  1.0 ], \
   [  4.0,  5.0,  1.0,  1.0 ], \
   [  1.0,  1.0,  4.0,  2.0 ], \
   [  1.0,  1.0,  2.0,  4.0 ] ] )

  return a

def rutis2_condition ( ):

#*****************************************************************************80
#
## rutis2_condition() returns the L1 condition of the RUTIS2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the condition.
#
  a_norm = 11.0
  b_norm = 1.04
  value = a_norm * b_norm

  return value

def rutis2_determinant ( ):

#*****************************************************************************80
#
## rutis2_determinant() returns the determinant of the RUTIS2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 100.0

  return value

def rutis2_eigen_right ( ):

#*****************************************************************************80
#
## rutis2_eigen_right() returns the right eigenvectors of the RUTIS2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
    [  2.0, -1.0,  0.0, -1.0 ], \
    [  2.0, -1.0,  0.0,  1.0 ], \
    [  1.0,  2.0, -1.0,  0.0 ], \
    [  1.0,  2.0,  1.0,  0.0 ] ] )

  return a

def rutis2_eigenvalues ( ):

#*****************************************************************************80
#
## rutis2_eigenvalues() returns the eigenvalues of the RUTIS2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real LAM(4), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
    [ 10.0 ], \
    [  5.0 ], \
    [  2.0 ], \
    [  1.0 ] ] )

  return lam

def rutis2_inverse ( ):

#*****************************************************************************80
#
## rutis2_inverse() returns the inverse of the RUTIS2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
    [  28.0,  -22.0, -1.0, -1.0 ], \
    [ -22.0,   28.0, -1.0, -1.0 ], \
    [  -1.0,   -1.0, 17.0, -8.0 ], \
    [  -1.0,   -1.0, -8.0, 17.0 ] ] )

  for j in range ( 0, 4 ):
    for i in range ( 0, 4 ):
      a[i,j] = a[i,j] / 50.0

  return a

def rutis2_test ( ):

#*****************************************************************************80
#
## rutis2_test() tests rutis2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rutis2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rutis2_matrix() computes the RUTIS2 matrix.' )

  n = 4
  a = rutis2_matrix ( )
  r8mat_print ( n, n, a, '  RUTIS2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rutis2_test' )
  print ( '  Normal end of execution.' )
  return

def rutis3_matrix ( ):

#*****************************************************************************80
#
## rutis3_matrix() returns the RUTIS3 matrix.
#
#  Example:
#
#    4 -5  0  3
#    0  4 -3 -5
#    5 -3  4  0
#    3  0  5  4
#
#  Properties:
#
#    A is not symmetric: A' /= A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A has distinct eigenvalues.
#
#    A has a pair of complex eigenvalues.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 4.0, -5.0,  0.0,  3.0 ], \
    [ 0.0,  4.0, -3.0, -5.0 ], \
    [ 5.0, -3.0,  4.0,  0.0 ], \
    [ 3.0,  0.0,  5.0,  4.0 ] ] )

  return a

def rutis3_condition ( ):

#*****************************************************************************80
#
## rutis3_condition() returns the L1 condition of the RUTIS3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the condition.
#
  a_norm = 12.0
  b_norm = 0.5
  value = a_norm * b_norm

  return value

def rutis3_determinant ( ):

#*****************************************************************************80
#
## rutis3_determinant() returns the determinant of the RUTIS3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 624.0

  return value

def rutis3_inverse ( ):

#*****************************************************************************80
#
## rutis3_inverse() returns the inverse of the RUTIS3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
    [  103.0,  125.0,   -5.0,  79.0 ], \
    [    5.0,  103.0,  -79.0, 125.0 ], \
    [ -125.0,  -79.0,  103.0,  -5.0 ], \
    [   79.0,    5.0, -125.0, 103.0 ] ] )

  for i in range ( 0, 4 ):
    for j in range ( 0, 4 ):
      a[i,j] = a[i,j] / 624.0

  return a

def rutis3_test ( ):

#*****************************************************************************80
#
## rutis3_test() tests rutis3_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rutis3_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rutis3_matrix() computes the RUTIS3 matrix.' )

  n = 4
  a = rutis3_matrix ( )
  r8mat_print ( n, n, a, '  RUTIS3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rutis3_test' )
  print ( '  Normal end of execution.' )
  return

def rutis4_matrix ( n ):

#*****************************************************************************80
#
## rutis4_matrix() returns the RUTIS4 matrix.
#
#  Example:
#
#    N = 6
#
#    14 14  6  1  0  0
#    14 20 15  6  1  0
#     6 15 20 15  6  1
#     1  6 15 20 15  6
#     0  1  6 15 20 14
#     0  0  1  6 14 14
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is banded with a bandwidth of 7.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is the cube of the scalar tridiagonal matrix whose diagonals
#    are ( 1, 2, 1 ).
#
#    LAMBDA(I) = 64 * ( cos ( i * pi / ( 2 * ( n + 1 ) ) ) )^6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( 0 <= i - 3 ):
      a[i,i-3] = 1.0

    if ( 0 <= i - 2 ):
      a[i,i-2] = 6.0

    if ( 0 <= i - 1 ):
      a[i,i-1] = 15.0

    a[i,i] = 20.0

    if ( i + 1 <= n - 1 ):
      a[i,i+1] = 15.0

    if ( i + 2 <= n - 1 ):
      a[i,i+2] = 6.0

    if ( i + 3 <= n - 1 ):
      a[i,i+3] = 1.0

  a[0,0] = 14.0
  a[0,1] = 14.0
  a[1,0] = 14.0

  a[n-1,n-1] = 14.0
  a[n-2,n-1] = 14.0
  a[n-1,n-2] = 14.0

  return a

def rutis4_determinant ( n ):

#*****************************************************************************80
#
## rutis4_determinant() returns the determinant of the RUTIS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  value = 1.0

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    value = value * 64.0 * ( np.cos ( angle ) ) ** 6

  return value

def rutis4_eigenvalues ( n ):

#*****************************************************************************80
#
## rutis4_eigenvalues() returns the eigenvalues of the RUTIS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    lam[i] = 64.0 * ( np.cos ( angle ) ) ** 6

  return lam

def rutis4_inverse ( n ):

#*****************************************************************************80
#
## rutis4_inverse() returns the inverse of the RUTIS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  c = oto_inverse ( n )

  b = r8mat_mm ( n, n, n, c, c )

  a = r8mat_mm ( n, n, n, c, b )

  return a

def rutis4_test ( ):

#*****************************************************************************80
#
## rutis4_test() tests rutis4_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rutis4_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rutis4_matrix() computes the RUTIS4 matrix.' )

  n = 5
  a = rutis4_matrix ( n )
  r8mat_print ( n, n, a, '  RUTIS4 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rutis4_test' )
  print ( '  Normal end of execution.' )
  return

def rutis5_matrix ( ):

#*****************************************************************************80
#
## rutis5_matrix() returns the RUTIS5 matrix.
#
#  Example:
#
#    10  1  4  0
#    1  10  5 -1
#    4   5 10  7
#    0  -1  7  9
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Todd,
#    Basic Numerical Mathematics, Volume 2: Numerical Algebra,
#    Academic Press, 1977.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
   [ 10.0,  1.0,  4.0,  0.0 ], \
   [  1.0, 10.0,  5.0, -1.0 ], \
   [  4.0,  5.0, 10.0,  7.0 ], \
   [  0.0, -1.0,  7.0,  9.0 ] ] )

  return a

def rutis5_condition ( ):

#*****************************************************************************80
#
## rutis5_condition() returns the L1 condition of the RUTIS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real COND, the L1 condition number.
#
  cond = 62608.0

  return cond

def rutis5_determinant ( ):

#*****************************************************************************80
#
## rutis5_determinant() returns the determinant of the RUTIS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def rutis5_eigen_right ( ):

#*****************************************************************************80
#
## rutis5_eigen_right() returns the right eigenvectors of the RUTIS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(4,4), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
   [  0.356841883715928, \
      0.382460905084129, \
      0.718205429169617, \
      0.458877421126365 ], \
   [ -0.341449101169948, \
     -0.651660990948502, \
      0.087555987078632, \
      0.671628180850787 ], \
   [  0.836677864423576, \
     -0.535714651223808, \
     -0.076460316709461, \
     -0.084461728708607 ], \
   [ -0.236741488801405, \
     -0.376923628103094, \
      0.686053008598214, \
    - 0.575511351279045 ] ] )

  a = np.transpose ( a )
  
  return a

def rutis5_eigenvalues ( ):

#*****************************************************************************80
#
## rutis5_eigenvalues() returns the eigenvalues of the RUTIS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real LAM(4), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
    [ 19.122479087555860 ], \
    [ 10.882816916492464 ], \
    [  8.994169735037230 ], \
    [  0.000534260914449 ] ] )

  return lam

def rutis5_inverse ( ):

#*****************************************************************************80
#
## rutis5_inverse() returns the inverse of the RUTIS5 matrix.
#
#  Example:
#
#     105  167 -304  255
#     167  266 -484  406
#    -304 -484  881 -739
#     255  406 -739  620
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Todd,
#    Basic Numerical Mathematics, Volume 2: Numerical Algebra,
#    Academic Press, 1977.
#
#  Output:
#
#    real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
    [  105.0,  167.0, -304.0,  255.0 ], \
    [  167.0,  266.0, -484.0,  406.0 ], \
    [ -304.0, -484.0,  881.0, -739.0 ], \
    [  255.0,  406.0, -739.0,  620.0 ] ] )

  return a

def rutis5_test ( ):

#*****************************************************************************80
#
## rutis5_test() tests rutis5_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rutis5_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rutis5_matrix() computes the RUTIS5 matrix.' )

  n = 4
  a = rutis5_matrix ( )
  r8mat_print ( n, n, a, '  RUTIS5 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rutis5_test' )
  print ( '  Normal end of execution.' )
  return

def schur_block_matrix ( n, x, y ):

#*****************************************************************************80
#
## schur_block_matrix() returns the SCHUR BLOCK matrix.
#
#  Formula:
#
#    if ( i == j )
#      a(i,j) = x( (i+1)/2 )
#    else ( mod ( i, 2 ) == 1 & j == i + 1 )
#      a(i,j) = y( (i+1)/2 )
#    else ( mod ( i, 2 ) == 0 & j == i - 1 )
#      a(i,j) = -y( (i+1)/2 )
#    else
#      a(i,j) = 0.0
#
#  Example:
#
#    N = 5, X = ( 1, 2, 3 ), Y = ( 4, 5 )
#
#    1  4    0    0    0
#   -4  1    0    0    0
#    0  0    2    5    0
#    0  0   -5    2    0
#    0  0    0    0    3
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is block diagonal, with the blocks being 2 by 2 or 1 by 1 in size.
#
#    A is in real Schur form.
#
#    The eigenvalues of A are X(I) +/- sqrt ( - 1 ) * Y(I)
#
#    A is tridiagonal.
#
#    A is banded, with bandwidth 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Francoise Chatelin,
#    Section 4.2.7,
#    Eigenvalues of Matrices,
#    John Wiley, 1993.
#
#    Francoise Chatelin, Valerie Fraysse,
#    Qualitative computing: Elements of a theory for finite precision
#    computation, Lecture notes,
#    CERFACS, Toulouse, France and THOMSON-CSF, Orsay, France, June 1993.
#
#  Input:
#
#    integer N, the order of A.
#
#    real X( (N+1)/2 ), specifies the diagonal elements
#    of A.
#
#    real Y( N/2 ), specifies the off-diagonal elements 
#    of the Schur blocks.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    ih = ( i // 2 )
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = x[ih]
      elif ( ( i % 2 ) == 0 and j == i + 1 ):
        a[i,j] = y[ih]
      elif ( ( i % 2 ) == 1 and j == i - 1 ):
        a[i,j] = - y[ih]

  return a

def schur_block_determinant ( n, x, y ):

#*****************************************************************************80
#
## schur_block_determinant() returns the determinant of the SCHUR_BLOCK matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X( (N+1)/2 ), specifies the diagonal 
#    elements of A.
#
#    real Y( N/2 ), specifies the off-diagonal 
#    elements of the Schur blocks.
#
#  Output:
#
#    real VALUE, the determinant of A.
#
  value = 1.0

  ihi = ( n // 2 )
  for i in range ( 0, ihi ):
    value = value * ( x[i] ** 2 + y[i] ** 2 )

  if ( ( n % 2 ) == 1 ):
    value = value * x[ihi]

  return value

def schur_block_inverse ( n, x, y ):

#*****************************************************************************80
#
## schur_block_inverse() returns the inverse of the SCHUR_BLOCK matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X( (N+1)/2 ), specifies the diagonal elements
#    of A.
#
#    real Y( N/2 ), specifies the off-diagonal elements 
#    of the Schur blocks.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      k = ( i // 2 )

      if ( i == j ):

        if ( i == n - 1 and ( n % 2 ) == 1 ):
          a[i,j] = 1.0 / x[k]
        else:
          a[i,j] = x[k] / ( x[k] ** 2 + y[k] ** 2 )

      elif ( ( i % 2 ) == 0 and j == i + 1 ):

        a[i,j] = - y[k] / ( x[k] ** 2 + y[k] ** 2 )

      elif ( ( i % 2 ) == 1 and j == i - 1 ):

        a[i,j] =   y[k] / ( x[k] ** 2 + y[k] ** 2 )

  return a

def schur_block_test ( ):

#*****************************************************************************80
#
## schur_block_test() tests schur_block_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'schur_block_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  schur_block_matrix() computes the SCHUR_BLOCK matrix.' )

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  x_n = ( ( n + 1 ) // 2 )
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( x_n )
  y_n = ( n // 2 )
  y = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( y_n )
  a = schur_block_matrix ( n, x, y )

  r8mat_print ( n, n, a, '  SCHUR_BLOCK matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'schur_block_test' )
  print ( '  Normal end of execution.' )
  return

def spd_random_matrix ( n, key ):

#*****************************************************************************80
#
## spd_random_matrix() returns a random symmetric positive definite matrix.
#
#  Discussion:
#
#    The matrix returned will have eigenvalues in the range [0,1].
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is positive definite: 0 < x'*A*x for nonzero x.
#
#    The eigenvalues of A will be real.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np
#
#  Get a random set of eigenvalues.
#
  np.random.seed ( key )
  lam = np.random.rand ( n )
#
#  Get a random orthogonal matrix Q.
#
  q = orthogonal_random_matrix ( n, key )
#
#  Set A = Q * Lambda * Q'.
#
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * lam[k] * q[j,k]

  return a

def spd_random_determinant ( n, key ):

#*****************************************************************************80
#
## spd_random_determinant() returns the determinant of the spd random matrix.
#
#  Discussion:
#
#    This routine will only work properly if the SAME value of SEED
#    is input that was input to spd_random.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  np.random.seed ( key )
  lam = np.random.rand ( n )

  value = np.prod ( lam )

  return value

def spd_random_eigen_right ( n, key ):

#*****************************************************************************80
#
## spd_random_eigen_right() returns the right eigenvectors of the spd random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real Q(N,N), the matrix.
#
  import numpy as np
#
#  Get a random set of eigenvalues.
#
  np.random.seed ( key )
  lam = np.random.rand ( n )
#
#  Get a random orthogonal matrix Q.
#
  q = orthogonal_random_matrix ( n, key )

  return q

def spd_random_eigenvalues ( n, key ):

#*****************************************************************************80
#
## spd_random_eigenvalues() returns the eigenvalues of the spd random matrix.
#
#  Discussion:
#
#    This routine will only work properly if the SAME value of SEED
#    is input that was input to spd_random_matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  np.random.seed ( key )
  lam = np.random.rand ( n )

  return lam

def spd_random_inverse ( n, key ):

#*****************************************************************************80
#
## spd_random_inverse() returns the inverse of the spd random matrix.
#
#  Discussion:
#
#    The matrix returned will have eigenvalues in the range [0,1].
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is positive definite: 0 < x'*A*x for nonzero x.
#
#    The eigenvalues of A will be real.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    integer KEY, a positive value that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
#
#  Get a random set of eigenvalues.
#
  np.random.seed ( key )
  lam = np.random.rand ( n )
#
#  Get a random orthogonal matrix Q.
#
  q = orthogonal_random_matrix ( n, key )
#
#  Set A = Q * Lambda * Q'.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * ( 1.0 / lam[k] ) * q[j,k]

  return a

def spd_random_test ( ):

#*****************************************************************************80
#
## spd_random_test() tests spd_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'spd_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  spd_random_matrix() computes the spd_random matrix.' )

  n = 5
  key = 123456789
  a = spd_random_matrix ( n, key )

  r8mat_print ( n, n, a, '  spd_random matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'spd_random_test' )
  print ( '  Normal end of execution.' )
  return

def spline_matrix ( n, x ):

#*****************************************************************************80
#
## spline_matrix() returns the SPLINE matrix.
#
#  Discussion:
#
#    This matrix arises during interpolation with cubic splines.
#
#  Formula:
#
#    if ( I = 1 and J = I )
#      A(I,J) = 2 * X(I)
#    elseif ( I = 1 and J = I + 1 )
#      A(I,J) = X(I)
#    elseif ( I = N and J = I )
#      A(I,J) = 2 * X(N-1)
#    elseif ( I = N and J = I - 1 )
#      A(I,J) = X(N-1)
#    elseif ( J = I )
#      A(I,J) = 2 * (X(I-1)+X(I))
#    elseif ( J = I-1 )
#      A(I,J) = X(I-1)
#    elseif ( J = I + 1 )
#      A(I,J) = X(I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#    X = ( 1, 1, 1, 1 )
#
#    2   1   0   0  0
#    1   4   1   0  0
#    0   1   4   1  0
#    0   0   1   4  1
#    0   0   0   1  2
#
#    N = 5
#    X = ( 1, 2, 3, 4 )
#
#    2   1   0   0  0
#    1   6   2   0  0
#    0   2  10   3  0
#    0   0   3  14  4
#    0   0   0   4  8
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    If the entries of X are positive, then A is positive definite.
#
#    If the entries of X are all of one sign, then A is diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(N-1), values that represent the spacing 
#    between points, and which define the entries of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 and j == 0 ):
        a[i,j] = 2.0 * x[0]
      elif ( i == 0 and j == i + 1 ):
        a[i,j] = x[0]
      elif ( i == n - 1 and j == i ):
        a[i,j] = 2.0 * x[n-2]
      elif ( i == n and j == i - 1 ):
        a[i,j] = x[n-2]
      elif ( j == i ):
        a[i,j] = 2.0 * ( x[i-1] + x[i] )
      elif ( j == i - 1 ):
        a[i,j] = x[i-1]
      elif ( j == i + 1 ):
        a[i,j] = x[i]

  return a

def spline_determinant ( n, x ):

#*****************************************************************************80
#
## spline_determinant() returns the determinant of the SPLINE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N-1), the elements.
#
#  Output:
#
#    real VALUE, the determinant.
#
  determ_nm1 = 2.0 * x[n-2]

  if ( n == 1 ):
    value = determ_nm1
    return value

  determ_nm2 = determ_nm1
  if ( n == 2 ):
    determ_nm1 = 4.0 *            x[n-2]   * x[n-2] - x[n-2] * x[n-2]
  else:
    determ_nm1 = 4.0 * ( x[n-3] + x[n-2] ) * x[n-2] - x[n-2] * x[n-2]

  if ( n == 2 ):
    value = determ_nm1
    return value

  for i in range ( n - 3, -1, -1 ):

    if ( i == 0 ):
      value = 2.0 *            x[i]   * determ_nm1 - x[i] * x[i] * determ_nm2
    else:
      value = 2.0 * ( x[i-1] + x[i] ) * determ_nm1 - x[i] * x[i] * determ_nm2
 
    determ_nm2 = determ_nm1
    determ_nm1 = value
 
  return value

def spline_inverse ( n, x ):

#*****************************************************************************80
#
## spline_inverse() returns the inverse of the SPLINE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    CM daFonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real X(N-1), the parameters.
#
#  Output:
#
#    real A(N,N), the inverse of the matrix.
#
  import numpy as np

  d = np.zeros ( n )
  d[n-1] = 2.0 * x[n-2]
  for i in range ( n - 2, 0, -1 ):
    d[i] = 2.0 * ( x[i-1] + x[i] ) - x[i] * x[i] / d[i+1]
  d[0] = 2.0 * x[0] - x[0] * x[0] / d[1]

  e = np.zeros ( n )
  e[0] = 2.0 * x[0]
  for i in range ( 1, n - 1 ):
    e[i] = 2.0 * ( x[i-1] + x[i] ) - x[i-1] * x[i-1] / e[i-1]
  e[n-1] = 2.0 * x[n-2] - x[n-2] * x[n-2] / e[n-2]

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    for j in range ( 0, i + 1 ):
      p1 = 1.0
      for k in range ( j, i ):
        p1 = p1 * x[k]
      p2 = 1.0
      for k in range ( i + 1, n ):
        p2 = p2 * d[k]
      p3 = 1.0
      for k in range ( j, n ):
        p3 = p3 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 * p2 / p3

    for j in range ( i + 1, n ):
      p1 = 1.0
      for k in range ( i, j ):
        p1 = p1 * x[k]
      p2 = 1.0
      for k in range ( j + 1, n ):
        p2 = p2 * d[k]
      p3 = 1.0
      for k in range ( i, n ):
        p3 = p3 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 * p2 / p3

  return a

def spline_test ( ):

#*****************************************************************************80
#
## spline_test() tests spline_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'spline_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  spline_matrix() computes the SPLINE matrix.' )

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n - 1 )

  a = spline_matrix ( n, x )
 
  r8mat_print ( m, n, a, '  SPLINE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'spline_test' )
  print ( '  Normal end of execution.' )
  return

def stirling_matrix ( m, n ):

#*****************************************************************************80
#
## stirling_matrix() returns the STIRLING matrix.
#
#  Comments:
#
#    The absolute value of the Stirling number S1(I,J) gives the number
#    of permutations on I objects having exactly J cycles, while the
#    sign of the Stirling number records the sign (odd or even) of
#    the permutations.  For example, there are six permutations on 3 objects:
#
#      A B C   3 cycles (A) (B) (C)
#      A C B   2 cycles (A) (BC)
#      B A C   2 cycles (AB) (C)
#      B C A   1 cycle  (ABC)
#      C A B   1 cycle  (ABC)
#      C B A   2 cycles (AC) (B)
#
#    There are
#
#      2 permutations with 1 cycle, and S1(3,1) = 2
#      3 permutations with 2 cycles, and S1(3,2) = -3,
#      1 permutation with 3 cycles, and S1(3,3) = 1.
#
#    Since there are N! permutations of N objects, the sum of the absolute
#    values of the Stirling numbers in a given row,
#
#      sum ( 1 <= J <= I ) abs ( S1(I,J) ) = N!
#
#  First terms:
#
#    I/J:  1     2      3     4     5    6    7    8
#
#    1     1     0      0     0     0    0    0    0
#    2    -1     1      0     0     0    0    0    0
#    3     2    -3      1     0     0    0    0    0
#    4    -6    11     -6     1     0    0    0    0
#    5    24   -50     35   -10     1    0    0    0
#    6  -120   274   -225    85   -15    1    0    0
#    7   720 -1764   1624  -735   175  -21    1    0
#    8 -5040 13068 -13132  6769 -1960  322  -28    1
#
#  Recursion:
#
#    S1(I,1) = (-1)^(I-1) * (I-1)! for all I.
#    S1(I,I) = 1 for all I.
#    S1(I,J) = 0 if I < J.
#
#    S1(I,J) = S1(I-1,J-1) - (I-1) * S1(I-1,J)
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is lower triangular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    After row 1, each row sums to 0.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )
  
  a[0,0] = 1.0

  for i in range ( 1, m ):

    a[i,0] = - float ( i ) * a[i-1,0]

    for j in range ( 1, n ):
      a[i,j] = a[i-1,j-1] - float ( i ) * a[i-1,j]

  return a

def stirling_determinant ( n ):

#*****************************************************************************80
#
## stirling_determinant() returns the determinant of the STIRLING matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def stirling_inverse ( n ):

#*****************************************************************************80
#
## stirling_inverse() returns the inverse of the STIRLING matrix.
#
#  Comments:
#
#    The inverse of S1, the matrix of Stirling numbers of the first kind,
#    is S2, the matrix of Stirling numbers of the second kind.
#
#    S2(I,J) represents the number of distinct partitions of I elements
#    into J nonempty sets.  For any I, the sum over J of the Stirling
#    numbers S2(I,J) is represented by B(I), called "Bell's number",
#    and represents the number of distinct partitions of I elements.
#
#    For example, with 4 objects, there are:
#
#    1 partition into 1 set:
#
#      (A,B,C,D)
#
#    7 partitions into 2 sets:
#
#      (A,B,C) (D)
#      (A,B,D) (C)
#      (A,C,D) (B)
#      (A) (B,C,D)
#      (A,B) (C,D)
#      (A,C) (B,D)
#      (A,D) (B,C)
#
#    6 partitions into 3 sets:
#
#      (A,B) (C) (D)
#      (A) (B,C) (D)
#      (A) (B) (C,D)
#      (A,C) (B) (D)
#      (A,D) (B) (C)
#      (A) (B,D) (C)
#
#    1 partition into 4 sets:
#
#      (A) (B) (C) (D)
#
#    So S2(4,1) = 1, S2(4,2) = 7, S2(4,3) = 6, S2(4,4) = 1, and B(4) = 15.
#
#
#  First terms:
#
#    I/J: 1    2    3    4    5    6    7    8
#
#    1    1    0    0    0    0    0    0    0
#    2    1    1    0    0    0    0    0    0
#    3    1    3    1    0    0    0    0    0
#    4    1    7    6    1    0    0    0    0
#    5    1   15   25   10    1    0    0    0
#    6    1   31   90   65   15    1    0    0
#    7    1   63  301  350  140   21    1    0
#    8    1  127  966 1701 1050  266   28    1
#
#  Recursion:
#
#    S2(I,1) = 1 for all I.
#    S2(I,I) = 1 for all I.
#    S2(I,J) = 0 if I < J.
#
#    S2(I,J) = J * S2(I-1,J) + S2(I-1,J-1)
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is lower triangular.
#
#    A is nonnegative.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the  matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  for i in range ( 1, n ):

    a[i,0] = 1.0

    for j in range ( 1, n ):
      a[i,j] = float ( j + 1 ) * a[i-1,j] + a[i-1,j-1]

  return a

def stirling_test ( ):

#*****************************************************************************80
#
## stirling_test() tests stirling_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'stirling_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  stirling_matrix() computes the STIRLING matrix.' )

  m = 5
  n = m

  a = stirling_matrix ( m, n )
 
  r8mat_print ( m, n, a, '  STIRLING matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'stirling_test' )
  print ( '  Normal end of execution.' )
  return

def sudoku_adj_matrix ( ):

#*****************************************************************************80
#
## sudoku_adj_matrix() returns the Sudoku adjacency matrix.
#
#  Discussion:
#
#    A Sudoko is a 9x9 array, subdivided into 9 3x3 blocks.
#
#    Two elements of the 9x9 array are adjacent if they lie in the same
#    row, column, or 3x3 subblock.
#
#    The eigenvalues of the Sudoku adjacency matrix are all integers.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(81,81), the matrix.
#
  import numpy as np

  a = np.zeros ( [ 81, 81 ] )

  for i in range ( 0, 81 ):
    rowi = i // 9
    coli = i % 9
    browi = rowi // 3
    bcoli = coli // 3
    for j in range ( 0, 81 ):
      rowj = j // 9
      colj = j % 9
      browj = rowj // 3
      bcolj = colj // 3
      if ( rowi == rowj or coli == colj or ( browi == browj and bcoli == bcolj ) ):
        a[i,j] = 1

  return a

def sudoku_adj_test ( ):

#*****************************************************************************80
#
## sudoku_adj_test() tests sudoku_adj_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2018
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import platform

  print ( '' )
  print ( 'sudoku_adj_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sudoku_adj_matrix() computes the sudoku_adj matrix.' )

  a = sudoku_adj_matrix ( )
 
  plt.spy ( a )
  plt.show ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sudoku_adj_test' )
  print ( '  Normal end of execution.' )
  return

def summation_matrix ( m, n ):

#*****************************************************************************80
#
## summation_matrix() returns the summation matrix.
#
#  Example:
#
#    M = 5, N = 5
#
#    1  0  0  0  0
#    1  1  0  0  0
#    1  1  1  0  0
#    1  1  1  1  0
#    1  1  1  1  1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is lower triangular.
#
#    A is a 0/1 matrix.
#
#    The vector Y = A * X contains the partial sums of the vector X.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is nonsingular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( j <= i ):
        a[i,j] = 1.0

  return a

def summation_condition ( n ):

#*****************************************************************************80
#
## summation_condition() returns the L1 condition of the SUMMATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real COND, the L1 condition.
#
  if ( n == 1 ):
    cond = 1.0
  else:
    cond = 2.0 * float ( n )

  return cond

def summation_determinant ( n ):

#*****************************************************************************80
#
## summation_determinant() returns the determinant of the SUMMATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 1.0

  return value

def summation_inverse ( n ):

#*****************************************************************************80
#
## summation_inverse() returns the inverse of the summation matrix.
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  0
#   -1  1  0  0  0
#    0 -1  1  0  0
#    0  0 -1  1  0
#    0  0  0 -1  1
#
#  Properties:
#
#    A is lower triangular.
#
#    A is lower bidiagonal.
#
#    Because A is bidiagonal, it has property A (bipartite).
#
#    A is Toeplitz: constant along diagonals.
#
#    A is nonsingular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is the inverse of the summation matrix.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 1.0
      elif ( i == j + 1 ):
        a[i,j] = -1.0

  return a

def summation_test ( ):

#*****************************************************************************80
#
## summation_test() tests summation_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'summation_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  summation_matrix() computes the SUMMATION matrix.' )

  m = 5
  n = 4
  a = summation_matrix ( m, n )
  r8mat_print ( m, n, a, '  SUMMATION matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'summation_test' )
  print ( '  Normal end of execution.' )
  return

def sweet1_matrix ( ):

#*****************************************************************************80
#
## sweet1_matrix() returns the SWEET1 matrix.
#
#  Example:
#
#    20.0  15.0   2.5   6.0   1.0  -2.0
#    15.0  20.0  15.0   2.5   6.0   1.0
#     2.5  15.0  20.0  15.0   2.5   6.0
#     6.0   2.5  15.0  20.0  15.0   2.5
#     1.0   6.0   2.5  15.0  20.0  15.0
#    -2.0   1.0   6.0   2.5  15.0  20.0
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Per Hansen, Tony Chan,
#    FORTRAN Subroutines for General Toeplitz Systems,
#    ACM Transactions on Mathematical Software,
#    Volume 18, Number 3, September 1992, pages 256-273.
#
#    Douglas Sweet,
#    The use of pivoting to improve the numerical performance of
#    Toeplitz solvers,
#    In "Advanced Algorithms and Architectures for Signal Processing",
#    Edited by J M Speiser,
#    Proceedings SPIE 696, 1986, pages 8-18.
#
#  Output:
#
#    real A(6,6), the matrix.
#
  import numpy as np

  n = 6

  value = np.array ( [ 20.0, 15.0, 2.5, 6.0, 1.0, -2.0 ] )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = value[abs(j-i)]

  return a

def sweet1_condition ( ):

#*****************************************************************************80
#
## sweet1_condition() returns the L1 condition of the SWEET1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the condition.
#
  a_norm = 61.0
  b_norm = 0.278145899201815
  value = a_norm * b_norm

  return value

def sweet1_determinant ( ):

#*****************************************************************************80
#
## sweet1_determinant() returns the determinant of the SWEET1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = - 2.0468186E+07

  return value

def sweet1_inverse ( ):

#*****************************************************************************80
#
## sweet1_inverse() returns the inverse of the SWEET1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(6,6), the matrix.
#
  import numpy as np

  a = np.array ( [ \
  [  0.073125159943338,  -0.029629732454063,  -0.020045010339460, \
     0.032364910109767,  -0.056244145182187,   0.052945000841794 ], \
  [ -0.029629732454063,   0.046796984109877,   0.019214941666057, \
    -0.056592264698005,   0.069667831091627,  -0.056244145182187 ], \
  [ -0.020045010339460,   0.019214941666057,   0.009031577102143, \
     0.035236537326757,  -0.056592264698005,   0.032364910109767 ], \
  [  0.032364910109767,  -0.056592264698005,   0.035236537326757, \
     0.009031577102143,   0.019214941666057,  -0.020045010339460 ], \
  [ -0.056244145182187,   0.069667831091627,  -0.056592264698005, \
     0.019214941666057,   0.046796984109877,  -0.029629732454063 ], \
  [  0.052945000841794,  -0.056244145182187,   0.032364910109767, \
    -0.020045010339460,  -0.029629732454063,   0.073125159943338 ] ] )

  return a

def sweet1_test ( ):

#*****************************************************************************80
#
## sweet1_test() tests sweet1_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sweet1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sweet1_matrix() computes the SWEET1 matrix.' )

  n = 6
  a = sweet1_matrix ( )
  r8mat_print ( n, n, a, '  SWEET1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'sweet1_test' )
  print ( '  Normal end of execution.' )
  return

def sweet2_matrix ( ):

#*****************************************************************************80
#
## sweet2_matrix() returns the SWEET2 matrix.
#
#  Example:
#
#     4.0  8.0  1.0  6.0  2.0  3.0
#     6.0  4.0  8.0  1.0  6.0  2.0
#    71/15 6.0  4.0  8.0  1.0  6.0
#     5.0 71/15 6.0  4.0  8.0  1.0
#     3.0  5.0 71/15 6.0  4.0  8.0
#     1.0  3.0  5.0 71/15 6.0  4.0
#
#  Properties:
#
#    A is Toeplitz: constant along diagonals.
#
#    A is generally not symmetric: A' /= A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Per Hansen, Tony Chan,
#    FORTRAN Subroutines for General Toeplitz Systems,
#    ACM Transactions on Mathematical Software,
#    Volume 18, Number 3, September 1992, pages 256-273.
#
#    Douglas Sweet,
#    The use of pivoting to improve the numerical performance of
#    Toeplitz solvers,
#    In "Advanced Algorithms and Architectures for Signal Processing",
#    Edited by J M Speiser,
#    Proceedings SPIE 696, 1986, pages 8-18.
#
#  Output:
#
#    real A(6,6), the matrix.
#
  import numpy as np

  n = 6

  v = np.array ( [ 1.0, 3.0, 5.0, 71.0 / 15.0, 6.0, 4.0, \
    8.0, 1.0, 6.0, 2.0, 3.0 ] )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = v[j-i+5]

  return a

def sweet2_condition ( ):

#*****************************************************************************80
#
## sweet2_condition() returns the L1 condition of the SWEET2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the condition.
#
  a_norm = 30.733333333333334
  b_norm = 1.601605164968818
  value = a_norm * b_norm

  return value

def sweet2_determinant ( ):

#*****************************************************************************80
#
## sweet2_determinant() returns the determinant of the SWEET2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = 9.562518834567902E+03

  return value

def sweet2_inverse ( ):

#*****************************************************************************80
#
## sweet2_inverse() returns the inverse of the SWEET2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(6,6), the matrix.
#
  import numpy as np

  a = np.array ( [ \
  [ -0.188192659589482,  -0.145188896312202,   0.063613055049687, \
     0.406962974759668,   0.271408731947181,  -0.526238847310597 ], \
  [  0.324411348442568,   0.213721529181228,  -0.131983821377206, \
    -0.344055452089408,  -0.168794206390780,   0.271408731947181 ], \
  [  0.038585525550130,   0.275974273184732,   0.137312031652403, \
    -0.366985595257679,  -0.344055452089408,   0.406962974759669 ], \
  [ -0.105091418281329,  -0.159756451255461,   0.216482246086901, \
     0.137312031652403,  -0.131983821377206,   0.063613055049687 ], \
  [ -0.043938024069266,  -0.157319070822594,  -0.159756451255461, \
     0.275974273184732,   0.213721529181228,  -0.145188896312202 ], \
  [ -0.054227038968746,  -0.043938024069265,  -0.105091418281329, \
     0.038585525550129,   0.324411348442568,  -0.188192659589482 ] ] )

  return a

def sweet2_test ( ):

#*****************************************************************************80
#
## sweet2_test() tests sweet2_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sweet2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sweet2_matrix() computes the SWEET2 matrix.' )

  n = 6
  a = sweet2_matrix ( )
  r8mat_print ( n, n, a, '  SWEET2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'sweet2_test' )
  print ( '  Normal end of execution.' )
  return

def sweet3_matrix ( ):

#*****************************************************************************80
#
## sweet3_matrix() returns the SWEET3 matrix.
#
#  Example:
#
#      8    4    1    6    2    3
#      4    8    4    1    6    2
#    -34    4    8    4    1    6
#      5  -34    4    8    4    1
#      3    5  -34    4    8    4
#      1    3    5  -34    4    8
#
#  Properties:
#
#    A is Toeplitz: constant along diagonals.
#
#    A is generally not symmetric: A' /= A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Per Hansen, Tony Chan,
#    FORTRAN Subroutines for General Toeplitz Systems,
#    ACM Transactions on Mathematical Software,
#    Volume 18, Number 3, September 1992, pages 256-273.
#
#    Douglas Sweet,
#    The use of pivoting to improve the numerical performance of
#    Toeplitz solvers,
#    In "Advanced Algorithms and Architectures for Signal Processing",
#    Edited by J M Speiser,
#    Proceedings SPIE 696, 1986, pages 8-18.
#
#  Output:
#
#    real A(6,6), the matrix.
#
  import numpy as np

  n = 6

  v = np.array ( [ 1.0, 3.0, 5.0, -34.0, 4.0, 8.0, 4.0, \
    1.0, 6.0, 2.0, 3.0 ] )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = v[j-i+5]

  return a

def sweet3_condition ( ):

#*****************************************************************************80
#
## sweet3_condition() returns the L1 condition of the SWEET3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the condition.
#
  a_norm = 58.0
  b_norm = 0.427215561206108
  value = a_norm * b_norm

  return value

def sweet3_determinant ( ):

#*****************************************************************************80
#
## sweet3_determinant() returns the determinant of the SWEET3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = - 5.4056067E+07

  return value

def sweet3_inverse ( ):

#*****************************************************************************80
#
## sweet3_inverse() returns the inverse of the SWEET3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(6,6), the matrix.
#
  import numpy as np

  a = np.array ( [ \
  [  0.041073816931594,  -0.007888550234334,  -0.020859268211281, \
     0.000304369165444,  -0.003979664299291,   0.004165693371662 ], \
  [  0.008091247186000,   0.017910145035154,   0.000156985153951, \
    -0.024742218112169,  -0.001114102511380,  -0.003979664299291 ], \
  [  0.006256245020564,   0.027534337635034,   0.003121055773444, \
     0.003970174152700,  -0.024742218112169,   0.000304369165444 ], \
  [  0.038877153234252,  -0.002789344626201,   0.008678729808441, \
     0.003121055773444,   0.000156985153951,  -0.020859268211281 ], \
  [ -0.119845197024785,   0.170102571465290,  -0.002789344626201, \
     0.027534337635034,   0.017910145035154,  -0.007888550234334 ], \
  [  0.213071901808913,  -0.119845197024785,   0.038877153234252, \
     0.006256245020564,   0.008091247186000,   0.041073816931594 ] ] )

  return a

def sweet3_test ( ):

#*****************************************************************************80
#
## sweet3_test() tests sweet3_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sweet3_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sweet3_matrix() computes the SWEET3 matrix.' )

  n = 6
  a = sweet3_matrix ( )
  r8mat_print ( n, n, a, '  SWEET3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'sweet3_test' )
  print ( '  Normal end of execution.' )
  return

def sweet4_matrix ( ):

#*****************************************************************************80
#
## sweet4_matrix() returns the SWEET4 matrix.
#
#  Example:
#
#    5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0  -2.0  -7.0   1.0  10.0 -15.0
#    1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0  -2.0  -7.0   1.0  10.0
#   -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0  -2.0  -7.0   1.0
#   12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0  -2.0  -7.0
#  -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0  -2.0
#   28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0  -5.0
#   -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8   3.0
#   -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6   5.8
#    2.0  -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0   5.6
#    1.0   2.0  -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0   2.0
#   -6.0   1.0   2.0  -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0   6.0
#    1.0  -6.0   1.0   2.0  -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0  -1.0
#   -0.5   1.0  -6.0   1.0   2.0  -1.0  -7.0  28.3 -19.6  12.7  -3.0   1.0   5.0
#
#  Properties:
#
#    A is Toeplitz: constant along diagonals.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Per Hansen, Tony Chan,
#    FORTRAN Subroutines for General Toeplitz Systems,
#    ACM Transactions on Mathematical Software,
#    Volume 18, Number 3, September 1992, pages 256-273.
#
#    Douglas Sweet,
#    The use of pivoting to improve the numerical performance of
#    Toeplitz solvers,
#    In "Advanced Algorithms and Architectures for Signal Processing",
#    Edited by J M Speiser,
#    Proceedings SPIE 696, 1986, pages 8-18.
#
#  Output:
#
#    real A(6,6), the matrix.
#
  import numpy as np

  n = 13

  v = np.array ( [ \
  -0.5,  1.0,  -6.0,     1.0,    2.0, \
  -1.0, -7.0,  28.361, -19.656, 12.755, \
  -3.0,  1.0,   5.0,    -1.0,    6.0, \
   2.0,  5.697, 5.850,   3.0,   -5.0, \
  -2.0, -7.0,   1.0,    10.0,  -15.0 ] )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = v[j-i+12]

  return a

def sweet4_condition ( ):

#*****************************************************************************80
#
## sweet4_condition() returns the L1 condition of the SWEET4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the condition.
#
  a_norm = 100.3190000000000
  b_norm = 0.510081684645161
  value = a_norm * b_norm

  return value

def sweet4_determinant ( ):

#*****************************************************************************80
#
## sweet4_determinant() returns the determinant of the SWEET4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the determinant.
#
  value = - 6.463481763930611E+16

  return value

def sweet4_inverse ( ):

#*****************************************************************************80
#
## sweet4_inverse() returns the inverse of the SWEET4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(13,13), the matrix.
#
  import numpy as np
#
#  Note that matrix entries are given by row.
#
  a = np.array ( [ \
  [ -0.006395453515049,   0.030690839549686, \
    -0.002288997065175,  -0.008539260151857, \
    -0.001015137652004,   0.040513470913244, \
     0.017598472282428,  -0.008312925397734, \
    -0.015546543686421,  -0.010969455314610, \
    -0.017014452081345,  -0.017669033095207, \
    -0.013805699365025 ], \
  [  0.004338135763774,   0.039852868508471, \
    -0.006409462970417,  -0.010789166315387, \
     0.023605183638394,   0.023524498024753, \
     0.032221111978773,   0.010175588114759, \
    -0.018129776994110,  -0.028500341074603, \
    -0.029318921760199,  -0.030615698849391, \
    -0.017669033095207 ], \
  [  0.011852844358462,   0.033292080046396, \
    -0.005374341111703,  -0.008875487063420, \
     0.031350558988152,   0.015098401236510, \
    -0.004426214105193,   0.030910853378811, \
     0.012927937004693,  -0.023901509668313, \
    -0.035222171390576,  -0.029318921760199, \
    -0.017014452081345 ], \
  [  0.013846756886370,   0.028058421670586, \
    -0.009388803334490,  -0.004500416153857, \
     0.032089285374445,   0.007746385727172, \
    -0.018511813509106,  -0.002525445590655, \
     0.039475608232317,   0.011543138436698, \
    -0.023901509668313,  -0.028500341074603, \
    -0.010969455314610 ], \
  [  0.009447720973799,   0.021796805754657, \
     0.000727759422194,  -0.008130365160809, \
     0.021992767390463,   0.013573971521042, \
    -0.015354921685074,  -0.016609776210723, \
     0.004261697864111,   0.039475608232316, \
     0.012927937004693,  -0.018129776994110, \
    -0.015546543686421 ], \
  [  0.009432787993907,   0.039704365747118, \
    -0.018354056201609,  -0.002772215599655, \
     0.028789202755591,   0.020818744033636, \
    -0.008277808905384,  -0.017802710611741, \
    -0.016609776210723,  -0.002525445590655, \
     0.030910853378811,   0.010175588114759, \
    -0.008312925397734 ], \
  [  0.006050784346575,   0.020779138484695, \
     0.018595613535238,  -0.018881036665831, \
     0.017128957468121,   0.021782629702447, \
     0.006363468918819,  -0.008277808905384, \
    -0.015354921685074,  -0.018511813509106, \
    -0.004426214105193,   0.032221111978773, \
     0.017598472282428 ], \
  [ -0.001688517566864,  -0.071337491505107, \
     0.069446707802933,   0.034560078451674, \
    -0.059246627902032,  -0.038486648845696, \
     0.021782629702447,   0.020818744033636, \
     0.013573971521042,   0.007746385727172, \
     0.015098401236510,   0.023524498024753, \
     0.040513470913244 ], \
  [ -0.024098383394697,  -0.082853404494777, \
     0.033466389466084,   0.079212314240954, \
    -0.061573703805162,  -0.059246627902032, \
     0.017128957468121,   0.028789202755591, \
     0.021992767390463,   0.032089285374445, \
     0.031350558988152,   0.023605183638394, \
    -0.001015137652004 ], \
  [ -0.014571843537603,   0.050761162107706, \
    -0.090910979018549,   0.012959017667649, \
     0.079212314240954,   0.034560078451674, \
    -0.018881036665831,  -0.002772215599655, \
    -0.008130365160809,  -0.004500416153857, \
    -0.008875487063420,  -0.010789166315387, \
    -0.008539260151857 ], \
  [  0.006620954487991,  -0.004862149070269, \
     0.029222791279654,  -0.090910979018549, \
     0.033466389466084,   0.069446707802933, \
     0.018595613535238,  -0.018354056201609, \
     0.000727759422194,  -0.009388803334490, \
    -0.005374341111703,  -0.006409462970417, \
    -0.002288997065175 ], \
  [  0.017905883190490,  -0.068187074515203, \
    -0.004862149070269,   0.050761162107706, \
    -0.082853404494777,  -0.071337491505107, \
     0.020779138484695,   0.039704365747118, \
     0.021796805754657,   0.028058421670586, \
     0.033292080046396,   0.039852868508471, \
     0.030690839549686 ], \
  [ -0.031068329896258,   0.017905883190490, \
     0.006620954487991,  -0.014571843537603, \
    -0.024098383394697,  -0.001688517566864, \
     0.006050784346575,   0.009432787993907, \
     0.009447720973799,   0.013846756886370, \
     0.011852844358462,   0.004338135763774, \
    -0.006395453515049 ] ] )

  return a

def sweet4_test ( ):

#*****************************************************************************80
#
## sweet4_test() tests sweet4_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sweet4_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sweet4_matrix() computes the SWEET4 matrix.' )

  n = 13
  a = sweet4_matrix ( )
  r8mat_print ( n, n, a, '  SWEET4 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'sweet4_test' )
  print ( '  Normal end of execution.' )
  return

def sylvester_kac_matrix ( n ):

#*****************************************************************************80
#
## sylvester_kac_matrix() returns the SYLVESTER_KAC matrix.
#
#  Formula:
#
#    If J = I - 1
#      A(I,J) = N + 1 - I
#    If J = I + 1
#      A(I,J) = I
#
#  Example:
#
#    N = 5,
#
#    0 1 0 0 0
#    4 0 2 0 0
#    0 3 0 3 0
#    0 0 2 0 4
#    0 0 0 1 0
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    If N is odd, the eigenvalues are:
#      -(N-1), -(N-3), ..., -2, 0, 2, ... (N-3), (N-1).
#
#    If N is even, the eigenvalues are:
#      -(N-1), -(N-3), ..., -1, +1, ..., (N-3), (N-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Clement,
#    A class of triple-diagonal matrices for test purposes,
#    SIAM Review,
#    Volume 1, 1959, pages 50-52.
#
#  Input:
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n - 1 ):
    a[i,i+1] = float (     i + 1 )
    a[i+1,i] = float ( n - i - 1 )

  return a

def sylvester_kac_determinant ( n ):

#*****************************************************************************80
#
## sylvester_kac_determinant() returns the determinant of the SYLVESTER_KAC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real VALUE, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    value = 0.0
  else:
    value = 1.0
    for i in range ( - n + 1, n + 1, 2 ):
      value = value * float ( i )

  return value

def sylvester_kac_eigen_right ( n ):

#*****************************************************************************80
#
## sylvester_kac_eigen_right(): right eigenvectors of the SYLVESTER_KAC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real V(N,N), the right eigenvectors.
#
  import numpy as np

  b = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    b[i] = float ( i + 1 )

  c = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    c[i] = float ( n - 1 - i )

  v = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):

    lam = float ( - n + 1 + 2 * j )

    a = np.zeros ( n )
    a[0] = 1.0
    a[1] = - lam
    for i in range ( 2, n ):
      a[i] = - lam * a[i-1] - b[i-2] * c[i-2] * a[i-2]

    bot = 1.0
    v[0,j] = 1.0
    for i in range ( 1, n ):
      bot = bot * b[i-1]
      v[i,j] = r8_mop ( i ) * a[i] / bot

  return v

def sylvester_kac_eigenvalues ( n ):

#*****************************************************************************80
#
## sylvester_kac_eigenvalues() returns the eigenvalues of the SYLVESTER_KAC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    lam[i] = float ( - n + 1 + 2 * i )

  return lam

def sylvester_kac_inverse ( n ):

#*****************************************************************************80
#
## sylvester_kac_inverse() returns the inverse of the SYLVESTER_KAC matrix.
#
#  Example:
#
#    N = 6:
#
#      0     1/5    0  -2/15  0   8/15
#      1      0     0    0    0    0
#      0      0     0   1/3   0  -4/3
#    -4/3     0    1/3   0    0    0
#      0      0     0    0    0    1
#     8/15    0   -2/15  0   1/5   0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  if ( ( n % 2 ) == 1 ):
    print ( '' )
    print ( 'sylvester_kac_inverse - Fatal error!' )
    print ( '  The matrix is singular for odd N.' )
    raise Exception ( 'sylvester_kac_inverse - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):

      for j in range ( i, n - 1, 2 ):

        if ( j == i ):
          prod1 = 1.0 / float ( n - 1 - j )
          prod2 = 1.0 / float (     1 + j )
        else:
          prod1 = - prod1 * float (     j ) / float ( n - 1 - j )
          prod2 = - prod2 * float ( n - j ) / float (     1 + j )

        a[i,j+1] = prod1
        a[j+1,i] = prod2

  return a

def sylvester_kac_test ( ):

#*****************************************************************************80
#
## sylvester_kac_test() tests sylvester_kac_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sylvester_kac_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sylvester_kas_matrix() computes the SYLVESTER_KAC matrix.' )

  m = 5
  n = m
  a = sylvester_kac_matrix ( n )
  r8mat_print ( m, n, a, '  SYLVESTER_KAC matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'sylvester_kac_test' )
  print ( '  Normal end of execution.' )
  return

def symmetric_random_matrix ( n, d, key ):

#*****************************************************************************80
#
## symmetric_random_matrix() returns the symmetric_random matrix.
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    The eigenvalues of A will be real.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real D(N), the desired eigenvalues for the matrix.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np
#
#  Get a random orthogonal matrix Q.
#
  q = orthogonal_random_matrix ( n, key )
#
#  Set A = Q * Lambda * Q'.
#
  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * d[k] * q[j,k]

  return a

def symmetric_random_determinant ( n, d, key ):

#*****************************************************************************80
#
## symmetric_random_determinant(): determinant of the symmetric_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real D(N), the desired eigenvalues for the matrix.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real VALUE, the determinant.
#
  import numpy as np

  value = np.prod ( d )

  return value

def symmetric_random_eigen_left ( n, d, key ):

#*****************************************************************************80
#
## symmetric_random_eigen_left(): left eigenvectors for the symmetric_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real D(N), the desired eigenvalues for the matrix.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real V(N,N), the vectors.
#

#
#  Get a random orthogonal matrix Q.
#
  x = orthogonal_random_matrix ( n, key )
#
#  Transpose.
#
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      t      = x[i,j]
      x[i,j] = x[j,i]
      x[j,i] = t

  return x

def symmetric_random_eigen_right ( n, d, key ):

#*****************************************************************************80
#
## symmetric_random_eigen_right(): right eigenvectors for the symmetric_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real D(N), the desired eigenvalues for the matrix.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real V(N,N), the vectors.
#

#
#  Get a random orthogonal matrix Q.
#
  x = orthogonal_random_matrix ( n, key )

  return x

def symmetric_random_eigenvalues ( n, d, key ):

#*****************************************************************************80
#
## symmetric_random_eigenvalues(): eigenvalues for the symmetric_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real D(N), the desired eigenvalues for the matrix.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.copy ( d )

  return lam

def symmetric_random_inverse ( n, d, key ):

#*****************************************************************************80
#
## symmetric_random_inverse(): inverse of the symmetric_random matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real D(N), the desired eigenvalues for the matrix.
#
#    integer KEY, a positive integer that selects the data.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np
#
#  Get a random orthogonal matrix Q.
#
  q = orthogonal_random_matrix ( n, key )
#
#  Set A = Q * 1/Lambda * Q'.
#
  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * ( 1.0 / d[k] ) * q[j,k]

  return a

def symmetric_random_test ( ):

#*****************************************************************************80
#
## symmetric_random_test() tests symmetric_random_matrix().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'symmetric_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  symmetric_random_matrix() computes the symmetric_random matrix.' )

  n = 3
  r8_lo = -5.0
  r8_hi = +5.0
  d = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )

  key = 123456789
  a = symmetric_random_matrix ( n, d, key )
  r8mat_print ( n, n, a, '  symmetric_random matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'symmetric_random_test' )
  print ( '  Normal end of execution.' )
  return

def test_condition ( ):

#*****************************************************************************80
#
## test_condition() tests the L1 condition number computations.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_condition()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Compute the L1 condition number of an example of each' )
  print ( '  test matrix' )
  print ( '' )
  print ( '  Title                    N            COND            COND' )
  print ( '' )
#
#  aegerter
#
  title = 'aegerter'
  n = 5
  cond1 = aegerter_condition ( n )

  a = aegerter_matrix ( n )
  b = aegerter_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  bab
#
  title = 'bab'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  beta = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = bab_condition ( n, alpha, beta )

  a = bab_matrix ( n, alpha, beta )
  b = bab_inverse ( n, alpha, beta )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  bauer
#
  title = 'bauer'
  n = 6
  cond1 = bauer_condition ( )

  a = bauer_matrix ( )
  b = bauer_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  bis
#
  title = 'bis'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  beta = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = bis_condition ( alpha, beta, n )

  a = bis_matrix ( alpha, beta, n, n )
  b = bis_inverse ( alpha, beta, n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  biw
#
  title = 'biw'
  n = 5
  cond1 = biw_condition ( n )

  a = biw_matrix ( n )
  b = biw_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  bodewig
#
  title = 'bodewig'
  n = 4
  cond1 = bodewig_condition ( )

  a = bodewig_matrix ( )
  b = bodewig_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  boothroyd
#
  title = 'boothroyd'
  n = 5
  cond1 = boothroyd_condition ( n )

  a = boothroyd_matrix ( n )
  b = boothroyd_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  combin
#
  title = 'combin'
  n = 3
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  beta = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = combin_condition ( alpha, beta, n )

  a = combin_matrix ( alpha, beta, n )
  b = combin_inverse ( alpha, beta, n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  companion
#
  title = 'companion'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )
  cond1 = companion_condition ( n, x )

  a = companion_matrix ( n, x )
  b = companion_inverse ( n, x )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  conex1
#
  title = 'conex1'
  n = 4
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = conex1_condition ( alpha )

  a = conex1_matrix ( alpha )
  b = conex1_inverse ( alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  conex2
#
  title = 'conex2'
  n = 3
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = conex2_condition ( alpha )

  a = conex2_matrix ( alpha )
  b = conex2_inverse ( alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  conex3
#
  title = 'conex3'
  n = 5
  cond1 = conex3_condition ( n )

  a = conex3_matrix ( n )
  b = conex3_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  conex4
#
  title = 'conex4'
  n = 4
  cond1 = conex4_condition ( )

  a = conex4_matrix ( )
  b = conex4_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  daub2
#
  title = 'daub2'
  n = 4
  cond1 = daub2_condition ( n )

  a = daub2_matrix ( n )
  b = daub2_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  daub4
#
  title = 'daub4'
  n = 8
  cond1 = daub4_condition ( n )

  a = daub4_matrix ( n )
  b = daub4_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  daub6
#
  title = 'daub6'
  n = 12
  cond1 = daub6_condition ( n )

  a = daub6_matrix ( n )
  b = daub6_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  daub8
#
  title = 'daub8'
  n = 16
  cond1 = daub8_condition ( n )

  a = daub8_matrix ( n )
  b = daub8_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  daub10
#
  title = 'daub10'
  n = 20
  cond1 = daub10_condition ( n )

  a = daub10_matrix ( n )
  b = daub10_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  daub12
#
  title = 'daub12'
  n = 24
  cond1 = daub12_condition ( n )

  a = daub12_matrix ( n )
  b = daub12_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  diagonal
#
  title = 'diagonal'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )
  cond1 = diagonal_condition ( n, x )

  a = diagonal_matrix ( n, n, x )
  b = diagonal_inverse ( n, x )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  dif2
#
  title = 'dif2'
  n = 5
  cond1 = dif2_condition ( n )

  a = dif2_matrix ( n, n )
  b = dif2_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  downshift
#
  title = 'downshift'
  n = 5
  cond1 = downshift_condition ( n )

  a = downshift_matrix ( n )
  b = downshift_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  exchange
#
  title = 'exchange'
  n = 5
  cond1 = exchange_condition ( n )

  a = exchange_matrix ( n, n )
  b = exchange_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  fibonacci2
#
  title = 'fibonacci2'
  n = 5
  cond1 = fibonacci2_condition ( n )

  a = fibonacci2_matrix ( n )
  b = fibonacci2_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  gfpp
#
  title = 'gfpp'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = gfpp_condition ( n, alpha )

  a = gfpp_matrix ( n, alpha )
  b = gfpp_inverse ( n, alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  givens
#
  title = 'givens'
  n = 5
  cond1 = givens_condition ( n )

  a = givens_matrix ( n, n )
  b = givens_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  hankel_n
#
  title = 'hankel_n'
  n = 5
  cond1 = hankel_n_condition ( n )

  a = hankel_n_matrix ( n )
  b = hankel_n_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  harman
#
  title = 'harman'
  n = 8
  cond1 = harman_condition ( )

  a = harman_matrix ( )
  b = harman_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  hartley
#
  title = 'hartley'
  n = 5
  cond1 = hartley_condition ( n )

  a = hartley_matrix ( n )
  b = hartley_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  identity
#
  title = 'identity'
  n = 5
  cond1 = identity_condition ( n )

  a = identity_matrix ( n, n )
  b = identity_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  ill3
#
  title = 'ill3'
  n = 3
  cond1 = ill3_condition ( )

  a = ill3_matrix ( )
  b = ill3_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  jordan
#
  title = 'jordan'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = jordan_condition ( n, alpha )

  a = jordan_matrix ( n, n, alpha )
  b = jordan_inverse ( n, alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  kershaw
#
  title = 'kershaw'
  n = 4
  cond1 = kershaw_condition ( )

  a = kershaw_matrix ( )
  b = kershaw_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  lietzke
#
  title = 'lietzke'
  n = 5
  cond1 = lietzke_condition ( n )

  a = lietzke_matrix ( n )
  b = lietzke_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  maxij
#
  title = 'maxij'
  n = 5
  cond1 = maxij_condition ( n )

  a = maxij_matrix ( n, n )
  b = maxij_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  minij
#
  title = 'minij'
  n = 5
  cond1 = minij_condition ( n )

  a = minij_matrix ( n, n )
  b = minij_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  orthogonal_symmetric
#
  title = 'orthogonal_symmetric'
  n = 5
  cond1 = orthogonal_symmetric_condition ( n )

  a = orthogonal_symmetric_matrix ( n )
  b = orthogonal_symmetric_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  oto
#
  title = 'oto'
  n = 5
  cond1 = oto_condition ( n )

  a = oto_matrix ( n, n )
  b = oto_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  pascal1
#
  title = 'pascal1'
  n = 5
  cond1 = pascal1_condition ( n )

  a = pascal1_matrix ( n )
  b = pascal1_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  pascal3
#
  title = 'pascal3'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = pascal3_condition ( n, alpha )

  a = pascal3_matrix ( n, alpha )
  b = pascal3_inverse ( n, alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  pei
#
  title = 'pei'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = pei_condition ( alpha, n )

  a = pei_matrix ( alpha, n )
  b = pei_inverse ( alpha, n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  rodman
#
  title = 'rodman'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = rodman_condition ( n, alpha )

  a = rodman_matrix ( n, n, alpha )
  b = rodman_inverse ( n, alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  rutis1
#
  title = 'rutis1'
  n = 4
  cond1 = rutis1_condition ( )

  a = rutis1_matrix ( )
  b = rutis1_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  rutis2
#
  title = 'rutis2'
  n = 4
  cond1 = rutis2_condition ( )

  a = rutis2_matrix ( )
  b = rutis2_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  rutis3
#
  title = 'rutis3'
  n = 4
  cond1 = rutis3_condition ( )

  a = rutis3_matrix ( )
  b = rutis3_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  rutis5
#
  title = 'rutis5'
  n = 4
  cond1 = rutis5_condition ( )

  a = rutis5_matrix ( )
  b = rutis5_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  summation
#
  title = 'summation'
  n = 5
  cond1 = summation_condition ( n )

  a = summation_matrix ( n, n )
  b = summation_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  sweet1
#
  title = 'sweet1'
  n = 6
  cond1 = sweet1_condition ( )

  a = sweet1_matrix ( )
  b = sweet1_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  sweet2
#
  title = 'sweet2'
  n = 6
  cond1 = sweet2_condition ( )

  a = sweet2_matrix ( )
  b = sweet2_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  sweet3
#
  title = 'sweet3'
  n = 6
  cond1 = sweet3_condition ( )

  a = sweet3_matrix ( )
  b = sweet3_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  sweet4
#
  title = 'sweet4'
  n = 13
  cond1 = sweet4_condition ( )

  a = sweet4_matrix ( )
  b = sweet4_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  tri_upper
#
  title = 'tri_upper'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  cond1 = tri_upper_condition ( alpha, n )

  a = tri_upper_matrix ( alpha, n )
  b = tri_upper_inverse ( alpha, n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  upshift
#
  title = 'upshift'
  n = 5
  cond1 = upshift_condition ( n )

  a = upshift_matrix ( n )
  b = upshift_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  wilk03
#
  title = 'wilk03'
  n = 3
  cond1 = wilk03_condition ( )

  a = wilk03_matrix ( )
  b = wilk03_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  wilk04
#
  title = 'wilk04'
  n = 4
  cond1 = wilk04_condition ( )

  a = wilk04_matrix ( )
  b = wilk04_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  wilk05
#
  title = 'wilk05'
  n = 5
  cond1 = wilk05_condition ( )

  a = wilk05_matrix ( )
  b = wilk05_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  wilson
#
  title = 'wilson'
  n = 4
  cond1 = wilson_condition ( )

  a = wilson_matrix ( )
  b = wilson_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print ( '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_condition():' )
  print ( '  Normal end of execution.' )
  return

def test_determinant ( ):

#*****************************************************************************80
#
## test_determinant() tests the determinant computations.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_determinant():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Compute the determinants of an example of each' )
  print ( '  test matrix compare with the determinant routine,' )
  print ( '  if available.  Print the matrix Frobenius norm' )
  print ( '  for an estimate of magnitude.' )
  print ( '' )
  print ( '  Title                    N      Determ          Determ          ||A||' )
  print ( '' )
#
#  a123
#
  title = 'a123'
  n = 3
  a = a123_matrix ( )
  determ1 = a123_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius ) )
#
#  aegerter
#
  title = 'aegerter'
  n = 5
  a = aegerter_matrix ( n )
  determ1 = aegerter_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius ) )
#
#  ANTICIRCULANT
#
  title = 'ANTICIRCULANT'
  for n in range ( 3, 6 ):
    r8_lo = -5.0
    r8_hi = +5.0
    x = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( n )
# a = anticirculant_matrix ( n, n, x )
# determ1 = anticirculant_determinant ( n, x )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print ( '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius ) )
#
#  ANTIHADAMARD
#
  title = 'ANTIHADAMARD'
  n = 5
# a = antihadamard_matrix ( n )
# determ1 = antihadamard_determinant ( n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print ( '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius ) )
#
#  antisymmetric_random
#
  title = 'antisymmetric_random'
  for n in range ( 5, 7 ):
    key = 123456789
    a = antisymmetric_random_matrix ( n, key )
    determ1 = antisymmetric_random_determinant ( n, key )
    determ2 = np.linalg.det ( a )
    norm_frobenius = r8mat_norm_fro ( n, n, a )
    print ( '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
      title, n, determ1, determ2, norm_frobenius ) )
#
#  bab
#
  title = 'bab'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  beta = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
  a = bab_matrix ( n, alpha, beta )
  determ1 = bab_determinant ( n, alpha, beta )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius ) )
#
#  bauer
#
  title = 'bauer'
  n = 6
  a = bauer_matrix ( )
  determ1 = bauer_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius ) )
#
#  bernstein
#
  title = 'bernstein'
  n = 5
  a = bernstein_matrix ( n )
  determ1 = bernstein_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius ) )
#
#  bimarkov_random
#
  title = 'bimarkov_random'
  n = 5
  key = 123456789
  a = bimarkov_random_matrix ( n, key )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d                  %14g  %10.2g' % ( \
