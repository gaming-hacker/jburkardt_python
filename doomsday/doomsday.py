#! /usr/bin/env python3
#
def doomsday_gregorian ( y, m, d ):

#*****************************************************************************80
#
## doomsday_gregorian(): weekday given any date in Gregorian calendar.
#
#  Discussion:
#
#    This procedure does not include any procedure to switch to the Julian
#    calendar for dates early enough that that calendar was used instead.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Conway,
#    Tomorrow is the Day After Doomsday,
#    Eureka,
#    Volume 36, October 1973, pages 28-31.
#
#  Input:
#
#    integer Y, M, D, the year, month and day of the date.
#    Note that the year must be positive.
#
#  Output:
#
#    integer W, the weekday of the date.
#
  import numpy as np

  anchor = np.array ( [ 1, 6, 4, 3 ] )
  mdoom = np.array ( [ 3, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12 ] )
#
#  Refuse to handle Y <= 0.
#
  if ( y <= 0 ):
    print ( '' )
    print ( 'doomsday_gregorian - Fatal error!' )
    print ( '  Y <= 0.' )
    raise Exception ( 'doomsday_gregorian - Fatal error!' )
#
#  Force Y to be an integer value.
#
  y = int ( y )
#
#  Determine the century C.
#
  c = y // 100
#
#  Determine the last two digits of the year, YY
#
  yy = ( y % 100 )
