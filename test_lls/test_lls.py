#! /usr/bin/env python3
#
def p00_a ( prob, m, n ):

#*****************************************************************************80
#
## p00_a() returns the matrix A for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  if ( prob == 1 ):
    a = p01_a ( m, n )
  elif ( prob == 2 ):
    a = p02_a ( m, n )
  elif ( prob == 3 ):
    a = p03_a ( m, n )
  elif ( prob == 4 ):
    a = p04_a ( m, n )
  elif ( prob == 5 ):
    a = p05_a ( m, n )
  elif ( prob == 6 ):
    a = p06_a ( m, n )
  else:
    print ( '' )
    print ( 'p00_a - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    raise Exception ( 'p00_a - Fatal error!' )

  return a

def p00_b ( prob, m ):

#*****************************************************************************80
#
## p00_b returns the right hand side B for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  if ( prob == 1 ):
    b = p01_b ( m )
  elif ( prob == 2 ):
    b = p02_b ( m )
  elif ( prob == 3 ):
    b = p03_b ( m )
  elif ( prob == 4 ):
    b = p04_b ( m )
  elif ( prob == 5 ):
    b = p05_b ( m )
  elif ( prob == 6 ):
    b = p06_b ( m )
  else:
    print ( '' )
    print ( 'p00_b - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    raise Exception ( 'p00_b - Fatal error!' )

  return b

def p00_m ( prob ):

#*****************************************************************************80
#
## p00_m returns the number of equations M for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#  Output:
#
#    integer M, the number of equations.
#
  if ( prob == 1 ):
    m = p01_m ( )
  elif ( prob == 2 ):
    m = p02_m ( )
  elif ( prob == 3 ):
    m = p03_m ( )
  elif ( prob == 4 ):
    m = p04_m ( )
  elif ( prob == 5 ):
    m = p05_m ( )
  elif ( prob == 6 ):
    m = p06_m ( )
  else:
    print ( '' )
    print ( 'p00_m - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    raise Exception ( 'p00_m - Fatal error!' )

  return m

def p00_n ( prob ):

#*****************************************************************************80
#
## p00_n returns the number of variables N for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#  Output:
#
#    integer N, the number of variables.
#
  if ( prob == 1 ):
    n = p01_n ( )
  elif ( prob == 2 ):
    n = p02_n ( )
  elif ( prob == 3 ):
    n = p03_n ( )
  elif ( prob == 4 ):
    n = p04_n ( )
  elif ( prob == 5 ):
    n = p05_n ( )
  elif ( prob == 6 ):
    n = p06_n ( )
  else:
    print ( '' )
    print ( 'p00_n - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    raise Exception ( 'p00_n - Fatal error!' )

  return n

def p00_prob_num ( ):

#*****************************************************************************80
#
## p00_prob_num returns the number of least squares problems.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real PROB_num, the number of problems.
#
  prob_num = 6

  return prob_num

def p00_x ( prob, n ):

#*****************************************************************************80
#
## p00_x returns the least squares solution X for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  if ( prob == 1 ):
    x = p01_x ( n )
  elif ( prob == 2 ):
    x = p02_x ( n )
  elif ( prob == 3 ):
    x = p03_x ( n )
  elif ( prob == 4 ):
    x = p04_x ( n )
  elif ( prob == 5 ):
    x = p05_x ( n )
  elif ( prob == 6 ):
    x = p06_x ( n )
  else:
    print ( '' )
    print ( 'p00_x - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    raise Exception ( 'p00_x - Fatal error!' )

  return x

def p01_a ( m, n ):

#*****************************************************************************80
#
## p01_a returns the matrix A for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    a[i,0] = 1.0
    for j in range ( 1, n ):
      a[i,j] = a[i,j-1] * float ( i + 1 )

  return a

def p01_b ( m ):

#*****************************************************************************80
#
## p01_b returns the right hand side B for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 1.0, 2.3, 4.6, 3.1, 1.2 ] )

  return b

def p01_m ( ):

#*****************************************************************************80
#
## p01_m returns the number of equations M for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 5

  return m

def p01_n ( ):

#*****************************************************************************80
#
## p01_n returns the number of variables N for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 3

  return n

def p01_x ( n ):

#*****************************************************************************80
#
## p01_x returns the least squares solution X for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ -3.0200000, 4.4914286, -0.72857143 ] )

  return x

def p02_a ( m, n ):

#*****************************************************************************80
#
## p02_a returns the matrix A for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625,
#    ebook: http://www.mathworks.com/moler/chapters.html
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    a[i,n-1] = 1.0
    for j in range ( n - 2, -1, -1 ):
      a[i,j] = a[i,j+1] * float ( i ) / 5.0

  return a

def p02_b ( m ):

#*****************************************************************************80
#
## p02_b returns the right hand side B for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 150.697, 179.323, 203.212, 226.505, 249.633, 281.422 ] )

  return b

def p02_m ( ):

#*****************************************************************************80
#
## p02_m returns the number of equations M for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 6

  return m

def p02_n ( ):

#*****************************************************************************80
#
## p02_n returns the number of variables N for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 3

  return n

def p02_x ( n ):

#*****************************************************************************80
#
## p02_x returns the least squares solution X for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ 5.7013, 121.1341, 152.4745 ] )

  return x

def p03_a ( m, n ):

#*****************************************************************************80
#
## p03_a returns the matrix A for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625,
#    ebook: http://www.mathworks.com/moler/chapters.html
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  a = np.array ( [ \
       [  1.0,  2.0,  3.0 ], \
       [  4.0,  5.0,  6.0 ], \
       [  7.0,  8.0,  9.0 ], \
       [ 10.0, 11.0, 12.0 ], \
       [ 13.0, 14.0, 15.0 ] ] )

  return a

def p03_b ( m ):

#*****************************************************************************80
#
## p03_b returns the right hand side B for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 16.0, 17.0, 18.0, 19.0, 20.0 ] )

  return b

def p03_m ( ):

#*****************************************************************************80
#
## p03_m returns the number of equations M for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 5

  return m

def p03_n ( ):

#*****************************************************************************80
#
## p03_n returns the number of variables N for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 3

  return n

def p03_x ( n ):

#*****************************************************************************80
#
## p03_x returns the least squares solution X for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ -7.5555556, 0.1111111, 7.7777778 ] )

  return x

def p04_a ( m, n ):

#*****************************************************************************80
#
## p04_a returns the matrix A for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = float ( j + 1 ) ** i

  return a

def p04_b ( m ):

#*****************************************************************************80
#
## p04_b returns the right hand side B for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 15.0, 55.0, 225.0 ] )

  return b

def p04_m ( ):

#*****************************************************************************80
#
## p04_m returns the number of equations M for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 3

  return m

def p04_n ( ):

#*****************************************************************************80
#
## p04_n returns the number of variables N for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 5

  return n

def p04_x ( n ):

#*****************************************************************************80
#
## p04_x returns the least squares solution X for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )

  return x

def p05_a ( m, n ):

#*****************************************************************************80
#
## p05_a returns the matrix A for problem 5.
#
#  Discussion:
#
#    A is the Hilbert matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = 1.0 / float ( i + j + 1 )

  return a

def p05_b ( m ):

#*****************************************************************************80
#
## p05_b returns the right hand side B for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.zeros ( m )

  b[0] = 1.0

  return b

def p05_m ( ):

#*****************************************************************************80
#
## p05_m returns the number of equations M for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 10

  return m

def p05_n ( ):

#*****************************************************************************80
#
## p05_n returns the number of variables N for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 10

  return n

def p05_x ( n ):

#*****************************************************************************80
#
## p05_x returns the least squares solution X for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  from scipy.special import comb
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = r8_mop ( i + 2 ) * float ( i + 1 ) \
      * comb ( n + i, n - 1 ) * comb ( n, n - i - 1 )

  return x

def p06_a ( m, n ):

#*****************************************************************************80
#
## p06_a returns the matrix A for problem 6.
#
#  Discussion:
#
#    A is a symmetric, orthogonal matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      angle = float ( i + 1 ) * float ( j + 1 ) * np.pi / float ( n + 1 )
      a[i,j] = np.sin ( angle )

  a[0:m,0:n] = a[0:m,0:n] * np.sqrt ( 2.0 / ( n + 1 ) )

  return a

def p06_b ( m ):

#*****************************************************************************80
#
## p06_b returns the right hand side B for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.zeros ( m )

  b[0] = 1.0

  return b

def p06_m ( ):

#*****************************************************************************80
#
## p06_m returns the number of equations M for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 10

  return m

def p06_n ( ):

#*****************************************************************************80
#
## p06_n returns the number of variables N for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 10

  return n

def p06_x ( n ):

#*****************************************************************************80
#
## p06_x returns the least squares solution X for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    x[i] = np.sin ( angle )

  x[0:n] = x[0:n] * np.sqrt ( 2.0 / float ( n + 1) )

  return x

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real VALUE, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## r8_mop_test tests r8_mop.
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
  print ( 'r8_mop_test' )
  print ( '  r8_mop evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_mop(I4)' )
  print ( '' )

  i4_min = -100
  i4_max = +100

  for test in range ( 0, 10 ):
    i4 = np.random.random_integers ( i4_min, i4_max )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_mop_test' )
  print ( '  Normal end of execution.' )
  return

def test_lls_test ( ):

#*****************************************************************************80
#
## test_lls_test() tests test_lls().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'test_lls_test()' )
  print ( '  Python version.' )
  print ( '  Test test_lls().' )

  ls_data_test ( )
  lstsq_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_lls_test()' )
  print ( '  Normal end of execution.' )
  return

def lstsq_test ( ):

#*****************************************************************************80
#
## lstsq_test tries out the NUMPY LINALG least squares solver on the data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'lstsq_test' )
  print ( '  lstsq() is the NUMPY LINALG least squares solver.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = %d' % ( prob_num ) )
  print ( '' )
  print ( '  Index     M     N         ||B||     ||X1-X2||         ||X1|| ', end = '' )
  print ( '       ||X2||        ||R1||        ||R2||' )
  print ( '' )

  for prob in range ( 1, prob_num ):

    m = p00_m ( prob )
    n = p00_n ( prob )

    a = p00_a ( prob, m, n )
    b = p00_b ( prob, m )
    x1 = p00_x ( prob, n )

    r1 = np.dot ( a, x1 ) - b

    b_norm = np.linalg.norm ( b )
    x1_norm = np.linalg.norm ( x1 )
    r1_norm = np.linalg.norm ( r1 )

    [ x2, resids, rank, s ] = np.linalg.lstsq ( a, b, rcond = None )
    r2 = np.dot ( a, x2 ) - b
    x2_norm = np.linalg.norm ( x2 )
    r2_norm = np.linalg.norm ( r2 )

    x_diff_norm = np.linalg.norm ( x1 - x2 )

    print ( '  %5d  %4d  %4d  %12.4g  %12.4g  %12.4g  %12.4g  %12.4g  %12.4g' \
      % ( prob, m, n, b_norm, x_diff_norm, x1_norm, x2_norm, r1_norm, r2_norm ) )

  return

def ls_data_test ( ):

#*****************************************************************************80
#
## ls_data_test summarizes the test data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ls_data_test' )
  print ( '  Get each least squares test and compute the maximum residual.' )
  print ( '  The L2 norm of the residual MUST be no greater than' )
  print ( '  the L2 norm of the right hand side, else 0 is a better solution.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = %d' % ( prob_num ) )
  print ( '' )
  print ( '  Index     M     N         ||B||         ||X||         ||R||' )
  print ( '' )

  for prob in range ( 1, prob_num + 1 ):

    m = p00_m ( prob )
    n = p00_n ( prob )

    a = p00_a ( prob, m, n )
    b = p00_b ( prob, m )
    x = p00_x ( prob, n )

    r = np.dot ( a, x ) - b

    b_norm = np.linalg.norm ( b )
    x_norm = np.linalg.norm ( x )
    r_norm = np.linalg.norm ( r )

    print ( '  %5d  %4d  %4d  %12.4g  %12.4g  %12.4g' \
      % ( prob, m, n, b_norm, x_norm, r_norm ) )

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
  test_lls_test ( )
  timestamp ( )

