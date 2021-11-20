#! /usr/bin/env python3
#
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

def vanderpol_deriv ( t, y ):

#*****************************************************************************80
#
## vanderpol_deriv() returns the right hand side of the vanderpol ODE.
#
#  Discussion:
#
#    The parameter MU is defined by the function vanderpol_mu()
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y(2), the arguments of the derivative.
#
#  Output:
#
#    real DYDT(2), the value of the derivative.
#
  import numpy as np

  mu, t0, y0, tstop = vanderpol_parameters ( )

  u = y[0]
  v = y[1]

  dudt = v
  dvdt = mu * ( 1.0 - u**2 ) * v - u

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def vanderpol_events ( t, y ):

#*****************************************************************************80
#
## vanderpol_events() defines an event as a zero value for the first component.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Calculating the period of Van der Pol Oscillators,
#    https://www.johndcook.com/blog/2019/12/26/van-der-pol-period/
#    26 December 2019.
#
#  Input:
#
#    real T, Y[*]: a time and ODE solution.
#
#  Output:
#
#    real EVENT: a quantity which is zero if an "event" has occurred.
#
  return y[0]

def vanderpol_ode_test ( ):

#*****************************************************************************80
#
## vanderpol_ode_test() calls solve_ivp() to solve the van der Pol ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2020
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
  print ( 'vanderpol_ode_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve the van der Pol oscillator ODE using solve_ivp().' )
#
#  Get parameter values.
#
  mu, t0, y0, tstop = vanderpol_parameters ( )

  print ( '' )
  print ( '  Parameters:' )
  print ( '    mu    = ', mu )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  dydt = vanderpol_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( dydt, tspan, y0, t_eval = t, events = vanderpol_events )
#
#  Time plot of y(t), y'(t).
#
  plt.clf ( )
  plt.plot ( t, sol.y[0], 'r-', t, sol.y[1], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- Y(T) -->' )
  s = ( 'van der Pol solve_ivp, mu = %g' % ( mu ) )
  plt.title ( s )
  plt.legend ( ( 'y(t)', 'y\'(t)' ) )
  filename = 'vanderpol_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Phase plot.
#
  plt.clf ( )
  plt.plot ( sol.y[0], sol.y[1], linewidth = 3 )
  plt.plot ( sol.y[0,0], sol.y[1,0], 'g.', markersize = 40 )
  plt.plot ( sol.y[0,-1], sol.y[1,-1], 'r.', markersize = 30 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.xlabel ( '<-- Y(T) -->' )
  plt.ylabel ( '<-- Y''(T) -->' )
  s = ( 'van der Pol solve_ivp phase plot, mu = %g' % ( mu ) )
  plt.title ( s )
  filename = 'vanderpol_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Zeros plot.
#  zeros[] records values of t for which the first component was zero.
#
  zeros = sol.t_events[0]
  spacing = zeros[1:] - zeros[:-1]
  deltas = spacing[1:] - spacing[:-1]
  print ( '  Estimated period is ', 2 * spacing[-1] );

  plt.clf ( )
  plt.bar ( zeros[1:], spacing )
  plt.grid ( True )
  plt.xlabel ( '<-- T -->' )
  plt.ylabel ( '<-- Spacing -->' )
  s = ( 'van der Pol solve_ivp zero spacing, mu = %g' % ( mu ) )
  plt.title ( s )
  filename = 'vanderpol_solve_ivp_spacing.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'vanderpol_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def vanderpol_parameters ( ):

#*****************************************************************************80
#
## vanderpol_parameters() returns the parameters of the vanderpol ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 August 2021
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real MU: the mu parameter.
#
#    real T0: the initial time.
#
#    real Y0(2): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  mu = 2.0
  t0 = 0.0
  u0 = 1.0
  v0 = 0.0
  y0 = np.array ( [ u0, v0 ] )
  tstop = 40.0

  return mu, t0, y0, tstop

if ( __name__ == '__main__' ):
  timestamp ( )
  vanderpol_ode_test ( )
  timestamp ( )

