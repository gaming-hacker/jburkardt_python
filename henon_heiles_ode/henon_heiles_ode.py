#! /usr/bin/env python3
#
def euler ( dydt, tspan, y0, n ):

#*****************************************************************************80
#
## euler() approximates the solution to an ODE using Euler's method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function dydt: points to a function that evaluates the right
#    hand side of the ODE.
#
#    real tspan[2]: contains the initial and final times.
#
#    real y0[m]: an array containing the initial condition.
#
#    integer n: the number of steps to take.
#
#  Output:
#
#    real t[n+1], y[n+1,m]: the times and solution values.
#
  import numpy as np

  if ( np.ndim ( y0 ) == 0 ):
    m = 1
  else:
    m = len ( y0 )

  tfirst = tspan[0]
  tlast = tspan[1]
  dt = ( tlast - tfirst ) / n
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )
  t[0] = tspan[0]
  y[0,:] = y0

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] + dt * ( dydt ( t[i], y[i,:] ) )

  return t, y

def henon_heiles_choose_xp ( e, lam, x, y, yp ):

#*****************************************************************************80
#
## henon_heiles_choose_xp(): consistent initial condition for Henon Heiles ODE.
#
#  Discussion:
#
#    It must be the case that 0 <= 2e-yp^2-x^2-y^2-2x^2y+2y^3/3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michel Henon, Carl Heiles,
#    The applicability of the third integral of motion: 
#    Some numerical experiments,
#    The Astronomical Journal,
#    Volume 69, pages 73-79, 1964.
#
#  Input:
#
#    real E: proposed initial energy.
#
#    real LAM: a parameter.
#
#    real X, Y, YP: proposed initial values for three coordinates.
#
#  Output:
#
#    real XP: a value which gives a consistent initial condition.
#
  import numpy as np

  xpsq = 2.0 * e - yp**2 - x**2 - y**2 \
    - 2.0 * lam * ( x**2 * y - y**3 / 3.0 )

  if ( xpsq < 0.0 ):
    print ( 'henon_heiles_choose_xp - Fatal error!' )
    print ( '  2e-yp^2-x^2-y^2-2x^2y+2y^3/3 < 0' )

  xp = np.sqrt ( xpsq )

  return xp

def henon_heiles_conserved ( w ):

#*****************************************************************************80
#
## henon_heiles_conserved() evaluates conserved quantities for the Henon Heiles ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michel Henon, Carl Heiles,
#    The applicability of the third integral of motion: 
#    Some numerical experiments,
#    The Astronomical Journal,
#    Volume 69, pages 73-79, 1964.
#
#  Input:
#
#    real W(N,4): the current coordinates.
#
#  Output:
#
#    real H(N): the conserved quantities.
#
  e, lam, t0, w0, tstop = henon_heiles_parameters ( )

  x =  w[:,0]
  xp = w[:,1]
  y =  w[:,2]
  yp = w[:,3]

  h = 0.5 * ( xp**2 + yp**2 ) + 0.5 * ( x**2 + y**2 ) \
    + lam * ( x**2 * y - y**3 / 3.0 )

  return h

def henon_heiles_deriv ( t, w ):

#*****************************************************************************80
#
## henon_heiles_deriv() evaluates the derivative of the Henon Heiles ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michel Henon, Carl Heiles,
#    The applicability of the third integral of motion: 
#    Some numerical experiments,
#    The Astronomical Journal,
#    Volume 69, pages 73-79, 1964.
#
#  Input:
#
#    real T, W(4): the arguments of the derivative.
#
#  Output:
#
#    real DWDT(4): the value of the derivative.
#
  import numpy as np

  e, lam, t0, w0, tstop = henon_heiles_parameters ( )

  x =  w[0]
  xp = w[1]
  y =  w[2]
  yp = w[3]

  dxdt = xp
  dxpdt = - x - 2.0 * lam * x * y
  dydt = yp
  dypdt = - y - lam * ( x**2 - y**2 )

  dwdt = np.array ( [ dxdt, dxpdt, dydt, dypdt ] )

  return dwdt

def henon_heiles_euler ( n ):

#*****************************************************************************80
#
## henon_heiles_euler() uses euler() to solve the Henon Heiles problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2020
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'henon_heiles_euler():' )
  print ( '  Use euler to solve the Henon Heiles problem.' )

  e, lam, t0, w0, tstop = henon_heiles_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  t, w = euler ( henon_heiles_deriv, tspan, w0, n )
#
#  Make plots.
#
  plt.plot ( t, w[:,0], 'r-', linewidth = 2 )
  plt.plot ( t, w[:,1], 'g-', linewidth = 2 )
  plt.plot ( t, w[:,2], 'b-', linewidth = 2 )
  plt.plot ( t, w[:,3], 'm-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  p,q  --->' )
  plt.title ( 'euler: Henon Heiles Time Plot' )
  plt.legend ( ( 'X', 'X\'', 'Y', 'Y\'' ) )
  filename = 'henon_heiles_euler_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( w[:,0], w[:,2] )
  plt.grid ( True )
  plt.xlabel ( '<---  q1  --->' )
  plt.ylabel ( '<---  q2  --->' )
  plt.title ( 'euler: Henon Heiles Orbit' )
  filename = 'henon_heiles_euler_orbit.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = henon_heiles_conserved ( w )

  plt.plot ( t, h, 'r-', linewidth = 3 )
  plt.plot ( [ tspan[0], tspan[1] ], [0.0, 0.0 ], 'k-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- H(T) -->' )
  plt.title ( 'euler: H(T) conservation' )
  filename = 'henon_heiles_euler_conserved.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def henon_heiles_ode_test ( ):

#*****************************************************************************80
#
## henon_heiles_ode_test() solves the henon heiles ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'henon_heiles_ode_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test henon_heiles_ode using various ODE solvers.' )

  e, lam, t0, w0, tstop = henon_heiles_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    e     = ', e )
  print ( '    lam   = ', lam )
  print ( '    t0    = ', t0 )
  print ( '    w0    = (%g,%g,%g,%g)' \
    % ( w0[0], w0[1], w0[2], w0[3] ) )
  print ( '    tstop = ', tstop )

  n = 10000
  henon_heiles_euler ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'henon_heiles_ode_test:' )
  print ( '  Normal end of execution.' )
  return

def henon_heiles_parameters ( ):

#*****************************************************************************80
#
## henon_heiles_parameters() returns parameters for the henon heiles ODE.
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
#    real E: the initial energy.
#
#    real LAM: a parameter.
#
#    real T0: the initial time.
#
#    real W0(4): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  e = 0.05
  lam = 1.0
  t0 = 0.0
  x = 0.0
  y = 0.0
  yp = 0.0
  xp = henon_heiles_choose_xp ( e, lam, x, y, yp )
  w0 = np.array ( [ x, xp, y, yp ] )
  tstop = 30.0

  return e, lam, t0, w0, tstop

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
  henon_heiles_ode_test ( )
  timestamp ( )

