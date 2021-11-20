#! /usr/bin/env python3
#
def cg_rc ( n, b, x, r, z, p, q, job, iterate, rho, rho_old, rlbl ):

#*****************************************************************************80
#
## cg_rc() is a reverse communication conjugate gradient routine.
#
#  Discussion:
#
#    This routine seeks a solution of the linear system A*x=b
#    where b is a given right hand side vector, A is an n by n
#    symmetric positive definite matrix, and x is an unknown vector
#    to be determined.
#
#    Under the assumptions that the matrix A is large and sparse,
#    the conjugate gradient method may provide a solution when
#    a direct approach would be impractical because of excessive
#    requirements of storage or even of time.
#
#    The conjugate gradient method presented here does not require the
#    user to store the matrix A in a particular way.  Instead, it only
#    supposes that the user has a way of calculating
#      y = alpha * A * x + b * y
#    and of solving the preconditioned linear system
#      M * x = b
#    where M is some preconditioning matrix, which might be merely
#    the identity matrix, or a diagonal matrix containing the
#    diagonal entries of A.
#
#    This routine was extracted from the "templates" package.
#    There, it was not intended for direct access by a user
#    instead, a higher routine called "cg()" was called once by
#    the user.  The cg() routine then made repeated calls to
#    cgrevcom() before returning the result to the user.
#
#    The reverse communication feature of cgrevcom() makes it, by itself,
#    a very powerful function.  It allows the user to handle issues of
#    storage and implementation that would otherwise have to be
#    mediated in a fixed way by the function argument list.  Therefore,
#    this version of cgrecom() has been extracted from the templates
#    library and documented as a stand-alone procedure.
#
#    The user sets the value of JOB to 1 before the first call,
#    indicating the beginning of the computation, and to the value of
#    2 thereafter, indicating a continuation call.
#    The output value of JOB is set by cgrevcom(), which
#    will return with an output value of JOB that requests a particular
#    new action from the user.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Barrett, Michael Berry, Tony Chan, James Demmel,
#    June Donato, Jack Dongarra, Victor Eijkhout, Roidan Pozo,
#    Charles Romine, Henk van der Vorst,
#    Templates for the Solution of Linear Systems:
#    Building Blocks for Iterative Methods,
#    SIAM, 1994,
#    ISBN: 0898714710,
#    LC: QA297.8.T45.
#
#  Input:
#
#    integer N, the dimension of the matrix.
#
#    real B(N), the right hand side vector.
#
#    real X(N).  On first call, the user
#    should store an initial guess for the solution in X.
#
#    real R(N), Z(N), P(N), Q(N), work arrays.  The user should
#    create each of these before the first call, using the zeros() command.
#    On subsequent calls, the user may be asked to assign a value to one
#    of these vectors.
#
#    integer JOB, communicates the task to be done.
#    The user needs to set the input value of JOB to 1, before the first call,
#    and then to 2 for every subsequent call for the given problem.
#
#  Output:
#
#    real X(N), the current solution estimate.
#    Each time JOB is returned as 4, X has been updated.
#
#    real R(N), Z(N), P(N), Q(N), work arrays.  Depending on the
#    output value of JOB, the user may be asked to carry out a computation
#    involving some of these vectors.
#
#    integer JOB, communicates the task to be done.
#    * JOB = 1, compute Q = A * P
#    * JOB = 2: solve M*Z=R, where M is the preconditioning matrix
#    * JOB = 3: compute R = R - A * X
#    * JOB = 4: check the residual R for convergence.  
#               If satisfactory, terminate the iteration.
#               If too many iterations were taken, terminate the iteration.
#
  import numpy as np
#
#  Initialization.
#  Ask the user to compute the initial residual.
#
  if ( job == 1 ):

    r = b.copy ( )

    job = 3
    rlbl = 2
#
#  Begin first conjugate gradient loop.
#  Ask the user for a preconditioner solve.
#
  elif ( rlbl == 2 ):

    iter = 1

    job = 2
    rlbl = 3
#
#  Compute the direction.
#  Ask the user to compute ALPHA.
#  Save A*P to Q.
#
  elif ( rlbl == 3 ):

    rho = np.dot ( r, z )

    if ( 1 < iterate ):
      beta = rho / rho_old
      z = z + beta * p

    p = z.copy ( )

    job = 1
    rlbl = 4
#
#  Compute current solution vector.
#  Ask the user to check the stopping criterion.
#
  elif ( rlbl == 4 ):

    pdotq = np.dot ( p, q )
    alpha = rho / pdotq
    x = x + alpha * p
    r = r - alpha * q

    job = 4
    rlbl = 5
