#! /usr/bin/env python3
#
def brusselator_deriv ( t, xy ):

#*****************************************************************************80
#
## brusselator_deriv() defines the Brusselator ODE system.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Behold! The Brusselator!,
#    https://www.johndcook.com/blog/
#    Posted 07 February 2020.
#
#    Rene Lefever, Gregoire Nicholis,
#    Chemical instabilities and sustained oscillations,
#    Journal of Theoretical Biology,
#    Volume 30, Issue 2, February 1971, Pages 267-284.
#
#  Input:
#
#    real T, the current time.
#
#    real XY(2), the current solution variables.
#
#  Output:
#
#    real DXYDT(2), the right hand side of the 2 ODE's.
#
  import numpy as np

  a, b, t0, xy0, tstop = brusselator_parameters ( )

  x = xy[0]
  y = xy[1]

  dxdt = a + x * x * y - ( b + 1.0 ) * x
  dydt = b * x - x * x * y

  dxydt = np.array ( [ dxdt, dydt ] )

  return dxydt

def brusselator_ode_test ( ):

#*****************************************************************************80
#
## brusselator_ode_test() tests brusselator_ode().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Behold! The Brusselator!,
#    https://www.johndcook.com/blog/
#    Posted 07 February 2020.
#
#    Rene Lefever, Gregoire Nicholis,
#    Chemical instabilities and sustained oscillations,
#    Journal of Theoretical Biology,
#    Volume 30, Issue 2, February 1971, Pages 267-284.
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'brusselator_ode_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test brusselator_ode.' )

  a, b, t0, xy0, tstop = brusselator_parameters ( )

  plt.clf ( )

  for x0 in range ( 0, 6 ):
    for y0 in range ( 0, 4 ):
      xy0 = np.array ( [ x0, y0 ] )
      tspan = np.array ( [ t0, tstop ] )
      t = np.linspace ( t0, tstop, 101 )

      sol = solve_ivp ( brusselator_deriv, tspan, xy0, t_eval = t )

      plt.plot ( sol.y[0,:], sol.y[1,:] )

  plt.grid ( True );
  plt.xlabel ( '<---  x(t)  --->' )
  plt.ylabel ( '<---  y(t)  --->' )
  plt.title ( 'Brusselator phase plot' )
  filename = 'brusselator_ode_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'brusselator_ode_test:' )
  print ( '  Normal end of execution.' )
  return

def brusselator_parameters ( ):

#*****************************************************************************80
#
## brusselator_parameters() returns parameters for the brusselator ODE.
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
#    real A: a parameter.
#
#    real B: a parameter.
#
#    real T0: the initial time.
#
#    real XY0(2): the initial condition at time T0.
#
#    real TSTOP: the final time.
#
  import numpy as np

  a = 1.0
  b = 3.0
  t0 = 0.0
  xy0 = np.array ( [ 0.0, 0.0 ] )
  tstop = 10.0

  return a, b, t0, xy0, tstop

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
  brusselator_ode_test ( )
  timestamp ( )

