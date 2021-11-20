#! /usr/bin/env python3
#
def file_column_count ( filename ):

#*****************************************************************************80
#
## file_column_count() counts the number of words in a typical column of a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file.
#
#  Output:
#
#    integer column_count, the number of words in a typical column.
#
  column_count = -1

  input = open ( filename, 'r' )

  column_count = 0

  for line in input:

    if ( line[0] == '#' ):
      continue
    else:

      wc = 0
      for word in line.strip().split():
         wc = wc + 1

      if ( wc == 0 ):
        continue
      elif ( column_count == 0 ):
        column_count = wc
        break

  input.close ( )

  return column_count

def file_column_count_test ( ):

#*****************************************************************************80
#
## file_column_count_test tests file_column_count.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'file_column_count_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Count the number of columns in a typical text file line.' )

  filename = 'r8mat_write_test.txt'
  column_count = file_column_count ( filename )

  print ( '' )
  print ( '  Number of columns in "%s" is %d' % ( filename, column_count ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'file_column_count_test:' )
  print ( '  Normal end of execution.' )
  return

def file_row_count ( filename ):

#*****************************************************************************80
#
## file_row_count counts the number of rows (lines) in a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file.
#
#  Output:
#
#    integer ROW_count, the number of rows in the file.
#
  row_count = -1

  input = open ( filename, 'r' )

  row_count = 0

  for line in input:

    if ( line[0] == '#' ):
      continue
    else:

      wc = 0
      for word in line.strip().split():
         wc = wc + 1

      if ( wc == 0 ):
        continue
      else:
        row_count = row_count + 1

  input.close ( )

  return row_count

def file_row_count_test ( ):

#*****************************************************************************80
#
## file_row_count_test tests file_row_count.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'file_row_count_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Count the number of rows in a text file.' )

  filename = 'i4mat_write_test.txt'
  row_count = file_row_count ( filename )

  print ( '' )
  print ( '  Number of rows in "%s" is %d' % ( filename, row_count ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'file_row_count_test:' )
  print ( '  Normal end of execution.' )
  return

def i4_log_10 ( i ):

#*****************************************************************************80
#
## i4_log_10 returns the integer part of the logarithm base 10 of ABS(X).
#
#  Example:
#
#        I  VALUE
#    -----  --------
#        0    0
#        1    0
#        2    0
#        9    0
#       10    1
#       11    1
#       99    1
#      100    2
#      101    2
#      999    2
#     1000    3
#     1001    3
#     9999    3
#    10000    4
#
#  Discussion:
#
#    i4_log_10 ( I ) + 1 is the number of decimal digits in I.
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
#    integer I, the number whose logarithm base 10 is desired.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm base 10 of
#    the absolute value of X.
#
  import numpy as np

  i = np.floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0
    ten_pow = 10

    i_abs = abs ( i )

    while ( ten_pow <= i_abs ):
      value = value + 1
      ten_pow = ten_pow * 10

  return value

def i4_log_10_test ( ) :

#*****************************************************************************80
#
## i4_log_10_test tests i4_log_10.
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
  import platform

  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ( '' )
  print ( 'i4_log_10_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_log_10: whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_log_10_test' )
  print ( '  Normal end of execution.' )
  return

def i4mat_data_read ( filename, m, n ):

#*****************************************************************************80
#
## i4mat_data_read reads the data from an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an array of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#    integer M, the number of rows in the file.
#
#    integer N, the number of columns in the file.
#
#  Output:
#
#    integer TABLE(M,N), the data.
#
  import numpy as np

  j = -1

  input = open ( filename, 'r' )

  table = np.zeros ( ( m, n ), dtype=np.int )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      j = 0
      for word in line.strip().split():
        table[i,j] = int ( word )
        j = j + 1
      i = i + 1

  input.close ( )

  return table

def i4mat_data_read_test ( ):

#*****************************************************************************80
#
## i4mat_data_read_test tests i4mat_data_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4mat_data_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test i4mat_data_read, which reads data from an I4MAT.' )

  m = 5
  n = 3
  filename = 'i4mat_write_test.txt'
  a = i4mat_data_read ( filename, m, n )
  i4mat_print ( m, n, a, '  Data read from file:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4mat_data_read_test:' )
  print ( '  Normal end of execution.' )
  return

def i4mat_header_read ( filename ):

#*****************************************************************************80
#
## i4mat_header_read reads the header from an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an array of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    Input, string FILENAME, the name of the input file.
#
#  Output:
#
#    integer M, the number of rows in the file.
#
#    integer N, the number of columns in the file.
#
  m = file_row_count ( filename )
  n = file_column_count ( filename )

  return m, n

def i4mat_header_read_test ( ):

#*****************************************************************************80
#
## i4mat_header_read_test tests i4mat_header_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4mat_header_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4mat_header_read counts rows and columns in a file' )
  print ( '  containing an I4MAT.' )

  filename = 'i4mat_write_test.txt'
  m, n = i4mat_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows and %d columns.' % ( filename, m, n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4mat_header_read_test:' )
  print ( '  Normal end of execution.' )
  return

def i4mat_indicator ( m, n ):

#*****************************************************************************80
#
## i4mat_indicator sets up an indicator I4MAT.
#
#  Discussion:
#
#    The value of each entry suggests its location, as in:
#
#      11  12  13  14
#      21  22  23  24
#      31  32  33  34
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#  Output:
#
#    integer TABLE(M,N), the indicator table.
#
  import numpy as np

  table = np.zeros ( ( m, n ), dtype = np.int32 )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      table[i,j] = fac * ( i + 1 ) + ( j + 1 )

  return table

def i4mat_indicator_test ( ):

#*****************************************************************************80
#
## i4mat_indicator_test tests i4mat_indicator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4mat_indicator_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4mat_indicator creates an "indicator" I4MAT.' )

  m = 5
  n = 4
  a = i4mat_indicator ( m, n )
  i4mat_print ( m, n, a, '  The indicator matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4mat_indicator_test' )
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
## i4mat_print_test tests i4mat_print.
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
#    08 September 2018
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
  incx = 10

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
      print ( '%7d  ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%7d  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def i4mat_print_some_test ( ):

#*****************************************************************************80
#
## i4mat_print_some_test tests i4mat_print_some.
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

def i4mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## i4mat_write writes an I4MAT to a file.
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
#    integer A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %d' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def i4mat_write_test ( ):

#*****************************************************************************80
#
## i4mat_write_test tests i4mat_write.
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
  print ( 'i4mat_write_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4mat_write writes an I4MAT to a file.' )

  filename = 'i4mat_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 11, 12, 13 ), \
    ( 21, 22, 23 ), \
    ( 31, 32, 33 ), \
    ( 41, 42, 43 ), \
    ( 51, 52, 53 ) ) )
  i4mat_write ( filename, m, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4mat_write_test:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_data_read ( filename, m ):

#*****************************************************************************80
#
## i4vec_data_read reads the data from an I4VEC.
#
#  Discussion:
#
#    An I4VEC is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#    integer M, the number of rows in the file.
#
#  Output:
#
#    real TABLE(M), the data.
#
  import numpy as np

  j = -1

  input = open ( filename, 'r' )

  table = np.zeros ( m, dtype = np.int32 )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      table[i] = int ( line.strip() )
      i = i + 1

  input.close ( )

  return table

def i4vec_data_read_test ( ):

#*****************************************************************************80
#
## i4vec_data_read_test tests i4vec_data_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4vec_data_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_data_read reads data from an I4VEC.' )

  m = 5
  n = 3
  filename = 'i4vec_write_test.txt'
  a = i4vec_data_read ( filename, m )
  i4vec_print ( m, a, '  Data read from file:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_data_read_test:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_header_read ( filename ):

#*****************************************************************************80
#
## i4vec_header_read reads the header from an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#  Output:
#
#    integer M, the number of rows in the file.
#
  m = file_row_count ( filename )

  return m

def i4vec_header_read_test ( ):

#*****************************************************************************80
#
## i4vec_header_read_test tests i4vec_header_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4vec_header_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_header_read counts rows in a file' )
  print ( '  containing an I4VEC.' )

  filename = 'i4vec_write_test.txt'
  m = i4vec_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows.' % ( filename, m ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_header_read_test:' )
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
## i4vec_print_test tests i4vec_print.
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

def i4vec_write ( filename, n, a ):

#*****************************************************************************80
#
## i4vec_write writes an I4VEC to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer N, the number of entris in A.
#
#    integer A(N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %d\n' % ( a[i] )
    output.write ( s )

  output.close ( )

  return

def i4vec_write_test ( ):

#*****************************************************************************80
#
## i4vec_write_test tests i4vec_write.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4vec_write_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_write writes an I4VEC to a file.' )

  filename = 'i4vec_write_test.txt'
  n = 5
  a = np.array ( ( 11, 22, 33, 44, 55 ) )
  i4vec_write ( filename, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_write_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_data_read ( filename, m, n ):

#*****************************************************************************80
#
## r8mat_data_read reads the data from an R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#    integer M, the number of rows in the file.
#
#    integer N, the number of columns in the file.
#
#  Output:
#
#    real TABLE(M,N), the data.
#
  import numpy as np

  j = -1

  input = open ( filename, 'r' )

  table = np.zeros ( ( m, n ) )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      j = 0
      for word in line.strip().split():
        table[i,j] = float ( word )
        j = j + 1
      i = i + 1

  input.close ( )

  return table

def r8mat_data_read_test ( ):

#*****************************************************************************80
#
## r8mat_data_read_test tests r8mat_data_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8mat_data_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_data_read reads data from an R8MAT.' )

  m = 5
  n = 3
  filename = 'r8mat_write_test.txt'
  a = r8mat_data_read ( filename, m, n )
  r8mat_print ( m, n, a, '  Data read from file:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_data_read_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_header_read ( filename ):

#*****************************************************************************80
#
## r8mat_header_read reads the header from an R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#  Output:
#
#    integer M, the number of columns in the file.
#
#    integer N, the number of rows in the file.
#
  m = file_row_count ( filename )
  n = file_column_count ( filename )

  return m, n

def r8mat_header_read_test ( ):

#*****************************************************************************80
#
## r8mat_header_read_test tests r8mat_header_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_header_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_header_read counts rows and columns in a file' )
  print ( '  containing an R8MAT.' )

  filename = 'r8mat_write_test.txt'
  m, n = r8mat_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows and %d columns.' % ( filename, m, n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_header_read_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_indicator ( m, n ):

#*****************************************************************************80
#
## r8mat_indicator sets up an indicator R8MAT.
#
#  Discussion:
#
#    The value of each entry suggests its location, as in:
#
#      11  12  13  14
#      21  22  23  24
#      31  32  33  34
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#  Output:
#
#    real TABLE(M,N), the indicator table.
#
  import numpy as np

  table = np.zeros ( ( m, n ), dtype = np.float64 )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      table[i,j] = fac * ( i + 1 ) + ( j + 1 )

  return table

def r8mat_indicator_test ( ):

#*****************************************************************************80
#
## r8mat_indicator_test tests r8mat_indicator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8mat_indicator_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_indicator creates an "indicator" R8MAT.' )

  m = 5
  n = 4
  a = r8mat_indicator ( m, n )
  r8mat_print ( m, n, a, '  The indicator matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_indicator_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2020
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
## r8mat_print_test tests r8mat_print.
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
#    08 May 2020
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
## r8mat_print_some_test tests r8mat_print_some.
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
## r8mat_transpose_print_test tests r8mat_transpose_print.
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
## r8mat_transpose_print_some_test tests r8mat_transpose_print_some.
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

def r8mat_transpose_write ( filename, m, n, a ):

#*****************************************************************************80
#
## r8mat_transpose_write writes the transpose of an R8MAT to a file.
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

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8mat_transpose_write_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_write_test tests r8mat_transpose_write.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_transpose_write_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test r8mat_transpose_write, which writes the transpose of an R8MAT to a file.' )

  filename = 'r8mat_transpose_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 1.1, 1.2, 1.3 ), \
    ( 2.1, 2.2, 2.3 ), \
    ( 3.1, 3.2, 3.3 ), \
    ( 4.1, 4.2, 4.3 ), \
    ( 5.1, 5.2, 5.3 ) ) )
  r8mat_transpose_write ( filename, m, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_transpose_write_test:' )
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
## r8mat_write_test tests r8mat_write.
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

def r8vec2_data_read ( filename, m ):

#*****************************************************************************80
#
## r8vec2_data_read reads the data from an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is an pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#    integer M, the number of rows in the file.
#
#  Output:
#
#    real X(M), Y(M), the data.
#
  import numpy as np

  input = open ( filename, 'r' )

  x = np.zeros ( m )
  y = np.zeros ( m )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      data = line.split ( )
      x[i] = data[0]
      y[i] = data[1]
      i = i + 1

  input.close ( )

  return x, y

def r8vec2_data_read_test ( ):

#*****************************************************************************80
#
## r8vec2_data_read_test tests r8vec2_data_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  print ( '' )
  print ( 'r8vec2_data_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_data_read reads data from an R8VEC2.' )

  m = 5
  filename = 'r8vec2_write_test.txt'
  x, y = r8vec2_data_read ( filename, m )
  r8vec2_print ( x, y, '  Data read from file:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_data_read_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_header_read ( filename ):

#*****************************************************************************80
#
## r8vec2_header_read reads the header from an R8VEC2 file.
#
#  Discussion:
#
#    An R8VEC2 is a pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#  Output:
#
#    integer M, the number of rows in the file.
#
  n = file_column_count ( filename )

  if ( n != 2 ):
    print ( '' )
    print ( 'r8vec2_header_read - Fatal error!' )
    print ( '  The number of columns is not 2, but %d.' % ( n ) )
    raise Exception ( 'r8vec2_header_read - Fatal error!' )

  m = file_row_count ( filename )

  return m

def r8vec2_header_read_test ( ):

#*****************************************************************************80
#
## r8vec2_header_read_test tests r8vec2_header_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_header_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_header_read counts rows in a file containing an R8VEC2.' )

  filename = 'r8vec2_write_test.txt'
  m = r8vec2_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows.' % ( filename, m ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_header_read_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_print ( a1, a2, title ):

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
#    20 June 2020
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
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 June 2020
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
  print ( '  r8vec2_print() prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( v, w, '  Print a pair of R8VEC\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_write ( filename, n, a, b ):

#*****************************************************************************80
#
## r8vec2_write writes an R8VEC2 to a file.
#
#  Discussion:
#
#    An R8VEC2 is a pair of vectors of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer N, the number of entries in A.
#
#    real A(N), B(N), the vectors.
#
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g  %g\n' % ( a[i], b[i] )
    output.write ( s )

  output.close ( )

  return

def r8vec2_write_test ( ):

#*****************************************************************************80
#
## r8vec2_write_test tests r8vec2_write.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_write_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test r8vec2_write, which writes an R8VEC2 to a file.' )

  filename = 'r8vec2_write_test.txt'
  n = 5
  a = np.array ( [ 1.1, 1.2, 1.3, 1.4, 1.5 ] )
  b = np.array ( [ 1.2, 2.2, 3.2, 4.2, 5.2 ] )
  r8vec2_write ( filename, n, a, b )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_write_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_data_read ( filename, m ):

#*****************************************************************************80
#
## r8vec_data_read reads the data from an R8VEC.
#
#  Discussion:
#
#    An R8VEC is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#    integer M, the number of rows in the file.
#
#  Output:
#
#    real TABLE(M), the data.
#
  import numpy as np

  j = -1

  input = open ( filename, 'r' )

  table = np.zeros ( m )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      table[i] = float ( line.strip() )
      i = i + 1

  input.close ( )

  return table

def r8vec_data_read_test ( ):

#*****************************************************************************80
#
## r8vec_data_read_test tests r8vec_data_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8vec_data_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_data_read reads data from an R8VEC.' )

  m = 5
  n = 3
  filename = 'r8vec_write_test.txt'
  a = r8vec_data_read ( filename, m )
  r8vec_print ( m, a, '  Data read from file:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_data_read_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_header_read ( filename ):

#*****************************************************************************80
#
## r8vec_header_read reads the header from an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#  Output:
#
#    integer M, the number of rows in the file.
#
  m = file_row_count ( filename )

  return m

def r8vec_header_read_test ( ):

#*****************************************************************************80
#
## r8vec_header_read_test tests r8vec_header_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_header_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_header_read counts rows in a file' )
  print ( '  containing an R8VEC.' )

  filename = 'r8vec_write_test.txt'
  m = r8vec_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows.' % ( filename, m ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_header_read_test:' )
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

  return

def r8vec_print_test ( ):

#*****************************************************************************80
#
## r8vec_print_test tests r8vec_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2021
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
  print ( '  Test r8vec_print(), which prints an R8VEC.' )
#
#  Use r8vec_print:
#
  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  label = '  Use r8vec_print():'
  r8vec_print ( n, v, label )
#
#  Use Python print()
#
  print ( '' )
  print ( '  Use python print():' )
  print ( '' )
  print ( v )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_write ( filename, n, a ):

#*****************************************************************************80
#
## r8vec_write writes an R8VEC to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer N, the number of entries in A.
#
#    real A(N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g\n' % ( a[i] )
    output.write ( s )

  output.close ( )

  return

def r8vec_write_test ( ):

#*****************************************************************************80
#
## r8vec_write_test tests r8vec_write.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_write_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test r8vec_write, which writes an R8VEC to a file.' )
  filename = 'r8vec_write_test.txt'
  n = 5
  a = np.array ( ( 1.1, 2.2, 3.3, 4.4, 5.5 ) )
  r8vec_write ( filename, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_write_test:' )
  print ( '  Normal end of execution.' )
  return

def table_io_test ( ):

#*****************************************************************************80
#
## table_io_test() tests table_io().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'table_io_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test table_io().' )

  file_column_count_test ( )
  file_row_count_test ( )

  i4_log_10_test ( )

  i4mat_indicator_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )

  i4vec_print_test ( )

  r8mat_indicator_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )

  r8vec_print_test ( )
#
#  Write an I4MAT to a file, then read header and data.
#
  i4mat_write_test ( )
  i4mat_header_read_test ( )
  i4mat_data_read_test ( )
#
#  Write an I4VEC to a file, then read header and data.
#
  i4vec_write_test ( )
  i4vec_header_read_test ( )
  i4vec_data_read_test ( )
#
#  Write an R8MAT transposed to a file.
#
  r8mat_transpose_write_test ( )
#
#  Write an R8MAT to a file, then read header and data.
#
  r8mat_write_test ( )
  r8mat_header_read_test ( )
  r8mat_data_read_test ( )
#
#  Write an R8VEC to a file, then read header and data.
#
  r8vec_write_test ( )
  r8vec_header_read_test ( )
  r8vec_data_read_test ( )
#
#  Write an R8VEC2 to a file, then read header and data.
#
  r8vec2_write_test ( )
  r8vec2_header_read_test ( )
  r8vec2_data_read_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'table_io_test():' )
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
  table_io_test ( )
  timestamp ( )

