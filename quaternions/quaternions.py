#! /usr/bin/env python3
#
def degrees_to_radians ( degrees ):

#*****************************************************************************80
#
## degrees_to_radians() converts an angle from degrees to radians.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real degrees, an angle in degrees.
#
#  Output:
#
#    real VALUE, the equivalent angle in radians.
#
  import numpy as np

  value = ( degrees / 180.0 ) * np.pi

  return value

def degrees_to_radians_test ( ):

#*****************************************************************************80
#
## degrees_to_radians_test() tests degrees_to_radians.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'degrees_to_radians_test' )
  print ( '  degrees_to_radians converts an angle from degrees' )
  print ( '  to radians;' )
  print ( '' )
  print ( '  degrees     radians     degrees' )
  print ( '' )

  for i in range ( -2, 15 ):
    angle_deg = float ( 30 * i )
    angle_rad = degrees_to_radians ( angle_deg )
    angle_deg2 = radians_to_degrees ( angle_rad )
    print ( '  %10f  %10f  %10f' % ( angle_deg, angle_rad, angle_deg2 ) )

  return

def q8_conjugate ( q ):

#*****************************************************************************80
#
## q8_conjugate() conjugates a quaternion.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#
#    The conjugate of Q is
#
#      conj ( Q ) = A - Bi - Cj - Dk.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q(4), the quaternion to be conjugated.
#
#  Output:
#
#    real Q2(4), the conjugated quaternion.
#
  import numpy as np

  q2 = np.zeros ( 4 )

  q2[0]   =   q[0]
  q2[1:4] = - q[1:4]

  return q2

def q8_conjugate_test ( ):

#*****************************************************************************80
#
## q8_conjugate_test() tests q8_conjugate().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 July 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'q8_conjugate_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  q8_conjugate conjugates a quaternion' )

  for i in range ( 0, 5 ):

    q1 = q8_normal_01 ( )
    q2 = q8_conjugate ( q1 )

    print ( '' )
    q8_transpose_print ( q1, '  q1 = q8_normal_01 ():' )
    q8_transpose_print ( q2, '  q2 = q8_conjugate ( q1 ):  ' )  
#
#  Terminate.
#
  print ( '' )
  print ( 'q8_conjugate_test' )
  print ( '  Normal end of execution.' )
  return

def q8_exponentiate ( q1 ):

#*****************************************************************************80
#
## q8_exponentiate() exponentiates a quaternion.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#    
#    The exponential of Q can be set by
#      V = sqrt ( B^2 + C^2 + D^2 )
#      e^Q = e^A * ( cos ( ||V|| ) + V/||V|| sin ||V|| )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q1(4), the quaternions to exponentiate.
#
#  Output:
#
#    real Q2(4), the exponential of the quaternion.
#
  import numpy as np

  vnorm = np.sqrt ( np.sum ( q1[1:4] ** 2 ) )

  q2 = np.zeros ( 4 )

  q2[0] = np.cos ( vnorm )
  if ( vnorm != 0.0 ):
    q2[1:4] = np.sin ( vnorm ) * q1[1:4] / vnorm

  q2[0:4] = np.exp ( q1[0] ) * q2[0:4]

  return q2

def q8_exponentiate_test ( ):

#*****************************************************************************80
#
## q8_exponentiate_test() tests q8_exponentiate().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'q8_exponentiate_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  q8_exponentiate exponentiates a quaternion' )

  for i in range ( 0, 5 ):

    q1 = q8_normal_01 ( )
    q2 = q8_exponentiate ( q1 )

    print ( '' )
    q8_transpose_print ( q1, '  q1 = q8_normal_01 ( ):' )
    q8_transpose_print ( q2, '  q2 = q8_exponentiate ( q1 ):' )  
#
#  Terminate.
#
  print ( '' )
  print ( 'q8_exponentiate_test' )
  print ( '  Normal end of execution.' )
  return

def q8_inverse ( q ):

#*****************************************************************************80
#
## q8_inverse() returns the inverse of a quaternion.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#
#    The inverse of Q is
#
#      inverse ( Q ) = conjugate ( Q ) / ( norm ( Q ) )^2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q(4), the quaternion to be inverted.
#
#  Output:
#
#    real Q2(4), the inverse of the input quaternion.
#
  import numpy as np

  q2 = q.copy ( );
  q_norm_sq = np.sum ( q[0:4] ** 2 )
  q2[0:4] = q2[0:4] / q_norm_sq
  q2[1:4] = - q2[1:4]

  return q2

def q8_inverse_test ( ):

