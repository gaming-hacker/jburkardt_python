#! /usr/bin/env python3
#
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

  prec = np.finfo(float).eps

  e[n-1] = 0.0

  for l in range ( 1, n + 1 ):

    j = 0

    while ( True ):

      for m in range ( l, n + 1 ):

        if ( m == n ):
          break

        if ( abs ( e[m-1] ) <= prec * ( abs ( lam[m-1] ) + abs ( lam[m] ) ) ):
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
## imtqlx_test tests imtqlx.
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

def parchk ( kind, m, alpha, beta ):

#*****************************************************************************80
#
## parchk() checks parameters ALPHA and BETA for classical weight functions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2010
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    MATLAB version by John Burkardt.
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
#    integer KIND, the rule.
#    1, Legendre,             (a,b)       1.0
#    2, Chebyshev Type 1,     (a,b)       ((b-x)*(x-a))^(-0.5)
#    3, Gegenbauer,           (a,b)       ((b-x)*(x-a))^alpha
#    4, Jacobi,               (a,b)       (b-x)^alpha*(x-a)^beta
#    5, Generalized Laguerre, (a,+oo)     (x-a)^alpha*exp(-b*(x-a))
#    6, Generalized Hermite,  (-oo,+oo)   |x-a|^alpha*exp(-b*(x-a)^2)
#    7, Exponential,          (a,b)       |x-(a+b)/2.0|^alpha
#    8, Rational,             (a,+oo)     (x-a)^alpha*(x+b)^beta
#    9, Chebyshev Type 2,     (a,b)       ((b-x)*(x-a))^(+0.5)
#
#    integer M, the order of the highest moment to
#    be calculated.  This value is only needed when KIND = 8.
#
#    real ALPHA, BETA, the parameters, if required
#    by the value of KIND.
#
#  Output:
#
#    bool CHECK, is TRUE if the variables are OK.
#
  check = True

  if ( kind < 1 ):
    check = False
    print ( '' )
    print ( 'parchk - Fatal error!' )
    print ( '  kind < 1.' )
    print ( '  kind = ', kind )
    raise Exception ( 'parchk - Fatal error!' )

  if ( 9 < kind ):
    check = False
    print ( '' )
    print ( 'parchk - Fatal error!' )
    print ( '  9 < KIND.' )
    raise Exception ( 'parchk - Fatal error!' )
#
#  Check ALPHA for Gegenbauer, Jacobi, Laguerre, Hermite, Exponential.
#
  if ( 3 <= kind and kind <= 8 and alpha <= -1.0 ):
    check = False
    print ( '' )
    print ( 'parchk - Fatal error!' )
    print ( '  ( 3 <= KIND <= 8 ) and ALPHA <= -1.' )
    raise Exception ( 'parchk - Fatal error!' )
#
#  Check BETA for Jacobi.
#
  if ( kind == 4 and beta <= -1.0 ):
    check = False
    print ( '' )
    print ( 'parchk - Fatal error!' )
    print ( '  KIND == 4 and BETA <= -1.0.' )
    raise Exception ( 'parchk - Fatal error!' )
#
#  Check ALPHA and BETA for rational.
#
  if ( kind == 8 ):
    if ( 0.0 <= alpha + beta + m + 1.0 ):
      check = False
      print ( '' )
      print ( 'parchk - Fatal error!' )
      print ( '  KIND == 8 but 0 <= ALPHA + BETA + M + 1.' )
      raise Exception ( 'parchk - Fatal error!' )
    if ( alpha + m + 1.0 <= 0.0 ):
      check = False
      print ( '' )
      print ( 'parchk - Fatal error!' )
      print ( '  KIND == 8 but ALPHA + M + 1.0 <= 0.0.' )
      raise Exception ( 'parchk - Fatal error!' )

  return check

def parchk_test ( ):

