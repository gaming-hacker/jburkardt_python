#! /usr/bin/env python3
#
def lorenz_deriv ( t, xyz ):

#*****************************************************************************80
#
## lorenz_deriv() evaluates the right hand side of the Lorenz ODE.
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
#  Input:
#
#    real T, the value of the independent variable.
#
#    real XYZ[3], the values of the dependent variables at time T.
#
#  Output:
#
#    real DXDT(3), the values of the derivatives
#    of the dependent variables at time T.
#
  import numpy as np

  beta, rho, sigma, t0, y0, tstop = lorenz_parameters ( )

  dxdt = np.zeros ( 3 )

  dxdt[0] = sigma * ( xyz[1] - xyz[0] )
  dxdt[1] = xyz[0] * ( rho - xyz[2] ) - xyz[1]
  dxdt[2] = xyz[0] * xyz[1] - beta * xyz[2]

  return dxdt

def lorenz_ode_test ( ):

#*****************************************************************************80
#
## lorenz_ode_test() tests lorenz_ode.
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
  print ( 'lorenz_ode_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Compute solutions of the Lorenz system.' )

  t, x, y, z = lorenz_ode_solve_ivp ( )
  lorenz_ode_plot_components ( t, x, y, z )
  lorenz_ode_plot_3d ( t, x, y, z )
#
#  Terminate.
#
  print ( '' )
  print ( 'lorenz_ode_test:' )
  print ( '  Normal end of execution.' )
  return

def lorenz_ode_solve_ivp ( ):

#*****************************************************************************80
#
## lorenz_ode_solve_ivp() solves the Lorenz ODE using solve_ivp.
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
 
  beta, rho, sigma, t0, xyz0, tstop = lorenz_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  sol = solve_ivp ( lorenz_deriv, tspan, xyz0 )

  t = sol.t
  x = sol.y[0,:]
  y = sol.y[1,:]
  z = sol.y[2,:]

  return t, x, y, z

def lorenz_ode_plot_components ( t, x, y, z ):

#*****************************************************************************80
#
## lorenz_ode_plot_components() plots X(T), Y(T) and Z(T) for the Lorenz ODE.
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
#
  import matplotlib.pyplot as plt
#
#  Plot the data.
#
  plt.plot ( t, x, linewidth = 2, color = 'b' )
  plt.plot ( t, y, linewidth = 2, color = 'r' )
  plt.plot ( t, z, linewidth = 2, color = 'g' )
  plt.grid ( True )
  plt.xlabel ( '<--- Time --->' )
  plt.ylabel ( '<--- X(T), Y(T), Z(T) --->' )
  plt.title ( 'Lorenz Time Series Plot' )
  plt.savefig ( 'lorenz_ode_components.png' )
  print ( '' )
  print ( '  Graphics data saved as "lorenz_ode_components.png"' )
  plt.show ( block = False )
  plt.close ( )

  return

def lorenz_ode_plot_3d ( t, x, y, z ):

#*****************************************************************************80
#
## lorenz_ode_plot_3d() plots (X,Y,Z) for the Lorenz ODE.
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
  ax = fig.gca ( projection = '3d' )
  ax.plot ( x, y, z, linewidth = 1, color = 'b' )
  ax.grid ( True )
  ax.set_xlabel ( '<--- X(T) --->' )
  ax.set_ylabel ( '<--- Y(T) --->' )
  ax.set_zlabel ( '<--- Z(T) --->' )
  ax.set_title ( 'Lorenz 3D Plot' )
  plt.savefig ( 'lorenz_ode_3d.png' )
  print ( '' )
  print ( '  Graphics data saved as "lorenz_ode_3d.png"' )
  plt.show ( block = False )
  plt.close ( )

  return

def lorenz_parameters ( ):

#*****************************************************************************80
#
## lorenz_parameters() returns parameters for the lorenz ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real BETA: problem parameter.
#
#    real RHO: problem parameter.
#
#    real SIGMA: problem parameter.
#
#    real T0: the initial time.
#
#    real Y0(3): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  beta = 8.0 / 3.0
  rho = 28.0
  sigma = 10.0
  t0 = 0.0
  y0 = np.array ( [ 8.0, 1.0, 1.0 ] )
  tstop = 40.0

  return beta, rho, sigma, t0, y0, tstop

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

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  lorenz_ode_test ( )
  timestamp ( )

