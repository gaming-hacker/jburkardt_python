#! /usr/bin/env python3
#
def r8vec3_print ( n, a1, a2, a3, title ):

#*****************************************************************************80
#
## r8vec3_print() prints an R8VEC3.
#
#  Discussion:
#
#    An R8VEC3 is a dataset consisting of 3 vectors of N real values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), A3(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g  %12g' % ( i, a1[i], a2[i], a3[i] ) )

  return

def r8vec3_print_test ( ):

#*****************************************************************************80
#
## r8vec3_print_test() tests r8vec3_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec3_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec3_print prints an R8VEC.' )

  n = 6

  t = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  u = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  v = np.array ( [ 0.0, 0.24, 0.56, 0.96, 1.44, 2.0 ], dtype = np.float64 )

  r8vec3_print ( n, t, u, v, '  X, X^2, X+X^2\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec3_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_linspace2 ( n, a, b ):

#*****************************************************************************80
#
## r8vec_linspace2() creates a vector of linearly spaced values.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    5 points evenly spaced between 0 and 12 will yield 2, 4, 6, 8, 10.
#
#    In other words, the interval is divided into N+1 even subintervals,
#    and the endpoints of internal intervals are used as the points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 August 2016
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
#    real X(N), a vector of linearly spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = ( float ( n - i     ) * a \
           + float (     i + 1 ) * b ) \
           / float ( n     + 1 )
 
  return x

def r8vec_linspace2_test ( ):

#*****************************************************************************80
#
## r8vec_linspace2_test() tests r8vec_linspace2().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_linspace2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_linspace2 returns evenly spaced values between A and B' )
  print ( '  omitting the endpoints.' )

  n = 4
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_linspace2 ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The linspace2 vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_linspace2_test' )
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

def cosine_sum ( x ):

#*****************************************************************************80
#
## cosine_sum() evaluates a function which is a cosine sum.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  import numpy as np

  value =   np.cos (       x ) \
    + 5.0 * np.cos ( 1.6 * x ) \
    - 2.0 * np.cos ( 2.0 * x ) \
    + 5.0 * np.cos ( 4.5 * x ) \
    + 7.0 * np.cos ( 9.0 * x )

  return value

def poly5 ( x ):

#*****************************************************************************80
#
## poly5() evaluates a particular fifth-degree polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value of the polynomial at X.
#
  value = ( x - 0.1 ) * \
          ( x - 0.2 ) * \
          ( x - 0.4 ) * \
          ( x - 2.1 ) * \
          ( x - 3.0 )

  return value

def sine_transform_data ( n, d ):

#*****************************************************************************80
#
## sine_transform_data() does a sine transform on a vector of data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data points.
#
#    real D(N), the vector of data.
#
#  Output:
#
#    real S(N), the sine transform coefficients.
#
  import numpy as np

  s = np.zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      s[i] = s[i] + np.sin ( np.pi * float ( ( i + 1 ) * ( j + 1 ) ) / float ( n + 1 ) ) * d[j]
    s[i] = s[i] * np.sqrt ( float ( 2 ) / float ( n + 1 ) )

  return s

def sine_transform_data_test ( ):

#*****************************************************************************80
#
## sine_transform_data_test() tests sine_transform_data().
#
#  Discussion:
#
#    This program demonstrates that the transform is its own inverse.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2012
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10

  print ( '' )
  print ( 'sine_transform_data_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sine_transform_data does a sine transform of data' )
  print ( '  defined by a vector.' )
  print ( '' )
  print ( '  Demonstrate that the transform is its own inverse.' )
  print ( '  Let R be a random N vector.' )
  print ( '  Let S be the transform of D.' )
  print ( '  Let T be the transform of E.' )
  print ( '  Then R and T will be equal.' )

  r = np.random.rand ( n )
  s = sine_transform_data ( n, r )
  t = sine_transform_data ( n, s )

  r8vec3_print ( n, r, s, t, '       I          R             S             T' )
#
#  Terminate.
#
  print ( '' )
  print ( 'sine_transform_data_test' )
  print ( '  Normal end of execution.' )
  return

def sine_transform_function ( n, a, b, f ):

#*****************************************************************************80
#
## sine_transform_function() does a sine transform on functional data.
#
#  Discussion:
#
#    The interval [A,B] is divided into N+1 intervals using N+2 points,
#    which are indexed by 0 through N+1.
#
#    The original function F(X) is regarded as the sum of a linear function 
#    F1 that passes through (A,F(A)) and (B,F(B)), and a function F2
#    which is 0 at A and B.
#
#    The sine transform coefficients for F2 are then computed.
#
#    To recover the interpolant of F(X), it is necessary to combine the
#    linear part F1 with the sine transform interpolant:
#
#      Interp(F)(X) = F1(X) + F2(X)
#
#    This can be done by calling sine_transform_interpolant().
#    
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data points.
#
#    real A, B, the interval endpoints.
#
#    function value = F ( x ), a pointer to the function.
#
#  Output:
#
#    real S(N), the sine transform coefficients.
#
  import numpy as np

  x = r8vec_linspace2 ( n, a, b )
