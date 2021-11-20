#! /usr/bin/env python3
#
def sir_conserved ( y ):

#*****************************************************************************80
#
## sir_conserved() returns a conserved quantity for the SIR ODE.
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
#    real Y(:,3): the current solution.
#
#  Output:
#
#    real H(:): the value of the conserved quantity.
#
  import numpy as np

  h = np.sum ( y, axis = 0 )

  return h

def sir_deriv ( t, y ):

#*****************************************************************************80
#
## sir_deriv() evaluates the right hand side of the SIR ode.
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
#    real T: the time.
#
#    real y(3), the susceptible, infected, and recovered populations.
#
#  Output:
#
#    real dydt(3), the values of dSdt, dIdt, dRdt.
#
  import numpy as np

  alpha, beta, gamma, t0, y0, tstop = sir_parameters ( )

  S = y[0]
  I = y[1]
  R = y[2]

  N = S + I + R
  dSdt = - alpha * S * I / N            + gamma * R
  dIdt =   alpha * S * I / N - beta * I
  dRdt =                       beta * I - gamma * R

  dydt = np.array ( [ dSdt, dIdt, dRdt ] )

  return dydt

def sir_solve_ivp ( ):

#*****************************************************************************80
#
## sir_solve_ivp() solves the SIR ODE using solve_ivp().
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
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sir_solve_ivp):' )
  print ( '  Solve the SIR ODE using solve_ivp().' )

  alpha, beta, gamma, t0, y0, tstop = sir_parameters ( )
#
#  Compute the approximate solution.
#
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( tspan[0], tspan[1], 101 )

  sol = solve_ivp ( sir_deriv, tspan, y0, t_eval = t )
#
#  Plot S(t), I(t), R(t).
#
  plt.plot ( t, sol.y[0], 'g', linewidth = 3 )
  plt.plot ( t, sol.y[1], 'r', linewidth = 3 )
  plt.plot ( t, sol.y[2], 'b', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Cases -->' )
  plt.legend ( ( 'Susceptible', 'Infected', 'Recovered' ) )
  s = ( 'SIR solve_ivp: alpha = %g, beta = %g, gamma = %g' \
    % ( alpha, beta, gamma ) )
  plt.title ( s )
  filename = 'sir_solve_ivp.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot N(t) = S(t) + I(t) + R(t).
#
  h = sir_conserved ( sol.y )

  plt.plot ( t, h, 'c-', linewidth = 3 )
  plt.plot ( [ t0, tstop ], [ 0.0, 0.0 ], 'k-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- N(t) -->' )
  s = ( 'SIR solve_ivp: alpha = %g, beta = %g, gamma = %g' \
    % ( alpha, beta, gamma ) )
  plt.title ( s )
  filename = 'sir_solve_ivp_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def sir_ode_test ( ):

#*****************************************************************************80
#
## sir_ode_test() tests sir_ode.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'sir_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve the SIR ODE.' )

  alpha, beta, gamma, t0, y0, tstop = sir_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    alpha = ', alpha )
  print ( '    beta  = ', beta )
  print ( '    gamma = ', gamma )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  sir_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sir_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def sir_parameters ( ):

#*****************************************************************************80
#
## sir_parameters() returns parameters for the SIR ODE.
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
#    real ALPHA: the parameters.
#
#    real BETA: the parameters.
#
#    real GAMMA: the parameters.
#
#    real T0: the initial time
#
#    real Y0[3]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  alpha = 0.0075
  beta  = 0.0050
  gamma = 0.0010
  t0 = 0.0
  y0 = np.array ( [ 99.0, 1.0, 0.0 ] )
  tstop = 5000.0

  return alpha, beta, gamma, t0, y0, tstop

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
  sir_ode_test ( )
  timestamp ( )

