#! /usr/bin/env python3
#
def naca4_cambered ( m, p, t, c, xc ):

#*****************************************************************************80
#
## naca4_cambered(): (xu,yu), (xl,yl) for a NACA cambered 4-digit airfoil.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eastman Jacobs, Kenneth Ward, Robert Pinkerton,
#    "The characteristics of 78 related airfoil sections from tests in
#    the variable-density wind tunnel",
#    NACA Report 460, 1933.
#
#  Input:
#
#    real M, the maximum camber.
#    0 < M.
#
#    real P, the location of maximum camber.
#    0.0 < P < 1.0
#
#    real T, the maximum relative thickness.
#    0.0 < T <= 1.0
#
#    real C, the chord length.
#    0.0 < C.
#
#    real XC(*), points along the chord length.  
#    0.0 <= XC(*) <= C.
#
#  Output:
#
#    real XU(*), YU(*), XL(*), YL(*), for each value of XC, measured
#    along the camber line, the corresponding values (XU,YU) on the upper
#    airfoil surface and (XL,YL) on the lower airfoil surface.
#
  import numpy as np

  i = np.nonzero ( 0.0 <= xc / c ) and np.nonzero ( xc / c <= p   )
  j = np.nonzero ( p   <= xc / c ) and np.nonzero ( xc / c <= 1.0 )
  k = np.nonzero ( xc / c < 0.0 ) or np.nonzero ( 1.0 < xc / c )

  n = len ( xc )

  divisor = np.zeros ( n )
  divisor[i] =         p  ** 2
  divisor[j] = ( 1.0 - p ) ** 2
  divisor[k] = 1.0

  dycdx = 2.0 * m * ( p - xc / c ) / divisor

  theta = np.arctan ( dycdx )
   
  yt = 5.0 * t * c * ( \
     0.2969 * np.sqrt ( xc / c ) \
     + (((( \
       - 0.1015 ) * ( xc / c ) \
       + 0.2843 ) * ( xc / c ) \
       - 0.3516 ) * ( xc / c ) \
       - 0.1260 ) * ( xc / c ) )

  yc = np.zeros ( n )
  yc[i] = m * ( xc[i]     ) * ( 2.0 * p - xc[i] / c       ) /         p   ** 2
  yc[j] = m * ( xc[j] - c ) * ( 2.0 * p - xc[j] / c - 1.0 ) / ( 1.0 - p ) ** 2
  yc[k] = 0.0

  xu = xc - yt * np.sin ( theta )
  yu = yc + yt * np.cos ( theta )
  xl = xc + yt * np.sin ( theta )
  yl = yc - yt * np.cos ( theta )

  return xu, yu, xl, yl

def naca4_cambered_test ( m, p, t ):

#*****************************************************************************80
#
## naca4_cambered_test() tests naca4_cambered().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real M, the maximum camber.
#    0 < M.
#
#    real P, the location of maximum camber.
#    0.0 < P < 1.0.
#
#    real T, the maximum relative thickness.
#    0.0 < T <= 1.0.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'NACA4_CAMBERED_TEST' )
  print ( '  NACA4_CAMBERED evaluates (xu,yu) and (xl,yl) for a NACA' )
  print ( '  cambered airfoil defined by a 4-digit code.' )

  c = 10.0
  n = 51

  xc = np.linspace ( 0.0, c, n )

  xu, yu, xl, yl = naca4_cambered ( m, p, t, c, xc )

  x2 = np.append ( xu, np.flip ( xl, 0 ) )
  y2 = np.append ( yu, np.flip ( yl, 0 ) )
#
#  Plot the wing surface.
#
  plt.plot ( x2, y2, 'b-', linewidth = 3 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.xlabel ( '<---X--->', fontsize = 16 )
  plt.ylabel ( '<---Y--->', fontsize = 16 )
  plt.title ( 'NACA 4-digit cambered airfoil', fontsize = 24 )

  filename = 'naca4_cambered_test.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved in file "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Save data to a file.
#
  filename = 'naca4_cambered_test.txt'
  output = open ( filename, 'w' )
  for i in range ( 0, 2 * n ):
    s = '  %g  %g\n' % ( x2[i], y2[i] )
    output.write ( s )
  output.close ( )
  print ( '  Data saved in file "%s"' % ( filename ) )

  return

def naca4_display_test ( ):

#*****************************************************************************80
#
## naca4_display_test() displays symmetric and cambered NACA 4 digit airfoils.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2018
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'NACA4_DISPLAY_TEST' )
  print ( '  Display symmetric and cambered NACA 4 digit airfoils.' )
  print ( '' )

  codes = np.array ( [ \
       6,    8,    9,   10,   12, \
      15,   18,   21,   24, 1408, 
    1410, 1412, 2408, 2410, 2411, 
    2412, 2414, 2415, 2418, 2421, 
    2424, 4412, 4415, 4418, 4421, 
    4424, 6409, 6412 ] )

  code_num = 28

  c = 10.0
  n = 51
  x = np.linspace ( 0.0, c, n )

  for code in codes:
 
    print ( '  NACA %04d airfoil.' % ( code ) )

    m, p, t = naca4_mpt ( code )

    if ( m == 0.0 ):

      y = naca4_symmetric ( t, c, x )
      x2 = np.append ( x, np.flip ( x, 0 ) )
      y2 = np.append ( y, np.flip ( -y, 0 ) )

      s = 'NACA%04d symmetric airfoil' % ( code )

    else:

      [ xu, yu, xl, yl ] = naca4_cambered ( m, p, t, c, x )
      x2 = np.append ( xu, np.flip ( xl, 0 ) )
      y2 = np.append ( yu, np.flip ( yl, 0 ) )

      s = 'NACA%04d cambered airfoil' % ( code )

    plt.plot ( x2, y2, 'b-', linewidth = 3 )
    plt.axis ( 'equal' )
    plt.grid ( True )
    plt.xlabel ( '<---X--->', fontsize = 16 )
    plt.ylabel ( '<---Y--->', fontsize = 16 )
    plt.title ( s, fontsize = 24 )
    plt.show ( block = False )
    plt.close ( )

  return

