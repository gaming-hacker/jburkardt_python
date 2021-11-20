#! /usr/bin/env python3
#
arg_save = 0.0
c = 0.0
d = 0.0
e = 0.0
epsilon = 0.0
epsilon_sqrt = 0.0
fu = 0.0
fv = 0.0
fw = 0.0
fx = 0.0
midpoint = 0.0
p = 0.0
q = 0.0
r = 0.0
tol = 0.0
tol1 = 0.0
tol2 = 0.0
u = 0.0
v = 0.0
w = 0.0
x = 0.0

def g_01 ( x ):

#*****************************************************************************80
#
## g_01() evaluates (x-2)^2 + 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2008
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  value = ( x - 2.0 ) * ( x - 2.0 ) + 1.0

  return value

def g_02 ( x ):

#*****************************************************************************80
#
## g_02() evaluates x^2 + exp ( - x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2008
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = x * x + np.exp ( - x )

  return value

def g_03 ( x ):

#*****************************************************************************80
#
## g_03() evaluates x^4+2x^2+x+3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2008
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  value = ( ( x * x + 2.0 ) * x + 1.0 ) * x + 3.0

  return value

def g_04 ( x ):

#*****************************************************************************80
#
## g_04() evaluates exp(x)+1/(100X)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2008
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = np.exp ( x ) + 0.01 / x

  return value

def g_05 ( x ):

#*****************************************************************************80
#
## g_05() evaluates exp(x) - 2x + 1/(100x) - 1/(1000000x^2)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2008
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = np.exp ( x ) - 2.0 * x + 0.01 / x - 0.000001 / x / x

  return value

def g_06 ( x ):

#*****************************************************************************80
#
## g_06() evaluates - x * sin(10 pi x ) - 1.0
#
#  Discussion:
#
#    There is a local minimum between 1.80 and 1.90 at about
#    1.850547466.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = - x * np.sin ( 10.0 * np.pi * x ) - 1.0

  return value

def g_07 ( x ):

#*****************************************************************************80
#
## g_07() evaluates 2x^4 - 4x^2 + x + 20
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = 2.0 * x * x * x * x - 4.0 * x * x + x + 20.0

  return value

def local_min_rc ( a, b, status, value ):

#*****************************************************************************80
#
## local_min_rc() seeks a minimizer of a scalar function of a scalar variable.
#
#  Discussion:
#
#    This routine seeks an approximation to the point where a function
#    F attains a minimum on the interval (A,B).
#
#    The method used is a combination of golden section search and
#    successive parabolic interpolation.  Convergence is never much
#    slower than that for a Fibonacci search.  If F has a continuous
#    second derivative which is positive at the minimum (which is not
#    at A or B), then convergence is superlinear, and usually of the
#    order of about 1.324...
#
#    The routine is a revised version of the Brent local minimization 
#    algorithm, using reverse communication.
#
#    It is worth stating explicitly that this routine will NOT be
#    able to detect a minimizer that occurs at either initial endpoint
#    A or B.  If this is a concern to the user, then the user must
#    either ensure that the initial interval is larger, or to check
#    the function value at the returned minimizer against the values
#    at either endpoint.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization Without Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Parameters
#
#    real A, B, the lower and upper bounds for an interval containing 
#    the minimizer.  It is required that A < B.
#
#    integer STATUS, used to communicate between the user and the routine.  
#    The user only sets STATUS to zero on the first  call, to indicate that this
#    is a startup call.  On each subsequent call, the input value of STATUS
#    should be its output value from the previous call.
#
#    real VALUE, the function value at ARG, as requested
#    by the routine on the previous call.
#
#  Output:
#
#    real ARG, the currently estimate for the minimizer.  On return 
#    with STATUS positive, the user is requested to evaluate the function at ARG, 
#    and return the value in VALUE.  On return with STATUS zero, ARG is the routine's
#    estimate for the function minimizer.
#
#    integer STATUS.  The routine returns STATUS positive to request 
#    that the function be evaluated at ARG, or returns STATUS as 0, to indicate 
#    that the iteration is complete and that ARG is the estimated minimizer.
#
#    real A, B, the lower and upper bounds for an interval containing 
#    the minimizer.
#
  import numpy as np

  global arg_save
  global c
  global d
  global e
  global epsilon
  global epsilon_sqrt
  global fu
  global fv
  global fw
  global fx
  global midpoint
  global p
  global q
  global r
  global tol
  global tol1
  global tol2
  global u
  global v
  global w
  global x