#*****************************************************************************80
#
## parchk_test tests parchk.
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
#    John Burkardt.
#
  import numpy as np
  import platform

  test_num = 18

  kind_vec  = np.array ( [  \
    0, \
    1, \
    2, \
    3, 3, \
    4, 4, 4, \
    5, 5, \
    6, 6, \
    7, 7, \
    8, 8, 8, \
    9 ] )
  m_vec = np.array ( [ \
    0, \
    0, \
    0, \
    0, 0, \
    0, 0, 0, \
    0, 0, \
    0, 0, \
    0, 0, \
    3, 3, 3, \
    0 ] )
  alpha_vec = np.array ( [ \
    0.5, \
    0.5, \
    0.5, \
   -0.5, -1.5, \
   -0.5, -1.5, 0.5, \
   -0.5, -1.5, \
   -0.5, -1.5, \
   -0.5, -1.5, \
   -2.0, -0.5, -0.5, \
    0.5, ] )
  beta_vec  = np.array ( [ \
    0.5, \
    0.5, \
    0.5, \
    0.5,  0.5, \
    0.5,  0.5, -2.0, \
    0.5,  0.5, \
    0.5,  0.5, \
    0.5,  0.5, \
   -3.0, -4.0, -3.0, \
    0.5, ] )

  print ( '' )
  print ( 'parchk_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  parchk checks quadrature rule parameters.' )
  print ( '' )
  print ( '  KIND   M           ALPHA            BETA  CHECK?' )
  print ( '' )

  for test in range ( 0, test_num ):

    kind = kind_vec[test]
    m = m_vec[test]
    alpha = alpha_vec[test]
    beta = beta_vec[test]

    try:
      check = parchk ( kind, m, alpha, beta )
      print ( '     %1d  %2d  %14.6g  %14.6g  %s' % ( kind, m, alpha, beta, check ) )
    except:
      print ( '     %1d  %2d  %14.6g  %14.6g  FAILED' % ( kind, m, alpha, beta ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'parchk_test():' )
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
## r8vec_print_test tests r8vec_print.
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

def toms655_test ( ):

#*****************************************************************************80
#
## toms655_test() tests toms655().
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
  import platform

  print ( '' )
  print ( 'toms655_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test toms655().' )

  imtqlx_test ( )

  parchk_test ( )

  wm_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'toms655_test():' )
  print ( '  Normal end of execution.' )
  return

def wm ( m, kind, alpha, beta ):

#*****************************************************************************80
#
## wm evaluates the first M moments of classical weight functions.
#
#  Discussion:
#
#    W(K) = Integral ( A <= X <= B ) X^(K-1) * W(X) dx
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
#    integer M, the number of moments to evaluate.
#
#    integer KIND, the rule.
#    1, Legendre,             (a,b)       1.0
#    2, Chebyshev Type 1,     (a,b)       ((b-x)*(x-a))^(-0.5)
#    3, Gegenbauer,           (a,b)       ((b-x)*(x-a))^alpha
#    4, Jacobi,               (a,b)       (b-x)^alpha*(x-a)^beta
#    5, Generalized Laguerre, (a,+oo)     (x-a)^alpha*exp(-b*(x-a))
#    6, Generalized Hermite,  (-oo,+oo)   |x-a|^alpha*exp(-b*(x-a)^2)
#    7, Exponential,          (a,b)       |x-(a+b)/2.0|^alpha
#    8, Rational,             (a,+oo)     (x-a)^alpha*(x+b)^beta
#    9, Chebyshev Type 2,     (a,b)       ((b-x)*(x-a))^(+0.5)
#
#    real ALPHA, the value of Alpha, if needed.
#
#    real BETA, the value of Beta, if needed.
#
#  Output:
#
#    real W(M), the first M moments.
#
  from scipy.special import gamma
  import numpy as np

  parchk ( kind, m, alpha, beta )

  w = np.zeros ( m )

  if ( kind == 1 ):

    for k in range ( 0, m, 2 ):
      w[k] = 2.0 / float ( k + 1 )

  elif ( kind == 2 ):

    w[0] = np.pi
    for k in range ( 2, m, 2 ):
      w[k] = w[k-2] * float ( k - 1 ) / float ( k )

  elif ( kind == 3 ):

    w[0] = np.sqrt ( np.pi ) * gamma ( alpha + 1.0 ) \
      / gamma ( alpha + 3.0 / 2.0 )

    for k in range ( 2, m, 2 ):
      w[k] = w[k-2] * float ( k - 1.0 ) / ( 2.0 * alpha + k + 1 )

  elif ( kind == 4 ):

    als = alpha + beta + 1.0
    w[0] = 2.0 ** als * gamma ( alpha + 1.0 ) \
      / gamma ( als + 1.0 ) * gamma ( beta + 1.0 )

    for k in range ( 1, m ):

      sum = 0.0
      trm = 1.0

      for i in range ( 0, ( k - 1 ) // 2 + 1 ):

        tmpa = trm
        for ja in range ( 1, 2 * i + 1 ):
          tmpa = tmpa * ( alpha + ja ) / ( als + ja )

        for jb in range ( 1, k + 1 - 2 * i ):
          tmpa = tmpa * ( beta + jb ) / ( als + 2 * i + jb )

        tmpa = tmpa / ( 2 * i + 1.0 ) * \
          ( 2 * i * ( beta + alpha ) + beta - k * alpha ) \
          / ( beta + k + 1 - 2 * i - 1.0 )
        sum = sum + tmpa

        trm = trm * ( k - 2 * i ) \
          / ( 2 * i + 1.0 ) * ( k - 2 * i - 1.0 ) / ( 2 * i + 2.0 )

      if ( ( k % 2 ) == 0 ):
        tmpb = 1.0
        for i in range ( 0, k ):
          tmpb = tmpb * ( alpha + i + 1 ) / ( als + i + 1 )
        sum = sum + tmpb

      w[k] = sum * w[0]

  elif ( kind == 5 ):

    w[0] = gamma ( alpha + 1.0 )

    for k in range ( 1, m ):
      w[k] = ( alpha + k ) * w[k-1]

  elif ( kind == 6 ):

    w[0] = gamma ( ( alpha + 1.0 ) / 2.0 )

    for k in range ( 2, m, 2 ):
      w[k] = w[k-2] * ( alpha + k - 1.0 ) / 2.0

  elif ( kind == 7 ):

    als = alpha
    for k in range ( 0, m, 2 ):
      w[k] = 2.0 / ( k + 1 + als )

  elif ( kind == 8 ):

    w[0] = gamma ( alpha + 1.0 ) \
      * gamma ( - alpha - beta - 1.0 ) \
      / gamma ( - beta )

    for k in range ( 1, m ):
      w[k] = - w[k-1] * ( alpha + k ) / ( alpha + beta + k + 1 )

  elif ( kind == 9 ):

    w[0] = np.pi / 2.0
    for k in range ( 2, m, 2 ):
      w[k] = w[k-2] * float ( k - 1.0 ) / float ( k + 2.0 )

  return w

def wm_test ( ):

#*****************************************************************************80
#
## wm_test calls wm_tester with various parameter values.
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
#    John Burkardt.
#
  m = 5
  kind = 1
  alpha = 0.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 2
  alpha = 0.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 3
  alpha = 0.5
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 4
  alpha = 0.25
  beta = 0.75
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 5
  alpha = 2.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 6
  alpha = 1.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 7
  alpha = 2.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 8
  alpha = -0.5
  beta = -6.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 9
  alpha = 0.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )
