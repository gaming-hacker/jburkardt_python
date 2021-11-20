#! /usr/bin/env python3
#
def chebyshev1 ( n ):

#*****************************************************************************80
#
## chebyshev1() returns the Type 1 chebyshev points.
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
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the points.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = np.cos ( float ( 2 * i + 1 ) * np.pi / float ( 2 * n ) )

  return x

def chebyshev2 ( n ):

#*****************************************************************************80
#
## chebyshev2() returns the Type 2 chebyshev points.
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
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the points.
#
  import numpy as np

  x = np.zeros ( n )

  if ( 1 < n ):
    for i in range ( 0, n ):
      x[i] = np.cos ( float ( n - 1 - i ) * np.pi / float ( n - 1 ) )

  return x

def chebyshev3 ( n ):

#*****************************************************************************80
#
## chebyshev3() returns the Type 3 chebyshev points.
#
#  Discussion:
#
#    Note that this point set is NOT symmetric in [-1,+1].
#    It is sometimes augmented by the value -1.
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
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the points.
#
  import numpy as np

  angle = np.zeros ( n )

  for i in range ( 0, n ):
    angle[i] = ( 2 * n - 2 * i - 1 ) * np.pi / float ( 2 * n + 1 )

  x = np.cos ( angle )

  return x

def chebyshev4 ( n ):

#*****************************************************************************80
#
## chebyshev4() returns the Type 4 chebyshev points.
#
#  Discussion:
#
#    Note that this point set is NOT symmetric in [-1,+1].
#    It is sometimes augmented by the value +1.
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
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the points.
#
  import numpy as np

  angle = np.zeros ( n )

  for i in range ( 0, n ):
    angle[i] = float ( 2 * ( n - i ) ) * np.pi / float ( 2 * n + 1 )

  x = np.cos ( angle )

  return x

def equidistant1 ( n ):

#*****************************************************************************80
#
## equidistant1() returns the Type 1 equidistant points.
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
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the points.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = float ( 1 - n + 2 * i ) / float ( n + 1 )

  return x

def equidistant2 ( n ):

#*****************************************************************************80
#
## equidistant2() returns the Type 2 equidistant points.
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
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the points.
#
  import numpy as np

  x = np.zeros ( n )

  if ( 1 < n ):
    for i in range ( 0, n ):
      x[i] = float ( 1 - n + 2 * i ) / float ( n - 1 )

  return x

def equidistant3 ( n ):

#*****************************************************************************80
#
## equidistant3() returns the Type 3 equidistant points.
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
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the points.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = float ( 1 - n + 2 * i ) / float ( n )

  return x

def fejer1 ( n ):

#*****************************************************************************80
#
## fejer1() returns the Type 1 Fejer points.
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
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the points.
#
  import numpy as np

  theta = np.zeros ( n )

  for i in range ( 0, n ):
    theta[i] = float ( 2 * n - 1 - 2 * i ) * np.pi / float ( 2 * n )

  x = np.cos ( theta )

  return x

def fejer2 ( n ):

#*****************************************************************************80
#
## fejer2() returns the Type 2 Fejer points.
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
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the points.
#
  import numpy as np

  theta = np.zeros ( n )

  for i in range ( 0, n ):
    theta[i] = float ( n - i ) * np.pi / float ( n + 1 )

  x = np.cos ( theta )

  return x

def lagrange_value ( data_num, t_data, interp_num, t_interp ):

