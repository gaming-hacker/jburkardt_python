#! /usr/bin/env python3
#
def angle_degree ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## angle_degree() returns the degree angle defined by three points.
#
#  Discussion:
#
#        P1
#        /
#       /
#      /7
#     /
#    P2--------->P3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X1, Y1, X2, Y2, X3, Y3, the coordinates of the points
#    P1, P2, P3.
#
#  Output:
#
#    real VALUE, the angle swept out by the rays, measured
#    in degrees.  0 <= VALUE < 360.  If either ray has zero length,
#    then VALUE is set to 0.
#
  import numpy as np

  x = ( x3 - x2 ) * ( x1 - x2 ) + ( y3 - y2 ) * ( y1 - y2 )

  y = ( x3 - x2 ) * ( y1 - y2 ) - ( y3 - y2 ) * ( x1 - x2 )

  if ( x == 0.0 and y == 0.0 ):
    value = 0.0
    return value

  value = np.arctan2 ( y, x )

  if ( value < 0.0 ):
    value = value + 2.0 * np.pi

  value = 180.0 * value / np.pi

  return value

def angle_degree_test ( ):

#*****************************************************************************80
#
## angle_degree_test() tests angle_degree.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_angle = 12

  print ( '' )
  print ( 'angle_degree_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  angle_DEG_2D computes an angle;' )
  print ( '' )
  print ( '           X           Y       Theta  atan2(y,x)  angle_degree' )
  print ( '' )

  x2 = 0.0
  y2 = 0.0
  x3 = 1.0
  y3 = 0.0

  for i in range ( 0, n_angle + 1 ):

    thetad = float ( i ) * 360.0       / float ( n_angle )
    thetar = float ( i ) * 2.0 * np.pi / float ( n_angle )

    x1 = np.cos ( thetar )
    y1 = np.sin ( thetar )

    t1 = np.arctan2 ( y1, x1 ) * 180.0 / np.pi

    t2 = angle_degree ( x1, y1, x2, y2, x3, y3 )

    print ( '  %10f  %10f  %10f  %10f  %10f' \
      % ( x1, y1, thetad, t1, t2 ) )

  return

def angle_half ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## angle_half finds half an angle.
#
#  Discussion:
#
#    The original angle is defined by the sequence of points P1, P2 and P3.
#
#    The point P4 is calculated so that:
#
#      (P1,P2,P4) = (P1,P2,P3) / 2
#
#        P1
#        /
#       /   P4
#      /  .
#     / .
#    P2--------->P3
#
#    Thanks to Cesar Fraga Bobis for pointing out a typographical error in
#    a previous version of this routine.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X1, Y1, X2, Y2, X2, Y3, points defining the angle.
#
#  Output:
#
#    real P4(2), a point defining the half angle.
#    The vector P4 - P2 will have unit norm.
#
  import numpy as np

  p4 = np.zeros ( 2 )

  norm12 = np.sqrt ( ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2 )
  norm32 = np.sqrt ( ( x3 - x2 ) ** 2 + ( y3 - y2 ) ** 2 ) 

  x4 = 0.5 * ( ( x1 - x2 ) / norm12 + ( x3 - x2 ) / norm32 )

  y4 = 0.5 * ( ( y1 - y2 ) / norm12 + ( y3 - y2 ) / norm32 )

  norm = np.sqrt ( x4 ** 2 + y4 ** 2 )

  p4[0] = x2 + x4 / norm
  p4[1] = y2 + y4 / norm

  return p4

def angle_half_test ( ):

#*****************************************************************************80
#
## angle_half_test() tests angle_half.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_angle = 12

  print ( '' )
  print ( 'angle_half_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  angle_half is given P1, P2, P3, forming an angle;' )
  print ( '  It finds P4 so P4, P2, P3 is half the angle.' )
  print ( '' )
  print ( '  Original Angle    Half Angle' )
  print ( '' )

  x2 = 0.0
  y2 = 0.0
  x3 = 1.0
  y3 = 0.0

  for i in range ( 0, n_angle + 1 ):

    thetad = float ( i ) * 360.0       / float ( n_angle )
    thetar = float ( i ) * 2.0 * np.pi / float ( n_angle )

    x1 = np.cos ( thetar )
    y1 = np.sin ( thetar )

    t1 = np.arctan2 ( y1, x1 )

    t2 = angle_radian ( x1, y1, x2, y2, x3, y3 )

    p4 = angle_half ( x1, y1, x2, y2, x3, y3 )
    x4 = p4[0]
    y4 = p4[1]

    t3 = angle_radian ( x4, y4, x2, y2, x3, y3 )

    print ( '  %10f  %10f' % ( t2, t3 ) )

  return

def angle_radian ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## angle_radian returns the angle swept out between two rays.
#
#  Discussion:
#
#    Except for the zero angle case, it should be true that
#
#      angle_radian(P1,P2,P3) + angle_radian(P3,P2,P1) = 2 * PI
#
#        P1
#        /
#       /
#      /
#     /
#    P2--------->P3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X1, Y1, X2, Y2, X3, Y3, define the rays
#    P1 - P2 and P3 - P2 which in turn define the angle.
#
#  Output:
#
#    real VALUE, the angle swept out by the rays, measured
#    in radians.  0 <= VALUE < 2*PI.  If either ray has zero length,
#    then VALUE is set to 0.
#
  import numpy as np

  p = np.zeros ( 2 )

  p[0] = ( x3 - x2 ) * ( x1 - x2 ) \
       + ( y3 - y2 ) * ( y1 - y2 )

  p[1] = ( x3 - x2 ) * ( y1 - y2 ) \
       - ( y3 - y2 ) * ( x1 - x2 )

  if ( p[0] == 0.0 and p[1] == 0.0 ):
    value = 0.0
    return value

  value = np.arctan2 ( p[1], p[0] )

  if ( value < 0.0 ):
    value = value + 2.0 * np.pi

  return value

def angle_radian_test ( ):

#*****************************************************************************80
#
## angle_radian_test() tests angle_radian.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_angle = 12

  print ( '' )
  print ( 'angle_radian_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  angle_radian computes an angle in radians;' )
  print ( '' )
  print ( '           X           Y       Theta  atan2(y,x)  angle_radian' )
  print ( '' )

  x2 = 0.0
  y2 = 0.0
  x3 = 1.0
  y3 = 0.0

  for i in range ( 0, n_angle + 1 ):

    thetad = float ( i ) * 360.0       / float ( n_angle )
    thetar = float ( i ) * 2.0 * np.pi / float ( n_angle )

    x1 = np.cos ( thetar )
    y1 = np.sin ( thetar )

    t1 = np.arctan2 ( y1, x1 )

    t2 = angle_radian ( x1, y1, x2, y2, x3, y3 )

    print ( '  %10f  %10f  %10f  %10f  %10f' \
      % ( x1, y1, thetad, t1, t2 ) )

  return

def between ( xa, ya, xb, yb, xc, yc ):

#*****************************************************************************80
#
## between() is TRUE if vertex C is between vertices A and B.
#
#  Discussion:
#
#    The points must be (numerically) collinear.
#
#    Given that condition, we take the greater of XA - XB and YA - YB
#    as a "scale" and check where C's value lies.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, the coordinates of 
#    the vertices.
#
#  Output:
#
#    bool VALUE, is TRUE if C is between A and B.
#
  if ( not collinear ( xa, ya, xb, yb, xc, yc ) ):
    value = False
  elif ( abs ( ya - yb ) < abs ( xa - xb ) ):
    xmax = max ( xa, xb )
    xmin = min ( xa, xb )
    value = ( xmin <= xc and xc <= xmax )
  else:
    ymax = max ( ya, yb )
    ymin = min ( ya, yb )
    value = ( ymin <= yc and yc <= ymax )

  return value

def collinear ( xa, ya, xb, yb, xc, yc ):

#*****************************************************************************80
#
## collinear() returns a measure of collinearity for three points.
#
#  Discussion:
#
#    In order to deal with collinear points whose coordinates are not
#    numerically exact, we compare the area of the largest square
#    that can be created by the line segment between two of the points
#    to (twice) the area of the triangle formed by the points.
#
#    If the points are collinear, their triangle has zero area.
#    If the points are close to collinear, then the area of this triangle
#    will be small relative to the square of the longest segment.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 September 2016
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, the coordinates of 
#    the vertices.
#
#  Output:
#
#    bool VALUE, is TRUE if the points are judged 
#    to be collinear.
#
  r8_eps = 2.220446049250313E-016

  area = triangle_area ( xa, ya, xb, yb, xc, yc )

  side_ab_sq = ( xa - xb ) ** 2 + ( ya - yb ) ** 2
  side_bc_sq = ( xb - xc ) ** 2 + ( yb - yc ) ** 2
  side_ca_sq = ( xc - xa ) ** 2 + ( yc - ya ) ** 2

  side_max_sq = max ( side_ab_sq, max ( side_bc_sq, side_ca_sq ) )

  if ( side_max_sq <= r8_eps ):
    value = True
  elif ( 2.0 * abs ( area ) <= r8_eps * side_max_sq ):
    value = True
  else:
    value = False

  return value

def diagonal ( im1, ip1, n, prev_node, next_node, x, y ):

#*****************************************************************************80
#
## diagonal(): VERTEX(IM1) to VERTEX(IP1) is a proper internal diagonal.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    integer IM1, IP1, the indices of two vertices.
#
#    integer N, the number of vertices.
#
#    integer PREV_NODE(N), the previous neighbor of each vertex.
#
#    integer NEXT_NODE(N), the next neighbor of each vertex.
#
#    real X(N), Y(N), the coordinates of each vertex.
#
#  Output:
#
#    bool VALUE, the value of the test.
#  
  value1 = in_cone ( im1, ip1, n, prev_node, next_node, x, y )
  value2 = in_cone ( ip1, im1, n, prev_node, next_node, x, y )
  value3 = diagonalie ( im1, ip1, n, next_node, x, y )

  value = ( value1 and value2 and value3 )

  return value

def diagonalie ( im1, ip1, n, next_node, x, y ):

#*****************************************************************************80
#
## diagonalie() is true if VERTEX(IM1):VERTEX(IP1) is a proper diagonal.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    integer IM1, IP1, the indices of two vertices.
#
#    integer N, the number of vertices.
#
#    integer NEXT_NODE(N), the next neighbor of each vertex.
#
#    real X(N), Y(N), the coordinates of each vertex.
#
#  Output:
#
#    bool VALUE, the value of the test.
#
  first = im1
  j = first
  jp1 = next_node[first]

  value = True
#
#  For each edge VERTEX(J):VERTEX(JP1) of the polygon:
#
  while ( True ):
#
#  Skip any edge that includes vertex IM1 or IP1.
#
    if ( j == im1 or j == ip1 or jp1 == im1 or jp1 == ip1 ):
      pass
    else:

      value2 = intersect ( \
        x[im1], y[im1], x[ip1], y[ip1], x[j], y[j], x[jp1], y[jp1] )

      if ( value2 ):
        value = False
        break

    j = jp1
    jp1 = next_node[j]

    if ( j == first ):
      break

  return value

def i4_ceiling ( x ) :

#*****************************************************************************80
#
## i4_ceiling rounds an R8 up to the next I4.
#
#  Example:
#
#    X         Value
#
#   -1.1      -1
#   -1.0      -1
#   -0.9       0
#   -0.1       0
#    0.0       0
#    0.1       1
#    0.9       1
#    1.0       1
#    1.1       2
#    2.9       3
#    3.0       3
#    3.14159   4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number to be rounded up.
#
#  Output:
#
#    integer VALUE, the rounded value of X.
#
  import numpy as np

  value = int ( np.ceil ( x ) )

  return value

