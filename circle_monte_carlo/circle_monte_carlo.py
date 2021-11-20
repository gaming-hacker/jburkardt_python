#! /usr/bin/env python3
#
def circle01_length ( ):

#*****************************************************************************80
#
## circle01_length(): length of the circumference of the unit circle in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the length.
#
  import numpy as np

  r = 1.0
  value = 2.0 * np.pi * r

  return value

def circle01_length_test ( ) :

#*****************************************************************************80
#
## circle01_length() tests circle01_length().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'circle01_length_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  circle01_length() returns the length of the unit circle.' )

  value = circle01_length ( )

  print ( '' )
  print ( '  circle01_length() = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'circle01_length_test():' )
  print ( '  Normal end of execution.' )
  return

def circle01_monomial_integral ( e ):

#*****************************************************************************80
#
## circle01_monomial_integral(): integrals on circumference of unit circle in 2D.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 = 1.
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Academic Press, 1984, page 263.
#
#  Input:
#
#    integer E(2), the exponents of X and Y in the 
#    monomial.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  from scipy.special import gamma

  if ( e[0] < 0 or e[1] < 0 ):
    print ( '' )
    print ( 'circle01_monomial_integral - Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'circle01_monomial_integral - Fatal error!' )

  if ( ( ( e[0] % 2 ) == 1 ) or ( ( e[1] % 2 ) == 1 ) ):

    integral = 0.0

  else:

    integral = 2.0

    for i in range ( 0, 2 ):
      integral = integral * gamma ( 0.5 * float ( e[i] + 1 ) )

    integral = integral / gamma ( 0.5 * float ( e[0] + e[1] + 2 ) )

  return integral

def circle01_monomial_integral_test ( ):

#*****************************************************************************80
#
## circle01_monomial_integral_test() tests circle01_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 2
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'circle01_monomial_integral_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  circle01_monomial_integral() returns the value of the' )
  print ( '  integral of a monomial over the unit circle in 2D.' )
  print ( '  Compare with a Monte Carlo estimate.' )
#
#  Get sample points.
#
  x = circle01_sample_random ( n )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose X, Y exponents.
#
  print ( '' )
  print ( '  If any exponent is odd, the integral is zero.' )
  print ( '  We restrict this test to randomly chosen even exponents.' )
  print ( '' )
  print ( '  Ex  Ey     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = np.random.random_integers ( 0, 5, size = m )

    e[0] = e[0] * 2
    e[1] = e[1] * 2

    value = monomial_value ( m, n, e, x )

    result = circle01_length ( ) * np.sum ( value ) / float ( n )
    exact = circle01_monomial_integral ( e )
    error = abs ( result - exact )

    print ( '  %2d  %2d  %14.6g  %14.6g  %10.2g' \
      % ( e[0], e[1], result, exact, error ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'circle01_monomial_integral_test()' )
  print ( '  Normal end of execution.' )
  return

def circle01_sample_ergodic ( n, angle ):

#*****************************************************************************80
#
## circle01_sample_ergodic() samples points on the circumference of the unit circle in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 June 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real ANGLE, an angle between 0 and 2 PI.
#
#  Output:
#
#    real X(2,N), the points.
#
#    real ANGLE, an updated angle.
#
  import numpy as np

  r = 1.0
  c = np.zeros ( 2 )

  golden_ratio = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0

  golden_angle = 2.0 * np.pi / golden_ratio ** 2

  x = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
    x[0,j] = c[0] + r * np.cos ( angle )
    x[1,j] = c[1] + r * np.sin ( angle )
    angle = np.mod ( angle + golden_angle, 2.0 * np.pi )

  return x, angle

def circle01_sample_ergodic_test ( ):

#*****************************************************************************80
#
## circle01_sample_ergodic_test() tests circle01_sample_ergodic().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 June 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  import numpy as np

  e = np.zeros ( 2 )
  e_test = np.array ( [ \
    [ 0, 0 ], \
    [ 2, 0 ], \
    [ 0, 2 ], \
    [ 4, 0 ], \
    [ 2, 2 ], \
    [ 0, 4 ], \
    [ 6, 0 ] ] )

  print ( '' )
  print ( 'circle01_sample_ergodic_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  circle01_sample_ergodic() ergodically samples the unit circle.' )
  print ( '  Use it to estimate integrals.' )

  print ( '' );
  print ( '         N        1              X^2             Y^2             X^4           X^2Y^2          Y^4          X^6' )
  print ( '' )

  n = 1

  while ( n <= 65536 ):
    angle = 0.0
    x, angle = circle01_sample_ergodic ( n, angle )
    print ( '  %8d' % ( n ), end = '' )
    for i in range ( 0, 7 ):
      for j in range ( 0, 2 ):
        e[j] = e_test[i,j]

      value = monomial_value ( 2, n, e, x )

      result = circle01_length ( ) * np.sum ( value ) / float ( n )
      print ( '  %14.10g' % ( result ), end = '' )

    print ('' )
    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )
  for i in range ( 0, 7 ):
    for j in range ( 0, 2 ):
      e[j] = e_test[i,j]
    exact = circle01_monomial_integral ( e )
    print ( '  %14.10g' % ( exact ), end = '' )
  print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'circle01_sample_ergodic_test():' )
  print ( '  Normal end of execution.' )
  return

def circle01_sample_random ( n ):

#*****************************************************************************80
#
## circle01_sample_random() samples points on the circumference of the unit circle in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 September 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Russell Cheng,
#    Random Variate Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998, pages 168.
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
#    real X(2,N), the points.
#
  import numpy as np

  r = 1.0
  c = np.zeros ( 2 )

  theta = np.random.rand ( n )

  x = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
    x[0,j] = c[0] + r * np.cos ( 2.0 * np.pi * theta[j] )
    x[1,j] = c[1] + r * np.sin ( 2.0 * np.pi * theta[j] )

  return x

def circle01_sample_random_test ( ):

#*****************************************************************************80
#
## circle01_sample_random_test tests circle01_sample_random.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 June 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  import numpy as np

  e = np.zeros ( 2 )
  e_test = np.array ( [ \
    [ 0, 0 ], \
    [ 2, 0 ], \
    [ 0, 2 ], \
    [ 4, 0 ], \
    [ 2, 2 ], \
    [ 0, 4 ], \
    [ 6, 0 ] ] )

  print ( '' )
  print ( 'circle01_sample_random_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  circle01_sample_random() randomly samples the unit circle.' )
  print ( '  Use it to estimate integrals.' )

  print ( '' );
  print ( '         N        1              X^2             Y^2             X^4           X^2Y^2          Y^4          X^6' )
  print ( '' )

  n = 1

  while ( n <= 65536 ):

    x = circle01_sample_random ( n )
    print ( '  %8d' % ( n ), end = '' )
    for i in range ( 0, 7 ):
      for j in range ( 0, 2 ):
        e[j] = e_test[i,j]

      value = monomial_value ( 2, n, e, x )

      result = circle01_length ( ) * np.sum ( value ) / float ( n )
      print ( '  %14.10g' % ( result ), end = '' )

    print ('' )
    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )
  for i in range ( 0, 7 ):
    for j in range ( 0, 2 ):
      e[j] = e_test[i,j]
    exact = circle01_monomial_integral ( e )
    print ( '  %14.10g' % ( exact ), end = '' )
  print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'circle01_sample_random_test():' )
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
  print ( 'i4vec_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_print() prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_print_test():' )
  print ( '  Normal end of execution.' )
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

