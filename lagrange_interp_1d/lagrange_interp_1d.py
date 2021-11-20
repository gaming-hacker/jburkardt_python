#! /usr/bin/env python3
#
def lagrange_basis_1d ( nd, xd, ni, xi ):

#*****************************************************************************80
#
## lagrange_basis_1d() evaluates a 1D Lagrange basis.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ND, the number of data points.
#
#    real XD(ND,1), the interpolation nodes.
#
#    integer NI, the number of evaluation points.
#
#    real XI(NI,1), the evaluation points.
#
#  Output:
#
#    real LB(NI,ND), the value, at the I-th point XI, of the
#    Jth basis function.
#
  import numpy as np

  lb = np.zeros ( [ ni, nd ] )
  
  for i in range ( 0, ni ):
    for j in range ( 0, nd ):
      lb[i,j] = 1.0
      for k in range ( 0, nd ):
        if ( k != j ):
          lb[i,j] = lb[i,j] * ( xi[i] - xd[k]  ) / ( xd[j] - xd[k]  )

  return lb

def lagrange_basis_1d_test ( ):

#*****************************************************************************80
#
## lagrange_basis_1d_test() tests lagrange_basis_1d().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nd = 4
  ni = 21

  xd = np.array ( [ 0.0, 2.0, 5.0, 10.0 ] )
 
  print ( '' )
  print ( 'lagrange_basis_1d_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  lagrange_basis_1d evaluates the Lagrange 1D basis' )
  print ( '  functions.' )

  x_min = 0.0
  x_max = 10.0
  xi = np.linspace ( x_min, x_max, ni )

  lb = lagrange_basis_1d ( nd, xd, ni, xi )

  r8mat_print ( ni, nd, lb, '  The Lagrange basis functions:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'lagrange_basis_1d_test:' )
  print ( '  Normal end of execution.' )
  return

def lagrange_interp_1d_test ( ):

#*****************************************************************************80
#
## lagrange_interp_1d_test() tests lagrange_interp_1d().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'lagrange_interp_1d_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the lagrange_interp_1d library.' )
#
#  Utility functions.
#
  p00_prob_num_test ( )
  p00_title_test ( )
  p00_f_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8vec_cheby_extreme_test ( )
  r8vec_print_test ( )
  r8vec2_print_test ( )
#
#  Library functions.
#
  lagrange_basis_1d_test ( )
  lagrange_value_1d_test ( )

  prob_num = p00_prob_num ( );
  for prob in range ( 1, prob_num + 1 ):
    for nd in ( [ 4, 8, 16, 32, 64 ] ):
      lagrange_interp_1d_test01 ( prob, nd )

  prob_num = p00_prob_num ( );
  for prob in range ( 1, prob_num + 1 ):
    for nd in ( [ 4, 8, 16, 32, 64 ] ):
      lagrange_interp_1d_test02 ( prob, nd )
#
#  Terminate.
#
  print ( '' )
  print ( 'lagrange_interp_1d_test:' )
  print ( '  Normal end of execution.' )
  return

def lagrange_interp_1d_test01 ( prob, nd ):

#*****************************************************************************80
#
## lagrange_interp_1d_test01() tests lagrange_value_1d() with evenly spaced data
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer ND, the number of data points to use.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'lagrange_interp_1d_test01:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Interpolate data from TEST_interp_1d problem #%d.' % ( prob ) )
  print ( '  Use even spacing for data points.' )
  print ( '  Number of data points = %d' % ( nd ) )

  a = 0.0
  b = 1.0
  xd = np.linspace ( a, b, nd )

  yd = p00_f ( prob, nd, xd )

  if ( nd < 10 ):
    r8vec2_print ( nd, xd, yd, '  Data array:' )
#
#  #1:  Does interpolant match function at interpolation points?
#
  ni = nd
  xi = xd
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  int_error = np.linalg.norm ( yi - yd ) / float ( ni )

  print ( '' )
  print ( '  L2 interpolation error averaged per interpolant node = %g' % ( int_error ) )
