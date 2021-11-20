#! /usr/bin/env python3
#
def pendulum_conserved ( y ):

#*****************************************************************************80
#
## pendulum_conserved() returns a conserved quantity for the pendulum ODE.
#
#  Discussion:
#
#    This conserved quantity can be regarded as the total energy of
#    the system.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Y(:,2): the current solution.
#
#  Output:
#
#    real H(:): the value of the conserved quantity.
#
  import numpy as np

  u = y[0]
  v = y[1]

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  h = 0.5 * m * g * l * u**2 + 0.5 * m * v**2

  return h

def pendulum_deriv ( t, y ):

#*****************************************************************************80
#
## pendulum_deriv() returns the right hand side of the linear pendulum ODE.
#
#  Discussion:
#
#    Y1 is the angular displacement
#    Y2 is the angular velocity
#
#    G is the gravitational coefficient.
#    L is the length of the pendulum.
#    M is the pendulum mass.
#
#    u' = v
#    v' = - ( g / l ) * u
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the current time.
#
#    real Y(2), the current state values.
#
#  Output:
#
#    real dydt(2), the time derivatives of the current state values.
#
  import numpy as np

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  u = y[0]
  v = y[1]

  dudt = v
  dvdt = - ( g / l ) * u

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def pendulum_exact ( t ):

#*****************************************************************************80
#
## pendulum_exact() returns the exact solution for the pendulum ODE.
#
#  Discussion:
#
#    This solution satisfies the pendulum ODE:
#
#    u' = v
#    v' = - sqrt ( g / l ) * u
#
#    u(t0) = u0 = y0(1)
#    v(t0) = v0 = y0(2)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:): the current time.
#
#  Output:
#
#    real Y(2): the exact solution.
#
  import numpy as  np

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  p = np.sqrt ( g / l )

  u =               y0[0] * np.cos ( p * ( t - t0 ) ) \
    + ( 1.0 / p ) * y0[1] * np.sin ( p * ( t - t0 ) )

  v =       - p   * y0[0] * np.sin ( p * ( t - t0 ) ) \
    +               y0[1] * np.cos ( p * ( t - t0 ) )

  y = np.array ( [ u, v ] )

  return y

def pendulum_ode_test ( ):

#*****************************************************************************80
#
## pendulum_ode_test() tests pendulum_ode.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2021
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pendulum_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve the pendulum ODE.' )

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  p = pendulum_period ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    gravity (m/s^2) = ', g )
  print ( '    length (m)      = ', l )
  print ( '    mass (g)        = ', m )
  print ( '    t0 (s)          = ', t0 )
  print ( '    u0 (rad)        = ', y0[0] )
  print ( '    v0 (rad/s)      = ', y0[1] )
  print ( '    tstop (s)       = ', tstop )
  print ( '    p (s)           = ', p )

  pendulum_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pendulum_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def pendulum_parameters ( ):

#*****************************************************************************80
#
## pendulum_parameters() returns parameters for the pendulum ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real G: the gravitational constant, in meters/second^2
#
#    real L: the pendulum length in meters
#
#    real M: the pendulum mass, in grams.
#
#    real T0: the initial time, in seconds
#
#    real Y0(2): the initial values, in radians, and radians per second.
#
#    real TSTOP: the final time, in seconds.
#
  import numpy as np

  m = 1.0
  g = 9.8
  l = 1.0
  m = 1.0
  t0 = 0.0
  u0 = np.pi / 3.0
  v0 = 0.0
  y0 = np.array ( [ u0, v0 ] )
  tstop = 20.0

  return g, l, m, t0, y0, tstop

def pendulum_period ( ):

#*****************************************************************************80
#
## pendulum_period() returns the period for the pendulum ODE.
#
#  Discussion:
#
#    The period is the smallest time interval P such that, for any T and X,
#      Y(T,X) = Y(T+P,X)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real P: the period of the pendulum.
#
  import numpy as np

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  p = 2.0 * np.pi * np.sqrt ( l / g )

  return p

def pendulum_solve_ivp ( ):

#*****************************************************************************80
#
## pendulum_solve_ivp() tests pendulum_ode using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'pendulum_solve_ivp:' )
  print ( '  Test pendulum_ode using solve_ivp.' )

  g, l, m, t0, y0, tstop = pendulum_parameters ( )

  f = pendulum_deriv
  tspan = np.array ( [ t0, tstop ] )
  n = 101
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  ye = pendulum_exact ( t )
#
#  Plot u = theta.
#
  plt.plot ( t, sol.y[0], 'ro', \
             t, ye[0], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Angular deflection (radians) -->' )
  plt.title ( 'Linear pendulum, theta: solve_ivp' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'pendulum_solve_ivp_theta.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot v = thetadot.
#
  plt.plot ( t, sol.y[1], 'ro', \
             t, ye[1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Angular velocity (radians/sec) -->' )
  plt.title ( 'Linear pendulum, thetadot: solve_ivp' )
  plt.legend ( ( 'solve_ivp', 'exact' ) )
  filename = 'pendulum_solve_ivp_thetadot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot energy.
#
  h = pendulum_conserved ( sol.y )

  plt.plot ( t, h, 'b-', linewidth = 2 )
  plt.plot ( np.array ( [ t0, tstop ] ), np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  plt.title ( 'Energy conservation: solve_ivp' )
  filename = 'pendulum_solve_ivp_energy.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

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
  pendulum_ode_test ( )
  timestamp ( )

