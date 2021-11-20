#! /usr/bin/env python3
#
def annulus_area ( center, r1, r2 ):

#*****************************************************************************80
#
## annulus_area() computes the area of a circular annulus in 2D.
#
#  Discussion:
#
#    A circular annulus with center (XC,YC), inner radius R1 and
#    outer radius R2, is the set of points (X,Y) so that
#
#      R1^2 <= (X-XC)^2 + (Y-YC)^2 <= R2^2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real CENTER(2), the coordinates of the center.
#    This data is actually not necessary for area calculations.
#
#    real R1, R2, the inner and outer radii of the annulus.
#    0.0 <= R1 <= R2.
#
#  Output:
#
#    real AREA, the area of the annulus.
#
  import numpy as np
 
  if ( r1 < 0.0 ):
    print ( '' )
    print ( 'annulus_area - Fatal error!' )
    print ( '  Inner radius R1 < 0.0.' )
    raise Exception ( 'annulus_area - Fatal error!' )

  if ( r2 < r1 ):
    print ( '' )
    print ( 'annulus_area - Fatal error!' )
    print ( '  Outer radius R1 < R1 = inner radius.' )
    raise Exception ( 'annulus_area - Fatal error!' )

  area = np.pi * ( r2 + r1 ) * ( r2 - r1 )

  return area

def annulus_area_test ( ):

