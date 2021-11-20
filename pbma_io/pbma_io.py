#! /usr/bin/python3
#
def pbma_io_test ( ):

#*****************************************************************************80
#
## pbma_io_test() tests pbma_io().
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
  print ( 'pbma_io_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test pbma_io()' )

  pbma_write_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pbma_io_test:' )
  print ( '  Normal end of execution.' )
  return

def pbma_write ( file_name, comment, width, height, bits ):

#*****************************************************************************80
#
## pbma_write() writes an ASCII PBM graphics file.
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
#    integer BITS[WIDTH,HEIGHT], bits values of 0 or 1.
#
  file_type = 'P1'

  file_handle = open ( file_name, 'wt' )
  file_handle.write ( "%s\n" % ( file_type ) ) 
  file_handle.write ( "#%s\n" % ( comment ) ) 
  file_handle.write ( "%d %d\n" % ( width, height ) ) 

  for i in range ( height ):
    for j in range ( width ):
      file_handle.write ( " %d" % ( bits[i,j] ) ) 
    file_handle.write ( "\n" )

  file_handle.close ( )

  return

def pbma_write_test ( ):

#*****************************************************************************80
#
## pbma_write_test() tests pbma_write().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 May 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pbma_write_test():' )
  print ( '  pbma_write() writes an ASCII PBM graphics file.' )

  file_name = 'pbma_io.pbm'

  comment = 'Example ASCII PBM graphics file.'

  width = 24
  height = 7

  bits = np.array \
  ( [ \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0 ], \
    [ 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0 ], \
    [ 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0 ], \
    [ 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ], \
    [ 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]  \
  ] )

  pbma_write ( file_name, comment, width, height, bits )

  print ( '' )
  print ( '  Graphics data stored in file "%s".' % ( file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'pbma_write_test():' )
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
  pbma_io_test ( )
  timestamp ( )