#
#  STATUS (INPUT) = 0, startup.
#
  if ( status == 0 ):

    if ( b <= a ):
      print ( '' )
      print ( 'local_min_rc(): Fatal error!' )
      print ( '  A < B is required, but' )
      print ( '  A = %f' % ( a ) )
      print ( '  B = %f' % ( b ) )
      status = -1
      raise Exception ( 'local_min_rc(): Fatal error!' )

    c = 0.5 * ( 3.0 - np.sqrt ( 5.0 ) )

    epsilon = np.finfo(float).eps
    epsilon_sqrt = np.sqrt ( epsilon )
    tol = epsilon

    v = a + c * ( b - a )
    w = v
    x = v
    e = 0.0

    status = 1
    arg = x
    arg_save = arg

    return arg, status, a, b
#
#  STATUS (INPUT) = 1, return with initial function value of FX.
#
  elif ( status == 1 ):

    fx = value
    fv = fx
    fw = fx
#
#  STATUS (INPUT) = 2 or more, update the data.
#
  elif ( 2 <= status ):

    fu = value

    if ( fu <= fx ):

      if ( x <= u ):
        a = x
      else:
        b = x

      v = w
      fv = fw
      w = x
      fw = fx
      x = u
      fx = fu

    else:

      if ( u < x ):
        a = u
      else:
        b = u

      if ( fu <= fw or w == x ):
        v = w
        fv = fw
        w = u
        fw = fu
      elif ( fu <= fv or v == x or v == w ):
        v = u
        fv = fu
#
#  Take the next step.
#
  midpoint = 0.5 * ( a + b )
  tol1 = epsilon_sqrt * np.abs ( x ) + tol / 3.0
  tol2 = 2.0 * tol1
#
#  If the stopping criterion is satisfied, we can finish.
#
  if ( np.abs ( x - midpoint ) <= ( tol2 - 0.5 * ( b - a ) ) ):
    status = 0
    arg = arg_save
    return arg, status, a, b
#
#  Is golden-section necessary?
#
  if ( np.abs ( e ) <= tol1 ):
    if ( midpoint <= x ):
      e = a - x
    else:
      e = b - x

    d = c * e
#
#  Consider fitting a parabola.
#
  else:

    r = ( x - w ) * ( fx - fv )
    q = ( x - v ) * ( fx - fw )
    p = ( x - v ) * q - ( x - w ) * r
    q = 2.0 * ( q - r )
    if ( 0.0 < q ):
      p = - p
    q = np.abs ( q )
    r = e
    e = d
#
#  Choose a golden-section step if the parabola is not advised.
#
    if ( \
      ( np.abs ( 0.5 * q * r ) <= np.abs ( p ) ) or \
      ( p <= q * ( a - x ) ) or \
      ( q * ( b - x ) <= p ) ):

      if ( midpoint <= x ):
        e = a - x
      else:
        e = b - x

      d = c * e
#
#  Choose a parabolic interpolation step.
#
    else:

      d = p / q
      u = x + d

      if ( ( u - a ) < tol2 ):
        d = tol1 * r8_sign ( midpoint - x )

      if ( ( b - u ) < tol2 ):
        d = tol1 * r8_sign ( midpoint - x )
#
#  F must not be evaluated too close to X.
#
  if ( tol1 <= np.abs ( d ) ):
    u = x + d

  if ( np.abs ( d ) < tol1 ):
    u = x + tol1 * r8_sign ( d )
#
#  Request value of F(U).
#
  arg = u
  arg_save = arg
  status = status + 1

  return arg, status, a, b

