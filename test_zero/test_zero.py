#! /usr/bin/env python3
#
def bisection ( fatol, step_max, prob, xatol, xa, xb, fxa, fxb ):

#*****************************************************************************80
#
## bisection() carries out the bisection method to seek a root of F(X) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real FATOL, an absolute error tolerance for
#    the function value of the root.  If an approximate root X satisfies
#      ABS ( F ( X ) ) <= FATOL, then X will be accepted as the
#    root and the iteration will be terminated.
#
#    integer STEP_MAX, the maximum number of steps
#    allowed for an iteration.
#
#    integer PROB, the index of the function whose root is
#    to be sought.
#
#    real XATOL, an absolute error tolerance for the root.
#
#    real XA, XB, two points at which the
#    function differs in sign.
#
#    real FXA, FXB, the value of the function at XA and XB.
#
#  Output:
#
#    real XA, XB, two updated points at which the
#    function differs in sign.  
#
#    real FXA, FXB, the value of the function at XA and XB.
#
  print ( '' )
  print ( '  Bisection method for problem %d' % ( prob ) )
  print ( '' )
  print ( '  Step      XA            XB             F(XA)         F(XB)' )
  print ( '' )
#
#  Make A the root with negative F, B the root with positive F.
#
  if ( 0.0 < fxa ):
    t = xa
    xa = xb
    xb = t
    t = fxa
    fxa = fxb
    fxb = t

  step_num = 0
#
#  Loop
#
  while ( True ):

    print ( '  %4d  %14e  %14e  %14e  %14e' % ( step_num, xa, xb, fxa, fxb ) )

    step_num = step_num + 1

    if ( step_max < step_num ):
      print ( '' )
      print ( '  Maximum number of steps taken without convergence.' )
      break

    if ( abs ( xa - xb ) < xatol ):
      print ( '' )
      print ( '  Interval small enough for convergence.' )
      break

    if ( abs ( fxa ) <= fatol or abs ( fxb ) <= fatol ):
      print ( '' )
      print ( '  Function small enough for convergence.' )
      break
#
#  Compute the next iterate.
#
    xc = 0.5 * ( xa + xb )
    fxc = p00_fx ( prob, xc )
#
#  Replace one of the old points.
#
    if ( fxc < 0.0 ):
      xa = xc
      fxa = fxc
    else:
      xb = xc
      fxb = fxc

  return xa, xb, fxa, fxb

def bisection_test ( ):

#*****************************************************************************80
#
## bisection_test tests the bisection method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bisection_test' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    start_num = p00_start_num ( prob )

    if ( start_num < 2 ):
      print ( '  Do not have two starting values for this problem.' )
      continue

    xa = p00_start ( prob, 1 )
    xb = p00_start ( prob, 2 )
    fxa = p00_fx ( prob, xa )
    fxb = p00_fx ( prob, xb )

    if ( ( fxa < 0.0 and fxb < 0.0 ) or ( 0.0 < fxa and 0.0 < fxb ) ):
      print ( '  First two starting points agree in sign.' )
      continue

    xa2, xb2, fxa2, fxb2 = bisection ( fatol, step_max, prob, xatol, xa, xb, fxa, fxb )

    root_num = p00_root_num ( prob )

    if ( 0 < root_num ):
      print ( '' )
    else:
      print ( '  Exact root not known' )

    for root in range ( 1, root_num + 1 ):
      x = p00_root ( prob, root )
      fx = p00_fx ( prob, x )
      print ( '  Root  %14e                  %14e' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'bisection_test' )
  print ( '  Normal end of execution.' )
  return

def brent ( fatol, step_max, prob, xatol, xrtol, xa, xb, fxa, fxb ):

#*****************************************************************************80
#
## brent() implements the Brent bisection-based zero finder.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization without Derivatives,
#    Prentice Hall, 1973.
#
#  Input:
#
#    real FATOL, an absolute error tolerance for the
#    function value of the root.  If an approximate root X satisfies
#      ABS ( F ( X ) ) <= FATOL, then X will be accepted as the
#    root and the iteration will be terminated.
#
#    integer STEP_MAX, the maximum number of steps allowed
#    for an iteration.
#
#    integer PROB, the index of the function whose root is
#    to be sought.
#
#    real XATOL, XRTOL, absolute and relative error
#    tolerances for the root.
#
#    real XA, XB, two points at which the
#    function differs in sign.  
#
#    real FXA, FXB, the value of the function at XA and XB.
#
#  Output:
#
#    real XA, XB, two updated points at which the
#    function differs in sign.  
#
#    real FXA, FXB, the value of the function at XA and XB.
#

#
#  Initialization.
#
  print ( '' )
  print ( 'BRENT' )
  print ( '' )
  print ( '  Step      XA            XB             F(XA)         F(XB)' )
  print ( '' )

  step_num = 0

  fxa = p00_fx ( prob, xa )
  fxb = p00_fx ( prob, xb )
#
#  Check that f(ax) and f(bx) have different signs.
#
  if ( ( fxa < 0.0 and fxb < 0.0 ) or \
       ( 0.0 < fxa and 0.0 < fxb ) ):
    print ( '' )
    print ( 'BRENT - Fatal error!' )
    print ( '  F(XA) and F(XB) have same sign.' )
    return xa, xb, fxa, fxb

  xc = xa
  fxc = fxa
  d = xb - xa
  e = d

  while ( True ):

    print ( '  %4d  %14e  %14e  %12e  %12e' % ( step_num, xb, xc, fxb, fxc ) )

    step_num = step_num + 1

    if ( step_max < step_num ):
      print ( '' )
      print ( '  Maximum number of steps taken.' )
      break

    if ( abs ( fxc ) < abs ( fxb ) ):
      xa = xb
      xb = xc
      xc = xa
      fxa = fxb
      fxb = fxc
      fxc = fxa

    xtol = 2.0 * xrtol * abs ( xb ) + 0.5 * xatol
#
#  XM is the halfwidth of the current change-of-sign interval.
#
    xm = 0.5 * ( xc - xb )

    if ( abs ( xm ) <= xtol ):
      print ( '' )
      print ( '  Interval small enough for convergence.' )
      break

    if ( abs ( fxb ) <= fatol ):
      print ( '' )
      print ( '  Function small enough for convergence.' )
      break
#
#  See if a bisection is forced.
#
    if ( abs ( e ) < xtol or abs ( fxa ) <= abs ( fxb ) ):

      d = xm
      e = d

    else:

      s = fxb / fxa
#
#  Linear interpolation.
#
      if ( xa == xc ):

        p = 2.0 * xm * s
        q = 1.0 - s
#
#  Inverse quadratic interpolation.
#
      else:

        q = fxa / fxc
        r = fxb / fxc
        p = s * ( 2.0 * xm * q * ( q - r ) - ( xb - xa ) * ( r - 1.0 ) )
        q = ( q - 1.0 ) * ( r - 1.0 ) * ( s - 1.0 )

      if ( 0.0 < p ):
        q = - q
      else:
        p = - p

      s = e
      e = d

      if ( 3.0 * xm * q - abs ( xtol * q ) <= 2.0 * p or \
           abs ( 0.5 * s * q ) <= p ):
        d = xm
        e = d
      else:
        d = p / q
#
#  Save in XA, FXA the previous values of XB, FXB.
#
    xa = xb
    fxa = fxb
#
#  Compute the new value of XB, and evaluate the function there.
#
    if ( xtol < abs ( d ) ):
      xb = xb + d
    elif ( 0.0 < xm ):
      xb = xb + xtol
    elif ( xm <= 0.0 ):
      xb = xb - xtol

    fxb = p00_fx ( prob, xb )
#
#  If the new FXB has the same sign as FXC, then replace XC by XA.
#
    if ( ( 0.0 < fxb and 0.0 < fxc ) or \
         ( fxb < 0.0 and fxc < 0.0 ) ):
      xc = xa
      fxc = fxa
      d = xb - xa
      e = d

  return xa, xb, fxa, fxb

def brent_test ( ):

#*****************************************************************************80
#
## brent_test tests the Brent method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'brent_test' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06
  xrtol = 1.0E-06

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    start_num = p00_start_num ( prob )

    if ( start_num < 2 ):
      print ( '  Do not have two starting values for this problem.' )
      continue

    xa = p00_start ( prob, 1 )
    xb = p00_start ( prob, 2 )
    fxa = p00_fx ( prob, xa )
    fxb = p00_fx ( prob, xb )

    if ( ( fxa < 0.0 and fxb < 0.0 ) or ( 0.0 < fxa and 0.0 < fxb ) ):
      print ( '  First two starting points agree in sign.' )
      continue

    xa2, xb2, fxa2, fxb2 = brent ( fatol, step_max, prob, xatol, xrtol, \
      xa, xb, fxa, fxb )

    root_num = p00_root_num ( prob )

    if ( 0 < root_num ):
      print ( '' )
    else:
      print ( '  Exact root not known' )

    for root in range ( 1, root_num + 1 ):
      x = p00_root ( prob, root )
      fx = p00_fx ( prob, x )
      print ( '  Root  %14e                  %14e' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'brent_test' )
  print ( '  Normal end of execution.' )
  return

def muller ( fatol, step_max, prob, xatol, xrtol, xa, xb, xc, fxa, fxb, fxc ):

#*****************************************************************************80
#
## muller() carries out Muller's method for a real root of a nonlinear function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real FATOL, an absolute error tolerance for the
#    function value of the root.  If an approximate root X satisfies
#      ABS ( F ( X ) ) <= FATOL, then X will be accepted as the
#    root and the iteration will be terminated.
#
#    integer STEP_MAX, the maximum number of steps allowed
#    for an iteration.
#
#    integer PROB, the index of the function whose root is
#    to be sought.
#
#    real XATOL, XRTOL, absolute and relative error
#    tolerances  for the root.
#
#    real XA, XB, XC, three points.
#
#    real FXA, FXB, FXC, the value of the
#    function at XA, XB, and XC.
#
#  Output:
#
#    real XA, XB, XC, three updated points.
#
#    real FXA, FXB, FXC, the value of the
#    function at XA, XB, and XC.
#

#
#  Initialization.
#
  print ( '' )
  print ( 'MULLER' )
  print ( '' )
  print ( '  Step      XA           XB           XC' )
  print ( '          F(XA)        F(XB)        F(XC)' )
  print ( '' )

  i = 0

  print ( '  %4d  %14g  %14g  %14g' % ( i,  xa,  xb,  xc ) )
  print ( '        %14g  %14g  %14g' % ( fxa, fxb, fxc ) )

  for i in range ( 1, step_max + 1 ):
