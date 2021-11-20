#! /usr/bin/env python3
#
def i4_to_l4 ( i4 ):

#*****************************************************************************80
#
## i4_to_l4 converts an I4 to an L4.
#
#  Discussion:
#
#    An I4 is an integer value.
#    An L4 is a bool value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I4, an integer.
#
#  Output:
#
#    bool i4_to_l4, the bool value of I4.
#
  value = ( i4 != 0 )

  return value

def i4_to_l4_test ( ):

#*****************************************************************************80
#
## i4_to_l4_test() tests i4_to_l4(). 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_to_l4_test' )
  print ( '  i4_to_l4 converts an I4 to an L4.' )
  print ( '' )
  print ( '  I4   L4' )
  print ( '' )

  for i4 in range ( -5, +6 ):

    l4 = i4_to_l4 ( i4 )
    print ( '  %2d  %s' % ( i4, l4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_to_l4_test' )
  print ( '  Normal end of execution.' )
  return

def i4_to_l4vec ( i4, n ):

#*****************************************************************************80
#
## i4_to_l4vec() converts an I4 into an L4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I4, the integer.
#
#    integer N, the dimension of the vector.
#
#  Output:
#
#    bool L4VEC(N), the vector.
#
  import numpy as np

  l4vec = np.zeros ( n, dtype = np.bool )

  for i in range ( n - 1, -1, -1 ):
    l4vec[i] = ( ( i4 % 2 ) == 1 )
    i4 = ( i4 // 2 )

  return l4vec

def i4_to_l4vec_test ( ):

#*****************************************************************************80
#
## i4_to_l4vec_test() tests i4_to_l4vec(). 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 September 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_to_l4vec_test' )
  print ( '  i4_to_l4vec converts an I4 to an L4VEC.' )
  print ( '' )
  print ( '  I4   L4VEC' )
  print ( '' )

  n = 8

  for i4 in range ( 0, 11 ):

    l4vec = i4_to_l4vec ( i4, n )
    print ( '  %2d: ' % ( i4 ), end = '' )
    for j in range ( 0, n ):
      print ( ' %1d' % ( l4vec[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' ) 
  print ( 'i4_to_l4vec_test' )
  print ( '  Normal end of execution.' )
  return

def l4lib_test ( ):

#*****************************************************************************80
#
## l4lib_test() tests l4lib().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'l4lib_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test l4lib().' )

  i4_to_l4_test ( )
  i4_to_l4vec_test ( )

  l4_to_i4_test ( )
  l4_to_s_test ( )
  l4_uniform_test ( )
  l4_xor_test ( )

  l4mat_print_test ( )
  l4mat_print_some_test ( )
  l4mat_transpose_print_test ( )
  l4mat_transpose_print_some_test ( )
  l4mat_uniform_test ( )

  l4vec_next_test ( )
  l4vec_print_test ( )
  l4vec_uniform_test ( )

  s_to_l4_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4lib_test:' )
  print ( '  Normal end of execution.' )
  print ( '' )
  return

def l4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## l4mat_print() prints an L4MAT.
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
  l4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def l4mat_print_test ( ):

#*****************************************************************************80
#
## l4mat_print_test() tests l4mat_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'l4mat_print_test:' )
  print ( '  l4mat_print prints an L4MAT.' )

  m = 5
  n = 12
  a = l4mat_uniform ( m, n )
  title = '  A 5 x 3 integer matrix:'
  l4mat_print ( m, n, a, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4mat_print_test:' )
  print ( '  Normal end of execution.' )
  return

def l4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## l4mat_print_some() prints out a portion of an L4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 September 2018
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
  incx = 35

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%2d' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( a[i,j] == 0 ):
          print ( ' F', end = '' )
        else:
          print ( ' T', end = '' )
      print ( '' )

  return

def l4mat_print_some_test ( ):

#*****************************************************************************80
#
## l4mat_print_some_test() tests l4mat_print_some().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'l4mat_print_some_test' )
  print ( '  l4mat_print_some prints some of an L4MAT.' )

  m = 4
  n = 6
  v = l4mat_uniform ( m, n )
  l4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is L4MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4mat_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def l4mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## l4mat_transpose_print() prints an L4MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
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
  l4mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def l4mat_transpose_print_test ( ):

#*****************************************************************************80
#
## l4mat_transpose_print_test() tests l4mat_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'l4mat_transpose_print_test:' )
  print ( '  l4mat_transpose_print prints an L4MAT transposed.' )

  m = 5
  n = 12
  a = l4mat_uniform ( m, n )
  title = '  A 5 x 12 integer matrix:'
  l4mat_transpose_print ( m, n, a, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4mat_transpose_print_test:' )
  print ( '  Normal end of execution.' )
  return

def l4mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## l4mat_transpose_print_some() prints some of an L4MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
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
  incx = 35

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
      print ( '%2d' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( ' %4d: ' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        if ( a[i,j] == 0 ):
          print ( ' F', end = '' )
        else:
          print ( ' T', end = '' )
      print ( '' )

  return

def l4mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## l4mat_transpose_print_some_test() tests l4mat_transpose_print_some().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'l4mat_transpose_print_some_test' )
  print ( '  l4mat_transpose_print_some prints some of an L4MAT, transposed.' )

  m = 4
  n = 6
  v = l4mat_uniform ( m, n )
  l4mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  Here is L4MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4mat_transpose_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def l4mat_uniform ( m, n ):

#*****************************************************************************80
#
## l4mat_uniform() returns a pseudorandom L4MAT.
#
#  Discussion:
#
#    An L4MAT is a two dimensional array of bool values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    bool L4MAT(M,N), a pseudorandom matrix.
#
  import numpy as np

  i4mat = np.random.random_integers ( 0, 1, size = ( m, n ) )
  l4mat = ( i4mat == 1 )

  return l4mat

def l4mat_uniform_test ( ):

#*****************************************************************************80
#
## l4mat_uniform_test() tests l4mat_uniform().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 4

  print ( '' )
  print ( 'l4mat_uniform_test' )
  print ( '  l4mat_uniform computes a random L4MAT.' )
  print ( '' )

  v = l4mat_uniform ( m, n )

  l4mat_print ( m, n, v, '  Random L4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4mat_uniform_test:' )
  print ( '  Normal end of execution.' )

  return

def l4_to_i4 ( l ):

#*****************************************************************************80
#
## l4_to_i4() converts an L4 to an I4.
#
#  Discussion:
#
#    0 is FALSE, and anything else if TRUE.
#
#    An I4 is an integer value.
#    An L4 is a bool value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    bool L, a value.
#
#  Output:
#
#    integer VALUE, the integer value of L.
#
  if ( l ):
    value = 1
  else:
    value = 0

  return value

def l4_to_i4_test ( ):

#*****************************************************************************80
#
## l4_to_i4_test() tests l4_to_i4(). 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'l4_to_i4_test' )
  print ( '  l4_to_i4 converts an L4 to an I4.' )
  print ( '' )
  print ( '      L4   I4' )
  print ( '' )

  l4 = False
  i4 = l4_to_i4 ( l4 )
  print ( '   %5s    %1d' % ( l4, i4 ) )

  l4 = True
  i4 = l4_to_i4 ( l4 )
  print ( '   %5s    %1d' % ( l4, i4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4_to_i4_test' )
  print ( '  Normal end of execution.' )

def l4_to_s ( l4 ):

#*****************************************************************************80
#
## l4_to_s() converts an L4 to a string.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    bool L4, a value.
#
#  Output:
#
#    string VALUE, the string.
#
  if ( l4 ):
    value = 'True'
  else:
    value = 'False'

  return value

def l4_to_s_test ( ):

#*****************************************************************************80
#
## l4_to_s_test() tests l4_to_s(). 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'l4_to_s_test' )
  print ( '  l4_to_s converts an L4 to a string.' )
  print ( '' )
  print ( '      L4   S' )
  print ( '' )

  l4 = False
  s= l4_to_s ( l4 )
  print ( '   %5s    %s' % ( l4, s ) )

  l4 = True
  s = l4_to_s ( l4 )
  print ( '   %5s    %s' % ( l4, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4_to_s_test' )
  print ( '  Normal end of execution.' )

def l4_uniform ( ):

#*****************************************************************************80
#
## l4_uniform() returns a pseudorandom L4.
#
#  Discussion:
#
#    An L4 is a bool value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    bool L4, a pseudorandom value.
#
  import numpy as np

  i4 = np.random.random_integers ( 0, 1 )
  l4 = ( i4 == 1 )

  return l4

def l4_uniform_test ( ):

#*****************************************************************************80
#
## l4_uniform_test() tests l4_uniform().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'l4_uniform_test' )
  print ( '  l4_uniform returns random bool values' )
  print ( '' )

  for i in range ( 0, 10 ):
    l4 = l4_uniform ( )
    print ( '  %d' % ( l4 ) )

  print ( '' )
  print ( 'l4_uniform_test' )
  print ( '  Normal end of execution' )

  return

def l4vec_next ( n, l4vec ):

#*****************************************************************************80
#
## l4vec_next() generates the next bool vector.
#
#  Discussion:
#
#    In the following discussion, we will let '0' stand for FALSE and
#    '1' for TRUE.
#
#    The vectors have the order
#
#      (0,0,...,0),
#      (0,0,...,1),
#      ...
#      (1,1,...,1)
#
#    and the "next" vector after (1,1,...,1) is (0,0,...,0).  That is,
#    we allow wrap around.
#
#  Example:
#
#    N = 3
#
#    Input      Output
#    -----      ------
#    0 0 0  =>  0 0 1
#    0 0 1  =>  0 1 0
#    0 1 0  =>  0 1 1
#    0 1 1  =>  1 0 0
#    1 0 0  =>  1 0 1
#    1 0 1  =>  1 1 0
#    1 1 0  =>  1 1 1
#    1 1 1  =>  0 0 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    bool L4VEC(N), the vector whose successor is desired.
#
#  Output:
#
#    bool L4VEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( not l4vec[i] ):
      l4vec[i] = True
      break

    l4vec[i] = False

  return l4vec

def l4vec_next_test ( ):

#*****************************************************************************80
#
## l4vec_next_test() tests l4vec_next().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'l4vec_next_test' )
  print ( '  l4vec_next generates bool vectors of dimension N one at a time.' )

  for n in range ( 2, 4 ):

    print ( '' )
    print ( '  Vector size N = %d' % ( n ) )
    print ( '' )

    k = 0

    l4vec = np.zeros ( n, dtype = np.bool )

    for i in range ( 0, n ):
      l4vec[i] = False

    while ( True ):

      print ( '  %2d:  ' % ( k ), end = '' )
      for i in range ( 0, n ):
        print ( '  %s' % ( l4vec[i] ), end = '' )
      print ( '' )

      l4vec = l4vec_next ( n, l4vec )

      if ( not any ( l4vec ) ):
        break

      k = k + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'l4vec_next_test:' )
  print ( '  Normal end of execution.' )
  return

def l4vec_print ( n, a, title ):

#*****************************************************************************80
#
## l4vec_print() prints an L4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    bool A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    if ( a[i] == 0 ):
      print ( '%6d  F' % ( i ) )
    else:
      print ( '%6d  T' % ( i ) )

  return

def l4vec_print_test ( ):

#*****************************************************************************80
#
## l4vec_print_test() tests l4vec_print().
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

  print ( '' )
  print ( 'l4vec_print_test' )
  print ( '  l4vec_print prints an L4VEC.' )

  n = 10
  v = l4vec_uniform ( n )
  l4vec_print ( n, v, '  Here is an L4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4vec_print_test:' )
  print ( '  Normal end of execution.' )
  return

def l4vec_uniform ( n ):

#*****************************************************************************80
#
## l4vec_uniform() returns a pseudorandom L4VEC.
#
#  Discussion:
#
#    An L4VEC is a vector of bool values.
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
#    integer N, the order of the vector.
#
#  Output:
#
#    bool L4VEC(N), a pseudorandom vector.
#
  import numpy as np

  i4vec = np.random.random_integers ( 0, 1, size = n )
  l4vec = ( i4vec == 1 )

  return l4vec

def l4vec_uniform_test ( ):

#*****************************************************************************80
#
## l4vec_uniform_test() tests l4vec_uniform().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'l4vec_uniform_test' )
  print ( '  l4vec_uniform computes a random L4VEC.' )
  print ( '' )

  v = l4vec_uniform ( n )

  l4vec_print ( n, v, '  Random L4VEC:' )

  print ( '' )
  print ( 'l4vec_uniform_test:' )
  print ( '  Normal end of execution.' )

  return

def l4_xnor ( l1, l2 ):

#*****************************************************************************80
#
## l4_xnor() returns the complement exclusive OR of two L4's.
#
#  Discussion:
#
#    An L4 is a bool value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2017
#
#  Author:
#
#   John Burkardt
#
#  Input:
#
#    bool L1, L2, two values.
#
#  Output:
#
#    bool VALUE, the complement exclusive OR of L1 and L2.
#
  value =  ( (       l1   and       l2   ) or \
             ( ( not l1 ) and ( not l2 ) ) )

  return value

def l4_xnor_test ( ):

#*****************************************************************************80
#
## l4_xnor_test() tests l4_xnor(). 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'l4_xnor_test' )
  print ( '  l4_xnor computes the complement exclusive OR of two L4\'s' )
  print ( '' )
  print ( '      L1      L2  l4_xor(L1,L2)' )
  print ( '' )

  for l1 in ( False, True ):
    for l2 in ( False, True ):
      l4 = l4_xnor ( l1, l2 )
      print ( '   %5s   %5s    %5s' % ( l1, l2, l4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4_xnor_test' )
  print ( '  Normal end of execution.' )
  return

def l4_xor ( l1, l2 ):

#*****************************************************************************80
#
## l4_xor() returns the exclusive OR of two L4's.
#
#  Discussion:
#
#    An L4 is a bool value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#   John Burkardt
#
#  Input:
#
#    bool L1, L2, two values whose exclusive OR is needed.
#
#  Output:
#
#    bool VALUE, the exclusive OR of L1 and L2.
#
  value =  ( (       l1   and ( not l2 ) ) or \
             ( ( not l1 ) and       l2   ) )

  return value

def l4_xor_test ( ):

#*****************************************************************************80
#
## l4_xor_test() tests l4_xorv. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'l4_xor_test' )
  print ( '  l4_xor computes the exclusive OR of two L4\'s' )
  print ( '' )
  print ( '      L1      L2  l4_xor(L1,L2)' )
  print ( '' )

  for l1 in ( False, True ):
    for l2 in ( False, True ):
      l4 = l4_xor ( l1, l2 )
      print ( '   %5s   %5s    %5s' % ( l1, l2, l4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4_xor_test' )
  print ( '  Normal end of execution.' )
  return

def s_to_l4 ( s ):

#*****************************************************************************80
#
## s_to_l4() reads a bool value from a string.
#
#  Discussion:
#
#    There are several ways of representing bool data that this routine
#    recognizes:
#
#      False   True
#      -----   ----
#
#      0       1
#      F       T
#      f       t
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S, the string to be read.
#
#  Output:
#
#    bool L, the value read from the string.
#
  s_length = len ( s )

  for i in range ( 0, s_length ):

    if ( s[i] == '0' or s[i] == 'F' or s[i] == 'f' ):
      l = False
      return l
    elif ( s[i] == '1' or s[i] == 'T' or s[i] == 't' ):
      l = True
      return l

  print ( '' )
  print ( 's_to_l4 - Fatal error!' )
  print ( '  The input string did not contain bool data.' )
  raise Exception ( 'S_to_l4 - Fatal error!' )

def s_to_l4_test ( ):

#*****************************************************************************80
#
## s_to_l4_test() tests s_to_l4().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
  test_num = 10

  import numpy as np

  s_test = [ \
    '0      ', \
    'F      ', \
    'f      ', \
    '1      ', \
    'T      ', \
    't      ', \
    '  0    ', \
    '  1  0 ', \
    '  01   ', \
    '  Talse' ]

  print ( '' )
  print ( 's_to_l4_test' )
  print ( '  s_to_l4 reads bool data from a string.' )
  print ( '' )
  print ( '        S   L4' )
  print ( '' )

  for test in range ( 0, test_num ):
    s = s_test[test]
    l4 = s_to_l4 ( s )
    print ( '  "%7s"  %s' % ( s, l4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 's_to_l4_test' )
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
  l4lib_test ( )
  timestamp ( )