def i4vec_transpose_print_test ( ):

#*****************************************************************************80
#
## i4vec_transpose_print_test() tests i4vec_transpose_print().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4vec_transpose_print_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_transpose_print() prints an I4VEC' )
  print ( '  with 5 entries to a row, and an optional title.' )

  n = 12
  a = np.zeros ( n, dtype = np.int32 )
  
  for i in range ( 0, n ):
    a[i] = i + 1

  i4vec_transpose_print ( n, a, '  My array:  ' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_transpose_print_test():' )
  print ( '  Normal end of execution.' )
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

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_test() tests r8mat_transpose_print().
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
  print ( 'r8mat_transpose_print_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_transpose_print() prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_transpose_print_test():' )
  print ( '  Normal end of execution.' )
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

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_some_test() tests r8mat_transpose_print_some().
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
  print ( 'r8mat_transpose_print_some_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_transpose_print_some() prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_transpose_print_some_test():' )
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

def r8vec_print_test ( ):

#*****************************************************************************80
#
## r8vec_print_test() tests r8vec_print().
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
  import platform

  print ( '' )
  print ( 'r8vec_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_print() prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_print_test():' )
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

def circle_monte_carlo_test ( ):

#*****************************************************************************80
#
## circle_monte_carlo_test() tests circle_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 June 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'circle_monte_carlo_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test circle_monte_carlo().' )

  circle01_length_test ( )
  circle01_monomial_integral_test ( )
  circle01_sample_ergodic_test ( )
  circle01_sample_random_test ( )
  i4vec_print_test ( )
  i4vec_transpose_print_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_transpose_print_test ( )
  r8mat_transpose_print_some_test ( )
  r8vec_print_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'circle_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  circle_monte_carlo_test ( )
  timestamp ( )
 