#*****************************************************************************80
#
## lagrange_value() evaluates the Lagrange polynomials.
#
#  Discussion:
#
#    Given DATA_NUM distinct abscissas, T_DATA(1:DATA_NUM),
#    the I-th Lagrange polynomial L(I)(T) is defined as the polynomial of
#    degree DATA_NUM - 1 which is 1 at T_DATA(I) and 0 at the DATA_NUM - 1
#    other abscissas.
#
#    A formal representation is:
#
#      L(I)(T) = Product ( 1 <= J <= DATA_NUM, I /= J )
#       ( T - T(J) ) / ( T(I) - T(J) )
#
#    This routine accepts a set of INTERP_NUM values at which all the Lagrange
#    polynomials should be evaluated.
#
#    Given data values P_DATA at each of the abscissas, the value of the
#    Lagrange interpolating polynomial at each of the interpolation points
#    is then simple to compute by matrix multiplication:
#
#      P_INTERP(1:INTERP_NUM) =
#        P_DATA(1:DATA_NUM) * L_INTERP(1:DATA_NUM,1:INTERP_NUM)
#
#    or, in the case where P is multidimensional:
#      P_INTERP(1:M,1:INTERP_NUM) =
#        P_DATA(1:M,1:DATA_NUM) * L_INTERP(1:DATA_NUM,1:INTERP_NUM)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DATA_NUM, the number of data points.
#    DATA_NUM must be at least 1.
#
#    real T_DATA(DATA_NUM), the data points.
#
#    integer INTERP_NUM, the number of
#    interpolation points.
#
#    real T_INTERP(INTERP_NUM), the
#    interpolation points.
#
#  Output:
#
#    real L_INTERP(DATA_NUM,INTERP_NUM), the values
#    of the Lagrange polynomials at the interpolation points.
#
  import numpy as np
#
#  Evaluate the polynomial.
#
  l_interp = np.ones ( [ data_num, interp_num ] )

  for i in range ( 0, data_num ):

    for j in range ( 0, data_num ):

      if ( j != i ):

        for k in range ( 0, interp_num ):

          l_interp[i,k] = l_interp[i,k] \
            * ( t_interp[k] - t_data[j] ) / ( t_data[i] - t_data[j] )

  return l_interp

def lebesgue_chebyshev1_test ( ):

#*****************************************************************************80
#
## lebesgue_chebyshev1_test() looks at chebyshev1 points.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lebesgue_chebyshev1_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Analyze chebyshev1 points.' )

  nfun = 501
  xfun = np.linspace ( -1.0, +1.0, nfun )

  n_max = 21
  l = np.zeros ( n_max )
  for n in range ( 1, n_max + 1 ):
    x = chebyshev1 ( n )
    l[n-1] = lebesgue_constant ( n, x, nfun, xfun )

  r8vec_print ( n_max, l, '  chebyshev1 lebesgue constants:' )

  l2 = np.zeros ( n )
  for n in range ( 1, n_max + 1 ):
    l2[n-1] = l[n-1] / np.log ( n + 1 )

  r8vec_print ( n_max, l2, '  chebyshev1 lebesgue constants/log(N+1):' )
#
#  Examine one case more closely.
#
  n = 11
  x = chebyshev1 ( n )
  r8vec_print ( n, x, '  chebyshev1 points for N = 11' )

  label = 'chebyshev1 points for N = 11'
  filename = 'chebyshev1.png'
  lebesgue_plot ( n, x, nfun, xfun, label, filename )
  print ( '' )
  print ( '  Plot file saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lebesgue_chebyshev1_test' )
  print ( '  Normal end of execution.' )
  return

def lebesgue_chebyshev2_test ( ):

#*****************************************************************************80
#
## lebesgue_chebyshev2_test() looks at chebyshev2 points.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lebesgue_chebyshev2_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Analyze chebyshev2 points.' )

  nfun = 501
  xfun = np.linspace ( -1.0, +1.0, nfun )

  n_max = 11
  l = np.zeros ( n_max )
  for n in range ( 1, n_max + 1 ):
    x = chebyshev2 ( n )
    l[n-1] = lebesgue_constant ( n, x, nfun, xfun )

  r8vec_print ( n_max, l, '  chebyshev2 lebesgue constants for N = 1 to 11:' )

  l2 = np.zeros ( n )
  for n in range ( 1, n_max + 1 ):
    l2[n-1] = l[n-1] / np.log ( n + 1 )

  r8vec_print ( n_max, l2, '  chebyshev2 lebesgue constants/log(N+1):' )
#
#  Examine one case more closely.
#
  n = 11
  x = chebyshev2 ( n )
  r8vec_print ( n, x, '  chebyshev2 points for N = 11' )

  label = 'chebyshev2 points for N = 11'
  filename = 'chebyshev2.png'
  lebesgue_plot ( n, x, nfun, xfun, label, filename )
  print ( '' )
  print ( '  Plot file saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lebesgue_chebyshev2_test' )
  print ( '  Normal end of execution.' )
  return