#
#  Determine the coefficients
#    A, B, C
#  of the polynomial
#    Y(X) = A * (X-X2)^2 + B * (X-X2) + C
#  which goes through the data:
#    (X1,Y1), (X2,Y2), (X3,Y3).
#
    a = ( ( fxa - fxc ) * ( xb - xc ) \
        - ( fxb - fxc ) * ( xa - xc ) ) / \
          ( ( xa - xc ) * ( xb - xc ) * ( xa - xb ) )

    b = ( ( fxb - fxc ) * ( xa - xc ) * ( xa - xc ) \
        - ( fxa - fxc ) * ( xb - xc ) * ( xb - xc ) ) / \
        ( ( xa - xc ) * ( xb - xc ) * ( xa - xb ) )

    c = fxc
#
#  Get the real roots of the polynomial,
#  unless A = 0, in which case the algorithm is breaking down.
#
    if ( a != 0.0 ):

      z1, z2 = r8poly2_rroot ( a, b, c )

    elif ( b != 0.0 ):

      z2 = - c / b

    else:

      print ( '' )
      print ( '  Polynomial fitting has failed.' )
      print ( '  Muller\'s algorithm breaks down.' )
      return xa, xb, xc, fxa, fxb, fxc

    xd = xc + z2
#
#  Set XA, YA, based on which of XA and XB is closer to XD.
#
    if ( abs ( xd - xb ) < abs ( xd - xa ) ):
      t = xa
      xa = xb
      xb = t
      t = fxa
      fxa = fxb
      fxb = t
#
#  Set XB, YB, based on which of XB and XC is closer to XD.
#
    if ( abs ( xd - xc ) < abs ( xd - xb ) ):
      t = xb
      xb = xc
      xc = t
      t = fxb
      fxb = fxc
      fxc = t
#
#  Set XC, YC.
#
    xc = xd
    fxc = p00_fx ( prob, xc )

    print ( '  %4d  %14g  %14g  %14g' % ( i,  xa,  xb,  xc ) )
    print ( '        %14g  %14g  %14g' % ( fxa, fxb, fxc ) )
#
#  Estimate the relative significance of the most recent correction.
#
    if ( abs ( z2 ) <= xrtol * abs ( xc ) + xatol ):
      print ( '' )
      print ( '  Stepsize small enough for convergence.' )
      return xa, xb, xc, fxa, fxb, fxc

    if ( abs ( fxc ) < fatol ):
      print ( '' )
      print ( '  Function small enough for convergence.' )
      return xa, xb, xc, fxa, fxb, fxc

  print ( '' )
  print ( '  Took maximum number of steps without convergence.' )

  return xa, xb, xc, fxa, fxb, fxc

def muller_test ( ):

#*****************************************************************************80
#
## muller_test tests the Muller method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'muller_test' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06
  xrtol = 1.0E-06

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    start_num = p00_start_num ( prob )

    if ( start_num < 3 ):
      print ( '  Do not have three starting values for this problem.' )
      continue

    xa = p00_start ( prob, 1 )
    xb = p00_start ( prob, 2 )
    xc = p00_start ( prob, 3 )
    fxa = p00_fx ( prob, xa )
    fxb = p00_fx ( prob, xb )
    fxc = p00_fx ( prob, xc )

    xa2, xb2, xc2, fxa2, fxb2, fxc2 = muller ( fatol, step_max, prob, xatol, \
      xrtol, xa, xb, xc, fxa, fxb, fxc )

    root_num = p00_root_num ( prob )

    if ( 0 < root_num ):
      print ( '' )
    else:
      print ( '  Exact root not known' )

    for root in range ( 1, root_num + 1 ):
      x = p00_root ( prob, root )
      fx = p00_fx ( prob, x )
      print ( '  Root  %14e                  %14e' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'muller_test' )
  print ( '  Normal end of execution.' )
  return

def newton ( fatol, step_max, prob, xatol, xmin, xmax, xa, fxa ):

#*****************************************************************************80
#
## newton() carries out Newton's method to seek a root of F(X) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real FATOL, an absolute error tolerance for the
#    function value of the root.  If an approximate root X satisfies
#      ABS ( F ( X ) ) <= FATOL, then X will be accepted as the
#    root and the iteration will be terminated.
#
#    integer STEP_MAX, the maximum number of steps allowed
#    for an iteration.
#
#    integer PROB, the index of the function whose root is
#    to be sought.
#
#    real XATOL, an absolute error tolerance for the root.
#
#    real XMIN, XMAX, the interval in which the root should
#    be sought.
#
#    real XA.  The starting point for the iteration.
#
#    real FXA, the function value at XA.
#
#  Output:
#
#    real XA.  The current approximation to the root.
#
#    real FXA, the function value at XA.
#
  step = 0.0

  print ( '' )
  print ( 'NEWTON' )
  print ( '' )
  print ( '  Step         X             F(X)      FP(X)' )
  print ( '' )

  step_num = 0
  fp = p00_fx1 ( prob, xa )

  print ( '  %4d  %12g  %12g  %12g' % ( step_num, xa, fxa, fp ) )

  for step_num in range ( 1, step_max + 1 ):

    if ( xa < xmin or xmax < xa ):
      print ( '' )
      print ( '  The iterate X = %g' % ( xa ) )
      print ( '  has left the region [%g,%g].' % ( xmin, xmax ) )
      return xa, fxa

    if ( abs ( fxa ) <= fatol ):
      print ( '' )
      print ( '  The function norm is small enough for convergence.' )
      return xa, fxa

    if ( 1 < step_num and abs ( step ) <= xatol ):
      print ( '' )
      print ( '  The stepsize is small enough for convergence.' )
      return xa, fxa

    if ( fp == 0.0 ):
      print ( '' )
      print ( '  F\'(X)=0, the algorithm fails.' )
      return xa, fxa

    step = fxa / fp

    xa = xa - step

    fxa = p00_fx ( prob, xa )
    fp = p00_fx1 ( prob, xa )

    print ( '  %4d  %12g  %12g  %12g' % ( step_num, xa, fxa, fp ) )

  print ( '' )
  print ( '  Took maximum number of steps without convergence.' )

  return xa, fxa

def newton_test ( ):

#*****************************************************************************80
#
## newton_test tests the Newton method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'newton_test' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    print ( '' )
    print ( '  Problem %d' % ( prob ) )

    rang = p00_rang ( prob )
    xmin = rang[0]
    xmax = rang[1]
    xa = p00_start ( prob, 1 )
    fxa = p00_fx ( prob, xa )
 
    xa2, fxa2 = newton ( fatol, step_max, prob, xatol, xmin, xmax, xa, fxa )

    root_num = p00_root_num ( prob )

    if ( 0 < root_num ):
      print ( '' )
    else:
      print ( '  Exact root not known' )

    for root in range ( 1, root_num + 1 ):
      x = p00_root ( prob, root )
      fx = p00_fx ( prob, x )
      print ( '  Root  %14e                  %14e' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'newton_test' )
  print ( '  Normal end of execution.' )
  return

def p00_fx ( prob, x ):

#*****************************************************************************80
#
## p00_fx evaluates a function specified by problem number.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the problem.
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real FX, the value of the function at X.
#
  if ( prob == 1 ):
    fx = p01_fx ( x )
  elif ( prob == 2 ):
    fx = p02_fx ( x )
  elif ( prob == 3 ):
    fx = p03_fx ( x )
  elif ( prob == 4 ):
    fx = p04_fx ( x )
  elif ( prob == 5 ):
    fx = p05_fx ( x )
  elif ( prob == 6 ):
    fx = p06_fx ( x )
  elif ( prob == 7 ):
    fx = p07_fx ( x )
  elif ( prob == 8 ):
    fx = p08_fx ( x )
  elif ( prob == 9 ):
    fx = p09_fx ( x )
  elif ( prob == 10 ):
    fx = p10_fx ( x )
  elif ( prob == 11 ):
    fx = p11_fx ( x )
  elif ( prob == 12 ):
    fx = p12_fx ( x )
  elif ( prob == 13 ):
    fx = p13_fx ( x )
  elif ( prob == 14 ):
    fx = p14_fx ( x )
  elif ( prob == 15 ):
    fx = p15_fx ( x )
  elif ( prob == 16 ):
    fx = p16_fx ( x )
  elif ( prob == 17 ):
    fx = p17_fx ( x )
  elif ( prob == 18 ):
    fx = p18_fx ( x )
  elif ( prob == 19 ):
    fx = p19_fx ( x )
  else:
    print ( '' )
    print ( 'p00_fx - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_fx - Fatal error!' )

  return fx

def p00_fx1 ( prob, x ):

#*****************************************************************************80
#
## p00_fx1: first derivative of a function specified by problem number.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the problem.
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  if ( prob == 1 ):
    fx1 = p01_fx1 ( x )
  elif ( prob == 2 ):
    fx1 = p02_fx1 ( x )
  elif ( prob == 3 ):
    fx1 = p03_fx1 ( x )
  elif ( prob == 4 ):
    fx1 = p04_fx1 ( x )
  elif ( prob == 5 ):
    fx1 = p05_fx1 ( x )
  elif ( prob == 6 ):
    fx1 = p06_fx1 ( x )
  elif ( prob == 7 ):
    fx1 = p07_fx1 ( x )
  elif ( prob == 8 ):
    fx1 = p08_fx1 ( x )
  elif ( prob == 9 ):
    fx1 = p09_fx1 ( x )
  elif ( prob == 10 ):
    fx1 = p10_fx1 ( x )
  elif ( prob == 11 ):
    fx1 = p11_fx1 ( x )
  elif ( prob == 12 ):
    fx1 = p12_fx1 ( x )
  elif ( prob == 13 ):
    fx1 = p13_fx1 ( x )
  elif ( prob == 14 ):
    fx1 = p14_fx1 ( x )
  elif ( prob == 15 ):
    fx1 = p15_fx1 ( x )
  elif ( prob == 16 ):
    fx1 = p16_fx1 ( x )
  elif ( prob == 17 ):
    fx1 = p17_fx1 ( x )
  elif ( prob == 18 ):
    fx1 = p18_fx1 ( x )
  elif ( prob == 19 ):
    fx1 = p19_fx1 ( x )
  else:
    print ( '' )
    print ( 'p00_fx1 - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_fx1 - Fatal error!' )

  return fx1