def i4_ceiling_test ( ):

#*****************************************************************************80
#
## i4_ceiling_test() tests i4_ceiling.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  r8_lo = -100.0
  r8_hi =  100.0

  print ( '' )
  print ( 'i4_ceiling_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_ceiling evaluates the "ceiling" of a real number.' )
  print ( ' ' )
  print ( '      R8    i4_ceiling(R8)' )
  print ( ' ' )

  for i in range ( 0, 10 ):
    r8 = r8_lo + ( r8_hi - r8_lo ) * np.random.rand ( )
    i4 = i4_ceiling ( r8 )
    print ( '  %8.4f            %4d' % ( r8, i4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_ceiling_test' )
  print ( '  Normal end of execution.' )
  return

def i4_modp ( i, j ):

#*****************************************************************************80
#
## i4_modp returns the nonnegative remainder of I4 division.
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
#    integer VALUE, the nonnegative remainder when I is divided by J.
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
## i4_modp_test() tests i4_modp.
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

def i4_wrap ( value, lo, hi ):

#*****************************************************************************80
#
## i4_wrap forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    LO = 4, HI = 8
#
#    In   Out
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
#    23 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer VALUE, an integer value.
#
#    integer LO, HI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of VALUE.
#
  value = lo + ( ( value - lo ) % ( hi - lo + 1 ) )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## i4_wrap_test() tests i4_wrap.
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

def i4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## i4mat_print prints an I4MAT.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    integer A(M,N), the matrix.
#
#    string TITLE, a title.
#
  i4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_print_test ( ):

#*****************************************************************************80
#
## i4mat_print_test() tests i4mat_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4mat_print_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test i4mat_print, which prints an I4MAT.' )

  m = 5
  n = 6
  a = np.array ( ( \
    ( 11, 12, 13, 14, 15, 16 ), \
    ( 21, 22, 23, 24, 25, 26 ), \
    ( 31, 32, 33, 34, 35, 36 ), \
    ( 41, 42, 43, 44, 45, 46 ), \
    ( 51, 52, 53, 54, 55, 56 ) ) )
  title = '  A 5 x 6 integer matrix:'
  i4mat_print ( m, n, a, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4mat_print_test:' )
  print ( '  Normal end of execution.' )
  return

def i4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## i4mat_print_some prints out a portion of an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer A(M,N), an M by N matrix to be printed.
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
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d  ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%7d  ' % ( a[i,j] ) ),

      print ( '' )

  return

def i4mat_print_some_test ( ):

#*****************************************************************************80
#
## i4mat_print_some_test() tests i4mat_print_some.
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
  print ( 'i4mat_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4mat_print_some prints some of an I4MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is I4MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4mat_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print prints an I4VEC.
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
#    integer N, the dimension of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_test ( ):

#*****************************************************************************80
#
## i4vec_print_test() tests i4vec_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4vec_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_print prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_print_test:' )
  print ( '  Normal end of execution.' )
  return

def in_cone ( im1, ip1, n, prev_node, next_node, x, y ):

#*****************************************************************************80
#
## in_cone is TRUE if the diagonal VERTEX(IM1):VERTEX(IP1) is strictly internal.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    integer IM1, IP1, the indices of two vertices.
#
#    integer N, the number of vertices.
#
#    integer PREV_NODE(N), the previous neighbor of each vertex.
#
#    integer NEXT_NODE(N), the next neighbor of each vertex.
#
#    real X(N), Y(N), the coordinates of each vertex.
#
#  Output:
#
#    bool VALUE, the value of the test.
#
  im2 = prev_node[im1]
  i = next_node[im1]

  t1 = triangle_area ( x[im1], y[im1], x[i], y[i], x[im2], y[im2] )

  if ( 0.0 <= t1 ):

    t2 = triangle_area ( x[im1], y[im1], x[ip1], y[ip1], x[im2], y[im2] )
    t3 = triangle_area ( x[ip1], y[ip1], x[im1], y[im1], x[i], y[i] )
    value = ( ( 0.0 < t2 ) and ( 0.0 < t3 ) )

  else:

    t4 = triangle_area ( x[im1], y[im1], x[ip1], y[ip1], x[i], y[i] )
    t5 = triangle_area ( x[ip1], y[ip1], x[im1], y[im1], x[im2], y[im2] )
    value = not ( ( 0.0 <= t4 ) and ( 0.0 <= t5 ) )

  return value

def intersect ( xa, ya, xb, yb, xc, yc, xd, yd ):

#*****************************************************************************80
#
## intersect is true if lines VA:VB and VC:VD intersect.
#
#  Discussion:
#
#    Thanks to Gene Dial for correcting the call to intersect_prop(),
#    08 September 2016.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 September 2016
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, XD, YD, the X and Y 
#    coordinates of the four vertices.
#
#  Output:
#
#    bool VALUE, the value of the test.
#
  if ( intersect_prop ( xa, ya, xb, yb, xc, yc, xd, yd ) ):
    value = True
  elif ( between ( xa, ya, xb, yb, xc, yc ) ):
    value = True
  elif ( between ( xa, ya, xb, yb, xd, yd ) ):
    value = True
  elif ( between ( xc, yc, xd, yd, xa, ya ) ):
    value = True
  elif ( between ( xc, yc, xd, yd, xb, yb ) ):
    value = True
  else:
    value = False

  return value

def intersect_prop ( xa, ya, xb, yb, xc, yc, xd, yd ):

#*****************************************************************************80
#
## intersect_prop is TRUE if lines VA:VB and VC:VD have a proper intersection.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    FORTRAN90 version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, XD, YD, the X and Y 
#    coordinates of the four vertices.
#
#  Output:
#
#    bool VALUE, the result of the test.
#
  if ( collinear ( xa, ya, xb, yb, xc, yc ) ):
    value = False
  elif ( collinear ( xa, ya, xb, yb, xd, yd ) ):
    value = False
  elif ( collinear ( xc, yc, xd, yd, xa, ya ) ):
    value = False
  elif ( collinear ( xc, yc, xd, yd, xb, yb ) ):
    value = False
  else:
    t1 = triangle_area ( xa, ya, xb, yb, xc, yc )
    t2 = triangle_area ( xa, ya, xb, yb, xd, yd )
    t3 = triangle_area ( xc, yc, xd, yd, xa, ya )
    t4 = triangle_area ( xc, yc, xd, yd, xb, yb )

    value1 = ( 0.0 < t1 )
    value2 = ( 0.0 < t2 )
    value3 = ( 0.0 < t3 )
    value4 = ( 0.0 < t4 )

    value = ( l4_xor ( value1, value2 ) ) and ( l4_xor ( value3, value4 ) )
 
  return value

def l4_xor ( l1, l2 ):

#*****************************************************************************80
#
## l4_xor returns the exclusive OR of two L4's.
#
#  Discussion:
#
#    An L4 is a bool VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#   John Burkardt
#
#  Input:
#
#    bool L1, L2, two values whose exclusive OR 
#    is needed.
#
#  Output:
#
#    bool VALUE, the exclusive OR of L1 and L2.
#
  value1 = (       l1   and ( not l2 ) )
  value2 = ( ( not l1 ) and       l2   )

  value = ( value1 or value2 )

  return value

def polygon_angles ( n, v ):

#*****************************************************************************80
#
## polygon_angles computes the interior angles of a polygon.
#
#  Discussion:
#
#    The vertices should be listed in counterclockwise order.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#
#    real V(2,N), the vertices.
#
#  Output:
#
#    real ANGLE(N), the angles of the polygon,
#    in radians.
#
  import numpy as np

  angle = np.zeros ( n )

  if ( n <= 2 ):
    return angle

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 );
    ip1 = i4_wrap ( i + 1, 0, n - 1 );

    angle[i] = angle_radian ( v[0,im1], v[1,im1], v[0,i], v[1,i], \
      v[0,ip1], v[1,ip1] )

  return angle

def polygon_angles_test ( ):

#*****************************************************************************80
#
## polygon_angles_test() tests polygon_angles.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 6
  v = np.array ( [ \
    [ 0.0, 1.0, 2.0, 3.0, 3.0, 1.0 ], \
    [ 0.0, 0.0, 1.0, 0.0, 2.0, 1.0 ] ] )

  print ( '' )
  print ( 'polygon_angles_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_angles computes the angles of a polygon.' )

  print ( '' )
  print ( '  Number of polygonal vertices = %d' % ( n ) )

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  angle = polygon_angles ( n, v )

  print ( '' )
  print ( '  Polygonal angles in degrees:' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %8d  %14.6g' % ( i, angle[i] * 180.0 / np.pi ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_angles_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_area ( n, v ):

#*****************************************************************************80
#
## polygon_area computes the area of a polygon.
#
#  Discussion:
#
#    AREA = 1/2 * abs ( sum ( 1 <= I <= N ) X(I) * ( Y(I+1) - Y(I-1) ) )
#    where Y(0) should be replaced by Y(N), and Y(N+1) by Y(1).
#
#    If the vertices are given in counterclockwise order, the area
#    will be positive.  If the vertices are given in clockwise order,
#    the area will be negative.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#
#    real V(2,N), the vertices.
#
#  Output:
#
#    real AREA, the area of the polygon.
#
  area = 0.0

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )
    ip1 = i4_wrap ( i + 1, 0, n - 1 )

    area = area + v[0,i] * ( v[1,ip1] - v[1,im1] )

  area = 0.5 * area;

  return area

def polygon_area_test ( ):

#*****************************************************************************80
#
## polygon_area_test() tests polygon_area.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 2
  area_exact_test = np.array ( [ 2.0, 6.0 ] )
  n_test = np.array ( [ 4, 8 ] )

  print ( '' )
  print ( 'polygon_area_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_area computes the area of a polygon.' )

  for test in range ( 0, test_num ):

    n = n_test[test]
    area_exact = area_exact_test[test]

    if ( test == 0 ):

      v = np.array ( [ \
        [ 1.0, 2.0, 1.0, 0.0 ], \
        [ 0.0, 1.0, 2.0, 1.0 ] ] )

    elif ( test == 1 ):

      v = np.array ( [ \
        [ 0.0, 3.0, 3.0, 2.0, 2.0, 1.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 3.0, 3.0, 1.0, 1.0, 2.0, 2.0 ] ] )

    print ( '' )
    print ( '  Number of polygonal vertices = %d' % ( n ) )

    r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

    area = polygon_area ( n, v )

    print ( '' )
    print ( '  Exact area is        %g' % ( area_exact ) )
    print ( '  The computed area is %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_area_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_area_2 ( n, v ):

#*****************************************************************************80
#
## polygon_area_2 computes the area of a polygon.
#
#  Discussion:
#
#    The area is the sum of the areas of the triangles formed by
#    node N with consecutive pairs of nodes.
#
#    If the vertices are given in counterclockwise order, the area
#    will be positive.  If the vertices are given in clockwise order,
#    the area will be negative.
#
#    Thanks to Martin Pineault for noticing that an earlier version
#    of this routine would not correctly compute the area of a nonconvex
#    polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Adrian Bowyer, John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#
#    real V(2,N), the vertices.
#
#  Output:
#
#    real AREA, the area of the polygon.
#
  area = 0.0

  for i in range ( 0, n - 2 ):

    area_triangle = triangle_area ( \
      v[0,i],   v[1,i],   \
      v[0,i+1], v[1,i+1], \
      v[0,n-1], v[1,n-1] )

    area = area + area_triangle

  return area

def polygon_area_2_test ( ):

#*****************************************************************************80
#
## polygon_area_2_test() tests polygon_area_2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 2
  area_exact_test = np.array ( [ 2.0, 6.0 ] )
  n_test = np.array ( [ 4, 8 ] )

  print ( '' )
  print ( 'polygon_area_2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_area_2 computes the area of a polygon.' )

  for test in range ( 0, test_num ):

    n = n_test[test]
    area_exact = area_exact_test[test]

    if ( test == 0 ):

      v = np.array ( [ \
        [ 1.0, 2.0, 1.0, 0.0 ], \
        [ 0.0, 1.0, 2.0, 1.0 ] ] )

    elif ( test == 1 ):

      v = np.array ( [ \
        [ 0.0, 3.0, 3.0, 2.0, 2.0, 1.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 3.0, 3.0, 1.0, 1.0, 2.0, 2.0 ] ] )

    print ( '' )
    print ( '  Number of polygonal vertices = %d' % ( n ) )

    r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

    area = polygon_area_2 ( n, v )

    print ( '' )
    print ( '  Exact area is        %g' % ( area_exact ) )
    print ( '  The computed area is %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_area_2_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_area_3 ( n, x, y ):

#*****************************************************************************80
#
## polygon_area_3 returns the area of a polygon.
#
#  Discussion:
#
#    The vertices should be listed in counter-clockwise order so that
#    the area will be positive.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 September 2016
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the number of vertices.
#
#    real X(N), Y(N), the vertex coordinates.
#
#  Output:
#
#    real AREA, the area of the polygon.
#
  area = 0.0
  im1 = n - 1

  for i in range ( 0, n ):
    area = area + x[im1] * y[i] - x[i] * y[im1]
    im1 = i

  area = 0.5 * area

  return area

def polygon_centroid_2 ( n, v ):

#*****************************************************************************80
#
## polygon_centroid_2 computes the centroid of a polygon.
#
#  Discussion:
#
#    The centroid is the area-weighted sum of the centroids of
#    disjoint triangles that make up the polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Adrian Bowyer and John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Input:
#
#    integer N, the number of sides of the polygon.
#
#    real V(2,N), the coordinates of the vertices.
#
#  Output:
#
#    real CENTROID(2), the coordinates of the centroid.
#
  import numpy as np

  area = 0.0
  centroid = np.zeros ( 2 )

  for i in range ( 0, n - 2 ):

    area_triangle = triangle_area ( \
      v[0,i],   v[1,i], \
      v[0,i+1], v[1,i+1], \
      v[0,n-1], v[1,n-1] )

    area = area + area_triangle

    centroid[0] = centroid[0] + ( v[0,i] + v[0,i+1] + v[0,n-1] ) * area_triangle / 3.0
    centroid[1] = centroid[1] + ( v[1,i] + v[1,i+1] + v[1,n-1] ) * area_triangle / 3.0

  if ( area == 0.0 ):
    centroid[0] = v[0]
    centroid[1] = v[1]
  else:
    centroid[0] = centroid[0] / area
    centroid[1] = centroid[1] / area

  return centroid

def polygon_centroid_2_test ( ):

#*****************************************************************************80
#
## polygon_centroid_2_test() tests polygon_centroid_2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4
  v = np.array ( [ \
    [ 1.0, 2.0, 1.0, 0.0 ], \
    [ 0.0, 1.0, 2.0, 1.0 ] ] )

  print ( '' )
  print ( 'polygon_centroid_2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_centroid_2 computes the centroid of a polygon.' )

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  centroid = polygon_centroid_2 ( n, v )

  r8vec_print ( 2, centroid, '  polygon_centroid_2:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_centroid_2_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_centroid ( n, v ):

#*****************************************************************************80
#
## polygon_centroid computes the centroid of a polygon.
#
#  Discussion:
#
#    Denoting the centroid coordinates by CENTROID, then
#
#      CENTROID(1) = Integral ( Polygon interior ) x dx dy / Area ( Polygon )
#      CENTROID(2) = Integral ( Polygon interior ) y dx dy / Area ( Polygon ).
#
#    Green's theorem states that for continuously differentiable functions
#    M(x,y) and N(x,y),
#
#      Integral ( Polygon boundary ) ( M dx + N dy ) =
#      Integral ( Polygon interior ) ( dN/dx - dM/dy ) dx dy.
#
#    Using M(x,y) = 0 and N(x,y) = x^2/2, we get:
#
#      CENTROID(1) = 0.5 * Integral ( Polygon boundary ) x^2 dy
#                  / Area ( Polygon ),
#
#    which becomes
#
#      CENTROID(1) = 1/6 sum ( 1 <= I <= N )
#        ( X(I+1) + X(I) ) * ( X(I) * Y(I+1) - X(I+1) * Y(I))
#        / Area ( Polygon )
#
#    where, when I = N, the index "I+1" is replaced by 1.
#
#    A similar calculation gives us a formula for CENTROID(2).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gerard Bashein and Paul Detmer,
#    Centroid of a Polygon,
#    Graphics Gems IV,
#    edited by Paul Heckbert,
#    AP Professional, 1994.
#
#  Input:
#
#    integer N, the number of sides of the polygon.
#
#    real V(2,N), the coordinates of the vertices.
#
#  Output:
#
#    real CENTROID(2,1), the coordinates of the centroid.
#
  import numpy as np

  area = 0.0
  centroid = np.zeros ( 2 )

  for i in range ( 0, n ):

    ip1 = i4_wrap ( i + 1, 0, n - 1 )

    temp = ( v[0,i] * v[1,ip1] - v[0,ip1] * v[1,i] )

    area = area + temp

    centroid[0] = centroid[0] + ( v[0,ip1] + v[0,i] ) * temp
    centroid[1] = centroid[1] + ( v[1,ip1] + v[1,i] ) * temp

  area = area / 2.0

  if ( area == 0.0 ):
    centroid[0] = v[0]
    centroid[1] = v[1]
  else:
    centroid[0] = centroid[0] / ( 6.0 * area )
    centroid[1] = centroid[1] / ( 6.0 * area )

  return centroid

def polygon_centroid_test ( ):

#*****************************************************************************80
#
## polygon_centroid_test() tests polygon_centroid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4
  v = np.array ( [ \
    [ 1.0, 2.0, 1.0, 0.0 ], \
    [ 0.0, 1.0, 2.0, 1.0 ] ] )

  print ( '' )
  print ( 'polygon_centroid_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_centroid computes the centroid of a polygon.' )

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  centroid = polygon_centroid ( n, v )

  r8vec_print ( 2, centroid, '  polygon_centroid:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_centroid_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_contains_point_2 ( n, v, p ):

#*****************************************************************************80
#
## polygon_contains_point_2 finds if a point is inside a convex polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of nodes or vertices in the polygon.
#    N must be at least 3.
#
#    real V(2,N), the coordinates of the vertices of the polygon.
#
#    real P(2), the coordinates of the point to be tested.
#
#  Output:
#
#    bool INSIDE, is TRUE if the point is inside the polygon.
#
  import numpy as np

  inside = False
#
#  A point is inside a convex polygon if and only if it is inside
#  one of the triangles formed by X(1),Y(1) and any two consecutive
#  points on the polygon's circumference.
#
  t = np.zeros ( [ 2, 3 ] )

  t[0,0] = v[0,0]
  t[1,0] = v[1,0]

  for i in range ( 1, n - 1 ):

    t[0,1] = v[0,i]
    t[1,1] = v[1,i]
    t[0,2] = v[0,i+1]
    t[1,2] = v[1,i+1]

    inside = triangle_contains_point_1 ( t, p )

    if ( inside ):
      break

  return inside

def polygon_contains_point_2_test ( ):

#*****************************************************************************80
#
## polygon_contains_point_2_test() tests polygon_contains_point_2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  test_num = 4

  p_test = np.array ( [ \
    [ 1.0, 3.0, 0.0, 0.5 ], \
    [ 1.0, 4.0, 2.0, -0.25 ] ] )

  v = np.array ( [ \
    [ 0.0, 1.0, 2.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 2.0, 2.0 ] ] )
 
  p = np.zeros ( 2 )

  print ( '' )
  print ( 'polygon_contains_point_2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_contains_point_2 determines if' )
  print ( '  a point is in a polygon.' )

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  print ( '' )
  print ( '          P          Inside' )
  print ( '' )

  for test in range ( 0, test_num ):
 
    p[0] = p_test[0,test]
    p[1] = p_test[1,test]
 
    inside = polygon_contains_point_2 ( n, v, p )

    print ( '  %14.6g  %14.6g    %d' % ( p[0], p[1], inside ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_contains_point_2_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_contains_point ( x, y, px, py ):

#*****************************************************************************80
#
## polygon_contains_point finds if a point is inside a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the coordinates of the point to be tested.
#
#    real PX(N), PY(N), the coordinates of the vertices of the polygon.
#
#  Output:
#
#    bool INSIDE, is TRUE if the point is inside the polygon.
#
  n = len ( px )
  inside = False

  px1 = px[0]
  py1 = py[0]
  xints = x - 1.0
  for i in range ( 0, n + 1 ):
    px2 = px[i%n]
    py2 = py[i%n]
    if ( min ( py1, py2 ) < y ):
      if ( y <= max ( py1, py2 ) ):
        if ( x <= max ( px1, px2 ) ):
          if ( py1 != py2 ):
            xints = ( y - py1 ) * ( px2 - px1 ) / ( py2 - py1 ) + px1
          if ( px1 == px2 or x <= xints ):
            inside = not inside
    px1 = px2
    py1 = py2

  return inside

def polygon_contains_point_test ( ):

#*****************************************************************************80
#
## polygon_contains_point_test() tests polygon_contains_point.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  test_num = 4

  x_test = np.array ( [ 1.0, 3.0, 0.0, 0.5 ] )

  y_test = np.array ( [ 1.0, 4.0, 2.0, -0.25 ] )

  px = np.array ( [ 0.0, 1.0, 2.0, 1.0, 0.0 ] )
 
  py = np.array ( [ 0.0, 0.0, 1.0, 2.0, 2.0 ] )

  print ( '' )
  print ( 'polygon_contains_point_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_contains_point determines if' )
  print ( '  a point is in a polygon.' )

  r8vec2_print ( n, px, py, '  The polygon vertices:' )

  print ( '' )
  print ( '        X         Y     Inside?' )
  print ( '' )

  for test in range ( 0, test_num ):
 
    x = x_test[test]
    y = y_test[test]
 
    inside = polygon_contains_point ( x, y, px, py )

    print ( '  %8.2f  %8.2f    %s' % ( x, y, inside ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_contains_point_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_diameter ( n, v ):

#*****************************************************************************80
#
## polygon_diameter computes the diameter of a polygon.
#
#  Discussion:
#
#    The diameter of a polygon is the maximum distance between any
#    two points on the polygon.  It is guaranteed that this maximum
#    distance occurs between two vertices of the polygon.  It is
#    sufficient to check the distance between all pairs of vertices.
#    This is an N^2 algorithm.  There is an algorithm by Shamos which
#    can compute this quantity in order N time instead.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#
#    real V(2,N), the vertices.
#
#  Output:
#
#    real DIAMETER, the diameter of the polygon.
#
  import numpy as np

  diameter = 0.0

  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      diameter = max ( diameter, \
        np.sqrt ( ( v[0,i] - v[0,j] ) ** 2 + ( v[1,i] - v[1,j] ) ** 2 ) )

  return diameter

def polygon_diameter_test ( ):

#*****************************************************************************80
#
## polygon_diameter_test() tests polygon_diameter;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4
  diameter_exact = 2.0
  v = np.array ( [ \
    [ 1.0, 2.0, 1.0, 0.0 ], \
    [ 0.0, 1.0, 2.0, 1.0 ] ] )

  print ( '' )
  print ( 'polygon_diameter_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_diameter computes the diameter of a polygon.' )

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  diameter = polygon_diameter ( n, v )

  print ( '' )
  print ( '  Diameter ( computed ) %g' % ( diameter ) )
  print ( '  Diameter ( exact )    %g' % ( diameter_exact ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_diameter_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_expand ( n, v, h ):

#*****************************************************************************80
#
## polygon_expand expands a polygon.
#
#  Discussion:
#
#    This routine simple moves each vertex of the polygon outwards
#    in such a way that the sides of the polygon advance by H.
#
#    This approach should always work if the polygon is convex, or
#    star-shaped.  But for general polygons, it is possible
#    that this procedure, for large enough H, will create a polygon
#    whose sides intersect.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of sides of the polygon.
#
#    real V(2,N), the coordinates of the vertices.
#
#    real H, the expansion amount.
#
#  Output:
#
#    real W(2,N), the "expanded" coordinates.
#
  import numpy as np

  w = np.zeros ( [ 2, n ] )
#
#  Consider each angle, formed by the nodes P(I-1), P(I), P(I+1).
#
  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )
    ip1 = i4_wrap ( i + 1, 0, n - 1 )
#
#        P1
#        /
#       /   P4
#      /  .
#     / .
#    P2--------->P3
#
    p4 = angle_half ( v[0,im1], v[1,im1], v[0,i], v[1,i], v[0,ip1], v[1,ip1] )
#
#  Compute the value of the half angle.
#
    angle = angle_radian ( v[0,im1], v[1,im1], v[0,i], v[1,i], p4[0], p4[1] )
#
#  The stepsize along the ray must be adjusted so that the sides
#  move out by H.
#
    h2 = h / np.sin ( angle )

    w[0,i] = v[0,i] - h2 * ( p4[0] - v[0,i] )
    w[1,i] = v[1,i] - h2 * ( p4[1] - v[1,i] )

  return w

def polygon_expand_test ( ):

#*****************************************************************************80
#
## polygon_expand_test() tests polygon_expand;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  v = np.array ( [ \
    [ 1.0, 5.0, 2.0, 1.0 ], \
    [ 1.0, 1.0, 4.0, 3.0 ] ] )

  print ( '' )
  print ( 'polygon_expand_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_expand "expands" a polygon by an amount H.' )

  h = 0.5

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  print ( '' )
  print ( '  The expansion amount H = %g' % ( h ) )

  w = polygon_expand ( n, v, h )

  r8mat_transpose_print ( 2, n, w, '  The expanded polygon:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_expand_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_inrad_data ( n, radin ):

#*****************************************************************************80
#
## polygon_inrad_data determines polygonal data from its inner radius.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of sides of the polygon.
#    N must be at least 3.
#
#    real RADIN, the inner radius of the polygon, that is,
#    the radius of the largest circle that can be inscribed within
#    the polygon.
#
#  Output:
#
#    real AREA, the area of the regular polygon.
#
#    real RADOUT, the outer radius of the polygon, that is,
#    the radius of the smallest circle that can be described about
#    the polygon.
#
#    real SIDE, the length of one side of the polygon.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_inrad_data - Fatal error!' )
    print ( '  Input value of N must be at least 3' )
    print ( '  but your input value was N = %d' % ( n ) )
    raise Exception ( 'polygon_inrad_data - Fatal error!' )

  angle = np.pi / n
  area = n * radin * radin * np.tan ( angle )
  side = 2.0 * radin * np.tan ( angle )
  radout = 0.5 * side / np.sin ( angle )

  return area, radout, side

def polygon_inrad_data_test ( ):

#*****************************************************************************80
#
## polygon_inrad_data_test() tests polygon_inrad_data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'polygon_inrad_data_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_inrad_data uses the inradius of a regular polygon' )
  print ( '  to determine the area, outradius, and side length.' )

  for n in range ( 3, 6 ):

    print ( '' )
    print ( '  Number of polygonal sides = %d' % ( n ) )

    radin = 1.0
    print ( '' )
    print ( '  Assuming RADIN = %g' % ( radin ) )
    area, radout, side = polygon_inrad_data ( n, radin )
    print ( '    AREA =   %g' % ( area ) )
    print ( '    RADOUT = %g' % ( radout ) )
    print ( '    SIDE =   %g' % ( side ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_inrad_data_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_integral_1 ( n, v ):

#*****************************************************************************80
#
## polygon_integral_1 integrates the function 1 over a polygon.
#
#  Discussion
#
#    The polygon is bounded by the points (X(1:N), Y(1:N)).
#
#    INTEGRAL = 0.5 * SUM ( 1 <= I <= N )
#      ( X(I) + X(I-1) ) * ( Y(I) - Y(I-1) )
#
#    where X(0) and Y(0) should be replaced by X(N) and Y(N).
#
#    Note that the integral of 1 over a polygon is the area of the polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    S F Bockman,
#    Generalizing the Formula for Areas of Polygons to Moments,
#    American Mathematical Society Monthly,
#    1989, pages 131-132.
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#    N should be at least 3 for a nonzero result.
#
#    real V(2,N), the coordinates of the vertices
#    of the polygon.  These vertices should be given in counter-clockwise order.
#
#  Output:
#
#    real RESULT, the value of the integral.
#
  result = 0.0

  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_integral_1 - Warning!' )
    print ( '  The number of vertices must be at least 3.' )
    print ( '  The input value of N = %d' % ( n ) )
    raise Exception ( 'polygon_integral_1 - Fatal error!' )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )

    result = result + 0.5 * ( v[0,i] + v[0,im1] ) * ( v[1,i] - v[1,im1] )

  return result

def polygon_integral_1_test ( ):

#*****************************************************************************80
#
## polygon_integral_1_test() tests polygon_integral_1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  v1 = np.array ( [ \
    [ 0.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0 ] ] )

  n2 = 3
  v2 = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'polygon_integral_1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_integral_1 integrates 1 over a polygon' )

  r8mat_transpose_print ( 2, n1, v1, '  The polygon vertices:' )

  result = polygon_integral_1 ( n1, v1 )
  print ( '' )
  print ( '  1:    %14.6g' % ( result ) )

  r8mat_transpose_print ( 2, n2, v2, '  The polygon vertices:' )

  result = polygon_integral_1 ( n2, v2 )
  print ( '' )
  print ( '  1:    %14.6g' % ( result ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_integral_1_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_integral_x ( n, v ):

#*****************************************************************************80
#
## polygon_integral_x integrates the function X over a polygon.
#
#  Discussion
#
#    The polygon is bounded by the points (X(1:N), Y(1:N)).
#
#    INTEGRAL = (1/6) * sum ( 1 <= I <= N )
#      ( X(I)^2 + X(I) * X(I-1) + X(I-1)^2 ) * ( Y(I) - Y(I-1) )
#
#    where X(0) and Y(0) should be replaced by X(N) and Y(N).
#
#    Note that the integral of 1 over a polygon is the area of the polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    S F Bockman,
#    Generalizing the Formula for Areas of Polygons to Moments,
#    American Mathematical Society Monthly,
#    1989, pages 131-132.
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#    N should be at least 3 for a nonzero result.
#
#    real V(2,N), the coordinates of the vertices
#    of the polygon.  These vertices should be given in counter-clockwise order.
#
#  Output:
#
#    real RESULT, the value of the integral.
#
  result = 0.0

  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_integral_x - Warning!' )
    print ( '  The number of vertices must be at least 3.' )
    print ( '  The input value of N = %d' % ( n ) )
    raise Exception ( 'polygon_integral_x - Fatal error!' )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )

    result = result + ( v[0,i] ** 2 + v[0,i] * v[0,im1] + v[0,im1] ** 2 ) \
      * ( v[1,i] - v[1,im1] )

  result = result / 6.0

  return result

def polygon_integral_x_test ( ):

#*****************************************************************************80
#
## polygon_integral_x_test() tests polygon_integral_x.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  v1 = np.array ( [ \
    [ 0.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0 ] ] )

  n2 = 3
  v2 = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'polygon_integral_x_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_integral_x integrates x over a polygon' )

  r8mat_transpose_print ( 2, n1, v1, '  The polygon vertices:' )

  result = polygon_integral_x ( n1, v1 )
  print ( '' )
  print ( '  x:    %14.6g' % ( result ) )

  r8mat_transpose_print ( 2, n2, v2, '  The polygon vertices:' )

  result = polygon_integral_x ( n2, v2 )
  print ( '' )
  print ( '  x:    %14.6g' % ( result ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_integral_x_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_integral_xx ( n, v ):

#*****************************************************************************80
#
## polygon_integral_xx integrates the function x^2 over a polygon.
#
#  Discussion
#
#    The polygon is bounded by the points (X(1:N), Y(1:N)).
#
#    INTEGRAL = (1/12) * sum ( 1 <= I <= N )
#      ( X(I)^3 + X(I)^2 * X(I-1) + X(I) * X(I-1)^2 + X(I-1)^3 )
#      * ( Y(I) - Y(I-1) )
#
#    where X(0) and Y(0) should be replaced by X(N) and Y(N).
#
#    Note that the integral of 1 over a polygon is the area of the polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    S F Bockman,
#    Generalizing the Formula for Areas of Polygons to Moments,
#    American Mathematical Society Monthly,
#    1989, pages 131-132.
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#    N should be at least 3 for a nonzero result.
#
#    real V(2,N), the coordinates of the vertices
#    of the polygon.  These vertices should be given in counter-clockwise order.
#
#  Output:
#
#    real RESULT, the value of the integral.
#
  result = 0.0

  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_integral_xx - Warning!' )
    print ( '  The number of vertices must be at least 3.' )
    print ( '  The input value of N = %d' % ( n ) )
    raise Exception ( 'polygon_integral_xx - Fatal error!' )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )

    result = result + ( v[0,i] ** 3 + v[0,i] ** 2 * v[0,im1] \
      + v[0,i] * v[0,im1] ** 2 + v[0,im1] ** 3 ) * ( v[1,i] - v[1,im1] )

  result = result / 12.0

  return result

def polygon_integral_xx_test ( ):

#*****************************************************************************80
#
## polygon_integral_xx_test() tests polygon_integral_xx.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  v1 = np.array ( [ \
    [ 0.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0 ] ] )

  n2 = 3
  v2 = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'polygon_integral_xx_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_integral_xx integrates x^2 over a polygon' )

  r8mat_transpose_print ( 2, n1, v1, '  The polygon vertices:' )

  result = polygon_integral_xx ( n1, v1 )
  print ( '' )
  print ( '  x^2:    %14.6g' % ( result ) )

  r8mat_transpose_print ( 2, n2, v2, '  The polygon vertices:' )

  result = polygon_integral_xx ( n2, v2 )
  print ( '' )
  print ( '  x^2:    %14.6g' % ( result ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_integral_xx_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_integral_xy ( n, v ):

#*****************************************************************************80
#
## polygon_integral_xy integrates the function x*y over a polygon.
#
#  Discussion
#
#    The polygon is bounded by the points (X(1:N), Y(1:N)).
#
#    INTEGRAL = (1/24) * sum ( 1 <= I <= N )
#      ( Y(I)   * ( 3 * X(I)^2 + 2 * X(I) * X(I-1) +     X(I-1)^2 )
#      + Y(I-1) * (     X(I)^2 + 2 * X(I) * X(I-1) + 3 * X(I-1)^2 ) )
#      * ( Y(I) - Y(I-1) )
#
#    where X(0) and Y(0) should be replaced by X(N) and Y(N).
#
#    Note that the integral of 1 over a polygon is the area of the polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    S F Bockman,
#    Generalizing the Formula for Areas of Polygons to Moments,
#    American Mathematical Society Monthly,
#    1989, pages 131-132.
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#    N should be at least 3 for a nonzero result.
#
#    real V(2,N), the coordinates of the vertices
#    of the polygon.  These vertices should be given in counter-clockwise order.
#
#  Output:
#
#    real RESULT, the value of the integral.
#
  result = 0.0

  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_integral_xy - Warning!' )
    print ( '  The number of vertices must be at least 3.' )
    print ( '  The input value of N = %d' % ( n ) )
    raise Exception ( 'polygon_integral_xy - Fatal error!' )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )

    result = result + ( \
      v[1,i] * ( 3.0 * v[0,i] ** 2 + 2.0 * v[0,i] * v[0,im1] \
      + v[0,im1] ** 2 ) + v[1,im1] * ( v[0,i] ** 2 + 2.0 * v[0,i] * v[0,im1] \
      + 3.0 * v[0,im1] ** 2 ) ) * ( v[1,i] - v[1,im1] )

  result = result / 24.0

  return result

def polygon_integral_xy_test ( ):

#*****************************************************************************80
#
## polygon_integral_xy_test() tests polygon_integral_xy.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  v1 = np.array ( [ \
    [ 0.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0 ] ] )

  n2 = 3
  v2 = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'polygon_integral_xy_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_integral_xy integrates x*y over a polygon' )

  r8mat_transpose_print ( 2, n1, v1, '  The polygon vertices:' )

  result = polygon_integral_xy ( n1, v1 )
  print ( '' )
  print ( '  x*y:    %14.6g' % ( result ) )

  r8mat_transpose_print ( 2, n2, v2, '  The polygon vertices:' )

  result = polygon_integral_xy ( n2, v2 )
  print ( '' )
  print ( '  x*y:    %14.6g' % ( result ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_integral_xy_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_integral_y ( n, v ):

#*****************************************************************************80
#
## polygon_integral_y integrates the function y over a polygon.
#
#  Discussion
#
#    The polygon is bounded by the points (X(1:N), Y(1:N)).
#
#    INTEGRAL = (1/6) * sum ( 1 <= I <= N )
#      - ( Y(I)^2 + Y(I) * Y(I-1) + Y(I-1)^2 ) * ( X(I) - X(I-1) )
#
#    where X(0) and Y(0) should be replaced by X(N) and Y(N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    S F Bockman,
#    Generalizing the Formula for Areas of Polygons to Moments,
#    American Mathematical Society Monthly,
#    1989, pages 131-132.
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#    N should be at least 3 for a nonzero result.
#
#    real V(2,N), the coordinates of the vertices
#    of the polygon.  These vertices should be given in counter-clockwise order.
#
#  Output:
#
#    real RESULT, the value of the integral.
#
  result = 0.0

  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_integral_y - Warning!' )
    print ( '  The number of vertices must be at least 3.' )
    print ( '  The input value of N = %d' % ( n ) )
    raise Exception ( 'polygon_integral_y - Fatal error!' )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )

    result = result - ( v[1,i] ** 2 + v[1,i] * v[1,im1] + v[1,im1] ** 2 ) \
      * ( v[0,i] - v[0,im1] )

  result = result / 6.0

  return result

def polygon_integral_y_test ( ):

#*****************************************************************************80
#
## polygon_integral_y_test() tests polygon_integral_y.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  v1 = np.array ( [ \
    [ 0.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0 ] ] )

  n2 = 3
  v2 = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'polygon_integral_y_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_integral_y integrates y over a polygon' )

  r8mat_transpose_print ( 2, n1, v1, '  The polygon vertices:' )

  result = polygon_integral_y ( n1, v1 )
  print ( '' )
  print ( '  y:    %14.6g' % ( result ) )

  r8mat_transpose_print ( 2, n2, v2, '  The polygon vertices:' )

  result = polygon_integral_y ( n2, v2 )
  print ( '' )
  print ( '  y:    %14.6g' % ( result ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_integral_y_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_integral_yy ( n, v ):

#*****************************************************************************80
#
## polygon_integral_yy integrates the function Y^2 over a polygon.
#
#  Discussion
#
#    The polygon is bounded by the points (X(1:N), Y(1:N)).
#
#    INTEGRAL = (1/12) * sum ( 1 <= I <= N )
#      - ( Y(I)^3 + Y(I)^2 * Y(I-1) + Y(I) * Y(I-1)^2 + Y(I-1)^3 )
#      * ( X(I) - X(I-1) )
#
#    where X(0) and Y(0) should be replaced by X(N) and Y(N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    S F Bockman,
#    Generalizing the Formula for Areas of Polygons to Moments,
#    American Mathematical Society Monthly,
#    1989, pages 131-132.
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#    N should be at least 3 for a nonzero result.
#
#    real V(2,N), the coordinates of the vertices
#    of the polygon.  These vertices should be given in counter-clockwise order.
#
#  Output:
#
#    real RESULT, the value of the integral.
#
  result = 0.0

  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_integral_yy - Warning!' )
    print ( '  The number of vertices must be at least 3.' )
    print ( '  The input value of N = %d' % ( n ) )
    raise Exception ( 'polygon_integral_yy - Fatal error!' )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )

    result = result - ( v[1,i] ** 3 + v[1,i] ** 2 * v[1,im1] \
      + v[1,i] * v[1,im1] ** 2 + v[1,im1] ** 3 ) * ( v[0,i] - v[0,im1] )

  result = result / 12.0

  return result

def polygon_integral_yy_test ( ):

#*****************************************************************************80
#
## polygon_integral_yy_test() tests polygon_integral_yy.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  v1 = np.array ( [ \
    [ 0.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0 ] ] )

  n2 = 3
  v2 = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'polygon_integral_yy_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_integral_yy integrates y^2 over a polygon' )

  r8mat_transpose_print ( 2, n1, v1, '  The polygon vertices:' )

  result = polygon_integral_yy ( n1, v1 )
  print ( '' )
  print ( '  y^2:    %14.6g' % ( result ) )

  r8mat_transpose_print ( 2, n2, v2, '  The polygon vertices:' )

  result = polygon_integral_yy ( n2, v2 )
  print ( '' )
  print ( '  y^2:    %14.6g' % ( result ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_integral_yy_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_is_convex ( n, v ):

#*****************************************************************************80
#
## polygon_is_convex determines whether a polygon is convex.
#
#  Discussion:
#
#    If the polygon has less than 3 distinct vertices, it is
#    classified as convex degenerate.
#
#    If the polygon "goes around" more than once, it is classified
#    as NOT convex.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Peter Schorn and Frederick Fisher,
#    Testing the Convex ity of a Polygon,
#    Graphics Gems IV, 
#    edited by Paul Heckbert,
#    AP Professsional, 1994.
#
#  Parameters
#
#    integer N, the number of vertices.
#
#    real V(2,N), the coordinates of the vertices of the polygon.  
#
#  Output:
#
#    integer VALUE:
#    -1, the polygon is not convex
#     0, the polygon has less than 3 vertices it is "degenerately" convex
#     1, the polygon is convex and counterclockwise
#     2, the polygon is convex and clockwise.
#
  import numpy as np

  RAD_TO_DEG = 180.0 / np.pi

  CONVEX_CCW = 1
  CONVEX_CW = 2
  DEGENERATE_convex = 0
  NOT_convex = -1
  tol = 1.0

  exterior_total = 0.0
#
#  If there are not at least 3 distinct vertices, we are done.
#
  if ( n < 3 ):
    value = DEGENERATE_convex
    return value

  sense = 0.0
#
#  Consider each polygonal vertex I.
#
  for i in range ( 0, n ):

    ip1 = i4_wrap ( i + 1, 0, n - 1 )
    ip2 = i4_wrap ( i + 2, 0, n - 1 )

    dot =   ( v[0,ip2] - v[0,ip1] ) * ( v[0,i] - v[0,ip1] ) \
          + ( v[1,ip2] - v[1,ip1] ) * ( v[1,i] - v[1,ip1] )

    cross =   ( v[0,ip2] - v[0,ip1] ) * ( v[1,i] - v[1,ip1] ) \
            - ( v[0,i]   - v[0,ip1] ) * ( v[1,ip2] - v[1,ip1] )

    angle = np.arctan2 ( cross, dot )
#
#  See if the turn defined by this vertex is our first indication of
#  the "sense" of the polygon, or if it disagrees with the previously
#  defined sense.
#
    if ( sense == 0.0 ):

      if ( angle < 0.0 ):
        sense = -1.0
      elif ( 0.0 < angle ):
        sense = +1.0

    elif ( sense == 1.0 ):

      if ( angle < 0.0 ):
        value = NOT_convex
        return value

    elif ( sense == -1.0 ):

      if ( 0.0 < angle ):
        value = NOT_convex
        return value
#
#  If the exterior total is greater than 360, then the polygon is
#  going around again.
#
    angle = np.arctan2 ( -cross, -dot )

    exterior_total = exterior_total + angle

    if ( 360.0 + tol < abs ( exterior_total ) * RAD_TO_DEG ):
      value = NOT_convex
      return value

  if ( sense == 1.0 ):
    value = CONVEX_CCW
  elif ( sense == -1.0 ):
    value = CONVEX_CW

  return value

def polygon_is_convex_test ( ):

#*****************************************************************************80
#
## polygon_is_convex_test() tests polygon_is_convex.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_max = 10
  test_num = 11

  print ( '' )
  print ( 'polygon_is_convex_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_is_convex determines if a polygon is convex.' )

  for test in range ( 0, test_num ):

    if ( test == 0 ):
      n = 1
      v = np.array ( [ \
        [ 0.0 ], \
        [ 0.0 ] ] )
      title = '  A point:'
    elif ( test == 1 ):
      n = 2
      v = np.array ( [ \
        [ 0.0, 1.0 ], \
        [ 0.0, 2.0 ] ] )
      title = '  A line:'
    elif ( test == 2 ):
      n = 3
      v = np.array ( [ \
        [ 0.0, 2.0, 1.0 ], \
        [ 0.0, 0.0, 0.0 ] ] )
      title = '  A triangle:'
    elif ( test == 3 ):
      n = 3
      v = np.array ( [ \
        [ 0.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 2.0 ] ] )
      title = '  A CCW triangle:'
    elif ( test == 4 ):
      n = 3
      v = np.array ( [ \
        [ 0.0, 0.0, 1.0 ], \
        [ 0.0, 2.0, 0.0 ] ] )
      title = '  A CW triangle:'
    elif ( test == 5 ):
      n = 4
      v = np.array ( [ \
        [ 1.0, 2.0, 3.0, 0.0 ], \
        [ 0.0, 0.0, 1.0, 1.0 ] ] )
      title = '  Polygon with large angle:'
    elif ( test == 6 ):
      n = 5
      v = np.array ( [ \
        [ 0.0, 0.5, 1.0, 1.0, 0.0 ], \
        [ 0.0, 0.5, 0.0, 1.0, 1.0 ] ] )
      title = '  Polygon with huge angle:'
    elif ( test == 7 ):
      n = 5
      v = np.zeros ( [ 2, n ] )
      for i in range ( 0, n ):
        angle = i * 4.0 * np.pi / float ( n )
        v[0,i] = np.cos ( angle )
        v[1,i] = np.sin ( angle )
      title = '  A five-pointed star:'
    elif ( test == 8 ):
      n = 6
      v = np.zeros ( [ 2, n ] )
      for i in range ( 0, n ):
        angle = i * 2.0 * np.pi / float ( n )
        v[0,i] = np.cos ( angle )
        v[1,i] = np.sin ( angle )
      title = '  A hexagon:'
    elif ( test == 9 ):
      n = 6
      v = np.array ( [ \
        [ 0.0, 2.0, 1.0, 0.0, 2.0, 1.0 ], \
        [ 0.0, 0.0, 1.0, 0.0, 0.0, 1.0 ] ] )
      title = '  A triangle twice:'
    elif ( test == 10 ):
      n = 8
      v = np.array ( [ \
        [ 1.0, 3.0, 3.0, 0.0, 0.0, 2.0, 2.0, 1.0 ], \
        [ 0.0, 0.0, 3.0, 3.0, 1.0, 1.0, 2.0, 1.0 ] ] )
      title = '  Square knot:'

    r8mat_transpose_print ( 2, n, v, title )

    result = polygon_is_convex ( n, v )

    if ( result == -1 ):
      print ( '  The polygon is not convex.' )
    elif ( result == 0 ):
      print ( '  The polygon is degenerate and convex.' )
    elif ( result == 1 ):
      print ( '  The polygon is convex and counterclockwise.' )
    elif ( result == 2 ):
      print ( '  The polygon is convex and clockwise.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_is_convex_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_lattice_area ( i, b ):

#*****************************************************************************80
#
## polygon_lattice_area computes the area of a lattice polygon.
#
#  Discussion:
#
#    We define a lattice to be the 2D plane, in which the points
#    whose (X,Y) coordinates are both integers are given a special
#    status as "lattice points".
#
#    A lattice polygon is a polygon whose vertices are lattice points.
#
#    The area of a lattice polygon can be computed by Pick's Theorem:
#
#      Area = I + B / 2 - 1
#
#    where
#
#      I = the number of lattice points contained strictly inside the polygon;
#
#      B = the number of lattice points that lie exactly on the boundary.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Branko Gruenbaum and G C Shephard,
#    Pick's Theorem,
#    The American Mathematical Monthly,
#    Volume 100, 1993, pages 150-161.
#
#  Input:
#
#    integer I, the number of interior lattice points.
#
#    integer B, the number of boundary lattice points.
#
#  Output:
#
#    real AREA, the area of the lattice polygon.
#
  area = i + b / 2.0 - 1.0

  return area

def polygon_lattice_area_test ( ):

#*****************************************************************************80
#
## polygon_lattice_area_test() tests polygon_lattice_area.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'polygon_lattice_area_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_lattice_area returns the "area"' )
  print ( '  of a polygon, measured in lattice points.' )

  i = 5
  b = 6

  print ( '' )
  print ( '  Number of interior lattice points = %d' % ( i ) )
  print ( '  Number of boundary lattice points = %d' % ( b ) )

  area = polygon_lattice_area ( i, b )

  print ( '  Area of polygon is %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_lattice_area_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_outrad_data ( n, radout ):

#*****************************************************************************80
#
## polygon_outrad_data determines polygonal data from its outer radius.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of sides of the polygon.
#    N must be at least 3.
#
#    real RADOUT, the outer radius of the polygon, that is,
#    the radius of the smallest circle that can be described
#    around the polygon.
#
#  Output:
#
#    real AREA, the area of the regular polygon.
#
#    real RADIN, the inner radius of the polygon, that is,
#    the radius of the largest circle that can be inscribed
#    within the polygon.
#
#    real SIDE, the length of one side of the polygon.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_outrad_data - Fatal error!' )
    print ( '  Input value of N must be at least 3.' )
    print ( '  but your input value was N = %d' % ( n ) )
    raise Exception ( 'polygon_outrad_data - Fatal error!' )

  angle = np.pi / float ( n )
  area = 0.5 * float ( n ) * radout * radout * np.sin ( 2.0 * angle )
  side = 2.0 * radout * np.sin ( angle )
  radin = 0.5 * side / np.tan ( angle )

  return area, radin, side

def polygon_outrad_data_test ( ):

#*****************************************************************************80
#
## polygon_outrad_data_test() tests polygon_outrad_data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'polygon_outrad_data_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_outrad_data uses the outradius of a regular polygon' )
  print ( '  to determine the area, inradius, and sidelength.' )

  for n in range ( 3, 6 ):

    print ( '' )
    print ( '  Number of polygonal sides = %d' % ( n ) )

    radout = 1.0
    print ( '' )
    print ( '  Assuming RADOUT = %g' % ( radout ) )
    area, radin, side = polygon_outrad_data ( n, radout )
    print ( '    AREA =   %g' % ( area ) )
    print ( '    RADIN =  %g' % ( radin ) )
    print ( '    SIDE =   %g' % ( side ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_outrad_data_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_perimeter ( n, v ):

#*****************************************************************************80
#
## polygon_perimeter computes the perimeter of a polygon.
#
#  Discussion:
#
#    The perimeter is simply the sum of the side lengths.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#
#    real V(2,N), the vertices.
#
#  Output:
#
#    real PERIMETER, the perimeter.
#
  import numpy as np

  perimeter = 0.0

  im1 = n - 1

  for i in range ( 0, n ):
    l = np.sqrt ( ( v[0,im1] - v[0,i] ) ** 2 + ( v[1,im1] - v[1,i] ) ** 2 )
    perimeter = perimeter + l
    im1 = i

  return perimeter

def polygon_perimeter_test ( ):

#*****************************************************************************80
#
## polygon_perimeter_test() tests polygon_perimeter.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  n2 = 3
 
  v1 = np.array ( [ \
    [ 0.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0 ] ]  )
  v2 = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'polygon_perimeter_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_perimeter computes the perimeter of a polygon.' )

  r8mat_transpose_print ( 2, n1, v1, '  Vertices of polygon V1:' )

  perimeter = polygon_perimeter ( n1, v1 )
  print ( '' )
  print ( '  Perimeter of V1 = %g' % ( perimeter ) )

  r8mat_transpose_print ( 2, n2, v2, '  Vertices of polygon V2:' )

  perimeter = polygon_perimeter ( n2, v2 )
  print ( '' )
  print ( '  Perimeter of V2 = %g' % ( perimeter ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_perimeter_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_perimeter_quad ( n, v, hmax, f ):

#*****************************************************************************80
#
## polygon_perimeter_quad estimates an integral over the perimeter of a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#
#    real V(2,N), the vertices.
#
#    real HMAX, the maximum length of a quadrature interval.
#
#    def F ( X, Y ), a function whose integral over the perimeter 
#    is desired.
#
#  Output:
#
#    real VALUE, the estimated integral.
#
  import numpy as np
 
  value = 0.0

  for i in range ( 0, n ):

    ip1 = i4_wrap ( i + 1, 0, n - 1 )
    l = np.sqrt ( ( v[0,ip1] - v[0,i] ) ** 2 + ( v[1,ip1] - v[1,i] ) ** 2 )
    m = i4_ceiling ( l / hmax )
    dxy = l / float ( m )

    for j in range ( 1, 2 * m, 2 ):
      x = ( ( 2 * m - j ) * v[0,i] \
          + (         j ) * v[0,ip1] ) \
          / ( 2 * m     )
      y = ( ( 2 * m - j ) * v[1,i] \
          + (         j ) * v[1,ip1] ) \
          / ( 2 * m     )
      fxy = f ( x, y )
      value = value + fxy * dxy

  return value

def polygon_perimeter_quad_test ( ):

#*****************************************************************************80
#
## polygon_perimeter_quad_test() tests polygon_perimeter_quad.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  n2 = 3
 
  v1 = np.array ( [ \
    [ 0.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0 ] ]  )
  v2 = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'polygon_perimeter_quad_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_perimeter_quad estimates the integral of' )
  print ( '  a function over the perimeter of a polygon using' )
  print ( '  the composite midpoint rule over each side.' )

  r8mat_transpose_print ( 2, n1, v1, '  Vertices of polygon V1:' )

  hmax = 0.5
  value = polygon_perimeter_quad ( n1, v1, hmax, f1 )
  print ( '' )
  print ( '  Using HMAX = %g, estimated integral of 1 over perimeter = %g' % ( hmax, value ) )

  print ( '' )
  hmax = 2.0
  for i in range ( 0, 3 ):
    hmax = hmax / 2.0
    value = polygon_perimeter_quad ( n1, v1, hmax, fx2 )
    print ( '  Using HMAX = %g, estimated integral of x^2 over perimeter = %g' % ( hmax, value ) )

  r8mat_transpose_print ( 2, n2, v2, '  Vertices of polygon V2:' )

  hmax = 0.5
  value = polygon_perimeter_quad ( n2, v2, hmax, f1 )
  print ( '' )
  print ( '  Using HMAX = %g, estimated integral of 1 over perimeter = %g' % ( hmax, value ) )

  print ( '' )
  hmax = 2.0
  for i in range ( 0, 3 ):
    hmax = hmax / 2.0
    value = polygon_perimeter_quad ( n2, v2, hmax, fx2 )
    print ( '  Using HMAX = %g, estimated integral of x^2 over perimeter = %g' % ( hmax, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_perimeter_test' )
  print ( '  Normal end of execution.' )
  return

def f1 ( x, y ):

#*****************************************************************************80
#
## f1 evaluates f(x,y) = 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 October 2015
#
#  Author:
#
#    John Burkardt
#
  value = 1.0

  return value

def fx2 ( x, y ):

#*****************************************************************************80
#
## fx2 evaluates f(x,y) = x^2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 October 2015
#
#  Author:
#
#    John Burkardt
#
  value = x ** 2

  return value

def polygon_point_dist ( n, v, p ):

#*****************************************************************************80
#
## polygon_point_dist: distance ( polygon, point ).
#
#  Discussion:
#
#    Thanks to Stefano Zappacosta for pointing out that the arguments
#    passed to segment_point_dist_2D needed to be transposed,
#    27 June 2006.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vertices.
#
#    real V(2,N), the vertices of the polygon.
#
#    real P(2), the point to be checked.
#
#  Output:
#
#    real DIST, the distance from the point to the polygon.
#
  import numpy as np
#
#  Find the distance to each of the line segments.
#
  dist = float ( 'inf' )

  p1 = np.zeros ( 2 )
  p2 = np.zeros ( 2 )

  for j in range ( 0, n ):

    jp1 = i4_wrap ( j + 1, 0, n - 1 )

    p1[0] = v[0,j]
    p1[1] = v[1,j]
    p2[0] = v[0,jp1]
    p2[1] = v[1,jp1]

    dist2 = segment_point_dist ( p1, p2, p )

    if ( dist2 < dist ):
      dist = dist2

  return dist

def polygon_point_dist_test ( ):

#*****************************************************************************80
#
## polygon_point_dist_test() tests polygon_point_dist.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 3
 
  p_test = np.array ( [ \
    [ 4.0, 2.0, -2.0 ], \
    [ 5.0, 3.0, -1.0 ] ] )

  v = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'polygon_point_dist_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_point_dist computes polygon-point distance.' )

  r8mat_transpose_print ( 2, n, v, '  Vertices of polygon:' )

  print ( '' )
  print ( '       X             Y             DIST' )
  print ( '' )

  p = np.zeros ( 2 )

  for test in range ( 0, 3 ):

    p[0] = p_test[0,test]
    p[1] = p_test[1,test]
    dist = polygon_point_dist ( n, v, p )
    print ( '  %14.6g  %14.6g  %14.6g' % ( p[0], p[1], dist ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_point_dist_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_point_near ( n, v, p ):

#*****************************************************************************80
#
## polygon_point_near computes the nearest point on a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real V(2,N), the polygon vertices.
#
#    real P(2), the point whose nearest polygon point
#    is to be determined.
#
#  Output:
#
#    real PN(2), the nearest point to P.
#
#    real DIST, the distance from the point to the polygon.
#
  import numpy as np
#
#  Find the distance to each of the line segments that make up the edges
#  of the polygon.
#
  dist = float ( 'inf' )

  pn = np.zeros ( 2 )
  p1 = np.zeros ( 2 )
  p2 = np.zeros ( 2 )

  for j in range ( 0, n ):

    jp1 = i4_wrap ( j + 1, 0, n - 1 )

    p1[0] = v[0,j]
    p1[1] = v[1,j]
    p2[0] = v[0,jp1]
    p2[1] = v[1,jp1]

    pn2, dist2, tval = segment_point_near ( p1, p2, p )

    if ( dist2 < dist ):
      dist = dist2
      pn[0] = pn2[0]
      pn[1] = pn2[1]

  return pn, dist

def polygon_point_near_test ( ):

#*****************************************************************************80
#
## polygon_point_near_test() tests polygon_point_near.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 3
 
  p_test = np.array ( [ \
    [ 4.0, 2.0, -2.0 ], \
    [ 5.0, 3.0, -1.0 ] ] )

  v = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'polygon_point_near_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_point_near computes nearest point on polygon.' )

  r8mat_transpose_print ( 2, n, v, '  Vertices of polygon:' )

  print ( '' )
  print ( '       X             Y             XN             YN' )
  print ( '' )

  p = np.zeros ( 2 )

  for test in range ( 0, 3 ):

    p[0] = p_test[0,test]
    p[1] = p_test[1,test]
    pn, dist = polygon_point_near ( n, v, p )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( p[0], p[1], pn[0], pn[1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_point_near_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_properties_test ( ):

#*****************************************************************************80
#
## polygon_properties_test() tests polygon_properties().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'polygon_properties_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test polygon_properties().' )

  polygon_angles_test ( )
  polygon_area_test ( )
  polygon_area_2_test ( )
  polygon_centroid_test ( )
  polygon_centroid_2_test ( )
  polygon_contains_point_test ( )
  polygon_contains_point_2_test ( )
  polygon_diameter_test ( )
  polygon_expand_test ( )
  polygon_inrad_data_test ( )
  polygon_integral_1_test ( )
  polygon_integral_x_test ( )
  polygon_integral_xx_test ( )
  polygon_integral_xy_test ( )
  polygon_integral_y_test ( )
  polygon_integral_yy_test ( )
  polygon_is_convex_test ( )
  polygon_lattice_area_test ( )
  polygon_outrad_data_test ( )
  polygon_perimeter_test ( )
  polygon_perimeter_quad_test ( )
  polygon_point_dist_test ( )
  polygon_point_near_test ( )
  polygon_sample_test ( )
  polygon_side_data_test ( )
  polygon_triangulate_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_properties_test:' )
  print ( '  Normal end of execution.' )
  return

def polygon_sample ( nv, v, n ):

#*****************************************************************************80
#
## polygon_sample uniformly samples a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NV, the number of vertices.
#
#    real V(2,NV), the vertices of the polygon, listed in
#    counterclockwise order.
#
#    integer N, the number of points to create.
#
#  Output:
#
#    real S(2,N), the points.
#
  import numpy as np
#
#  Triangulate the polygon.
#
  x = np.zeros ( nv )
  y = np.zeros ( nv )
  for j in range ( 0, nv ):
    x[j] = v[0,j]
    y[j] = v[1,j]

  triangles = polygon_triangulate ( nv, x, y )
#
#  Determine the areas of each triangle.
#
  area_triangle = np.zeros ( nv - 2 )

  area_polygon = 0.0
  for i in range ( 0, nv - 2 ):
    area_triangle[i] = triangle_area ( \
      v[0,triangles[i,0]], v[1,triangles[i,0]], \
      v[0,triangles[i,1]], v[1,triangles[i,1]], \
      v[0,triangles[i,2]], v[1,triangles[i,2]] )
    area_polygon = area_polygon + area_triangle[i]
#
#  Normalize the areas.
#
  area_relative = np.zeros ( nv - 1 )

  for i in range ( 0, nv - 2 ):
    area_relative[i] = area_triangle[i] / area_polygon
#
#  Replace each area by the sum of itself and all previous ones.
#
  area_cumulative = np.zeros ( nv - 2 )

  area_cumulative[0] = area_relative[0]
  for i in range ( 1, nv - 2 ):
    area_cumulative[i] = area_relative[i] + area_cumulative[i-1]

  s = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
#
#  Choose triangle I at random, based on areas.
#
    area_percent = np.random.rand ( )

    for k in range ( 0, nv - 2 ):

      i = k

      if ( area_percent <= area_cumulative[k] ):
        break
#
#  Now choose a point at random in triangle I.
#
    r = np.random.rand ( 2 )

    if ( 1.0 < r[0] + r[1] ):
      r[0] = 1.0 - r[0]
      r[1] = 1.0 - r[1]

    s[0,j] = ( 1.0 - r[0] - r[1] ) * v[0,triangles[i,0]] \
                   + r[0]          * v[0,triangles[i,1]] \
                          + r[1]   * v[0,triangles[i,2]]

    s[1,j] = ( 1.0 - r[0] - r[1] ) * v[1,triangles[i,0]] \
                   + r[0]          * v[1,triangles[i,1]] \
                          + r[1]   * v[1,triangles[i,2]]

  return s

def polygon_sample_test ( ):

#*****************************************************************************80
#
## polygon_sample_test() tests polygon_sample.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 20
  nv = 6
  v = np.array ( [ \
    [ 0.0, 2.0, 2.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0, 2.0, 1.0 ] ] )

  print ( '' )
  print ( 'polygon_sample_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_sample samples a polygon.' )

  x = polygon_sample ( nv, v, n )

  r8mat_transpose_print ( 2, n, x, '  Sample points:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_sample_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_side_data ( n, side ):

#*****************************************************************************80
#
## polygon_side_data determines polygonal data from its side length.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of sides of the polygon.
#    N must be at least 3.
#
#    real SIDE, the length of one side of the polygon.
#
#  Output:
#
#    real AREA, the area of the regular polygon.
#
#    real RADIN, the inner radius of the polygon, that is,
#    the radius of the largest circle that can be inscribed within
#    the polygon.
#
#    real RADOUT, the outer radius of the polygon, that is,
#    the radius of the smallest circle that can be described about
#    the polygon.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_side_data - Fatal error!' )
    print ( '  Input value of N must be at least 3.' )
    print ( '  but your input value was N = %d' % ( n ) )
    raise Exception ( 'polygon_side_data - Fatal error!' )

  angle = np.pi / n
  area = 0.5 * n * side * side / np.tan ( angle )
  radin = 0.5 * side / np.tan ( angle )
  radout = 0.5 * side / np.sin ( angle )

  return area, radin, radout

def polygon_side_data_test ( ):

#*****************************************************************************80
#
## polygon_side_data_test() tests polygon_side_data;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'polygon_side_data_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_side_data uses the side length of a regular polygon' )
  print ( '  to compute the area, inradius, and outradius.' )

  for n in range ( 3, 6 ):

    print ( '' )
    print ( '  Number of polygonal sides = %d' % ( n ) )

    side = 1.0
    print ( '' )
    print ( '  Assuming SIDE = %g' % ( side ) )
    area, radin, radout = polygon_side_data ( n, side )
    print ( '    AREA =   %g' % ( area ) )
    print ( '    RADIN =  %g' % ( radin ) )
    print ( '    RADOUT = %g' % ( radout ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_side_data_test' )
  print ( '  Normal end of execution.' )
  return

def polygon_triangulate ( n, x, y ):

#*****************************************************************************80
#
## polygon_triangulate determines a triangulation of a polygon.
#
#  Discussion:
#
#    There are N-3 triangles in the triangulation.
#
#    For the first N-2 triangles, the first edge listed is always an
#    internal diagonal.
#
#    Thanks to Gene Dial for pointing out a mistake in the area calculation,
#    10 September 2016.
#
#    Thanks to Gene Dial for suggesting that the next() array should be
#    renamed next_node() to avoid the Python keyword next, 22 September 2016.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    2 September 2016
#
#  Author:
#
#    Original C version by Joseph ORourke.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Joseph ORourke,
#    Computational Geometry in C,
#    Cambridge, 1998,
#    ISBN: 0521649765,
#    LC: QA448.D38.
#
#  Input:
#
#    int N, the number of vertices.
#
#    real X[N], Y[N], the coordinates of each vertex.
#
#  Output:
#
#    int TRIANGLES[N-2,3], the triangles.
#
  import numpy as np
#
#  We must have at least 3 vertices.
#
  if ( n < 3 ):
    print ( '' )
    print ( 'polygon_triangulate - Fatal error!' )
    print ( '  N < 3' )
    raise Exception ( 'polygon_triangulate - Fatal error!' )
#
#  Consecutive vertices cannot be equal.
#
  node_m1 = n - 1
  for node in range ( 0, n ):
    if ( x[node_m1] == x[node] and y[node_m1] == y[node] ):
      print ( '' )
      print ( 'polygon_triangulate - Fatal error!' )
      print ( '  Two consecutive nodes are identical.' )
      raise Exception ( 'polygon_triangulate - Fatal error!' )

    node_m1 = node
#
#  No node can be the vertex of an angle less than 1 degree 
#  in absolute value.
#
  node1 = n - 1

  for node2 in range ( 0, n ):

    node3 = ( ( node2 + 1 ) % n )

    angle = angle_degree ( \
      x[node1], y[node1], \
      x[node2], y[node2], \
      x[node3], y[node3] )

    if ( abs ( angle ) <= 1.0 ):
      print ( '' )
      print ( 'polygon_triangulate - Fatal error!' )
      print ( '  Polygon has an angle %g smaller than 1 degree.' % ( angle ) )
      print ( '  occurring at node %d' % ( node2 ) )
      return None

    node1 = node2
#
#  Area must be positive.
#
  area = polygon_area_3 ( n, x, y )

  if ( area <= 0.0 ):
    print ( '' )
    print ( 'polygon_triangulate - Fatal error!' )
    print ( '  Polygon has zero or negative area.' )
    raise Exception ( 'polygon_triangulate - Fatal error!' )

  triangles = np.zeros ( [ n - 2,  3 ], dtype = np.int32 )
#
#  PREV_NODE and NEXT_NODE point to the previous and next nodes.
#
  prev_node = np.zeros ( n, dtype = np.int32 )
  next_node = np.zeros ( n, dtype = np.int32 )

  i = 0
  prev_node[i] = n - 1
  next_node[i] = i + 1

  for i in range ( 1, n - 1 ):
    prev_node[i] = i - 1
    next_node[i] = i + 1

  i = n - 1
  prev_node[i] = i - 1
  next_node[i] = 0
#
#  EAR indicates whether the node and its immediate neighbors form an ear
#  that can be sliced off immediately.
#
  ear = np.zeros ( n, dtype = np.bool )
  for i in range ( 0, n ):
    ear[i] = diagonal ( prev_node[i], next_node[i], n, prev_node, \
      next_node, x, y )

  triangle_num = 0

  i2 = 0

  while ( triangle_num < n - 3 ):
#
#  If I2 is an ear, gather information necessary to carry out
#  the slicing operation and subsequent "healing".
#
    if ( ear[i2] ):
      i3 = next_node[i2]
      i4 = next_node[i3]
      i1 = prev_node[i2]
      i0 = prev_node[i1]
#
#  Make vertex I2 disappear.
#
      next_node[i1] = i3
      prev_node[i3] = i1
#
#  Update the earity of I1 and I3, because I2 disappeared.
#
      ear[i1] = diagonal ( i0, i3, n, prev_node, next_node, x, y )
      ear[i3] = diagonal ( i1, i4, n, prev_node, next_node, x, y )
#
#  Add the diagonal [I3, I1, I2] to the list.
#
      triangles[triangle_num,0] = i3
      triangles[triangle_num,1] = i1
      triangles[triangle_num,2] = i2
      triangle_num = triangle_num + 1
#
#  Try the next vertex.
#
    i2 = next_node[i2]
#
#  The last triangle is formed from the three remaining vertices.
#
  i3 = next_node[i2]
  i1 = prev_node[i2]

  triangles[triangle_num,0] = i3
  triangles[triangle_num,1] = i1
  triangles[triangle_num,2] = i2
  triangle_num = triangle_num + 1

  return triangles

def polygon_triangulate_test ( ):

#*****************************************************************************80
#
## polygon_triangulate_test() tests the "comb_10" polygon.
#
#  Discussion:
#
#    There are N-3 triangles in the triangulation.
#
#    For the first N-2 triangles, the first edge listed is always an
#    internal diagonal.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 October 2015
#
  import numpy as np
  import platform

  n = 10
  x = np.array ( [ 8.0,  7.0,  6.0,  5.0,  4.0,  3.0,  2.0,  1.0,  0.0,  4.0 ] )
  y = np.array ( [ 0.0, 10.0,  0.0, 10.0,  0.0, 10.0,  0.0, 10.0,  0.0, -2.0 ] )

  print ( '' )
  print ( 'polygon_triangulate_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Triangulate the comb_10 polygon.' )

  triangles = polygon_triangulate ( n, x, y )

  i4mat_print ( n - 2, 3, triangles, '  Triangles' )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_triangulate_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_solve ( n, nrhs, a ):

#*****************************************************************************80
#
## r8mat_solve uses Gauss-Jordan elimination to solve an N by N linear system.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NRHS, the number of right hand sides.  NRHS
#    must be at least 0.
#
#    real A(N,N+NRHS), contains in rows and
#    columns 1 to N the coefficient matrix, and in columns N+1 through
#    N+NRHS, the right hand sides.
#
#  Output:
#
#    real A(N,N+NRHS), the coefficient matrix
#    area has been destroyed, while the right hand sides have
#    been overwritten with the corresponding solutions.
#
#    integer INFO, singularity flag.
#    0, the matrix was not singular, the solutions were computed;
#    J, factorization failed on step J, and the solutions could not
#    be computed.
#
  info = 0

  for j in range ( 0, n ):
#
#  Choose a pivot row IPIVOT.
#
    ipivot = j
    apivot = a[j,j]

    for i in range ( j + 1, n ):
      if ( abs ( apivot ) < abs ( a[i,j] ) ):
        apivot = a[i,j]
        ipivot = i

    if ( apivot == 0.0 ):
      info = j
      return a, info
#
#  Interchange.
#
    for k in range ( 0, n + nrhs ):
      temp        = a[ipivot,k]
      a[ipivot,k] = a[j,k]
      a[j,k]      = temp
#
#  A(J,J) becomes 1.
#
    a[j,j] = 1.0
    for k in range ( j + 1, n + nrhs ):
      a[j,k] = a[j,k] / apivot;
#
#  A(I,J) becomes 0.
#
    for i in range ( 0, n ):

      if ( i != j ):

        factor = a[i,j]
        a[i,j] = 0.0
        for k in range ( j + 1, n + nrhs ):
          a[i,k] = a[i,k] - factor * a[j,k]

  return a, info

def r8mat_solve_test ( ):

#*****************************************************************************80
#
## r8mat_solve_test() tests r8mat_solve.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 3
  rhs_num = 2
#
#  Each row of this definition is a COLUMN of the matrix.
#
  a = np.array ( [ \
    [ 1.0, 2.0, 3.0, 14.0,  7.0 ], \
    [ 4.0, 5.0, 6.0, 32.0, 16.0 ], \
    [ 7.0, 8.0, 0.0, 23.0,  7.0 ] ] )

  print ( '' )
  print ( 'r8mat_solve_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_solve solves linear systems.' )
#
#  Print out the matrix to be inverted.
#
  r8mat_print ( n, n + rhs_num, a, '  The linear system:' )
#
#  Solve the systems.
#
  a, info = r8mat_solve ( n, rhs_num, a )
 
  if ( info != 0 ):
    print ( '' )
    print ( '  The input matrix was singular.' )
    print ( '  The solutions could not be computed.' )
    return

  r8mat_print ( n, n + rhs_num, a, '  Factored matrix and solutions:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_solve_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_transpose_print prints an R8MAT, transposed.
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
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_test() tests r8mat_transpose_print.
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
  print ( 'r8mat_transpose_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_transpose_print prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_transpose_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_transpose_print_some prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
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

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_some_test() tests r8mat_transpose_print_some.
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
  print ( 'r8mat_transpose_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_transpose_print_some prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_transpose_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print prints an R8VEC.
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
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## r8vec_print_test() tests r8vec_print.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_print prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_print_test:' )
  print ( '  Normal end of execution.' )
  return

def segment_point_dist ( p1, p2, p ):

#*****************************************************************************80
#
## segment_point_dist: distance ( line segment, point ).
#
#  Discussion:
#
#    A line segment is the finite portion of a line that lies between
#    two points.
#
#    The nearest point will satisfy the condition
#
#      PN = (1-T) * P1 + T * P2.
#
#    T will always be between 0 and 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P1(2), P2(2), the endpoints of the line segment.
#
#    real P(2), the point whose nearest neighbor on the line
#    segment is to be determined.
#
#  Output:
#
#    real DIST, the distance from the point to the line segment.
#
  import numpy as np
#
#  If the line segment is actually a point, then the answer is easy.
#
  if ( p1[0] == p2[0] and p1[1] == p2[1] ):

    t = 0.0

  else:

    bot = ( p2[0] - p1[0] ) ** 2 + ( p2[1] - p1[1] ) ** 2

    t = ( ( p[0] - p1[0] ) * ( p2[0] - p1[0] ) \
        + ( p[1] - p1[1] ) * ( p2[1] - p1[1] ) ) / bot

    t = max ( t, 0.0 )
    t = min ( t, 1.0 )

  pn = np.zeros ( 2 )

  pn[0] = p1[0] + t * ( p2[0] - p1[0] )
  pn[1] = p1[1] + t * ( p2[1] - p1[1] )

  dist = np.sqrt ( ( pn[0] - p[0] ) ** 2 + ( pn[1] - p[1] ) ** 2 )

  return dist

def segment_point_near ( p1, p2, p ):

#*****************************************************************************80
#
## segment_point_near finds the line segment point nearest a point.
#
#  Discussion:
#
#    A line segment is the finite portion of a line that lies between
#    two points.
#
#    The nearest point will satisfy the condition
#
#      PN = (1-T) * P1 + T * P2.
#
#    T will always be between 0 and 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P1(2,1), P2(2,1), the endpoints of the line segment.
#
#    real P(2,1), the point whose nearest neighbor
#    on the line segment is to be determined.
#
#  Output:
#
#    real PN(2,1), the point on the line segment which is
#    nearest the point (X,Y).
#
#    real DIST, the distance from the point to the
#    nearest point on the line segment.
#
#    real T, the relative position of the point (XN,YN)
#    to the points (X1,Y1) and (X2,Y2).
#
  import numpy as np
#
#  If the line segment is actually a point, then the answer is easy.
#
  if ( p1[0] == p2[0] and p1[1] == p2[1] ):

    t = 0.0

  else:

    bot = ( p2[0] - p1[0] ) ** 2 + ( p2[1] - p1[1] ) ** 2

    t = ( ( p[0] - p1[0] ) * ( p2[0] - p1[0] ) \
        + ( p[1] - p1[1] ) * ( p2[1] - p1[1] ) ) / bot

    t = max ( t, 0.0 )
    t = min ( t, 1.0 )

  pn = np.zeros ( 2 )

  pn[0] = p1[0] + t * ( p2[0] - p1[0] )
  pn[1] = p1[1] + t * ( p2[1] - p1[1] )

  dist = np.sqrt ( ( pn[0] - p[0] ) ** 2 + ( pn[1] - p[1] ) ** 2 )

  return pn, dist, t

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

def triangle_area ( xa, ya, xb, yb, xc, yc ):

#*****************************************************************************80
#
## triangle_area() computes the signed area of a triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, the coordinates of
#    the vertices of the triangle, given in counterclockwise order.
#
#  Output:
#
#    real VALUE, the signed area of the triangle.
#
  value = 0.5 * ( ( xb - xa ) * ( yc - ya ) - ( xc - xa ) * ( yb - ya ) )

  return value

def triangle_barycentric ( t, p ):

#*****************************************************************************80
#
## triangle_barycentric() finds the barycentric coordinates of a point.
#
#  Discussion:
#
#    The barycentric coordinate of point X related to vertex A can be
#    interpreted as the ratio of the area of the triangle with
#    vertex A replaced by vertex X to the area of the original
#    triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#    The vertices should be given in counter clockwise order.
#
#    real P(2), the point to be checked.
#
#  Output:
#
#    real XSI(3), the barycentric coordinates of (X,Y)
#    with respect to the triangle.
#
  import numpy as np

  nrhs = 1
#
#  Set up the linear system
#
#    ( X2-X1  X3-X1 ) XSI(1)  = X-X1
#    ( Y2-Y1  Y3-Y1 ) XSI(2)    Y-Y1
#
#  which is satisfied by the barycentric coordinates of (X,Y).
#
  a = np.zeros ( [ 2, 3 ] )

  a[0,0] = t[0,1] - t[0,0]
  a[0,1] = t[0,2] - t[0,0]
  a[0,2] = p[0]   - t[0,0]

  a[1,0] = t[1,1] - t[1,0]
  a[1,1] = t[1,2] - t[1,0]
  a[1,2] = p[1]   - t[1,0]
#
#  Solve the linear system.
#
  a, info = r8mat_solve ( 2, nrhs, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'triangle_barycentric - Fatal error!' )
    print ( '  The linear system is singular.' )
    print ( '  The input data does not form a proper triangle.' )
    raise Exception ( 'triangle_barycentric - Fatal error!' )

  xsi = np.zeros ( 3 )

  xsi[0] = a[0,2]
  xsi[1] = a[1,2]
  xsi[2] = 1.0 - xsi[0] - xsi[1]

  return xsi

def triangle_contains_point_1 ( t, p ):

#*****************************************************************************80
#
## triangle_contains_point_1() finds if a point is inside a triangle.
#
#  Discussion:
#
#    It is conventional to list the triangle vertices in counter clockwise
#    order.  However, this routine does not require a particular order
#    for the vertices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#    real P(2,1), the point to be checked.
#
#  Output:
#
#    bool INSIDE, is TRUE if the point is inside
#    the triangle or on its boundary.
#
  xsi = triangle_barycentric ( t, p )

  if ( xsi[0] < 0.0 or xsi[1] < 0.0 or xsi[2] < 0.0 ):
    inside = False
  else:
    inside = True

  return inside

if ( __name__ == '__main__' ):
  timestamp ( )
  polygon_properties_test ( )
  timestamp ( )