def lebesgue_chebyshev3_test ( ):

#*****************************************************************************80
#
## lebesgue_chebyshev3_test() looks at chebyshev3 points.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lebesgue_chebyshev3_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Analyze chebyshev3 points.' )

  nfun = 501
  xfun = np.linspace ( -1.0, +1.0, nfun )

  n_max = 11
  l = np.zeros ( n_max )
  for n in range ( 1, n_max + 1 ):
    x = chebyshev3 ( n )
    l[n-1] = lebesgue_constant ( n, x, nfun, xfun )

  r8vec_print ( n_max, l, '  chebyshev3 lebesgue constants for N = 1 to 11:' )

  l2 = np.zeros ( n )
  for n in range ( 1, n_max + 1 ):
    l2[n-1] = l[n-1] / np.log ( n + 1 )

  r8vec_print ( n_max, l2, '  chebyshev3 lebesgue constants/log(N+1):' )
#
#  Examine one case more closely.
#
  n = 11
  x = chebyshev3 ( n )
  r8vec_print ( n, x, '  chebyshev3 points for N = 11' )

  label = 'chebyshev3 points for N = 11'
  filename = 'chebyshev3.png'
  lebesgue_plot ( n, x, nfun, xfun, label, filename )
  print ( '' )
  print ( '  Plot file saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lebesgue_chebyshev3_test' )
  print ( '  Normal end of execution.' )
  return

def lebesgue_chebyshev4_test ( ):

#*****************************************************************************80
#
## lebesgue_chebyshev4_test() looks at chebyshev4 points.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lebesgue_chebyshev4_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Analyze chebyshev4 points.' )

  nfun = 501
  xfun = np.linspace ( -1.0, +1.0, nfun )

  n_max = 11
  l = np.zeros ( n_max )
  for n in range ( 1, n_max + 1 ):
    x = chebyshev4 ( n )
    l[n-1] = lebesgue_constant ( n, x, nfun, xfun )

  r8vec_print ( n_max, l, '  chebyshev4 lebesgue constants for N = 1 to 11:' )

  l2 = np.zeros ( n )
  for n in range ( 1, n_max + 1 ):
    l2[n-1] = l[n-1] / np.log ( n + 1 )

  r8vec_print ( n_max, l2, '  chebyshev4 lebesgue constants/log(N+1):' )
#
#  Examine one case more closely.
#
  n = 11
  x = chebyshev4 ( n )
  r8vec_print ( n, x, '  chebyshev4 points for N = 11' )

  label = 'chebyshev4 points for N = 11'
  filename = 'chebyshev4.png'
  lebesgue_plot ( n, x, nfun, xfun, label, filename )
  print ( '' )
  print ( '  Plot file saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lebesgue_chebyshev4_test' )
  print ( '  Normal end of execution.' )
  return

def lebesgue_constant ( n, x, nfun, xfun ):

#*****************************************************************************80
#
## lebesgue_constant() estimates the lebesgue constant for a set of points.
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
#    John Burkardt.
#
#  Input:
#
#    Jean-Paul Berrut, Lloyd Trefethen,
#    Barycentric Lagrange Interpolation,
#    SIAM Review,
#    Volume 46, Number 3, September 2004, pages 501-517.
#
#  Input:
#
#    integer N, the number of interpolation points.
#
#    real X(N), the interpolation points.
#
#    integer NFUN, the number of evaluation points.
#
#    real XFUN(CONSTANT), the evaluation points.
#
#  Output:
#
#    real LMAX, an estimate of the lebesgue constant for the points.
#
  import numpy as np

  lfun = lebesgue_function ( n, x, nfun, xfun )

  lmax = np.max ( lfun )

  return lmax
  
def lebesgue_equidistant1_test ( ):

#*****************************************************************************80
#
## lebesgue_equidistant1_test() looks at equidistant1 points.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lebesgue_equidistant1_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Analyze equidistant1 points.' )

  nfun = 501
  xfun = np.linspace ( -1.0, +1.0, nfun )

  n_max = 11
  l = np.zeros ( n_max )
  for n in range ( 1, n_max + 1 ):
    x = equidistant1 ( n )
    l[n-1] = lebesgue_constant ( n, x, nfun, xfun )

  r8vec_print ( n_max, l, '  equidistant1 lebesgue constants for N = 1 to 11:' )