#
#  Subtract F1(X) from F(X) to get F2(X).
#
  fa = f ( a )
  fb = f ( b )

  f2 = np.zeros ( n )

  for i in range ( 0, n ):
    f2[i] = f ( x[i] ) - ( ( b - x[i]     ) * fa   \
                         + (     x[i] - a ) * fb ) \
                         / ( b        - a )
#
#  Compute the sine transform of F2(X).
#
  s = sine_transform_data ( n, f2 )

  return s

def sine_transform_function_test ( ):

#*****************************************************************************80
#
## sine_transform_function_test() tests sine_transform_function().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 9
  a = 1.0
  b = 3.0
  x = r8vec_linspace2 ( n, a, b )

  print ( '' )
  print ( 'sine_transform_function_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sine_transform_function does a sine transform of data' )
  print ( '  defined by a function F(X) evaluated at equally spaced' )
  print ( '  points in an interval [A,B].' )
  print ( '' )
  print ( '  Demonstrate that the transform is its own inverse.' )
  print ( '  Let X(0:N+1) be N+2 equally spaced points in [A,B].' )
  print ( '  Let S be the transform of F(X(1:N)).' )
  print ( '  Let F1 be the linear interpolant of (A,F(A)), (B,F(B)).' )
  print ( '  Let F2 be the transform of S.' )
  print ( '  Then F(X(1:N)) = F1(X(1:N)) + F2(1:N).' )

  s = sine_transform_function ( n, a, b, poly5 )

  fa = poly5 ( a )
  fb = poly5 ( b )

  f1 = np.zeros ( n + 2 )

  f1[0] = fa
  for i in range ( 1, n + 1 ):
    f1[i] = ( ( b - x[i-1]     ) * fa   \
          + (       x[i-1] - a ) * fb ) \
            / ( b          - a )
  f1[n+1] = fb

  f2 = sine_transform_data ( n, s )

  print ( '' )
  print ( '     I      X(I)      F(X(I))       S           F1          F2          F1+F2' )
  print ( '' )

  print ( '  %4d  %10f  %10f  %10f  %10f  %10f  %10f' \
    % ( 0, a, poly5 ( a ), 0.0, f1[0], 0.0, f1[0] ) )

  for i in range ( 1, n + 1 ):
    print ( '  %4d  %10f  %10f  %10f  %10f  %10f  %10f' \
      % ( i, x[i-1], poly5 ( x[i-1] ), s[i-1], f1[i], f2[i-1], f1[i] + f2[i-1] ) )

  print ( '  %4d  %10f  %10f  %10f  %10f  %10f  %10f' \
    % ( n+1, b, poly5 ( b ), 0.0, f1[n+1], 0.0, f1[n+1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'sine_transform_function_test' )
  print ( '  Normal end of execution.' )
  return

def sine_transform_interpolant ( n, a, b, fa, fb, s, nx, x ):

#*****************************************************************************80
#
## sine_transform_interpolant() evaluates the sine transform interpolant.
#
#  Discussion:
#
#    The interval [A,B] is divided into N+1 intervals using N+2 points,
#    which are indexed by 0 through N+1.
#
#    The original function F(X) is regarded as the sum of a linear function 
#    F1 that passes through (A,F(A)) and (B,F(B)), and a function F2
#    which is 0 at A and B.
#
#    The function F2 has been approximated using the sine transform,
#    and the interpolant is then evaluated as:
#
#      Interp(F)(X) = F1(X) + F2(X)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of terms in the approximation.
#
#    real A, B, the interval over which the approximant was defined.
#
#    real FA, FB, the function values at A and B.
#
#    real S(N), the approximant coefficients.
#
#    integer NX, the number of evaluation points.
#
#    real X(NX), the evaluation points.
#
#  Output:
#
#    real VALUE(NX), the value of the interpolant.
#
  import numpy as np
#
#  Compute linear function F1(X).
#
  f1 = np.zeros ( nx )

  for i in range ( 0, nx ):
    f1[i] = ( ( b - x[i]     ) * fa \
            + (     x[i] - a ) * fb ) \
            / ( b        - a )
#
#  Compute sine interpolant F2(X).
#
  f2 = np.zeros ( nx )

  for i in range ( 0, nx ):
    for j in range ( 0, n ):
      f2[i] = f2[i] + s[j] \
        * np.sin ( np.pi * float ( j + 1 ) * ( x[i] - a ) / ( b - a ) )
    f2[i] = f2[i] * np.sqrt ( 2.0 / float ( n + 1 ) )
#
#  Interpolant = F1 + F2.
#
  value = np.zeros ( nx )
  for i in range ( 0, nx ):
    value[i] = f1[i] + f2[i]

  return value

def sine_transform_interpolant_test ( ):

#*****************************************************************************80
#
## sine_transform_interpolant_test() tests sine_transform_interpolant().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'sine_transform_interpolant_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sine_transform_function does a sine transform of data' )
  print ( '  defined by a function F(X) evaluated at N equally spaced' )
  print ( '  points in an interval [A,B].' )
  print ( '  sine_transform_interpolant evaluates the interpolant.' )
  print ( '' )
  print ( '  The interpolant will be 0 at the 0th and (N+1)-th points.' )
  print ( '  It equals the function at points 1 through N.' )
  print ( '  In between, it can approximate smooth functions,' )
  print ( '  and the approximation improves with N.' )
#
#  N determines the number of data points, indexed by 1 to N.  
#  However, we essentially have N+2 data points, indexed 0 to N+1,
#  with the data value being 0 at the first and last auxilliary points.
#
  n = 9
  a = 1.0
  b = 4.0
  x = r8vec_linspace2 ( n, a, b )
#
#  Determine the interpolant coefficients.
#
  s = sine_transform_function ( n, a, b, poly5 )

  px = np.zeros ( n )
  for i in range ( 0, n ):
    px[i] = poly5 ( x[i] )

  r8vec3_print ( n, x, px, s, '     I      X(I)      F(X(I))        S(I)' )
#
#  Evaluate the interpolant.
#
  fa = poly5 ( a )
  fb = poly5 ( b )
  n2 = 1 + 2 * ( n + 1 )
  x2 = np.linspace ( a, b, n2 )
  f2 = sine_transform_interpolant ( n, a, b, fa, fb, s, n2, x2 )

  px2 = np.zeros ( n2 )
  for i in range ( 0, n2 ):
    px2[i] = poly5 ( x2[i] )

  r8vec3_print ( n2, x2, px2, f2, '     I      X            F(X)        FHAT(X)' )

  n3 = 501
  x3 = np.linspace ( a, b, n3 )
  px3 = np.zeros ( n3 )
  for i in range ( 0, n3 ):
    px3[i] = poly5 ( x3[i] )
#
#  Plot the sample points as blue dots,
#  the interpolant as a red line,
#  the exact function as a black line.
#
  plt.plot ( x, px, 'b*', markersize = 20 )
  plt.plot ( x2, f2, 'r-', linewidth = 8.0 )
  plt.plot ( x3, px3, 'k-', linewidth = 2.0 )
  plt.title ( 'Data (stars), interpolant (red), exact (black)' )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.savefig ( 'sine_interpolant.png' )
  plt.close ( )

  print ( '' )
  print ( '  Created plot file "sine_interpolant.png"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'sine_transform_interpolant_test' )
  print ( '  Normal end of execution.' )
  return

def sine_transform_interpolant_test2 ( ):

#*****************************************************************************80
#
## sine_transform_interpolant_test2() evaluates the sine transform interpolant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'sine_transform_interpolant_test2:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sine_transform_function does a sine transform of data' )
  print ( '  defined by a function F(X) evaluated at N equally spaced' )
  print ( '  points in an interval [A,B].' )
  print ( '  sine_transform_interpolant evaluates the interpolant.' )
  print ( '' )
  print ( '  The interpolant will be 0 at the 0th and (N+1)-th points.' )
  print ( '  It equals the function at points 1 through N.' )
  print ( '  In between, it can approximate smooth functions,' )
  print ( '  and the approximation improves with N.' )
#
#  N determines the number of data points, indexed by 1 to N.  
#  However, we essentially have N+2 data points, indexed 0 to N+1,
#  with the data value being 0 at the first and last auxilliary points.
#
  n = 15
  a = 0.0
  b = 7.0
  x = r8vec_linspace2 ( n, a, b )
  f = np.zeros ( n )
  for i in range ( 0, n ):
    f[i] = cosine_sum ( x[i] )
#
#  Determine the interpolant coefficients.
#
  s = sine_transform_function ( n, a, b, cosine_sum )
#
#  Evaluate the interpolant.
#
  fa = cosine_sum ( a )
  fb = cosine_sum ( b )
  n2 = 1 + 5 * ( n + 1 )
  x2 = np.linspace ( a, b, n2 )
  f2 = sine_transform_interpolant ( n, a, b, fa, fb, s, n2, x2 )
#
#  Plot the sample points as blue dots,
#  the approximant as a red line,
#  the exact function as a black line.
#
  n3 = 501
  x3 = np.linspace ( a, b, n3 )
  f3 = np.zeros ( n3 )
  for i in range ( 0, n3 ):
    f3[i] = cosine_sum ( x3[i] )

  plt.plot ( x, f, 'b*', markersize = 20 )
  plt.plot ( x2, f2, 'r-', linewidth = 8 )
  plt.plot ( x3, f3, 'k-', linewidth = 2 )
  plt.title ( 'Data (stars), interpolant (red), exact (black)' )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.savefig ( 'sine_interpolant2.png' )
  plt.close ( )

  print ( '' )
  print ( '  Created plot file "sine_interpolant2.png"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'sine_transform_interpolant2_test' )
  print ( '  Normal end of execution.' )
  return

def sine_transform_test ( ):

#*****************************************************************************80
#
## sine_transform_test() tests sine_transform().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sine_transform_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test sine_transform().' )
#
#  Libraries.
#
  sine_transform_data_test ( )
  sine_transform_function_test ( )
  sine_transform_interpolant_test ( )
  sine_transform_interpolant_test2 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sine_transform_test' )
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
  sine_transform_test ( )
  timestamp ( )

