#! /usr/bin/env python3
#
def rubber_band_deriv ( t, y ):

#*****************************************************************************80
#
## rubber_band_deriv() evaluates the right hand side of the rubber band ODE.
#
#  Discussion:
#
#    The original equation has the form:
#
#      y'' + 0.01 y' + a y(+) - b y(-) = 10 + lam sin ( mu t )
#
#    where y(+)=max(y,0) and y(-)=max(-y,0).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 April 2020
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt
#
#  Reference:
#
#    Lisa Humphreys, Ray Shammas,
#    Finding Unpredictable Behavior in a Simple Ordinary Differential Equation. 
#    The College Mathematics Journal, 
#    Volume 31, Number 5, November 2000, pages 338-346.
#
#    John D Cook,
#    A spring, a rubber band, and chaos
#    https://www.johndcook.com/blog/
#    26 April 2020.
#
#  Input
#
#    real T: the current time.
#
#    real Y(2): the current values of Y and Y'.
#
#  Output:
#
#    real DYDT(2): the current values of Y' and Y''.
#
  import numpy as np

  a, b, lam, mu, t0, y0, tstop = rubber_band_parameters ( )

  u = y[0]
  v = y[1]

  up = y[1]
  vp = 10.0 + lam * np.sin ( mu * t ) - 0.01 * v - a * max ( u, 0.0 ) \
    + b * max ( -u, 0.0 )
  
  dydt = np.array ( [ up, vp ] )

  return dydt

def rubber_band_ode_test ( ):

#*****************************************************************************80
#
## rubber_band_ode_test() solves the rubber band ODE using solve_ivp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 April 2020
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt
#
  import matplotlib.pyplot as plt
  import platform
  import numpy as np
  from scipy.integrate import solve_ivp

  print ( '' )
  print ( 'rubber_band_ode_test:' )
  print ( '  Use solve_ivp to solve the rubber band ODE.' )

  a, b, lam, mu, t0, y0, tstop = rubber_band_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 301 )
  
  sol = solve_ivp ( rubber_band_deriv, tspan, y0, t_eval = t )
#
#  Plot the result.
#
  plt.plot ( sol.t, sol.y[0], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( "<-- t -->" )
  plt.ylabel ( "<-- y(t) -->" )
  plt.title ( 'solve_ivp: rubber band ODE' )
  filename = 'rubber_band_ode.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'rubber_band_ode_test:' )
  print ( '  Normal end of execution.' )
  return

def rubber_band_parameters ( ):

#*****************************************************************************80
#
## rubber_band_parameters() returns parameters for the rubber band ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the coefficients of y+ and y-.
#
#    real LAM: the coefficient of the sinusoidal forcing term.
#
#    real MU: the coefficient of time in the sinusoidal forcing term.
#
#    real T0: the initial time.
#
#    real Y0(2): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  a = 17.0
  b = 1.0
  lam = 15.4
  mu = 0.75

  t0 = 0.0
  y0 = np.array ( [ 1.0, 0.0 ] )
  tstop = 100.0

  return a, b, lam, mu, t0, y0, tstop

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
  rubber_band_ode_test ( )
  timestamp ( )

