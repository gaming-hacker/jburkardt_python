#! /usr/bin/env python3
#
def d1mach ( i ):

#*****************************************************************************80
#
## d1mach() returns double precision real machine constants.
#
#  Discussion:
#
#    Assume that double precision real numbers are stored with a mantissa
#    of T digits in base B, with an exponent whose value must lie
#    between EMIN and EMAX.  Then for values of I between 1 and 5,
#    d1mach will return the following values:
#
#      d1mach(1) = B^(EMIN-1), the smallest positive magnitude.
#      d1mach(2) = B^EMAX*(1-B^(-T)), the largest magnitude.
#      d1mach(3) = B^(-T), the smallest relative spacing.
#      d1mach(4) = B^(1-T), the largest relative spacing.
#      d1mach(5) = log10(B)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    Original FORTRAN77 version by Phyllis Fox, Andrew Hall, Norman Schryer
#    Python version by John Burkardt.
#
#  Reference:
#
#    Phyllis Fox, Andrew Hall, Norman Schryer,
#    Algorithm 528,
#    Framework for a Portable Library,
#    ACM Transactions on Mathematical Software,
#    Volume 4, Number 2, June 1978, page 176-188.
#
#  Input:
#
#    integer I, chooses the parameter to be returned.
#    1 <= I <= 5.
#
#  Output:
#
#    real VALUE, the value of the chosen parameter.
#
  if ( i < 1 ):
    print ( '' )
    print ( 'd1mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'd1mach - Fatal error!' )
  elif ( i == 1 ):
    value = 1.112536929253601E-308
  elif ( i == 2 ):
    value = 4.494232837155789E+307
  elif ( i == 3 ):
    value = 1.110223024625157E-016
  elif ( i == 4 ):
    value = 2.220446049250313E-016
  elif ( i == 5 ):
    value = 0.301029995663981
  elif ( 5 < i ):
    print ( '' )
    print ( 'd1mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'd1mach - Fatal error!' )

  return value

def d1mach_test ( ):

#*****************************************************************************80
#
## d1mach_test() reports the constants returned by d1mach.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'd1mach_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  d1mach reports the value of constants associated' )
  print ( '  with real double precision computer arithmetic.' )

  print ( '' )
  print ( '  Assume that double precision numbers are stored ' )
  print ( '  with a mantissa of T digits in base B, with an' )
  print ( '  exponent whose value must lie between EMIN and EMAX.' )

  print ( '' )
  print ( '  For input arguments of 1 <= I <= 5,' )
  print ( '  d1mach will return the following values:' )

  print ( '' )
  print ( '  d1mach(1) = B^(EMIN-1), the smallest positive magnitude.' )
  print ( '  %26.16e' % ( d1mach ( 1 ) ) )

  print ( '' )
  print ( '  d1mach(2) = B^EMAX*(1-B^(-T)), the largest magnitude.' )
  print ( '  %26.16e' % ( d1mach ( 2 ) ) )

  print ( '' )
  print ( '  d1mach(3) = B^(-T), the smallest relative spacing.' )
  print ( '  %26.16e' % ( d1mach ( 3 ) ) )

  print ( '' )
  print ( '  d1mach(4) = B^(1-T), the largest relative spacing.' )
  print ( '  %26.16e' % ( d1mach ( 4 ) ) )

  print ( '' )
  print ( '  d1mach(5) = log10(B).' )
  print ( '  %26.16e' % ( d1mach ( 5 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'd1mach_test' )
  print ( '  Normal end of execution.' )
  return

def i1mach ( i ):

#*****************************************************************************80
#
## i1mach() returns integer machine constants.
#
#  Discussion:
#
#    Input/output unit numbers.
#
#      i1mach(1) = the standard input unit.
#      i1mach(2) = the standard output unit.
#      i1mach(3) = the standard punch unit.
#      i1mach(4) = the standard error message unit.
#
#    Words.
#
#      i1mach(5) = the number of bits per integer storage unit.
#      i1mach(6) = the number of characters per integer storage unit.
#
#    Integers.
#
#    Assume integers are represented in the S digit base A form:
#
#      Sign * (X(S-1)*A^(S-1) + ... + X(1)*A + X(0))
#
#    where 0 <= X(1:S-1) < A.
#
#      i1mach(7) = A, the base.
#      i1mach(8) = S, the number of base A digits.
#      i1mach(9) = A^S-1, the largest integer.
#
#    Floating point numbers
#
#    Assume floating point numbers are represented in the T digit
#    base B form:
#
#      Sign * (B^E) * ((X(1)/B) + ... + (X(T)/B^T) )
#
#    where 0 <= X(I) < B for I=1 to T, 0 < X(1) and EMIN <= E <= EMAX.
#
#      i1mach(10) = B, the base.
#
#    Single precision
#
#      i1mach(11) = T, the number of base B digits.
#      i1mach(12) = EMIN, the smallest exponent E.
#      i1mach(13) = EMAX, the largest exponent E.
#
#    Double precision
#
#      i1mach(14) = T, the number of base B digits.
#      i1mach(15) = EMIN, the smallest exponent E.
#      i1mach(16) = EMAX, the largest exponent E.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    Original FORTRAN77 version by Phyllis Fox, Andrew Hall, Norman Schryer
#    Python version by John Burkardt.
#
#  Reference:
#
#    Phyllis Fox, Andrew Hall, Norman Schryer,
#    Algorithm 528,
#    Framework for a Portable Library,
#    ACM Transactions on Mathematical Software,
#    Volume 4, Number 2, June 1978, page 176-188.
#
#  Input:
#
#    integer I, chooses the parameter to be returned.
#    1 <= I <= 16.
#
#  Output:
#
#    integer VALUE, the value of the chosen parameter.
#
  if ( i < 1 ):
    print ( '' )
    print ( 'i1mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 16.' )
    print ( '  I =   %d' % ( i ) )
    raise Exception ( 'i1mach - Fatal error!' )
  elif ( i == 1 ):
    value = 5
  elif ( i == 2 ):
    value = 6
  elif ( i == 3 ):
    value = 7
  elif ( i == 4 ):
    value = 6
  elif ( i == 5 ):
    value = 32
  elif ( i == 6 ):
    value = 4
  elif ( i == 7 ):
    value = 2
  elif ( i == 8 ):
    value = 31
  elif ( i == 9 ):
    value = 2147483647
  elif ( i == 10 ):
    value = 2
  elif ( i == 11 ):
    value = 24
  elif ( i == 12 ):
    value = -125
  elif ( i == 13 ):
    value = 128
  elif ( i == 14 ):
    value = 53
  elif ( i == 15 ):
    value = -1021
  elif ( i == 16 ):
    value = 1024
  elif ( 16 < i ):
    print ( '' )
    print ( 'i1mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 16.' )
    print ( '  I =   %d' % ( i ) )
    raise Exception ( 'i1mach - Fatal error!' )

  return value

def i1mach_test ( ):

#*****************************************************************************80
#
## i1mach_test() reports the constants returned by i1mach.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i1mach_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i1mach reports the value of constants associated' )
  print ( '  with integer computer arithmetic.' )

  print ( '' )
  print ( '  Numbers associated with input/output units:' )

  print ( '' )
  print ( '  i1mach(1) = the standard input unit.' )
  print ( '  %d' % ( i1mach ( 1 ) ) )

  print ( '' )
  print ( '  i1mach(2) = the standard output unit.' )
  print ( '  %d' % ( i1mach ( 2 ) ) )

  print ( '' )
  print ( '  i1mach(3) = the standard punch unit.' )
  print ( '  %d' % ( i1mach ( 3 ) ) )

  print ( '' )
  print ( '  i1mach(4) = the standard error message unit.' )
  print ( '  %d' % ( i1mach ( 4 ) ) )

  print ( '' )
  print ( '  Numbers associated with words:' )

  print ( '' )
  print ( '  i1mach(5) = the number of bits per integer.' )
  print ( '  %d' % ( i1mach ( 5 ) ) )

  print ( '' )
  print ( '  i1mach(6) = the number of characters per integer.' )
  print ( '  %d' % ( i1mach ( 6 ) ) )

  print ( '' )
  print ( '  Numbers associated with integer values:' )

  print ( '' )
  print ( '  Assume integers are represented in the S digit' )
  print ( '  base A form:' )
  print ( '' )
  print ( '    Sign * (X(S-1)*A^(S-1) + ... + X(1)*A + X(0))' )
  print ( '' )
  print ( '  where the digits X satisfy 0 <= X(1:S-1) < A.' )

  print ( '' )
  print ( '  i1mach(7) = A, the base.' )
  print ( '  %d' % ( i1mach ( 7 ) ) )

  print ( '' )
  print ( '  i1mach(8) = S, the number of base A digits.' )
  print ( '  %d' % ( i1mach ( 8 ) ) )

  print ( '' )
  print ( '  i1mach(9) = A^S-1, the largest integer.' )
  print ( '  %d' % ( i1mach ( 9 ) ) )

  print ( '' )
  print ( '  Numbers associated with floating point values:' )
  print ( '' )
  print ( '  Assume floating point numbers are represented ' )
  print ( '  in the T digit base B form:' )
  print ( '' )
  print ( '    Sign * (B^E) * ((X(1)/B) + ... + (X(T)/B^T) )' )
  print ( '' )
  print ( '  where' )
  print ( '' )
  print ( '    0 <= X(1:T) < B,' )
  print ( '    0 < X(1) (unless the value being represented is 0),' )
  print ( '    EMIN <= E <= EMAX.' )

  print ( '' )
  print ( '  i1mach(10) = B, the base.' )
  print ( '  %d' % ( i1mach ( 10 ) ) )

  print ( '' )
  print ( '  Numbers associated with single precision values:' )
  print ( '' )
  print ( '  i1mach(11) = T, the number of base B digits.' )
  print ( '  %d' % ( i1mach ( 11 ) ) )

  print ( '' )
  print ( '  i1mach(12) = EMIN, the smallest exponent E.' )
  print ( '  %d' % ( i1mach ( 12 ) ) )

  print ( '' )
  print ( '  i1mach(13) = EMAX, the largest exponent E.' )
  print ( '  %d' % ( i1mach ( 13 ) ) )

  print ( '' )
  print ( '  Numbers associated with double precision values:' )
  print ( '' )
  print ( '  i1mach(14) = T, the number of base B digits.' )
  print ( '  %d' % ( i1mach ( 14 ) ) )

  print ( '' )
  print ( '  i1mach(15) = EMIN, the smallest exponent E.' )
  print ( '  %d' % ( i1mach ( 15 ) ) )

  print ( '' )
  print ( '  i1mach(16) = EMAX, the largest exponent E.' )
  print ( '  %d' % ( i1mach ( 16 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i1mach_test' )
  print ( '  Normal end of execution.' )
  return

def machine_test ( ):

#*****************************************************************************80
#
## machine_test() tests machine().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'machine_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test machine()' )

  d1mach_test ( )
  i1mach_test ( )
  r1mach_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'MACHINE_test:' )
  print ( '  Normal end of execution.' )
  return

def r1mach ( i ):

#*****************************************************************************80
#
## r1mach() returns single precision real machine constants.
#
#  Discussion:
#
#    Assume that single precision real numbers are stored with a mantissa
#    of T digits in base B, with an exponent whose value must lie
#    between EMIN and EMAX.  Then for values of I between 1 and 5,
#    r1mach will return the following values:
#
#      r1mach(1) = B^(EMIN-1), the smallest positive magnitude.
#      r1mach(2) = B^EMAX*(1-B^(-T)), the largest magnitude.
#      r1mach(3) = B^(-T), the smallest relative spacing.
#      r1mach(4) = B^(1-T), the largest relative spacing.
#      r1mach(5) = log10(B)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    Original FORTRAN77 version by Phyllis Fox, Andrew Hall, Norman Schryer
#    Python version by John Burkardt.
#
#  Reference:
#
#    Phyllis Fox, Andrew Hall, Norman Schryer,
#    Algorithm 528,
#    Framework for a Portable Library,
#    ACM Transactions on Mathematical Software,
#    Volume 4, Number 2, June 1978, page 176-188.
#
#  Input:
#
#    integer I, chooses the parameter to be returned.
#    1 <= I <= 5.
#
#  Output:
#
#    real VALUE, the value of the chosen parameter.
#
  if ( i < 1 ):
    print ( '' )
    print ( 'r1mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'r1mach - Fatal error!' )
  elif ( i == 1 ):
    value = 1.1754944E-38
  elif ( i == 2 ):
    value = 3.4028235E+38
  elif ( i == 3 ):
    value = 5.9604645E-08
  elif ( i == 4 ):
    value = 1.1920929E-07
  elif ( i == 5 ):
    value = 0.3010300
  elif ( 5 < i ):
    print ( '' )
    print ( 'r1mach - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'r1mach - Fatal error!' )

  return value

def r1mach_test ( ):

#*****************************************************************************80
#
## r1mach_test() reports the constants returned by r1mach.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r1mach_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r1mach reports the value of constants associated' )
  print ( '  with real single precision computer arithmetic.' )

  print ( '' )
  print ( '  Assume that single precision numbers are stored ' )
  print ( '  with a mantissa of T digits in base B, with an ' )
  print ( '  exponent whose value must lie between EMIN and EMAX.' )

  print ( '' )
  print ( '  For input arguments of 1 <= I <= 5,' )
  print ( '  r1mach will return the following values:' )

  print ( '' )
  print ( '  r1mach(1) = B^(EMIN-1), the smallest positive magnitude.' )
  print ( '  %26.16e' % ( r1mach ( 1 ) ) )

  print ( '' )
  print ( '  r1mach(2) = B^EMAX*(1-B^(-T)), the largest magnitude.' )
  print ( '  %26.16e' % ( r1mach ( 2 ) ) )

  print ( '' )
  print ( '  r1mach(3) = B^(-T), the smallest relative spacing.' )
  print ( '  %26.16e' % ( r1mach ( 3 ) ) )

  print ( '' )
  print ( '  r1mach(4) = B^(1-T), the largest relative spacing.' )
  print ( '  %26.16e' % ( r1mach ( 4 ) ) )

  print ( '' )
  print ( '  r1mach(5) = log10(B).' )
  print ( '  %26.16e' % ( r1mach ( 5 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r1mach_test' )
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
  machine_test ( )
  timestamp ( )

