#! /usr/bin/env python3
#
def ball_grid_count ( n, r, c ):

#*****************************************************************************80
#
## ball_grid_count() counts grid points inside a ball.
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the ball,
#    and the number of subintervals N into which the horizontal radius
#    should be divided.  Thus, a value of N = 2 will result in 5 points
#    along that horizontal line.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of subintervals.
#
#    real R, the radius of the ball.
#
#    real C(3), the coordinates of the center of the ball.
#
#  Output:
#
#    integer NG, the number of grid points inside the ball.
#
  ng = 0

  for i in range ( 0, n + 1 ):

    x = c[0] + r * float ( 2 * i ) / float (  2 * n + 1 )
    
    for j in range ( 0, n + 1 ):

      y = c[1] + r * float ( 2 * j ) / float (  2 * n + 1 )
      
      for k in range ( 0, n + 1 ):

        z = c[2] + r * float ( 2 * k ) / float (  2 * n + 1 )

        if ( r * r < ( x - c[0] ) ** 2 \
                   + ( y - c[1] ) ** 2 \
                   + ( z - c[2] ) ** 2 ):
          break

        ng = ng + 1

        if ( 0 < i ):
          ng = ng + 1

        if ( 0 < j ):
          ng = ng + 1

        if ( 0 < k ):
          ng = ng + 1

        if ( 0 < i and 0 < j ):
          ng = ng + 1

        if ( 0 < i and 0 < k ):
          ng = ng + 1

        if ( 0 < j and 0 < k ):
          ng = ng + 1

        if ( 0 < i and 0 < j and 0 < k ):
          ng = ng + 1

  return ng

def ball_grid_count_test ( ):