#*****************************************************************************80
#
## q8_inverse_test() tests q8_inverse().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'q8_inverse_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  q8_inverse inverts a quaternion' )

  for i in range ( 0, 5 ):

    q1 = q8_normal_01 ( )
    q2 = q8_inverse ( q1 )
    q3 = q8_multiply ( q1, q2 )

    print ( '' )
    q8_transpose_print ( q1, '  q1 = q8_normal_01 ( ):' )
    q8_transpose_print ( q2, '  q2 = q8_inverse ( q1 ):    ' ) 
    q8_transpose_print ( q3, '  q3 = q8_multiply ( q1, q2 ):    ' )
     
#
#  Terminate.
#
  print ( '' )
  print ( 'q8_inverse_test' )
  print ( '  Normal end of execution.' )
  return

def q8_multiply2 ( q1, q2 ):

#*****************************************************************************80
#
## q8_multiply2() multiplies two quaternions using a matrix format.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#
#    To multiply two quaternions, use the relationships:
#
#      i * j = -j * i = k
#      j * k = -k * j = i
#      k * i = -i * k = j
#      i * i =  j * j = k * k = -1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q1[3], Q2[3], the two quaternions to be multiplied.
#
#  Output:
#
#    real Q3[3], the product of the two quaternions.
#
  import numpy as np

  qm = np.array ( [ \
    [ q1[0], -q1[1], -q1[2], -q1[3] ], \
    [ q1[1], +q1[0], -q1[3], +q1[2] ], \
    [ q1[2], +q1[3], +q1[0], -q1[1] ], \
    [ q1[3], -q1[2], +q1[1], +q1[0] ] ] )

  q3 = np.dot ( qm, q2 )
  
  return q3

def q8_multiply2_test ( ):

#*****************************************************************************80
#
## q8_multiply2_test() tests q8_multiply2().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 July 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'q8_multiply2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  q8_multiply2 multiplies two quaternions using a matrix' )

  for i in range ( 0, 5 ):

    q1 = q8_normal_01 ( )
    q2 = q8_normal_01 ( )
    q3 = q8_multiply2 ( q1, q2 )

    print ( '' )
    q8_transpose_print ( q1, '  q1 = q8_normal_01 ( )  :' )
    q8_transpose_print ( q2, '  q2 = q8_normal_01 ( )  :' )
    q8_transpose_print ( q3, '  q3 = q8_multiply2 ( q1, q2 ):' )  
#
#  Terminate.
#
  print ( '' )
  print ( 'q8_multiply2_test' )
  print ( '  Normal end of execution.' )
  return

def q8_multiply ( q1, q2 ):

#*****************************************************************************80
#
## q8_multiply() multiplies two quaternions.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#
#    To multiply two quaternions, use the relationships:
#
#      i * j = -j * i = k
#      j * k = -k * j = i
#      k * i = -i * k = j
#      i * i =  j * j = k * k = -1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q1[3], Q2[3], the two quaternions to be multiplied.
#
#  Output:
#
#    real Q3[3], the product of the two quaternions.
#
  import numpy as np

  q3 = np.zeros ( 4 )

  q3[0] = q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3]
  q3[1] = q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2]
  q3[2] = q1[0] * q2[2] - q1[1] * q2[3] + q1[2] * q2[0] + q1[3] * q2[1]
  q3[3] = q1[0] * q2[3] + q1[1] * q2[2] - q1[2] * q2[1] + q1[3] * q2[0]

  return q3

def q8_multiply_test ( ):

#*****************************************************************************80
#
## q8_multiply_test() tests q8_multiply().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 July 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'q8_multiply_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  q8_multiply multiplies two quaternions' )

  for i in range ( 0, 5 ):

    q1 = q8_normal_01 ( )
    q2 = q8_normal_01 ( )
    q3 = q8_multiply ( q1, q2 )

    print ( '' )
    q8_transpose_print ( q1, '  q1 = q8_normal_01 ( ) :' )
    q8_transpose_print ( q2, '  q2 = q8_normal_01 ( ) :' )
    q8_transpose_print ( q3, '  q3 = q8_multiply ( q1, q2 ):' )  
#
#  Terminate.
#
  print ( '' )
  print ( 'q8_multiply_test' )
  print ( '  Normal end of execution.' )
  return

def q8_normal_01 ( ):

#*****************************************************************************80
#
## q8_normal_01() returns a normally distributed quaternion.
#
#  Discussion:
#
#    The normal distribution with mean 0 and variance 1 is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real Q(4), the sampled quaternion.
#
  import numpy as np

  q = np.zeros ( 4 )

  r = np.random.rand ( 4 )

  q[0:3:2] = \
    np.sqrt ( -2.0 * np.log ( r[0:3:2] ) ) * np.cos ( 2.0 * np.pi * r[1:4:2] )

  q[1:4:2] = \
    np.sqrt ( -2.0 * np.log ( r[0:3:2] ) ) * np.sin ( 2.0 * np.pi * r[1:4:2] )

  return q

