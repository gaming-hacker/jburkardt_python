#! /usr/bin/env python3
#
def axon_current ( t ):

#*****************************************************************************80
#
## axon_current() evaluates the time dependent current I(t) of the axon ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the time.
#
#  Output:
#
#    real I: the current.
#
  I = 75.0 * ( t <= 0.80 )

  return I

def axon_deriv ( t, y ):

#*****************************************************************************80
#
## axon_deriv() evaluates the right hand side of the axon ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Hodgkin, Andrew Huxley,
#    A quantitative description of membrane current and its
#    application to conduction and excitation in nerve,
#    The Journal of Physiology,
#    Volume 117, Number 4, pages 500-544, August 1952.
#
#  Input:
#
#    real T, Y(4): the time and solution value.
#
#  Output:
#
#    real DYDT(4): the derivative value.
#
  import numpy as np
#
#  Extract individual variable values at time t.
#
  V = y[0]
  n = y[1]
  m = y[2]
  h = y[3]
#
#  Get parameter values.
#
  C, E_K, E_Na, E_rest, G_K, G_Na, t0, y0, tstop = axon_parameters ( )
#
#  Compute alpha and beta for n:
#  Equations 12 and 13.
#
  alpha_n = 0.01 * ( ( 10.0 - V ) / ( np.exp ( ( 10.0 - V ) / 10.0 ) - 1.0 ) )
  beta_n = 0.125 * np.exp ( - V / 80.0 )
#
#  Compute alpha and beta for m:
#  Equations 20 and 21.
#
  alpha_m = 0.1 * ( ( 25.0 - V ) / ( np.exp ( ( 25.0 - V ) / 10.0 ) - 1.0 ) )
  beta_m = 4.0 * np.exp ( - V / 18.0 )
#
#  Compute alpha and beta for h:
#  Equations 23 and 24.
#
  alpha_h = 0.07 * np.exp ( - V / 20.0 )
  beta_h = 1.0 / ( np.exp ( ( 30.0 - V ) / 10.0 ) + 1.0 )
#
#  Calculate the currents.
#  I_Na:  equations 3 and 14.
#  I_K:   equations 4 and 6.
#  I_ion: equation 26.
#
  I_Na = m**3 * G_Na * h * ( V - E_Na )
  I_K = n**4 * G_K * ( V - E_K )
  I_ion = axon_current ( t ) - I_K - I_Na
#
#  Evaluate the derivatives.
#
#  dndt: equation 7
#  dmdt: equation 15
#  dhdt: equation 16
#
  dVdt = I_ion / C
  dndt = alpha_n * ( 1.0 - n ) - beta_n * n
  dmdt = alpha_m * ( 1.0 - m ) - beta_m * m
  dhdt = alpha_h * ( 1.0 - h ) - beta_h * h
#
#  Pack derivatives into vector.
#
  dydt = np.array ( [ dVdt, dndt, dmdt, dhdt ] )

  return dydt

def axon_euler ( ):

#*****************************************************************************80
#
## axon_euler() solves the axon ODE using euler().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'axon_euler():' )
  print ( '  Solve the axon ODE using euler()' )
  print ( '' )
#
#  Get the parameters.
#
  C, E_K, E_Na, E_rest, G_K, G_Na, t0, y0, tstop = axon_parameters ( )

  f = axon_deriv
  tspan = np.array ( [ t0, tstop ] )
  nt = 1000
  print ( '  Number of fixed time steps = ', nt )

  t, y = euler ( f, tspan, y0, nt )
#
#  Plots.
#
  plt.clf ( )
  plt.plot ( t, y[:,0], 'r-', linewidth = 3 )
  plt.title ( 'axon ODE, euler, V(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- V(T) --->' )
  filename = 'axon_euler_v.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, y[:,1], 'g-', linewidth = 3 )
  plt.title ( 'axon ODE, euler, N(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- N(T) --->' )
  filename = 'axon_euler_n.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, y[:,2], 'b-', linewidth = 3 )
  plt.title ( 'axon ODE, euler, M(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- M(T) --->' )
  filename = 'axon_euler_m.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, y[:,3], 'c-', linewidth = 3 )
  plt.title ( 'axon ODE, euler, H(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H(T) --->' )
  filename = 'axon_euler_h.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'axon_euler():' )
  print ( '  Normal end of execution.' )

  return

def axon_solve_ivp ( ):

