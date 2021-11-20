#! /usr/bin/env python3
#
def blowup_deriv ( t, y ):

#*****************************************************************************80
#
## blowup_deriv() evaluates the right hand side of the blowup ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Approximating a solution that doesn't exist,
#    https://www.johndcook.com/blog/2009/08/11/approximating-a-solution-that-doesnt-exist/
#    11 August 2009.
#
#  Input:
#
#    real T, Y: the time and solution value.
#
#  Output:
#
#    real DYDT: the derivative value.
#
  dydt = y**2

  return dydt

def blowup_euler ( n ):

#*****************************************************************************80
#
## blowup_euler() solves the blowup ODE using euler.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'blowup_euler():' )
  print ( '  Use euler() to solve the blowup ODE' )
#
#  Get the parameters.
#
  t0, y0, tstop = blowup_parameters ( )

  f = blowup_deriv
  tspan = np.array ( [ t0, tstop ] )

  t, y = euler ( f, tspan, y0, n )

  print ( '' )
  print ( '  Number of equal steps is %d\n', n );

  ye = blowup_exact ( t )
#
#  Plot the solution curve.
#
  plt.clf ( )
  plt.plot ( t, y, 'ro', linewidth = 3 )
  plt.plot ( t, ye, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- X(T) --->' )
  plt.title ( 'blowup euler()' )
  plt.legend ( ( 'Computed', 'Exact' ) )
  filename = 'blowup_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def blowup_exact ( t ):

#*****************************************************************************80
#
## blowup_exact() evaluates the exact solution of the blowup ODE.
#
#  Discussion:
#
#    y' = y^2
#    dy/y^2 = dt                   (Separation of variables)
#    -1/y = t + C                  (Antiderivatives)
#     y = - 1 / ( t + C )
#     C = - t0 - 1/y0
#     y = - 1 / ( t - t0 - 1/y0 )  (Exact formula)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:): the evaluation times.
#
#  Output:
#
#    real Y(:): the exact solution values.
#
  import numpy as np

  t0, y0, tstop = blowup_parameters ( )

  if ( y0 == 0.0 ):
    value = np.zeros ( t.shape )
  else:
    value = - 1.0 / ( t - t0 - 1.0 / y0 )

  return value

def blowup_ode_test ( ):

#*****************************************************************************80
#
## blowup_ode_test() tests blowup_ode.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 November 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'blowup_ode_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test blowup_ode().' )

  n = 40
  blowup_euler ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'blowup_ode_test' )
  print ( '  Normal end of execution.' )
  return

def blowup_parameters ( ):

#*****************************************************************************80
#
## blowup_parameters() returns parameters for the blowup ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T0: the initial time, in seconds
#
#    real Y0: the initial value.
#
#    real TSTOP: the final time.
#
  t0 = 0.0
  y0 = 1.0
  tstop = 0.95

  return t0, y0, tstop

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

if ( __name__ == '__main__' ):
  timestamp ( )
  blowup_ode_test ( )
  timestamp ( )

