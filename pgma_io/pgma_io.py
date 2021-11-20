#! /usr/bin/python3
#
def pgma_io_test ( ):

#*****************************************************************************80
#
## pgma_io_test() tests pgma_io().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2021
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pgma_io_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test pgma_io()' )

  pgma_write_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pgma_io_test():' )
  print ( '  Normal end of execution.' )
  return

def pgma_write ( file_name, comment, width, height, maxval, gray ):

#*****************************************************************************80
#
## pgma_write() writes an ASCII PGM graphics file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILE_NAME, the name of the file.
#
#    string COMMENT, a comment, which may be empty ('');
#
#    integer WIDTH, HEIGHT, the width and height of the graphics image.
#
#    integer MAXVAL, the maximum allowed gray value.
#
#    integer GRAY[WIDTH,HEIGHT], gray values between 0 and MAXVAL.
#
  file_type = 'P2'

  file_handle = open ( file_name, 'wt' )
  file_handle.write ( "%s\n" % ( file_type ) ) 
  file_handle.write ( "#%s\n" % ( comment ) ) 
  file_handle.write ( "%d %d\n" % ( width, height ) ) 
  file_handle.write ( "%d\n" % ( maxval ) )

  for i in range ( height ):
    for j in range ( width ):
      file_handle.write ( " %d" % ( gray[i,j] ) ) 
    file_handle.write ( "\n" )

  file_handle.close ( )

  return

def pgma_write_test ( ):

#*****************************************************************************80
#
## pgma_write_test() tests pgma_write().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 May 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pgma_write_test():' )
  print ( '  pgma_write() writes an ASCII PGM graphics file.' )

  file_name = 'pgma_io.pgm'

  comment = 'Example ASCII PGM graphics file.'

  width = 24
  height = 7
  maxval = 255

  gray = np.array \
  ( [ \
    [ 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], \
    [ 0,  64,  64,  64,  64,   0,   0, 128, 128, 128, 128,   0,   0, 192, 192, 192, 192,   0,   0, 255, 255, 255, 255,   0], \
    [ 0,  64,   0,   0,   0,   0,   0, 128,   0,   0,   0,   0,   0, 192,   0,   0,   0,   0,   0, 255,   0,   0, 255,   0], \
    [ 0,  64,  64,  64,   0,   0,   0, 128, 128, 128,   0,   0,   0, 192, 192, 192,   0,   0,   0, 255, 255, 255, 255,   0], \
    [ 0,  64,   0,   0,   0,   0,   0, 128,   0,   0,   0,   0,   0, 192,   0,   0,   0,   0,   0, 255,   0,   0,   0,   0], \
    [ 0,  64,   0,   0,   0,   0,   0, 128, 128, 128, 128,   0,   0, 192, 192, 192, 192,   0,   0, 255,   0,   0,   0,   0], \
    [ 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]  \
  ] )

  pgma_write ( file_name, comment, width, height, maxval, gray )

  print ( '' )
  print ( '  Graphics data stored in file "%s".' % ( file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'pgma_write_test():' )
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
  pgma_io_test ( )
  timestamp ( )

