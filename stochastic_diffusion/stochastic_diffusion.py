#! /usr/bin/env python3
#
def diffusivity_1d_pwc ( mc, xc, vc, mp, xp ):

#*****************************************************************************80
#
## diffusivity_1d_pwc(): piecewise constant diffusivity function in 1D.
#
#  Discussion:
#
#    A piecewise constant function is defined over NC intervals, 
#    with interval IC associated with constant value VC(I),
#    separated by NC-1 ascending sorted breakpoints.
#
#    The function is to be evaluated at NP points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MC, the number of function values.
#
#    real XC(MC-1), the breakpoints, in ascending order.
#
#    real VC(MC), the function values over each interval.
#
#    integer MP, the number of evaluation points.
#
#    real XP(MP), the evaluation points.
#
#  Output:
#
#    real VP(MP), the function value at the evaluation points.
#
  import numpy as np

  vp = np.zeros ( mp )

  for ip in range ( 0, mp ):
    kc = 0
    for ic in range ( 0, mc - 1 ):
      if ( xp[ip] < xc[ic] ):
        break
      kc = kc + 1
    vp[ip] = vc[kc]

  return vp

def diffusivity_1d_pwc_test ( ):

#*****************************************************************************80
#
## diffusivity_1d_pwc_test tests diffusivity_1d_pwc.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'diffusivity_1d_xk_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_1d_pwc.' )

  mc = 10
  xc = np.array ( [ -0.9, -0.5, -0.45, -0.1, 0.2, 0.3, 0.32, 0.7, 0.85 ] )
  vc = np.array ( [  1.0,  1.5,  3.0,   1.2, 1.0, 0.8, 0.2,  0.4, 0.8, 1.0 ] )
#
#  Set the spatial grid.
#
  mp = 100
  x_min = -1.0
  x_max = +1.0
  xp = np.linspace ( x_min, x_max, mp )
  vp = diffusivity_1d_pwc ( mc, xc, vc, mp, xp )
#
#  Plot the diffusivity field.
#
  plt.plot ( xp, vp, linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( 'rho(X)' )
  plt.title ( 'PWC 1D Stochastic diffusivity function' )
  filename = 'diffusivity_1d_pwc.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_1d_pwc_test:' )
  print ( '  Normal end of execution.' )
  return

def diffusivity_1d_xk ( dc0, m, omega, n, x ):

#*****************************************************************************80
#
## DIFFUSIVITY_1D_XK evaluates a 1D stochastic diffusivity function.
#
#  Discussion:
#
#    The 1D diffusion equation has the form
#
#      - d/dx ( DC(X) Del U(X) ) = F(X)
#
#    where DC(X) is a function called the diffusivity.
#
#    In the stochastic version of the problem, the diffusivity function
#    includes the influence of stochastic quantities:
#
#      - d/dx ( DC(XOMEGA) d/dx U(X) ) = F(X).
#
#    In this function, the domain is assumed to be the unit interval [0.1].
#
#
#    For DC0 = 1 and F(X) = 0, with boundary conditions U(0:OMEGA) = 0,
#    U(1OMEGA) = 1, the exact solution is
#
#    If OMEGA ~= 0:
#
#      U(XOMEGA) = log ( 1 + OMEGA * X ) / log ( 1 + OMEGA )
#
#    If OMEGA = 0:
#
#      U(XOMEGA) = X
#
#    In the numerical experiments described in the paper, OMEGA was taken
#    to be a random variable with a Beta, or Uniform, or Gaussian or 
#    Poisson or Binomial distribution.
#
#    For the Gaussian and Poisson distributions, the positivity requirement could not
#    be guaranteed, and the experiments were simply made with a "small"
#    variance of 0.1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 December 2009
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dongbin Xiu, George Karniadakis,
#    Modeling uncertainty in steady state diffusion problems via
#    generalized polynomial chaos,
#    Computer Methods in Applied Mechanics and Engineering,
#    Volume 191, 2002, pages 4927-4948.
#
#  Input:
#
#    real DC0, the constant term in the expansion of the 
#    diffusion coefficient.
#
#    integer M, the number of stochastic parameters.
#
#    real OMEGA(M), the stochastic parameters.  
#
#    integer N, the number of evaluation points.
#
#    real X(N), the point where the diffusion coefficient is to 
#    be evaluated.
#
#  Output:
#
#    real DC(N), the value of the diffusion coefficient at X.
#
  import numpy as np

  k = 0
  w = 1.0
  arg = np.zeros(n)

  while ( k < m ):

    if ( k < m ):
      arg = arg + omega[k] * np.sin ( w * np.pi * x )
      k = k + 1

    if ( k < m ):
      arg = arg + omega[k] * np.cos ( w * np.pi * x )    
      k = k + 1

    w = w + 1.0

  arg = np.exp ( - 0.125 ) * arg

  dc = dc0 + np.exp ( arg )

  return dc