#
#  Terminate.
#
  print ( '' )
  print ( 'wm_test' )
  print ( '  Normal end of execution.' )
  return

def wm_tester ( m, kind, alpha, beta ):

#*****************************************************************************80
#
## wm_tester() tests wm().
#
#  Discussion:
#
#    Moment(K) = Integral ( A <= X <= B ) X^(K-1) * W(X) dx
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
#  Input:
#
#    integer M, the number of moments to evaluate.
#
#    integer KIND, the rule.
#    1, Legendre,             (a,b)       1.0
#    2, Chebyshev Type 1,     (a,b)       ((b-x)*(x-a))^(-0.5)
#    3, Gegenbauer,           (a,b)       ((b-x)*(x-a))^alpha
#    4, Jacobi,               (a,b)       (b-x)^alpha*(x-a)^beta
#    5, Generalized Laguerre, (a,+oo)     (x-a)^alpha*exp(-b*(x-a))
#    6, Generalized Hermite,  (-oo,+oo)   |x-a|^alpha*exp(-b*(x-a)^2)
#    7, Exponential,          (a,b)       |x-(a+b)/2.0|^alpha
#    8, Rational,             (a,+oo)     (x-a)^alpha*(x+b)^beta
#    9, Chebyshev Type 2,     (a,b)       ((b-x)*(x-a))^(+0.5)
#
#    real ALPHA, the value of Alpha, if needed.
#
#    real BETA, the value of Beta, if needed.
#
  import platform

  w = wm ( m, kind, alpha, beta )

  print ( '' )
  print ( 'wm_tester:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  wm_test computes moments for rule %d' % ( kind ) )
  print ( '  with ALPHA = %g, BETA = %g' % ( alpha, beta ) )
  print ( '' )
  print ( '  Order          Moment' )
  print ( '' )
  for i in range ( 0, m ):
    print ( '     %2d  %14.6g' % ( i, w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'wm_tester:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  toms655_test ( )
  timestamp ( )
