#! /usr/bin/env python3
#
def biochemical_linear_conserved ( y ):

#*****************************************************************************80
#
## biochemical_linear_conserved() evaluates a quantity that should be conserved.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Angela Martiradonna, Gianpiero Colonna, Fasma Diele,
#    GeCo: Geometric conservative nonstandard schemesfor biochemical systems,
#    Applied Numerical Mathematics,
#    2019.
#
#  Input:
#
#    real Y(2): the current solution.
#
#  Output:
#
#    real H: the conserved quantity.
#
  h = y[0] + y[1]

  return h

def biochemical_linear_deriv ( t, y ):

#*****************************************************************************80
#
## biochemical_linear_deriv() evaluates the derivative of a linear biochemical ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Angela Martiradonna, Gianpiero Colonna, Fasma Diele,
#    GeCo: Geometric conservative nonstandard schemesfor biochemical systems,
#    Applied Numerical Mathematics,
#    2019.
#
#  Input:
#
#    real T, Y(2): the arguments of the derivative.
#
#  Output:
#
#    real DYDT(2): the value of the derivative.
#
  import numpy as np

  a, b, t0, y0, tstop = biochemical_linear_parameters ( )

  y1 = y[0]
  y2 = y[1]

  S = np.array ( [ \
    [ -1.0,  1.0 ],
    [  1.0, -1.0 ] ] )

  r = np.array ( [ a * y1, b * y2 ] )
  
  dydt = np.matmul ( S, r )

  return dydt

def biochemical_linear_exact ( t ):

#*****************************************************************************80
#
## biochemical_linear_exact() returns the exact solution of a linear biochemical ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Angela Martiradonna, Gianpiero Colonna, Fasma Diele,
#    GeCo: Geometric conservative nonstandard schemesfor biochemical systems,
#    Applied Numerical Mathematics,
#    2019.
#
#  Input:
#
#    real T: the current time.
#
#  Output:
#
#    real Y(2): the exact solution.
#
  import numpy as np

  a, b, t0, y0, tstop = biochemical_linear_parameters ( )

  y10 = y0[0]
  y20 = y0[1]

  y1 = y10 + ( 1.0 - np.exp ( - ( a + b ) * ( t - t0 ) ) ) \
    * ( - a * y10 + b * y20 ) / ( a + b )
  y2 = y20 + ( 1.0 - np.exp ( - ( a + b ) * ( t - t0 ) ) ) \
    * (   a * y10 - b * y20 ) / ( a + b )

  y = np.array ( [ y1, y2 ] )

  return y

def biochemical_linear_ode_test ( ):

#*****************************************************************************80
#
## biochemical_linear_ode_test() tests biochemical_linear_ode().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Local:
#
#    real A, B: parameters.
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'biochemical_linear_ode_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test biochemical_linear_ode.' )

  a, b, t0, y0, tstop = biochemical_linear_parameters ( )

  tspan = ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( biochemical_linear_deriv, \
    t_span = tspan, y0 = y0, t_eval = t )

  ye = biochemical_linear_exact ( t )

  plt.clf ( )
  plt.plot ( t, sol.y[0,:], 'ro', t, ye[0,:], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y1, y1exact  --->' )
  plt.title ( 'y1: Linear biochemical ode' )
  plt.legend ( ( 'y1', 'y1exact' ) )
  filename = 'biochemical_linear_ode_y1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.clf ( )
  plt.plot ( t, sol.y[1,:], 'ro', t, ye[1,:], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y2, y2exact  --->' )
  plt.title ( 'y2: Linear biochemical ode' )
  plt.legend ( ( 'y2', 'y2exact' ) )
  filename = 'biochemical_linear_ode_y2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'biochemical_linear_ode_test:' )
  print ( '  Normal end of execution.' )
  return

def biochemical_linear_parameters ( ):

#*****************************************************************************80
#
## biochemical_linear_parameters(): parameters for the biochemical linear ODE.
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
#    real A, B: parameters;
#
#    real T0: the initial time.
#
#    real Y0[2]: the initial condition at time T0.
#
#    real TSTOP: the final time.
#
  import numpy as np

  a = 1.0
  b = 1.0
  t0 = 0.0
  y0 = np.array ( [ 29.98, 9.98 ] )
  tstop = 13.0

  return a, b, t0, y0, tstop

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
  biochemical_linear_ode_test ( )
  timestamp ( )
