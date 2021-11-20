#! /usr/bin/env python3
#
def flame_deriv ( t, y ):

#*****************************************************************************80
#
## flame_deriv() evaluates the derivative of the flame ODE.
#
#  Discussion:
#
#    1 equation.
#
#    Moler attributes this problem to Lawrence Shampine.
#
#    The equation describes the radius of a ball of flame that
#    begins, at time 0, at DELTA.
#
#      Y(0) = DELTA
#
#    The rate of fuel consumption is proportional to the volume, and
#    the rate of fuel intake is proportional to the area of the ball.
#    We take the constant of proportionality to be 1.
#
#      Y' = Y^2 - Y^3
#
#    The data is normalized so that Y = 1 is the equilibrium solution.
#
#    The computation is to be made from T = 0 to T = 2/DELTA.
#
#    For values of DELTA close to 1, such as 0.01, the equation is
#    not stiff.  But for DELTA = 0.0001, the equation can become
#    stiff as the solution approaches the equilibrium solution Y = 1,
#    and computed solutions may be wildly inaccurate or cautious
#    solvers may take very small timesteps.
#
#    The exact solution involves the Lambert W function, defined by
#
#      W(z) * exp ( W(z) ) = z
#
#    and if we set
#
#      A = ( 1 / DELTA - 1 )
#
#    then
#
#      Y(T) = 1 / ( W(A*exp(A-T)) + 1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Cleve's Corner: Stiff Differential Equations,
#    MATLAB News and Notes,
#    May 2003, pages 12-13.
#
#  Input:
#
#    real T, Y: the arguments of the derivative.
#
#  Output:
#
#    real DYDT: the value of the derivative.
#
  dydt = y**2 * ( 1.0 - y )

  return dydt

def flame_exact ( t ):

#*****************************************************************************80
#
## flame_exact() evaluates the exact solution of the flame ODE.
#
#  Discussion:
#
#    1 equation.
#
#    Moler attributes this problem to Lawrence Shampine.
#
#    The equation describes the radius of a ball of flame that
#    begins, at time 0, at DELTA.
#
#      Y(0) = DELTA
#
#    The rate of fuel consumption is proportional to the volume, and
#    the rate of fuel intake is proportional to the area of the ball.
#    We take the constant of proportionality to be 1.
#
#      Y' = Y^2 - Y^3
#
#    The data is normalized so that Y = 1 is the equilibrium solution.
#
#    The computation is to be made from T = 0 to T = 2/DELTA.
#
#    For values of DELTA close to 1, such as 0.01, the equation is
#    not stiff.  But for DELTA = 0.0001, the equation can become
#    stiff as the solution approaches the equilibrium solution Y = 1,
#    and computed solutions may be wildly inaccurate or cautious
#    solvers may take very small timesteps.
#
#    The exact solution involves the Lambert W function, defined by
#
#      W(z) * exp ( W(z) ) = z
#
#    and if we set
#
#      A = ( 1 / DELTA - 1 )
#
#    then
#
#      Y(T) = 1 / ( W(A*exp(A-T)) + 1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Cleve's Corner: Stiff Differential Equations,
#    MATLAB News and Notes,
#    May 2003, pages 12-13.
#
#  Input:
#
#    real T(:): the times.
#
#  Output:
#
#    real Y(:), the exact solution values.
#
  from scipy.special import lambertw
  import numpy as np

  t0, y0, tstop = flame_parameters ( )

  a = ( 1.0 - y0[0] ) / y0[0]
  y = 1.0 / np.real ( lambertw ( a * np.exp ( a - ( t - t0 ) ) ) + 1.0 )

  return y

def flame_ode_test ( ):

#*****************************************************************************80
#
## flame_ode_test() tests flame_ode.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 November 2020
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
  print ( 'flame_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  flame_ode uses an ODE to model combustion.' )

  t0, y0, tstop = flame_parameters ( )

  t_span = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( flame_deriv, t_span, y0, t_eval = t )
  ye = flame_exact ( t )
#
#  Plot the solution curve.
#
  plt.plot ( t, sol.y[0], 'ro', linewidth = 3 )
  plt.plot ( t, ye, 'b-', linewidth = 2 )
  s = ( 'Flame ODE, DELTA = %g' % ( y0 ) )
  plt.title ( s )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- X(T) --->' )
  plt.legend ( ( 'yapprox', 'yexact' ) )
  filename = 'flame.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'flame_ode_test:' )
  print ( '  Normal end of execution.' )
  return

def flame_parameters ( ):

#*****************************************************************************80
#
## flame_parameters() returns parameters for the flame ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T0: the initial time.
#
#    real Y0: the initial condition at time T0.
#
#    real TSTOP: the final time.
#
  import numpy as np

  t0 = 0.0
  y0 = np.array ( [ 0.01 ] )
  tstop = 2.0 / y0[0]

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
  flame_ode_test ( )
  timestamp ( )

