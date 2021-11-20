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

def ripple_deriv ( t, y ):

#*****************************************************************************80
#
## ripple_deriv() evaluates the derivative of the ripple ODE.
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
#    John D Cook,
#    Ripples and Hyperbolas,
#    https://www.johndcook.com/blog/2020/11/06/ripples-and-hyperbolas/
#    Posted 06 November 2020.
#
#    Wendell Mills, Boris Weisfeiler, Allan Krall,
#    Discovering Theorems with a Computer: The Case of y‘ = sin(xy). 
#    The American Mathematical Monthly, 
#    Volume 86, Number 9, November 1979, pages 733-739.
#
#  Input:
#
#    real T, Y: the arguments of the derivative.
#
#  Output:
#
#    real DYDT: the value of the derivative.
#
  import numpy as np

  dydt = np.sin ( t * y )

  return dydt

def ripple_euler ( n ):

#*****************************************************************************80
#
## ripple_euler() solves the ripple ODE using euler.
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
#    John D Cook,
#    Ripples and Hyperbolas,
#    https://www.johndcook.com/blog/2020/11/06/ripples-and-hyperbolas/
#    Posted 06 November 2020.
#
#    Wendell Mills, Boris Weisfeiler, Allan Krall,
#    Discovering Theorems with a Computer: The Case of y‘ = sin(xy). 
#    The American Mathematical Monthly, 
#    Volume 86, Number 9, November 1979, pages 733-739.
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'ripple_euler()' )
  print ( '  Use euler() to solve the ripple ODE.' )

  t0, y0, tstop = ripple_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  f = ripple_deriv
#
#  Plot the solution curve.
#
  for i in range ( 1, 8 ):

    y0 = float ( i )

    t, y = euler ( f, tspan, y0, n )
    plt.plot ( t, y, 'r-', linewidth = 3 )

  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- X(T) --->'  )
  plt.title ( 'ripple euler: time plot' )
  filename = 'ripple_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def ripple_ode_test ( ):

#*****************************************************************************80
#
## ripple_ode_test() tests ripple_ode.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'ripple_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ripple_ode models an equation with ripples and hyperbolas.' )

  t0, y0, tstop = ripple_parameters ( )

  n = 1000
  ripple_euler ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'ripple_ode_test:' )
  print ( '  Normal end of execution.' )
  return

def ripple_parameters ( ):

#*****************************************************************************80
#
## ripple_parameters() returns parameters for the ripple ode.
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
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#
  t0 = 0.0
  y0 = 7.0
  tstop = 25.0

  return t0, y0, tstop

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
  ripple_ode_test ( )
  timestamp ( )

