#! /usr/bin/env python3
#
def kepler_perturbed_conserved ( y ):

#*****************************************************************************80
#
## kepler_perturbed_conserved() evaluates the Hamiltonian of a perturbed Kepler ODE.
#
#  Discussion:
#
#    We consider a perturbed Kepler two-body gravitational problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 February 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer, Christian Lubich, Gerhard Wanner,
#    Geometric Numerical Integration:
#    Structure-Preserving Algorithms for Ordinary Differential Equations,
#    Springer, 2006,
#    ISSN: 0179-3632
#
#  Input:
#
#    real Y(4): the arguments of the Hamiltonian.
#
#  Output:
#
#    real H: the value of the Hamiltonian.
#
  import numpy as np

  q1 = y[0]
  q2 = y[1]
  p1 = y[2]
  p2 = y[3]

  h = 0.5 * ( p1**2 + p2**2 ) - 1.0 / np.sqrt ( q1**2 + q2**2 ) \
    - 0.005 / ( np.sqrt ( q1**2 + q2**2 ) )**3 / 2.0

  return h

def kepler_perturbed_deriv ( t, y ):

#*****************************************************************************80
#
## kepler_perturbed_deriv() evaluates the derivative of a perturbed Kepler ODE.
#
#  Discussion:
#
#    We consider a perturbed Kepler two-body gravitational problem.
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
#  Reference:
#
#    Ernst Hairer, Christian Lubich, Gerhard Wanner,
#    Geometric Numerical Integration:
#    Structure-Preserving Algorithms for Ordinary Differential Equations,
#    Springer, 2006,
#    ISSN: 0179-3632
#
#  Input:
#
#    real T, Y(4): the arguments of the derivative.
#
#  Output:
#
#    real DYDT(4): the value of the derivative.
#
  import numpy as np

  delta, e, t0, y0, tstop = kepler_perturbed_parameters ( )

  q1 = y[0]
  q2 = y[1]
  p1 = y[2]
  p2 = y[3]

  dq1dt = p1
  dq2dt = p2
  dp1dt =         - q1 / np.sqrt ( ( q1**2 + q2**2 )**3 ) \
          - delta * q1 / np.sqrt ( ( q1**2 + q2**2 )**5 )
  dp2dt =         - q2 / np.sqrt ( ( q1**2 + q2**2 )**3 ) \
          - delta * q2 / np.sqrt ( ( q1**2 + q2**2 )**5 )

  dydt = np.array ( [ dq1dt, dq2dt, dp1dt, dp2dt ] )

  return dydt

def kepler_perturbed_ode_test ( ):

#*****************************************************************************80
#
## kepler_perturbed_ode_test() tests kepler_perturbed_ode().
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'kepler_perturbed_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test kepler_perturbed_ode.' )

  delta, e, t0, y0, tstop = kepler_perturbed_parameters ( )

  f = kepler_perturbed_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Time plot.
#
  plt.plot ( t, sol.y[0], linewidth = 2 )
  plt.plot ( t, sol.y[1], linewidth = 2 )
  plt.plot ( t, sol.y[2], linewidth = 2 )
  plt.plot ( t, sol.y[3], linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y(1:4)  --->' )
  plt.title ( 'Perturbed Kepler Time Plot' )
  filename = 'kepler_perturbed_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Phase plot.
#
  plt.plot ( sol.y[0], sol.y[1], linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<---  y1  --->' )
  plt.ylabel ( '<---  y2  --->' )
  plt.title ( 'Perturbed Kepler Phase Plot' )
  filename = 'kepler_perturbed_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'kepler_perturbed_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def kepler_perturbed_parameters ( ):

#*****************************************************************************80
#
## kepler_perturbed_parameters: parameters for the perturbed Kepler ODE.
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
#  Output:
#
#    real DELTA: ?
#
#    real E: the orbital eccentricity
#
#    real T0: the initial time
#
#    real Y0(4): the initial values.
#
#    real TSTOP: the final time.
#
  import numpy as np

  delta = 0.015
  e = 0.6
  t0 = 0.0

  p0 = 1.0 - e
  p1 = 0.0
  q0 = 0.0
  q1 = np.sqrt ( ( 1.0 + e ) / ( 1.0 - e ) )
  y0 = np.array ( [ p0, p1, q0, q1 ] )
  tstop = 110.0

  return delta, e, t0, y0, tstop

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
  kepler_perturbed_ode_test ( )
  timestamp ( )

