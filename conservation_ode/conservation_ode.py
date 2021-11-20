#! /usr/bin/env python3
#
def conservation_ode_test ( ):

#*****************************************************************************80
#
## conservation_ode_test() tests conservation_ode().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 June 2021
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( 'conservation_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  conservation_ode() reports on the accuracy of an ODE solver' )
  print ( '  by monitoring the value of a quantity that should be conserved.' )

  pendulum_solve_ivp ( )
  predator_prey_solve_ivp ( )
  rigid_body_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'conservation_ode_test():' )
  print ( '  Normal end of execution.' )

  return

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
#
#  Plot u = theta.
#
  plt.plot ( t, sol.y[0], 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Angular deflection (radians) -->' )
  plt.title ( 'pendulum, solve ivp: theta' )
  filename = 'pendulum_solve_ivp_theta.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot v = thetadot.
#
  plt.plot ( t, sol.y[1], 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Angular velocity (radians/sec) -->' )
  plt.title ( 'pendulum, solve ivp: thetadot' )
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
  plt.plot ( tspan, np.array ( [ h[0], h[0] ] ), 'r--', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k--', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  plt.title ( 'pendulum, solve ivp: conservation ' )
  filename = 'pendulum_solve_ivp_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def predator_prey_conserved ( rf ):

#*****************************************************************************80
#
## predator_prey_conserved() evaluates a conserved quantity.
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
#    real RF[N,2]: the current solution variables, rabbits and foxes.
#
#  Output:
#
#    real H[N]: the value of the conserved quantity.
#
  import numpy as np

  r = rf[0]
  f = rf[1]

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  h = delta * r - gamma * np.log ( r ) + beta * f - alpha * np.log ( f )

  return h

def predator_prey_deriv ( t, rf ):

#*****************************************************************************80
#
## predator_prey_deriv() evaluates the right hand side of the system.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the current time.
#
#    real RF[2], the current solution variables, rabbits and foxes.
#
#  Output:
#
#    real DRFDT[2], the right hand side of the 2 ODE's.
#
  import numpy as np

  r = rf[0]
  f = rf[1]

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  drdt =   alpha * r - beta  * r * f
  dfdt = - gamma * f + delta * r * f

  drfdt = np.array ( [ drdt, dfdt ] )

  return drfdt

def predator_prey_parameters ( ):

#*****************************************************************************80
#
## predator_prey_parameters() returns parameter values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real ALPHA: a parameter value.
#
#    real BETA: a parameter value.
#
#    real GAMMA: a parameter value.
#
#    real DELTA: a parameter value.
#
#    real T0: the initial time.
#
#    real Y0[2]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  alpha = 2.0
  beta = 0.001
  gamma = 10.0
  delta = 0.002
  t0 = 0.0
  y0 = np.array ( [ 5000, 100 ] )
  tstop = 5.0

  return alpha, beta, gamma, delta, t0, y0, tstop

def predator_prey_solve_ivp ( ):

#*****************************************************************************80
#
## predator_prey_solve_ivp() solves the predator prey ODE using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 June 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'predator_prey_solve_ivp():\n' );
  print ( '  Solve the predator prey ODE system using solve_ivp().\n' );

  alpha, beta, gamma, delta, t0, y0, tstop = predator_prey_parameters ( )

  f = predator_prey_deriv
  tspan = np.array ( [ t0, tstop ] )
  n = 101
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  plt.plot ( t, sol.y[0], 'r-', linewidth = 2 )
  plt.plot ( t, sol.y[1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- Prey, Predators --->' )
  plt.legend ( ( 'Prey', 'Predators' ) )
  plt.title ( 'predator prey solve ivp: plot' )
  filename = 'predator_prey_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( sol.y[0], sol.y[1], 'ro', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'predator prey solve ivp: phase' )
  filename = 'predator_prey_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = predator_prey_conserved ( sol.y )

  plt.plot ( t, h, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [h[0], h[0]] ), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0,0.0] ), 'k--' )
  plt.grid ( True )
  plt.title ( 'predator prey solve ivp conservation ' )
  filename = 'predator_prey_solve_ivp_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def rigid_body_conserved ( xyz ):

#*****************************************************************************80
#
## rigid_body_conserved() evaluates conserved quantities for the rigid body ODE.
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
#  Reference:
#
#    Ernst Hairer,
#    Solving differential equations on manifolds,
#    Universite de Geneve,
#    June 2011.
#
#  Input:
#
#    real XYZ[:,3]: the current coordinates.
#
#  Output:
#
#    real H1[:], H2[]: the conserved quantities.
#
  import numpy as np

  i1, i2, i3, t0, xyz0, tstop = rigid_body_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  h1 = x**2 + y**2 + z**2

  h2 = x**2 / i1 + y**2 / i2 + z**2 / i3

  return h1, h2

def rigid_body_deriv ( t, xyz ):

#*****************************************************************************80
#
## rigid_body_deriv() evaluates the derivative of the rigid body ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer,
#    Solving differential equations on manifolds,
#    Universite de Geneve,
#    June 2011.
#
#    Ernst Hairer, Christian Lubich, Gerhard Wanner,
#    Geometric numerical integration,
#    Springer, 2006.
#
#  Input:
#
#    real T, XYZ[3]: the arguments of the derivative.
#
#  Output:
#
#    real DXYZDT[3]: the value of the derivative.
#
  import numpy as np

  i1, i2, i3, t0, xyz0, tstop = rigid_body_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  dxdt = ( 1.0 / i3 - 1.0 / i2 ) * z * y
  dydt = ( 1.0 / i1 - 1.0 / i3 ) * x * z
  dzdt = ( 1.0 / i2 - 1.0 / i1 ) * y * x

  dxyzdt = np.array ( [ dxdt, dydt, dzdt ] )

  return dxyzdt

def rigid_body_parameters ( ):

#*****************************************************************************80
#
## rigid_body_parameters() returns parameters for the rigid body ODE.
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
#    real I1: a moment of inertia.
#
#    real I2: a moment of inertia.
#
#    real I3: a moment of inertia.
#
#    real T0: the initial time.
#
#    real XYZ0(3): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  i1 = 1.6
  i2 = 1.0
  i3 = 2.0 / 3.0
  t0 = 0.0
  x0 = np.cos ( 0.9 )
  y0 = 0.0
  z0 = np.sin ( 0.9 )
  xyz0 = np.array ( [ x0, y0, z0 ] )
  tstop = 50.0

  return i1, i2, i3, t0, xyz0, tstop

def rigid_body_solve_ivp ( ):

#*****************************************************************************80
#
## rigid_body_solve_ivp() tests rigid_body_ode with solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib as mpl
  from mpl_toolkits.mplot3d import Axes3D
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'rigid_body_solve_ivp():' )
  print ( '  Solve rigid_body_ode using solve_ivp().' )
  print ( '  rigid_body_ode() models motion on the surface of a sphere.' )

  i1, i2, i3, t0, y0, tstop = rigid_body_parameters ( )

  f = rigid_body_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  plt.plot ( t, sol.y[0], linewidth = 3 )
  plt.plot ( t, sol.y[1], linewidth = 3 )
  plt.plot ( t, sol.y[2], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- X,Y,Z -->' )
  plt.title ( 'rigid body, solve ivp: (X(t),Y(t),Z(t))' )
  plt.legend ( ( 'X(t)', 'Y(t)', 'Z(t)' ) )
  filename = 'rigid_body_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  fig = plt.figure ( )
  ax = fig.gca ( projection = '3d' )
  ax.plot ( sol.y[0], sol.y[1], sol.y[2], linewidth = 3 )
  ax.grid ( True )
  ax.set_xlabel ( '<-- X -->' )
  ax.set_ylabel ( '<-- Y -->' )
  ax.set_zlabel ( '<-- Z -->' )
  ax.set_title ( 'rigid body, solve ivp: (x,y,z)(t)'  )
  filename = 'rigid_body_solve_ivp_plot3d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h1, h2 = rigid_body_conserved ( sol.y )

  plt.plot ( t, h1, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [h1[0],h1[0] ] ), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- H1(T) -->' )
  plt.title ( 'rigid_body solve ivp: H1(T)' )
  filename = 'rigid_body_solve_ivp_h1_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( t, h2, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [h2[0],h2[0] ] ), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- H2(T) -->' )
  plt.title ( 'rigid_body solve ivp: H2(T)' )
  filename = 'rigid_body_solve_ivp_h2_conservation.png'
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
  conservation_ode_test ( )
  timestamp ( )

