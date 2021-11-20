#! /usr/bin/env python3
#
def bulgaria_plot ( ):

#*****************************************************************************80
#
## bulgaria_plot() plots the population of Bulgaria over time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'bulgaria_plot():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot the population of Bulgaria over time.' )
#
#  Read the pairs "Year, Population" from the file.
#
  filename = 'bulgaria_data.txt'
  data = np.loadtxt ( filename )
#
#  Split data into separate year and population vectors.
#
  year = data[:,0]
  population = data[:,1]
#
#  Plot the data.
#
  plt.plot ( year, population, linewidth = 3, color = 'b' )
  plt.grid ( True )
  plt.xlabel ( '<--- Year --->', fontsize = 16 )
  plt.ylabel ( '<--- Population --->', fontsize = 16 )
  plt.title ( 'The Population of Bulgaria', fontsize = 16 )
  filename = 'bulgaria_plot.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'bulgaria_plot():' )
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
  bulgaria_plot ( )
  timestamp ( )
 
