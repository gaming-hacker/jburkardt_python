#! /usr/bin/env python3
#
def pendulum_nonlinear_conserved ( y ):

#*****************************************************************************80
#
## pendulum_nonlinear_conserved(): conserved quantity for the nonlinear pendulum ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2020
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

  g, l, m, t0, y0, tstop = pendulum_nonlinear_parameters ( )

  u = y[0]
  v = y[1]

  h = ( m * g / l ) * ( 1.0 - np.cos ( u ) ) + 0.5 * m * v**2

  return h

def pendulum_nonlinear_deriv ( t, y ):

#*****************************************************************************80
#
## pendulum_nonlinear_deriv(): right hand side of the nonlinear pendulum ODE.
#
#  Discussion:
#
#    Y1 is the angular displacement
#    Y2 is the angular velocity
#    L is the length of the pendulum (set to 1 here)
#    G is the gravitational coefficient (set to 9.8 here).
#
#    y1' = y2
#    y2' = - ( g / l ) * sin ( y1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2018
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
#    real DYDT(2), the time derivatives of the current state values.
#
  import numpy as np

  g, l, m, t0, y0, tstop = pendulum_nonlinear_parameters ( )

  u = y[0]
  v = y[1]

  dudt = v
  dvdt = - ( g / l ) * np.sin ( u )

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def pendulum_nonlinear_ode_test ( ):

#*****************************************************************************80
#
## pendulum_nonlinear_ode_test() tests pendulum_nonlinear_ode.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2020
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'pendulum_nonlinear_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test pendulum_nonlinear_ode using solve_ivp.' )

  g, l, m, t0, y0, tstop = pendulum_nonlinear_parameters ( )

  print ( '' )
  print ( '  Initial angular deflection = %g degrees' % ( y0[0] * 180 / np.pi ) )
  print ( '  Initial angular velocity = %g degrees/second' % ( y0[1] * 180 / np.pi ) )

  f = pendulum_nonlinear_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  yd = sol.y * 180.0 / np.pi
#
#  Plot theta, thetadot
#
  plt.plot ( t, yd[0], 'r-', linewidth = 2 )
  plt.plot ( t, yd[1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Theta, ThetaDot (degrees) -->' )
  plt.title ( 'Deflection of nonlinear pendulum.' )
  filename = 'pendulum_nonlinear_theta.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot energy.
#
  h = pendulum_nonlinear_conserved ( sol.y )

  plt.plot ( t, h, 'b-', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  plt.title ( 'nonlinear pendulum energy' )
  filename = 'pendulum_nonlinear_energy.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pendulum_nonlinear_ode_test:' )
  print ( '  Normal end of execution.' )
  return

def pendulum_nonlinear_parameters ( ):

#*****************************************************************************80
#
## pendulum_nonlinear_parameters(): parameters for the nonlinear pendulum ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2020
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
#    real TSTOP: the final time.
#
  import numpy as np

  m = 1.0
  g = 9.8
  l = 1.0
  m = 1.0
  t0 = 0.0
  u0 = 70.0 * np.pi / 180.0
  v0 = 0.0
  y0 = np.array ( [ u0, v0 ] )
  tstop = 50.0

  return g, l, m, t0, y0, tstop

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
  pendulum_nonlinear_ode_test ( )
  timestamp ( )

