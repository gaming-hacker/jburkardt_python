#! /usr/bin/env python3
#
def snowfall_histogram ( ):

#*****************************************************************************80
#
## snowfall_histogram() plots a histogram of snowfall levels.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'snowfall_histogram:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a histogram of yearly snowfall levels.' )
#
#  Read the pairs from the file.
#
  filename = 'snowfall_data.txt'
  data = np.loadtxt ( filename )
  inches = data[:,9]

  m = len ( inches )
  print ( '' )
  print ( '  %d data records read from file.' % ( m ) )
#
#  Plot the data.
#
  plt.hist ( inches, rwidth = 0.95 )
  plt.grid ( True )
  plt.xlabel ( '<-- Yearly Snowfall (inches) -->', fontsize = 16 )
  plt.ylabel ( '<-- Frequency -->', fontsize = 16 )
  plt.title ( 'Yearly snowfall at Michigan Tech', fontsize = 16 )
#
#  Save the graphics in a file.
#
  filename = 'snowfall_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'snowfall_histogram:' )
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

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  snowfall_histogram ( )
  timestamp ( )