def q8_normal_01_test ( ):

#*****************************************************************************80
#
## q8_normal_01_test() tests q8_normal_01().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'q8_normal_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  q8_normal_01 computes a normally distributed quaternion.' )
  print ( '' )

  for i in range ( 0, 5 ):
    q = q8_normal_01 ( )
    label = ( '  Sample # %d' % ( i ) )
    q8_transpose_print ( q, label )
#
#  Terminate.
#
  print ( '' )
  print ( 'q8_normal_01_test' )
  print ( '  Normal end of execution.' )
  return

def q8_norm ( q ):

#*****************************************************************************80
#
## q8_norm() computes the norm of a quaternion.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#
#    The norm of Q is
#
#      norm(Q) = sqrt ( A^2 + B^2 + C^2 + D^2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q(4), the quaternion.
#
#  Output:
#
#    real VALUE, the norm of the quaternion.
#
  import numpy as np

  value = np.sqrt ( np.sum ( q[0:4] ** 2 ) )

  return value

def q8_norm_test ( ):

#*****************************************************************************80
#
## q8_norm_test() tests q8_norm().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'q8_norm_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  q8_norm computes the norm of a quaternion.' )

  for i in range ( 0, 5 ):
    print ( '' )
    q = q8_normal_01 ( )
    label = '  q = q8_normal_01():'
    q8_transpose_print ( q, label )
    value = q8_norm ( q )
    print ( '  q8_norm(q) = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'q8_norm_test' )
  print ( '  Normal end of execution.' )
  return

def q8_transpose_print ( q, title ):

#*****************************************************************************80
#
## q8_transpose_print() prints a Q8 "transposed".
#
#  Discussion:
#
#    A Q8 is a quaternion using R8 arithmetic.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q(4), the quaternion to be printed.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( title, end = '' )

  print ( '%12g  %12g  %12g  %12g' % ( q[0], q[1], q[2], q[3] ) )
 
  return

def q8_transpose_print_test ( ):

#*****************************************************************************80
#
## q8_transpose_print_test() tests q8_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'q8_transpose_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  q8_transpose_print prints a quaternion "transposed",' )
  print ( '  that is, writing it as a row vector.' )
  print ( '' )

  q = q8_normal_01 ( )
  q8_transpose_print ( q, '  The quaternion:' )

  print ( '' )
  print ( '  Now print without a label:' )
  print ( '' )

  q8_transpose_print ( q, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'q8_transpose_print_test' )
  print ( '  Normal end of execution.' )
  return

def quaternions_test ( ):

#*****************************************************************************80
#
## quaternions_test() tests quaternions().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'quaternions_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the quaternions library.' )

  degrees_to_radians_test ( )

  q8_conjugate_test ( )
  q8_exponentiate_test ( )
  q8_inverse_test ( )
  q8_multiply_test ( )
  q8_multiply2_test ( )
  q8_norm_test ( )
  q8_normal_01_test ( )
  q8_transpose_print_test ( )

  radians_to_degrees_test ( )

  rotation_axis_vector_test ( )
  rotation_axis2mat_test ( )
  rotation_axis2quat_test ( )

  rotation_mat_vector_test ( )
  rotation_mat2axis_test ( )
  rotation_mat2quat_test ( )

  rotation_quat_vector_test ( )
  rotation_quat2axis_test ( )
  rotation_quat2mat_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'quaternions_test' )
  print ( '  Normal end of execution.' )
  return

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
## r8mat_print_test() tests r8mat_print().
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
## r8mat_print_some() prints out a portion of an R8MAT.
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
## r8mat_print_some_test() tests r8mat_print_some().
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

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
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
## r8vec_print_test() tests r8vec_print().
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

def radians_to_degrees ( radians ):

#*****************************************************************************80
#
## radians_to_degrees() converts an angle from radians to degrees.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real radians, an angle in radians.
#
#  Output:
#
#    real VALUE, the equivalent angle in degrees.
#
  import numpy as np

  value = ( radians / np.pi ) * 180.0

  return value

def radians_to_degrees_test ( ):

#*****************************************************************************80
#
## radians_to_degrees_test() tests radians_to_degrees().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'radians_to_degrees_test' )
  print ( '  radians_to_degrees converts an angle from radians' )
  print ( '  to degrees;' )
  print ( '' )
  print ( '  degrees     radians     degrees' )
  print ( '' )

  for i in range ( -2, 15 ):
    angle_deg = float ( 30 * i )
    angle_rad = degrees_to_radians ( angle_deg )
    angle_deg2 = radians_to_degrees ( angle_rad )
    print ( '  %10f  %10f  %10f' % ( angle_deg, angle_rad, angle_deg2 ) )

  return

