#! /usr/bin/env python3
#
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

def i4vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_transpose_print() prints an I4VEC "transposed".
#
#  Example:
#
#    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
#    TITLE = 'My vector:  '
#
#    My vector:
#
#       1    2    3    4    5
#       6    7    8    9   10
#      11
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  if ( 0 < n ):
    for i in range ( 0, n ):
      print ( '%8d' % ( a[i] ), end = '' )
      if ( ( i + 1 ) % 10 == 0 or i == n - 1 ):
        print ( '' )
  else:
    print ( '  (empty vector)' )

  return

def monomial_value ( m, n, e, x ):

#*****************************************************************************80
#
## monomial_value() evaluates a monomial.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      product ( 1 <= i <= m ) x(i)^e(i)
#
#    The combination 0.0^0, if encountered, is treated as 1.0.
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
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of evaluation points.
#
#    integer E(M), the exponents.
#
#    real X(M,N), the point coordinates.
#
#  Output:
#
#    real V(N), the monomial values.
#
  import numpy as np

  v = np.ones ( n )

  for i in range ( 0, m ):
    if ( 0 != e[i] ):
      for j in range ( 0, n ):
        v[j] = v[j] * x[i,j] ** e[i]

  return v

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

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_transpose_print() prints an R8MAT, transposed.
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
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_transpose_print_some() prints a portion of an R8MAT, transposed.
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

def wedge01_monomial_integral ( e ):

#*****************************************************************************80
#
## wedge01_monomial_integral(): integral of a monomial in the unit wedge in 3D.
#
#  Discussion:
#
#    This routine returns the integral of
#
#      product ( 1 <= I <= 3 ) X(I)^E(I)
#
#    over the unit wedge.
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1
#      -1 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Arthur Stroud,
#    Approximate Calculation of Multiple Integrals,
#    Prentice Hall, 1971,
#    ISBN: 0130438936,
#    LC: QA311.S85.
#
#  Input:
#
#    integer E(3), the exponents.
#
#  Output:
#
#    real VALUE, the integral of the monomial.
#
  value = 1.0

  k = e[0]

  for i in range ( 1, e[1] + 1 ):
    k = k + 1
    value = value * float ( i ) / float ( k )

  k = k + 1
  value = value / float ( k )

  k = k + 1
  value = value / float ( k )
#
#  Now account for integration in Z.
#
  if ( e[2] == - 1 ):
    print ( '' )
    print ( 'WEDGE01_MONOMIAL_INTEGRAL - Fatal error!' )
    print ( '  E(3) = -1 is not a legal input.' )
    raise Exception ( 'WEDGE01_MONOMIAL_INTEGRAL - Fatal error!' )
  elif ( ( e[2] % 2 ) == 1 ):
    value = 0.0
  else:
    value = value * 2.0 / float ( e[2] + 1 )

  return value

def wedge01_monomial_integral_test ( ):

#*****************************************************************************80
#
## wedge01_monomial_integral_test() tests wedge01_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 3
  n = 500000
  e_max = 6

  print ( '' )
  print ( 'WEDGE01_MONOMIAL_INTEGRAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEDGE01_MONOMIAL_INTEGRAL computes the integral of a monomial' )
  print ( '  over the interior of the unit wedge in 3D.' )
  print ( '  Compare with a Monte Carlo estimate.' )

  x = wedge01_sample ( n )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
  print ( '' )
  print ( '   E1  E2  E3     MC-Estimate      Exact           Error' )
  print ( '' )
