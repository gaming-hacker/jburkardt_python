#! /usr/bin/env python3
#
def robertson_conserved ( t, y ):

#*****************************************************************************80
#
## robertson_conserved() evaluates a quantity that should be conserved.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 August 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer, Gerhard Wanner,
#    Solving Ordinary Differential Equations II: 
#    Stiff and Differential-algebraic Problems,
#    Springer-Verlag, second revised edition, 1996.
#
#  Input:
#
#    real Y[3,:]: the current solution.
#
#  Output:
#
#    real H(:): the conserved quantity.
#
  import numpy as np

  h = np.sum ( y, axis = 0 )

  return h

def robertson_deriv ( t, y ):

#*****************************************************************************80
#
## robertson_deriv() evaluates the derivative of the Robertson ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 August 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer, Gerhard Wanner,
#    Solving Ordinary Differential Equations II: 
#    Stiff and Differential-algebraic Problems,
#    Springer-Verlag, second revised edition, 1996.
#
#  Input:
#
#    real T, Y(3): the arguments of the derivative.
#
#  Output:
#
#    real DYDT(3): the value of the derivative.
#
  import numpy as np

  y1 = y[0]
  y2 = y[1]
  y3 = y[2]

  dydt = np.zeros(3)

  dydt[0] = - 0.04 * y1 + 10000.0 * y2 * y3
  dydt[1] =   0.04 * y1 - 10000.0 * y2 * y3 - 30000000.0 * y2 * y2
  dydt[2] =                                 + 30000000.0 * y2 * y2  

  return dydt

def robertson_ode_test ( ):

#*****************************************************************************80
#
## robertson_ode_test() tests robertson_ode().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 August 2020
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
  print ( 'robertson_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test robertson_ode using scipy.integrate.solve_ivp().' )

  t0, y0, tstop = robertson_parameters ( )

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )
#
#  Use the LSODA solver, that is suitable for stiff systems.
#
  sol = solve_ivp ( robertson_deriv, tspan, y0, method = 'LSODA' )

  plt.plot ( sol.t, sol.y[0,:], linewidth = 3 )
  plt.plot ( sol.t, sol.y[1,:], linewidth = 3 )
  plt.plot ( sol.t, sol.y[2,:], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y(t)  --->' )
  plt.title ( 'Robertson ode' )
  plt.legend ( [ 'y1', 'y2', 'y3' ] )
  filename = 'robertson_ode.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = robertson_conserved ( sol.t, sol.y )

  plt.clf ( )
  plt.plot ( sol.t, h, 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  y1+y2+y3  --->' )
  plt.title ( 'Robertson ode conservation' )
  filename = 'robertson_ode_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'robertson_ode_test:' )
  print ( '  Normal end of execution.' )

  return

def robertson_parameters ( ):

#*****************************************************************************80
#
## robertson_parameters() returns the parameters of the robertson ODE.
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
  import numpy as np

  t0 = 0.0
  y0 = np.array ( [ 1.0, 0.0, 0.0 ] )
  tstop = 40.0

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
  robertson_ode_test ( )
  timestamp ( )

