#! /usr/bin/env python3
#
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

def r8st_header_print ( i_min, i_max, j_min, j_max, m, n, nst ):

#*****************************************************************************80
#
## r8st_header_print prints the header of an R8ST file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I_MIN, I_MAX, the minimum and maximum rows.
#
#    integer J_MIN, J_MAX, the minimum and maximum columns.
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NST, the number of nonzeros.
#
  print ( '' )
  print ( '  Sparse Triplet header:' )
  print ( '' )
  print ( '  Minimum row index I_MIN = %d' % ( i_min ) )
  print ( '  Maximum row index I_MAX = %d' % ( i_max ) )
  print ( '  Minimum col index J_MIN = %d' % ( j_min ) )
  print ( '  Maximum col index J_MAX = %d' % ( j_max ) )
  print ( '  Number of rows        M = %d' % ( m ) )
  print ( '  Number of columns     N = %d' % ( n ) )
  print ( '  Number of nonzeros  NST = %d' % ( nst ) )

  return

def r8st_header_print_test ( ):

#*****************************************************************************80
#
## r8st_header_print_test() tests r8st_header_print.
#
#  Discussion:
#
#    The matrix is:
#
#      11  12   0   0  15
#      21  22   0   0   0
#       0   0  33   0  35
#       0   0   0  44   0
#      51   0  53   0  55
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 5
  nst = 11
  ast = np.array ( [ 51.0, 12.0, 11.0, 33.0, 15.0, 53.0, 55.0, 22.0, 35.0, 44.0, 21.0 ] )
  ist = np.array ( [ 5, 1, 1, 3, 1, 5, 5, 2, 3, 4, 2 ] )
  jst = np.array ( [ 1, 2, 1, 3, 5, 3, 5, 2, 5, 4, 1 ] )

  print ( '' )
  print ( 'r8st_header_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8st_header_print prints the header of an R8ST matrix.' )

  i_min = min ( ist )
  i_max = max ( ist )
  j_min = min ( jst )
  j_max = max ( jst )

  r8st_header_print ( i_min, i_max, j_min, j_max, m, n, nst )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8st_header_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8st_print ( m, n, nst, ist, jst, ast, title ):

#*****************************************************************************80
#
## r8st_print prints an R8ST matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NST, the number of nonzeros.
#
#    integer IST(NST), JST(NST), the row and column indices.
#
#    real AST(NST), the nonzero values.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '  %d rows by %d columns' % ( m, n ) )
  print ( '' );

  for k in range ( 0, nst ):
    print ( '  %8d  %8d  %8d  %16.8f' % ( k, ist[k], jst[k], ast[k] ) )

  return

def r8st_print_test ( ):

