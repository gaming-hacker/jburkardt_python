#! /usr/bin/env python3
#
def roessler_deriv ( t, y ):

#*****************************************************************************80
#
## roessler_deriv() evaluates the right hand side of the Roessler ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Otto Roessler,
#    An Equation for Continuous Chaos,
#    Physics Letters, 
#    Volume 57A, Number 5, pages 397–398, 1976.
#
#  Input:
#
#    real T, the value of the independent variable.
#
#    real Y[3], the values of the dependent variables at time T.
#
#  Output:
#
#    real DYDT(3), the values of the derivatives
#    of the dependent variables at time T.
#
  import numpy as np

  alpha, beta, mu, t0, y0, tstop = roessler_parameters ( )

  dydt = np.zeros ( 3 )

  dydt[0] = - y[1] - y[2]
  dydt[1] = y[0] + alpha * y[1]
  dydt[2] = beta + ( y[0] - mu ) * y[2]

  return dydt

def roessler_ode_test ( ):

#*****************************************************************************80
#
## roessler_ode_test() tests roessler_ode.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'roessler_ode_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Compute solutions of the Roessler system.' )
  print ( '  Plot solution components (T,X(T)), (T,Y(T)), and (T,Z(T)).' )
  print ( '  Plot (X(T),Y(T),Z(T)).' )

  t, x, y, z = roessler_ode_solve_ivp ( )
  roessler_ode_plot_components ( t, x, y, z )
  roessler_ode_plot_3d ( t, x, y, z )
#
#  Terminate.
#
  print ( '' )
  print ( 'roessler_ode_test:' )
  print ( '  Normal end of execution.' )
  return

def roessler_ode_solve_ivp ( ):

#*****************************************************************************80
#
## roessler_ode_solve_ivp() solves the Roessler ODE using solve_ivp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(:), X(:), Y(:), Z(:), values of the discrete solution.
#
  import numpy as np
  from scipy.integrate import solve_ivp
 
  alpha, beta, mu, t0, y0, tstop = roessler_parameters ( )

  tspan = np.array ( [ t0, tstop ] )

  sol = solve_ivp ( roessler_deriv, tspan, y0 )

  t = sol.t
  x = sol.y[0,:]
  y = sol.y[1,:]
  z = sol.y[2,:]

  return t, x, y, z

def roessler_ode_plot_components ( t, x, y, z ):

#*****************************************************************************80
#
## roessler_ode_plot_components() plots X(T), Y(T) and Z(T) for the Roessler ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:), the value of the independent variable.
#
#    real X(:), Y(:), Z(:), the values of the dependent variables at time T.
#
  import matplotlib.pyplot as plt
#
#  Plot the data.
#
  plt.clf ( )
  plt.plot ( t, x, linewidth = 2, color = 'b' )
  plt.plot ( t, y, linewidth = 2, color = 'r' )
  plt.plot ( t, z, linewidth = 2, color = 'g' )
  plt.grid ( True )
  plt.xlabel ( '<--- Time --->' )
  plt.ylabel ( '<--- X(T), Y(T), Z(T) --->' )
  plt.title ( 'Roessler Time Series Plot' )
  filename = 'roessler_ode_components.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def roessler_ode_plot_3d ( t, x, y, z ):

#*****************************************************************************80
#
## roessler_ode_plot_3d() plots (X,Y,Z) for the Roessler ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(:), the value of the independent variable.
#
#    real X(:), Y(:), Z(:), the values of the dependent variables at time T.
#
  import matplotlib as mpl
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
#
#  Plot the data.
#
  fig = plt.figure ( )
  plt.clf ( )
  ax = fig.gca ( projection = '3d' )
  ax.plot ( x, y, z, linewidth = 1, color = 'b' )
  ax.grid ( True )
  ax.set_xlabel ( '<--- X(T) --->' )
  ax.set_ylabel ( '<--- Y(T) --->' )
  ax.set_zlabel ( '<--- Z(T) --->' )
  ax.set_title ( 'Roessler 3D Plot' )
  filename = 'roessler_ode_3d.png' 
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def roessler_parameters ( ):

#*****************************************************************************80
#
## roessler_parameters returns parameters for the roessler ODE.
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
#    real ALPHA: problem parameter.
#
#    real BETA: problem parameter.
#
#    real MU: problem parameter.
#
#    real T0: the initial time.
#
#    real Y0[3]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  alpha = 0.2
  beta = 0.2
  mu = 5.7

  t0 = 0.0
  y0 = np.array ( [ 8.0, 1.0, 1.0 ] )
  tstop = 100.0

  return alpha, beta, mu, t0, y0, tstop

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
#    06 April 2013
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
  roessler_ode_test ( )
  timestamp ( )

