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

def zombie_conserved ( y ):

#*****************************************************************************80
#
## zombie_conserved() returns a conserved quantity for the zombie ODE.
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
#  Input:
#
#    real Y(:,3): the current solution.
#
#  Output:
#
#    real H(:): the value of the conserved quantity.
#
  import numpy as np

  h = np.sum ( y, axis = 1 )

  return h

def zombie_deriv ( t, y ):

#*****************************************************************************80
#
## zombie_deriv() returns the right hand side of the zombie ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2020
#
#  Reference:
#
#    Philip Munz, Ioan Hudea, Joe Imad, Robert Smith,
#    When Zombies Attack!: Mathematical Modelling of an Outbreak
#    of Zombie Infection,
#    Infection Disease Modelling Progress, 
#    Editors: J M Tchuenche, C Chiyaka,
#    Nova Science Publishers, 2009.
#
#  Input:
#
#    real t: the current time.
#
#    real y(3): the current solution.
#
#  Output:
#
#    real dydt(3): the right hand side of the zombie ODE.
#
  import numpy as np

  alpha, beta, gamma, delta, t0, y0, tstop = zombie_parameters ( )

  s = y[0]
  z = y[1]
  r = y[2]

  dsdt = - beta * s * z                             - delta * s 
  dzdt =   beta * s * z - alpha * s * z + gamma * r
  drdt =                  alpha * s * z - gamma * r + delta * s

  dydt = np.array ( [ dsdt, dzdt, drdt ] )

  return dydt

def zombie_euler ( n ):

#*****************************************************************************80
#
## zombie_euler() uses the Euler method on the zombie epidemic.
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
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'zombie_euler:' )
  print ( '  Use the euler method on the zombie ODE.' )

  alpha, beta, gamma, delta, t0, y0, tstop = zombie_parameters ( )

  f = zombie_deriv
  tspan = np.array ( [ t0, tstop ] )

  t, y = euler ( f, tspan, y0, n )
#
#  Plot the solution.
#
  plt.plot ( t, y, linewidth = 2 )
  plt.xlabel ( '<--- Time --->' )
  plt.ylabel ( '<--- Population --->' )
  plt.title ( 'zombie euler: time plot' )
  plt.grid ( True )
  plt.legend ( ( 'Humans', 'Zombies', 'Suspended Zombies' ) )
  filename = 'zombie_euler_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot the conserved quantity.
#
  h = zombie_conserved ( y )

  p0 = np.sum ( y[0,:] )

  plt.plot ( t, h, 'b-', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'r--', linewidth= 2 )
  plt.plot ( tspan, np.array ( [ p0, p0 ] ), 'r--', linewidth = 2 )
  plt.xlabel ( '<--- Time --->' )
  plt.ylabel ( '<--- Total population --->' )
  plt.title ( 'zombie ode: population conservation' )
  plt.grid ( True )
  filename = 'zombie_euler_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def zombie_ode_test ( ):

#*****************************************************************************80
#
## zombie_ode_test tests zombie_ode.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'zombie_ode_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  zombie_ode models a zombie epidemic.' )

  alpha, beta, gamma, delta, t0, y0, tstop = zombie_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    alpha = ', alpha )
  print ( '    beta  = ', beta )
  print ( '    gamma = ', gamma )
  print ( '    delta = ', delta )
  print ( '    t0    = ', t0  )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  n = 2000
  zombie_euler ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'zombie_ode_test' )
  print ( '  Normal end of execution.' )
  return

def zombie_parameters ( ):

#*****************************************************************************80
#
## zombie_parameters() returns parameters for the zombie ode.
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
#    Philip Munz, Ioan Hudea, Joe Imad, Robert Smith,
#    When Zombies Attack!: Mathematical Modelling of an Outbreak
#    of Zombie Infection,
#    Infection Disease Modelling Progress, 
#    Editors: J M Tchuenche, C Chiyaka,
#    Nova Science Publishers, 2009.
#
#  Output:
#
#    real ALPHA: zombie destruction rate.
#
#    real BETA: new zombie rate.
#
#    real GAMMA: zombie resurrection rate.
#
#    real DELTA: background death rate.
#
#    real T0: the initial time.
#
#    real Y0(3): the initial populations of humans, zombies, and
#    suspended zombies.
#
#    real TSTOP: the final time.
#
  import numpy as np

  alpha = 0.008
  beta = 0.0095
  gamma = 0.02
  delta = 0.0001
  t0 = 0.0
  y0 = np.array ( [ 500.0, 0.0, 0.0 ] )
  tstop = 20.0

  return alpha, beta, gamma, delta, t0, y0, tstop

if ( __name__ == '__main__' ):
  timestamp ( )
  zombie_ode_test ( )
  timestamp ( )