#*****************************************************************************80
#
## axon_solve_ivp() solves the axon ODE using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'axon_solve_ivp():' )
  print ( '  Solve the axon ODE using solve_ivp()' )
  print ( '' )
#
#  Get the parameters.
#
  C, E_K, E_Na, E_rest, G_K, G_Na, t0, y0, tstop = axon_parameters ( )

  f = axon_deriv

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plots.
#
  plt.clf ( )
  plt.plot ( t, sol.y[0], 'r-', linewidth = 3 )
  plt.title ( 'axon ODE, solve ivp, V(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- V(T) --->' )
  filename = 'axon_solve_ivp_v.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, sol.y[1], 'g-', linewidth = 3 )
  plt.title ( 'axon ODE, solve ivp, N(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- N(T) --->' )
  filename = 'axon_solve_ivp_n.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, sol.y[2], 'b-', linewidth = 3 )
  plt.title ( 'axon ODE, solve ivp, M(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- M(T) --->' )
  filename = 'axon_solve_ivp_m.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, sol.y[3], 'c-', linewidth = 3 )
  plt.title ( 'axon ODE, solve_ivp, H(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H(T) --->' )
  filename = 'axon_solve_ivp_h.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'axon_solve_ivp():' )
  print ( '  Normal end of execution.' )

  return

def axon_ode_test ( ):

#*****************************************************************************80
#
## axon_ode_test() tests axon_ode().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'axon_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve the axon ODE.' )

  C, E_K, E_Na, E_rest, G_K, G_Na, t0, y0, tstop = axon_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    C =      ', C )
  print ( '    E_K =    ', E_K )
  print ( '    E_Na =   ', E_Na )
  print ( '    E_rest = ', E_rest )
  print ( '    G_K =    ', G_K )
  print ( '    G_Na =   ', G_Na )
  print ( '    t0 =     ', t0 )
  print ( '    V(0) =   ', y0[0] )
  print ( '    N(0) =   ', y0[1] )
  print ( '    M(0) =   ', y0[2] )
  print ( '    H(0) =   ', y0[3] )
  print ( '    tstop =  ', tstop )

  axon_euler ( )
  axon_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'axon_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def axon_parameters ( ):

#*****************************************************************************80
#
## axon_parameters() returns the parameters of the axon ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Hodgkin, Andrew Huxley,
#    A quantitative description of membrane current and its
#    application to conduction and excitation in nerve,
#    The Journal of Physiology,
#    Volume 117, Number 4, pages 500-544, August 1952.
#
#  Output:
#
#    real C: the membrane capacity per unit area.
#
#    real E_K: the equilibrium potential for potassium.
#
#    real E_Na: the equilibrium potential for sodium.
#
#    real E_rest: the resting potential.
#
#    real G_K: the potassium conductance.
#
#    real G_Na: the sodium conductance.
#
#    real t0: the initial time.
#
#    real y0(4): the values at the initial time of V, N, M, and H.
#
#    real tstop: the final time.
#
  import numpy as np

  C = 1.0
  E_K = -74.7
  E_Na = 54.2
  E_rest = -68.0
  G_K = 12.0
  G_Na = 30.0
  t0 = 0.0
  V_init = 0.0
  alpha_n = 0.01 * ( 10.0 - V_init ) / ( np.exp ( ( 10.0 - V_init ) / 10.0 ) - 1.0 )
  beta_n = 0.125 * np.exp ( - V_init / 80.0 )
  n_init = alpha_n / ( alpha_n + beta_n )
  alpha_m = 0.1 * ( 25.0 - V_init ) / ( np.exp ( ( 25.0 - V_init ) / 10.0 ) - 1.0 )
  beta_m = 4.0 * np.exp ( - V_init / 18.0 )
  m_init = alpha_m / ( alpha_m + beta_m )
  alpha_h = 0.07 * np.exp ( - V_init / 20.0 )
  beta_h = 1.0 / ( np.exp ( ( 30.0 - V_init ) / 10.0 ) + 1.0 )
  h_init = alpha_h / ( alpha_h + beta_h )
  y0 = np.array ( [ V_init, n_init, m_init, h_init ] )
  tstop = 10.0

  return C, E_K, E_Na, E_rest, G_K, G_Na, t0, y0, tstop

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

  t0 = tspan[0]
  tstop = tspan[1]
  dt = ( tstop - t0 ) / n
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )
  t[0] = t0
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
  axon_ode_test ( )
  timestamp ( )

