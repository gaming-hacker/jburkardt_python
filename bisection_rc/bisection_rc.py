#! /usr/bin/env python3
#
def bisection_rc ( a, b, x, fx, job, fa, fb, state ):

#*****************************************************************************80
#
## bisection_rc() seeks a zero of f(x) in a change of sign interval.
#
#  Discussion:
#
#    The bisection method is used.
#
#    This routine uses reverse communication, so that the function is always
#    evaluated in the calling program.
#
#    On the first call, the user sets JOB = 0, and the values of A and B.
#    Thereafter, the user checks the returned value of JOB and follows 
#    directions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the endpoints of the change of sign interval.  
#    The user only initializes these values on first call.
#
#    real X, set to A before the first call.
#
#    real FX, the function value at X.
#    Set this to 0 before the first call.  On subsequent calls, FX
#    should be set to the function value at X.
#
#    integer JOB, a communication flag.
#    Set JOB to 0 before the first call.
#
#    real FA, FB, data managed by bisection_rc.
#
#    integer STATE, data managed by bisection_rc.
#
#    real X_LOCAL, data managed by bisection_rc.
#
#  Output:
#
#    real A, B, the updated endpoints of the change of sign interval.  
#
#    real X, a point at which the function is to 
#    be evaluated.
#
#    integer JOB, a communication flag.
#
#    real FA, FB, updated data.
#
#    integer STATE, updated data.
#
  import numpy as np

  if ( job == 0 ):

    fa = 0.0
    fb = 0.0
    state = 1
    x = a
    job = 1

  elif ( state == 1 ):

    fa = fx
    x = b
    state = 2

  elif ( state == 2 ):

    fb = fx

    if ( np.sign ( fa ) == np.sign ( fb ) ):
      print ( '' )
      print ( 'bisection_rc - Fatal error!' )
      print ( '  F(A) and F(B) have the same sign.' )
      raise Exception ( 'bisection_rc - Fatal error!' )

    x = ( a + b ) / 2.0
    state = 3

  else:

    if ( np.sign ( fx ) == np.sign ( fa ) ):
      a = x
      fa = fx
    else:
      b = x
      fb = fx
    x = ( a + b ) / 2.0
    state = 3

  return a, b, x, job, fa, fb, state

def bisection_rc_test ( ):

#*****************************************************************************80
#
## bisection_rc_test() tests bisection_rc().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bisection_rc_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test bisection_rc().' )

  bisection_rc_test01 ( )
  bisection_rc_test02 ( )
  bisection_rc_test03 ( )
  bisection_rc_test04 ( )
  bisection_rc_test05 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'bisection_rc_test():' )
  print ( '  Normal end of execution.' )
  return

def bisection_rc_test01 ( ):