#
#  Examine one case more closely.
#
  n = 11
  x = equidistant1 ( n )
  r8vec_print ( n, x, '  equidistant1 points for N = 11' )

  label = 'equidistant1 points for N = 11'
  filename = 'equidistant1.png'
  lebesgue_plot ( n, x, nfun, xfun, label, filename )
  print ( '' )
  print ( '  Plot file saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lebesgue_equidistant1_test' )
  print ( '  Normal end of execution.' )
  return

def lebesgue_equidistant2_test ( ):

#*****************************************************************************80
#
## lebesgue_equidistant2_test() looks at equidistant2 points.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lebesgue_equidistant2_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Analyze equidistant2 points.' )

  nfun = 501
  xfun = np.linspace ( -1.0, +1.0, nfun )

  n_max = 11
  l = np.zeros ( n_max )
  for n in range ( 1, n_max + 1 ):
    x = equidistant2 ( n )
    l[n-1] = lebesgue_constant ( n, x, nfun, xfun )

  r8vec_print ( n_max, l, '  equidistant2 lebesgue constants for N = 1 to 11:' )
#
#  Examine one case more closely.
#
  n = 11
  x = equidistant2 ( n )
  r8vec_print ( n, x, '  equidistant2 points for N = 11' )

  label = 'equidistant2 points for N = 11'
  filename = 'equidistant2.png'
  lebesgue_plot ( n, x, nfun, xfun, label, filename )
  print ( '' )
  print ( '  Plot file saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lebesgue_equidistant2_test' )
  print ( '  Normal end of execution.' )
  return

def lebesgue_equidistant3_test ( ):

#*****************************************************************************80
#
## lebesgue_equidistant3_test() looks at equidistant3 points.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lebesgue_equidistant3_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Analyze equidistant3 points.' )

  nfun = 501
  xfun = np.linspace ( -1.0, +1.0, nfun )

  n_max = 11
  l = np.zeros ( n_max )
  for n in range ( 1, n_max + 1 ):
    x = equidistant3 ( n )
    l[n-1] = lebesgue_constant ( n, x, nfun, xfun )

  r8vec_print ( n_max, l, '  equidistant3 lebesgue constants for N = 1 to 11:' )
#
#  Examine one case more closely.
#
  n = 11
  x = equidistant3 ( n )
  r8vec_print ( n, x, '  equidistant3 points for N = 11' )

  label = 'equidistant3 points for N = 11'
  filename = 'equidistant3.png'
  lebesgue_plot ( n, x, nfun, xfun, label, filename )
  print ( '' )
  print ( '  Plot file saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lebesgue_equidistant3_test' )
  print ( '  Normal end of execution.' )
  return

def lebesgue_fejer1_test ( ):

#*****************************************************************************80
#
## lebesgue_fejer1_test() looks at Fejer 1 points.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lebesgue_fejer1_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Analyze Fejer1 points.' )

  nfun = 501
  xfun = np.linspace ( -1.0, +1.0, nfun )

  n_max = 11
  l = np.zeros ( n_max )
  for n in range ( 1, n_max + 1 ):
    x = fejer1 ( n )
    l[n-1] = lebesgue_constant ( n, x, nfun, xfun )

  r8vec_print ( n_max, l, '  Fejer1 lebesgue constants for N = 1 to 11:' )
#
#  Examine one case more closely.
#
  n = 11
  x = fejer1 ( n )
  r8vec_print ( n, x, '  Fejer1 points for N = 11' )

  label = 'Fejer1 points for N = 11'
  filename = 'fejer1.png'
  lebesgue_plot ( n, x, nfun, xfun, label, filename )
  print ( '' )
  print ( '  Plot file saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lebesgue_fejer1_test' )
  print ( '  Normal end of execution.' )
  return

def lebesgue_fejer2_test ( ):

