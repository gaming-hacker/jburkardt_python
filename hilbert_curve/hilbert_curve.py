#! /usr/bin/env python3
#
def d2xy ( m, d ):

#*****************************************************************************80
#
## d2xy() converts a 1D Hilbert coordinate to a 2D Cartesian coordinate.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2016
#
#  Input:
#
#    integer M, the index of the Hilbert curve.
#    The number of cells is N=2^M.
#    0 < M.
#
#    integer D, the Hilbert coordinate of the cell.
#    0 <= D < N * N.
#
#  Output:
#
#    integer X, Y, the Cartesian coordinates of the cell.
#    0 <= X, Y < N.
#
  n = 2 ** m

  x = 0
  y = 0
  t = d
  s = 1

  while ( s < n ):

    rx = ( ( t // 2 ) % 2 )
    if ( rx == 0 ):
      ry = ( t % 2 )
    else:
      ry = ( ( t ^ rx ) % 2 )
    x, y = rot ( s, x, y, rx, ry )
    x = x + s * rx
    y = y + s * ry
    t = ( t // 4 )

    s = s * 2

  return x, y

def d2xy_test ( ):

#*****************************************************************************80
#
## d2xy_test() tests d2xy().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'd2xy_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  d2xy() converts a Hilbert linear D coordinate to an (X,Y) 2D coordinate.' )

  m = 3
  n = 2 ** m

  print ( '' )
  print ( '    D    X    Y' )
  print ( '' )

  for d in range ( 0, n * n ):
    x, y = d2xy ( m, d )
    print ( '  %3d  %3d  %3d' % ( d, x, y ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'd2xy_test():' )
  print ( '  Normal end of execution.' )
  return

def hilbert_curve_test ( ):

#*****************************************************************************80
#
## hilbert_curve_test() tests hilbert_curve().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hilbert_curve_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test hilbert_curve().' )

  d2xy_test ( )
  rot_test ( )
  xy2d_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hilbert_curve_test():' )
  print ( '  Normal end of execution.' )
  return

def rot ( n, x, y, rx, ry ):

#*****************************************************************************80
#
## rot() rotates and flips a quadrant appropriately.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2016
#
#  Input:
#
#    integer N, the length of a side of the square.  
#    N must be a power of 2.
#
#    integer X, Y, the coordinates of a point.
#
#    integer RX, RY, ???
#
#  Output:
#
#    integer X, Y, the transformed point coordinates.
#
  if ( ry == 0 ):
#
#  Reflect.
#
    if ( rx == 1 ):
      x = n - 1 - x
      y = n - 1 - y
#
#  Flip.
#
    t = x
    x = y
    y = t

  return x, y

def rot_test ( ):

#*****************************************************************************80
#
## rot_test() tests rot().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rot_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rot() rotates and flips a quadrant appropriately.' )
  print ( '' )
  print ( '   X   Y  X0  Y0  X1  Y1' )
  print ( '' )

  m = 3
  n = 2 ** m
  ry = 0

  for y in range ( 0, n ):
    for x in range ( 0, n ):
      rx = 0
      x0 = x
      y0 = y
      x0, y0 = rot ( n, x0, y0, rx, ry )
      rx = 1
      x1 = x
      y1 = y
      x1, y1 = rot ( n, x1, y1, rx, ry )
      print ( '  %2d  %2d  %2d  %2d  %2d  %2d' % ( x, y, x0, y0, x1, y1 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'rot_test():' )
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

def xy2d ( m, x, y ):

#*****************************************************************************80
#
## xy2d() converts a 2D Cartesian coordinate to a 1D Hilbert coordinate.
#
#  Discussion:
#
#    It is assumed that a square has been divided into an NxN array of cells,
#    where N is a power of 2.
#
#    Cell (0,0) is in the lower left corner, and (N-1,N-1) in the upper 
#    right corner.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2016
#
#  Input:
#
#    integer M, the index of the Hilbert curve.
#    The number of cells is N=2^M.
#    0 < M.
#
#    integer X, Y, the Cartesian coordinates of a cell.
#    0 <= X, Y < N.
#
#  Output:
#
#    integer D, the Hilbert coordinate of the cell.
#    0 <= D < N * N.
#
  xcopy = x
  ycopy = y

  d = 0
  n = 2 ** m

  s = ( n // 2 )

  while ( 0 < s ):

    if ( 0 <  ( abs ( xcopy ) & s ) ):
      rx = 1
    else:
      rx = 0

    if ( 0 < ( abs ( ycopy ) & s ) ):
      ry = 1
    else:
      ry = 0

    d = d + s * s * ( ( 3 * rx ) ^ ry )
    
    xcopy, ycopy = rot ( s, xcopy, ycopy, rx, ry )

    s = ( s // 2 )

  return d

def xy2d_test ( ):

#*****************************************************************************80
#
## xy2d_test() tests xy2d().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'xy2d_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  xy2d() converts an (X,Y) 2D coordinate to a Hilbert linear D coordinate.' )

  m = 3
  n = 2 ** m

  print ( '' )
  print ( '        ', end = '' )
  for x in range ( 0, n ):
    print ( '%3d' % ( x ), end = '' )
  print ( '' )

  print ( '' )
  for y in range ( n - 1, -1, -1 ):
    print ( '  %3d:  ' % ( y ), end = '' )
    for x in range ( 0, n ):
      d = xy2d ( m, x, y )
      print ( '%3d' % ( d ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'xy2d_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  hilbert_curve_test ( )
  timestamp ( )