#
#  #2: Compare estimated curve length to piecewise linear (minimal) curve length.
#  Assume data is sorted, and normalize X and Y dimensions by (XMAX-XMIN) and
#  (YMAX-YMIN).
#
  ymin = np.min ( yd )
  ymax = np.max ( yd )

  ni = 501
  xi = np.linspace ( a, b, ni )
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  ld = 0.0

  for i in range ( 0, nd - 1 ):
    ld = ld + ( ( xd[i+1] - xd[i] ) / ( b - a ) ) ** 2 \
            + ( ( yd[i+1] - yd[i] ) / ( ymax - ymin ) ) ** 2
  ld = np.sqrt ( ld )

  li = 0.0
  for i in range ( 0, ni - 1 ):
    li = li + ( ( xi[i+1] - xi[i] ) / ( b - a ) ) ** 2 \
            + ( ( yi[i+1] - yi[i] ) / ( ymax - ymin ) ) ** 2
  li = np.sqrt ( li )

  print ( '' )
  print ( '  Normalized length of piecewise linear interpolant = %g' % ( ld ) )
  print ( '  Normalized length of polynomial interpolant       = %g' % ( li ) )
#
#  #3: Plot the data.
#
  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xd, yd, 'ro', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Interpolation data at ' + str ( nd ) + ' even nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_dataeven_' + str ( nd ) + '.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '' )
  print ( '  Created plot file "%s"' % ( filename ) )
#
#  #4: Plot the piecewise linear and polynomial interpolants.
#
  ni = 501
  xi = np.linspace ( a, b, ni )
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xi, yi, 'r-', linewidth = 4.0 )
  plt.plot ( xd, yd, 'k.', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Lagrange/Even Polynomial Interpolant for ' + str ( nd ) + ' nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_lageven_' + str ( nd ) + '.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Created plot file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lagrange_interp_1d_test01:' )
  print ( '  Normal end of execution.' )
  return

def lagrange_interp_1d_test02 ( prob, nd ):

#*****************************************************************************80
#
## lagrange_interp_1d_test02() tests lagrange_value_1d() with Chebyshev spaced data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer ND, the number of data points to use.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'lagrange_interp_1d_test02:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Interpolate data from TEST_interp_1d problem #%d.' % ( prob ) )
  print ( '  Use Chebyshev spacing for data points.' )
  print ( '  Number of data points = %d' % ( nd ) )

  a = 0.0
  b = 1.0
  xd = r8vec_cheby_extreme ( nd, a, b )

  yd = p00_f ( prob, nd, xd )

  if ( nd < 10 ):
    r8vec2_print ( nd, xd, yd, '  Data array:' )
#
#  #1:  Does interpolant match function at interpolation points?
#
  ni = nd
  xi = xd
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  int_error = np.linalg.norm ( yi - yd ) / float ( ni )

  print ( '' )
  print ( '  L2 interpolation error averaged per interpolant node = %g' % ( int_error ) )
#
#  #2: Compare estimated curve length to piecewise linear (minimal) curve length.
#  Assume data is sorted, and normalize X and Y dimensions by (XMAX-XMIN) and
#  (YMAX-YMIN).
#
  ymin = np.min ( yd )
  ymax = np.max ( yd )

  ni = 501
  xi = np.linspace ( a, b, ni )
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  ld = 0.0

  for i in range ( 0, nd - 1 ):
    ld = ld + ( ( xd[i+1] - xd[i] ) / ( b - a ) ) ** 2 \
            + ( ( yd[i+1] - yd[i] ) / ( ymax - ymin ) ) ** 2
  ld = np.sqrt ( ld )

  li = 0.0
  for i in range ( 0, ni - 1 ):
    li = li + ( ( xi[i+1] - xi[i] ) / ( b - a ) ) ** 2 \
            + ( ( yi[i+1] - yi[i] ) / ( ymax - ymin ) ) ** 2
  li = np.sqrt ( li )

  print ( '' )
  print ( '  Normalized length of piecewise linear interpolant = %g' % ( ld ) )
  print ( '  Normalized length of polynomial interpolant       = %g' % ( li ) )
#
#  #3: Plot the data.
#
  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xd, yd, 'ro', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Interpolation data at ' + str ( nd ) + ' Chebyshev nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_datacheby_' + str ( nd ) + '.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '' )
  print ( '  Created plot file "%s"' % ( filename ) )
#
#  #4: Plot the piecewise linear and polynomial interpolants.
#
  ni = 501
  xi = np.linspace ( a, b, ni )
  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  plt.plot ( xd, yd, 'b-', linewidth = 3.0 )
  plt.plot ( xi, yi, 'r-', linewidth = 4.0 )
  plt.plot ( xd, yd, 'k.', markersize = 10 )
  t = 'p0' + str ( prob ) + ' Lagrange/Chebyshev Polynomial Interpolant for ' + str ( nd ) + ' nodes.'
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  filename = 'p0' + str ( prob ) + '_lagcheby_' + str ( nd ) + '.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Created plot file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lagrange_interp_1d_test02:' )
  print ( '  Normal end of execution.' )
  return