def rotation_axis2mat ( axis, angle ):

#*****************************************************************************80
#
## rotation_axis2mat() converts a rotation from axis to matrix format in 3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Foley, van Dam, Feiner, Hughes,
#    Computer Graphics, Principles and Practice,
#    Addison Wesley, Second Edition, 1990.
#
#  Input:
#
#    real AXIS[3], the axis vector which remains 
#    unchanged by the rotation.
#
#    real ANGLE, the angular measurement of the
#    rotation about the axis, in radians.
#
#  Output:
#
#    real A[3,3], the rotation matrix.
#
  import numpy as np

  a = np.zeros ( [ 3, 3 ] )

  axis_norm = np.linalg.norm ( axis )
  if ( axis_norm == 0.0 ):
    return a

  axis[0:3] = axis[0:3] / axis_norm

  ca = np.cos ( angle )
  sa = np.sin ( angle )

  a[0,0] =                axis[0] * axis[0] + ca * ( 1.0 - axis[0] * axis[0] )
  a[0,1] = ( 1.0 - ca ) * axis[0] * axis[1] - sa * axis[2]
  a[0,2] = ( 1.0 - ca ) * axis[0] * axis[2] + sa * axis[1]

  a[1,0] = ( 1.0 - ca ) * axis[1] * axis[0] + sa * axis[2]
  a[1,1] =                axis[1] * axis[1] + ca * ( 1.0 - axis[1] * axis[1] )
  a[1,2] = ( 1.0 - ca ) * axis[1] * axis[2] - sa * axis[0]

  a[2,0] = ( 1.0 - ca ) * axis[2] * axis[0] - sa * axis[1]
  a[2,1] = ( 1.0 - ca ) * axis[2] * axis[1] + sa * axis[0]
  a[2,2] =                axis[2] * axis[2] + ca * ( 1.0 - axis[2] * axis[2] )

  return a

def rotation_axis2mat_test ( ):

