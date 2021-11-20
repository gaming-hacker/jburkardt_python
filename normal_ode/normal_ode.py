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

def normal_deriv ( t, y ):

#*****************************************************************************80
#
## normal_deriv() returns the right hand side of the NORMAL ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y, the arguments.
#
#  Output:
#
#    real DYDT, the value of the right hand side of the ODE.
#
  dydt = - t * y

  return dydt

def normal_ode_test ( n1 ):

#*****************************************************************************80
#
## normal_ode_test() tests normal_ode().
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
#  Input:
#
#    integer N1: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'normal_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  normal_ode() defines an ODE for the normal PDF.' )
  print ( '  Solve this ODE using the Euler method.' )
  print ( '  Estimate ODE approximation error by taking twice as many steps.' )

  t0, y0, tstop = normal_parameters ( )

  dydt = normal_deriv
  tspan = np.array ( [ t0, tstop ] )

  t1, y1 = euler ( dydt, tspan, y0, n1 )

  n2 = 2 * n1
  t2, y2 = euler ( dydt, tspan, y0, n2 )

  y = normal_exact ( t1 )
#
#  Caution!  In Python, a non-unit array index increment
#  is the third item, not the second, as in "0:n2+1:2"
#
  e =  y[:]           - y1[:,0]
  e2 = y2[0:n2+1:2,0] - y1[:,0]

  e_norm = rms ( e )
  e2_norm = rms ( e2 )

  tplot = np.linspace ( t0, tstop, 101 )
  yplot = normal_exact ( tplot )
  plt.plot ( t1, y1, 'ro', t2, y2, 'b+', tplot, yplot, 'k-', linewidth = 3 )
  plt.grid ( True )
  s = ( 'Compare normal ODE solutions using ', n1, ' and ', n2, ' steps' )
  plt.title ( s )
  plt.legend ( ( 'N steps', '2N steps', 'exact' ) )
  filename = 'normal_ode.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( np.array ( [t0,tstop] ), np.array ( [0.0,0.0] ), 'k--', \
    t1, e2, 'r-', t1, e, 'k-', linewidth = 3 )
  plt.grid ( True )
  s = ( 'normal ODE estimated error using ', n1, ' and ', n2, ' steps' )
  plt.title ( s )
  plt.legend ( ( 'Zero error', 'Estimated error', 'Exact error' ) )
  filename = 'normal_ode_error.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  print ( '' )
  print ( '  Solution used ', n1, ' and ', n2, ' steps.' )
  print ( '  Estimated RMS error = ', e2_norm )
  print ( '  Exact     RMS error = ', e_norm )

  print ( '' )
  print ( '  At the point t         = ', tstop )
  print ( '  Y estimate             = ', y1[n1] )
  print ( '  Y double step estimate = ', y2[n2] )
  print ( '  Y exact value          = ', y[n1] )
  print ( '  Y error estimate       = ', y2[n2] - y1[n1] )
  print ( '  Y exact error          = ', y[n1]  - y1[n1] )
#
#  Terminate.
#
  print ( '' )
  print ( 'normal_ode_test:' )
  print ( '  Normal end of execution.' )

  return

def normal_exact ( t ):

#*****************************************************************************80
#
## normal_exact(): the normal PDF function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the current time.
#
#  Output:
#
#    real Y: the value of the function at t.
#
  import numpy as np

  value = np.exp ( - t**2 / 2.0 ) / np.sqrt ( 2.0 * np.pi )

  return value

def normal_parameters ( ):

#*****************************************************************************80
#
## normal_parameters() returns the parameters of the normal ODE.
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
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#
  t0 = -5.0
  y0 = normal_exact ( t0 )
  tstop = 5.0

  return t0, y0, tstop

def rms ( x ):

#*****************************************************************************80
#
## rms() returns the root-mean-square norm of a vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N): the vector.
#
#  Output:
#
#    real VALUE: the RMS of the vector.
#
  import numpy as np

  n = x.shape[0]
  value = 0.0
  for i in range ( 0, n ):
    value = value + x[i]**2
  value = np.sqrt ( value / n )

  return value

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
  normal_ode_test ( 100 )
  timestamp ( )

