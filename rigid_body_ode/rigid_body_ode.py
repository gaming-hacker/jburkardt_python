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

def rk4 ( dydt, tspan, y0, n ):

#*****************************************************************************80
#
## rk4() approximates the solution to an ODE using the RK4 method.
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

    f1 = dydt ( t[i],            y[i,:] )
    f2 = dydt ( t[i] + dt / 2.0, y[i,:] + dt * f1 / 2.0 )
    f3 = dydt ( t[i] + dt / 2.0, y[i,:] + dt * f2 / 2.0 )
    f4 = dydt ( t[i] + dt,       y[i,:] + dt * f3 )

    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] + dt * ( f1 + 2.0 * f2 + 2.0 * f3 + f4 ) / 6.0

  return t, y

def rigid_body_conserved ( xyz ):

#*****************************************************************************80
#
## rigid_body_conserved() evaluates conserved quantities for the rigid body ODE.
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
#  Reference:
#
#    Ernst Hairer,
#    Solving differential equations on manifolds,
#    Universite de Geneve,
#    June 2011.
#
#  Input:
#
#    real XYZ[:,3]: the current coordinates.
#
#  Output:
#
#    real H1[:], H2[]: the conserved quantities.
#
  import numpy as np

  i1, i2, i3, t0, xyz0, tstop = rigid_body_parameters ( )

  x = xyz[:,0]
  y = xyz[:,1]
  z = xyz[:,2]

  h1 = x**2 + y**2 + z**2

  h2 = x**2 / i1 + y**2 / i2 + z**2 / i3

  return h1, h2

def rigid_body_deriv ( t, xyz ):

#*****************************************************************************80
#
## rigid_body_deriv() evaluates the derivative of the rigid body ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ernst Hairer,
#    Solving differential equations on manifolds,
#    Universite de Geneve,
#    June 2011.
#
#    Ernst Hairer, Christian Lubich, Gerhard Wanner,
#    Geometric numerical integration,
#    Springer, 2006.
#
#  Input:
#
#    real T, XYZ[3]: the arguments of the derivative.
#
#  Output:
#
#    real DXYZDT[3]: the value of the derivative.
#
  import numpy as np

  i1, i2, i3, t0, xyz0, tstop = rigid_body_parameters ( )

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  dxdt = ( 1.0 / i3 - 1.0 / i2 ) * z * y
  dydt = ( 1.0 / i1 - 1.0 / i3 ) * x * z
  dzdt = ( 1.0 / i2 - 1.0 / i1 ) * y * x

  dxyzdt = np.array ( [ dxdt, dydt, dzdt ] )

  return dxyzdt

def rigid_body_euler ( tspan, xyz0, n ):

#*****************************************************************************80
#
## rigid_body_euler() solves the rigid body ODE using the Euler method.
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
#    real tspan[2]: the time span
#
#    real xyz0[3]: the initial condition.
#
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'rigid_body_euler():' )
  print ( '  Solve the rigid body ODE using euler().' )

  t, xyz = euler ( rigid_body_deriv, tspan, xyz0, n )

  plt.plot ( t, xyz, linewidth = 3 )

  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- X, Y, Z --->' )
  plt.title ( 'rigid body euler: time plot' )
  plt.legend ( [ 'X(t)', 'Y(t)', 'Z(t)' ] )
  filename = 'rigid_body_euler_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h1, h2 = rigid_body_conserved ( xyz )

  plt.clf ( )
  plt.plot ( t, h1, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ h1[0], h1[0] ] ), 'k:', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H1(T) --->' )
  plt.title ( 'rigid body euler: conservation h1' )
  filename = 'rigid_body_euler_conservation_h1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( t, h2, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ h2[0], h2[0] ] ), 'k:', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H2(T) --->' )
  plt.title ( 'rigid body euler: conservation h2' )
  filename = 'rigid_body_euler_conservation_h2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def rigid_body_midpoint ( tspan, xyz0, n ):

