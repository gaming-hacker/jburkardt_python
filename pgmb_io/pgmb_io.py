#! /usr/bin/python3
#
def pgmb_io_test ( ):

#*****************************************************************************80
#
## pgmb_io_test() tests pgmb_io().
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
  print ( 'pgmb_io_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test pgmb_io()' )

  pgmb_write_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pgmb_io_test():' )
  print ( '  Normal end of execution.' )
  return

def pgmb_write ( file_name, width, height, maxval, gray ):

#*****************************************************************************80
#
## pgmb_write() writes a binary PGM graphics file.
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
#    integer MAXVAL, the maximum allowed gray value.
#
#    integer GRAY[WIDTH*HEIGHT], values between 0 and MAXVAL.
#
  import numpy as np
  import struct

  file_handle = open ( file_name, 'wb' )
#
#  Set up the header.
#
  pgm_header = f'P5 {width} {height} {maxval}\n'
  file_handle.write ( bytearray ( pgm_header, 'ascii' ) ) 
#
#  Convert 2D array to 1D vector.
#
  grayV = np.reshape ( gray, width * height )
#
#  Pack entries of vector into a string of bytes, replacing each integer
#  as an unsigned 1 byte character.
#
  grayB = struct.pack ( '%sB' % len(grayV), *grayV )
  file_handle.write ( grayB )
 
  file_handle.close ( )

  return

def pgmb_write_test ( ):

#*****************************************************************************80
#
## pgmb_write_test() tests pgmb_write().
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
  import platform

  print ( '' )
  print ( 'pgmb_write_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pgmb_write() writes a binary PGM graphics file.' )

  file_name = 'pgmb_io.pgm'
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

  pgmb_write ( file_name, width, height, maxval, gray )

  print ( '' )
  print ( '  Graphics data stored in file "%s".' % ( file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'pgmb_write_test():' )
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
  pgmb_io_test ( )
  timestamp ( )

