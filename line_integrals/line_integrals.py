#! /usr/bin/env python3
#
def line01_length ( ):

#*****************************************************************************80
#
## line01_length(): length of the unit line in 1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the length.
#
  value = 1.0

  return value

def line01_length_test ( ) :

#*****************************************************************************80
#
## line01_length_test() tests line01_length().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'line01_length_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  line01_length returns the length of the unit line.' )

  value = line01_length ( )

  print ( '' )
  print ( '  line01_length() = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'line01_length_test' )
  print ( '  Normal end of execution.' )
  return

def line01_monomial_integral ( e ):

#*****************************************************************************80
#
## line01_monomial_integral(): monomial integral over the unit line in 1D.
#
#  Discussion:
#
#    The integration region is 
#
#      0 <= X <= 1.
#
#    The monomial is F(X) = X^E.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 June 2015
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
#    integer E, the exponent.
#    E must not equal -1.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  if ( e == -1 ):
    print ( '' )
    print ( 'line01_monomial_integral - Fatal error!' )
    print ( '  Exponent E = -1 is not allowed!' )
    raise Exception ( 'line01_monomial_integral - Fatal error!' )

  integral = 1.0 / float ( e + 1 )

  return integral

def line01_monomial_integral_test ( ):

#*****************************************************************************80
#
## line01_monomial_integral_test() tests line01_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 1
  n = 4192
  test_num = 11

  print ( '' )
  print ( 'line01_monomial_integral_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  line01_monomial_integral computes integrals of monomials' )
  print ( '  along the length of the unit line in 1D.' )
  print ( '  Compare with a Monte Carlo estimate.' )
#
#  Get sample points.
#
  x = line01_sample ( n )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
  print ( '' )
  print ( '   E     MC-Estimate      Exact           Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = test

    value = monomial_value_1d ( n, e, x )

    result = line01_length ( ) * np.sum ( value ) / float ( n )
    exact = line01_monomial_integral ( e )
    error = abs ( result - exact )

    print ( '  %2d  %14.6g  %14.6g  %10.2g' % ( e, result, exact, error ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'line01_monomial_integral_test:' )
  print ( '  Normal end of execution.' )
  return

def line01_sample ( n ):

#*****************************************************************************80
#
## line01_sample() samples the unit line in 1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#  Output:
#
#    real X(N), the points.
#
  import numpy as np

  x = np.random.rand ( n )

  return x

def line01_sample_test ( ):

#*****************************************************************************80
#
## line01_sample_test() tests line01_sample().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'line01_sample_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  line01_sample samples the unit line.' )

  n = 10

  x = line01_sample ( n )

  r8vec_print ( n, x, '  Sample points in the unit line.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'line01_sample_test' )
  print ( '  Normal end of execution.' )
  return

def line_integrals_test ( ):

#*****************************************************************************80
#
## line_integrals_test() tests line_integrals().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'line_integrals_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test line_integrals().' )
#
#  Utility functions.
#
  r8vec_print_test ( )
#
#  Library functions.
#
  line01_length_test ( )
  line01_monomial_integral_test ( )
  line01_sample_test ( )
  monomial_value_1d_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'line_integrals_test:' )
  print ( '  Normal end of execution.' )
  return

def monomial_value_1d ( n, e, x ):

#*****************************************************************************80
#
## monomial_value_1d() evaluates a monomial in 1D.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      x^e
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    integer E, the exponent.
#
#    real X(N), the point coordinates.
#
#  Output:
#
#    real VALUE(N), the value of the monomial.
#
  import numpy as np

  value = np.zeros ( n )

  for i in range ( 0, n ):
    value[i] = x[i] ** e

  return value

def monomial_value_1d_test ( ):

#*****************************************************************************80
#
## monomial_value_1d_test() tests monomial_value_1d().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_value_1d_test' )
  print ( '  monomial_value_1d evaluates a monomial of a 1D argument.' )
  print ( '' )
  print ( '      X^(-1)       X^(0)       X^(1)       X^(2)       X^(5)' )
  print ( '' )

  n = 5
  x_min = -2.0
  x_max = +10.0

  x = x_min + ( x_max - x_min ) * np.random.rand ( n )

  e = -1
  vm1 = monomial_value_1d ( n, e, x )
  e = 0
  v0 = monomial_value_1d ( n, e, x )
  e = 1
  v1 = monomial_value_1d ( n, e, x )
  e = 2
  v2 = monomial_value_1d ( n, e, x )
  e = 5
  v5 = monomial_value_1d ( n, e, x )

  for j in range ( 0, n ):
    print ( '  %10g  %10g  %10g  %10g  %10g' \
      % ( vm1[j], v0[j], v1[j], v2[j], v5[j] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'monomial_value_1d_test' )
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

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  line_integrals_test ( )
  timestamp ( )

