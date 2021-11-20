#! /usr/bin/env python3
#
def delaunay_test ( ):

#*****************************************************************************80
#
## delaunay_test() tests delaunay() and triplot().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 October 2016
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import platform
  import numpy as np
  from scipy.spatial import Delaunay

  print ( '' )
  print ( 'DELAUNAY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  scipy.spatial.Delaunay computes the Delaunay triangulation of a set of points.' )
  print ( '  matplotlib.pyplot.triplot will plot it.' )
#
#  Select the points.
#
  nc = 25
  xy = np.random.random ( [ nc, 2 ] )
#
#  Compute the diagram.
#
  triangulation = Delaunay ( xy )
#
#  Plot the diagram.
#
  plt.triplot ( xy[:,0], xy[:,1], triangulation.simplices.copy ( ) )
#
#  Save the plot.
#
  filename = 'delaunay_test.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'DELAUNAY_TEST:' )
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
  import numpy as np
  timestamp ( )
  delaunay_test ( )
  timestamp ( )