#
#  Begin the next step.
#  Ask for a preconditioner solve.
#
  elif ( rlbl == 5 ):

    rho_old = rho
    iterate = iterate + 1

    job = 2
    rlbl = 3

  return x, r, z, p, q, job, iterate, rho, rho_old, rlbl

def cg_rc_test01 ( ):

#*****************************************************************************80
#
## cg_rc_test01() uses cg_rc() for the simple 1, -2, 1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 21

  print ( '' )
  print ( 'cg_rc_test01():' )
  print ( '  Use cg_rc() on the 1, -2, 1 matrix.' )
#
#  In order to specify the right hand side, pick an exact solution,
#  and multiply by the matrix.
#
  x_exact = np.zeros ( n )
  for i in range ( 0, n ):
    angle = 2.0 * np.pi * float ( i ) / float ( n - 1 )
    x_exact[i] = np.sin ( angle )

  b = np.zeros ( n )
  b = - 2.0 * x_exact.copy ( )
  b[0:n-1] = b[0:n-1] + x_exact[1:n]
  b[1:n] = b[1:n] + x_exact[0:n-1]
#
#  Here is the initial guess for the solution.
#
  x = np.zeros ( n )
#
#  Parameters we need for the stopping test.
#
  it = 0
  it_max = 30
  tol = 1.0E-05
  bnrm2 = np.linalg.norm ( b )
#
#  Set parameters for cg_rc.
#
  r = np.zeros ( n )
  z = np.zeros ( n )
  p = np.zeros ( n )
  q = np.zeros ( n )
  job = 1
  iterate = 0
  rho  = 0.0
  rho_old = 0.0
  rlbl = 0
#
#  Repeatedly call cg_rc, and on return, do what JOB tells you.
#
  while ( True ):

    x, r, z, p, q, job, iterate, rho, rho_old, rlbl = \
      cg_rc ( n, b, x, r, z, p, q, job, iterate, rho, rho_old, rlbl )
#
#  Compute q = A * p.
#
    if ( job == 1 ):

      q[0:n] = - 2.0 * p[0:n]
      q[0:n-1] = q[0:n-1] + p[1:n]
      q[1:n] = q[1:n] + p[0:n-1]
#
#  Solve M * z = r
#
    elif ( job == 2 ):

      z = r.copy( ) / ( -2.0 )
#
#  Compute r = r - A * x.
#
    elif ( job == 3 ):

      r[0:n] = r[0:n] + 2.0 * x[0:n]
      r[0:n-1] = r[0:n-1] - x[1:n]
      r[1:n] = r[1:n] - x[0:n-1]
