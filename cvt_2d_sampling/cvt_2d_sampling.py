#! /usr/bin/env python3
#
def cvt_2d_sampling ( g_num = 0, it_num = 0, s1d_num = 0 ):

#*****************************************************************************80
#
## cvt_2d_sampling() carries out the Lloyd algorithm in a 2D unit box.
#
#  Discussion:
#
#    This program is a variation of the CVT_2D_LLOYD method.
#
#    Instead of using an exact technique to determine the Voronoi
#    regions, it uses sampling.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G_NUM, the number of generators.
#    A value of 50 is reasonable.
#
#    integer IT_NUM, the number of CVT iterations.
#    A value of 20 or 50 might be reasonable.
#
#    integer S1D_NUM, the number of sample points to use
#    when estimating the Voronoi regions.
#    A value of 1,000 is too low.  A value of 1,000,000 is somewhat high.
#
  import numpy as np
  import matplotlib.pyplot as plt
  import platform
  from scipy.spatial import Delaunay
  from scipy.spatial import Voronoi
  from scipy.spatial import voronoi_plot_2d
  from scipy import argmin
  from scipy import inner

  print ( '' )
  print ( 'cvt_2d_sampling():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use sampling to approximate Lloyd\'s algorithm' )
  print ( '  in the 2D unit square.' )

  if ( g_num <= 0 ):
    prompt = '  Enter number of generators:  '
    inp = raw_input ( prompt )
    g_num = int ( inp )

  if ( it_num <= 0 ):
    prompt = '  Enter number of iterations:  '
    inp = raw_input ( prompt )
    it_num = int ( inp )

  if ( s1d_num <= 0 ):
    prompt = '  Enter number of sample points:  '
    inp = raw_input ( prompt )
    s1d_num = int ( inp )

  s_num = s1d_num * s1d_num

  print ( '' )
  print ( '  Number of generators is %d' % ( g_num ) )
  print ( '  Number of iterations is %d' % ( it_num ) )
  print ( '  Number of 1d samples is %d' % ( s1d_num ) )
  print ( '  Number of 2d samples is %d' % ( s_num ) )
#
#  Initialize the generators.
#
  gx = np.random.rand ( g_num )
  gy = np.random.rand ( g_num )
#
#  Generate a fixed grid of sample points.
#  Since MESHGRID's documentation is too obscure, let's just do it the hard way.
#
  s_1d = np.linspace ( 0.0, 1.0, s1d_num )
  sx = np.zeros ( s_num )
  sy = np.zeros ( s_num )
  s = np.zeros ( [ s_num, 2 ] )
  k = 0
  for j in range ( 0, s1d_num ):
    for i in range ( 0, s1d_num ):
      sx[k] = s_1d[i]
      sy[k] = s_1d[j]
      s[k,0] = s_1d[i]
      s[k,1] = s_1d[j]
      k = k + 1
#
#  Carry out the iteration.
#
#  ERROR: I want to plot log ( E ) and log ( GM ) every step.
#  I should initialize E and GM to NAN's, assuming that, like
#  MATLAB, they won't plot.
#
  step = np.zeros ( it_num )
  e = 1.0E-10 * np.ones ( it_num )
  gm = 1.0E-10 * np.ones ( it_num )

  for it in range ( 0, it_num ):

    step[it] = it
#
#  Compute the Delaunay triangle information T for the current nodes.
#  Since my version of NUMPY is too old, I can't use the STACK command
#  to combine two vectors into an array.
#
    g = np.zeros ( [ g_num, 2 ] )
    g[:,0] = gx[:]
    g[:,1] = gy[:]
    tri = Delaunay ( g )
#
#  Display the Voronoi cells.
#
    subfig1 = plt.subplot ( 2, 2, 1 )   
    vor = Voronoi ( g )
    voronoi_plot_2d ( vor, ax = subfig1 )
#
#  Display the Delaunay triangulation.
#
    subfig2 = plt.subplot ( 2, 2, 2 )
    plt.triplot ( gx, gy, tri.simplices.copy( ) )
    plt.plot ( gx, gy, 'o' )
#
#  For each sample point, find K, the index of the nearest generator.
#
    k = [ argmin ( [ inner ( gg - ss, gg - ss ) for gg in g ] ) for ss in s ]
#
#  For each generator, M counts the number of sample points it is nearest to.
#  Note that for a nonuniform density, we just set W to the density.
#
    w = np.ones ( s_num )
    m = np.bincount ( k, weights = w )
#
#  G is the average of the sample points it is nearest to.
#  Where M is zero, we shouldn't modify G.
#
    gx_new = np.bincount ( k, weights = sx )
    gy_new = np.bincount ( k, weights = sy )

    for i in range ( 0, g_num ):
      if ( 0 < m[i] ):
        gx_new[i] = gx_new[i] / float ( m[i] )
        gy_new[i] = gy_new[i] / float ( m[i] )
#
#  Compute the energy.
#
    e[it] = 0.0
    for i in range ( 0, s_num ):
      e[it] = e[it] + ( sx[i] - gx_new[k[i]] ) ** 2 \
                    + ( sy[i] - gy_new[k[i]] ) ** 2
#
#  Display the log of the energy.
#
    subfig3 = plt.subplot ( 2, 2, 3 )
    plt.plot ( step[0:it+1], np.log ( e[0:it+1] ), 'm-*', linewidth = 2 )
    plt.title ( 'Log (Energy)' )
    plt.xlabel ( 'Step' )
    plt.ylabel ( 'Energy' )
    plt.grid ( True )
#
#  Compute the generator motion.
#
    for i in range ( 0, g_num ):
      gm[it] = gm[it] + ( gx_new[i] - gx[i] ) ** 2 \
                      + ( gy_new[i] - gy[i] ) ** 2
#
#  Display the generator motion.
#
    subfig4 = plt.subplot ( 2, 2, 4 )
    plt.plot ( step[0:it+1], np.log ( gm[0:it+1] ), 'm-*', linewidth = 2 )
    plt.title ( 'Log (Average generator motion)' )
    plt.xlabel ( 'Step' )
    plt.ylabel ( 'Energy' )
    plt.grid ( True )
#
#  Put a title on the plot.
#
    super_title = 'Iteration ' + str ( it )
    plt.suptitle ( super_title )
#
#  Save the first and last plots.
#
    if ( it == 0 ):
      filename = 'initial.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "', filename, '"' )
    elif ( it == it_num - 1 ):
      filename = 'final.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "', filename, '"' )

    plt.show ( block = False )
    plt.close ( )
#
#  Update the generators.
#
    gx = gx_new
    gy = gy_new

  return

def cvt_2d_sampling_test ( ):

#*****************************************************************************80
#
## cvt_2d_sampling_test() tests cvt_2d_sampling().
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
  print ( 'cvt_2d_sampling_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test cvt_2d_sampling()' )

  cvt_2d_sampling ( 16, 20, 100 )
#
#  Terminate.
#
  print ( '' )
  print ( 'cvt_2d_sampling_test()' )
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
  cvt_2d_sampling_test ( )
  timestamp ( )