#
#  Divide the last two digits of the year by 12.
#
  yy = ( y % 100 )
  yy12d = ( yy // 12 )
  yy12r = ( yy % 12 ) 
  yy12r4d = ( yy12r // 4 )
  drd = yy12d + yy12r + yy12r4d
  drdr = ( drd % 7 )
  t = ( ( c - 1 ) % 4 )
  ydoom = anchor[t] + drdr
  ydoom = i4_wrap ( ydoom, 1, 7 )
#
#  If M = 1 or 2, and leap year, add 1.
#
  if ( ( m == 1 or m == 2 ) and year_is_leap_gregorian ( y ) ):
    l = 1
  else:
    l = 0

  w = ydoom + ( d -  mdoom[m-1] - l )
  w = i4_wrap ( w, 1, 7 )

  return w

def doomsday_gregorian_test01 ( ):

#*****************************************************************************80
#
## doomsday_gregorian_test01() tests doomsday_gregorian() against a couple of test dates.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( ' ' )
  print ( 'doomsday_gregorian_test01' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Try a couple selected dates.' )
  print ( ' ' )
  print ( '  YYYY  MM  DD  Weekday    Weekday' )
  print ( '                Tabulated  Computed' )
  print ( ' ' )

  y = 1989
  m = 7
  d = 13
  w = doomsday_gregorian ( y, m, d )
  s1 = weekday_to_name_common ( w )
  s2 = 'Thursday'
  print ( '  %4d  %2d  %2d  %10s  %10s' % ( y, m, d, s1, s2 ) )

  y = 2012
  m = 5
  d = 26
  w = doomsday_gregorian ( y, m, d )
  s1 = weekday_to_name_common ( w )
  s2 = 'Saturday'
  print ( '  %4d  %2d  %2d  %10s  %10s' % ( y, m, d, s1, s2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'doomsday_gregorian_test01' )
  print ( '  Normal end of execution.' )

  return

def doomsday_gregorian_test02 ( ):

#*****************************************************************************80
#
## doomsday_gregorian_test02() tests doomsday_gregorian() against a number of known values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2012
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( ' ' )
  print ( 'doomsday_gregorian_test02' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  weekday_values supplies a list of dates and weekdays.' )
  print ( ' ' )
  print ( '  YYYY  MM  DD  Weekday    Weekday' )
  print ( '                Tabulated  Computed' )
  print ( ' ' )

  n_data = 0

  while ( True ):

    n_data, y, m, d, w1 = weekday_values ( n_data )

    if ( n_data <= 0 ):
      break
#
#  The transition from Julian to Gregorian calendars occurred in 1582
#  (for some people).  The data in "weekday_values" before the transition
#  is stored in Julian format, which doomsday_gregorian can't handle.
#  So let's just refuse to handle 1582 or earlier#
#
    if ( y <= 1582 ):
      continue

    w2 = doomsday_gregorian ( y, m, d )

    s1 = weekday_to_name_common ( w1 )
    s2 = weekday_to_name_common ( w2 )

    print ( '  %4d  %2d  %2d  %10s  %10s' % ( y, m, d, s1, s2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'doomsday_gregorian_test02' )
  print ( '  Normal end of execution.' )
  return

def doomsday_test ( ):

#*****************************************************************************80
#
## doomsday_test() tests doomsday().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'doomsday_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test doomsday().' )

  doomsday_gregorian_test01 ( )
  doomsday_gregorian_test02 ( )
  i4_modp_test ( )
  i4_wrap_test ( )
  weekday_to_name_common_test ( )
  weekday_values_test ( )
  year_is_leap_gregorian_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'doomsday_test' )
  print ( '  Normal end of execution.' )
  return

def i4_modp ( i, j ):

#*****************************************************************************80
#
## i4_modp() returns the nonnegative remainder of I4 division.
#
#  Discussion:
#
#    If
#      NREM = i4_modp ( I, J )
#      NMULT = ( I - NREM ) / J
#    then
#      I = J * NMULT + NREM
#    where NREM is always nonnegative.
#
#    The MOD function computes a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, i4_modp(A,360) is between 0 and 360, always.
#
#  Example:
#
#        I     J     MOD  i4_modp    Factorization
#
#      107    50       7       7    107 =  2 *  50 + 7
#      107   -50       7       7    107 = -2 * -50 + 7
#     -107    50      -7      43   -107 = -3 *  50 + 43
#     -107   -50      -7      43   -107 =  3 * -50 + 43
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number to be divided.
#
#    integer J, the number that divides I.
#
#  Output:
#
#    integer VALUE, the nonnegative remainder when I is
#    divided by J.
#
  if ( j == 0 ):
    print ( '' )
    print ( 'i4_modp - Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    raise Exception ( 'i4_modp - Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + abs ( j )

  return value

def i4_modp_test ( ):

#*****************************************************************************80
#
## i4_modp_test() tests i4_modp().
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

  test_num = 4

  n_vec = np.array ( ( 107, 107, -107, -107 ) )
  d_vec = np.array ( ( 50, -50, 50, -50 ) )

  print ( '' )
  print ( 'i4_modp_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_modp factors a number' )
  print ( '  into a multiple M and a positive remainder R.' )
  print ( '' )
  print ( '    Number   Divisor  Multiple Remainder' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    r = i4_modp ( n, d )
    m = ( n - r ) // d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  print ( '' )
  print ( '  Repeat using Python % Operator:' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_modp_test' )
  print ( '  Normal end of execution.' )
  return

def i4_wrap ( ival, ilo, ihi ):

#*****************************************************************************80
#
## i4_wrap() forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    ILO = 4, IHI = 8
#
#    I   Value
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer IVAL, an integer value.
#
#    integer ILO, IHI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of IVAL.
#
  jlo = min ( ilo, ihi )
  jhi = max ( ilo, ihi )

  wide = jhi - jlo + 1

  if ( wide == 1 ):
    value = jlo
  else:
    value = jlo + i4_modp ( ival - jlo, wide )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## i4_wrap_test() tests i4_wrap().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'i4_wrap_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_wrap forces an integer to lie within given limits.' )
  print ( '' )
  print ( '  ILO = %d' % ( ilo ) )
  print ( '  IHI = %d' % ( ihi ) )
  print ( '' )
  print ( '     I  i4_wrap(I)' )
  print ( '' )

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print ( '  %6d  %6d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_wrap_test' )
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

def weekday_to_name_common ( w ):

#*****************************************************************************80
#
## weekday_to_name_common returns the name of a Common weekday.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer W, the weekday index.
#    1 <= W <= 7.
#
#  Output:
#
#    string S, the weekday name.
#
  name = [ 
    'Sunday',
    'Monday', 
    'Tuesday', 
    'Wednesday',
    'Thursday', 
    'Friday', 
    'Saturday' ]
#
#  Return the weekday name.
#
  s = name[w-1]

  return s

def weekday_to_name_common_test ( ):

#*****************************************************************************80
#
## weekday_to_name_common_test() tests weekday_to_name_common().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'weekday_to_name_common_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  weekday_to_name_common returns the name of a day of the week' )
  print ( '  in the common calendar.' )
  print ( '' )
  print ( '  Index  Name' )
  print ( '' )

  for i in range ( 1, 8 ):
    name = weekday_to_name_common ( i )
    print ( '  %5d  %s' % ( i, name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'weekday_to_name_common_test' )
  print ( '  Normal end of execution.' )
  return

def weekday_values ( n_data ):

#*****************************************************************************80
#
## weekday_values() returns the day of the week for various dates.
#
#  Discussion:
#
#    The CE or Common Era calendar is used, under the
#    hybrid Julian/Gregorian Calendar, with a transition from Julian
#    to Gregorian.  The day after 04 October 1582 was 15 October 1582.  
#
#    The year before 1 AD or CE is 1 BC or BCE.  In this data set,
#    years BC/BCE are indicated by a negative year value.  
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Reingold, Nachum Dershowitz,
#    Calendrical Calculations: The Millennium Edition,
#    Cambridge University Press, 2001,
#    ISBN: 0 521 77752 6
#    LC: CE12.R45.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer Y, M, D, the Common Era date.
#
#    integer W, the day of the week.  Sunday = 1.
#
  import numpy as np

  n_max = 34

  d_vec = np.array ( ( \
    30, \
     8, \
    26, \
     3, \
     7, \
    18, \
     7, \
    19, \
    14, \
    18, \
    16, \
     3, \
    26, \
    20, \
     4, \
    25, \
    31, \
     9, \
    24, \
    10, \
    30, \
    24, \
    19, \
     2, \
    27, \
    19, \
    25, \
    29, \
    19, \
     7, \
    17, \
    25, \
    10, \
    18 ))

  m_vec = np.array ( ( \
     7, \
    12, \
     9, \
    10, \
     1, \
     5, \
    11, \
     4, \
    10, \
     5, \
     3, \
     3, \
     3, \
     4, \
     6, \
     1, \
     3, \
     9, \
     2, \
     6, \
     6, \
     7, \
     6, \
     8, \
     3, \
     4, \
     8, \
     9, \
     4, \
    10, \
     3, \
     2, \
    11, \
     7 ))

  w_vec = np.array ( ( \
    1, \
    4, \
    4, \
    1, \
    4, \
    2, \
    7, \
    1, \
    7, \
    1, \
    6, \
    7, \
    6, \
    1, \
    1, \
    4, \
    7, \
    7, \
    7, \
    4, \
    1, \
    6, \
    1, \
    2, \
    4, \
    1, \
    1, \
    2, \
    2, \
    5, \
    3, \
    1, \
    4, \
    1 ))

  y_vec = np.array ( ( \
    - 587, \
    - 169, \
       70, \
      135, \
      470, \
      576, \
      694, \
     1013, \
     1066, \
     1096, \
     1190, \
     1240, \
     1288, \
     1298, \
     1391, \
     1436, \
     1492, \
     1553, \
     1560, \
     1648, \
     1680, \
     1716, \
     1768, \
     1819, \
     1839, \
     1903, \
     1929, \
     1941, \
     1943, \
     1943, \
     1992, \
     1996, \
     2038, \
     2094 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    y = 0
    m = 0
    d = 0
    w = 0
  else:
    y = y_vec[n_data]
    m = m_vec[n_data]
    d = d_vec[n_data]
    w = w_vec[n_data]
    n_data = n_data + 1

  return n_data, y, m, d, w

def weekday_values_test ( ):

#*****************************************************************************80
#
## weekday_values_test() tests weekday_values().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'weekday_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  weekday_values stores values of' )
  print ( '  the weekday for a given Y/M/D date' )
  print ( '' )
  print ( '         Y       M       D           W' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, y, m, d, w = weekday_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %6d  %6d  %6d' % ( y, m, d, w ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'weekday_values_test:' )
  print ( '  Normal end of execution.' )
  return

def year_is_leap_gregorian ( y ):

#*****************************************************************************80
#
## year_is_leap_gregorian() returns TRUE if the Gregorian year was a leap year.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer Y, the year to be checked.
#
#  Output:
#
#    bool year_is_leap_gregorian, TRUE if the year was a leap year,
#    FALSE otherwise.
#
  if ( y <= 0 ):
    print ( '' )
    print ( 'year_is_leap_gregorian - Fatal error!' )
    print ( '  This function will not accept nonpositive years.' )
    raise Exception ( 'year_is_leap_gregorian - Fatal error!' )

  if ( ( y % 400 ) == 0 ):
    value = True
  elif ( ( y % 100 ) == 0 ):
    value = False
  elif ( ( y % 4 ) == 0 ):
    value = True
  else:
    value = False

  return value

def year_is_leap_gregorian_test ( ):

#*****************************************************************************80
#
## year_is_leap_gregorian_test() tests year_is_leap_gregorian().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'year_is_leap_gregorian_test' )
  print ( '  year_is_leap_gregorian reports leap years in the Gregorian calendar.' )
  print ( '' )
  print ( '  Year  Leap?' )
  print ( '' )

  for i in range ( 0, 20 ):
    y = np.random.random_integers ( 1, 2100 )
    is_leap = year_is_leap_gregorian ( y )
    print ( '  %4d  %s' % ( y, is_leap ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'year_is_leap_gregorian_test' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  doomsday_test ( )
  timestamp ( )