#*****************************************************************************80
#
## ball_grid_count_test() tests ball_grid_count().
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the ball,
#    and the number of subintervals N into which the radius
#    should be divided.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ball_grid_count_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ball_grid_count() counts the number of grid points needed' )
  print ( '  for a grid of points inside a ball of radius R and center C.' )

  print ( '' )
  print ( '  N = number of subintervals of the horizontal radius.' )
  print ( '  NG = resulting number of grid points.' )
  print ( '' )
  print ( '     N        NG' )
  print ( '' )

  for n in [ 1, 2, 4, 8, 16  ]:
    r = 1.0
    c = np.array ( [ 0.0, 0.0, 0.0 ] )
    ng = ball_grid_count ( n, r, c )
    print ( '  %4d  %8d' % ( n, ng ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ball_grid_count_test():' )
  print ( '  Normal end of execution.' )
  return
  
def ball_grid_display ( r, c, ng, xg, filename ):

#*****************************************************************************80
#
## ball_grid_display() displays grid points inside a ball.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the radius of the disk.
#
#    real C(3), the coordinates of the center of the disk.
#
#    integer NG, the number of grid points inside the ball.
#
#    real XG(NG,3), the grid points.
#
#    real R, the radius of the disk.
#
#    string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.scatter ( xg[:,0], xg[:,1], xg[:,2], 'b' );

  ax.set_xlabel ( '<---X--->' )
  ax.set_ylabel ( '<---Y--->' )
  ax.set_zlabel ( '<---Z--->' )
  ax.set_title ( 'Grid points in ball' )
  ax.grid ( True )
# ax.axis ( 'equal' )
  plt.savefig ( filename )
  plt.show ( block = False )

  plt.close ( )

  return

def ball_grid_display_test ( ):

#*****************************************************************************80
#
## ball_grid_display_test() tests ball_grid_display().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ball_grid_display_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ball_grid_display() displays a grid of points in a ball.' )

  r = 2.0
  c = np.array ( [ 0.0, 0.0, 0.0 ] )
  ng = 25
  xg = np.array ( [ \
    [  0.0,  0.0,  0.0 ], \
    [  1.0,  0.0,  0.0 ], \
    [ -1.0,  0.0,  0.0 ], \
    [  0.0,  1.0,  0.0 ], \
    [  0.0, -1.0,  0.0 ], \
    [  0.0,  0.0,  1.0 ], \
    [  0.0,  0.0, -1.0 ], \
    [  1.0,  1.0,  0.0 ], \
    [  1.0, -1.0,  0.0 ], \
    [  1.0,  0.0,  1.0 ], \
    [  1.0,  0.0, -1.0 ], \
    [ -1.0,  1.0,  0.0 ], \
    [ -1.0, -1.0,  0.0 ], \
    [ -1.0,  0.0,  1.0 ], \
    [ -1.0,  0.0, -1.0 ], \
    [  0.0,  1.0,  1.0 ], \
    [  0.0,  1.0, -1.0 ], \
    [  0.0, -1.0,  1.0 ], \
    [  0.0, -1.0, -1.0 ], \
    [  2.0,  0.0,  0.0 ], \
    [ -2.0,  0.0,  0.0 ], \
    [  0.0,  2.0,  0.0 ], \
    [  0.0, -2.0,  0.0 ], \
    [  0.0,  0.0,  2.0 ], \
    [  0.0,  0.0, -2.0 ] ] )

  filename = 'ball_grid_display.png'

  ball_grid_display ( r, c, ng, xg, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'ball_grid_display_test():' )
  print ( '  Normal end of execution.' )
  return
  
def ball_grid_points ( n, r, c, ng ):

#*****************************************************************************80
#
## ball_grid_points() computes grid points inside a ball.
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the ball,
#    and the number of subintervals N into which the horizontal radius
#    should be divided.  Thus, a value of N = 2 will result in 5 points
#    along that horizontal line.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of subintervals.
#
#    real R, the radius of the ball.
#
#    real C(3), the coordinates of the center of the ball.
#
#    integer NG, the number of grid points, as determined by
#    ball_grid_count.
#
#  Output:
#
#    real BG(3,NG), the grid points inside the ball.
#
  import numpy as np

  bg = np.zeros ( ( ng, 3 ) )

  p = 0

  for i in range ( 0, n + 1 ):

    x = c[0] + r * float ( i ) / float ( n )

    for j in range ( 0, n + 1 ):

      y = c[1] + r * float ( j ) / float ( n )

      for k in range ( 0, n + 1 ):

        z = c[2] + r * float ( k ) / float ( n )

        if ( r * r < ( x - c[0] ) ** 2 \
                   + ( y - c[1] ) ** 2 \
                   + ( z - c[2] ) ** 2 ):
          break

        bg[p,0] = x
        bg[p,1] = y
        bg[p,2] = z
        p = p + 1

        if ( 0 < i ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = y
          bg[p,2] = z
          p = p + 1

        if ( 0 < j ):
          bg[p,0] = x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = z
          p = p + 1

        if ( 0 < k ):
          bg[p,0] = x
          bg[p,1] = y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

        if ( 0 < i and 0 < j ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = z
          p = p + 1

        if ( 0 < i and 0 < k ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

        if ( 0 < j and 0 < k ):
          bg[p,0] = x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

        if ( 0 < i and 0 < j and 0 < k ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

  return bg

def ball_grid_points_test ( ):

#*****************************************************************************80
#
## ball_grid_points_test() tests ball_grid_points().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ball_grid_points_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ball_grid_points() can define a grid of points' )
  print ( '  with N+1 points on a horizontal or vertical radius,' )
  print ( '  based on any ball.' )

  n = 4
  r = 2.0
  c = np.array ( [ 1.0, 5.0, 2.0 ] )

  print ( '' )
  print ( '  We use N = %d' % ( n ) )
  print ( '  Radius R = %g' % ( r ) )
  print ( '  Center C = (%g,%g,%g)' % ( c[0], c[1], c[2] ) )

  ng = ball_grid_count ( n, r, c )

  print ( '' )
  print ( '  Number of grid points will be %d' % ( ng ) )

  xg = ball_grid_points ( n, r, c, ng )

  r83col_print_part ( ng, xg, 20, '  Part of the grid point array:' )

  filename = 'ball_grid_points.xyz'

  r8mat_write ( filename, ng, 3, xg )

  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )
#
#  Plot the grid.
#
  filename = 'ball_grid_points.png'

  ball_grid_display ( r, c, ng, xg, filename )

  print ( '' )
  print ( '  Plot written to the file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ball_grid_points_test():' )
  print ( '  Normal end of execution.' )
  return
  
def ball_grid_test ( ):

#*****************************************************************************80
#
## ball_grid_test() tests ball_grid().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ball_grid_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test ball_grid()' )
#
#  Utilities:
#
  r83col_print_part_test ( )
  r8mat_write_test ( )
#
#  Library.
#
  ball_grid_display_test ( )
  ball_grid_count_test ( )
  ball_grid_points_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ball_grid_test():' )
  print ( '  Normal end of execution.' )

def r83col_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## r83col_print_part() prints "part" of an R83COL.
#
#  Discussion:
#
#    An R83COL is a (3,N) array of R8's.
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_PRINT, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(N,3), the vector to be printed.
#
#    integer MAX_PRINT, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( 0 < max_print ):

    if ( 0 < n ):

      if ( 0 < len ( title ) ):
        print ( '' )
        print ( title )

      print ( '' )

      if ( n <= max_print ):

        for i in range ( 0, n ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
        print ( '  ....  ..............  ..............  ..............' )
        i = n - 1
        print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )

      else:

        for i in range ( 0, max_print - 1 ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
        i = max_print - 1
        print ( '  %4d  %14g  %14g  %14g  ...more entries...' \
          % ( i, a[i,0], a[i,1], a[i,2] ) )

  return

def r83col_print_part_test ( ):

#*****************************************************************************80
#
## r83col_print_part_test() tests r83col_print_part().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r83col_print_part_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r83col_print_part() prints part of an R83COL.' )

  n = 10

  v = np.array ( [ \
    [  11,  12,  13 ], \
    [  21,  22,  23 ], \
    [  31,  32,  33 ], \
    [  41,  42,  43 ], \
    [  51,  52,  53 ], \
    [  61,  62,  63 ], \
    [  71,  72,  73 ], \
    [  81,  82,  83 ], \
    [  91,  92,  93 ], \
    [ 101, 102, 103 ] ] )

  max_print = 2
  r83col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 2' )

  max_print = 5
  r83col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 5' )

  max_print = 25
  r83col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 25' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r83col_print_part_test():' )
  print ( '  Normal end of execution.' )
  return

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## r8mat_write() writes an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8mat_write_test ( ):

#*****************************************************************************80
#
## r8mat_write_test() tests r8mat_write().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_write_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_write() writes an R8MAT to a file.' )

  filename = 'r8mat_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 1.1, 1.2, 1.3 ), \
    ( 2.1, 2.2, 2.3 ), \
    ( 3.1, 3.2, 3.3 ), \
    ( 4.1, 4.2, 4.3 ), \
    ( 5.1, 5.2, 5.3 ) ) )
  r8mat_write ( filename, m, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_write_test():' )
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
  ball_grid_test ( )
  timestamp ( )