#*****************************************************************************80
#
## bisection_rc_test01() tests bisection_rc(), evaluating the function in a separate routine.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bisection_rc_test01():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Demonstrate bisection_rc() on a simple example.' )
  print ( '  The function is evaluated in a separate routine.' )

  fx_tol = 1.0E-08
  dx_tol = 1.0E-06
  it = 0
  it_max = 30

  a = 0.0
  b = 1.0
  x = a
  fx = 0.0
  job = 0
  fa = 0.0
  fb = 0.0
  state = 1

  print ( '' )
  print ( '     I      X               FX              DX' )
  print ( '' )

  while ( True ):

    a, b, x,     job, fa, fb, state = bisection_rc ( \
    a, b, x, fx, job, fa, fb, state )

    if ( job < 0 ):
      print ( '' )
      print ( '  Error return.' )
      break

    it = it + 1

    fx = f01 ( x )

    if ( it <= 2 ):
      dx = abs ( b - a )
    else:
      dx = 0.5 * abs ( b - a )

    print ( '  %4d  %14.6g  %14.6g  %14.6g' % ( it, x, fx, dx ) )

    if ( abs ( fx ) <= fx_tol ):
      print ( '' )
      print ( '  Function is small.' )
      break

    if ( dx <= dx_tol ):
      print ( '' )
      print ( '  Interval is tiny.' )
      break
 
    if ( it_max <= it ):
      print ( '' )
      print ( '  Reached iteration limit.' )
      break

  print ( '' )
  print ( '  A = %14g, F(A) = %14g' % ( a, f01 ( a ) ) )
  print ( '  X = %14g, F(X) = %14g' % ( x, f01 ( x ) ) )
  print ( '  B = %14g, F(B) = %14g' % ( b, f01 ( b ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'bisection_rc_test01():' )
  print ( '  Normal end of execution.' )
  return

def f01 ( x ):

#*****************************************************************************80
#
## f01() evaluates the function f(x) = cos ( x ) - x which is zero around 0.74
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the function value.
#
  import numpy as np

  value = np.cos ( x ) - x

  return value

def bisection_rc_test02 ( ):

#*****************************************************************************80
#
## bisection_rc_test02() tests bisection_rc(), evaluating the function within the routine.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  from scipy.special import erf

  print ( '' )
  print ( 'bisection_rc_test02():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Demonstrate bisection_rc() on a simple example.' )
  print ( '  The function is evaluated within this routine.' )

  fx_tol = 1.0E-09
  dx_tol = 1.0E-09
  it = 0
  it_max = 30

  a = 0.0
  b = 1.0
  x = a
  fx = 0.0
  job = 0
  fa = 0.0
  fb = 0.0
  state = 1

  print ( '' )
  print ( '     I      X               FX              DX' )
  print ( '' )

  while ( True ):

    a, b, x,     job, fa, fb, state = bisection_rc ( \
    a, b, x, fx, job, fa, fb, state )

    if ( job < 0 ):
      print ( '' )
      print ( '  Error return.' )
      break

    it = it + 1

    fx = np.cos ( 100.0 * x ) - 4.0 * erf ( 30.0 * x - 10.0 )

    if ( it <= 2 ):
      dx = abs ( b - a )
    else:
      dx = 0.5 * abs ( b - a )

    print ( '  %4d  %14.6g  %14.6g  %14.6g' % ( it, x, fx, dx ) )

    if ( abs ( fx ) <= fx_tol ):
      print ( '' )
      print ( '  Function is small.' )
      break

    if ( dx <= dx_tol ):
      print ( '' )
      print ( '  Interval is tiny.' )
      break

    if ( it_max <= it ):
      print ( '' )
      print ( '  Reached iteration limit.' )
      break

  print ( '' )
  fx = np.cos ( 100.0 * a ) - 4.0 * erf ( 30.0 * a - 10.0 )
  print ( '  A = %g, F(A) = %g' % ( a, fx ) )
  fx = np.cos ( 100.0 * x ) - 4.0 * erf ( 30.0 * x - 10.0 )
  print ( '  X = %g, F(X) = %g' % ( x, fx ) )
  fx = np.cos ( 100.0 * b ) - 4.0 * erf ( 30.0 * b - 10.0 )
  print ( '  B = %g, F(B) = %g' % ( b, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'bisection_rc_test02():' )
  print ( '  Normal end of execution.' )
  return

def bisection_rc_test03 ( ):

#*****************************************************************************80
#
## bisection_rc_test03() tests bisection_rc(), to invert the cardiod CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  alpha = 0.0
  beta = 0.25

  print ( '' )
  print ( 'bisection_rc_test03():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Demonstrate bisection_rc() on a probability example.' )
  print ( '' )
  print ( '  The cardioid probability density function has a' )
  print ( '  cumulative density function of the form:' )
  print ( '    CDF(X) = ( pi + x - alpha + 2 beta * sin ( x - alpha ) ) / ( 2 * pi )' )
  print ( '  where alpha and beta are parameters, and x is a value' )
  print ( '  in the range -pi <= x <= +pi.' )
  print ( '' )
  print ( '  CDF(X) is the probability that a random sample will have' )
  print ( '  a value less than or equal to X.' )
  print ( '' )
  print ( '  As X moves from -pi to +pi,' )
  print ( '  the CDF rises from 0 (no probability)' )
  print ( '  to 1 (certain probability).' )
  print ( '' )
  print ( '  Assuming that:' )
  print ( '  * ALPHA = %g' % ( alpha ) )
  print ( '  * BETA =  %g' % ( beta ) )
  print ( '  determine the value X where the Cardioid CDF is exactly 0.75.' )

  fx_tol = 1.0E-06
  dx_tol = 1.0E-08
  it = 0
  it_max = 30

  a = - np.pi
  b = + np.pi
  x = a
  fx = 0.0
  job = 0
  fa = 0.0
  fb = 0.0
  state = 1

  print ( '' )
  print ( '     I      X               FX              DX' )
  print ( '' )

  while ( True ):

    a, b, x,     job, fa, fb, state = bisection_rc ( \
    a, b, x, fx, job, fa, fb, state )

    if ( job < 0 ):
      print ( '' )
      print ( '  Error return.' )
      break

    it = it + 1

    cdf = ( np.pi + x - alpha + 2.0 * beta * np.sin ( x - alpha ) ) / ( 2.0 * np.pi )
    fx = cdf - 0.75

    if ( it <= 2 ):
      dx = abs ( b - a )
    else:
      dx = 0.5 * abs ( b - a )

    print ( '  %4d  %14.6g  %14.6g  %14.6g' % ( it, x, fx, dx ) )

    if ( abs ( fx ) <= fx_tol ):
      print ( '' )
      print ( '  Function is small.' )
      break

    if ( dx <= dx_tol ):
      print ( '' )
      print ( '  Interval is tiny.' )
      break

    if ( it_max <= it ):
      print ( '' )
      print ( '  Reached iteration limit.' )
      break

  print ( '' )
  cdf = ( np.pi + a - alpha + 2.0 * beta * np.sin ( a - alpha ) ) / ( 2.0 * np.pi )
  fx = cdf - 0.75
  print ( '  A = %14.6g, F(A) = %14.6g' % ( a, fx ) )
  cdf = ( np.pi + x - alpha + 2.0 * beta * np.sin ( x - alpha ) ) / ( 2.0 * np.pi )
  fx = cdf - 0.75
  print ( '  X = %14.6g, F(X) = %14.6g' % ( x, fx ) )
  cdf = ( np.pi + b - alpha + 2.0 * beta * np.sin ( b - alpha ) ) / ( 2.0 * np.pi )
  fx = cdf - 0.75
  print ( '  B = %14.6g, F(B) = %14.6g' % ( b, fx ) )

  print ( '' )
  print ( '  Look at the actual cardioid CDF value now:' )
  print ( '' )
  cdf = ( np.pi + x - alpha + 2.0 * beta * np.sin ( x - alpha ) ) / ( 2.0 * np.pi )
  print ( '  Cardioid(%g) = %g' % ( x, cdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'bisection_rc_test03():' )
  print ( '  Normal end of execution.' )
  return

def bisection_rc_test04 ( ):

#*****************************************************************************80
#
## bisection_rc_test04() tests bisection_rc() for the pipe freezing problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2016
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
#    LC: QA297.M625,
#    ebook: https://www.mathworks.com/moler/chapters.html
#
  import numpy as np
  import platform

  from scipy.special import erf

  print ( '' )
  print ( 'bisection_rc_test04():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  The freezing pipe problem.' )
  print ( '' )
  print ( '  At the beginning of a cold spell, the soil is at a uniform' )
  print ( '  temperature of Ti.  The cold spell applies a uniform air' )
  print ( '  temperature of Tc, which begins to cool the soil.' )
  print ( '  As a function of depth x and time t, the soil temperature' )
  print ( '  will now cool down as:' )
  print ( '    ( T(x,t) - Tc ) / ( Ti - Tc ) = erf ( 0.5 * x / sqrt ( alpha * t ) ).' )
  print ( '  where:' )
  print ( '    Ti =  20 degrees centigrade,' )
  print ( '    Tc = -15 degrees centigrade,' )
  print ( '    alpha = 0.000000138 meter^2 / second, thermal conductivity' )
  print ( '    and erf() is the error function.' )
  print ( '  Water freezes at 0 degrees centigrade.' )
  print ( '' )
  print ( '  What depth x in meters must a water pipe be buried so that it will' )
  print ( '  not freeze even if this cold snap lasts for 60 days?' )
#
#  Problem parameters.
#
  ti = 20.0
  tc = -15.0
  t = 60.0 * 24 * 60.0 * 60.0
  alpha = 0.000000138
#
#  Iteration parameters.
#
  fx_tol = 1.0E-09
  dx_tol = 1.0E-09
  it = 0
  it_max = 30
#
#  Initial guess for interval.
#
  a = 0.0
  b = 1000.0
  x = a
  fx = 0.0
  job = 0
  fa = 0.0
  fb = 0.0
  state = 1

  print ( '' )
  print ( '     I      X               FX              DX' )
  print ( '' )

  while ( True ):

    a, b, x,     job, fa, fb, state = bisection_rc ( \
    a, b, x, fx, job, fa, fb, state )

    if ( job < 0 ):
      print ( '' )
      print ( '  Error return.' )
      break

    it = it + 1

    fx = tc + ( ti - tc ) * erf ( 0.5 * x / np.sqrt ( alpha * t ) )

    if ( it <= 2 ):
      dx = abs ( b - a )
    else:
      dx = 0.5 * abs ( b - a )

    print ( '  %4d  %14.6g  %14.6g  %14.6g' % ( it, x, fx, dx ) )

    if ( abs ( fx ) <= fx_tol ):
      print ( '' )
      print ( '  Function is small.' )
      break

    if ( dx <= dx_tol ):
      print ( '' )
      print ( '  Interval is tiny.' )
      break

    if ( it_max <= it ):
      print ( '' )
      print ( '  Reached iteration limit.' )
      break

  print ( '' )
  fx = tc + ( ti - tc ) * erf ( 0.5 * a / np.sqrt ( alpha * t ) )
  print ( '  A = %14.6g, F(A) = %14.6g' % ( a, fx ) )
  fx = tc + ( ti - tc ) * erf ( 0.5 * x / np.sqrt ( alpha * t ) )
  print ( '  X = %14.6g, F(X) = %14.6g' % ( x, fx ) )
  fx = tc + ( ti - tc ) * erf ( 0.5 * b / np.sqrt ( alpha * t ) )
  print ( '  B = %14.6g, F(B) = %14.6g' % ( b, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'bisection_rc_test04():' )
  print ( '  Normal end of execution.' )
  return

def bisection_rc_test05 ( ):

#*****************************************************************************80
#
## bisection_rc_test05() tests bisection_rc() for Kepler's problem.
#
#  Discussion:
#
#    Kepler's equation has the form:
#
#      X = M + E * sin ( X )
#
#    X represents the eccentric anomaly of a planet, the angle between the
#    perihelion (the point on the orbit nearest to the sun) through the sun 
#    to the center of the ellipse, and the line from the center of the ellipse
#    to the planet.
#
#    There are two parameters, E and M:
#
#    * E is the eccentricity of the orbit, which should be between 0 and 1.0
#
#    * M is the angle from the perihelion made by a fictitious planet traveling
#      on a circular orbit centered at the sun, and traveling at a constant
#      angular velocity equal to the average angular velocity of the true
#      planet.  M is usually between 0 and 180 degrees, but can have any value.
#
#    For convenience, X and M are measured in degrees.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2016
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
#    LC: QA297.M625,
#    ebook: https://www.mathworks.com/moler/chapters.html
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'bisection_rc_test05():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  The Kepler equation.' )
  print ( '' )
  print ( '  The Kepler equation has the form' )
  print ( '' )
  print ( '    X = M + E * sin ( X )' )
  print ( '' )
  print ( '  X represents the eccentric anomaly of a planet, the angle between the' )
  print ( '  perihelion (the point on the orbit nearest to the sun) through the sun ' )
  print ( '  to the center of the ellipse, and the line from the center of the ellipse' )
  print ( '  to the planet.' )
  print ( '' )
  print ( '  There are two parameters, E and M:' )
  print ( '' )
  print ( '  * E is the eccentricity of the orbit, which should be between 0 and 1.0' )
  print ( '' )
  print ( '  * M is the angle from the perihelion made by a fictitious planet traveling' )
  print ( '    on a circular orbit centered at the sun, and traveling at a constant' )
  print ( '    angular velocity equal to the average angular velocity of the true' )
  print ( '    planet.  M is usually between 0 and 180 degrees, but can have any value.' )
  print ( '' )
  print ( '  For convenience, X and M are measured in degrees.' )
#
#  Problem parameters.
#
  md = 24.851090
  mr = md * np.pi / 180.0
  e = 0.1

  print ( '' )
  print ( '  Given eccentricity E = %g' % ( e ) )
  print ( '  Given angle M = %g (degrees)' % ( md ) )
  print ( '                = %g (radians)' % ( mr ) )
  print ( '' )
  print ( '  Given E and M, find corresponding X.' )
#
#  Iteration parameters.
#
  fx_tol = 1.0E-09
  dx_tol = 1.0E-09
  it = 0
  it_max = 30
#
#  Initial guess for interval.
#
  ad = 0.0
  bd = 180.0

  ar = ad * np.pi / 180.0
  br = bd * np.pi / 180.0
  xr = ar
  fx = 0.0
  job = 0
  fa = 0.0
  fb = 0.0
  state = 1

  print ( '' )
  print ( '     I      X               FX              DX' )
  print ( '' )

  while ( True ):

    ar, br, xr,     job, fa, fb, state = bisection_rc ( \
    ar, br, xr, fx, job, fa, fb, state )

    if ( job < 0 ):
      print ( '' )
      print ( '  Error return.' )
      break
 
    it = it + 1

    fx = xr - mr - e * np.sin ( xr )

    if ( it <= 2 ):
      dx = abs ( br - ar )
    else:
      dx = 0.5 * abs ( br - ar )

    print ( '  %4d  %14.6g  %14.6g  %14.6g' % ( it, xr, fx, dx ) )

    if ( abs ( fx ) <= fx_tol ):
      print ( '' )
      print ( '  Function is small.' )
      break

    if ( dx <= dx_tol ):
      print ( '' )
      print ( '  Interval is tiny.' )
      break

    if ( it_max <= it ):
      print ( '' )
      print ( '  Reached iteration limit.' )
      break
 
  print ( '' )
  print ( '  In RADIANS:' )
  print ( '' )
  fx = ar - mr - e * np.sin ( ar )
  print ( '  A = %24.16g, F(A) = %14.6g' % ( ar, fx ) )
  fx = xr - mr - e * np.sin ( xr  )
  print ( '  X = %24.16g, F(X) = %14.6g' % ( xr, fx ) )
  fx = br - mr - e * np.sin ( br )
  print ( '  B = %24.16g, F(B) = %14.6g' % ( br, fx ) )

  ad = ar * 180 / np.pi
  xd = xr * 180 / np.pi
  bd = br * 180 / np.pi
  print ( '' )
  print ( '  In DEGREES:' )
  print ( '' )
  fx = ( ad - md ) * np.pi / 180 - e * np.sin ( ad * np.pi / 180 )
  print ( '  A = %24.16g, F(A) = %14.6g' % ( ad, fx ) )
  fx = ( xd - md ) * np.pi / 180 - e * np.sin ( xd * np.pi / 180  )
  print ( '  X = %24.16g, F(X) = %14.6g' % ( xd, fx ) )
  fx = ( bd - md ) * np.pi / 180 - e * np.sin ( bd * np.pi / 180 )
  print ( '  B = %24.16g, F(B) = %14.6g' % ( bd, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'bisection_rc_test05():' )
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
  bisection_rc_test ( )
  timestamp ( )

