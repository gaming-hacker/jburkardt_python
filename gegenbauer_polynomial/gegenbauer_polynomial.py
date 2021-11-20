#! /usr/bin/env python3
#
def gegenbauer_alpha_check ( alpha ):

#*****************************************************************************80
#
## gegenbauer_alpha_check() checks the value of ALPHA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, a parameter which is part of the definition of
#    the Gegenbauer polynomials.  It must be greater than -0.5.
#
#  Output:
#
#    bool CHECK.
#    TRUE, ALPHA is acceptable.
#    FALSE, ALPHA is not acceptable. 
#
  squawk = False

  if ( -0.5 < alpha ):
    check = True
  else:
    check = False

    if ( squawk ):
      print ( '' )
      print ( 'gegenbauer_polynomial_value - Fatal error!' )
      print ( '  Illegal value of ALPHA.' )
      print ( '  ALPHA = %g' % ( alpha ) )
      print ( '  but ALPHA must be greater than -0.5.' )

  return check

def gegenbauer_alpha_check_test ( ):

#*****************************************************************************80
#
## gegenbauer_alpha_check_test() tests gegenbauer_alpha_check().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gegenbauer_alpha_check_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gegenbauer_alpha_check checks that ALPHA is legal;' )
  print ( '' )
  print ( '       ALPHA       Check?' )
  print ( '' )

  for n in range ( 0, 10 ):

    alpha = -5.0 + 10.0 * np.random.rand ( )
    check = gegenbauer_alpha_check ( alpha )
    print ( '  %10.4f       %5s' % ( alpha, check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'gegenbauer_alpha_check_test' )
  print ( '  Normal end of execution.' )
  return

def gegenbauer_ek_compute ( n, alpha ):

#*****************************************************************************80
#
## gegenbauer_ek_compute(): Elhay-Kautsky method for Gauss-Gegenbauer rule.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= 1 ) (1-x^2)^(alpha-1/2) * f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Input:
#
#    integer N, the order.
#
#    real ALPHA, determines the exponent of (1-X^2)^(ALPHA-1/2).
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
  from scipy.special import gamma
#
#  Define the zero-th moment.
#
  zemu = 2.0 ** ( 2.0 * alpha + 1.0 ) \
    * gamma ( alpha + 1.0 ) \
    * gamma ( alpha + 1.0 ) \
    / gamma ( 2.0 * alpha + 2.0 )
#
#  Define the Jacobi matrix.
#
  x = np.zeros ( n )

  bj = np.zeros ( n )

  bj[0] = 4.0 * ( alpha + 1.0 ) ** 2 \
    / ( ( 2.0 * alpha + 3.0 ) * ( 2.0 * alpha + 2.0 ) ** 2 )

  for i in range ( 2, n ):
    abi = 2.0 * ( alpha + i )
    bj[i-1] = 4.0 * i * ( alpha + i ) ** 2 * ( 2.0 * alpha + i ) \
      / ( ( abi - 1.0 ) * ( abi + 1.0 ) * abi * abi )

  for i in range ( 0, n ):
    bj[i] = np.sqrt ( bj[i] )

  w = np.zeros ( n )

  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def gegenbauer_ek_compute_test ( ):

#*****************************************************************************80
#
## gegenbauer_ek_compute_test() tests gegenbauer_ek_compute().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  alpha = 0.5

  print ( '' )
  print ( 'gegenbauer_ek_compute_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gegenbauer_ek_compute computes Gauss-Gegenbauer rules' )
  print ( '' )
  print ( '  Abscissas and weights for a generalized Gauss Gegenbauer rule' )
  print ( '  with ALPHA = %g' % ( alpha ) )
  print ( '  Integration interval is [-1,+1]' )

  for n in range ( 1, 11 ):

    x, w = gegenbauer_ek_compute ( n, alpha )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, w[i], x[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'gegenbauer_ek_compute_test' )
  print ( '  Normal end of execution.' )
  return

def gegenbauer_integral ( expon, alpha ):

#*****************************************************************************80
#
## gegenbauer_integral() evaluates the integral of a monomial with Gegenbauer weight.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= +1 ) x^EXPON (1-x^2)^ALPHA dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#    real ALPHA, the exponent of (1-X^2) in the weight factor.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import gamma

  if ( ( expon % 2 ) == 1 ):
    value = 0.0
    return value

  c = expon

  arg1 = - alpha
  arg2 =   1.0 + c
  arg3 =   2.0 + alpha + c
  arg4 = - 1.0

  value1 = r8_hyper_2f1 ( arg1, arg2, arg3, arg4 )

  value = 2.0 * gamma ( 1.0 + c ) * gamma ( 1.0 + alpha ) \
    * value1 / gamma ( 2.0 + alpha  + c )

  return value

def gegenbauer_integral_test ( ):

#*****************************************************************************80
#
## gegenbauer_integral_test() tests gegenbauer_integral().
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

  alpha = 0.25

  print ( '' )
  print ( 'gegenbauer_integral_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gegenbauer_integral evaluates' )
  print ( '  Integral ( -1 < x < +1 ) x^n * (1-x*x)^alpha dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = gegenbauer_integral ( n, alpha )

    print ( '  %8d  %24.16g' % ( n, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'gegenbauer_integral_test' )
  print ( '  Normal end of execution.' )
  return

def gegenbauer_polynomial_test ( ):

#*****************************************************************************80
#
## gegenbauer_polynomial_test() tests gegenbauer_polynomial().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gegenbauer_polynomial_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the gegenbauer_polynomial library.' )

  gegenbauer_alpha_check_test ( )
  gegenbauer_ek_compute_test ( )
  gegenbauer_integral_test ( )
  gegenbauer_polynomial_value_test ( )
  gegenbauer_ss_compute_test ( )

  imtqlx_test ( )

  r8_hyper_2f1_test ( )
  r8_psi_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gegenbauer_polynomial_test:' )
  print ( '  Normal end of execution.' )
  return

def gegenbauer_polynomial_value ( m, n, alpha, x ):

#*****************************************************************************80
#
## gegenbauer_polynomial_value() computes Gegenbauer polynomials C(I,ALPHA)(X).
#
#  Differential equation:
#
#    (1-X*X) Y'' - (2 ALPHA + 1) X Y' + M (M + 2 ALPHA) Y = 0
#
#  Recursion:
#
#    C(0,ALPHA,X) = 1,
#    C(1,ALPHA,X) = 2*ALPHA*X
#    C(M,ALPHA,X) = (  ( 2*M-2+2*ALPHA) * X * C(M-1,ALPHA,X) 
#                    + (  -M+2-2*ALPHA)   *   C(M-2,ALPHA,X) ) / M
#
#  Restrictions:
#
#    ALPHA must be greater than -0.5.
#
#  Special values:
#
#    If ALPHA = 1, the Gegenbauer polynomials reduce to the Chebyshev
#    polynomials of the second kind.
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) ( 1 - X^2 )^( ALPHA - 0.5 ) * C(M,ALPHA,X)^2 dX
#
#    = PI * 2^( 1 - 2 * ALPHA ) * Gamma ( M + 2 * ALPHA ) 
#      / ( M! * ( M + ALPHA ) * ( Gamma ( ALPHA ) )^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer M, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    integer N, the number of evaluation points.
#
#    real ALPHA, a parameter which is part of the definition of
#    the Gegenbauer polynomials.  It must be greater than -0.5.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real C(1:M+1,N), the values of Gegenbauer polynomials 0 through M
#    at the N points X.  
#
  import numpy as np

  check = gegenbauer_alpha_check ( alpha )

  if ( not check ):
    print ( '' )
    print ( 'gegenbauer_polynomial_value - Fatal error!' )
    print ( '  gegenbauer_alpha_check failed.' )
    raise Exception ( 'gegenbauer_polynomial_value - Fatal error!' )

  c = np.zeros ( [ m + 1, n ] )

  if ( m < 0 ):
    return c

  for j in range ( 0, n ):
    c[0,j] = 1.0

  if ( n == 0 ):
    return c

  if ( m < 1 ):
    return c

  for j in range ( 0, n ):
    c[1,j] = 2.0 * alpha * x[j]

  for i in range ( 2, m + 1 ):
    for j in range ( 0, n ):
      c[i,j] = (  (     2 * i - 2  + 2.0 * alpha ) * x[j] * c[i-1,j]   \
               +  (       - i + 2  - 2.0 * alpha ) *        c[i-2,j] ) \
               /            i 

  return c

def gegenbauer_polynomial_value_test ( ):

#*****************************************************************************80
#
## gegenbauer_polynomial_value_test() tests gegenbauer_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gegenbauer_polynomial_value_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gegenbauer_polynomial_value evaluates the Gegenbauer polynomial.' )
  print ( '' )
  print ( '       M     ALPHA         X           GPV    GEGENBAUER' )
  print ( '' )

  n_data = 0
  x = np.zeros ( 1 )

  while ( True ):

    n_data, m, alpha, xscalar, fx = gegenbauer_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break
#
#  Since gegenbauer_polynomial_value expects a vector input X, we have to
#  do a little "rewrapping" of the input.
#
    n = 1
    x[0] = xscalar
    c = gegenbauer_polynomial_value ( m, n, alpha, x )
    print ( '  %6d  %8.2f  %8.2f  %12f  %12f' % ( m, alpha, x[0], fx, c[m,0] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'gegenbauer_polynomial_value_test:' )
  print ( '  Normal end of execution.' )
  return

def gegenbauer_polynomial_values ( n_data ):

#*****************************************************************************80
#
## gegenbauer_polynomial_values() returns some values of the Gegenbauer polynomials.
#
#  Discussion:
#
#    The Gegenbauer polynomials are also known as the "spherical
#    polynomials" or "ultraspherical polynomials".
#
#    In Mathematica, the function can be evaluated by:
#
#      GegenbauerC[n,m,x]
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
#    integer N, the order parameter of the function.
#
#    real A, the real parameter of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 38

  a_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.0E+00, \
      1.0E+00, \
      2.0E+00, \
      3.0E+00, \
      4.0E+00, \
      5.0E+00, \
      6.0E+00, \
      7.0E+00, \
      8.0E+00, \
      9.0E+00, \
     10.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00 ))

  f_vec = np.array ( ( \
       1.0000000000E+00, \
       0.2000000000E+00, \
      -0.4400000000E+00, \
      -0.2800000000E+00, \
       0.2320000000E+00, \
       0.3075200000E+00, \
      -0.0805760000E+00, \
      -0.2935168000E+00, \
      -0.0395648000E+00, \
       0.2459712000E+00, \
       0.1290720256E+00, \
       0.0000000000E+00, \
      -0.3600000000E+00, \
      -0.0800000000E+00, \
       0.8400000000E+00, \
       2.4000000000E+00, \
       4.6000000000E+00, \
       7.4400000000E+00, \
      10.9200000000E+00, \
      15.0400000000E+00, \
      19.8000000000E+00, \
      25.2000000000E+00, \
      -9.0000000000E+00, \
      -0.1612800000E+00, \
      -6.6729600000E+00, \
      -8.3750400000E+00, \
      -5.5267200000E+00, \
       0.0000000000E+00, \
       5.5267200000E+00, \
       8.3750400000E+00, \
       6.6729600000E+00, \
       0.1612800000E+00, \
      -9.0000000000E+00, \
     -15.4252800000E+00, \
      -9.6969600000E+00, \
      22.4409600000E+00, \
     100.8892800000E+00, \
     252.0000000000E+00 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  2, \
     2,  2,  2, \
     2,  2,  2, \
     2,  2,  2, \
     2,  5,  5, \
     5,  5,  5, \
     5,  5,  5, \
     5,  5,  5, \
     5,  5,  5, \
     5,  5 ))

  x_vec = np.array ( ( \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
     -0.50E+00, \
     -0.40E+00, \
     -0.30E+00, \
     -0.20E+00, \
     -0.10E+00, \
      0.00E+00, \
      0.10E+00, \
      0.20E+00, \
      0.30E+00, \
      0.40E+00, \
      0.50E+00, \
      0.60E+00, \
      0.70E+00, \
      0.80E+00, \
      0.90E+00, \
      1.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, a, x, f

def gegenbauer_polynomial_values_test ( ):

#*****************************************************************************80
#
## gegenbauer_polynomial_values_test() tests gegenbauer_polynomial_values().
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
  print ( 'gegenbauer_polynomial_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gegenbauer_polynomial_values stores values of the Gegenbauer polynomials.' )
  print ( '' )
  print ( '      N            A         X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, a, x, fx = gegenbauer_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %12f  %24.16g' % ( n, a, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'gegenbauer_polynomial_values_test:' )
  print ( '  Normal end of execution.' )
  return

def gegenbauer_ss_compute ( n, alpha ):

#*****************************************************************************80
#
## gegenbauer_ss_compute() computes a Gauss-Gegenbauer quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) (1-X^2)^ALPHA * F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    Thanks to Janiki Raman for pointing out a problem in an earlier
#    version of the code that occurred when ALPHA was -0.5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    Original FORTRAN77 version by Arthur Stroud, Don Secrest.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    integer N, the order.
#
#    real ALPHA, the exponent of (1-X^2) in the weight.  
#    -1.0 < ALPHA is required.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
  from scipy.special import gamma
#
#  Check N.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'gegenbauer_ss_compute - Fatal error!' )
    print ( '  1 <= N is required.' )
    raise Exception ( 'gegenbauer_ss_compute - Fatal error!' )
#
#  Check ALPHA.
#
  if ( alpha <= -1.0 ):
    print ( '' )
    print ( 'gegenbauer_ss_compute - Fatal error!' )
    print ( '  -1.0 < ALPHA is required.' )
    raise Exception ( 'gegenbauer_ss_compute - Fatal error!' )

  x = np.zeros ( n )
  w = np.zeros ( n )
#
#  Set the recursion coefficients.
#
  c = np.zeros ( n )

  c[0] = 0.0;
  if ( 2 <= n ):
    c[1] = 1.0 / ( 2.0 * alpha + 3.0 )

  for i in range ( 2, n ):

    c[i] = float ( i ) \
      * ( alpha + alpha + i ) / \
      ( ( alpha + alpha + 2 * i + 1 ) \
      * ( alpha + alpha + 2 * i - 1 ) )

  delta = gamma ( alpha         + 1.0 ) \
        * gamma (         alpha + 1.0 ) \
        / gamma ( alpha + alpha + 2.0 )

  c_product = 1.0
  for i in range ( 1, n ):
    c_product = c_product * c[i]

  cc = delta * 2.0 ** ( 2.0 * alpha + 1.0 ) * c_product

  for i in range ( 0, n ):

    if ( i == 0 ):

      an = alpha / float ( n )

      r1 = ( 1.0 + alpha ) * ( 2.78 / ( 4.0 + n * n ) + 0.768 * an / n )

      r2 = 1.0 + 2.44 * an + 1.281 * an ** 2

      xval = ( r2 - r1 ) / r2

    elif ( i == 1 ):

      r1 = ( 4.1 + alpha ) / ( ( 1.0 + alpha ) * ( 1.0 + 0.156 * alpha ) )

      r2 = 1.0 + 0.06 * ( n - 8.0 ) * ( 1.0 + 0.12 * alpha ) / n

      r3 = 1.0 + 0.012 * alpha * ( 1.0 + 0.25 * abs ( alpha ) ) / n

      xval = xval - r1 * r2 * r3 * ( 1.0 - xval )

    elif ( i == 2 ):

      r1 = ( 1.67 + 0.28 * alpha ) / ( 1.0 + 0.37 * alpha )

      r2 = 1.0 + 0.22 * ( n - 8.0 ) / n

      r3 = 1.0 + 8.0 * alpha / ( ( 6.28 + alpha ) * n * n )

      xval = xval - r1 * r2 * r3 * ( x[0] - xval )

    elif ( i < n - 2 ):

      xval = 3.0 * x[i-1] - 3.0 * x[i-2] + x[i-3]

    elif ( i == n - 2 ):

      r1 = ( 1.0 + 0.235 * alpha ) / ( 0.766 + 0.119 * alpha )

      r2 = 1.0 / ( 1.0 + 0.639 * ( n - 4.0 ) / ( 1.0 + 0.71 * ( n - 4.0 ) ) )

      r3 = 1.0 / ( 1.0 + 20.0 * alpha / ( ( 7.5 + alpha ) * n * n ) )

      xval = xval + r1 * r2 * r3 * ( xval - x[i-2] )

    elif ( i == n - 1 ):

      r1 = ( 1.0 + 0.37 * alpha ) / ( 1.67 + 0.28 * alpha )

      r2 = 1.0 / ( 1.0 + 0.22 * ( n - 8.0 ) / n )

      r3 = 1.0 / ( 1.0 + 8.0 * alpha / ( ( 6.28 + alpha ) * n * n ) )

      xval = xval + r1 * r2 * r3 * ( xval - x[i-2] )

    xval, dp2, p1 = gegenbauer_ss_root ( xval, n, alpha, c )
 
    x[i] = xval
    w[i] = cc / ( dp2 * p1 )
#
#  Reverse the order of the values.
#
  x = r8vec_reverse ( n, x );
  w = r8vec_reverse ( n, w );

  return x, w

def gegenbauer_ss_recur ( x, n, alpha, c ):

#*****************************************************************************80
#
## gegenbauer_ss_recur(): value and derivative of a Gegenbauer polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    Original FORTRAN77 version by Arthur Stroud, Don Secrest,
#    Python version by John Burkardt,
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    real X, the point at which polynomials are evaluated.
#
#    integer N, the order of the polynomial to be computed.
#
#    real ALPHA, the exponent of (1-X^2) in the quadrature rule.
#
#    real C(N), the recursion coefficients.
#
#  Output:
#
#    real P2, the value of J(N)(X).
#
#    real DP2, the value of J'(N)(X).
#
#    real P1, the value of J(N-1)(X).
#
  p1 = 1.0
  dp1 = 0.0

  p2 = x
  dp2 = 1.0

  for i in range ( 1, n ):

    p0 = p1
    dp0 = dp1

    p1 = p2
    dp1 = dp2

    p2 = x * p1 - c[i] * p0
    dp2 = x * dp1 + p1 - c[i] * dp0

  return p2, dp2, p1

def gegenbauer_ss_root ( x, n, alpha, c ):

#*****************************************************************************80
#
## gegenbauer_ss_root() improves an approximate root of a Gegenbauer polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    real X, the approximate root.
#
#    integer N, the order of the polynomial to be computed.
#
#    real ALPHA, the exponent of (1-X^2) in the quadrature rule.
#
#    real C(N), the recursion coefficients.
#
#  Output:
#
#    real X, the improved approximate root.
#
#    real DP2, the value of J'(N)(X).
#
#    real P1, the value of J(N-1)(X).
#
  maxstep = 10
  eps = 2.220446049250313E-016

  for i in range ( 0, maxstep ):

    p2, dp2, p1 = gegenbauer_ss_recur ( x, n, alpha, c )

    d = p2 / dp2
    x = x - d

    if ( abs ( d ) <= eps * ( abs ( x ) + 1.0 ) ):
      break

  return x, dp2, p1

def gegenbauer_ss_compute_test ( ):

#*****************************************************************************80
#
## gegenbauer_ss_compute_test() tests gegenbauer_ss_compute().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  alpha = 0.5

  print ( '' )
  print ( 'gegenbauer_ss_compute_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  gegenbauer_ss_compute computes Gauss-Gegenbauer rules;' )
  print ( '' )
  print ( '  Abscissas and weights for a generalized Gauss Gegenbauer rule' )
  print ( '  with ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '   #                         W                         X' )
  print ( '' )

  for n in range ( 1, 11 ):

    x, w = gegenbauer_ss_compute ( n, alpha );

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, w[i], x[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'gegenbauer_ss_compute_test:' )
  print ( '  Normal end of execution.' )
  return

def hyper_2f1_values ( n_data ):

#*****************************************************************************80
#
## hyper_2f1_values() returns some values of the hypergeometric 2F1 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = Hypergeometric2F1 [ a, b, c, x ]
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
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996,
#    ISBN: 0-8493-2479-3,
#    LC: QA47.M315.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call. 
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again..
#
#    real A, B, C, X, the parameters.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 24

  a_vec = np.array ( ( \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3 ))

  b_vec = np.array ( ( \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7 ))

  c_vec = np.array ( ( \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5 ))

  f_vec = np.array ( ( \
    0.72356129348997784913, \
    0.97911109345277961340, \
    1.0216578140088564160, \
    1.4051563200112126405, \
    0.46961431639821611095, \
    0.95296194977446325454, \
    1.0512814213947987916, \
    2.3999062904777858999, \
    0.29106095928414718320, \
    0.92536967910373175753, \
    1.0865504094806997287, \
    5.7381565526189046578, \
    15090.669748704606754, \
   -104.31170067364349677, \
    21.175050707768812938, \
    4.1946915819031922850, \
    1.0170777974048815592E+10, \
   -24708.635322489155868, \
    1372.2304548384989560, \
    58.092728706394652211, \
    5.8682087615124176162E+18, \
   -4.4635010147295996680E+08, \
    5.3835057561295731310E+06, \
    20396.913776019659426 ))

  x_vec = np.array ( ( \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.55, \
    0.55, \
    0.55, \
    0.55, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.55, \
    0.55, \
    0.55, \
    0.55, \
    0.85, \
    0.85, \
    0.85, \
    0.85 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    b = 0
    c = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    c = c_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, c, x, f

def hyper_2f1_values_test ( ):

#*****************************************************************************80
#
## hyper_2f1_values_test() tests hyper_2f1_values().
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
  print ( 'hyper_2f1_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hyper_2f1_values stores values of the hypergeometric function 2F1' )
  print ( '' )
  print ( '     A     B        C           X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, c, x, f = hyper_2f1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %4d  %12f  %12f  %24.16g' % ( a, b, c, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'hyper_2f1_values_test:' )
  print ( '  Normal end of execution.' )
  return

def imtqlx ( n, d, e, z ):

#*****************************************************************************80
#
## imtqlx() diagonalizes a symmetric tridiagonal matrix.
#
#  Discussion:
#
#    This routine is a slightly modified version of the EISPACK routine to
#    perform the implicit QL algorithm on a symmetric tridiagonal matrix.
#
#    The authors thank the authors of EISPACK for permission to use this
#    routine.
#
#    It has been modified to produce the product Q' * Z, where Z is an input
#    vector and Q is the orthogonal matrix diagonalizing the input matrix.
#    The changes consist (essentially) of applying the orthogonal 
#    transformations directly to Z as they are generated.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#    Roger Martin, James Wilkinson,
#    The Implicit QL Algorithm,
#    Numerische Mathematik,
#    Volume 12, Number 5, December 1968, pages 377-383.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real D(N), the diagonal entries of the matrix.
#
#    real E(N), the subdiagonal entries of the
#    matrix, in entries E(1) through E(N-1). 
#
#    real Z(N), a vector to be operated on.
#
#  Output:
#
#    real LAM(N), the diagonal entries of the diagonalized matrix.
#
#    real QTZ(N), the value of Q' * Z, where Q is the matrix that 
#    diagonalizes the input symmetric tridiagonal matrix.
#
  import numpy as np

  lam = np.zeros ( n )
  for i in range ( 0, n ):
    lam[i] = d[i]

  qtz = np.zeros ( n )
  for i in range ( 0, n ):
    qtz[i] = z[i]

  if ( n == 1 ):
    return lam, qtz

  itn = 30

  epsilon = np.finfo(float).eps

  e[n-1] = 0.0

  for l in range ( 1, n + 1 ):

    j = 0

    while ( True ):

      for m in range ( l, n + 1 ):

        if ( m == n ):
          break

        if ( abs ( e[m-1] ) <= epsilon * ( abs ( lam[m-1] ) + abs ( lam[m] ) ) ):
          break

      p = lam[l-1]

      if ( m == l ):
        break

      if ( itn <= j ):
        print ( '' )
        print ( 'imtqlx - Fatal error!' )
        print ( '  Iteration limit exceeded.' )
        raise Exception ( 'imtqlx - Fatal error!' )

      j = j + 1
      g = ( lam[l] - p ) / ( 2.0 * e[l-1] )
      r = np.sqrt ( g * g + 1.0 )

      if ( g < 0.0 ):
        t = g - r
      else:
        t = g + r

      g = lam[m-1] - p + e[l-1] / ( g + t )
 
      s = 1.0
      c = 1.0
      p = 0.0
      mml = m - l

      for ii in range ( 1, mml + 1 ):

        i = m - ii
        f = s * e[i-1]
        b = c * e[i-1]

        if ( abs ( g ) <= abs ( f ) ):
          c = g / f
          r = np.sqrt ( c * c + 1.0 )
          e[i] = f * r
          s = 1.0 / r
          c = c * s
        else:
          s = f / g
          r = np.sqrt ( s * s + 1.0 )
          e[i] = g * r
          c = 1.0 / r
          s = s * c

        g = lam[i] - p
        r = ( lam[i-1] - g ) * s + 2.0 * c * b
        p = s * r
        lam[i] = g + p
        g = c * r - b
        f = qtz[i]
        qtz[i]   = s * qtz[i-1] + c * f
        qtz[i-1] = c * qtz[i-1] - s * f

      lam[l-1] = lam[l-1] - p
      e[l-1] = g
      e[m-1] = 0.0

  for ii in range ( 2, n + 1 ):

     i = ii - 1
     k = i
     p = lam[i-1]

     for j in range ( ii, n + 1 ):

       if ( lam[j-1] < p ):
         k = j
         p = lam[j-1]

     if ( k != i ):

       lam[k-1] = lam[i-1]
       lam[i-1] = p

       p        = qtz[i-1]
       qtz[i-1] = qtz[k-1]
       qtz[k-1] = p

  return lam, qtz

def imtqlx_test ( ):

#*****************************************************************************80
#
## imtqlx_test() tests imtqlx().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'imtqlx_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  imtqlx takes a symmetric tridiagonal matrix A' )
  print ( '  and computes its eigenvalues LAM.' )
  print ( '  It also accepts a vector Z and computes Q\'*Z,' )
  print ( '  where Q is the matrix that diagonalizes A.' )

  n = 5
  d = np.zeros ( n )
  for i in range ( 0, n ):
    d[i] = 2.0;
  e = np.zeros ( n )
  for i in range ( 0, n - 1 ):
    e[i] = -1.0
  e[n-1] = 0.0
  z = np.ones ( n )

  lam, qtz = imtqlx ( n, d, e, z )

  r8vec_print ( n, lam, '  Computed eigenvalues:' )

  lam2 = np.zeros ( n )
  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    lam2[i] = 4.0 * ( np.sin ( angle ) ) ** 2

  r8vec_print ( n, lam2, '  Exact eigenvalues:' )

  r8vec_print ( n, z, '  Vector Z:' )
  r8vec_print ( n, qtz, '  Vector Q''*Z:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'imtqlx_test:' )
  print ( '  Normal end of execution.' )
  return

def psi_values ( n_data ):

#*****************************************************************************80
#
## psi_values() returns some values of the Psi or Digamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyGamma[x]
#
#    or
#
#      PolyGamma[0,x]
#
#    PSI(X) = d ln ( Gamma ( X ) ) / d X = Gamma'(X) / Gamma(X)
#
#    PSI(1) = -Euler's constant.
#
#    PSI(X+1) = PSI(X) + 1 / X.
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
    -10.42375494041108E+00, \
     -5.289039896592188E+00, \
     -3.502524222200133E+00, \
     -2.561384544585116E+00, \
     -1.963510026021423E+00, \
     -1.540619213893190E+00, \
     -1.220023553697935E+00, \
     -0.9650085667061385E+00, \
     -0.7549269499470514E+00, \
     -0.5772156649015329E+00, \
     -0.4237549404110768E+00, \
     -0.2890398965921883E+00, \
     -0.1691908888667997E+00, \
     -0.6138454458511615E-01, \
      0.3648997397857652E-01, \
      0.1260474527734763E+00, \
      0.2085478748734940E+00, \
      0.2849914332938615E+00, \
      0.3561841611640597E+00, \
      0.4227843350984671E+00 ))

  x_vec = np.array ( ( \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00, \
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def psi_values_test ( ):

#*****************************************************************************80
#
## psi_values_test() tests psi_values().
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
  print ( 'psi_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  psi_values stores values of the PSI function.' )
  print ( '' )
  print ( '      X         PSI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'psi_values_test:' )
  print ( '  Normal end of execution.' )
  return

def r8_hyper_2f1 ( a, b, c, x ):

#*****************************************************************************80
#
## r8_hyper_2f1() evaluates the hypergeometric function F(A,B,C,X).
#
#  Discussion:
#
#    A minor bug was corrected.  The HW variable, used in several places as
#    the "old" value of a quantity being iteratively improved, was not
#    being initialized.  JVB, 11 February 2008.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
#    Python version by John Burkardt.
#
#    The F77 original version of this routine is copyrighted by
#    Shanjie Zhang and Jianming Jin.  However, they give permission to
#    incorporate this routine into a user program provided that the copyright
#    is acknowledged.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#  Input:
#
#    real A, B, C, X, the arguments of the function.
#    C must not be equal to a nonpositive integer.
#    X < 1.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np
  from scipy.special import gamma

  el = 0.5772156649015329

  l0 = ( c == int ( c ) ) and ( c < 0.0 )
  l1 = ( 1.0 - x < 1.0E-15 ) and ( c - a - b <= 0.0 )
  l2 = ( a == int ( a ) ) and ( a < 0.0 )
  l3 = ( b == int ( b ) ) and ( b < 0.0 )
  l4 = ( c - a == int ( c - a ) ) and ( c - a <= 0.0 )
  l5 = ( c - b == int ( c - b ) ) and ( c - b <= 0.0 )

  if ( l0 ):
    print ( '' )
    print ( 'R8_hyper_2f1 - Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  C is integral and negative.' )
    print ( '  C = %f' % ( c ) )

  if ( l1 ):
    print ( '' )
    print ( 'R8_hyper_2f1 - Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  1 = X < 0, C - A - B <= 0.' )
    print ( '  A = %f' % ( a ) )
    print ( '  B = %f' % ( b ) )
    print ( '  C = %f' % ( c ) )
    print ( '  X = %f' % ( x ) )

  if ( 0.95 < x ):
    eps = 1.0E-08
  else:
    eps = 1.0E-15

  if ( x == 0.0 or a == 0.0 or b == 0.0 ):

    value = 1.0
    return value

  elif ( 1.0 - x == eps and 0.0 < c - a - b ):

    gc = gamma ( c )
    gcab = gamma ( c - a - b )
    gca = gamma ( c - a )
    gcb = gamma ( c - b )
    value = gc * gcab / ( gca * gcb )
    return value

  elif ( 1.0 + x <= eps and abs ( c - a + b - 1.0 ) <= eps ):

    g0 = np.sqrt ( np.pi ) * 2.0 ** ( - a )
    g1 = gamma ( c )
    g2 = gamma ( 1.0 + a / 2.0 - b )
    g3 = gamma ( 0.5 + 0.5 * a )
    value = g0 * g1 / ( g2 * g3 )
    return value

  elif ( l2 or l3 ):

    if ( l2 ):
      nm = int ( abs ( a ) )

    if ( l3 ):
      nm = int ( abs ( b ) )

    value = 1.0
    r = 1.0

    for k in range ( 1, nm + 1 ):
      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r

    return value

  elif ( l4 or l5 ):

    if ( l4 ):
      nm = int ( abs ( c - a ) )
 
    if ( l5 ):
      nm = int ( abs ( c - b ) )

    value = 1.0
    r  = 1.0
    for k in range ( 1, nm + 1 ):
      r = r * ( c - a + float ( k ) - 1.0 ) * ( c - b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r
    value = ( 1.0 - x ) ** ( c - a - b ) * hf
    return value

  aa = a
  bb = b
  x1 = x

  if ( x < 0.0 ):
    x = x / ( x - 1.0 )
    if ( a < c and b < a and 0.0 < b ):
      a = bb
      b = aa
    b = c - b

  if ( 0.75 <= x ):

    gm = 0.0

    if ( abs ( c - a - b - int ( c - a - b ) ) < 1.0E-15 ):

      m = int ( c - a - b )
      ga = gamma ( a )
      gb = gamma ( b )
      gc = gamma ( c )
      gam = gamma ( a + float ( m ) )
      gbm = gamma ( b + float ( m ) )

      pa = r8_psi ( a )
      pb = r8_psi ( b )

      if ( m != 0 ):
        gm = 1.0

      for j in range ( 1, abs ( m ) ):
        gm = gm * float ( j )

      rm = 1.0
      for j in range ( 1, abs ( m ) + 1 ):
        rm = rm * float ( j )
 
      f0 = 1.0
      r0 = 1.0
      r1 = 1.0
      sp0 = 0.0
      sp = 0.0

      if ( 0 <= m ):

        c0 = gm * gc / ( gam * gbm )
        c1 = - gc * ( x - 1.0 ) ** m / ( ga * gb * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0
 
        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / ( a + float ( k ) - 1.0 ) \
            + 1.0 / ( b + float ( k ) - 1.0 ) - 1.0 / float ( k )

        f1 = pa + pb + sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + ( 1.0 - a ) \
              / ( float ( j + k ) * ( a + float ( j + k ) - 1.0 ) ) \
              + 1.0 / ( b + float ( j + k ) - 1.0 )

          rp = pa + pb + 2.0 * el + sp + sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + m + float ( k ) - 1.0 ) * ( b + m + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break
 
          hw = f1

        value = f0 * c0 + f1 * c1

      elif ( m < 0 ):

        m = - m
        c0 = gm * gc / ( ga * gb * ( 1.0 - x ) ** m )
        c1 = - ( - 1 ) ** m * gc / ( gam * gbm * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a - float ( m ) + float ( k ) - 1.0 ) \
            * ( b - float ( m ) + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0

        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / float ( k )

        f1 = pa + pb - sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) \
            / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + 1.0 / float ( j + k )

          rp = pa + pb + 2.0 * el + sp - sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break

          hw = f1

        value = f0 * c0 + f1 * c1

    else:

      ga = gamma ( a )
      gb = gamma ( b )
      gc = gamma ( c )
      gca = gamma ( c - a )
      gcb = gamma ( c - b )
      gcab = gamma ( c - a - b )
      gabc = gamma ( a + b - c )
      c0 = gc * gcab / ( gca * gcb )
      c1 = gc * gabc / ( ga * gb ) * ( 1.0 - x ) ** ( c - a - b )
      value = 0.0
      hw = value
      r0 = c0
      r1 = c1

      for k in range ( 1, 251 ):

        r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( a + b - c + float ( k ) ) ) * ( 1.0 - x )

        r1 = r1 * ( c - a + float ( k ) - 1.0 ) \
          * ( c - b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( c - a - b + float ( k ) ) ) * ( 1.0 - x )

        value = value + r0 + r1

        if ( abs ( value - hw ) < abs ( value ) * eps ):
          break

        hw = value

      value = value + c0 + c1

  else:

    a0 = 1.0

    if ( a < c and c < 2.0 * a and b < c and c < 2.0 * b ):

      a0 = ( 1.0 - x ) ** ( c - a - b )
      a = c - a
      b = c - b

    value = 1.0
    hw = value
    r = 1.0

    for k in range ( 1, 251 ):

      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( k * ( c + float ( k ) - 1.0 ) ) * x

      value = value + r

      if ( abs ( value - hw ) <= abs ( value ) * eps ):
        break

      hw = value

    value = a0 * value

  if ( x1 < 0.0 ):
    x = x1
    c0 = 1.0 / ( 1.0 - x ) ** aa
    value = c0 * value

  if ( 120 < k ):
    print ( '' )
    print ( 'r8_hyper_2f1 - Warning!' )
    print ( '  A large number of iterations were needed.' )
    print ( '  The accuracy of the results should be checked.' )

  return value

def r8_hyper_2f1_test ( ):

#*****************************************************************************80
#
## r8_hyper_2f1_test() tests r8_hyper_2f1().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8_hyper_2f1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_hyper_2f1 evaluates the hypergeometric 2F1 function.' )
  print ( '' )
  print ( '      A       B       C       X       2F1                       2F1                     DIFF' )
  print ( '                                     ' )
  print ( '(tabulated)               (computed)' )
  print ( '' )

  n_data = 0

  while ( True ):

    [ n_data, a, b, c, x, fx1 ] = hyper_2f1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_hyper_2f1 ( a, b, c, x )
 
    diff = abs ( fx1 - fx2 )
    print ( '  %6g  %6g  %6g  %6g  %24g  %24g  %10g' \
      % ( a, b, c, x, fx1, fx2, diff ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_hyper_2f1_test' )
  print ( '  Normal end of execution.' )
  return

def r8_psi ( x ):

#*****************************************************************************80
#
## r8_psi() evaluates the function Psi(X).
#
#  Discussion:
#
#    This routine evaluates the logarithmic derivative of the
#    Gamma function,
#
#      PSI(X) = d/dX ( GAMMA(X) ) / GAMMA(X)
#             = d/dX LN ( GAMMA(X) )
#
#    for real X, where either
#
#      - XMAX1 < X < - XMIN, and X is not a negative integer,
#
#    or
#
#      XMIN < X.
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
#    Original FORTRAN77 version by William Cody.
#    Python version by John Burkardt.
#
#  Reference:
#
#    William Cody, Anthony Strecok, Henry Thacher,
#    Chebyshev Approximations for the Psi Function,
#    Mathematics of Computation,
#    Volume 27, Number 121, January 1973, pages 123-127.
#
#  Input:
#
#    real X, the argument of the function.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np

  p1 = np.array ( ( \
   4.5104681245762934160E-03, \
   5.4932855833000385356, \
   3.7646693175929276856E+02, \
   7.9525490849151998065E+03, \
   7.1451595818951933210E+04, \
   3.0655976301987365674E+05, \
   6.3606997788964458797E+05, \
   5.8041312783537569993E+05, \
   1.6585695029761022321E+05 ))

  p2 = np.array ( ( \
  -2.7103228277757834192, \
  -1.5166271776896121383E+01, \
  -1.9784554148719218667E+01, \
  -8.8100958828312219821, \
  -1.4479614616899842986, \
  -7.3689600332394549911E-02, \
  -6.5135387732718171306E-21 ))

  piov4 = 0.78539816339744830962

  q1 = np.array ( ( \
   9.6141654774222358525E+01, \
   2.6287715790581193330E+03, \
   2.9862497022250277920E+04, \
   1.6206566091533671639E+05, \
   4.3487880712768329037E+05, \
   5.4256384537269993733E+05, \
   2.4242185002017985252E+05, \
   6.4155223783576225996E-08 ))

  q2 = np.array ( ( \
   4.4992760373789365846E+01, \
   2.0240955312679931159E+02, \
   2.4736979003315290057E+02, \
   1.0742543875702278326E+02, \
   1.7463965060678569906E+01, \
   8.8427520398873480342E-01 ))

  x01 = 187.0
  x01d = 128.0
  x02 = 6.9464496836234126266E-04
  xinf = 1.70E+38
  xlarge = 2.04E+15
  xmax1 = 3.60E+16
  xmin1 = 5.89E-39
  xsmall = 2.05E-09

  w = abs ( x )
  aug = 0.0
#
#  Check for valid arguments, then branch to appropriate algorithm.
#
  if ( xmax1 <= - x or w < xmin1 ):

    if ( 0.0 < x ):
      value = - xinf
    else:
      value = xinf;

    return value

  if ( x < 0.5 ):
#
#  X < 0.5, use reflection formula: psi(1-x) = psi(x) + pi * cot(pi*x)
#  Use 1/X for PI*COTAN(PI*X)  when  XMIN1 < |X| <= XSMALL.
#
    if ( w <= xsmall ):

      aug = - 1.0 / x
#
#  Argument reduction for cotangent.
#
    else:

      if ( x < 0.0 ):
        sgn = piov4
      else:
        sgn = - piov4

      w = w - int ( w )
      nq = int ( w * 4.0 )
      w = 4.0 * ( w - float ( nq ) * 0.25 )
#
#  W is now related to the fractional part of 4.0 * X.
#  Adjust argument to correspond to values in the first
#  quadrant and determine the sign.
#
      n = ( nq // 2 )

      if ( n + n != nq ):
        w = 1.0 - w

      z = piov4 * w

      if ( ( n % 2 ) != 0 ):
        sgn = - sgn
#
#  Determine the final value for  -pi * cotan(pi*x).
#
      n = ( ( nq + 1 ) // 2 )
      if ( ( n % 2 ) == 0 ):
#
#  Check for singularity.
#
        if ( z == 0.0 ):

          if ( 0.0 < x ):
            value = - xinf
          else:
            value = xinf

          return value

        aug = sgn * ( 4.0 / np.tan ( z ) )

      else:

        aug = sgn * ( 4.0 * np.tan ( z ) )

    x = 1.0 - x
#
#  0.5 <= X <= 3.0.
#
  if ( x <= 3.0 ):

    den = x
    upper = p1[0] * x
    for i in range ( 0, 7 ):
      den = ( den + q1[i] ) * x
      upper = ( upper + p1[i+1] ) * x

    den = ( upper + p1[8] ) / ( den + q1[7] )
    x = ( x - x01 / x01d ) - x02
    value = den * x + aug
    return value
#
#  3.0 < X.
#
  if ( x < xlarge ):
    w = 1.0 / ( x * x )
    den = w
    upper = p2[0] * w
    for i in range ( 0, 5 ):
      den = ( den + q2[i] ) * w
      upper = ( upper + p2[i+1] ) * w
    aug = ( upper + p2[6] ) / ( den + q2[5] ) - 0.5 / x + aug

  value = aug + np.log ( x )

  return value

def r8_psi_test ( ):

#*****************************************************************************80
#
## r8_psi_test() tests r8_psi().
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
  import platform

  print ( '' )
  print ( 'r8_psi_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_psi evaluates the PSI function.' )
  print ( '' )
  print ( '      X            PSI(X)    r8_psi(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_psi ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_psi_test' )
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
  print ( 'r8vec_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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

def r8vec_reverse ( n, a1 ):

#*****************************************************************************80
#
## r8vec_reverse() reverses the elements of an R8VEC.
#
#  Example:
#
#    Input:
#
#      N = 5, A = ( 11.0, 12.0, 13.0, 14.0, 15.0 ).
#
#    Output:
#
#      A = ( 15.0, 14.0, 13.0, 12.0, 11.0 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    real A1(N), the array to be reversed.
#
#  Output:
#
#    real A2(N), the reversed array.
#
  import numpy as np

  a2 = np.zeros ( n )
  for i in range ( 0, n ):
    a2[i] = a1[n-1-i]

  return a2

def r8vec_reverse_test ( ):

#*****************************************************************************80
#
## r8vec_reverse_test() tests r8vec_reverse().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8vec_reverse_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_reverse reverses an R8VEC.' )
 
  a1 = np.zeros ( n )
  for i in range ( 0, n ):
    a1[i] = float ( i + 1 )
 
  r8vec_print ( n, a1, '  Original array:' )

  a2 = r8vec_reverse ( n, a1 )

  r8vec_print ( n, a2, '  Reversed array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_reverse_test:' )
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
  gegenbauer_polynomial_test ( )
  timestamp ( )