def p00_fx2 ( prob, x ):

#*****************************************************************************80
#
## p00_fx2: second derivative of a function specified by problem number.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the problem.
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  if ( prob == 1 ):
    fx2 = p01_fx2 ( x )
  elif ( prob == 2 ):
    fx2 = p02_fx2 ( x )
  elif ( prob == 3 ):
    fx2 = p03_fx2 ( x )
  elif ( prob == 4 ):
    fx2 = p04_fx2 ( x )
  elif ( prob == 5 ):
    fx2 = p05_fx2 ( x )
  elif ( prob == 6 ):
    fx2 = p06_fx2 ( x )
  elif ( prob == 7 ):
    fx2 = p07_fx2 ( x )
  elif ( prob == 8 ):
    fx2 = p08_fx2 ( x )
  elif ( prob == 9 ):
    fx2 = p09_fx2 ( x )
  elif ( prob == 10 ):
    fx2 = p10_fx2 ( x )
  elif ( prob == 11 ):
    fx2 = p11_fx2 ( x )
  elif ( prob == 12 ):
    fx2 = p12_fx2 ( x )
  elif ( prob == 13 ):
    fx2 = p13_fx2 ( x )
  elif ( prob == 14 ):
    fx2 = p14_fx2 ( x )
  elif ( prob == 15 ):
    fx2 = p15_fx2 ( x )
  elif ( prob == 16 ):
    fx2 = p16_fx2 ( x )
  elif ( prob == 17 ):
    fx2 = p17_fx2 ( x )
  elif ( prob == 18 ):
    fx2 = p18_fx2 ( x )
  elif ( prob == 19 ):
    fx2 = p19_fx2 ( x )
  else:
    print ( '' )
    print ( 'p00_fx2 - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_fx2 - Fatal error!' )

  return fx2

def p00_prob_num ( ):

#*****************************************************************************80
#
## p00_prob_num returns the number of problems available.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer PROB_num, the number of problems available.
#
  prob_num = 19

  return prob_num

def p00_rang ( prob ):

#*****************************************************************************80
#
## p00_rang returns an interval bounding the root for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the problem.
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  if ( prob == 1 ):
    rang = p01_rang ( )
  elif ( prob == 2 ):
    rang = p02_rang ( )
  elif ( prob == 3 ):
    rang = p03_rang ( )
  elif ( prob == 4 ):
    rang = p04_rang ( )
  elif ( prob == 5 ):
    rang = p05_rang ( )
  elif ( prob == 6 ):
    rang = p06_rang ( )
  elif ( prob == 7 ):
    rang = p07_rang ( )
  elif ( prob == 8 ):
    rang = p08_rang ( )
  elif ( prob == 9 ):
    rang = p09_rang ( )
  elif ( prob == 10 ):
    rang = p10_rang ( )
  elif ( prob == 11 ):
    rang = p11_rang ( )
  elif ( prob == 12 ):
    rang = p12_rang ( )
  elif ( prob == 13 ):
    rang = p13_rang ( )
  elif ( prob == 14 ):
    rang = p14_rang ( )
  elif ( prob == 15 ):
    rang = p15_rang ( )
  elif ( prob == 16 ):
    rang = p16_rang ( )
  elif ( prob == 17 ):
    rang = p17_rang ( )
  elif ( prob == 18 ):
    rang = p18_rang ( )
  elif ( prob == 19 ):
    rang = p19_rang ( )
  else:
    print ( '' )
    print ( 'p00_rang - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_rang - Fatal error!' )

  return rang

def p00_root ( prob, i ):

#*****************************************************************************80
#
## p00_root returns a known root for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the problem.
#
#    integer I, the index of the root to return.
#
#  Output:
#
#    real X, the I-th root.
#
  if ( prob == 1 ):
    x = p01_root ( i )
  elif ( prob == 2 ):
    x = p02_root ( i )
  elif ( prob == 3 ):
    x = p03_root ( i )
  elif ( prob == 4 ):
    x = p04_root ( i )
  elif ( prob == 5 ):
    x = p05_root ( i )
  elif ( prob == 6 ):
    x = p06_root ( i )
  elif ( prob == 7 ):
    x = p07_root ( i )
  elif ( prob == 8 ):
    x = p08_root ( i )
  elif ( prob == 9 ):
    x = p09_root ( i )
  elif ( prob == 10 ):
    x = p10_root ( i )
  elif ( prob == 11 ):
    x = p11_root ( i )
  elif ( prob == 12 ):
    x = p12_root ( i )
  elif ( prob == 13 ):
    x = p13_root ( i )
  elif ( prob == 14 ):
    x = p14_root ( i )
  elif ( prob == 15 ):
    x = p15_root ( i )
  elif ( prob == 16 ):
    x = p16_root ( i )
  elif ( prob == 17 ):
    x = p17_root ( i )
  elif ( prob == 18 ):
    x = p18_root ( i )
  elif ( prob == 19 ):
    x = p19_root ( i )
  else:
    print ( '' )
    print ( 'p00_root - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_root - Fatal error!' )

  return x

def p00_root_num ( prob ):

#*****************************************************************************80
#
## p00_root_num returns the number of known roots for a problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the problem.
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#    This value may be zero.
#
  if ( prob == 1 ):
    root_num = p01_root_num ( )
  elif ( prob == 2 ):
    root_num = p02_root_num ( )
  elif ( prob == 3 ):
    root_num = p03_root_num ( )
  elif ( prob == 4 ):
    root_num = p04_root_num ( )
  elif ( prob == 5 ):
    root_num = p05_root_num ( )
  elif ( prob == 6 ):
    root_num = p06_root_num ( )
  elif ( prob == 7 ):
    root_num = p07_root_num ( )
  elif ( prob == 8 ):
    root_num = p08_root_num ( )
  elif ( prob == 9 ):
    root_num = p09_root_num ( )
  elif ( prob == 10 ):
    root_num = p10_root_num ( )
  elif ( prob == 11 ):
    root_num = p11_root_num ( )
  elif ( prob == 12 ):
    root_num = p12_root_num ( )
  elif ( prob == 13 ):
    root_num = p13_root_num ( )
  elif ( prob == 14 ):
    root_num = p14_root_num ( )
  elif ( prob == 15 ):
    root_num = p15_root_num ( )
  elif ( prob == 16 ):
    root_num = p16_root_num ( )
  elif ( prob == 17 ):
    root_num = p17_root_num ( )
  elif ( prob == 18 ):
    root_num = p18_root_num ( )
  elif ( prob == 19 ):
    root_num = p19_root_num ( )
  else:
    print ( '' )
    print ( 'p00_root_num - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_root_num - Fatal error!' )

  return root_num

def p00_start ( prob, i ):

#*****************************************************************************80
#
## p00_start returns a starting point for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the problem.
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( prob == 1 ):
    x = p01_start ( i )
  elif ( prob == 2 ):
    x = p02_start ( i )
  elif ( prob == 3 ):
    x = p03_start ( i )
  elif ( prob == 4 ):
    x = p04_start ( i )
  elif ( prob == 5 ):
    x = p05_start ( i )
  elif ( prob == 6 ):
    x = p06_start ( i )
  elif ( prob == 7 ):
    x = p07_start ( i )
  elif ( prob == 8 ):
    x = p08_start ( i )
  elif ( prob == 9 ):
    x = p09_start ( i )
  elif ( prob == 10 ):
    x = p10_start ( i )
  elif ( prob == 11 ):
    x = p11_start ( i )
  elif ( prob == 12 ):
    x = p12_start ( i )
  elif ( prob == 13 ):
    x = p13_start ( i )
  elif ( prob == 14 ):
    x = p14_start ( i )
  elif ( prob == 15 ):
    x = p15_start ( i )
  elif ( prob == 16 ):
    x = p16_start ( i )
  elif ( prob == 17 ):
    x = p17_start ( i )
  elif ( prob == 18 ):
    x = p18_start ( i )
  elif ( prob == 19 ):
    x = p19_start ( i )
  else:
    print ( '' )
    print ( 'p00_start - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_start - Fatal error!' )

  return x

def p00_start_num ( prob ):

#*****************************************************************************80
#
## p00_start_num returns the number of starting points for a problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the problem.
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  if ( prob == 1 ):
    start_num = p01_start_num ( )
  elif ( prob == 2 ):
    start_num = p02_start_num ( )
  elif ( prob == 3 ):
    start_num = p03_start_num ( )
  elif ( prob == 4 ):
    start_num = p04_start_num ( )
  elif ( prob == 5 ):
    start_num = p05_start_num ( )
  elif ( prob == 6 ):
    start_num = p06_start_num ( )
  elif ( prob == 7 ):
    start_num = p07_start_num ( )
  elif ( prob == 8 ):
    start_num = p08_start_num ( )
  elif ( prob == 9 ):
    start_num = p09_start_num ( )
  elif ( prob == 10 ):
    start_num = p10_start_num ( )
  elif ( prob == 11 ):
    start_num = p11_start_num ( )
  elif ( prob == 12 ):
    start_num = p12_start_num ( )
  elif ( prob == 13 ):
    start_num = p13_start_num ( )
  elif ( prob == 14 ):
    start_num = p14_start_num ( )
  elif ( prob == 15 ):
    start_num = p15_start_num ( )
  elif ( prob == 16 ):
    start_num = p16_start_num ( )
  elif ( prob == 17 ):
    start_num = p17_start_num ( )
  elif ( prob == 18 ):
    start_num = p18_start_num ( )
  elif ( prob == 19 ):
    start_num = p19_start_num ( )
  else:
    print ( '' )
    print ( 'p00_start_num - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_start_num - Fatal error!' )

  return start_num

def p00_title ( prob ):