def lagrange_value_1d ( nd, xd, yd, ni, xi ):

#*****************************************************************************80
#
## lagrange_value_1d() evaluates the Lagrange interpolant.
#
#  Discussion:
#
#    The Lagrange interpolant L(ND,XD,YD)(X) is the unique polynomial of
#    degree ND-1 which interpolates the points (XD(I),YD(I)) for I = 1
#    to ND.
#
#    The Lagrange interpolant can be constructed from the Lagrange basis
#    polynomials.  Given ND distinct abscissas, XD(1:ND), the I-th Lagrange 
#    basis polynomial LB(ND,XD,I)(X) is defined as the polynomial of degree 
#    ND - 1 which is 1 at  XD(I) and 0 at the ND - 1 other abscissas.
#
#    Given data values YD at each of the abscissas, the value of the
#    Lagrange interpolant may be written as
#
#      L(ND,XD,YD)(X) = sum ( 1 <= I <= ND ) LB(ND,XD,I)(X) * YD(I)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ND, the number of data points.
#    ND must be at least 1.
#
#    real XD(ND,1), the data points.
#
#    real YD(ND,1), the data values.
#
#    integer NI, the number of interpolation points.
#
#    real XI(NI,1), the interpolation points.
#
#  Output:
#
#    real YI(NI,1), the interpolated values.
#
  import numpy as np

  lb = lagrange_basis_1d ( nd, xd, ni, xi )

  yi = np.dot ( lb, yd )

  return yi

def lagrange_value_1d_test ( ):

#*****************************************************************************80
#
## lagrange_value_1d_test() tests lagrange_value_1d().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nd = 4
  ni = 21