#*****************************************************************************80
#
## r8st_print_test() tests r8st_print.
#
#  Discussion:
#
#    The matrix is:
#
#      11  12   0   0  15
#      21  22   0   0   0
#       0   0  33   0  35
#       0   0   0  44   0
#      51   0  53   0  55
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 5
  nst = 11
  ast = np.array ( [ 51.0, 12.0, 11.0, 33.0, 15.0, 53.0, 55.0, 22.0, 35.0, 44.0, 21.0 ] )
  ist = np.array ( [ 5, 1, 1, 3, 1, 5, 5, 2, 3, 4, 2 ] )
  jst = np.array ( [ 1, 2, 1, 3, 5, 3, 5, 2, 5, 4, 1 ] )

  print ( '' )
  print ( 'r8st_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8st_print print an R8ST matrix.' )

  r8st_print ( m, n, nst, ist, jst, ast, '  R8ST Matrix data:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8st_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8st_print_some ( row1, row2, col1, col2, nst, ist, jst, ast, title ):

#*****************************************************************************80
#
## r8st_print_some prints some of an R8ST file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ROW1, ROW2, the first and last rows to print.
#
#    integer COL1, COL2, the first and last columns to print.
#
#    integer NST, the number of nonzeros.
#
#    integer IST(NST), COL(NST), the row and column indices.
#
#    real A(NST), the nonzero values.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )

  for k in range ( 0, nst ):
    if ( row1 <= ist[k] and ist[k] <= row2 and col1 <= jst[k] and jst[k] <= col2 ):
      print ( '  %8d  %8d  %8d  %16.8f' % ( k, ist[k], jst[k], ast[k] ) )

  return

def r8st_print_some_test ( ):

#*****************************************************************************80
#
## r8st_print_some_test() tests r8st_print_some.
#
#  Discussion:
#
#    The matrix is:
#
#      11  12   0   0  15
#      21  22   0   0   0
#       0   0  33   0  35
#       0   0   0  44   0
#      51   0  53   0  55
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 5
  nst = 11
  ast = np.array ( [ 51.0, 12.0, 11.0, 33.0, 15.0, 53.0, 55.0, 22.0, 35.0, 44.0, 21.0 ] )
  ist = np.array ( [ 5, 1, 1, 3, 1, 5, 5, 2, 3, 4, 2 ] )
  jst = np.array ( [ 1, 2, 1, 3, 5, 3, 5, 2, 5, 4, 1 ] )

  print ( '' )
  print ( 'r8st_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8st_print_some prints some of an R8ST matrix.' )

  row1 = 3
  row2 = 4
  col1 = 3
  col2 = 5

  r8st_print_some ( row1, row2, col1, col2, nst, ist, jst, ast, '  R8ST Matrix data:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8st_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def r8st_data_read ( filename, m, n, nst ):

#*****************************************************************************80
#
## r8st_data_read reads the data of an R8ST file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file.
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NST, the number of nonzeros.
#
#  Output:
#
#    integer IST(NST), JST(NST), the row and column indices.
#
#    real AST(NST), the nonzero values.
#
  import numpy as np

  ist = np.zeros ( nst, dtype = np.int32 )
  jst = np.zeros ( nst, dtype = np.int32 )
  ast = np.zeros ( nst, dtype = np.float64 )

  input = open ( filename, 'r' )

  k = 0

  for line in input:

    word = line.strip().split()

    ist[k] = int ( word[0] )
    jst[k] = int ( word[1] )
    ast[k] = float ( word[2] )
    k = k + 1

  input.close ( )

  return ist, jst, ast

def r8st_header_read ( filename ):

#*****************************************************************************80
#
## r8st_header_read reads the header of an R8ST file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2018
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
#    integer I_MIN, I_MAX, the minimum and maximum rows.
#
#    integer J_MIN, J_MAX, the minimum and maximum columns.
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NST, the number of nonzeros.
#
  import numpy as np

  input = open ( filename, 'r' )

  nst = 0
  i_min = + np.inf
  i_max = - np.inf
  j_min = + np.inf
  j_max = - np.inf

  for line in input:

    word = line.strip().split()

    i = int ( word[0] )
    j = int ( word[1] )
    aij = float ( word[2] )

    nst = nst + 1
    i_min = min ( i_min, i )
    i_max = max ( i_max, i )
    j_min = min ( j_min, j )
    j_max = max ( j_max, j )

  input.close ( )

  m = i_max - i_min + 1
  n = j_max - j_min + 1

  return i_min, i_max, j_min, j_max, m, n, nst

def r8st_read_test ( ):

#*****************************************************************************80
#
## r8st_read_test() tests r8st_header_read, r8st_data_read.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  filename = 'kershaw_r8.st'

  print ( '' )
  print ( 'r8st_read_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8st_header_read reads the header from an R8ST file.' )
  print ( '  r8st_data_read reads the data from an R8ST file.' )
  print ( '' )
  print ( '  Read the data from "%s".' % ( filename ) )

  i_min, i_max, j_min, j_max, m, n, nst = r8st_header_read ( filename )

  r8st_header_print ( i_min, i_max, j_min, j_max, m, n, nst )

  ist, jst, ast = r8st_data_read ( filename, m, n, nst )

  r8st_print ( m, n, nst, ist, jst, ast, '  Sparse Triplet data from file' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8st_read_test:' )
  print ( '  Normal end of execution.' )
  return

def r8st_sort_a ( m, n, nst, ist, jst, ast ):

#*****************************************************************************80
#
## r8st_sort_a sorts the entries of an R8ST matrix by column.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NST, the number of nonzeros.
#
#    integer IST(NST), JST(NST), the row and column indices.
#
#    real AST(NST), the nonzero matrix values.
#
#  Output:
#
#    integer IST(NST), JST(NST), the sorted row and column indices.
#
#    real AST(NST), the sorted nonzero matrix values.
#

#
#  Initialize.
#
  i = 0
  indx = 0
  isgn = 0
  j = 0

  i1 = 0
  j1 = 0
  k0 = 0
  k1 = 0
  n1 = 0
#
#  Call the external heap sorter.
#
  while ( True ):

    indx, i, j, i1, j1, k0, k1, n1 = sort_heap_external ( nst, indx, isgn, \
      i1, j1, k0, k1, n1 )
#
#  Interchange the I and J objects.
#
    if ( 0 < indx ):

      rij    = ist[i]
      ist[i] = ist[j]
      ist[j] = rij

      cij    = jst[i]
      jst[i] = jst[j]
      jst[j] = cij

      aij    = ast[i]
      ast[i] = ast[j]
      ast[j] = aij
#
#  Compare the I and J objects.
#
    elif ( indx < 0 ):

      if ( jst[i] == jst[j] ):

        if ( ist[i] < ist[j] ):
          isgn = - 1
        elif ( ist[i] == ist[j] ):
          isgn = 0
        elif ( ist[j] < ist[i] ):
          isgn = + 1

      elif ( jst[i] < jst[j] ):

        isgn = - 1

      elif ( jst[j] < jst[i] ):

        isgn = + 1

    elif ( indx == 0 ):

      break

  return ist, jst, ast

def r8st_sort_a_test ( ):

#*****************************************************************************80
#
## r8st_sort_a_test() tests r8st_sort_a.
#
#  Discussion:
#
#    The matrix is:
#
#      11  12   0   0  15
#      21  22   0   0   0
#       0   0  33   0  35
#       0   0   0  44   0
#      51   0  53   0  55
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 5
  nst = 11
  ast = np.array ( [ 51.0, 12.0, 11.0, 33.0, 15.0, 53.0, 55.0, 22.0, 35.0, 44.0, 21.0 ] )
  ist = np.array ( [ 5, 1, 1, 3, 1, 5, 5, 2, 3, 4, 2 ] )
  jst = np.array ( [ 1, 2, 1, 3, 5, 3, 5, 2, 5, 4, 1 ] )

  print ( '' )
  print ( 'r8st_sort_a_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8st_sort_a sorts an R8ST matrix by columns.' )

  i_min = min ( ist )
  i_max = max ( ist )
  j_min = min ( jst )
  j_max = max ( jst )

  r8st_header_print ( i_min, i_max, j_min, j_max, m, n, nst )

  r8st_print ( m, n, nst, ist, jst, ast, '  Matrix data before sorting:' )

  ist, jst, ast = r8st_sort_a ( m, n, nst, ist, jst, ast )

  r8st_print ( m, n, nst, ist, jst, ast, '  Matrix data after sorting:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8st_sort_a_test:' )
  print ( '  Normal end of execution.' )
  return

def r8st_transpose ( m, n, nst, ist, jst, ast ):

#*****************************************************************************80
#
## r8st_transpose transposes an R8ST matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NST, the number of nonzeros.
#
#    integer IST(NST), JST(NST), the row and column indices.
#
#    real AST(NST), the nonzero values.
#
#  Output:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NST, the number of nonzeros (unchanged).
#
#    integer IST(NST), JST(NST), the row and column indices.
#
#    real AST(NST), the nonzero values (unchanged).
#
  t = m
  m = n
  n = t

  t = ist.copy ( )
  ist = jst.copy ( )
  jst = t.copy ( )

  return m, n, nst, ist, jst, ast

def r8st_transpose_test ( ):

#*****************************************************************************80
#
## r8st_transpose_test() tests r8st_transpose.
#
#  Discussion:
#
#    The matrix is:
#
#      11  12   0   0  15
#      21  22   0   0   0
#       0   0  33   0  35
#       0   0   0  44   0
#      51   0  53   0  55
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 5
  nst = 11
  ast = np.array ( [ 51.0, 12.0, 11.0, 33.0, 15.0, 53.0, 55.0, 22.0, 35.0, 44.0, 21.0 ] )
  ist = np.array ( [ 5, 1, 1, 3, 1, 5, 5, 2, 3, 4, 2 ] )
  jst = np.array ( [ 1, 2, 1, 3, 5, 3, 5, 2, 5, 4, 1 ] )

  print ( '' )
  print ( 'r8st_transpose_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8st_transpose transposes an R8ST matrix.' )

  r8st_print ( m, n, nst, ist, jst, ast, '  R8ST Matrix data:' )

  mt, nt, nstt, istt, jstt, astt = r8st_transpose ( m, n, nst, ist, jst, ast )

  r8st_print ( mt, nt, nstt, istt, jstt, astt, '  Transposed matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8st_transpose_test:' )
  print ( '  Normal end of execution.' )
  return

def r8st_write ( filename, m, n, nst, ist, jst, ast ):

#*****************************************************************************80
#
## r8st_write writes an R8ST file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file.
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NST, the number of nonzeros.
#
#    integer IST(NST), JST(NST), the row and column indices.
#
#    real AST(NST), the nonzero values.
#
  output = open ( filename, 'w' )

  for k in range ( 0, nst ):
    output.write ( '  %d  %d  %f\n' % ( ist[k], jst[k], ast[k] ) )

  output.close ( )

  return

def r8st_write_test ( ):

#*****************************************************************************80
#
## r8st_write_test() tests r8st_write.
#
#  Discussion:
#
#    The matrix is:
#
#      11  12   0   0  15
#      21  22   0   0   0
#       0   0  33   0  35
#       0   0   0  44   0
#      51   0  53   0  55
#
#    The index vectors are 1 based, and so have to be converted to
#    0-base before being written.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 5
  nst = 11
  ast = np.array ( [ 51.0, 12.0, 11.0, 33.0, 15.0, 53.0, 55.0, 22.0, 35.0, 44.0, 21.0 ] )
  ist = np.array ( [ 5, 1, 1, 3, 1, 5, 5, 2, 3, 4, 2 ] )
  jst = np.array ( [ 1, 2, 1, 3, 5, 3, 5, 2, 5, 4, 1 ] )

  filename = 'a5by5_r8.st'

  print ( '' )
  print ( 'r8st_write_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8st_write writes an R8ST file.' )

  ist[0:nst] = ist[0:nst] - 1
  jst[0:nst] = jst[0:nst] - 1

  i_min = min ( ist )
  i_max = max ( ist )
  j_min = min ( jst )
  j_max = max ( jst )

  r8st_header_print ( i_min, i_max, j_min, j_max, m, n, nst )

  r8st_print ( m, n, nst, ist, jst, ast, '  Sparse Triplet (ST) data:' )

  r8st_write ( filename, m, n, nst, ist, jst, ast )

  print ( '' )
  print ( '  Wrote the matrix data to "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8st_write_test:' )
  print ( '  Normal end of execution.' )
  return

def sort_heap_external ( n, indx,isgn, i1, j1, k0, k1, n1 ):

#*****************************************************************************80
#
## sort_heap_external externally sorts a list of items into ascending order.
#
#  Discussion:
#
#    The actual list of data is not passed to the routine.  Hence this
#    routine may be used to sort integers, reals, numbers, names,
#    dates, shoe sizes, and so on.  After each call, the routine asks
#    the user to compare or interchange two items, until a special
#    return value signals that the sorting is completed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf.
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the number of items to be sorted.
#
#    integer INDX, the main communication signal.
#    The user must set INDX to 0 before the first call.
#    Thereafter, the user should set the input value of INDX
#    to the output value from the previous call.
#
#    integer ISGN, results of comparison of elements I and J.
#    (Used only when the previous call returned INDX less than 0).
#    ISGN <= 0 means I is less than or equal to J
#    0 <= ISGN means I is greater than or equal to J.
#
#    integer I1, J1, K0, K1, N1, bookkeeping variables that
#    are used for bookkeeping.  The user should declare them, and pass the
#    output values from one call as input values on the next call.  The user
#    should not change these variables.
#
#  Output:
#
#    integer INDX, the main communication signal.
#    If INDX is
#
#      greater than 0, the user should:
#      * interchange items I and J
#      * call again.
#
#      less than 0, the user should:
#      * compare items I and J
#      * set ISGN = -1 if I < J, ISGN = +1 if J < I
#      * call again.
#
#      equal to 0, the sorting is done.
#
#    integer I, J, the indices of two items.
#    On return with INDX positive, elements I and J should be interchanged.
#    On return with INDX negative, elements I and J should be compared, and
#    the result reported in ISGN on the next call.
#
#    integer I1, J1, K0, K1, N1, bookkeeping variables.
#

#
#  INDX = 0: This is the first call.
#
  if ( indx == 0 ):
      
    k0 = ( n // 2 )
    k1 = ( n // 2 )
    n1 = n
#
#  INDX < 0: The user is returning the results of a comparison.
#
  elif ( indx < 0 ):

    if ( indx == -2 ):

      if ( isgn < 0 ):
        i1 = i1 + 1

      j1 = k1
      k1 = i1
      indx = -1
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    if ( 0 < isgn ):
      indx = 2
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    if ( k0 <= 1 ):

      if ( n1 == 1 ):
        i1 = 0
        j1 = 0
        indx = 0
      else:
        i1 = n1
        n1 = n1 - 1
        j1 = 1
        indx = 1

      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    k0 = k0 - 1
    k1 = k0
#
#  0 < INDX, the user was asked to make an interchange.
#
  elif ( indx == 1 ):

    k1 = k0

  while ( True ):

    i1 = 2 * k1

    if ( i1 == n1 ):
      j1 = k1
      k1 = i1
      indx = -1
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1
    elif ( i1 < n1 ):
      j1 = i1 + 1
      indx = -2
      i = i1 - 1
      j = j1 - 1
      return indx, i, j, i1, j1, k0, k1, n1

    if ( k0 <= 1 ):
      break

    k0 = k0 - 1
    k1 = k0

  if ( n1 == 1 ):
    i1 = 0
    j1 = 0
    indx = 0
    i = i1 - 1
    j = j1 - 1
  else:
    i1 = n1
    n1 = n1 - 1
    j1 = 1
    indx = 1
    i = i1 - 1
    j = j1 - 1

  return indx, i, j, i1, j1, k0, k1, n1

def sort_heap_external_test ( ):

#*****************************************************************************80
#
## sort_heap_external_test() tests sort_heap_external.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 20

  print ( '' )
  print ( 'sort_heap_external_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sort_heap_external sorts objects externally.' )

  a = np.random.random_integers ( 1, n, size = n )

  i4vec_print ( n, a, '  Unsorted array:' )

  indx = 0
  isgn = 0
  i1 = 0
  j1 = 0
  k0 = 0
  k1 = 0
  n1 = 0

  while ( True ):

    indx, i, j, i1, j1, k0, k1, n1 = sort_heap_external ( n, indx, \
      isgn, i1, j1, k0, k1, n1 )

    if ( indx < 0 ):
      isgn = 1
      if ( a[i] <= a[j] ):
        isgn = -1
    elif ( 0 < indx ):
      t    = a[i]
      a[i] = a[j]
      a[j] = t
    else:
      break

  i4vec_print ( n, a, '  Sorted array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'sort_heap_external_test:' )
  print ( '  Normal end of execution.' )
  return

def st_io_test ( ):

#*****************************************************************************80
#
## st_io_test() tests st_io().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'st_io_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test st_io().' )

  r8st_header_print_test ( )
  r8st_print_test ( )
  r8st_print_some_test ( )
  r8st_read_test ( )
  r8st_sort_a_test ( )
  r8st_transpose_test ( )
  r8st_write_test ( )
  sort_heap_external_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'st_io_test:' )
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
  st_io_test ( )
  timestamp ( )

