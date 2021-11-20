#! /usr/bin/env python3
#
def arenstorf_deriv ( t, xy ):

#*****************************************************************************80
#
## arenstorf_deriv() evaluates the right hand side of the Arenstorf ODE.
#
#  Discussion:
#
#    The Arenstorf ODE produces a stable periodic orbit for a three body 
#    problem involving the Earth, the Moon, and a spacecraft.
#
#    Although the orbit should be periodic, and repeats after a time interval
#    of a little more than 17 units, most ODE solvers will have difficulty
#    coming close to periodicity.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    The orbit that put men on the moon,
#    https://www.johndcook.com/blog/
#    Posted 08 February 2020.
#
#    Ernst Hairer, Syvert Norsett, Gerhard Wanner,
#    Solving Ordinary Differential Equations I: Nonstiff Problems,
#    Springer, 1987.
#
#  Input:
#
#    real T, XY(4): the time, and position and speed of the spacecraft.
#
#  Output:
#
#    real DXYDT(4): the value of the derivative.
#
  import numpy as np

  x = xy[0]
  y = xy[1]
  xp = xy[2]
  yp = xy[3]
#
#  mu1 = relative mass of moon, mu2 = relative mass of earth.
#
  mu1, mu2, t0, xy0, tstop = arenstorf_parameters ( )

  d1 = np.sqrt ( ( ( x + mu1 )**2 + y**2 )**3 )
  d2 = np.sqrt ( ( ( x - mu2 )**2 + y**2 )**3 )

  dxdt = xp
  dydt = yp
  dxpdt = x + 2.0 * yp - mu2 * ( x + mu1 ) / d1 - mu1 * ( x - mu2 ) / d2
  dypdt = y - 2.0 * xp - mu2 * y / d1 - mu1 * y / d2

  dxydt = np.array ( [ dxdt, dydt, dxpdt, dypdt ] )

  return dxydt

def arenstorf_ode_test ( ):

#*****************************************************************************80
#
## arenstorf_ode_test() tests arenstorf_ode().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import platform
  import numpy as np

  print ( '' )
  print ( 'arenstorf_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test arenstorf_ode().' )
#
#  Get the parameters.
#
  mu1, mu2, t0, xy0, tstop = arenstorf_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( arenstorf_deriv, tspan, xy0, t_eval = t )

  plt.plot ( sol.y[0], sol.y[1], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  q1  --->' )
  plt.ylabel ( '<---  q2  --->' )
  plt.title ( 'Arenstorf phase plot' )
  filename = 'arenstorf_ode_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'arenstorf_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def arenstorf_parameters ( ):

#*****************************************************************************80
#
## arenstorf_parameters() returns parameters for the arenstorf ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real MU1: the relative mass of the moon;
#
#    real MU2: the relative mass of the earth.
#
#    real T0: the initial time.
#
#    real XY0(4): the initial condition at time T0.
#
#    real TSTOP: the final time.
#
  import numpy as np

  mu1 = 0.012277471
  mu2 = 1.0 - mu1

  t0 = 0.0
  xy0 = np.array ( [ 0.994, 0.0, 0.0, -2.00158510637908252240537862224 ] )
  tstop = 17.0652165601579625588917206249

  return mu1, mu2, t0, xy0, tstop

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
  arenstorf_ode_test ( )
  timestamp ( )