#*****************************************************************************80
#
## rotation_axis2mat_test() tests rotation_axis2mat().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rotation_axis2mat_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rotation_axis2mat converts a rotation axis to a matrix.' )

  v = np.array ( [ 1.0, 4.0, 10.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  axis = np.array ( [ 0.2361737, -0.8814124, -0.4090649 ] )
  r8vec_print ( 3, axis, '  The rotation axis:' )

  angle = 1.159804
  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  a = rotation_axis2mat ( axis, angle )

  r8mat_print ( 3, 3, a, '  The rotation matrix A:' )

  w = np.dot ( a, v )

  r8vec_print ( 3, w, '  The rotated vector W = A * V:' )
#
#  Test an axis vector that does not have unit length.
#
  v = np.array ( [ 1.0, 1.0, 1.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  axis = np.array ( [ 0.0, 0.0, 2.0 ] )
  r8vec_print ( 3, axis, '  The rotation axis:' )

  angle = 90.0
  angle = degrees_to_radians ( angle )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  a = rotation_axis2mat ( axis, angle )

  r8mat_print ( 3, 3, a, '  The rotation matrix A:' )

  w = np.dot ( a, v )

  r8vec_print ( 3, w, '  The rotated vector W = A * V:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rotation_axis2mat_test' )
  print ( '  Normal end of execution.' )
  return

def rotation_axis2quat ( axis, angle ):

#*****************************************************************************80
#
## rotation_axis2quat() converts a rotation from axis to quaternion format in 3D.
#
#  Discussion:
#
#    A rotation quaternion Q has the form:
#
#      Q = A + Bi + Cj + Dk
#
#    where A, B, C and D are real numbers, and i, j, and k are to be regarded
#    as symbolic constant basis vectors, similar to the role of the "i"
#    in the representation of imaginary numbers.
#
#    A is the cosine of half of the angle of rotation.  (B,C,D) is a
#    unit vector pointing in the direction of the axis of rotation.
#    Rotation multiplication and inversion can be carried out using
#    this format and the usual rules for quaternion multiplication
#    and inversion.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real AXIS(3), the axis vector which remains 
#    unchanged by the rotation.
#
#    real ANGLE, the angular measurement of the 
#    rotation about the axis, in radians.
#
#  Output:
#
#    real Q(4), the quaternion representing the rotation.
#
  import numpy as np

  q = np.zeros ( 4 )

  axis_norm = np.linalg.norm ( axis )

  if ( axis_norm == 0.0 ):
    print ( '' )
    print ( 'rotation_axis2quat_3D - Fatal error!' )
    print ( '  The axis vector is null.' )

  q[0]   = np.cos ( 0.5 * angle )
  q[1:4] = np.sin ( 0.5 * angle ) * axis[0:3] / axis_norm

  return q

def rotation_axis2quat_test ( ):

#*****************************************************************************80
#
## rotation_axis2quat_test() tests rotation_axis2quat().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rotation_axis2quat_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rotation_axis2quat converts a rotation axis to a quaternion.' )
 
  v = np.array ( [ 1.0, 4.0, 10.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  axis = np.array ( [ 0.2361737, -0.8814124, -0.4090649 ] )
  r8vec_print ( 3, axis, '  The rotation axis:' )

  angle = 1.159804
  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  q = rotation_axis2quat ( axis, angle )

  r8vec_print ( 4, q, '  The rotation quaternion Q:' )

  w = rotation_quat_vector ( q, v )

  r8vec_print ( 3, w, '  The rotated vector W:' )
#
#  Another test of rotation_axis_vector with an axis vector
#  that does not have unit length.
#
  v = np.array ( [ 1.0, 1.0, 1.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  axis = np.array ( [ 0.0, 0.0, 2.0 ] )
  r8vec_print ( 3, axis, '  The rotation axis:' )

  angle = 90.0
  angle = degrees_to_radians ( angle )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )
  q = rotation_axis2quat ( axis, angle )

  r8vec_print ( 4, q, '  The rotation quaternion Q:' )

  w = rotation_quat_vector ( q, v )

  r8vec_print ( 3, w, '  The rotated vector W:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rotation_axis2quat_test' )
  print ( '  Normal end of execution.' )
  return

def rotation_axis_vector ( axis, angle, v ):

#*****************************************************************************80
#
## rotation_axis_vector() rotates a vector around an axis vector in 3D.
#
#  Discussion:
#
#    Thanks to Cody Farnell for correcting some mistakes in an earlier
#    version of this routine.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real AXIS(3), the axis vector for the rotation.
#
#    real ANGLE, the angle, in radians, of the rotation.
#
#    real V(3), the vector to be rotated.
#
#  Output:
#
#    real W(3), the rotated vector.
#
  import numpy as np
#
#  Compute the length of the rotation axis.
#
  u = axis.copy ( )
  axis_norm = np.linalg.norm ( u )

  if ( axis_norm == 0.0 ):
    w = np.zeros ( 3 )
    return w

  u = u / axis_norm
#
#  Compute the dot product of the vector and the rotation axis.
#
  udotv = np.dot ( u, v )
#
#  Compute the parallel component of the vector.
#
  parallel = udotv * u
#
#  Compute the normal component of the vector.
#
  normal = v - parallel

  normal_norm = np.linalg.norm ( normal )

  if ( normal_norm == 0.0 ):
    w = parallel.copy ( )
    return w

  normal = normal / normal_norm
#
#  Compute a second vector, lying in the plane, perpendicular
#  to V, and forming a right-handed system, as the cross product
#  of the first two vectors.
#
  normal2 = np.zeros ( 3 )

  normal2[0] = u[1] * normal[2] - u[2] * normal[1]
  normal2[1] = u[2] * normal[0] - u[0] * normal[2]
  normal2[2] = u[0] * normal[1] - u[1] * normal[0]

  normal2_norm = np.linalg.norm ( normal2 )

  normal2 = normal2 / normal2_norm
#
#  Rotate the normal component by the angle.
#
  rot = normal_norm * ( \
      np.cos ( angle ) * normal \
    + np.sin ( angle ) * normal2 )
#
#  The rotated vector is the parallel component plus the rotated component.
#
  w = parallel + rot

  return w

def rotation_axis_vector_test ( ):

#*****************************************************************************80
#
## rotation_axis_vector_test() tests rotation_axis_vector().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 July 2019=8
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  angle = 1.159804
  axis = np.array ( [ 0.2361737, -0.8814124, -0.4090649 ] )
  v = np.array ( [ 1.0, 4.0, 10.0 ] )

  print ( '' )
  print ( 'rotation_axis_vector_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rotation_axis_vector applies an axis' )
  print ( '  rotation to a vector' )

  r8vec_print ( 3, v, '  The vector:' )

  r8vec_print ( 3, axis, '  The rotation axis:' )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  w = rotation_axis_vector ( axis, angle, v )

  r8vec_print ( 3, w, '  The rotated vector:' )
#
#  Another test of rotation_axis_vector with an axis vector
#  that does not have unit length.
#
  v = np.array ( [ 1.0, 1.0, 1.0 ] )

  r8vec_print ( 3, v, '  The vector:' )

  axis = np.array ( [ 0.0, 0.0, 2.0 ] )

  r8vec_print ( 3, axis, '  The rotation axis:' )

  angle = 90.0
  angle = degrees_to_radians ( angle )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  w = rotation_axis_vector ( axis, angle, v )

  r8vec_print ( 3, w, '  The rotated vector:' )

#
#  Terminate.
#
  print ( '' )
  print ( 'rotation_axis_vector_test' )
  print ( '  Normal end of execution.' )
  return

def rotation_mat2axis ( a ):

#*****************************************************************************80
#
## rotation_mat2axis() converts a rotation from matrix to axis format in 3D.
#
#  Discussion:
#
#    The computation is based on the fact that a rotation matrix must
#    have an eigenvector corresponding to the eigenvalue of 1, hence:
#
#      ( A - I ) * v = 0.
#
#    The eigenvector V is the axis of rotation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jack Kuipers,
#    quaternions and Rotation Sequences,
#    Princeton, 1998.
#
#  Input:
#
#    real A(3,3), the rotation matrix.
#
#  Output:
#
#    real AXIS(3), the axis vector which remains
#    unchanged by the rotation.
#
#    real ANGLE, the angular measurement of the
#    rotation about the axis, in radians.
#
  import numpy as np
#
#  Compute the normalized axis of rotation.
#
  axis = np.zeros ( 3 )

  axis[0] = a[2,1] - a[1,2]
  axis[1] = a[0,2] - a[2,0]
  axis[2] = a[1,0] - a[0,1]

  axis_norm = np.linalg.norm ( axis )

  if ( axis_norm == 0.0 ):
    print ( '' )
    print ( 'rotation_mat2axis - Fatal error!' )
    print ( '  A is not a rotation matrix,' )
    print ( '  or there are multiple axes of rotation.' )
    raise Exception ( 'rotation_mat2axis - Fatal error!' )

  axis = axis / axis_norm
#
#  Find the angle.
#
  angle = np.arccos ( 0.5 * ( a[0,0] + a[1,1] + a[2,2] - 1.0 ) )

  return axis, angle

def rotation_mat2axis_test ( ):

#*****************************************************************************80
#
## rotation_mat2axis_test() tests rotation_mat2axis().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  a = np.array ( [ \
   [  0.43301269,  0.25,       -0.86602539 ], \
   [ -0.5,         0.86602539,  0.0 ], \
   [  0.75,        0.43301269,  0.5 ] ])

  print ( '' )
  print ( 'rotation_mat2axis_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rotation_mat2axis computes a rotation axis' )
  print ( '  and angle from a rotation matrix.' )
  print ( '  rotation_axis2mat computes a rotation matrix' )
  print ( '  from a rotation axis and angle.' )

  r8mat_print ( 3, 3, a, '  The rotation matrix:' )

  axis, angle = rotation_mat2axis ( a )

  r8vec_print ( 3, axis, '  The rotation axis:' )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  a = rotation_axis2mat ( axis, angle )

  r8mat_print ( 3, 3, a, '  The recovered rotation matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rotation_mat2axis_test' )
  print ( '  Normal end of execution.' )
  return

def rotation_mat2quat ( a ):

#*****************************************************************************80
#
## rotation_mat2quat() converts a rotation from matrix to quaternion format in 3D.
#
#  Discussion:
#
#    The computation is based on the fact that a rotation matrix must
#    have an eigenvector corresponding to the eigenvalue of 1, hence:
#
#      ( A - I ) * v = 0.
#
#    The eigenvector V is the axis of rotation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jack Kuipers,
#    quaternions and Rotation Sequences,
#    Princeton, 1998.
#
#  Input:
#
#    real A(3,3), the rotation matrix.
#
#  Output:
#
#    real Q(4), the quaternion representing the rotation.
#
  import numpy as np
#
#  Compute the normalized axis of rotation.
#
  axis = np.zeros ( 3 )
  axis[0] = a[2,1] - a[1,2]
  axis[1] = a[0,2] - a[2,0]
  axis[2] = a[1,0] - a[0,1]

  axis_norm = np.linalg.norm ( axis )

  if ( axis_norm == 0.0 ):
    print ( '' )
    print ( 'rotation_mat2quat - Fatal error!' )
    print ( '  A is not a rotation matrix,' )
    print ( '  or there are multiple axes of rotation.' )
    raise Exception ( 'rotation_mat2quat - Fatal error!' )

  axis = axis / axis_norm
#
#  Compute the angle.
#
  angle = np.arccos ( 0.5 * ( a[0,0] + a[1,1] + a[2,2] - 1.0 ) )
#
#  Compute the quaternion.
#
  cos_phi = np.cos ( 0.5 * angle )

  sin_phi = np.sqrt ( 1.0 - cos_phi * cos_phi )

  q = np.zeros ( 4 )
  q[0]   = cos_phi
  q[1:4] = sin_phi * axis[0:3]

  return q

def rotation_mat2quat_test ( ):

#*****************************************************************************80
#
## rotation_mat2quat_test() tests rotation_mat2quat().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  a = np.array ( [ \
   [  0.43301269,  0.25,       -0.86602539 ], \
   [ -0.5,         0.86602539,  0.0 ], \
   [  0.75,        0.43301269,  0.5 ] ] )

  print ( '' )
  print ( 'rotation_mat2quat_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rotation_mat2quat computes a quaternion' )
  print ( '  from a rotation matrix.' )
  print ( '  rotation_quat2mat computes a rotation matrix' )
  print ( '  from a quaternion.' )

  r8mat_print ( 3, 3, a, '  The rotation matrix:' )

  q = rotation_mat2quat ( a )

  r8vec_print ( 4, q, '  The rotation quaternion Q:' )

  a = rotation_quat2mat ( q )

  r8mat_print ( 3, 3, a, '  The recovered rotation matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rotation_mat2quat_test' )
  print ( '  Normal end of execution.' )
  return

def rotation_mat_vector ( a, v ):

#*****************************************************************************80
#
## rotation_mat_vector() applies a matrix rotation to a vector in 3d.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(3,3), the matrix defining the rotation.
#
#    real V(3,1), the vector to be rotated.
#
#  Output:
#
#    real W(3), the rotated vector.
#  
  import numpy as np

  w = np.dot ( a, v )

  return w

def rotation_mat_vector_test ( ):

#*****************************************************************************80
#
## rotation_mat_vector_test() tests rotation_mat_vector().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rotation_mat_vector_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rotation_mat_vector applies a matrix' )
  print ( '  rotation to a vector.' )
 
  a = np.array ( [ \
  [  0.43301269,  0.25,       -0.86602539 ], \
  [ -0.5,         0.86602539,  0.0 ], \
  [  0.75,        0.43301269,  0.5 ] ] )

  r8mat_print ( 3, 3, a, '  The rotation matrix:' )

  v = np.array ( [ 1.0, 4.0, 10.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  w = rotation_mat_vector ( a, v )
  r8vec_print ( 3, w, '  The rotated vector W = A * V:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rotation_mat_vector_test' )
  print ( '  Normal end of execution.' )
  return

def rotation_quat2axis ( q ):

#*****************************************************************************80
#
## rotation_quat2axis() converts a rotation from quaternion to axis format in 3D.
#
#  Discussion:
#
#    A rotation quaternion Q has the form:
#
#      Q = A + Bi + Cj + Dk
#
#    where A, B, C and D are real numbers, and i, j, and k are to be regarded
#    as symbolic constant basis vectors, similar to the role of the "i"
#    in the representation of imaginary numbers.
#
#    A is the cosine of half of the angle of rotation.  (B,C,D) is a
#    vector pointing in the direction of the axis of rotation.
#    Rotation multiplication and inversion can be carried out using
#    this format and the usual rules for quaternion multiplication
#    and inversion.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q(4), the quaternion representing the rotation.
#
#  Output:
#
#    real AXIS(3), the axis vector which remains 
#    unchanged by the rotation.
#
#    real ANGLE, the angular measurement of the 
#    rotation about the axis, in radians.
#
  import numpy as np

  cos_phi = q[0]
  sin_phi = np.linalg.norm ( q[1:4] )

  angle = 2.0 * np.arctan2 ( sin_phi, cos_phi )

  if ( sin_phi == 0.0 ):
    axis = np.array ( [ 1.0, 0.0, 0.0 ] )
  else:
    axis = q[1:4] / sin_phi

  return axis, angle

def rotation_quat2axis_test ( ):

#*****************************************************************************80
#
## rotation_quat2axis_test() tests rotation_quat2axis().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  q = np.array ( [ 0.836516, 0.12941, -0.482963, -0.224144 ] )

  print ( '' )
  print ( 'rotation_quat2axis_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rotation_quat2axis computes a rotation axis' )
  print ( '  and angle from a rotation quaternion.' )
  print ( '  rotation_axis2quat computes a rotation' )
  print ( '  quaternion from a rotation axis and angle.' )

  q8_transpose_print ( q, '  The rotation quaternion:' )

  axis, angle = rotation_quat2axis ( q )

  r8vec_print ( 3, axis, '  The rotation axis:' )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  q = rotation_axis2quat ( axis, angle )

  q8_transpose_print ( q, '  The recoverd rotation quaternion:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rotation_quat2axis_test' )
  print ( '  Normal end of execution.' )
  return

def rotation_quat2mat ( q ):

#*****************************************************************************80
#
## rotation_quat2mat() converts a rotation from quaternion to matrix format in 3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Foley, van Dam, Feiner, Hughes,
#    Computer Graphics, Principles and Practice,
#    Addison Wesley, Second Edition, 1990.
#
#  Input:
#
#    real Q(4), the quaternion representing the rotation.
#
#  Output:
#
#    real A(3,3), the rotation matrix.
#
  import numpy as np

  cos_phi = q[0]
  sin_phi = np.linalg.norm ( q[1:4] )

  angle = 2.0 * np.arctan2 ( sin_phi, cos_phi )

  if ( sin_phi == 0.0 ):
    v1 = 1.0
    v2 = 0.0
    v3 = 0.0
  else:
    v1 = q[1] / sin_phi
    v2 = q[2] / sin_phi
    v3 = q[3] / sin_phi

  ca = np.cos ( angle )
  sa = np.sin ( angle )

  a = np.zeros ( [ 3, 3 ] )

  a[0,0] =                v1 * v1 + ca * ( 1.0 - v1 * v1 )
  a[0,1] = ( 1.0 - ca ) * v1 * v2 - sa * v3
  a[0,2] = ( 1.0 - ca ) * v1 * v3 + sa * v2

  a[1,0] = ( 1.0 - ca ) * v2 * v1 + sa * v3
  a[1,1] =                v2 * v2 + ca * ( 1.0 - v2 * v2 )
  a[1,2] = ( 1.0 - ca ) * v2 * v3 - sa * v1

  a[2,0] = ( 1.0 - ca ) * v3 * v1 - sa * v2
  a[2,1] = ( 1.0 - ca ) * v3 * v2 + sa * v1
  a[2,2] =                v3 * v3 + ca * ( 1.0 - v3 * v3 )

  return a

def rotation_quat2mat_test ( ):

#*****************************************************************************80
#
## rotation_quat2mat_test() tests rotation_quat2mat().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  q = np.array ( [ 0.836516, 0.12941, -0.482963, -0.224144 ] )

  print ( '' )
  print ( 'rotation_quat2mat_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rotation_quat2mat computes a rotation axis' )
  print ( '  from a rotation quaternion.' )
  print ( '  rotation_mat2quat computes a rotation' )
  print ( '  quaternion from a rotation matrix.' )

  print ( '' )
  q8_transpose_print ( q, '  The rotation quaternion:' )

  a = rotation_quat2mat ( q )

  r8mat_print ( 3, 3, a, '  The rotation matrix:' )

  q = rotation_mat2quat ( a )

  print ( '' );
  q8_transpose_print ( q, '  The recovered rotation quaternion:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rotation_quat2mat_test' )
  print ( '  Normal end of execution.' )
  return

def rotation_quat_vector ( q, v ):

#*****************************************************************************80
#
## rotation_quat_vector() applies a quaternion rotation to a vector in 3D.
#
#  Discussion:
#
#    If Q is a unit quaternion that encodes a rotation of ANGLE
#    radians about the vector AXIS, then for an arbitrary real
#    vector V, the result W of the rotation on V can be written as:
#
#      W = Q * V * Conj(Q)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q[3], the quaternion defining the rotation.
#
#    real V[2], the vector to be rotated.
#
#  Output:
#
#    real W[2], the rotated vector.
#
  import numpy as np

  w = np.zeros ( 3 )

  w[0] = \
         ( 2.0 * ( q[0] * q[0] + q[1] * q[1] ) - 1.0 ) * v[0] \
       +   2.0 * ( q[1] * q[2] - q[0] * q[3] )         * v[1] \
       +   2.0 * ( q[1] * q[3] + q[0] * q[2] )         * v[2]

  w[1] = \
           2.0 * ( q[1] * q[2] + q[0] * q[3] )         * v[0] \
       + ( 2.0 * ( q[0] * q[0] + q[2] * q[2] ) - 1.0 ) * v[1] \
       +   2.0 * ( q[2] * q[3] - q[0] * q[1] )         * v[2]

  w[2] = \
           2.0 * ( q[1] * q[3] - q[0] * q[2] )         * v[0] \
       +   2.0 * ( q[2] * q[3] + q[0] * q[1] )         * v[1] \
       + ( 2.0 * ( q[0] * q[0] + q[3] * q[3] ) - 1.0 ) * v[2]

  return w

def rotation_quat_vector_test ( ):

#*****************************************************************************80
#
## rotation_quat_vector_test() tests rotation_quat_vector().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform
  import numpy as np

  print ( '' )
  print ( 'rotation_quat_vector_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  rotation_quat_vector applies a quaternion' )
  print ( '  rotation to a vector.' )

  q = np.array ( [ 0.836516, 0.12941, -0.482963, -0.224144 ] )
  r8vec_print ( 4, q, '  The rotation quaternion:' )

  v = np.array ( [ 1.0, 4.0, 10.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  w = rotation_quat_vector ( q, v )
  r8vec_print ( 3, w, '  The rotated vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rotation_quat_vector_test' )
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
#  Input:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  quaternions_test ( )
  timestamp ( )