def diffusivity_1d_xk_contour ( ):

#*****************************************************************************80
#
## diffusivity_1d_xk_contour displays contour plots of a 1D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is compute by DIFFUSIVITY_1D_XK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dongbin Xiu, George Karniadakis,
#    Modeling uncertainty in steady state diffusion problems via
#    generalized polynomial chaos,
#    Computer Methods in Applied Mechanics and Engineering,
#    Volume 191, 2002, pages 4927-4948.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'diffusivity_1d_xk_contour' )
  print ( '  Display the stochastic diffusivity function' )
  print ( '  defined by DIFFUSIVITY_1D_XK.' )
#
#  Set the spatial grid.
#
  n = 51
  x_min = -1.0
  x_max = +1.0
  x = np.linspace ( x_min, x_max, n )
#
#  Sample the OMEGA values.
#
  m = 5
  omega = np.random.randn ( m )
#
#  Compute the diffusivity field.
#
  dc0 = 10.0
  dc = diffusivity_1d_xk ( dc0, m, omega, n, x )
#
#  Plot the diffusivity field.
#
  plt.plot ( x, dc, linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( 'DC(X)' )
  plt.title ( 'XK Stochastic diffusivity function' )
  filename = 'diffusivity_1d_xk.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def diffusivity_1d_xk_test ( ):

#*****************************************************************************80
#
## diffusivity_1d_xk_test tests diffusivity_1d_xk.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'diffusivity_1d_xk_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_1d_xk.' )

  diffusivity_1d_xk_contour ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_1d_xk_test:' )
  print ( '  Normal end of execution.' )
  return

def diffusivity_2d_bnt ( dc0, omega, n, x, y ):

#*****************************************************************************80
#
## DIFFUSIVITY_2D_BNT evaluates a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The 2D diffusion equation has the form
#
#      - Del ( DC(X,Y) Del U(X,Y) ) = F(X,Y)
#
#    where DC(X,Y) is a function called the diffusivity.
#
#    In the stochastic version of the problem, the diffusivity function
#    includes the influence of stochastic quantities:
#
#      - Del ( DC(X,YOMEGA) Del U(X,YOMEGA) ) = F(X,Y).
#
#    In this function, the domain is the rectangle [-1.5,0]x[-0.4,0.8].
#
#    The four stochastic parameters OMEGA(1:4) are assumed to be independent
#    identically distributed random variables with mean value zero and 
#    variance 1.  The distribution is typically taken to be Gaussian or
#    uniform.
#
#    A collocation approach to this problem would then use the roots of
#    Hermite or Legendre polynomials.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ivo Babuska, Fabio Nobile, Raul Tempone,
#    A stochastic collocation method for elliptic partial differential equations
#    with random input data,
#    SIAM Journal on Numerical Analysis,
#    Volume 45, Number 3, 2007, pages 1005-1034.
#
#  Input:
#
#    real DC0, the constant term in the expansion of the 
#    diffusion coefficient.  Take DC0 = 10.
#
#    real OMEGA(4), the stochastic parameters.
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the points where the diffusion coefficient is to 
#    be evaluated.
#
#  Output:
#
#    real DC(N), the value of the diffusion coefficient at (X,Y).
#
  import numpy as np

  arg = omega[0] * np.cos ( np.pi * x ) \
      + omega[1] * np.sin ( np.pi * x ) \
      + omega[2] * np.cos ( np.pi * y ) \
      + omega[3] * np.sin ( np.pi * y )

  arg = np.exp ( - 0.125 ) * arg

  dc = dc0 + np.exp ( arg )

  return dc

def diffusivity_2d_bnt_contour ( ):

#*****************************************************************************80
#
## diffusivity_2d_bnt_contour displays contour plots of a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is compute by DIFFUSIVITY_2D_BNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ivo Babuska, Fabio Nobile, Raul Tempone,
#    A stochastic collocation method for elliptic partial differential equations
#    with random input data,
#    SIAM Journal on Numerical Analysis,
#    Volume 45, Number 3, 2007, pages 1005-1034.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import numpy as np

  print ( '' )
  print ( 'diffusivity_2d_bnt_contour' )
  print ( '  Display contour or surface plots of the stochastic' )
  print ( '  diffusivity function defined by DIFFUSIVITY_2D_BNT.' )
#
#  Set the spatial grid.
#
  nx = 151
  ny = 121

  x_1d = np.linspace ( -1.5, 0.0, nx )
  y_1d = np.linspace ( -0.4, 0.8, ny )

  X, Y = np.meshgrid ( x_1d, y_1d )
#
#  Sample OMEGA.
#
  m = 4
  omega = np.random.rand ( m )
#
#  Compute the diffusivity field, using a uniform OMEGA.
#
  dc0 = 10.0
  n = nx * ny
  DC = diffusivity_2d_bnt ( dc0, omega, n, X, Y )
#
#  Plot the diffusivity field as a surface plot.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, DC, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( 'Y' )
  ax.set_ylabel ( 'X' )
  ax.set_zlabel ( 'DC(X,Y)' )
  ax.set_title ( 'BNT Stochastic diffusivity function' )
  filename = 'diffusivity_2d_bnt.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def diffusivity_2d_bnt_test ( ):

#*****************************************************************************80
#
## diffusivity_2d_bnt_test tests diffusivity_2d_bnt.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'diffusivity_2d_bnt_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_2d_bnt.' )

  diffusivity_2d_bnt_contour ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_2d_bnt_test:' )
  print ( '  Normal end of execution.' )
  return

def diffusivity_2d_elman ( a, cl, dc0, m_1d, omega, n1, n2, x, y ):

#*****************************************************************************80
#
## diffusivity_2d_elman evaluates a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The 2D diffusion equation has the form
#
#      - Del ( DC(X,Y) Del U(X,Y) ) = F(X,Y)
#
#    where DC(X,Y) is a function called the diffusivity.
#
#    In the stochastic version of the problem, the diffusivity function
#    includes the influence of stochastic quantities:
#
#      - Del ( DC(X,YOMEGA) Del U(X,YOMEGA) ) = F(X,Y).
#
#    In this function, the domain is assumed to be the square [-A,+A]x[-A,+A].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Howard Elman, Darran Furnaval,
#    Solving the stochastic steady-state diffusion problem using multigrid,
#    IMA Journal on Numerical Analysis,
#    Volume 27, Number 4, 2007, pages 675-688.
#
#    Roger Ghanem, Pol Spanos,
#    Stochastic Finite Elements: A Spectral Approach,
#    Revised Edition,
#    Dover, 2003,
#    ISBN: 0486428184,
#    LC: TA347.F5.G56.
#
#  Input:
#
#    real A, the "radius" of the square region.  The region
#    is assumed to be [-A,+A]x[-A,+A].
#    0 < A.
#
#    real CL, the correlation length.
#    0 < CL.
#
#    real DC0, the constant term in the expansion of the 
#    diffusion coefficient.  Take DC0 = 10.
#
#    integr M_1D, the first and second dimensions of the stochastic
#    parameter array.
#
#    real OMEGA(M_1D*M_1D), the stochastic parameters.
#
#    integer N1, N2, the dimensions of the X and Y arrays.
#
#    real X(N1,N2), Y(N1,N2), the points where the diffusion 
#    coefficient is to be evaluated.
#
#  Output:
#
#    real DC(N1,N2), the value of the diffusion coefficient at X.
#
  import numpy as np
#
#  Compute THETA.
#
  theta_1d = theta_solve ( a, cl, m_1d )
#
#  Compute LAMBDA_1D.
#
  lambda_1d = 2.0 * cl / ( 1.0 + cl ** 2 * theta_1d ** 2 )
#
#  Compute C_1DX(1:M1D)  and C_1DY(1:M1D) at (X,Y).
#
  c_1dx = np.zeros ( [ m_1d, n1, n2 ] )
  c_1dy = np.zeros ( [ m_1d, n1, n2 ] )

  k = -1

  while ( True ):

    k = k + 1

    if ( m_1d <= k ):
      break

    c_1dx[k,0:n1,0:n2] = np.cos ( theta_1d[k] * a * x[0:n1,0:n2] ) \
      / np.sqrt ( a + np.sin ( 2.0 * theta_1d[k] * a ) / ( 2.0 * theta_1d[k] ) )
    c_1dy[k,0:n1,0:n2] = np.cos ( theta_1d[k] * a * y[0:n1,0:n2] ) \
      / np.sqrt ( a + np.sin ( 2.0 * theta_1d[k] * a ) / ( 2.0 * theta_1d[k] ) )

    k = k + 1

    if ( m_1d <= k ):
      break

    c_1dx[k,0:n1,0:n2] = np.sin ( theta_1d[k] * a * x[0:n1,0:n2] ) \
      / np.sqrt ( a - np.sin ( 2.0 * theta_1d[k] * a ) / ( 2.0 * theta_1d[k] ) )
    c_1dy[k,0:n1,0:n2] = np.sin ( theta_1d[k] * a * y[0:n1,0:n2] ) \
      / np.sqrt ( a - np.sin ( 2.0 * theta_1d[k] * a ) / ( 2.0 * theta_1d[k] ) )
#
#  Evaluate the diffusion coefficient DC at (X,Y).
#  This nonsense of fussy array shapes really frustrates me!
#
  k = 0
  dc3 = dc0 * np.ones ( [ 1, n1, n2 ] )
  for j in range ( 0, m_1d ):
    for i in range ( 0, m_1d ):
      dc3[0,0:n1,0:n2] = dc3[0,0:n1,0:n2] + np.sqrt ( lambda_1d[i] * lambda_1d[j] ) \
        * c_1dx[i,0:n1,0:n2] * c_1dy[j,0:n1,0:n2] * omega[k]
      k = k + 1

  dc = np.zeros ( [ n1, n2 ] )
  dc[0:n1,0:n2] = dc3[0,0:n1,0:n2]

  return dc

def theta_solve ( a, cl, m ):

#*****************************************************************************80
#
## theta_solve solves a pair of transcendental equations.
#
#  Discussion:
#
#    The vector THETA returned by this function is needed in order to define
#    the terms in a Karhunen-Loeve expansion of a diffusion coefficient.
#
#    The two equations are:
#
#      1/CL - THETA * TAN ( A * THETA ) = 0
#      THETA - 1/CL * TAN ( A * THETA ) = 0
#
#    A and CL are taken to be positive.  Over each open interval 
#
#      ( n - 1/2 pi, n + 1/2 pi ) / A, for N = 0, 1, ...
#
#    the function TAN ( A * THETA ) monotonically rises from -oo to +00 
#    therefore, it can be shown that there is one root of each equation 
#    in every interval of this form.  Moreover, because of the positivity
#    of A and CL, we can restrict our search to the interval 
#
#      [ n pi, n + 1/2 pi ) / A, for N = 0, 1, ...
#
#    This function computes K such roots, starting in the first interval,
#    finding those two roots, moving to the next interval, and so on, until
#    the requested number of roots have been found.  Odd index roots will
#    correspond to the first equation, and even index roots to the second.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Howard Elman, Darran Furnival,
#    Solving the Stochastic Steady-State Diffusion Problem Using Multigrid,
#    University of Maryland Department of Computer Science,
#    Technical Report TR-4786.
#
#  Input:
#
#    real A, the "radius" of the domain, D = (-A,A)x(-A,A).
#    0 < A.
#
#    real CL, the correlation length.
#    0 < CL.
#
#    integer M, the number of values to compute.
#
#  Output:
#
#    real THETA(M), the values of Theta.
#
  import numpy as np

  eps = np.finfo(float).eps

  k = -1
  theta = np.zeros ( m )
#
#  [ XA_INIT, XB_INIT] = [ n * pi, n+1/2 pi ] / a, n = 0, 1, 2, ...
#
  xa_init = 0.0
  xb_init = ( np.pi / 2.0 ) / a

  while ( True ):
#
#  Seek root of equation 1 in interval.
#
    k = k + 1

    if ( m <= k ):
      break

    xa = xa_init
    fa = 1.0 / cl - xa * np.tan ( a * xa )
    ftol = eps * ( abs ( fa ) + 1.0 )
    xb = xb_init
    fb = - fa
    fc = fa
    bmatol = 100.0 * eps * ( abs ( xa ) + abs ( xb ) )

    while ( bmatol < xb - xa ):

      xc = ( xa + xb ) / 2.0
      fc = 1.0 / cl - xc * np.tan ( a * xc )

      if ( abs ( fc ) <= ftol ):
        break
      elif ( 0 < fc ):
        xa = xc
      else:
        xb = xc

    theta[k] = xc
#
#  Seek root of equation 2 in interval.
#
    k = k + 1
    if ( m <= k ):
      break
#
#  In the first interval, we need to skip the zero root of equation 2.
#
    if ( k == 1 ):

      k = k - 1

    else:

      xa = xa_init
      fa = xa - np.tan ( a * xa ) / cl
      ftol = eps * ( abs ( fa ) + 1.0 )
      xb = xb_init
      fb = - fa

      while ( bmatol < xb - xa ):

        xc = ( xa + xb ) / 2.0
        fc = xc - np.tan ( a * xc ) / cl

        if ( abs ( fc ) <= ftol ):
          break
        elif ( 0.0 < fc ):
          xa = xc
        else:
          xb = xc

      theta[k] = xc
#
#  Advance the interval.
#
    xa_init = xa_init + np.pi / a
    xb_init = xb_init + np.pi / a

  return theta

def diffusivity_2d_elman_contour ( ):

#*****************************************************************************80
#
## diffusivity_2d_elman_contour displays a contour plot of a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is compute by DIFFUSIVITY_2D_ELMAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Howard Elman, Darran Furnaval,
#    Solving the stochastic steady-state diffusion problem using multigrid,
#    IMA Journal on Numerical Analysis,
#    Volume 27, Number 4, 2007, pages 675-688.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import numpy as np

  print ( '' )
  print ( 'diffusivity_2d_elman_contour' )
  print ( '  Display contour or surface plots of the stochastic' )
  print ( '  diffusivity function defined by DIFFUSIVITY_2D_ELMAN.' )
#
#  Specify the X and Y evaluation points.
#
  nx = 51
  a = 1.0
  xvec = np.linspace ( -a, +a, nx )
  yvec = np.linspace ( -a, +a, nx )

  X, Y = np.meshgrid ( xvec, yvec )
#
#  Sample OMEGA.
#
  m_1d = 5
  msq = m_1d * m_1d
  omega = np.random.randn ( msq )
#
#  Compute the diffusivity field.
#
  cl = 0.1
  ac0 = 10.0
  A = diffusivity_2d_elman ( a, cl, ac0, m_1d, omega, nx, nx, X, Y )
#
#  Make a surface plot.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, A, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( 'Y' )
  ax.set_ylabel ( 'X' )
  ax.set_zlabel ( 'DC(X,Y)' )
  ax.set_title ( 'ELMAN Stochastic diffusivity function' )
  filename = 'diffusivity_2d_elman.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def diffusivity_2d_elman_test ( ):

#*****************************************************************************80
#
## diffusivity_2d_elman_test tests diffusivity_2d_elman.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'diffusivity_2d_elman_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_2d_elman.' )

  diffusivity_2d_elman_contour ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_2d_elman_test:' )
  print ( '  Normal end of execution.' )
  return

def diffusivity_2d_jvb ( a0, m, omega, n, x, y ):

#*****************************************************************************80
#
## diffusivity_2d_jvb evaluates a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The 2D stochastic diffusion equation has the form
#
#      - Del ( A(X,Y;OMEGA) Del U(X,Y;OMEGA) ) = F(X,Y).
#
#    The stochastic parameters OMEGA(1:4*M) are assumed to be independent
#    identically distributed random variables with mean value zero and 
#    variance 1.  The distribution is typically taken to be Gaussian or
#    uniform.
#
#    For physical and mathematical reasons, the diffusivity function 
#    A(X,Y;OMEGA) must be positive.  Our random KL expansion can guarantee
#    this by using an exponential format:
#
#      A(X,Y;OMEGA) = A0 + exp ( sum(j=1:4*m) OMEGA(J) * PSI(J)(X,Y) )
#
#    This function generalizes the 4-term expansion in diffusivity_2d_bnt,
#    used by Babuska, Nobile, Tempone, to a 4*M term expansion.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ivo Babuska, Fabio Nobile, Raul Tempone,
#    A stochastic collocation method for elliptic partial differential equations
#    with random input data,
#    SIAM Journal on Numerical Analysis,
#    Volume 45, Number 3, 2007, pages 1005-1034.
#
#  Input:
#
#    real A0, the constant term in the expansion.
#
#    integer M, controls the number of values OMEGA.
#    0 <= M.
#
#    real OMEGA(4*M), the stochastic parameters.
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the points where the diffusion coefficient is to 
#    be evaluated.
#
#  Output:
#
#    real A(N), the value of the diffusion coefficient at (X,Y).
#
  import numpy as np

  ma, na = x.shape
  arg = np.zeros ( [ ma, na ] )
  
  for j in range ( 0, m ):
#
#  Reduce strength of higher order terms.
#
    jsq = 1.0 / ( float ( j + 1 ) ) ** 2;

    arg = arg + jsq * ( \
        omega[4* j ] * np.cos ( ( j + 1 ) * np.pi * x ) \
      + omega[4*j+1] * np.sin ( ( j + 1 ) * np.pi * x ) \
      + omega[4*j+2] * np.cos ( ( j + 1 ) * np.pi * y ) \
      + omega[4*j+3] * np.sin ( ( j + 1 ) * np.pi * y ) )
#
#  Add the (positive) terms.
#
  a = a0 + np.exp ( arg );

  return a

def diffusivity_2d_jvb_contour ( m ):

#*****************************************************************************80
#
## diffusivity_2d_jvb_contour displays contour plots of a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is compute by DIFFUSIVITY_2D_BNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ivo Babuska, Fabio Nobile, Raul Tempone,
#    A stochastic collocation method for elliptic partial differential equations
#    with random input data,
#    SIAM Journal on Numerical Analysis,
#    Volume 45, Number 3, 2007, pages 1005-1034.
#
#  Input:
#
#    integer M, controls the number of random coefficients, which
#    will be 4*M.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import numpy as np

  print ( '' )
  print ( 'diffusivity_2d_jvb_contour' )
  print ( '  Display contour or surface plots of the stochastic' )
  print ( '  diffusivity function defined by diffusivity_2d_jvb.' )
#
#  Set the spatial grid.
#
  nx = 101
  ny = 101

  x_1d = np.linspace ( -1.0, 0.0, nx )
  y_1d = np.linspace ( -1.0, 1.0, ny )

  X, Y = np.meshgrid ( x_1d, y_1d )
#
#  Compute the diffusivity field, using a uniform OMEGA.
#
  a0 = 2.0
  omega = -1.0 + 2.0 * np.random.rand ( 4 * m )
  n = nx * ny
  A = diffusivity_2d_jvb ( a0, m, omega, n, X, Y )
#
#  Plot the diffusivity field as a surface plot.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, A, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( 'Y' )
  ax.set_ylabel ( 'X' )
  ax.set_zlabel ( 'A(X,Y)' )
  ax.set_title ( 'JVB Stochastic diffusivity function' )
  filename = 'diffusivity_2d_jvb.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def diffusivity_2d_jvb_test ( ):

#*****************************************************************************80
#
## diffusivity_2d_jvb_test tests diffusivity_2d_jvb.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'diffusivity_2d_jvb_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_2d_jvb.' )

  m = 3
  diffusivity_2d_jvb_contour ( m )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_2d_jvb_test:' )
  print ( '  Normal end of execution.' )
  return

def diffusivity_2d_ntw ( cl, a0, m, omega, n, x, y ):

#*****************************************************************************80
#
## diffusivity_2d_ntw evaluates a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The 2D diffusion equation has the form
#
#      - Del ( DC(X,Y) Del U(X,Y) ) = F(X,Y)
#
#    where DC(X,Y) is a function called the diffusivity.
#
#    In the stochastic version of the problem, the diffusivity function
#    includes the influence of stochastic quantities:
#
#      - Del ( DC(X,YOMEGA) Del U(X,YOMEGA) ) = F(X,Y).
#
#    In this function, the domain is the rectangle [0,D]x[0,D] where D = 1.
#
#    Note that in this problem the diffusivity has a one-dimensional
#    spatial dependence on X, but not on Y!
#
#    The random variables OMEGA are independent, have zero mean and unit
#    variance, and are uniformly distributed in [-sqrt(3),+sqrt(3)].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Xiang Ma, Nicholas Zabaras,
#    An adaptive hierarchical sparse grid collocation algorithm for the solution
#    of stochastic differential equations,
#    Journal of Computational Physics,
#    Volume 228, pages 3084-3113, 2009.
#
#    Fabio Nobile, Raul Tempone, Clayton Webster,
#    A Sparse Grid Stochastic Collocation Method for Partial Differential
#    Equations with Random Input Data,
#    SIAM Journal on Numerical Analysis,
#    Volume 46, Number 5, 2008, pages 2309-2345.
#
#  Input:
#
#    real CL, the desired physical correlation length for the
#    coefficient.
#
#    real A0, the constant term in the expansion of the 
#    diffusion coefficient.  Take A0 = 0.5.
#
#    integer M, the number of terms in the expansion.
#
#    real OMEGA(M), the stochastic parameters.
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the points where the diffusion coefficient is to 
#    be evaluated.
#
#  Output:
#
#    real A(N), the value of the diffusion coefficient at (X,Y).
#
  import numpy as np

  d = 1.0
  lp = max ( d, 2.0 * cl )
  l = cl / lp

  dc_arg = 1.0 + omega[0] * np.sqrt ( np.sqrt ( np.pi ) * l / 2.0 )

  for i in range ( 2, m + 1 ):

    zeta_arg = - ( np.floor ( i / 2 ) * np.pi * l ) ** 2 / 8.0
    zeta = np.sqrt ( np.sqrt ( np.pi ) * l ) * np.exp ( zeta_arg )

    if ( np.mod ( i, 2 ) == 0 ):
      phi = np.sin ( np.floor ( i / 2 ) * np.pi * x / lp )
    else:
      phi = np.cos ( np.floor ( i / 2 ) * np.pi * x / lp )

    dc_arg = dc_arg + zeta * phi * omega[i-1]

  A = a0 + np.exp ( dc_arg )

  return A

def diffusivity_2d_ntw_contour ( ):

#*****************************************************************************80
#
## diffusivity_2d_ntw_contour displays a contour plot of a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is compute by diffusivity_2d_ntw.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Fabio Nobile, Raul Tempone, Clayton Webster,
#    A Sparse Grid Stochastic Collocation Method for Partial Differential
#    Equations with Random Input Data,
#    SIAM Journal on Numerical Analysis,
#    Volume 46, Number 5, 2008, pages 2309-2345.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import numpy as np

  print ( '' )
  print ( 'diffusivity_2d_ntw_contour' )
  print ( '  Display contour or surface plots of the stochastic' )
  print ( '  diffusivity function defined by diffusivity_2d_ntw.' )
#
#  Set the spatial grid.
#
  nx = 101
  ny = 101
  xvec = np.linspace ( 0.0, 1.0, nx )
  yvec = np.linspace ( 0.0, 1.0, ny )

  X, Y = np.meshgrid ( xvec, yvec )
#
#  Evaluate the diffusivity field.
#
  cl = 0.1
  a0 = 0.5
  m = 21
  omega = np.random.rand ( m )
  omega = ( 1.0 - omega ) * ( - np.sqrt ( 3.0 ) ) \
        +         omega   *     np.sqrt ( 3.0 )
  n = nx * ny

  A = diffusivity_2d_ntw ( cl, a0, m, omega, n, X, Y )
#
#  Make a surface plot of the diffusivity coefficient.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, A, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( 'Y' )
  ax.set_ylabel ( 'X' )
  ax.set_zlabel ( 'DC(X,Y)' )
  ax.set_title ( 'NTW Stochastic diffusivity function' )
  filename = 'diffusivity_2d_ntw.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def diffusivity_2d_ntw_test ( ):

#*****************************************************************************80
#
## diffusivity_2d_ntw_test tests diffusivity_2d_ntw.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'diffusivity_2d_ntw_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_2d_ntw.' )

  diffusivity_2d_ntw_contour ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_2d_ntw_test:' )
  print ( '  Normal end of execution.' )
  return

def diffusivity_2d_pwc ( h, w, a, b, c, d, omega, n, x, y ):

#*****************************************************************************80
#
## diffusivity_2d_pwc evaluates a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The 2D stochastic diffusion equation has the form
#
#      - Del ( RHO(X,Y;OMEGA) Del U(X,Y;OMEGA) ) = F(X,Y).
#
#    Here, the diffusivity RHO is assumed to be a piecewise constant function,
#    defined on rectangular grid over [A,B]x[C,D] that is H cells high
#    and W cells wide.  The parameters OMEGA(H*W) are assumed to be given 
#    positive values that are bounded away from 0.
#
#    The underlying grid is assumed to be equally spaced, so each cell
#    is (D-C)/M units high and (B-A)/N wide.
#
#       ^  ^  +-------+-------+-------+-------+
#       D  H  | (H,1) | (H,2) | ----- | (H,W) |
#       |  |  +-------+-------+-------+-------+
#             | ----- | ----- | (I,J) | ----- |
#       Y  I  +-------+-------+-------+-------+
#             | (2,1) | (2,2) | ----- | (2,W) |
#       |  |  +-------+-------+-------+-------+
#       |  |  | (1,1) | (1,2) | ----- | (1,W) |
#       C  1  +-------+-------+-------+-------+
#       |  |
#       +--+--1-------------- J --------------W->
#       +--+--A-------------- X --------------B->
#
#    Indexing is tricky, since our (X,Y) coordinate system indexing and
#    conventions for indexing an array and for ordering indices do not
#    match up.  An arbitrary choice must be made, and here we associate
#    "width" and "X" and "J", as well as "height" and "Y" and "I".
#    We start in the lower left corner, and proceed right first, and
#    then move up one row.
#
#    The following coordinate systems are available:
#
#    * cell index (I,J):  (1,1) <= (I,J) <= (H,W). 
#      I refers to "height" and J to "width".
#
#    * cell counter K:    1     <= K     <= H*W
#      Count from lower left to lower right, then
#      go up one row.
#
#    * physical cell center coordinates (XC,YC)
#      the (X,Y) coordinates of the centers of a cell
#
#    * physical coordinates (X,Y) in [A,B]x[C,D].
#      the (X,Y) coordinates of any point
#      
#    * normalized coordinates (X01,Y01) in [0,1]x[0,1].
#   
#    Transformations from one coordinate system to another:
#
#    * (I,J) --> (XC,YC)
#                X01 = (2*J-1)/2/W
#                Y01 = (2*I-1)/2/H
#                XC = A + (B-A) * X01
#                YC = C + (D-C) * Y01
#
#    * (I,J) --> K
#                K = (I-1)*W+J
#
#    * K     --> (I,J)
#                I = floor ( K - 1 ) / W ) + 1
#                J = mod ( K - 1, W ) + 1
#
#    * K     --> (XC,YC)
#                I = floor ( K - 1 ) / W ) + 1
#                J = mod ( K - 1, W ) + 1
#                X01 = (2*J-1)/2/W
#                Y01 = (2*I-1)/2/H
#                XC = A + (B-A) * X01
#                YC = C + (D-C) * Y01
#
#    * (X,Y) --> (I,J)
#                X01 = ( X - A ) / ( B - A )
#                Y01 = ( Y - C ) / ( D - C )
#                I = round ( ( 2 * h * Y01 + 1 ) / 2 );
#                J = round ( ( 2 * w * X01 + 1 ) / 2 );
#
#    * (X,Y) --> K
#                X01 = ( X - A ) / ( B - A )
#                Y01 = ( Y - C ) / ( D - C )
#                I = round ( ( 2 * h * Y01 + 1 ) / 2 );
#                J = round ( ( 2 * w * X01 + 1 ) / 2 );
#                K = (I-1)*W+J
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer H, W, specifies the number of elements.
#
#    real A, B, the lower and upper limits of X.
#
#    real C, D, the lower and upper limits of Y.
#
#    real OMEGA(H*W), the parameters.
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the points where the diffusion coefficient is to 
#    be evaluated.
#
#  Output:
#
#    real RHO(N), the value of the diffusion coefficient at each point.
#
  import numpy as np

  drat = x.shape
  n1 = drat[0]
  n2 = drat[1]

  rho = x.copy( )
  
  for ii in range ( 0, n1 ):
    for jj in range ( 0, n2 ):

      x01 = ( x[ii,jj] - a ) / ( b - a )
      y01 = ( y[ii,jj] - c ) / ( d - c )

      i = int ( np.round ( ( 2 * h * y01 - 1 ) / 2 ) )
      i = max ( i, 0 )
      i = min ( i, h - 1 )

      j = int ( np.round ( ( 2 * w * x01 - 1 ) / 2 ) )
      j = max ( j, 0 )
      j = min ( j, w - 1 )

      k = i * w + j

      rho[ii,jj] = omega[k]
 
  return rho

def diffusivity_2d_pwc_contour ( h, w, a, b, c, d ):

#*****************************************************************************80
#
## diffusivity_2d_pwc_contour displays contour plots of a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is computed by diffusivity_2d_pwc.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer H, W, the height and width of the element grid.
#
#    float A, B, C, D, the lower and upper limits of X, and of Y.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import numpy as np

  print ( '' )
  print ( 'diffusivity_2d_pwc_contour' )
  print ( '  Display contour or surface plots of the stochastic' )
  print ( '  diffusivity function defined by diffusivity_2d_pwc.' )
  print ( '' )
  print ( '  Underlying grid is %d elements wide (X) and %d high (Y)' % ( w, h ) )
#
#  Set the spatial grid.
#
  nx = 101
  ny = 101

  x_1d = np.linspace ( a, b, nx )
  y_1d = np.linspace ( c, d, ny )

  X, Y = np.meshgrid ( x_1d, y_1d )
#
#  Sample OMEGA.
#
  omega = 1.0 - 0.5 * np.random.rand ( h * w )
#
#  Compute the diffusivity field, using a uniform OMEGA.
#
  n = nx * ny
  RHO = diffusivity_2d_pwc ( h, w, a, b, c, d, omega, n, X, Y );
#
#  Plot the diffusivity field as a surface plot.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, RHO, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( 'Y' )
  ax.set_ylabel ( 'X' )
  ax.set_zlabel ( 'Rho(X,Y)' )
  ax.set_title ( 'PWC Stochastic diffusivity function' )
  filename = 'diffusivity_2d_pwc.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def diffusivity_2d_pwc_test ( ):

#*****************************************************************************80
#
## diffusivity_2d_pwc_test tests diffusivity_2d_pwc.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 March 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'diffusivity_2d_pwc_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_2d_pwc.' )

  h = 5
  w = 4
  a = - 1.0
  b = + 1.0
  c = - 1.0
  d = + 1.0

  diffusivity_2d_pwc_contour ( h, w, a, b, c, d )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_2d_pwc_test:' )
  print ( '  Normal end of execution.' )
  return

def stochastic_diffusion_test ( ):

#*****************************************************************************80
#
## stochastic_diffusion_test tests stochastic_diffusion.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 March 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'stochastic_diffusion_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test stochastic_diffusion.' )

  diffusivity_1d_pwc_test ( )
  diffusivity_1d_xk_test ( )
  diffusivity_2d_bnt_test ( )
  diffusivity_2d_elman_test ( )
  diffusivity_2d_jvb_test ( )
  diffusivity_2d_ntw_test ( )
  diffusivity_2d_pwc_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'stochastic_diffusion_test:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
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
  stochastic_diffusion_test ( )
  timestamp ( )