def naca4_mpt ( code ):

#*****************************************************************************80
#
## naca4_mpt() returns the parameters stored in a NACA 4 digit airfoil code.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer CODE, the NACA4 code.
#    0 <= CODE <= 9999.
#
#  Output:
#
#    real M, the maximum camber, as a percentage of the chord length.
#    0 <= M <= 1.0.
#
#    real P, the relative distance of the occurrence of the maximum 
#    camber from the beginning of the chord.
#    0 <= P <= 1.0.
#
#    real T, the maximum thickness relative to the chord length.
#    0 <= T <= 1.0.
#
  if ( code < 0 or 9999 < code ):
    print ( '' )
    print ( 'NACA4_MPT - Fatal error!' )
    print ( '  CODE should be an integer between 0 and 9999.' )
    raise Exception ( 'NACA4_MPT - Fatal error!' )

  m = ( code // 1000 )
  code = code - m * 1000
  m = m / 100.0

  p = ( code // 100 )
  code = code - p * 100
  p = p / 10.0

  t = code / 100.0

  return m, p, t

def naca4_mpt_test ( ):

#*****************************************************************************80
#
## naca4_mpt_test() tests naca4_mpt().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'NACA4_MPT_TEST' )
  print ( '  NACA4_MPT converts a NACA 4-digit code to' )
  print ( '  M, P, T values.' )

  codes = np.array ( [ \
       6,    8,    9,   10,   12, \
      15,   18,   21,   24, 1408, \
    1410, 1412, 2408, 2410, 2411, \
    2412, 2414, 2415, 2418, 2421, \
    2424, 4412, 4415, 4418, 4421, \
    4424, 6409, 6412 ] )

  print ( '' )
  print ( '  CODE      M       P       T' )
  print ( '' )

  for code in codes:
    m, p, t = naca4_mpt ( code )
    print ( '  %04d  %6.2f  %6.2f  %6.2f' % ( code, m, p, t ) )

def naca4_symmetric ( t, c, x ):

#*****************************************************************************80
#
## naca4_symmetric() evaluates y(x) for a NACA symmetric 4-digit airfoil.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eastman Jacobs, Kenneth Ward, Robert Pinkerton,
#    "The characteristics of 78 related airfoil sections from tests in
#    the variable-density wind tunnel",
#    NACA Report 460, 1933.
#
#  Input:
#
#    real T, the maximum relative thickness.
#
#    real C, the chord length.
#
#    real X(*), points along the chord length.  
#    0.0 <= X(*) <= C.
#
#  Output:
#
#    real Y(*), for each value of X, the corresponding value of Y
#    so that (X,Y) is on the upper wing surface, and (X,-Y) is on the
#    lower wing surface.
#
  import numpy as np

  y = 5.0 * t * c * ( \
    0.2969 * np.sqrt ( x / c )\
    + (((( \
      - 0.1015 ) * ( x / c ) \
      + 0.2843 ) * ( x / c ) \
      - 0.3516 ) * ( x / c ) \
      - 0.1260 ) * ( x / c ) )

  return y

def naca4_symmetric_test ( ):

#*****************************************************************************80
#
## naca4_symmetric_test() tests naca4_symmetric().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2018
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'NACA4_SYMMETRIC_TEST' )
  print ( '  NACA4_SYMMETRIC evaluates y(x) for a NACA' )
  print ( '  symmetric airfoil defined by a 4-digit code.' )

  c = 10.0
  t = 0.15
  n = 51
  x = np.linspace ( 0.0, c, n )
  x2 = np.append ( x, np.flip ( x, 0 ) )
  y = naca4_symmetric ( t, c, x )
  y2 = np.append ( y, np.flip ( -y, 0 ) )
#
#  Plot the wing surface.
#
  plt.plot ( x2, y2, 'b-', linewidth = 3 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.xlabel ( '<---X--->', fontsize = 16 )
  plt.ylabel ( '<---Y--->', fontsize = 16 )
  plt.title ( 'NACA 4-digit symmetric airfoil', fontsize = 24 )

  filename = 'naca4_symmetric_test.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved in file "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Save data to a file.
#
  filename = 'naca4_symmetric_test.txt'
  output = open ( filename, 'w' )
  for i in range ( 0, 2 * n ):
    s = '  %g  %g\n' % ( x2[i], y2[i] )
    output.write ( s )
  output.close ( )
  print ( '  Data saved in file "%s"' % ( filename ) )

  return

def naca_test ( ):

#*****************************************************************************80
#
## naca_test() tests naca().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NACA_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test naca().' )

  naca4_mpt_test ( )

  naca4_symmetric_test ( )

  code = 2412
  m, p, t = naca4_mpt ( code )
  naca4_cambered_test ( m, p, t )

  naca4_display_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'NACA_TEST:' )
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
  naca_test ( )
  timestamp ( )

