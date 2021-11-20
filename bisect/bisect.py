#! /usr/bin/env python3
#
class bisect ( ):

  def __init__ ( self, a, b, f ):

    self.a = a
    self.fa = f ( a )
    self.b = b
    self.fb = f ( b )
    self.f = f

  def x ( self ):
    value = ( self.a + self.b ) / 2.0
    return value

  def bisect ( self ):
    c = ( self.a + self.b ) / 2.0
    fc = self.f ( c )
    if ( fc <= 0.0 and self.fa <= 0.0 ):
      self.a = c
      self.fa = fc
    else:
      self.b = c
      self.fb = fc
    return

def bisect_test ( ):

#*****************************************************************************80
#
## bisect_test() tests bisect().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'bisect_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bisect() seeks a root of a nonlinear equation using bisection.' )

  a = 2.0
  b = 3.0
  f = lambda x : x ** 3 - 2.0 * x - 5
  wallis = bisect ( a, b, f )

  print ('  Wallis.x = %g' % ( wallis.x ( ) ) )

  for test in range ( 0, 20 ):
    wallis.bisect ( )
    print ( '  Wallis.a = %g, Wallis.b = %g' % ( wallis.a, wallis.b ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'bisect_test():' )
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
  bisect_test ( )
  timestamp ( )