#
#  Check all monomials up to total degree E_MAX.
#
  e = np.zeros ( 3, dtype = np.int32 )

  for e3 in range ( 0, e_max + 1 ):
    e[2] = e3
    for e2 in range ( 1, e_max - e3 + 1 ):
      e[1] = e2
      for e1 in range ( 0, e_max - e3 - e2 + 1 ):
        e[0] = e1

        value = monomial_value ( m, n, e, x )

        q = wedge01_volume ( ) * np.sum ( value ) / float ( n )
        exact = wedge01_monomial_integral ( e )
        error = abs ( q - exact )

        print ( '  %2d  %2d  %2d  %14.6g  %14.6g  %14.6g' \
          % ( e[0], e[1], e[2], q, exact, error ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'WEDGE01_MONOMIAL_INTEGRAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def wedge01_monte_carlo_test ( ):

#*****************************************************************************80
#
## wedge01_monte_carlo_test() uses wedge01_sample() with an increasing number of points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 3

  e_test = np.array ( [ \
    [ 0, 0, 0 ], \
    [ 1, 0, 0 ], \
    [ 0, 1, 0 ], \
    [ 0, 0, 1 ], \
    [ 2, 0, 0 ], \
    [ 1, 1, 0 ], \
    [ 0, 0, 2 ], \
    [ 3, 0, 0 ] ] )

  print ( '' )
  print ( 'WEDGE01_MONTE_CARLO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use WEDGE01_SAMPLE for a Monte Carlo estimate of an' )
  print ( '  integral over the interior of the unit wedge in 3D.' )
  print ( '' )
  print ( '         N        1               X               Y               Z                X^2            XY              Z^2            X^3' )
  print ( '' )

  n = 1

  e = np.zeros ( 3, dtype = np.int32 )

  while ( n <= 65536 ):

    x = wedge01_sample ( n )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 8 ):

      e[0:m] = e_test[j,0:m]

      value = monomial_value ( m, n, e, x )

      result = wedge01_volume ( ) * np.sum ( value[0:n] ) / float ( n )
      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )

  for j in range ( 0, 8 ):

    e[0:m] = e_test[j,0:m]
    result = wedge01_monomial_integral ( e )
    print ( '  %14.6g' % ( result ), end = '' )

  print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'WEDGE01_MONTE_CARLO_TEST' )
  print ( '  Normal end of execution.' )
  return

def wedge01_sample ( n ):

#*****************************************************************************80
#
## wedge01_sample() samples points uniformly from the unit wedge in 3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity 
#    of Queueing Networks,
#    Krieger, 1992,
#    ISBN: 0894647644,
#    LC: QA298.R79.
#
#  Input:
#
#    integer N, the number of points.
#
#  Output:
#
#    real X(3,N), the points.
#
  import numpy as np

  m = 3

  x = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    e = np.random.rand ( m + 1 )

    el = np.zeros ( m )

    el_sum = 0.0
    for i in range ( 0, m ):
      el[i] = - np.log ( e[i] )
      el_sum = el_sum + el[i]

    x[0,j] = el[0] / el_sum
    x[1,j] = el[1] / el_sum
    x[2,j] = 2.0 * e[3] - 1.0

  return x

def wedge01_sample_test ( ):

#*****************************************************************************80
#
## wedge01_sample_test() tests wedge01_sample().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'WEDGE01_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEDGE01_SAMPLE samples the unit wedge.' )

  m = 3
  n = 10

  x = wedge01_sample ( n )

  r8mat_transpose_print ( m, n, x, '  Sample points in the unit wedge.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'WEDGE01_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def wedge01_volume ( ):

#*****************************************************************************80
#
## wedge01_volume() returns the volume of the unit wedge in 3D.
#
#  Discussion:
#
#    The unit wedge is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1
#      -1 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the volume of the unit wedge.
#
  value = 1.0

  return value

def wedge01_volume_test ( ) :

#*****************************************************************************80
#
## wedge01_volume_test() tests wedge01_volume().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'WEDGE01_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEDGE01_VOLUME returns the volume of the unit wedge.' )

  value = wedge01_volume ( )

  print ( '' )
  print ( '  WEDGE01_VOLUME() = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'WEDGE01_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

def wedge_monte_carlo_test ( ):

#*****************************************************************************80
#
## wedge_monte_carlo_test() tests wedge_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'WEDGE_MONTE_CARLO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test WEDGE_MONTE_CARLO()' )

  wedge01_monomial_integral_test ( )
  wedge01_monte_carlo_test ( )
  wedge01_sample_test ( )
  wedge01_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'WEDGE_MONTE_CARLO_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  wedge_monte_carlo_test ( )
  timestamp ( )

