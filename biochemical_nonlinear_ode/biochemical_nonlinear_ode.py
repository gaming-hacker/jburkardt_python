#! /usr/bin/env python3
#
def biochemical_nonlinear_conserved ( t, y ):

#*****************************************************************************80
#
## biochemical_nonlinear_conserved() evaluates two conserved quantities.
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
#    GeCo: Geometric conservative nonstandard schemes for biochemical systems,
#    Applied Numerical Mathematics,
#    2019.
#
#  Input:
#
#    real T: the current time.
#
#    real Y(4): the current solution.
#
#    real A, B: parameter values.
#
#  Output:
#
#    real H(2): the conserved quantities.
#
  import numpy as np

  a, b, kc, kn, rmax, e, t0, y0, tstop = biochemical_nonlinear_parameters ( )

  E = np.array ( [ \
    [ 1.0, 0.0, a, a ], \
    [ 0.0, 1.0, b, b ] ] )

  h = np.matmul ( E, y )

  return h

def biochemical_nonlinear_deriv ( t, cnpd ):

#*****************************************************************************80
#
## biochemical_nonlinear_deriv(): derivative of a nonlinear biochemical ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2020
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
#    real T, CNPD(4): the arguments of the derivative.
#
#  Output:
#
#    real DCNPDDT(4): the value of the derivative.
#
  import numpy as np

  a, b, kc, kn, rmax, e, t0, y0, tstop = biochemical_nonlinear_parameters ( )

  c = cnpd[0]
  n = cnpd[1]
  p = cnpd[2]
  d = cnpd[3]

  S = np.array ( [
    [ -a,    0.0 ], \
    [ -b,    0.0 ], \
    [  1.0, -1.0 ], \
    [  0.0,  1.0 ] ] )

  r = np.array ( [ \
    rmax * c / ( kc + c ) * n * ( kn + n ) * p , \
    e * p ] )
  
  dcnpddt = np.matmul ( S, r )

  return dcnpddt

def biochemical_nonlinear_ode_test ( ):

#*****************************************************************************80
#
## biochemical_nonlinear_ode_test() tests biochemical_nonlinear_ode().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2020
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
  print ( 'biochemical_nonlinear_ode_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test biochemical_nonlinear_ode using ode45.' )

  a, b, kc, kn, rmax, e, t0, y0, tstop = biochemical_nonlinear_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( biochemical_nonlinear_deriv, \
    t_span = tspan, y0 = y0, t_eval = t )

  plt.clf ( )
  plt.plot ( t, sol.y[0,:], 'r-', linewidth = 3 )
  plt.plot ( t, sol.y[1,:], 'g-', linewidth = 3 )
  plt.plot ( t, sol.y[2,:], 'b-', linewidth = 3 )
  plt.plot ( t, sol.y[3,:], 'm-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---    --->' )
  plt.title ( 'biochemical nonlinear ode' )
  plt.legend ( ( 'C', 'N', 'P', 'D' ) )
  filename = 'biochemical_nonlinear_ode.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'biochemical_nonlinear_ode_test:' )
  print ( '  Normal end of execution.' )
  return

def biochemical_nonlinear_parameters ( ):

#*****************************************************************************80
#
## biochemical_nonlinear_parameters(): parameters for biochemical npnlinear ODE.
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
#    real KC, KN: parameters
#
#    real RMAX: a parameter.
#
#    real E: a parameter.
#
#    real T0: the initial time.
#
#    real Y0[4]: the initial condition at time T0.
#
#    real TSTOP: the final time.
#
  import numpy as np

  a = 1.0
  b = 1.0
  kc = 1.0
  kn = 1.0
  rmax = 1.0
  e = 0.3
  t0 = 0.0
  y0 = np.array ( [ 29.98, 9.98, 0.01, 0.01 ] )
  tstop = 13.0

  return a, b, kc, kn, rmax, e, t0, y0, tstop

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
  biochemical_nonlinear_ode_test ( )
  timestamp ( )

