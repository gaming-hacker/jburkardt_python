#! /usr/bin/env python3
#
def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## r8mat_print_test() tests r8mat_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_print prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_print_some_test() tests r8mat_print_some.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_print_some prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## r8mat_write writes an R8MAT to a file.
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
## r8mat_write_test() tests r8mat_write.
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
  print ( 'r8mat_write_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test r8mat_write, which writes an R8MAT to a file.' )

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
  print ( 'r8mat_write_test:' )
  print ( '  Normal end of execution.' )
  return
  
def sphere_fibonacci_grid_display ( ng, xg, filename ):

#*****************************************************************************80
#
## sphere_fibonacci_grid_display displays a Fibonacci grid on a sphere.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NG, the number of grid points.
#
#    real XG(3,NG), the coordinates of the grid points.
#
#    string FILENAME, the name of the output file.
#
  import matplotlib.pyplot as plt
  import numpy as np
  from mpl_toolkits.mplot3d import Axes3D

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
#
#  Draw the grid points.
#
  ax.scatter ( xg[:,0], xg[:,1], xg[:,2], 'b' )

  ax.set_xlabel ( '<---X--->' )
  ax.set_ylabel ( '<---Y--->' )
  ax.set_zlabel ( '<---Z--->' )
  ax.set_title ( 'Fibonacci spiral on sphere' )
  ax.grid ( True )
# ax.axis ( 'equal' )
  print ( '  Graphics saved as "', filename, '"' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  return

def sphere_fibonacci_grid_display_test ( ):

#*****************************************************************************80
#
## sphere_fibonacci_grid_display_test() tests sphere_fibonacci_grid_display.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sphere_fibonacci_grid_display_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sphere_fibonacci_grid_display displays points on a sphere' )
  print ( '  that lie on a Fibonacci spiral.' )

  ng = 1000
  print ( '' )
  print ( '  Number of points NG = %d' % ( ng ) )

  xg = sphere_fibonacci_grid_points ( ng )
#
#  Display the nodes.
#
  filename = 'sphere_fibonacci_grid_display.png'

  sphere_fibonacci_grid_display ( ng, xg, filename )

  print ( '' )
  print ( '  Plot saved to file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'sphere_fibonacci_grid_display_test:' )
  print ( '  Normal end of execution.' )
  return

def sphere_fibonacci_grid_points ( ng ):

#*****************************************************************************80
#
## sphere_fibonacci_grid_points: Fibonacci spiral gridpoints on a sphere.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Swinbank, James Purser,
#    Fibonacci grids: A novel approach to global modelling,
#    Quarterly Journal of the Royal Meteorological Society,
#    Volume 132, Number 619, July 2006 Part B, pages 1769-1793.
#
#  Input:
#
#    integer NG, the number of points.
#
#  Output:
#
#    real XG(3,N), the grid points.
#
  import numpy as np

  phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0

  theta = np.zeros ( ng )
  sphi = np.zeros ( ng )
  cphi = np.zeros ( ng )

  for i in range ( 0, ng ):
    i2 = 2 * i - ( ng - 1 ) 
    theta[i] = 2.0 * np.pi * float ( i2 ) / phi
    sphi[i] = float ( i2 ) / float ( ng )
    cphi[i] = np.sqrt ( float ( ng + i2 ) * float ( ng - i2 ) ) / float ( ng )

  xg = np.zeros ( ( ng, 3 ) )

  for i in range ( 0, ng ) :
    xg[i,0] = cphi[i] * np.sin ( theta[i] )
    xg[i,1] = cphi[i] * np.cos ( theta[i] )
    xg[i,2] = sphi[i]

  return xg

def sphere_fibonacci_grid_points_test ( ):

#*****************************************************************************80
#
## sphere_fibonacci_grid_points_test() tests sphere_fibonacci_grid_points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sphere_fibonacci_grid_points_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sphere_fibonacci_grid_points computes points on a sphere' )
  print ( '  that lie on a Fibonacci spiral.' )

  ng = 1000
  print ( '' )
  print ( '  Number of points NG = %d' % ( ng ) )

  xg = sphere_fibonacci_grid_points ( ng )

  r8mat_print_some ( ng, 3, xg, 0, 0, 19, 2, '  Part of the grid array:' )
#
#  Write the nodes to a file.
#
  filename = 'sphere_fibonacci_grid_points.xyz'

  r8mat_write ( filename, ng, 3, xg )
#
#  Terminate.
#
  print ( '' )
  print ( 'sphere_fibonacci_grid_points_test:' )
  print ( '  Normal end of execution.' )
  return

def sphere_fibonacci_grid_test ( ):

#*****************************************************************************80
#
## sphere_fibonacci_grid_test() tests sphere_fibonacci_grid().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sphere_fibonacci_grid_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test sphere_fibonacci_grid().' )
#
#  Utilities:
#
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_write_test ( )
#
#  Library.
#
  sphere_fibonacci_grid_points_test ( )
  sphere_fibonacci_grid_display_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sphere_fibonacci_grid_test():' )
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
  sphere_fibonacci_grid_test ( )
  timestamp ( )

