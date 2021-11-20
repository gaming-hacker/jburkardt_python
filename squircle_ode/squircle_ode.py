#! /usr/bin/env python3
#
def midpoint ( f, tspan, y0, n ):

#*****************************************************************************80
#
## midpoint() uses the implicit midpoint method to solve an ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real tspan[2]: the starting and ending times.
#
#    real y0[m]: the initial conditions. 
#
#    integer n: the number of steps.
#
#  Output:
#
#    real t[n+1], y[n+1,m]: the solution estimates.
#
  from scipy.optimize import fsolve
  import numpy as np

  if ( np.ndim ( y0 ) == 0 ):
    m = 1
  else:
    m = len ( y0 )

  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )

  dt = ( tspan[1] - tspan[0] ) / float ( n )

  t[0] = tspan[0];
  y[0,:] = y0

  for i in range ( 0, n ):

    to = t[i]
    yo = y[i,:]

    th = to + 0.5 * dt
    yh = yo + 0.5 * dt * f ( to, yo )
    yh = fsolve ( midpoint_residual, yh, args = ( f, to, yo, th ) )

    tp = to + dt
    yp = 2.0 * yh - yo

    t[i+1]   = tp
    y[i+1,:] = yp

  return t, y

def midpoint_residual ( yh, f, to, yo, th ):

#*****************************************************************************80
#
## midpoint_residual() evaluates the midpoint residual.
#
#  Discussion:
#
#    We are seeking a value YH defined by the implicit equation:
#
#      YH = YO + ( TH - TO ) * F ( TH, YH )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real yh: the estimated solution value at the midpoint time.
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real to, yo: the old time and solution value.
#
#    real th: the midpoint time.
#
#  Output:
#
#    real value: the midpoint residual.
#
  value = yh - yo - ( th - to ) * f ( th, yh );

  return value

def squircle_conserved ( u, v ):

#*****************************************************************************80
#
## squircle_conserved() returns a conserved quantity for the squircle ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real U[N], V[N]: the current solution.
#
#  Output:
#
#    real H[N]: the value of the conserved quantity.
#
  s, t0, y0, tstop = squircle_parameters ( )

  h = u**s + v**s

  return h

def squircle_deriv ( t, y ):

#*****************************************************************************80
#
## squircle_deriv() returns the right hand side of the squircle ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    A generalization of sine and cosine,
#    https://www.johndcook.com/blog/2020/12/21/generalization-sine-cosine/
#
#    David Shelupsky,
#    A generalization of the trigonometric functions,
#    The American Mathematical Monthly,
#    Volume 66, Number 10, December 1959, pages 879-884.
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

  s, t0, y0, tstop = squircle_parameters ( )

  u = y[0]
  v = y[1]

  dudt =     v ** ( s - 1 )
  dvdt = - ( u ** ( s - 1 ) )

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def squircle_midpoint ( n ):

#*****************************************************************************80
#
## squircle_midpoint tests squircle_ode using midpoint().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'squircle_midpoint():' )
  print ( '  Test squircle_ode() using midpoint.' )

  s, t0, y0, tstop = squircle_parameters ( )

  f = squircle_deriv
  tspan = np.array ( [ t0, tstop ] )

  t, y = midpoint ( f, tspan, y0, n )

  t.shape
  y.shape

  print ( '' )
  print ( '  Number of steps taken was ', n )
#
#  Plot u, v.
#
  plt.clf ( )
  plt.plot ( t, y[:,0], 'r-', linewidth = 2 )
  plt.plot ( t, y[:,1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Solution components -->' )
  plt.title ( 'squircle midpoint: solution components' )
  plt.legend ( ( 'y_1', 'y_2' ) )
  filename = 'squircle_midpoint_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Phase plot.
#
  plt.clf ( )
  plt.plot ( y[:,0], y[:,1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- y_1 -->' )
  plt.ylabel ( '<-- y_2 -->' )
  plt.title ( 'squircle midpoint: phase plot' )
  plt.axis ( 'equal' )
  filename = 'squircle_midpoint_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot energy.
#
  h = squircle_conserved ( y[:,0], y[:,1] )

  plt.clf ( )
  plt.plot ( t, h, 'r-', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ h[0], h[0] ] ), 'b--', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  plt.title ( 'squircle midpoint: energy' )
  plt.legend ( ( 'Computed energy', 'Exact energy', 'Zero energy' ) )
  filename = 'squircle_midpoint_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def squircle_ode_test ( ):

#*****************************************************************************80
#
## squircle_ode_test() solves the squircle ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'squircle_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve the squircle ODE.' )

  s, t0, y0, tstop = squircle_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    s     = ', s )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0[0], y0[1] )
  print ( '    tstop = ', tstop )

  n = 100
  squircle_midpoint ( n )

  squircle_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'squircle_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def squircle_parameters ( ):

#*****************************************************************************80
#
## squircle_parameters() returns parameters for the squircle ODE.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer S: the exponent.
#
#    real T0: the initial time
#
#    real Y0(2): the initial values.
#
#    real TSTOP: the final time.
#
  import numpy as np

  s = 4.0
  t0 = 0.0
  y0 = np.array ( [ 0.0, 1.0 ] )
  tstop = 20.0
  
  return s, t0, y0, tstop

def squircle_solve_ivp ( ):

#*****************************************************************************80
#
## squircle_solve_ivp() tests squircle_ode using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'squircle_solve_ivp():' )
  print ( '  Test squircle_ode() using solve_ivp().' )

  s, t0, y0, tstop = squircle_parameters ( )

  f = squircle_deriv
  tspan = np.array ( [ t0, tstop ] )
  n = 101
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plot u, v.
#
  plt.plot ( t, sol.y[0], 'r-', linewidth = 2 )
  plt.plot ( t, sol.y[1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Solution components -->' )
  plt.title ( 'squircle solve_ivp: solution components' )
  plt.legend ( ( 'y_1', 'y_2' ) )
  filename = 'squircle_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Phase plot.
#
  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- y_1 -->' )
  plt.ylabel ( '<-- y_2 -->' )
  plt.title ( 'squircle solve_ivp: phase plot' )
  plt.axis ( 'equal' )
  filename = 'squircle_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot energy.
#
  h = squircle_conserved ( sol.y[0], sol.y[1] )

  plt.plot ( t, h, 'r-', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ h[0], h[0] ] ), 'b--', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  plt.title ( 'squircle solve_ivp: energy' )
  plt.legend ( ( 'Computed energy', 'Exact energy', 'Zero energy' ) )
  filename = 'squircle_solve_ivp_conservation.png'
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
  squircle_ode_test ( )
  timestamp ( )