#*****************************************************************************80
#
## annulus_area_test() test annulus_area().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'annulus_area_test():' )
  print ( '  annulus_area() computes the area of an annulus with' )
  print ( '  center = (CX,CY), inner radius R1 and outer radius R2.' )
  print ( '' )
  print ( '  (   CX        CY     )    R1         R2         Area' )
  print ( '' )

  center = np.zeros ( 2 )

  for i in range ( 0, 10 ):
    data = np.random.rand ( 4 )
    center[0] = 10.0 * data[0] - 5.0
    center[1] = 10.0 * data[1] - 5.0
    r1 = data[2]
    r2 = r1 + data[3]
    area = annulus_area ( center, r1, r2 )
    print ( '  (%9.6f,%9.6f)  %9.6f  %9.6f  %9.6f' \
      % ( center[0], center[1], r1, r2, area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'annulus_area_test():' )
  print ( '  Normal end of execution.' )
  return

def annulus_monte_carlo_test ( ):

#*****************************************************************************80
#
## annulus_monte_carlo_test() tests annulus_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'annulus_monte_carlo_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test annulus_monte_carlo().' )

  annulus_area_test ( )

  center = np.array ( [ 0.0, 0.0 ] )
  r1 = 0.0
  r2 = 1.0
  annulus_sample_test ( center, r1, r2 )

  center = np.array ( [ 0.0, 0.0 ] )
  r1 = 0.5
  r2 = 1.0
  annulus_sample_test ( center, r1, r2 )

  center = np.array ( [ 1.0, 0.0 ] )
  r1 = 0.0
  r2 = 1.0
  annulus_sample_test ( center, r1, r2 )
#
#  Terminate.
#
  print ( '' )
  print ( 'annulus_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  return

def annulus_sample ( pc, r1, r2, n ):

#*****************************************************************************80
#
## annulus_sample() samples a circular annulus.
#
#  Discussion:
#
#    A circular annulus with center PC, inner radius R1 and
#    outer radius R2, is the set of points P so that
#
#      R1^2 <= (P(1)-PC(1))^2 + (P(2)-PC(2))^2 <= R2^2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Peter Shirley,
#    Nonuniform Random Point Sets Via Warping,
#    Graphics Gems, Volume III,
#    edited by David Kirk,
#    AP Professional, 1992, 
#    ISBN: 0122861663,
#    LC: T385.G6973.
#
#  Input:
#
#    real PC(2), the center.
#
#    real R1, R2, the inner and outer radii.
#    0.0 <= R1 <= R2.
#
#    integer N, the number of points to generate.
#
#  Output:
#
#    real P(2,N), sample points.
#
  import numpy as np

  if ( r1 < 0.0 ):
    print ( '' )
    print ( 'annulus_sample - Fatal error!' )
    print ( '  Inner radius R1 < 0.0.' )
    raise Exception ( 'annulus_sample - Fatal error!' )

  if ( r2 < r1 ):
    print ( '' )
    print ( 'annulus_sample - Fatal error!' )
    print ( '  Outer radius R1 < R1 = inner radius.' )
    raise Exception ( 'annulus_sample - Fatal error!' )

  theta = 2.0 * np.pi * np.random.rand ( n )

  v = np.random.rand ( n )

  r = np.sqrt ( ( 1.0 - v[:] ) * r1 * r1 \
    +                   v[:]   * r2 * r2 )

  p = np.zeros ( [ 2, n ] )

  p[0,:] = pc[0] + r[:] * np.cos ( theta[:] )
  p[1,:] = pc[1] + r[:] * np.sin ( theta[:] )

  return p

def annulus_sample_test ( center, r1, r2 ):

#*****************************************************************************80
#
## annulus_sample_test() tests annulus_sample().
#
#  Discussion:
#
#    If CENTER=(0,0) and R1 = 0 and R2 = 1, then we can compare exact values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  e_test = np.array ( [ \
    [0, 0], \
    [2, 0], \
    [0, 2], \
    [4, 0], \
    [2, 2], \
    [0, 4], \
    [6, 0] ] )

  print ( '' )
  print ( 'annulus_sample_test():' )
  print ( '  annulus_sample() can sample an annulus uniformly.' )
  print ( '  Use it to estimate integrals in the annulus' )
  print ( '  centered at (%g,%g) with R1 = %g, R2 = %g' \
    % ( center[0], center[1], r1, r2 ) )

  print ( '' )
  print ( '         N        1              X^2             Y^2             X^4             X^2Y^2           Y^4             X^6' )
  print ( '' )

  n = 1

  while ( n <= 65536 ):

    x = annulus_sample ( center, r1, r2, n )

    print ( '  %8d' % ( n ), end = '' )
    for i in range ( 0, 7 ):
      e = e_test[i,:]
      value = monomial_value ( 2, n, e, x )
      result = annulus_area ( center, r1, r2 ) * np.sum ( value[:] ) / n
      print ( '  %14.6g' % ( result ), end = '' )
    print ( '' )

    n = 2 * n

  if ( \
    center[0] == 0.0 and \
    center[1] == 0.0 and \
    r1 == 0.0 and \
    r2 == 1.0 ):
    print ( '' )
    print ( '     Exact', end = '' )
    for i in range ( 0, 7 ):
      e = e_test[i,:]
      result = disk01_monomial_integral ( e )
      print ( '  %14.6g' % ( result ), end = '' )
    print ( '' )

  return

def disk01_monomial_integral ( e ):

#*****************************************************************************80
#
## disk01_monomial_integral() returns monomial integrals in the unit disk.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 <= 1.
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 July 2018
#
#  Author:
#
#    John Burkardt
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

  r = 1.0

  if ( e[0] < 0 or e[1] < 0 ):
    print ( '' )
    print ( 'disk01_monomial_integral - Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'disk01_monomial_integral - Fatal error!' )

  if ( ( ( e[0] % 2 ) == 1 ) or ( ( e[1] % 2 ) == 1 ) ):

    integral = 0.0

  else:

    integral = 2.0

    for i in range ( 0, 2 ):
      arg = 0.5 * float ( e[i] + 1 )
      integral = integral * gamma ( arg )

    arg = 0.5 * float ( e[0] + e[1] + 2 )
    integral = integral / gamma ( arg )
#
#  The surface integral is now adjusted to give the volume integral.
#
  s = e[0] + e[1] + 2

  integral = integral * r ** s / float ( s )

  return integral

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
  annulus_monte_carlo_test ( )
  timestamp ( )