#
#  Stopping test.
#
    elif ( job == 4 ):

      rnrm2 = np.linalg.norm ( r )

      if ( bnrm2 == 0.0 ):
        if ( rnrm2 <= tol ):
          break
      else:
        if ( rnrm2 <= tol * bnrm2 ):
          break

      it = it + 1

      if ( it_max <= it ):
        print ( '' )
        print ( '  Iteration limit exceeded.' )
        print ( '  Terminating early.' )
        break

    job = 2

  print ( '' )
  print ( '  Number of iterations was %d' % ( it ) )
  print ( '  Estimated error is %g' % ( rnrm2 ) )
  err = max ( abs ( x_exact[0:n] - x[0:n] ) )
  print ( '  Loo error is %g' % ( err ) )

  print ( '' )
  print ( '     I      X(I)         X_EXACT(I)        B(I)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %14f  %14f  %14f' % ( i, x[i], x_exact[i], b[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'cg_rc_test01():' )
  print ( '  Normal end of execution.' )
  return

def cg_rc_test02 ( ):

#*****************************************************************************80
#
## cg_rc_test02() tests cg_rc() with the Wathen matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 79

  print ( '' )
  print ( 'cg_rc_test02():' )
  print ( '  Use cg_rc() to solve a linear system' )
  print ( '  involving the Wathen matrix.' )

  nx = 5
  ny = 4

  print ( '' )
  print ( '  NX = %d' % ( nx ) )
  print ( '  NY = %d' % ( ny ) )
  print ( '  N  = %d' % ( n ) )

  a = wathen ( nx, ny, n )

  x_exact = np.random.rand ( n )

  b = np.dot ( a, x_exact )

  x = np.zeros ( n )
#
#  Parameters we need for the stopping test.
#
  it = 0
  it_max = 30
  tol = 1.0E-05
  bnrm2 = np.linalg.norm ( b )
#
#  Set parameters for cg_rc.
#
  r = np.zeros ( n )
  z = np.zeros ( n )
  p = np.zeros ( n )
  q = np.zeros ( n )
  job = 1
  iterate = 0
  rho  = 0.0
  rho_old = 0.0
  rlbl = 0
#
#  Repeatedly call cg_rc, and on return, do what JOB tells you.
#
  while ( True ):

    x, r, z, p, q, job, iterate, rho, rho_old, rlbl = \
      cg_rc ( n, b, x, r, z, p, q, job, iterate, rho, rho_old, rlbl )
#
#  Compute q = A * p.
#
    if ( job == 1 ):

      q = np.dot ( a, p )
#
#  Solve M * z = r
#
    elif ( job == 2 ):

      for i in range ( 0, n ):
        z[i] = r[i] / a[i,i]
#
#  Compute r = r - A * x.
#
    elif ( job == 3 ):

      r = r - np.dot ( a, x )
#
#  Stopping test.
#
    elif ( job == 4 ):

      rnrm2 = np.linalg.norm ( r )

      if ( bnrm2 == 0.0 ):
        if ( rnrm2 <= tol ):
          break
      else:
        if ( rnrm2 <= tol * bnrm2 ):
          break

      it = it + 1

      if ( it_max <= it ):
        print ( '' )
        print ( '  Iteration limit exceeded.' )
        print ( '  Terminating early.' )
        break

    job = 2

  print ( '' )
  print ( '  Number of iterations was %d' % ( it ) )
  print ( '  Estimated error is %g' % ( rnrm2 ) )
  err = max ( abs ( x_exact[0:n] - x[0:n] ) )
  print ( '  Loo error is %g' % ( err ) )

  print ( '' )
  print ( '     I      X(I)         X_EXACT(I)        B(I)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %14f  %14f  %14f' % ( i, x[i], x_exact[i], b[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'cg_rc_test02():' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## r8vec_print_test() tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_print() prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_print_test():' )
  print ( '  Normal end of execution.' )
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

def wathen ( nx, ny, n ):

#*****************************************************************************80
#
## wathen() returns the Wathen matrix, using general (GE) storage.
#
#  Discussion:
#
#    The Wathen matrix is a finite element matrix which is sparse.
#
#    The entries of the matrix depend in part on a physical quantity
#    related to density.  That density is here assigned random values between
#    0 and 100.
#
#    The matrix order N is determined by the input quantities NX and NY,
#    which would usually be the number of elements in the X and Y directions.
#    The value of N is
#
#      N = 3*NX*NY + 2*NX + 2*NY + 1,
#
#    The matrix is the consistent mass matrix for a regular NX by NY grid
#    of 8 node serendipity elements.
#
#    The local element numbering is
#
#      3--2--1
#      |     |
#      4     8
#      |     |
#      5--6--7
#
#    Here is an illustration for NX = 3, NY = 2:
#
#     23-24-25-26-27-28-29
#      |     |     |     |
#     19    20    21    22
#      |     |     |     |
#     12-13-14-15-16-17-18
#      |     |     |     |
#      8     9    10    11
#      |     |     |     |
#      1--2--3--4--5--6--7
#
#    For this example, the total number of nodes is, as expected,
#
#      N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
#
#    The matrix is symmetric positive definite for any positive values of the
#    density RHO(X,Y).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, Number 4, October 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of the matrix.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  em = np.array \
  ( \
    ( ( 6.0, -6.0,  2.0, -8.0,  3.0, -8.0,  2.0, -6.0 ), \
      (-6.0, 32.0, -6.0, 20.0, -8.0, 16.0, -8.0, 20.0 ), \
      ( 2.0, -6.0,  6.0, -6.0,  2.0, -8.0,  3.0, -8.0 ), \
      (-8.0, 20.0, -6.0, 32.0, -6.0, 20.0, -8.0, 16.0 ), \
      ( 3.0, -8.0,  2.0, -6.0,  6.0, -6.0,  2.0, -8.0 ), \
      (-8.0, 16.0, -8.0, 20.0, -6.0, 32.0, -6.0, 20.0 ), \
      ( 2.0, -8.0,  3.0, -8.0,  2.0, -6.0,  6.0, -6.0 ), \
      (-6.0, 20.0, -8.0, 16.0, -8.0, 20.0, -6.0, 32.0 ) )\
  )

  node = np.zeros ( 8, dtype = np.int32 )

  for j in range ( 0, ny ):

    for i in range ( 0, nx ):
#
#  For the element (I,J), determine the indices of the 8 nodes.
#
      node[0] = ( 3 * ( j + 1 )     ) * nx + 2 * ( j + 1 ) + 2 *  ( i + 1 ) + 1 - 1
      node[1] = node[0] - 1
      node[2] = node[0] - 2

      node[3] = ( 3 * ( j + 1 ) - 1 ) * nx + 2 *  ( j + 1 ) + ( i + 1 ) - 1 - 1
      node[7] = node[3] + 1

      node[4] = ( 3 *  ( j + 1 ) - 3 ) * nx + 2 *  ( j + 1 ) + 2 *  ( i + 1 ) - 3 - 1
      node[5] = node[4] + 1
      node[6] = node[4] + 2

      rho = 100.0 * np.random.rand ( )

      for krow in range ( 0, 8 ):
        for kcol in range ( 0, 8 ):
          a[node[krow],node[kcol]] = a[node[krow],node[kcol]] \
            + rho * em[krow,kcol]

  return a

def wathen_test ( ):

#*****************************************************************************80
#
## wathen_test() assembles, factor and solve using the Wathen matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import scipy.linalg as la
  from numpy.linalg import norm

  print ( '' )
  print ( 'wathen_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Assemble, factor and solve a Wathen system' )
  print ( '  defined by wathen().' )
  print ( '' )

  nx = 4
  ny = 4
  print ( '  Elements in X direction NX = %d' % ( nx ) )
  print ( '  Elements in Y direction NY = %d' % ( ny ) )
  print ( '  Number of elements = %d' % ( nx * ny ) )
#
#  Compute the number of unknowns.
#
  n = wathen_order ( nx, ny )
  print ( '  Number of nodes N = %d' % ( n ) )
#
#  Set up a random solution X1.
#
  x1 = np.random.rand ( n )
#
#  Compute the matrix.
#
  a = wathen ( nx, ny, n )
#
#  Compute the corresponding right hand side B.
#
  b = np.dot ( a, x1 )
#
#  Solve the linear system.
#
  x2 = la.solve ( a, b )
#
#  Compute the norm of the solution error.
#
  e = norm ( x1 - x2 )
  print ( '  Norm of solution error is %g' % ( e ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'wathen_test():' )
  print ( '  Normal end of execution.' )
  return

def wathen_order ( nx, ny ):

#*****************************************************************************80
#
## wathen_order() returns the order of the WATHEN matrix.
#
#  Discussion:
#
#    N = 3 * 3 * 2 + 2 * 2 + 2 * 3 + 1 = 29
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, 1987, pages 449-457.
#
#  Input:
#
#    integer NX, NY, values which determine the size of A.
#
#  Output:
#
#    integer N, the order of the matrix,
#    as determined by NX and NY.
#
  n = 3 * nx * ny + 2 * nx + 2 * ny + 1

  return n

def wathen_order_test ( ):

#*****************************************************************************80
#
## wathen_order_test() tests wathen_order().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    Algorithm 694: A Collection of Test Matrices in MATLAB,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 3, September 1991, pages 289-305.
#
#    Andrew Wathen,
#    Realistic eigenvalue bounds for the Galerkin mass matrix,
#    IMA Journal of Numerical Analysis,
#    Volume 7, 1987, pages 449-457.
#
  import platform

  print ( '' )
  print ( 'wathen_order_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  wathen_order() returns N, the order of a Wathen finite element' )
  print ( '  matrix given NX and NY, the number of rows and columns of' )
  print ( '  nodes in the underlying grid.' )
  print ( '' )
  print ( '       NX / NY: 1       2       3       4       5       6' )
  print ( '' )

  for ny in range ( 1, 11 ):
    print ( '       %2d' % ( ny ), end = '' )
    for nx in range ( 1, 7 ):
      n = wathen_order ( nx, ny )
      print ( '  %5d' % ( n ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'wathen_order_test():' )
  print ( '  Normal end of execution.' )
  return

def cg_rc_test ( ):

#*****************************************************************************80
#
## cg_rc_test() tests cg_rc().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2013
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'cg_rc_test():' )
  print ( '  Python version' )
  print ( '  Test cg_rc().' )

  cg_rc_test01 ( )
  cg_rc_test02 ( )
  wathen_test ( )
  wathen_order_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'cg_rc_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  cg_rc_test ( )
  timestamp ( )