#
#  Values of f(x) = x^3 - 12 x^2 + 39 x -28 = ( x - 1 ) * ( x - 4 ) * ( x - 7 )
#
  xd = np.array ( [ 0.0, 2.0, 5.0, 10.0 ] )
  yd = np.array ( [ -28.0, +10.0, -8.0, +162.0 ] )
 
  print ( '' )
  print ( 'lagrange_value_1d_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  lagrange_value_1d evaluates a Lagrange 1D interpolant.' )

  x_min = 0.0
  x_max = 10.0
  xi = np.linspace ( x_min, x_max, ni )

  yi = lagrange_value_1d ( nd, xd, yd, ni, xi )

  r8vec2_print ( ni, xi, yi, '  Table of interpolant values:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'lagrange_value_1d_test:' )
  print ( '  Normal end of execution.' )
  return

def p00_f ( prob, n, x ):

#*****************************************************************************80
#
## p00_f() evaluates the function for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the desired test problem.
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real VALUE(N), the function values.
#
  if ( prob == 1 ):
    value = p01_f ( n, x )
  elif ( prob == 2 ):
    value = p02_f ( n, x )
  elif ( prob == 3 ):
    value = p03_f ( n, x )
  elif ( prob == 4 ):
    value = p04_f ( n, x )
  elif ( prob == 5 ):
    value = p05_f ( n, x )
  elif ( prob == 6 ):
    value = p06_f ( n, x )
  elif ( prob == 7 ):
    value = p07_f ( n, x )
  elif ( prob == 8 ):
    value = p08_f ( n, x )
  else:
    print ( '' )
    print ( 'p00_f - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_f - Fatal error!' )

  return value

def p01_f ( n, x ):

#*****************************************************************************80
#
## p01_f() evaluates the function for problem p01.
#
#  Discussion:
#
#    Step function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real VALUE(N), the function values.
#
  import numpy as np

  value = 2.0 * np.ones ( n )

  i = ( x <= 1.0 / 3.0 )
  j = ( 4.0 / 5.0 <= x )

  value[i] = -1.0
  value[j] = +1.0

  return value

def p02_f ( n, x ):

#*****************************************************************************80
#
## p02_f() evaluates the function for problem p02.
#
#  Discussion:
#
#    Nondifferentiable function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real VALUE(N), the function values.
#
  import numpy as np

  value = np.zeros ( n )

  i = ( x <= 1.0 / 3.0 )
  j = ( 1.0 / 3.0 < x )

  value[i] = 1.0 - 3.0 * x[i]
  value[j] = 6.0 * x[j] - 2.0

  return value

def p03_f ( n, x ):

#*****************************************************************************80
#
## p03_f() evaluates the function for problem p03.
#
#  Discussion:
#
#    Step function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real VALUE(N), the function values.
#
  import numpy as np

  value = x * ( 10.0 * x - 1.0 ) * ( 5.0 * x - 2.0 ) * ( 5.0 * x - 2.0 ) \
    * ( 4 * x - 3.4 ) * ( x - 1.0 )

  return value

def p04_f ( n, x ):

#*****************************************************************************80
#
## p04_f() evaluates the function for problem p04.
#
#  Discussion:
#
#    Step function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real VALUE(N), the function values.
#
  import numpy as np

  value = np.arctan ( 40.0 * x - 15.0 )

  return value

def p05_f ( n, x ):

#*****************************************************************************80
#
## p05_f() evaluates the function for problem p05.
#
#  Discussion:
#
#    Step function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real VALUE(N), the function values.
#
  import numpy as np

  value =       np.cos (  7.0 * x ) \
        + 5.0 * np.cos ( 11.2 * x ) \
        - 2.0 * np.cos ( 14.0 * x ) \
        + 5.0 * np.cos ( 31.5 * x ) \
        + 7.0 * np.cos ( 63.0 * x )

  return value

def p06_f ( n, x ):

#*****************************************************************************80
#
## p06_f() evaluates the function for problem p06.
#
#  Discussion:
#
#    f(x) = exp ( - (4 * x - 1)^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Genz,
#    A Package for Testing Multiple Integration Subroutines,
#    in Numerical Integration: Recent Developments, Software
#    and Applications,
#    edited by Patrick Keast and Graeme Fairweather,
#    D Reidel, 1987, pages 337-340,
#    LC: QA299.3.N38.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real VALUE(N), the function values.
#
  import numpy as np

  value = np.exp ( - ( 4.0 * x - 1.0 ) ** 2 )

  return value

def p07_f ( n, x ):

#*****************************************************************************80
#
## p07_f() evaluates the function for problem p07.
#
#  Discussion:
#
#    f(x) = exp ( 4 * x ) if x <= 1/2
#           0                  otherwise
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Genz,
#    A Package for Testing Multiple Integration Subroutines,
#    in Numerical Integration: Recent Developments, Software
#    and Applications,
#    edited by Patrick Keast and Graeme Fairweather,
#    D Reidel, 1987, pages 337-340,
#    LC: QA299.3.N38.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real VALUE(N), the function values.
#
  import numpy as np

  value = np.zeros ( n )

  i = ( x < 0.5 )

  value[i] = np.exp ( 4.0 * x[i] )

  return value

def p08_f ( n, x ):

#*****************************************************************************80
#
## p08_f() evaluates the function for problem p08.
#
#  Discussion:
#
#    This is a famous example, due to Runge.  If equally spaced
#    abscissas are used, the sequence of interpolating polynomials Pn(X)
#    diverges, in the sense that the max norm of the difference
#    between Pn(X) and F(X) becomes arbitrarily large as N increases.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real VALUE(N), the function values.
#
  import numpy as np

  value = 1.0 / ( ( 10.0 * ( x - 0.5 ) ) ** 2 + 1.0 )

  return value

def p00_f_test ( ):

#*****************************************************************************80
#
## p00_f_test tests p00_f.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'p00_f_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p00_f() evaluates any function at N points X.' )

  prob_num = p00_prob_num ( )

  n = 11
  a = 0.0
  b = 1.0
  x = np.linspace ( a, b, n )

  print ( '' )

  for prob in range ( 1, prob_num + 1 ):

    y = p00_f ( prob, n, x )
    title = 'X, Y for problem ' + str ( prob )
    r8vec2_print ( n, x, y, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'p00_f_test:' )
  print ( '  Normal end of execution.' )
  return

def p00_prob_num ( ):

#*****************************************************************************80
#
## p00_prob_num() returns the number of problems.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer VALUE, the number of problems.
#
  value = 8

  return value

def p00_prob_num_test ( ):

#*****************************************************************************80
#
## p00_prob_num_test() tests p00_prob_num().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'p00_prob_num_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p00_prob_num returns the number of test problems.' )

  num = p00_prob_num ( )
  print ( '' )
  print ( '  test_interp_1d includes %d test problems.' % ( num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'p00_prob_num_test:' )
  print ( '  Normal end of execution.' )
  return

def p00_title ( prob ):

#*****************************************************************************80
#
## p00_title() returns the title of any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the desired test problem.
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  if ( prob == 1 ):
    title = p01_title ( )
  elif ( prob == 2 ):
    title = p02_title ( )
  elif ( prob == 3 ):
    title = p03_title ( )
  elif ( prob == 4 ):
    title = p04_title ( )
  elif ( prob == 5 ):
    title = p05_title ( )
  elif ( prob == 6 ):
    title = p06_title ( )
  elif ( prob == 7 ):
    title = p07_title ( )
  elif ( prob == 8 ):
    title = p08_title ( )
  else:
    print ( '' )
    print ( 'p00_title - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_title - Fatal error!' )

  return title

def p01_title ( ):

#*****************************************************************************80
#
## p01_title() returns the title of problem p01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x) = steps -1/2/1 at [0,1/3], [1/3,4/5], [4/5,1].'

  return title

def p02_title ( ):

#*****************************************************************************80
#
## p02_title() returns the title of problem p02.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x) = (1-3x), x < 1/3 (6x-2) if 1/3 < x'

  return title

def p03_title ( ):

#*****************************************************************************80
#
## p03_title() returns the title of problem p03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x) = x (10*x-1) (5x-2) (5x-2) (4x-3.4) (x-1)'

  return title

def p04_title ( ):

#*****************************************************************************80
#
## p04_title() returns the title of problem p04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x) = atan ( 40 * x - 15 )'

  return title

def p05_title ( ):

#*****************************************************************************80
#
## p05_title() returns the title of problem p05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x) = cos(7*x)+5*cos(11.2*x)-2*cos(14*x)+5*cos(31.5*x)+7*cos(63*x).'

  return title

def p06_title ( ):

#*****************************************************************************80
#
## p06_title() returns the title of problem p06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x) = exp ( - ( 4*x-1 )^2 )'

  return title

def p07_title ( ):

#*****************************************************************************80
#
## p07_title() returns the title of problem p07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x) = exp ( 2 x ) if x < 0.5, 0 otherwise'

  return title

def p08_title ( ):

#*****************************************************************************80
#
## p08_title() returns the title of problem p08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x) = 1 / ( 1 + ( 10 * (x-1/2) )^2 )'

  return title

def p00_title_test ( ):

#*****************************************************************************80
#
## p00_title_test() tests p00_title().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'p00_title_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p00_title() returns the title of any test problems.' )

  num = p00_prob_num ( )
  print ( '' )
  print ( '  test_interp_1d includes %d test problems.' % ( num ) )

  print ( '' )
  for prob in range ( 1, num + 1 ):
    title = p00_title ( prob )
    print ( '  #%d  "%s"' % ( prob, title ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'p00_title_test:' )
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
  print ( 'r8mat_print_SOME_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_print_SOME prints some of an R8MAT.' )

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
  print ( 'r8mat_print_SOME_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an r8vec2.
#
#  Discussion:
#
#    An r8vec2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print prints a pair of r8vec\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of r8vec\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_cheby_extreme ( n, a, b ):

#*****************************************************************************80
#
## r8vec_cheby_extreme() creates Chebyshev Extreme values in [A,B].
#
#  Discussion:
#
#    An r8vec is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( n - i - 1 ) * np.pi / float ( n - 1 )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

def r8vec_cheby_extreme_test ( ):

#*****************************************************************************80
#
## r8vec_cheby_extreme_test() tests r8vec_cheby_extreme().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_cheby_extreme_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_cheby_extreme returns Chebyshev Extreme values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_cheby_extreme ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_cheby_extreme_test' )
  print ( '  Normal end of execution.' )
  return

def r8vec_chebyspace ( n, a, b ):

#*****************************************************************************80
#
## r8vec_chebyspace() creates a vector of Chebyshev spaced values in [A,B].
#
#  Discussion:
#
#    An r8vec is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( n - i - 1 ) * np.pi / float ( n - 1 )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

def r8vec_chebyspace_test ( ):

#*****************************************************************************80
#
## r8vec_chebyspace_test() tests r8vec_chebyspace().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_chebyspace_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_chebyspace returns Chebyshev spaced values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_chebyspace ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_chebyspace_test' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an r8vec.
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
  print ( 'r8vec_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_print prints an r8vec.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an r8vec:' )
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

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  lagrange_interp_1d_test ( )
  timestamp ( )

