#! /usr/bin/python3
#
def pbmb_io_test ( ):

#*****************************************************************************80
#
## pbmb_io_test() tests pbmb_io().
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
  print ( 'pbmb_io_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test pbmb_io()' )

  pbmb_write_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pbmb_io_test:' )
  print ( '  Normal end of execution.' )
  return

def pbmb_write ( file_name, width, height, bits ):

#*****************************************************************************80
#
## pbmb_write() writes a binary PBM graphics file.
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
#  Input:
#
#    string FILE_NAME, the name of the file.
#
#    integer WIDTH, HEIGHT, the width and height of the graphics image.
#
#    integer BITS[WIDTH*HEIGHT], values of 0 or 1.
#
  import numpy as np

  pbm_header = f'P4 {width} {height}\n'

  file_handle = open ( file_name, 'wb' )

  file_handle.write ( bytearray ( pbm_header, 'ascii' ) ) 

  np.packbits ( bits, axis = -1 ).tofile ( file_handle )

  file_handle.close ( )

  return

def pbmb_write_test ( ):

#*****************************************************************************80
#
## pbmb_write_test() tests pbmb_write().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'pbmb_write_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pbmb_write() writes a binary PBM graphics file.' )

  file_name = 'pbmb_io.pbm'

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

  pbmb_write ( file_name, width, height, bits )

  print ( '' )
  print ( '  Graphics data stored in file "%s".' % ( file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'pbmb_write_test():' )
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
  pbmb_io_test ( )
  timestamp ( )