def local_min_rc_test ( ):

#*****************************************************************************80
#
## local_min_rc_test() tests local_min_rc().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'local_min_rc_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  local_min_rc() seeks a local minimizer of a function F(X)' )
  print ( '  in an interval [A,B], using reverse communication.' )

  epsilon = np.finfo(float).eps
  t = 10.0 * np.sqrt ( epsilon )

  a = 0.0
  b = 3.141592653589793
  test_example ( a, b, t, g_01, 'g_01(x) = ( x - 2 ) * ( x - 2 ) + 1' )

  a = 0.0
  b = 1.0
  test_example ( a, b, t, g_02, 'g_02(x) = x * x + exp ( - x )' )

  a = -2.0
  b =  2.0
  test_example ( a, b, t, g_03, 'g_03(x) = x^4 + 2x^2 + x + 3' )

  a =  0.0001
  b =  1.0
  test_example ( a, b, t, g_04, 'g_04(x) = exp ( x ) + 1 / ( 100 x )' )

  a =  0.0002
  b = 2.0
  test_example ( a, b, t, g_05, 'g_05(x) = exp ( x ) - 2x + 1/(100x) - 1/(1000000x^2)' )

  a = 1.8
  b = 1.9
  test_example ( a, b, t, g_06, 'g_06(x) = - x sin ( 10 pi x ) - 1' )

  a = 0.0
  b = 2.0
  test_example ( a, b, t, g_07, 'g_07(x) = 2x^4 - 4x^2 + x + 20' )

  a = -2.0
  b = 0.0
  test_example ( a, b, t, g_07, 'g_07(x) = 2x^4 - 4x^2 + x + 20' )
#
#  Terminate.
#
  print ( '' )
  print ( 'local_min_rc_test()' )
  print ( '  Normal end of execution.' )
  return

def test_example ( a, b, t, f, title ):

#*****************************************************************************80
#
## test_example() tests local_min_rc() on one test function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the endpoints of the interval.
#
#    real T, a positive absolute error tolerance.
#
#    real value = F ( x ), the name of a user-supplied
#    function whose local minimum is being sought.
#
#    string TITLE, a title for the problem.
#
  print ( '' )
  print ( '  %s' % ( title ) )
  print ( '' )
  print ( '  Step      X                          F(X)' )
  print ( '' )
  step = 0

  arg = a
  value = f ( arg )
  print ( '  %4d  %24.16e  %24.16e' % ( step, arg, value ) )

  arg = b
  value = f ( arg )
  print ( '  %4d  %24.16e  %24.16e' % ( step, arg, value ) )

  a2 = a
  b2 = b
  status = 0

  while ( True ):

    arg, status, a2, b2 = local_min_rc ( a2, b2, status, value )
 
    if ( status < 0 ):
      print ( '' )
      print ( 'test_example - Fatal error!' )
      print ( '  local_min_rc returned negative status.' )
      break

    value = f ( arg )

    step = step + 1
    print ( '  %4d  %24.16e  %24.16e' % ( step, arg, value ) )

    if ( status == 0 ):
      break

    if ( 50 < step ):
      print ( '' )
      print ( 'test_example - Fatal error!' )
      print ( '  Too many steps.' )
      break

  return

def r8_sign ( x ):

#*****************************************************************************80
#
## r8_sign() returns the sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose sign is desired.
#
#  Output:
#
#    real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  else:
    value = +1.0
 
  return value

def r8_sign_test ( ):

#*****************************************************************************80
#
## r8_sign_test() tests r8_sign().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 5

  r8_test = np.array ( [ -1.25, -0.25, 0.0, +0.5, +9.0 ] )

  print ( '' )
  print ( 'r8_sign_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sign() returns the sign of an R8.' )
  print ( '' )
  print ( '     R8     R8_SIGN(R8)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_test[test]
    s = r8_sign ( r8 )
    print ( '  %8.4f  %8.0f' % ( r8, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_sign_test():' )
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
  local_min_rc_test ( )
  timestamp ( )
 