#*****************************************************************************80
#
## p00_title returns the title for a given problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the problem.
#
#  Output:
#
#    string TITLE, the title of the given problem.
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
  elif ( prob == 9 ):
    title = p09_title ( )
  elif ( prob == 10 ):
    title = p10_title ( )
  elif ( prob == 11 ):
    title = p11_title ( )
  elif ( prob == 12 ):
    title = p12_title ( )
  elif ( prob == 13 ):
    title = p13_title ( )
  elif ( prob == 14 ):
    title = p14_title ( )
  elif ( prob == 15 ):
    title = p15_title ( )
  elif ( prob == 16 ):
    title = p16_title ( )
  elif ( prob == 17 ):
    title = p17_title ( )
  elif ( prob == 18 ):
    title = p18_title ( )
  elif ( prob == 19 ):
    title = p19_title ( )
  else:
    print ( '' )
    print ( 'p00_title - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    raise Exception ( 'p00_title - Fatal error!' )

  return title

def p01_fx ( x ):

#*****************************************************************************80
#
## p01_fx evaluates sin ( x ) - x / 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  import numpy as np

  fx = np.sin ( x ) - 0.5 * x

  return fx

def p01_fx1 ( x ):

#*****************************************************************************80
#
## p01_fx1 evaluates the derivative of the function for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  import numpy as np

  fx1 = np.cos ( x ) - 0.5

  return fx1

def p01_fx2 ( x ):

#*****************************************************************************80
#
## p01_fx2 evaluates the second derivative of the function for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  import numpy as np

  fx2 = - np.sin ( x )

  return fx2

def p01_rang ( ):

#*****************************************************************************80
#
## p01_rang returns an interval bounding the root for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ -1000.0, 1001.0 ] )

  return rang

def p01_root ( i ):

#*****************************************************************************80
#
## p01_root returns a root for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  if ( ( i % 3 ) == 1 ):
    x = - 1.895494267033981
  elif ( ( i % 3 ) == 2 ):
    x = 0.0
  elif ( ( i % 3 ) == 0 ):
    x = 1.895494267033981

  return x

def p01_root_num ( ):

#*****************************************************************************80
#
## p01_root_num returns the number of known roots for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 3

  return root_num

def p01_start ( i ):

#*****************************************************************************80
#
## p01_start returns a starting point for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  import numpy as np

  if ( ( i % 2 ) == 1 ):
    x = 0.5 * np.pi
  elif ( ( i % 2 ) == 0 ):
    x = np.pi

  return x

def p01_start_num ( ):

#*****************************************************************************80
#
## p01_start_num returns the number of starting points for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 2

  return start_num

def p01_title ( title ):

#*****************************************************************************80
#
## p01_title returns the title of problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'F(X) = SIN(X) - 0.5 * X'

  return title

def p02_fx ( x ):

#*****************************************************************************80
#
## p02_fx evaluates 2 * x - exp ( - x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  import numpy as np

  fx = 2.0 * x - np.exp ( - x )

  return fx

def p02_fx1 ( x ):

#*****************************************************************************80
#
## p02_fx1 evaluates the derivative of the function for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  import numpy as  np

  fx1 = 2.0 + np.exp ( - x )

  return fx1

def p02_fx2 ( x ):

#*****************************************************************************80
#
## p02_fx2 evaluates the second derivative of the function for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  import numpy as np

  fx2 = - np.exp ( - x )

  return fx2

def p02_rang ( ):

#*****************************************************************************80
#
## p02_rang returns an interval bounding the root for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ -10.0, 100.0 ] )

  return rang

def p02_root ( i ):

#*****************************************************************************80
#
## p02_root returns a root for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 0.35173371124919584

  return x

def p02_root_num ( ):

#*****************************************************************************80
#
## p02_root_num returns the number of known roots for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p02_start ( i ):

#*****************************************************************************80
#
## p02_start returns a starting point for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 4 ) == 1 ):
    x = 0.0
  elif ( ( i % 4 ) == 2 ):
    x = 1.0
  elif ( ( i % 4 ) == 3 ):
    x = -5.0
  elif ( ( i % 4 ) == 0 ):
    x = 10.0

  return x

def p02_start_num ( ):

#*****************************************************************************80
#
## p02_start_num returns the number of starting points for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 4

  return start_num

def p02_title ( title ):

#*****************************************************************************80
#
## p02_title returns the title of problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'F(X) = 2 * X - EXP ( - X )'

  return title

def p03_fx ( x ):

#*****************************************************************************80
#
## p03_fx evaluates x * exp ( - x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#    real FX(*), the value of the function at X.
#
  import numpy as np

  fx = x * np.exp ( - x )

  return fx

def p03_fx1 ( x ):

#*****************************************************************************80
#
## p03_fx1 evaluates the derivative of the function for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  import numpy as np

  fx1 = np.exp ( - x ) * ( 1.0 - x )

  return fx1

def p03_fx2 ( x ):

#*****************************************************************************80
#
## p03_fx2 evaluates the second derivative of the function for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  import numpy as np

  fx2 = np.exp ( - x ) * ( x - 2.0 )

  return fx2

def p03_rang ( ):

#*****************************************************************************80
#
## p03_rang returns an interval bounding the root for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ -10.0, 100.0 ] )

  return rang

def p03_root ( i ):

#*****************************************************************************80
#
## p03_root returns a root for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 0.0

  return x

def p03_root_num ( ):

#*****************************************************************************80
#
## p03_root_num returns the number of known roots for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p03_start ( i ):

#*****************************************************************************80
#
## p03_start returns a starting point for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 3 ) == 1 ):
    x = -1.0
  elif ( ( i % 3 ) == 2 ):
    x =  0.5
  elif ( ( i % 3 ) == 0 ):
    x =  2.0

  return x

def p03_start_num ( ):

#*****************************************************************************80
#
## p03_start_num returns the number of starting points for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 3

  return start_num

def p03_title ( title ):

#*****************************************************************************80
#
## p03_title returns the title of problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'F(X) = X * EXP ( - X )'

  return title

def p04_fx ( x ):

#*****************************************************************************80
#
## p04_fx evaluates exp ( x ) - 1 / ( 10 * x )^2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  import numpy as np

  fx = np.exp ( x ) - 1.0 / ( 100.0 * x * x )

  return fx

def p04_fx1 ( x ):

#*****************************************************************************80
#
## p04_fx1 evaluates the derivative of the function for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  import numpy as np

  fx1 = np.exp ( x ) + 2.0 / ( 100.0 * x * x * x )

  return fx1

def p04_fx2 ( x ):

#*****************************************************************************80
#
## p04_fx2 evaluates the second derivative of the function for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  import numpy as np

  fx2 = np.exp ( x ) - 6.0 / ( 100.0 * x * x * x * x )

  return fx2

def p04_rang ( ):

#*****************************************************************************80
#
## p04_rang returns an interval bounding the root for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ 0.00001, 20.0 ] )

  return rang

def p04_root ( i ):

#*****************************************************************************80
#
## p04_root returns a root for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 0.09534461720025875

  return x

def p04_root_num ( ):

#*****************************************************************************80
#
## p04_root_num returns the number of known roots for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p04_start ( i ):

#*****************************************************************************80
#
## p04_start returns a starting point for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 2 ) == 1 ):
    x = 0.03
  elif ( ( i % 2 ) == 0 ):
    x = 1.0

  return x

def p04_start_num ( ):

#*****************************************************************************80
#
## p04_start_num returns the number of starting points for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 2

  return start_num

def p04_title ( title ):

#*****************************************************************************80
#
## p04_title returns the title of problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'F(X) = EXP ( X ) - 1 / ( 10 * X )^2'

  return title

def p05_fx ( x ):

#*****************************************************************************80
#
## p05_fx evaluates ( x + 3 ) * ( x - 1 )^2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  fx = ( x + 3.0 ) * ( x - 1.0 ) * ( x - 1.0 )

  return fx

def p05_fx1 ( x ):

#*****************************************************************************80
#
## p05_fx1 evaluates the derivative of the function for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  fx1 = ( 3.0 * x + 5.0 ) * ( x - 1.0 )

  return fx1

def p05_fx2 ( x ):

#*****************************************************************************80
#
## p05_fx2 evaluates the second derivative of the function for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  fx2 = 6.0 * x + 2.0

  return fx2

def p05_rang ( ):

#*****************************************************************************80
#
## p05_rangE returns an interval bounding the root for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ -1000.0, 1000.0 ] )

  return rang

def p05_root ( i ):

#*****************************************************************************80
#
## p05_root returns a root for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  if ( ( i % 3 ) == 1 ):
    x = - 3.0
  elif ( ( i % 3 ) == 2 ):
    x = 1.0
  elif ( ( i % 3 ) == 0 ):
    x = 1.0

  return x

def p05_root_num ( ):

#*****************************************************************************80
#
## p05_root_num returns the number of known roots for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 3

  return root_num

def p05_start ( i ):

#*****************************************************************************80
#
## p05_start returns a starting point for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 2 ) == 1 ):
    x =  2.0
  elif ( ( i % 2 ) == 0 ):
    x = - 5.0

  return x

def p05_start_num ( ):

#*****************************************************************************80
#
## p05_start_num returns the number of starting points for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 2

  return start_num

def p05_title ( title ):

#*****************************************************************************80
#
## p05_title returns the title of problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'F(X) = ( X + 3 ) * ( X - 1 )^2'

  return title

def p06_fx ( x ):

#*****************************************************************************80
#
## p06_fx evaluates exp ( x ) - 2 - 1 / ( 10 * x )^2 + 2 / ( 100 * x )^3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  import numpy as np

  fx = np.exp ( x ) - 2.0 - 1.0 / ( 10.0 * x ) ** 2 + 2.0 / ( 100.0 * x ) ** 3

  return fx

def p06_fx1 ( x ):

#*****************************************************************************80
#
## p06_fx1 evaluates the derivative of the function for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  import numpy as np

  fx1 = np.exp ( x ) + 2.0 / ( 100.0 * x ** 3 ) - 6.0 / ( 1000000.0 * x ** 4 )

  return fx1

def p06_fx2 ( x ):

#*****************************************************************************80
#
## p06_fx2 evaluates the second derivative of the function for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  import numpy as np

  fx2 = np.exp ( x ) - 6.0 / ( 100.0 * x ** 4 ) + 24.0 / ( 1000000.0 * x ** 5 )

  return fx2

def p06_rang ( ):

#*****************************************************************************80
#
## p06_rang returns an interval bounding the root for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ 0.00001, 20.0 ] )

  return rang

def p06_root ( i ):

#*****************************************************************************80
#
## p06_root returns a root for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 0.7032048403631358

  return x

def p06_root_num ( ):

#*****************************************************************************80
#
## p06_root_num returns the number of known roots for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:7
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p06_start ( i ):

#*****************************************************************************80
#
## p06_start returns a starting point for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 2 ) == 1 ):
    x = 0.0002
  elif ( ( i % 2 ) == 0 ):
    x = 2.0

  return x

def p06_start_num ( ):

#*****************************************************************************80
#
## p06_start_num returns the number of starting points for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 2

  return start_num

def p06_title ( title ):

#*****************************************************************************80
#
## p06_title returns the title of problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'F(X) = EXP(X) - 2 - 1 / ( 10 * X )^2 - 2 / ( 100 * X )^3'

  return title

def p07_fx ( x ):

#*****************************************************************************80
#
## p07_fx evaluates the function for problem 07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  fx = x ** 3

  return fx

def p07_fx1 ( x ):

#*****************************************************************************80
#
## p07_fx1 evaluates the derivative of the function for problem 7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  fx1 = 3.0 * x ** 2

  return fx1

def p07_fx2 ( x ):

#*****************************************************************************80
#
## p07_fx2 evaluates the second derivative of the function for problem 7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  fx2 = 6.0 * x

  return fx2

def p07_rang ( ):

#*****************************************************************************80
#
## p07_rang returns an interval bounding the root for problem 7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ -1000.0, 999.0 ] )

  return rang

def p07_root ( i ):

#*****************************************************************************80
#
## p07_root returns a root for problem 7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 0.0

  return x

def p07_root_num ( ):

#*****************************************************************************80
#
## p07_root_num returns the number of known roots for problem 7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p07_start ( i ):

#*****************************************************************************80
#
## p07_start returns a starting point for problem 7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 2 ) == 1 ):
    x = 1.0
  elif ( ( i % 2 ) == 0 ):
    x = -1000.0

  return x

def p07_start_num ( ):

#*****************************************************************************80
#
## p07_start_num returns the number of starting points for problem 7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 2

  return start_num

def p07_title ( title ):

#*****************************************************************************80
#
## p07_title returns the title of problem 7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'F(X) = X^3, only linear Newton convergence.'

  return title

def p08_fx ( x ):

#*****************************************************************************80
#
## p08_fx evaluates cos ( x ) - x.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  import numpy as np

  fx = np.cos ( x ) - x

  return fx

def p08_fx1 ( x ):

#*****************************************************************************80
#
## p08_fx1 evaluates the derivative of the function for problem 8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  import numpy as np

  fx1 = - np.sin ( x ) - 1.0

  return fx1

def p08_fx2 ( x ):

#*****************************************************************************80
#
## p08_fx2 evaluates the second derivative of the function for problem 8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  import numpy as np

  fx2 = - np.cos ( x )

  return fx2

def p08_rang ( ):

#*****************************************************************************80
#
## p08_rang returns an interval bounding the root for problem 8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ - 10.0, 10.0 ] )

  return rang

def p08_root ( i ):

#*****************************************************************************80
#
## p08_root returns a root for problem 8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 0.7390851332151607

  return x

def p08_root_num ( ):

#*****************************************************************************80
#
## p08_root_num returns the number of known roots for problem 8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p08_start ( i ):

#*****************************************************************************80
#
## p08_start returns a starting point for problem 8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 3 ) == 1 ):
    x = 1.0
  elif ( ( i % 3 ) == 2 ):
    x = 0.5
  elif ( ( i % 3 ) == 0 ):
    x = - 1.6

  return x

def p08_start_num ( ):

#*****************************************************************************80
#
## p08_start_num returns the number of starting points for problem 8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 3

  return start_num

def p08_title ( title ):

#*****************************************************************************80
#
## p08_title returns the title of problem 8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'F(X) = COS(X) - X'

  return title

def p09_fx ( x ):

#*****************************************************************************80
#
## p09_fx evaluates the Newton Baffler.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  fx = 0.0

  if ( x < 6.0 ):
    fx = 0.75 * ( x - 6.25 ) - 0.3125
  elif ( x <= 6.50 ):
    fx = 2.00 * ( x - 6.25 )
  else:
    fx = 0.75 * ( x - 6.25 ) + 0.3125

  return fx

def p09_fx1 ( x ):

#*****************************************************************************80
#
## p09_fx1 evaluates the derivative of the function for problem 9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  x2 = x - 6.25

  if ( x2 < - 0.25 ):
    fx1 = 0.75
  elif ( x2 < 0.25 ):
    fx1 = 2.0
  else:
    fx1 = 0.75

  return fx1

def p09_fx2 ( x ):

#*****************************************************************************80
#
## p09_fx2 evaluates the second derivative of the function for problem 9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 September 1999
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  fx2 = 0.0

  return fx2

def p09_rang ( ):

#*****************************************************************************80
#
## p09_rang returns an interval bounding the root for problem 9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ - 5.0, + 16.0 ] )

  return rang

def p09_root ( i ):

#*****************************************************************************80
#
## p09_root returns a root for problem 9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 6.25

  return x

def p09_root_num ( ):

#*****************************************************************************80
#
## p09_root_num returns the number of known roots for problem 9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p09_start ( i ):

#*****************************************************************************80
#
## p09_start returns a starting point for problem 9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 3 ) == 1 ):
    x = 6.25 + 5.0
  elif ( ( i % 3 ) == 2 ):
    x = 6.25 - 1.0
  elif ( ( i % 3 ) == 0 ):
    x = 6.25 + 0.1

  return x

def p09_start_num ( ):

#*****************************************************************************80
#
## p09_start_num returns the number of starting points for problem 9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 3

  return start_num

def p09_title ( title ):

#*****************************************************************************80
#
## p09_title returns the title of problem 9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'The Newton Baffler'

  return title

def p10_fx ( x ):

#*****************************************************************************80
#
## p10_fx evaluates the Repeller.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  fx = 20.0 * x / ( 100.0 * x * x + 1.0 )

  return fx

def p10_fx1 ( x ):

#*****************************************************************************80
#
## p10_fx1 evaluates the derivative of the function for problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  fx1 = ( 1.0 - 10.0 * x ) * ( 1.0 + 10.0 * x ) / ( 100.0 * x * x + 1.0 ) ** 2

  return fx1

def p10_fx2 ( x ):

#*****************************************************************************80
#
## p10_fx2 evaluates the second derivative of the function for problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  fx2 = - 200.0 * x * ( 3.0 - 100.0 * x ** 2 ) / ( 100.0 * x * x + 1.0 ) ** 3

  return fx2

def p10_rang ( ):

#*****************************************************************************80
#
## p10_rang returns an interval bounding the root for problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ - 10.0, + 11.0 ] )

  return rang

def p10_root ( i ):

#*****************************************************************************80
#
## p10_root returns a root for problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 0.0

  return x

def p10_root_num ( ):

#*****************************************************************************80
#
## p10_root_num returns the number of known roots for problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p10_start ( i ):

#*****************************************************************************80
#
## p10_start returns a starting point for problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 3 ) == 1 ):
    x = 1.0
  elif ( ( i % 3 ) == 2 ):
    x = - 0.14
  elif ( ( i % 3 ) == 0 ):
    x = 0.041

  return x

def p10_start_num ( ):

#*****************************************************************************80
#
## p10_start_num returns the number of starting points for problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 3

  return start_num

def p10_title ( title ):

#*****************************************************************************80
#
## p10_title returns the title of problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'The Repeller'

  return title

def p11_fx ( x ):

#*****************************************************************************80
#
## p11_fx evaluates the Pinhead.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  epsilon = 0.00001

  fx = ( 16.0 - x ** 4 ) / ( 16.0 * x ** 4 + epsilon )

  return fx

def p11_fx1 ( x ):

#*****************************************************************************80
#
## p11_fx1 evaluates the derivative of the function for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  epsilon = 0.00001

  fx1 = - 4.0 * x ** 3 * ( epsilon + 256.0 ) / ( 16.0 * x ** 4 + epsilon ) ** 2

  return fx1

def p11_fx2 ( x ):

#*****************************************************************************80
#
## p11_fx2 evaluates the second derivative of the function for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  epsilon = 0.00001

  fx2 = - 4.0 * ( epsilon + 256.0 ) \
    * ( 3.0 * epsilon - 80.0 * x ** 4 ) * x ** 2 \
    / ( 16.0 * x ** 4 + epsilon ) ** 3

  return fx2

def p11_rang ( ):

#*****************************************************************************80
#
## p11_rang returns an interval bounding the root for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ 0.0, + 10.0 ] )
 
  return rang

def p11_root ( i ):

#*****************************************************************************80
#
## p11_root returns a root for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  if (  ( i % 2 ) == 1 ):
    x = - 2.0
  elif ( ( i % 2 ) == 0 ):
    x = 2.0

  return x

def p11_root_num ( ):

#*****************************************************************************80
#
## p11_root_num returns the number of known roots for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 2

  return root_num

def p11_start ( i ):

#*****************************************************************************80
#
## p11_start returns a starting point for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 3 ) == 1 ):
    x = 0.25
  elif ( ( i % 3 ) == 2 ):
    x = 5.0
  elif ( ( i % 3 ) == 0 ):
    x = 1.1

  return x

def p11_start_num ( ):

#*****************************************************************************80
#
## p11_start_num returns the number of starting points for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 3

  return start_num

def p11_title ( title ):

#*****************************************************************************80
#
## p11_title returns the title of problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'The Pinhead'

  return title

def p12_fx ( x ):

#*****************************************************************************80
#
## p12_fx evaluates Flat Stanley.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  import numpy as np

  factor = 1000.0

  if ( x == 1.0 ):
    fx = 0.0
  elif ( x < 1.0 ):
    fx = - np.exp ( np.log ( factor ) + np.log ( abs ( x - 1.0 ) ) - 1.0 / ( x - 1.0 ) ** 2 )
  elif ( 1.0 < x ):
    fx = + np.exp ( np.log ( factor ) + np.log ( abs ( x - 1.0 ) ) - 1.0 / ( x - 1.0 ) ** 2 )

  return fx

def p12_fx1 ( x ):

#*****************************************************************************80
#
## p12_fx1 evaluates the derivative of the function for problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  import numpy as np

  factor = 1000.0

  if ( x == 1.0 ):
    fx1 = 0.0
  else:
    y = x - 1.0
    fx1 = factor * np.exp ( - 1.0 / y ** 2 ) * ( y ** 2 + 2.0 ) / y ** 2

  return fx1

def p12_fx2 ( x ):

#*****************************************************************************80
#
## p12_fx2 evaluates the second derivative of the function for problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  import numpy as np

  factor = 1000.0

  if ( x == 1.0 ):
    fx2 = 0.0
  else:
    y = x - 1.0
    fx2 = - 2.0 * factor * np.exp ( - 1.0 / y ** 2 ) * ( y ** 2 - 2.0 ) / y ** 5

  return fx2

def p12_rang ( ):

#*****************************************************************************80
#
## p12_rang returns an interval bounding the root for problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ - 4.0, + 4.1 ] )

  return rang

def p12_root ( i ):

#*****************************************************************************80
#
## p12_root returns a root for problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 1.0

  return x

def p12_root_num ( ):

#*****************************************************************************80
#
## p12_root_num returns the number of known roots for problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p12_start ( i ):

#*****************************************************************************80
#
## p12_start returns a starting point for problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 3 ) == 1 ):
    x = 2.0
  elif ( ( i % 3 ) == 2 ):
    x = 0.50
  elif ( ( i % 3 ) == 0 ):
    x = 4.0

  return x

def p12_start_num ( ):

#*****************************************************************************80
#
## p12_start_num returns the number of starting points for problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 3

  return start_num

def p12_title ( title ):

#*****************************************************************************80
#
## p12_title returns the title of problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Flat Stanley (ALL derivatives are zero at the root.)'

  return title

def p13_fx ( x ):

#*****************************************************************************80
#
## p13_fx evaluates Lazy Boy.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  slope = 0.00000000001

  fx = slope * ( x - 100.0 )

  return fx

def p13_fx1 ( x ):

#*****************************************************************************80
#
## p13_fx1 evaluates the derivative of the function for problem 13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  slope = 0.00000000001

  fx1 = slope

  return fx1

def p13_fx2 ( x ):

#*****************************************************************************80
#
## p13_fx2 evaluates the second derivative of the function for problem 13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  fx2 = 0.0

  return fx2

def p13_rang ( ):

#*****************************************************************************80
#
## p13_rang returns an interval bounding the root for problem 13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ - 10000000000000.0, 10000000000000.0 ] )

  return rang

def p13_root ( i ):

#*****************************************************************************80
#
## p13_root returns a root for problem 13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 100.0

  return x

def p13_root_num ( ):

#*****************************************************************************80
#
## p13_root_num returns the number of known roots for problem 13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p13_start ( i ):

#*****************************************************************************80
#
## p13_start returns a starting point for problem 13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 3 ) == 1 ):
    x = 100000000.0
  elif ( ( i % 3 ) == 2 ):
    x = - 100000000000.0
  elif ( ( i % 3 ) == 0 ):
    x = 100000013.0

  return x

def p13_start_num ( ):

#*****************************************************************************80
#
## p13_start_num returns the number of starting points for problem 13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 3

  return start_num

def p13_title ( title ):

#*****************************************************************************80
#
## p13_title returns the title of problem 13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Lazy Boy (Linear function, almost flat.)'

  return title

def p14_fx ( x ):

#*****************************************************************************80
#
## p14_fx evaluates the Camel.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  fx =   1.0 / ( ( x - 0.3 ) ** 2 + 0.01 ) \
       + 1.0 / ( ( x - 0.9 ) ** 2 + 0.04 ) \
       + 2.0 * x - 5.2

  return fx

def p14_fx1 ( x ):

#*****************************************************************************80
#
## p14_fx1 evaluates the derivative of the function for problem 14.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  fx1 = - 2.0 * ( x - 0.3 ) / ( ( x - 0.3 ) ** 2 + 0.01 ) ** 2 \
        - 2.0 * ( x - 0.9 ) / ( ( x - 0.9 ) ** 2 + 0.04 ) ** 2 \
        + 2.0

  return fx1

def p14_fx2 ( x ):

#*****************************************************************************80
#
## p14_fx2 evaluates the second derivative of the function for problem 14.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  t1 = - 2.0
  b1 = ( 0.04 + ( x - 0.9 ) ** 2 ) ** 2

  t2 = 8.0 * ( x - 0.9 ) ** 2
  b2 = ( 0.04 + ( x - 0.9 ) ** 2 ) ** 3

  t3 = 80.0 * ( 3.0 - 10.0 * x ) ** 2
  b3 = ( 1.0 - 6.0 * x + 10.0 * x ** 2 ) ** 3

  t4 = - 200.0
  b4 = ( 1.0 - 6.0 * x + 10.0 * x ** 2 ) ** 2

  fx2 = t1 / b1 + t2 / b2 + t3 / b3 + t4 / b4

  return fx2

def p14_rang ( ):

#*****************************************************************************80
#
## p14_rang returns an interval bounding the root for problem 14.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ - 10.0, 10.0 ] )

  return rang

def p14_root ( i ):

#*****************************************************************************80
#
## p14_root returns a root for problem 14.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  if ( ( i % 3 ) == 1 ):
    x = - 0.1534804948126991
  elif ( ( i % 3 ) == 2 ):
    x = 1.8190323925159182
  elif ( ( i % 3 ) == 0 ):
    x = 2.1274329318603367

  return x

def p14_root_num ( ):

#*****************************************************************************80
#
## p14_root_num returns the number of known roots for problem 14.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 3

  return root_num

def p14_start ( i ):

#*****************************************************************************80
#
## p14_start returns a starting point for problem 14.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 4 ) == 1 ):
    x = 3.0
  elif ( ( i % 4 ) == 2 ):
    x = - 0.5
  elif ( ( i % 4 ) == 3 ):
    x = 0.0
  elif ( ( i % 3 ) == 0 ):
    x = 2.12742

  return x

def p14_start_num ( ):

#*****************************************************************************80
#
## p14_start_num returns the number of starting points for problem 14.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 4

  return start_num

def p14_title ( title ):

#*****************************************************************************80
#
## p14_title returns the title of problem 14.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'The Camel (double hump and some shallow roots.)'

  return title

def p15_fx ( x ):

#*****************************************************************************80
#
## p15_fx evaluates a pathological function for Newton's method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 July 2011
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Donovan, Arnold Miller, Timothy Moreland,
#    Pathological Functions for Newton's Method,
#    American Mathematical Monthly, January 1993, pages 53-58.
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  import numpy as np

  if ( x < 0.0 ):
    fx = - abs ( x ) ** ( 1.0 / 3.0 ) * np.exp ( - x ** 2 )
  elif ( x == 0.0 ):
    fx = 0.0
  elif ( 0.0 < x ):
    fx = abs ( x ) ** ( 1.0 / 3.0 ) * np.exp ( - x ** 2 )

  return fx

def p15_fx1 ( x ):

#*****************************************************************************80
#
## p15_fx1 evaluates the derivative of the function for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  import numpy as np

  fx1 = ( 1.0 - 6.0 * x ** 2 ) * r8_cube_root ( x ) * np.exp ( - x ** 2 ) \
    / ( 3.0 * x )

  return fx1

def p15_fx2 ( x ):

#*****************************************************************************80
#
## p15_fx2 evaluates the second derivative of the function for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  import numpy as np

  fx2 = ( - 2.0 - 30.0 * x ** 2 + 36.0 * x ** 4 ) * r8_cube_root ( x ) \
    * exp ( - x ** 2 ) / ( 9.0 * x ** 2 )

  return fx2

def p15_rang ( ):

#*****************************************************************************80
#
## p15_rang returns an interval bounding the root for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ - 10.0, 10.0 ] )

  return rang

def p15_root ( i ):

#*****************************************************************************80
#
## p15_root returns a root for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 0.0

  return x

def p15_root_num ( ):

#*****************************************************************************80
#
## p15_root_num returns the number of known roots for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p15_start ( i ):

#*****************************************************************************80
#
## p15_start returns a starting point for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 2 ) == 1 ):
    x = 0.01
  elif ( ( i % 2 ) == 0 ):
    x = - 0.25

  return x

def p15_start_num ( ):

#*****************************************************************************80
#
## p15_start_num returns the number of starting points for problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 2

  return start_num

def p15_title ( title ):

#*****************************************************************************80
#
## p15_title returns the title of problem 15.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Donovan/Miller/Moreland Pathological Function'

  return title

def p16_fx ( x ):

#*****************************************************************************80
#
## p16_fx evaluates Kepler's Equation.
#
#  Discussion:
#
#    This is Kepler's equation.  The equation has the form:
#
#      X = M + E * sin ( X )
#
#    X represents the eccentric anomaly of a planet, the angle between the
#    perihelion (the point on the orbit nearest to the sun)
#    through the sun to the center of the ellipse, and the
#    line from the center of the ellipse to the planet.
#
#    There are two Input:
#
#    E is the eccentricity of the orbit, which should be between 0 and 1.0
#
#    M is the angle from the perihelion made by a fictitious planet traveling
#    on a circular orbit centered at the sun, and traveling at a constant
#    angular velocity equal to the average angular velocity of the true planet.
#    M is usually between 0 and 180 degrees, but can have any value.
#
#    For convenience, X and M are measured in degrees.
#
#    Sample results:
#
#    E        M      X
#    -----  ---  ----------
#    0.100    5    5.554589
#    0.200    5    6.246908
#    0.300    5    7.134960
#    0.400    5    8.313903
#    0.500    5    9.950063
#    0.600    5   12.356653
#    0.700    5   16.167990
#    0.800    5   22.656579
#    0.900    5   33.344447
#    0.990    5   45.361023
#    0.990    1   24.725822
#    0.990   33   89.722155
#    0.750   70  110.302
#    0.990    2   32.361007
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Peter Colwell,
#    Solving Kepler's Equation Over Three Centuries,
#    Willmann-Bell, 1993
#
#    Jean Meeus,
#    Astronomical Algorithms,
#    Willman-Bell, Inc, 1991,
#    QB51.3.E43M42
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  import numpy as np

  e = 0.8
  m = 5.0

  fx = np.pi * ( x - m ) / 180.0 - e * np.sin ( np.pi * x / 180.0 )

  return fx

def p16_fx1 ( x ):

#*****************************************************************************80
#
## p16_fx1 evaluates the derivative of the function for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  import numpy as np

  e = 0.8
  m = 5.0

  fx1 = ( np.pi / 180.0 ) - e * np.pi * np.cos ( np.pi * x / 180.0  ) / 180.0

  return fx1

def p16_fx2 ( x ):

#*****************************************************************************80
#
## p16_fx2 evaluates the second derivative of the function for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative of the function at X.
#
  import numpy as np

  e = 0.8
  m = 5.0

  fx2 = e * np.pi ** 2 * np.sin ( np.pi * x / 180.0  ) / 180.0 / 180.0

  return fx2

def p16_rang ( ):

#*****************************************************************************80
#
## p16_rang returns an interval bounding the root for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  e = 0.8
  m = 5.0

  rang = np.array ( [ m - 180.0, m + 180.0 ] )

  return rang

def p16_root ( i ):

#*****************************************************************************80
#
## p16_root returns a root for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 22.65657866956775

  return x

def p16_root_num ( ):

#*****************************************************************************80
#
## p16_root_num returns the number of known roots for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 0

  return root_num

def p16_start ( i ):

#*****************************************************************************80
#
## p16_start returns a starting point for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  e = 0.8
  m = 5.0

  if ( ( i % 3 ) == 1 ):
    x = 0.0
  elif ( ( i % 3 ) == 2 ):
    x = m + 180.0
  elif ( ( i % 3 ) == 0 ):
    x = m

  return x

def p16_start_num ( ):

#*****************************************************************************80
#
## p16_start_num returns the number of starting points for problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 3

  return start_num

def p16_title ( title ):

#*****************************************************************************80
#
## p16_title returns the title of problem 16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Kepler''s Eccentric Anomaly Equation, in degrees'

  return title

def p17_fx ( x ):

#*****************************************************************************80
#
## p17_fx evaluates the function for problem 17.
#
#  Discussion:
#
#    This simple example is of historical interest, since it was used
#    by Wallis to illustrate the use of Newton's method, and has been
#    a common example ever since.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  fx = x ** 3 - 2.0 * x - 5.0

  return fx

def p17_fx1 ( x ):

#*****************************************************************************80
#
## p17_fx1 evaluates the derivative of the function for problem 17.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX1, the first derivative of the function at X.
#
  fx1 = 3.0 * x * x - 2.0

  return fx1

def p17_fx2 ( x ):

#*****************************************************************************80
#
## p17_fx2 evaluates the second derivative of the function for problem 17.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the abscissa.
#
#  Output:
#
#    real FX2, the second derivative at X.
#
  fx2 = 6.0 * x

  return fx2

def p17_rang ( ):

#*****************************************************************************80
#
## p17_rang returns an interval bounding the root for problem 17.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ 2.0, 3.0 ] )

  return rang

def p17_root ( i ):

#*****************************************************************************80
#
## p17_root returns a root for problem 17.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 2.0945514815423265

  return x

def p17_root_num ( ):

#*****************************************************************************80
#
## p17_root_num returns the number of known roots for problem 17.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p17_start ( i ):

#*****************************************************************************80
#
## p17_start returns a starting point for problem 17.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 2 ) == 1 ):
    x = 2.0
  elif ( ( i % 2 ) == 0 ):
    x = 3.0

  return x

def p17_start_num ( ):

#*****************************************************************************80
#
## p17_start_num returns the number of starting points for problem 17.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 2

  return start_num

def p17_title ( title ):

#*****************************************************************************80
#
## p17_title returns the title of problem 17.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'The Wallis example, x^3-2x-5=0'

  return title

def p18_fx ( x ):

#*****************************************************************************80
#
## p18_fx evaluates the function for problem 18.
#
#  Discussion:
#
#    F(X) = 10^14 * (x-1)^7, but is written in term by term form.
#
#    This polynomial becomes difficult to evaluate accurately when 
#    written this way.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2011
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
#    LC: QA297.M625.
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  horners = False

  if ( horners ):

    fx = 10.0 ** 14 * ( ( ( ( ( ( ( ( \
                  1.0 ) 
           * x -  7.0 ) 
           * x + 21.0 )
           * x - 35.0 )
           * x + 35.0 )
           * x - 21.0 )
           * x +  7.0 )
           * x -  1.0 )

  else:

    fx = 10.0 ** 14 * (
             1.0 * x ** 7 
          -  7.0 * x ** 6 
          + 21.0 * x ** 5
          - 35.0 * x ** 4
          + 35.0 * x ** 3
          - 21.0 * x ** 2
          +  7.0 * x
          -  1.0 )

  return fx

def p18_fx1 ( x ):

#*****************************************************************************80
#
## p18_fx1 evaluates the derivative of the function for problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX1(*), the value of the derivative at X.
#
  fx1 = 10.0 ** 14 * ( \
          7 * x ** 6 \
      -  42 * x ** 5 \
      + 105 * x ** 4 \
      - 140 * x ** 3 \
      + 105 * x ** 2 \
      -  42 * x ** 1 \
      +   7 )

  return fx1

def p18_fx2 ( x ):

#*****************************************************************************80
#
## p18_fx2 evaluates the second derivative of the function for problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX2(*), the value of the second derivative at X.
#
  fx2 = 10.0 ** 14 * ( \
         42 * x ** 5 \
      - 210 * x ** 4 \
      + 420 * x ** 3 \
      - 420 * x ** 2 \
      + 210 * x    \
      -  42 )

  return fx2

def p18_rang ( ):

#*****************************************************************************80
#
## p18_rang returns an interval bounding the root for problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ 0.988, 1.012 ] )

  return rang

def p18_root ( i ):

#*****************************************************************************80
#
## p18_root returns a root for problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 1.0

  return x

def p18_root_num ( ):

#*****************************************************************************80
#
## p18_root_num returns the number of known roots for problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p18_start ( i ):

#*****************************************************************************80
#
## p18_start returns a starting point for problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( i == 1 ):
    x = 0.990
  elif ( i == 2 ):
    x = 1.013

  return x

def p18_start_num ( ):

#*****************************************************************************80
#
## p18_start_num returns the number of starting points for problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 2

  return start_num

def p18_title ( title ):

#*****************************************************************************80
#
## p18_title returns the title of problem 18.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2011
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = '10^14 * (x-1)^7, written term by term.'

  return title

def p19_fx ( x ):

#*****************************************************************************80
#
## p19_fx evaluates the function for problem 19.
#
#  Discussion:
#
#    This function looks like an elevated cosine curve, connected by a 
#    sudden drop to a submerged cosine curve.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX(*), the value of the function at X.
#
  import numpy as np
  from scipy.special import erf

  fx = np.cos ( 100.0 * x ) - 4.0 * erf ( 30.0 * x - 10.0 )

  return fx

def p19_fx1 ( x ):

#*****************************************************************************80
#
## p19_fx1 evaluates the derivative of the function for problem 19.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX1(*), the value of the derivative at X.
#
  import numpy as np

  arg = - ( 10.0 - 30.0 * x ) ** 2

  fx1 = - 100.0 * np.sin ( 100.0 * x ) + 240.0 * np.exp ( arg ) \
    / np.sqrt ( np.pi )

  return fx1

def p19_fx2 ( x ):

#*****************************************************************************80
#
## p19_fx2 evaluates the second derivative of the function for problem 19.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the point at which F is to be evaluated.
#
#  Output:
#
#    real FX2(*), the value of the second derivative at X.
#
  import numpy as np

  arg = - ( 10.0 - 30.0 * x ) ** 2

  fx2 = - 10000.0 * np.cos ( 100.0 * x ) \
    + 14400.0 * np.exp ( arg ) * ( 10.0 - 30.0 * x ) / np.sqrt ( np.pi )

  return fx2

def p19_rang ( ):

#*****************************************************************************80
#
## p19_rang returns an interval bounding the root for problem 19.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  import numpy as np

  rang = np.array ( [ 0.0, 1.0 ] )

  return rang

def p19_root ( i ):

#*****************************************************************************80
#
## p19_root returns a root for problem 19.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the requested root.
#
#  Output:
#
#    real X, the value of the root.
#
  x = 0.33186603357456253747

  return x

def p19_root_num ( ):

#*****************************************************************************80
#
## p19_root_num returns the number of known roots for problem 19.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer ROOT_num, the number of known roots.
#
  root_num = 1

  return root_num

def p19_start ( i ):

#*****************************************************************************80
#
## p19_start returns a starting point for problem 19.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the starting point.
#
#  Output:
#
#    real X, the starting point.
#
  if ( ( i % 3 ) == 1 ):
    x = 0.0
  elif ( ( i % 3 ) == 2 ):
    x = 1.0
  elif ( ( i % 3 ) == 0 ):
    x = 0.5

  return x

def p19_start_num ( ):

#*****************************************************************************80
#
## p19_start_num returns the number of starting points for problem 19.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer START_num, the number of starting points.
#
  start_num = 3

  return start_num

def p19_title ( title ):

#*****************************************************************************80
#
## p19_title returns the title of problem 19.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'The jumping cosine'

  return title

def r8_cube_root ( x ):

#*****************************************************************************80
#
## r8_cube_root returns the cube root of an R8.
#
#  Discussion:
#
#    This routine is designed to avoid the possible problems that can occur
#    when formulas like 0.0^(1/3) or (-1.0)^(1/3) are to be evaluated.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose cube root is desired.
#
#  Output:
#
#    real VALUE, the cube root of X.
#
  if ( 0.0 < x ):
    value = x ** ( 1.0 / 3.0 )
  elif ( x == 0.0 ):
    value = 0.0;
  else:
    value = - ( abs ( x ) ) ** ( 1.0 / 3.0 )

  return value

def r8_cube_root_test ( ):

#*****************************************************************************80
#
## r8_cube_root_test tests r8_cube_root.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8_cube_root_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_cube_root computes the cube root of an R8.' )
  print ( '' )
  print ( '       X               Y               Y^3' )
  print ( '' )

  a = -10.0
  b = +10.0

  for i in range ( 0, 10 ):
    x1 = a + ( b - a ) * np.random.rand ( )
    y = r8_cube_root ( x1 )
    x2 = y ** 3
    print ( '  %14.6g  %14.6g  %14.6g' % ( x1, y, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_cube_root_test' )
  print ( '  Normal end of execution.' )
  return

def r8poly2_rroot ( a, b, c ):

#*****************************************************************************80
#
## r8poly2_rroot returns the real parts of the roots of a quadratic polynomial.
#
#  Example:
#
#    A    B    C       roots              R1   R2
#   --   --   --     ------------------   --   --
#    1   -4    3     1          3          1    3
#    1    0    4     2*i      - 2*i        0    0
#    1   -6   10     3 +   i    3 -   i    3    3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the coefficients of the quadratic
#    polynomial A * X^2 + B * X + C = 0 whose roots are desired.
#    A must not be zero.
#
#  Output:
#
#    real R1, R2, the real parts of the roots
#    of the polynomial.
#
  import numpy as np
 
  if ( a == 0.0 ):
    print ( '' )
    print ( 'r8poly2_rroot - Fatal error!' )
    print ( '  The coefficient A is zero.' )
    raise Exception ( 'r8poly2_rroot - Fatal error!' )

  disc = b * b - 4.0 * a * c

  if ( 0.0 <= disc ):
    q = ( b + r8_sign ( b ) * np.sqrt ( disc ) )
    r1 = - 0.5 * q / a
    r2 = - 2.0 * c / q
  else:
    r1 = - b / 2.0 / a
    r2 = - b / 2.0 / a

  return r1, r2

def r8poly2_rroot_test ( ):

#*****************************************************************************80
#
## r8poly2_rroot_test tests r8poly2_rroot.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 5

  a_test = np.array ( [  2.0,    1.0,  1.0, 1.0,  1.0 ] )
  b_test = np.array ( [ -2.0,  -20.0, -2.0, 0.0, -6.0 ] )
  c_test = np.array ( [ -24.0, 100.0, 10.0, 1.0, 10.0 ] )
 
  print ( '' )
  print ( 'r8poly2_rroot_test' )
  print ( '  r8poly2_rroot finds the real parts of quadratic equation roots.' )
  print ( '' )
  print ( '         A         B         C     R1         R2' )
  print ( '' )

  for test in range ( 0, test_num ):

    a = a_test[test]
    b = b_test[test]
    c = c_test[test]

    r1, r2 = r8poly2_rroot ( a, b, c )
 
    print ( '  %8.4f  %8.4f  %8.4f  %8.4f  %8.4f' % ( a, b, c, r1, r2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8poly2_rroot_test' )
  print ( '  Normal end of execution.' )
  return

def r8_sign ( x ):

#*****************************************************************************80
#
## r8_sign returns the sign of an R8.
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
## r8_sign_test tests r8_sign.
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
  print ( 'r8_sign_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sign returns the sign of an R8.' )
  print ( '' )
  print ( '     R8     r8_sign(R8)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_test[test]
    s = r8_sign ( r8 )
    print ( '  %8.4f  %8.0f' % ( r8, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_sign_test' )
  print ( '  Normal end of execution.' )
  return

def regula_falsi ( fatol, step_max, prob, xatol, xa, xb, fxa, fxb ):

#*****************************************************************************80
#
## regula_falsi carries out the Regula Falsi method to seek a root of F(X) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real FATOL, an absolute error tolerance for the
#    function value of the root.  If an approximate root X satisfies
#      ABS ( F ( X ) ) <= FATOL, then X will be accepted as the
#    root and the iteration will be terminated.
#
#    integer STEP_MAX, the maximum number of steps allowed
#    for an iteration.
#
#    integer PROB, the index of the function whose root is
#    to be sought.
#
#    real XATOL, an absolute error tolerance for the root.
#
#    real XA, XB, two points at which the 
#    function differs in sign.  
#
#    real FXA, FXB, the value of the function 
#    at XA and XB.
# 
#  Output:
#
#    real XA, XB, two updated points at which the 
#    function differs in sign.
#
#    real FXA, FXB, the value of the function at XA and XB.
# 

#
#  The method requires a change-of-sign interval.
#
  if ( r8_sign ( fxa ) == r8_sign ( fxb ) ):
    print ( '' )
    print ( 'regula_falsi - Fatal error!' )
    print ( '  Function does not change sign at endpoints.' )
    raise Exception ( 'regula_falsi - Fatal error!' )
#
#  Make A the root with negative F, B the root with positive F.
#
  if ( 0.0 < fxa ):
    t = xa
    xa = xb
    xb = t
    t = fxa
    fxa = fxb
    fxb = t

  print ( '' )
  print ( 'REGULA FALSI' )
  print ( '' )
  print ( '  Step            XA            XB             F(XA)         F(XB)' )
  print ( '' )

  step_num = 0
  print ( '  %4d  %14g  %14g  %14g  %14g' % ( step_num, xa, xb, fxa, fxb ) )

  for step_num in range ( 1, step_max + 1 ):

    if ( abs ( xa - xb ) < xatol ):
      print ( '' )
      print ( '  Interval small enough for convergence.' )
      return xa, xb, fxa, fxb

    if ( abs ( fxa ) <= fatol or abs ( fxb ) <= fatol ):
      print ( '' )
      print ( '  Function small enough for convergence.' )
      return xa, xb, fxa, fxb

    xc = ( fxa * xb - fxb * xa ) / ( fxa - fxb )
    fxc = p00_fx ( prob, xc )

    if ( fxc < 0.0 ):
      xa = xc
      fxa = fxc
    else:
      xb = xc
      fxb = fxc

    print ( '  %4d  %14g  %14g  %14g  %14g' % ( step_num, xa, xb, fxa, fxb ) )

  print ( '' )
  print ( '  Took maximum number of steps without convergence.' )

  return xa, xb, fxa, fxb

def regula_falsi_test ( ):

#*****************************************************************************80
#
## regula_falsi_test tests the regula falsi method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'regula_falsi_test' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    start_num = p00_start_num ( prob )

    if ( start_num < 2 ):
      print ( '  Do not have two starting values for this problem.' )
      continue

    xa = p00_start ( prob, 1 )
    xb = p00_start ( prob, 2 )
    fxa = p00_fx ( prob, xa )
    fxb = p00_fx ( prob, xb )

    if ( ( fxa < 0.0 and fxb < 0.0 ) or ( 0.0 < fxa and 0.0 < fxb ) ):
      print ( '  First two starting points agree in sign.' )
      continue

    xa2, xb2, fxa2, fxb2 = regula_falsi ( fatol, step_max, prob, xatol, \
      xa, xb, fxa, fxb )

    root_num = p00_root_num ( prob )

    if ( 0 < root_num ):
      print ( '' )
    else:
      print ( '  Exact root not known' )

    for root in range ( 1, root_num + 1 ):
      x = p00_root ( prob, root )
      fx = p00_fx ( prob, x )
      print ( '  Root  %14g                  %14g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'regula_falsi_test' )
  print ( '  Normal end of execution.' )
  return

def secant ( fatol, step_max, prob, xatol, xmin, xmax, xa, xb, fxa, fxb ):

#*****************************************************************************80
#
## secant() carries out the secant method to seek a root of F(X) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real FATOL, an absolute error tolerance for the
#    function value of the root.  If an approximate root X satisfies
#      ABS ( F ( X ) ) <= FATOL, then X will be accepted as the
#    root and the iteration will be terminated.
#
#    integer STEP_MAX, the maximum number of steps allowed
#    for an iteration.
#
#    integer PROB, the index of the function whose root is
#    to be sought.
#
#    real XATOL, an absolute error tolerance for the root.
#
#    real XMAX, XMIN, the interval in which the root should
#    be sought.
#
#    real XA, XB, two points at which the 
#    function differs in sign.  
#
#    real FXA, FXB, the value of the function 
#    at XA and XB.
#
#  Output:
#
#    real XA, XB, two updated points at which the 
#    function differs in sign.  
#
#    real FXA, FXB, the value of the function 
#    at XA and XB.
#
  print ( '' )
  print ( 'SECANT' )
  print ( '' )
  print ( '  Step             X             F(X)' )
  print ( '' )

  step_num = -1
  print ( '  %4d  %14g  %14g' % ( step_num, xa, fxa ) )

  if ( abs ( fxa ) <= fatol ):
    print ( '' )
    print ( '  Function small enough for convergence.' )
    return xa, xb, fxa, fxb

  step_num = 0
  print ( '  %4d  %14g  %14g' % ( step_num, xb, fxb ) )

  for step_num in range ( 1, step_max + 1 ):

    if ( abs ( fxb ) <= fatol ):
      print ( '' )
      print ( '  Function small enough for convergence.' )
      return xa, xb, fxa, fxb

    if ( abs ( xa - xb ) < xatol ):
      print ( '' )
      print ( '  Interval small enough for convergence.' )
      return xa, xb, fxa, fxb

    if ( xb < xmin or xmax < xb ):
      print ( '' )
      print ( '  Iterate has left the region [%g,%g].' % ( xmin, xmax ) )
      return xa, xb, fxa, fxb

    if ( fxa == fxb ):
      print ( '' )
      print ( '  F(A) = F(B), algorithm fails.' )
      return xa, xb, fxa, fxb

    xc = ( fxa * xb - fxb * xa ) / ( fxa - fxb )

    fxc = p00_fx ( prob, xc )

    xa = xb
    fxa = fxb
    xb = xc
    fxb = fxc
    print ( '  %4d  %14g  %14g' % ( step_num, xb, fxb ) )

  print ( '' )
  print ( '  Took maximum number of steps.' )

  return xa, xb, fxa, fxb

def secant_test ( ):

#*****************************************************************************80
#
## secant_test tests the secant method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'secant_test' )

  fatol = 1.0E-06
  step_max = 25
  xatol = 1.0E-06

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    start_num = p00_start_num ( prob )

    if ( start_num < 2 ):
      print ( '  Do not have two starting values for this problem.' )
      continue

    rang = p00_rang ( prob )
    xmin = rang[0]
    xmax = rang[1]

    xa = p00_start ( prob, 1 )
    xb = p00_start ( prob, 2 )
    fxa = p00_fx ( prob, xa )
    fxb = p00_fx ( prob, xb )

    xa2, xb2, fxa2, fxb2 = secant ( fatol, step_max, prob, xatol, xmin, xmax, \
      xa, xb, fxa, fxb )

    root_num = p00_root_num ( prob )

    if ( 0 < root_num ):
      print ( '' )
    else:
      print ( '  Exact root not known' )

    for root in range ( 1, root_num + 1 ):
      x = p00_root ( prob, root )
      fx = p00_fx ( prob, x )
      print ( '  Root  %14g                  %14g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'secant_test' )
  print ( '  Normal end of execution.' )
  return

def test_zero_test ( ):

#*****************************************************************************80
#
## test_zero_test() tests test_zero().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'test_zero_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test test_zero().' )

  bisection_test ( )
  brent_test ( )
  muller_test ( )
  newton_test ( )
  regula_falsi_test ( )
  secant_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_zero_test' )
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
  test_zero_test ( )
  timestamp ( )

