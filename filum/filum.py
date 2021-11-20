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
#    string FILENAME: the name of the file.
#
#  Output:
#
#    integer COLUMN_COUNT, the number of words in a typical column.
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
## file_column_count_test() tests file_column_count().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'file_column_count_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  file_column_count() counts "columns" in a text file line.' )

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

def filename_inc ( filename ):

#*****************************************************************************80
#
## filename_inc() generates the next filename in a series.
#
#  Discussion:
#
#    It is assumed that the digits in the name, whether scattered or
#    connected, represent a number that is to be increased by 1 on
#    each call.  If this number is all 9's on input, the output number
#    is all 0's.  Non-numeric letters of the name are unaffected..
#
#    If the name is empty, then the routine stops.
#
#    If the name contains no digits, the empty string is returned.
#
#  Example:
#
#      Input            Output
#      -----            ------
#      'a7to11.txt'     'a7to12.txt'  (typical case.  Last digit incremented)
#      'a7to99.txt'     'a8to00.txt'  (last digit incremented, with carry.)
#      'a9to99.txt'     'a0to00.txt'  (wrap around)
#      'cat.txt'        ' '           (no digits in input name.)
#      ' '              STOP!         (error.)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the string to be incremented.
#
#  Output:
#
#    string FILENAME, the incremented string.
#
  i0 = ord ( '0' )
  i8 = ord ( '8' )
  i9 = ord ( '9' )

  lens = len ( filename )

  if ( lens <= 0 ):
    return None

  change = 0
  filename2 = ''

  for i in range ( lens - 1, -1, -1 ):

    c = filename[i]

    ic = ord ( c )

    if ( change < 2 and i0 <= ic and ic <= i8 ):
      ic = ic + 1
      filename2 = chr ( ic ) + filename2
      change = 2
    elif ( change == 0 and ic == i9 ):
      change = 1
      c = '0'
      filename2 = c + filename2
    else:
      filename2 = c + filename2

  if ( change == 0 ):
    filename2 = None

  return filename2

def filename_inc_test ( ):

#*****************************************************************************80
#
## filename_inc_test() tests filename_inc().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'filename_inc_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  filename_inc() "increments" a string' )
  print ( '' )
  print ( '     Input             Output' )

  for i in range ( 0, 4 ):

    if ( i == 0 ):
      filename = 'file???.dat'
    elif ( i == 1 ):
      filename = 'file072.dat'
    elif ( i == 2 ):
      filename = '2cat9.dat  '
    elif ( i == 3 ):
      filename = 'fred99.txt '

    print ( '' )
    for j in range ( 0, 4 ):
      filename2 = filename_inc ( filename )
      print ( '  ', filename, ' ' , filename2 )
      filename = filename2
      if ( filename == None ):
        break

  return

def file_row_count ( filename ):

#*****************************************************************************80
#
## file_row_count() counts the number of rows (lines) in a file.
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
#    integer ROW_COUNT, the number of rows in the file.
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
## file_row_count_test() tests file_row_count().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'file_row_count_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  file_row_count() counts the rows in a text file.' )

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

def filum_test ( ):

#*****************************************************************************80
#
## filum_test() tests filum().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'filum_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test filum().' )

  file_column_count_test ( )
  file_row_count_test ( )
  filename_inc_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'filum_test:' )
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
#    21 August 2019
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
  filum_test ( )
  timestamp ( )