#*****************************************************************************80
#
## rigid_body_midpoint() solves the rigid body ODE using the midpoint method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real tspan[2]: the time span
#
#    real xyz0[3]: the initial condition.
#
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'rigid_body_euler_test:' )
  print ( '  Solve the rigid body ODE using midpoint().' )

  t, xyz = midpoint ( rigid_body_deriv, tspan, xyz0, n )

  plt.plot ( t, xyz, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- X, Y, Z --->' )
  plt.title ( 'rigid body midpoint: time plot' )
  plt.legend ( [ 'X(t)', 'Y(t)', 'Z(t)' ] )
  filename = 'rigid_body_midpoint_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h1, h2 = rigid_body_conserved ( xyz )

  plt.plot ( t, h1, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ h1[0], h1[0] ] ), 'k:', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H1(T) --->' )
  plt.title ( 'rigid body midpoint: conservation h1' )
  filename = 'rigid_body_midpoint_conservation_h1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( t, h2, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ h2[0], h2[0] ] ), 'k:', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H2(T) --->' )
  plt.title ( 'rigid body midpoint: conservation h2' )
  filename = 'rigid_body_midpoint_conservation_h2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def rigid_body_ode_test ( ):

#*****************************************************************************80
#
## rigid_body_ode_test() solves the rigid body ODE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 April 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rigid_body_ode_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve the rigid body ODE.' )

  i1, i2, i3, t0, xyz0, tstop = rigid_body_parameters ( )

  print ( '' )
  print ( '  Parameter values:' )
  print ( '    i1    = ', i1 )
  print ( '    i2    = ', i2 )
  print ( '    i3    = ', i3 )
  print ( '    t0    = ', t0 )
  print ( '    xyz0  = ', xyz0 ) 
  print ( '    tstop = ', tstop )

  tspan = np.array ( [ t0, tstop ] )

  n = 200
  rigid_body_euler ( tspan, xyz0, n )

  n = 50
  rigid_body_midpoint ( tspan, xyz0, n )

  n = 50
  rigid_body_rk4 ( tspan, xyz0, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'rigid_body_ode_test():' )
  print ( '  Normal end of execution.' )
  return

def rigid_body_parameters ( ):

#*****************************************************************************80
#
## rigid_body_parameters() returns parameters for the rigid body ODE.
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
#    real I1: a moment of inertia.
#
#    real I2: a moment of inertia.
#
#    real I3: a moment of inertia.
#
#    real T0: the initial time.
#
#    real XYZ0(3): the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  i1 = 1.6
  i2 = 1.0
  i3 = 2.0 / 3.0
  t0 = 0.0
  x0 = np.cos ( 0.9 )
  y0 = 0.0
  z0 = np.sin ( 0.9 )
  xyz0 = np.array ( [ x0, y0, z0 ] )
  tstop = 50.0

  return i1, i2, i3, t0, xyz0, tstop

def rigid_body_rk4 ( tspan, xyz0, n ):

#*****************************************************************************80
#
## rigid_body_rk4() solves the rigid body ODE using the rk4 method.
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
#    real tspan[2]: the time span
#
#    real xyz0[3]: the initial condition.
#
#    integer n: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'rigid_body_rk4():' )
  print ( '  Solve the rigid body ODE using rk4().' )

  t, xyz = rk4 ( rigid_body_deriv, tspan, xyz0, n )

  plt.plot ( t, xyz, linewidth = 3 )

  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- X, Y, Z --->' )
  plt.title ( 'rigid body rk4: time plot' )
  plt.legend ( [ 'X(t)', 'Y(t)', 'Z(t)' ] )
  filename = 'rigid_body_rk4_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h1, h2 = rigid_body_conserved ( xyz )

  plt.plot ( t, h1, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ h1[0], h1[0] ] ), 'k:', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H1(T) --->' )
  plt.title ( 'rigid body rk4: conservation h1' )
  filename = 'rigid_body_rk4_conservation_h1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( t, h2, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ h2[0], h2[0] ] ), 'k:', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H2(T) --->' )
  plt.title ( 'rigid body rk4: conservation h2' )
  filename = 'rigid_body_rk4_conservation_h2.png'
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
  rigid_body_ode_test ( )
  timestamp ( )
 