#*****************************************************************************80
#
## lebesgue_fejer2_test() looks at Fejer2 points.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lebesgue_fejer2_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Analyze Fejer2 points.' )

  nfun = 501
  xfun = np.linspace ( -1.0, +1.0, nfun )

  n_max = 11
  l = np.zeros ( n_max )
  for n in range ( 1, n_max + 1 ):
    x = fejer2 ( n )
    l[n-1] = lebesgue_constant ( n, x, nfun, xfun )

  r8vec_print ( n_max, l, '  Fejer2 lebesgue constants for N = 1 to 11:' )
#
#  Examine one case more closely.
#
  n = 11
  x = fejer2 ( n )
  r8vec_print ( n, x, '  Fejer2 points for N = 11' )

  label = 'Fejer2 points for N = 11'
  filename = 'fejer2.png'
  lebesgue_plot ( n, x, nfun, xfun, label, filename )
  print ( '' )
  print ( '  Plot file saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lebesgue_fejer2_test' )
  print ( '  Normal end of execution.' )
  return

def lebesgue_function ( n, x, nfun, xfun ):

#*****************************************************************************80
#
## lebesgue_function() evaluates the lebesgue function for a set of points.
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
#    John Burkardt.
#
#  Input:
#
#    Jean-Paul Berrut, Lloyd Trefethen,
#    Barycentric Lagrange Interpolation,
#    SIAM Review,
#    Volume 46, Number 3, September 2004, pages 501-517.
#
#  Input:
#
#    integer N, the number of interpolation points.
#
#    real X(N), the interpolation points.
#
#    integer NFUN, the number of evaluation points.
#
#    real XFUN(NFUN), the evaluation points.
#
#  Output:
#
#    real LFUN(NFUN), the lebesgue function evaluated at XFUN.
#
  import numpy as np
#
#  Handle special case.
#
  if ( n == 1 ):

    lfun = np.ones ( nfun )

  else:

    llfun = lagrange_value ( n, x, nfun, xfun ) 

    lfun = np.zeros ( nfun )

    for j in range ( 0, nfun ):
      t = 0.0
      for i in range ( 0, n ):
        t = t + abs ( llfun[i,j] )
      lfun[j] = t

  return lfun

def lebesgue_plot ( n, x, nfun, xfun, label, filename ):

#*****************************************************************************80
#
## lebesgue_plot() plots the lebesgue function for a set of points.
#
#  Discussion:
#
#    The interpolation interval is assumed to be [min(XFUN), max(XFUN)].
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
#    John Burkardt.
#
#  Input:
#
#    Jean-Paul Berrut, Lloyd Trefethen,
#    Barycentric Lagrange Interpolation,
#    SIAM Review,
#    Volume 46, Number 3, September 2004, pages 501-517.
#
#  Input:
#
#    integer N, the number of interpolation points.
#
#    real X(N), the interpolation points.
#
#    integer NFUN, the number of evaluation points.
#
#    real XFUN(NFUN), the evaluation points.  
#
#    string LABEL, a title for the plot.
#
#    string FILENAME, a filename in which to save the plot.
#
  import matplotlib.pyplot as plt
  import numpy as np

  lfun = lebesgue_function ( n, x, nfun, xfun )

  plt.plot ( xfun, lfun, linewidth = 2 )

  ymax = np.ceil ( np.max ( lfun ) ) + 1

  xmin = np.min ( xfun )
  xmax = np.max ( xfun )

  plt.axis ( [ xmin, xmax, 0.0, ymax ] )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- lebesgue(X) --->' )
  plt.title ( label )

  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  return

def lebesgue_test ( ):

#*****************************************************************************80
#
## lebesgue_test() tests lebesgue().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2021
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'lebesgue_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test lebesgue()' )

  lebesgue_chebyshev1_test ( )
  lebesgue_chebyshev2_test ( )
  lebesgue_chebyshev3_test ( )
  lebesgue_chebyshev4_test ( )
  lebesgue_equidistant1_test ( )
  lebesgue_equidistant2_test ( )
  lebesgue_equidistant3_test ( )
  lebesgue_fejer1_test ( )
  lebesgue_fejer2_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lebesgue_test:' )
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
  print ( 'R8VEC_PRINT_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_test:' )
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
  lebesgue_test ( )
  timestamp ( )

