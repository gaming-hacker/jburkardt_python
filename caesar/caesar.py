#! /usr/bin/env python3
#
def caesar_test ( ):

#*****************************************************************************80
#
## caesar_test() tests caesar().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'caesar_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test CAESAR().' )
#
#  Test 1
#
  print ( '' )
  print ( '  S2 = S_TO_CAESAR ( S1, K ), varying K.' )
  print ( '' )
  print ( '   K  ---------------S1----------------  ---------------S2----------------' )
  print ( '' )
  for k in range ( -5, 6 ):
    s1 = 'A man, a plan, a canal: Panama!'
    s2 = s_to_caesar ( s1, k )
    print ( '  %2d  "%s"  "%s"' % ( k, s1, s2 ) )
#
#  Test 2
#
  print ( '' )
  print ( '  S2 = S_TO_CAESAR ( S1,  K ).' )
  print ( '  S3 = S_TO_CAESAR ( S2, -K )' )
  print ( '' )
  print ( '   K  ------------S1------------  ------------S2------------  ------------S3------------' )
  print ( '' )
  for k in range ( -5, 6 ):
    s1 = 'The key is under the mat'
    s2 = s_to_caesar ( s1, k )
    s3 = s_to_caesar ( s2, -k )
    print ( '  %2d  "%s"  "%s"  "%s"' % ( k, s1, s2, s3 ) )
#
#  Test 3
#
  print ( '' )
  print ( '  S2 = S_TO_CAESAR ( S1, K ), varying K.' )
  print ( '' )
  print ( '   K  ---------------S2---------------------------------------------------' )
  print ( '' )
  for k in range ( 0, 27 ):
    s1 = 'The only thing we have to fear is fear itself.'
    s2 = s_to_caesar ( s1, k )
    print ( '  %2d  "%s"' % ( k, s2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'caesar_test():' )
  print ( '  Normal end of execution.' )
  return

def s_to_caesar ( s1, k ):

#*****************************************************************************80
#
## s_to_caesar() applies a Caesar shift cipher to a string.
#
#  Discussion:
#
#    The Caesar shift cipher incremented each letter by 1, with Z going to A.
#
#    This function can apply a Caesar shift cipher to a string of characters,
#    using an arbitrary shift K, which can be positive, negative or zero.
#
#    Letters A through Z will be shifted by K, mod 26.
#    Letters a through z will be shifted by K, mod 26.
#    Non-alphabetic characters are unchanged.
#
#    s2 = s_to_caesar ( s1, 1 ) will apply the traditional Caesar cipher.
#    s3 = s_to_caesar ( s2, -1 ) will decipher the result.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S1, a string of characters.
#
#    integer K, the increment.
#
#  Output:
#
#    string S2, the string of enciphered characters.
#
  iacap = ord ( 'A' )
  ialow = ord ( 'a' )

  s1_length = len ( s1 )
  s2 = ''

  for i in range ( 0, s1_length ):

    i1 = ord ( s1[i] )

    if ( iacap <= i1 and i1 <= iacap + 25 ):
      i2 = ( ( i1 + k - iacap ) % 26 ) + iacap
      s2 = s2 + chr ( i2 )
    elif ( ialow <= i1 and i1 <= ialow + 25 ):
      i2 = ( ( i1 + k - ialow ) % 26 ) + ialow
      s2 = s2 + chr ( i2 )
    else:
      s2 = s2 + s1[i]
  
  return s2

def s_to_caesar_test ( ):

#*****************************************************************************80
#
## s_to_caesar_test() tests s_to_caesar().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 's_to_caesar_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  s_to_caesar() applies a Caesar shift cipher to a string.' )

  print ( '' )
  print ( '  S2 = S_TO_CAESAR ( S1, K ), varying K.' )
  print ( '' )
  print ( '   K  ---------------S1----------------  ---------------S2----------------' )
  print ( '' )
  for k in range ( -5, 6 ):
    s1 = 'A man, a plan, a canal: Panama!'
    s2 = s_to_caesar ( s1, k )
    print ( '  %2d  "%s"  "%s"' % ( k, s1, s2 ) )

  print ( '' )
  print ( '  S2 = S_TO_CAESAR ( S1,  K ).' )
  print ( '  S3 = S_TO_CAESAR ( S2, -K )' )
  print ( '' )
  print ( '   K  ------------S1------------  ------------S2------------  ------------S3------------' )
  print ( '' )
  for k in range ( -5, 6 ):
    s1 = 'The key is under the mat'
    s2 = s_to_caesar ( s1, k )
    s3 = s_to_caesar ( s2, -k )
    print ( '  %2d  "%s"  "%s"  "%s"' % ( k, s1, s2, s3 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 's_to_caesar_test():' )
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
  caesar_test ( )
  timestamp ( )

