#! /usr/bin/env python3
#
def bvec_print ( n, bvec, title ) :

#*****************************************************************************80
#
## bvec_print() prints a binary integer vector, with an optional title.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#    The vector is printed "backwards", that is, the first entry
#    printed is BVEC(N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    integer BVEC(N), the vector to be printed.
#
#    string TITLE, a title to be printed first.
#    TITLE may be blank.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  for ihi in range ( n - 1, -1, -70 ):
    ilo = max ( ihi - 70, -1 )
    print ( '  ', end = '' )
    for i in range ( ihi, -1, ilo ):
      print ( '%1d' % ( bvec[i] ), end = '' )
    print ( '' )

  return

def bvec_print_test ( ):

#*****************************************************************************80
#
## bvec_print_test() tests bvec_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  bvec = np.array ( [ 1, 0, 0, 1, 0, 1, 1, 1, 0, 0 ] )

  print ( '' )
  print ( 'bvec_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bvec_print() prints a binary vector.' )

  bvec_print ( n, bvec, '  BVEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'bvec_print_test():' )
  print ( '  Normal end of execution.' )
  return

def bvec_uniform ( n, seed ):

#*****************************************************************************80
#
## bvec_uniform() returns a pseudorandom BVEC.
#
#  Discussion:
#
#    A BVEC is a vector of binary (0/1) values, representing an integer.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer N, the order of the vector.
#
#    integer SEED, the "seed" value, which should NOT be 0.
#
#  Output:
#
#    integer BVEC(N), a pseudorandom binary vector.
#
#    integer SEED, the updated seed.
#
  import numpy as np

  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'bvec_uniform(): Fatal error!' )
    print ( '  Input value of SEED = 0.' )
    raise Exception ( 'bvec_uniform(): Fatal error!' )

  bvec = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    if ( i4_huge_half < seed ):
      bvec[i] = 0
    else:
      bvec[i] = 1

  return bvec, seed

def bvec_uniform_test ( ):

#*****************************************************************************80
#
## bvec_uniform_test() tests bvec_uniform().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'bvec_uniform_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  bvec_uniform() computes a random BVEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  print ( '' )
  for i in range ( 0, 10 ):
    v, seed = bvec_uniform ( n, seed )
    bvec_print ( n, v, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'bvec_uniform_test()::' )
  print ( '  Normal end of execution.' )
  return

def c4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## c4mat_print() prints a C4MAT.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    complex A(M,N), the matrix.
#
#    string TITLE, a title.
#
  c4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def c4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## c4mat_print_some() prints out a portion of a C4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    complex A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 4

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '       %7d              ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  %12gi ' % ( a.real[i,j], a.imag[i,j] ), end = '' )

      print ( '' )

  return

def c4mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## c4mat_uniform_01() returns a unit pseudorandom C4MAT.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer M, N, the number of rows and columns in the matrix.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    complex C(M,N), the pseudorandom complex matrix.
#
#    integer SEED, a seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647;

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'c4mat_uniform_01(): Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'c4mat_uniform_01(): Fatal error!' )

  c = np.zeros ( ( m, n ), 'complex' )

  for i2 in range ( 0, n ): 
    for i1 in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836;

      if ( seed < 0 ):
        seed = seed + i4_huge

      r = np.sqrt ( seed * 4.656612875E-10 )

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      if ( seed < 0 ):
        seed = seed + i4_huge

      theta = 2.0 * np.pi * seed * 4.656612875E-10

      c[i1][i2] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c, seed

def c4mat_uniform_01_test ( ):

#*****************************************************************************80
#
## c4mat_uniform_01_test() tests c4mat_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 3
  seed = 123456789

  print ( '' )
  print ( 'c4mat_uniform_01_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c4mat_uniform_01() computes a random C4MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = c4mat_uniform_01 ( m, n, seed )

  c4mat_print ( m, n, v, '  Random C4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'c4mat_uniform_01_test():' )
  print ( '  Normal end of execution.' )
  return

def c4_uniform_01 ( seed ):

#*****************************************************************************80
#
## c4_uniform_01() returns a unit pseudorandom C4.
#
#  Discussion:
#
#    The angle should be uniformly distributed between 0 and 2 * PI,
#    the square root of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    complex C, the pseudorandom complex value.
#
#    integer SEED, a seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'c4_uniform_01(): Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'c4_uniform_01(): Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = np.sqrt ( seed * 4.656612875E-10 )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  theta = 2.0 * np.pi * seed * 4.656612875E-10

  c = r * ( complex ( np.cos ( theta ), np.sin ( theta ) ) )

  return c, seed

def c4_uniform_01_test ( ):

#*****************************************************************************80
#
## c4_uniform_01_test() tests c4_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  seed = 123456789

  print ( '' )
  print ( 'c4_uniform_01_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c4_uniform_01() computes pseudorandom complex values' )
  print ( '  in the unit circle.' )

  print ( '' )
  print ( '  The initial seed is ', seed )
  print ( '' )

  for i in range ( 1, 11 ):
    x, seed = c4_uniform_01 ( seed )
    print ( '  %6d  ( %f, %f )' % ( i, x.real, x.imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'c4_uniform_01_test():' )
  print ( '  Normal end of execution.' )
  return

def c4vec_print ( n, a, title ):

#*****************************************************************************80
#
## c4vec_print() prints a c4vec.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    complex A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %12g  %12g' % ( i, a.real[i], a.imag[i] ) )

def c4vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## c4vec_uniform_01() returns a unit pseudorandom C4VEC.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer N, the number of values to compute.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    complex C(N), the pseudorandom complex vector.
#
#    integer SEED, a seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647;

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'c4vec_uniform_01(): Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'c4vec_uniform_01(): Fatal error!' )

  c = np.zeros ( n, 'complex' )

  for j in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    r = np.sqrt ( seed * 4.656612875E-10 )

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    theta = 2.0 * np.pi * seed * 4.656612875E-10

    c[j] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c, seed

def c4vec_uniform_01_test ( ):

#*****************************************************************************80
#
## c4vec_uniform_01_test() tests C4VEC_uniform_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  seed = 123456789

  print ( '' )
  print ( 'c4vec_uniform_01_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c4vec_uniform_01() computes pseudorandom complex values' )
  print ( '  in the unit circle.' )

  print ( '' )
  print ( '  The initial seed is ', seed )
  print ( '' )

  n = 10

  x, seed = c4vec_uniform_01 ( n, seed )

  for i in range ( 0, n ):
    print ( '  %6d  ( %f, %f )' % ( i, x[i].real, x[i].imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'c4vec_uniform_01_test():' )
  print ( '  Normal end of execution.' )
  return

def c8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## c8mat_print() prints a C8MAT.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    complex A(M,N), the matrix.
#
#    string TITLE, a title.
#
  c8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def c8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## c8mat_print_some() prints out a portion of a C8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    complex A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 4

  print ( '' )
  print  ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '       %7d              ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  %12gi ' % ( a.real[i,j], a.imag[i,j] ), end = '' )

      print ( '' )

  return

def c8mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## c8mat_uniform_01() returns a unit pseudorandom C8MAT.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer M, N, the number of rows and columns in the matrix.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    complex C(M,N), the pseudorandom complex matrix.
#
#    integer SEED, a seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647;

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'c8mat_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'c8mat_uniform_01 - Fatal error!' )

  c = np.zeros ( ( m, n ), 'complex' )

  for i2 in range ( 0, n ): 
    for i1 in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836;

      if ( seed < 0 ):
        seed = seed + i4_huge

      r = np.sqrt ( seed * 4.656612875E-10 )

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      if ( seed < 0 ):
        seed = seed + i4_huge

      theta = 2.0 * np.pi * seed * 4.656612875E-10

      c[i1][i2] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c, seed

def c8mat_uniform_01_test ( ):

#*****************************************************************************80
#
## c8mat_uniform_01_test() tests c8mat_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 3
  seed = 123456789

  print ( '' )
  print ( 'C8MAT_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  c8mat_uniform_01() computes a random C8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = c8mat_uniform_01 ( m, n, seed )

  c8mat_print ( m, n, v, '  Random C8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8MAT_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def c8_uniform_01 ( seed ):

#*****************************************************************************80
#
## c8_uniform_01() returns a unit pseudorandom C8.
#
#  Discussion:
#
#    The angle should be uniformly distributed between 0 and 2 * PI,
#    the square root of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    complex C, the pseudorandom complex value.
#
#    integer SEED, a seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647

  seed = np.floor ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'C8_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'C8_uniform_01 - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = np.sqrt ( seed * 4.656612875E-10 )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  theta = 2.0 * np.pi * seed * 4.656612875E-10

  c = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c, seed

def c8_uniform_01_test ( ):

#*****************************************************************************80
#
## c8_uniform_01_test() tests c8_uniform_01().
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
  import platform

  seed = 123456789

  print ( '' )
  print ( 'C8_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8_uniform_01 computes pseudorandom complex values' )
  print ( '  in the unit circle.' )

  print ( '' )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 0, 10 ):
    x, seed = c8_uniform_01 ( seed )
    print ( '  %6d  ( %g, %g )' % ( i, x.real, x.imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def c8vec_print ( n, a, title ):

#*****************************************************************************80
#
## c8vec_print() prints a c8vec().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    complex A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %12g  %12g' % ( i, a.real[i], a.imag[i] ) )

  return

def c8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## c8vec_uniform_01() returns a unit pseudorandom c8vec.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer N, the number of values to compute.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    complex C(N), the pseudorandom complex vector.
#
#    integer SEED, a seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'C8VEC_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'C8VEC_uniform_01 - Fatal error!' )

  c = np.zeros ( n, 'complex' )

  for j in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    r = np.sqrt ( seed * 4.656612875E-10 )

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    theta = 2.0 * np.pi * seed * 4.656612875E-10

    c[j] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c, seed

def c8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## c8vec_uniform_01_test() tests c8vec_uniform_01().
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
  import platform

  seed = 123456789

  print ( '' )
  print ( 'C8VEC_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8VEC_uniform_01 computes pseudorandom complex values' )
  print ( '  in the unit circle.' )

  print ( '' )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  n = 10

  x, seed = c8vec_uniform_01 ( n, seed )

  for i in range ( 0, n ):
    print ( '  %6d  ( %f, %f )' % ( i, x[i].real, x[i].imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8VEC_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def ch_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## ch_uniform_ab() returns a scaled pseudorandom CH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character A, B, the minimum and maximum acceptable characters.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    character CH, the randomly chosen character.
#
#    integer SEED, a seed for the random number generator.
#
  i1 = ord ( a )
  i2 = ord ( b )
  i3, seed = i4_uniform_ab ( i1, i2, seed )
  ch = chr ( i3 )

  return ch, seed

def ch_uniform_ab_test ( ):

#*****************************************************************************80
#
## ch_uniform_ab_test() tests ch_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  seed = 123456789

  print ( '' )
  print ( 'ch_uniform_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ch_uniform_ab computes pseudorandom character values' )
  print ( '  in the interval [CLO,CHI].' )

  clo = 'A'
  chi = 'J'

  print ( '' )
  print ( '  The lower endpoint CLO = %c' % ( clo ) )
  print ( '  The upper endpoint CHI = %c' % ( chi ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 11 ):
    ch, seed = ch_uniform_ab ( clo, chi, seed )
    print ( '  %6d  %c' % ( i, ch ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ch_uniform_ab_test:' )
  print ( '  Normal end of execution.' )
  return

def congruence ( a, b, c ):

#*****************************************************************************80
#
## congruence() solves a congruence of the form A * X = C ( mod B ).
#
#  Discussion:
#
#    A, B and C are given integers.  The equation is solvable if and only
#    if the greatest common divisor of A and B also divides C.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein, editor,
#    CRC Concise Encylopedia of Mathematics,
#    CRC Press, 1998, page 446.
#
#  Input:
#
#    integer A, B, C, the coefficients of the Diophantine equation.
#
#  Output:
#
#    integer X, the solution of the Diophantine equation.
#    X will be between 0 and B-1.
#
#    integer IERROR, error flag.
#    0, no error, X was computed.
#    1, A = B = 0, C is nonzero.
#    2, A = 0, B and C nonzero, but C is not a multiple of B.
#    3, A nonzero, B zero, C nonzero, but C is not a multiple of A.
#    4, A, B, C nonzero, but GCD of A and B does not divide C.
#    5, algorithm ran out of internal space.
#
  import numpy as np

  a = int ( a )
  b = int ( b )
  c = int ( c )

  nmax = 100
#
#  Defaults for output parameters.
#
  ierror = 0
  x = 0
  y = 0
#
#  Special cases.
#
  if ( a == 0 and b == 0 and c == 0 ):
    x = 0
    return x, ierror
  elif ( a == 0 and b == 0 and c != 0 ):
    ierror = 1
    x = 0
    return x, ierror
  elif ( a == 0 and b != 0 and c == 0 ):
    x = 0
    return x, ierror
  elif ( a == 0 and b != 0 and c != 0 ):
    x = 0
    if ( ( c % b ) != 0 ):
      ierror = 2
    return x, ierror
  elif ( a != 0 and b == 0 and c == 0 ):
    x = 0
    return x, ierror
  elif ( a != 0 and b == 0 and c != 0 ):
    x = ( c // a )
    if ( ( c % a ) != 0 ):
      ierror = 3
    return x, ierror
  elif ( a != 0 and b != 0 and c == 0 ):
#   g = i4_gcd ( a, b )
#   x = ( b // g )
    x = 0
    return x, ierror
#
#  Now handle the "general" case: A, B and C are nonzero.
#
#  Step 1: Compute the GCD of A and B, which must also divide C.
#
  g = i4_gcd ( a, b )

  if ( ( c % g ) != 0 ):
    ierror = 4
    return x, ierror

  a_copy = ( a // g )
  b_copy = ( b // g )
  c_copy = ( c // g )
#
#  Step 2: Split A and B into sign and magnitude.
#
  a_mag = abs ( a_copy )
  a_sign = i4_sign ( a_copy )
  b_mag = abs ( b_copy )
  b_sign = i4_sign ( b_copy )
#
#  Another special case, A_MAG = 1 or B_MAG = 1.
#
  if ( a_mag == 1 ):
    x = a_sign * c_copy
    return x, ierror
  elif ( b_mag == 1 ):
    x = 0
    return x, ierror
#
#  Step 3: Produce the Euclidean remainder sequence.
#
  q = np.zeros ( nmax )

  if ( b_mag <= a_mag ):
    swap = 0;
    q[0] = a_mag;
    q[1] = b_mag;
  else:
    swap = 1;
    q[0] = b_mag;
    q[1] = a_mag;

  n = 2

  while ( True ):

    q[n] = ( q[n-2] % q[n-1] )

    if ( q[n] == 1 ):
      break

    n = n + 1

    if ( nmax <= n ):
      ierror = 5
      print ( '' )
      print ( 'congruence - Fatal error!' )
      print ( '  Exceeded number of iterations.' )
      raise Exception ( 'congruence - Fatal error!' )
#
#  Step 4: Now go backwards to solve X * A_MAG + Y * B_MAG = 1.
#
  y = 0
  for k in range ( n, 0, -1 ):
    x = y
    y = ( 1 - x * q[k-1] ) // q[k]
#
#  Step 5: Undo the swapping.
#
  if ( swap ):
    z = x
    x = y
    y = z
#
#  Step 6: Now apply signs to X and Y so that X * A + Y * B = 1.
#
  x = x * a_sign
#
#  Step 7: Multiply by C, so that X * A + Y * B = C.
#
  x = x * c_copy
#
#  Step 8: Now force 0 <= X < B.
#
  x = ( x % b )
#
#  Step 9: Force positivity.
#
  if ( x < 0 ):
    x = x + b

  return x, ierror

def congruence_test ( ):

#*****************************************************************************80
#
## congruence_test() tests congruence().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 20

  a_test = np.array ( ( \
     1027,  1027,  1027,  1027, -1027, \
    -1027, -1027, -1027,     6,     0, \
        0,     0,     1,     1,     1, \
     1024,     0,     0,     5,     2 ) )
  b_test = np.array ( ( \
      712,   712,  -712,  -712,   712, \
      712,  -712,  -712,     8,     0, \
        1,     1,     0,     0,     1, \
   -15625,     0,     3,     0,     4 ) )
  c_test = np.array ( ( \
        7,    -7,     7,    -7,     7, \
       -7,     7,    -7,    50,     0, \
        0,     1,     0,     1,     0, \
    11529,     1,    11,    19,     7 ) )

  print ( '' )
  print ( 'congruence_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  congruence solves a congruence equation:' )
  print ( '    A * X = C mod ( B )' )
  print ( '' )
  print ( '   I        A         B         C         X     Mod ( A*X-C,B)' )
  print ( '' )

  for test_i in range ( 0, test_num ):

    a = a_test[test_i]
    b = b_test[test_i]
    c = c_test[test_i]

    x, ierror = congruence ( a, b, c )

    if ( b != 0 ):
      result = i4_modp ( a * x - c, b )
    else:
      result = 0

    print ( '  %2d  %8d  %8d  %8d  %8d  %8d' % ( test_i, a, b, c, x, result ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'congruence_test' )
  print ( '  Normal end of execution.' )
  return

def get_seed ( ):

#*****************************************************************************80
#
## get_seed() returns a random seed for the random number generator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer SEED, a random seed value.
#
  import time
#
#  Get a floating point number, measured in seconds,
#  that represents the elapsed time since the epoch.
#
  seed = time.time ( )
#
#  Reduce the number to an integer.
#
  seed = int ( seed )
#
#  Use modulo arithmetic to get an integer between 1 and i4_HUGE.
#
  i4_huge = 2147483647
  seed = ( seed % i4_huge ) + 1

  return seed

def get_seed_test ( ):

#*****************************************************************************80
#
## get_seed_test() tests get_seed().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 April 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'get_seed_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  get_seed picks an initial seed value for r8_uniform_01.' )
  print ( '  The value chosen should vary over time, because' )
  print ( '  the seed is based on reading the clock.' )
  print ( '' )
  print ( '  This is just the "calendar" clock, which does' )
  print ( '  not change very fast, so calling get_seed several' )
  print ( '  times in a row may result in the same value.' )

  seed = 12345678
  seed_old = seed

  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )
  print ( '' )
  print ( '  Next 3 values of r8_uniform_01:' )
  print ( '' )

  for j in range ( 0, 3 ):
    r, seed = r8_uniform_01 ( seed )
    print ( '  %f' % ( r ) )

  for i in range ( 0, 4 ):

    while ( True ):

      seed = get_seed ( )

      if ( seed != seed_old ):
        seed_old = seed
        break

    print ( '' )
    print ( '  New seed from get_seed is = %d' % ( seed ) )
    print ( '' )
    print ( '  Next 3 values of r8_uniform_01:' )
    print ( '' )

    for j in range ( 0, 3 ):
      r, seed = r8_uniform_01 ( seed )
      print ( '  %f' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'get_seed_test:' )
  print ( '  Normal end of execution.' )
  return

def i4_gcd ( i, j ):

#*****************************************************************************80
#
## i4_gcd() finds the greatest common divisor of I and J.
#
#  Discussion:
#
#    Only the absolute values of I and J are
#    considered, so that the result is always nonnegative.
#
#    If I or J is 0, i4_gcd is returned as max ( 1, abs ( I ), abs ( J ) ).
#
#    If I and J have no common factor, i4_gcd is returned as 1.
#
#    Otherwise, using the Euclidean algorithm, i4_gcd is the
#    largest common factor of I and J.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, two numbers whose greatest common divisor
#    is desired.
#
#    integer VALUE, the greatest common divisor of I and J.
#
  value = 1
#
#  Return immediately if either I or J is zero.
#
  if ( i == 0 ):
    value = max ( 1, abs ( j ) )
    return value
  elif ( j == 0 ):
    value = max ( 1, abs ( i ) )
    return value
#
#  Set IP to the larger of I and J, IQ to the smaller.
#  This way, we can alter IP and IQ as we go.
#
  ip = max ( abs ( i ), abs ( j ) )
  iq = min ( abs ( i ), abs ( j ) )
#
#  Carry out the Euclidean algorithm.
#
  while ( True ):

    ir = ( ip % iq )

    if ( ir == 0 ):
      break

    ip = iq
    iq = ir

  value = iq

  return value

def i4_gcd_test ( ):

#*****************************************************************************80
#
## i4_gcd_test() tests i4_gcd().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  test_num = 7

  i_test = [ 36, 49, 0, 12, 36, 1, 91 ]
  j_test = [ 30, -7, 71, 12, 49, 42, 28 ]

  print ( '' )
  print ( 'i4_gcd_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_gcd computes the greatest common factor' )
  print ( '' )
  print ( '     I     J   i4_gcd' )
  print ( '' )
 
  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    k = i4_gcd ( i, j )
    print ( '  %6d  %6d  %6d' % ( i, j, k ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_gcd_test' )
  print ( '  Normal end of execution' )
  return

def i4_huge ( ):

#*****************************************************************************80
#
## i4_huge() returns a "huge" I4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer VALUE, a huge integer.
#
  value = 2147483647

  return value;

def i4_huge_test ( ) :

#*****************************************************************************80
#
## i4_huge_test() tests i4_huge().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_HUGE_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_HUGE returns a huge integer.' )
  print ( '' )
  i = i4_huge ( )
  print ( '  i4_HUGE() = %d' % ( i ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_HUGE_test' )
  print ( '  Normal end of execution.' )
  return

def i4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## i4mat_print() prints an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    integer A(M,N), the matrix.
#
#    string TITLE, a title.
#
  i4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## i4mat_print_some() prints out a portion of an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d  ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%7d  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def i4mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## i4mat_uniform_ab() returns a scaled pseudorandom I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer M, N, the row and column dimensions of the matrix.
#
#    integer A, B, the minimum and maximum acceptable values.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    integer C(M,N), the randomly chosen integer vector.
#
#    integer SEED, the updated seed.
#
  import numpy as np

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'i4mat_uniform_ab - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'i4mat_uniform_ab - Fatal error!' )

  a = round ( a )
  b = round ( b )

  c = np.zeros ( [ m, n ], dtype = np.int32 )

  for j in range ( 0, n ):

    for i in range ( 0, m ): 

      k =  ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
      r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
        +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
      value = round ( r )

      value = max ( value, min ( a, b ) )
      value = min ( value, max ( a, b ) )

      c[i,j] = value

  return c, seed

def i4mat_uniform_ab_test ( ):

#*****************************************************************************80
#
## i4mat_uniform_ab_test() tests i4mat_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  a = -1
  b = +5
  seed = 123456789

  print ( '' )
  print ( 'i4mat_uniform_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4mat_uniform_ab computes a random R8MAT.' )
  print ( '' )
  print ( '  %d <= X <= %d' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = i4mat_uniform_ab ( m, n, a, b, seed )

  i4mat_print ( m, n, v, '  Random I4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4mat_uniform_ab_test:' )
  print ( '  Normal end of execution.' )
  return

def i4_modp ( i, j ):

#*****************************************************************************80
#
## i4_modp() returns the nonnegative remainder of I4 division.
#
#  Discussion:
#
#    If
#      NREM = i4_modp ( I, J )
#      NMULT = ( I - NREM ) / J
#    then
#      I = J * NMULT + NREM
#    where NREM is always nonnegative.
#
#    The MOD function computes a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, i4_modp(A,360) is between 0 and 360, always.
#
#  Example:
#
#        I     J     MOD  i4_modp    Factorization
#
#      107    50       7       7    107 =  2 *  50 + 7
#      107   -50       7       7    107 = -2 * -50 + 7
#     -107    50      -7      43   -107 = -3 *  50 + 43
#     -107   -50      -7      43   -107 =  3 * -50 + 43
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number to be divided.
#
#    integer J, the number that divides I.
#
#  Output:
#
#    integer VALUE, the nonnegative remainder when I is
#    divided by J.
#
  if ( j == 0 ):
    print ( '' )
    print ( 'i4_modp - Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    raise Exception ( 'i4_modp - Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + abs ( j )

  return value

def i4_modp_test ( ):

#*****************************************************************************80
#
## i4_modp_test() tests i4_modp().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 4

  n_vec = np.array ( ( 107, 107, -107, -107 ) )
  d_vec = np.array ( ( 50, -50, 50, -50 ) )

  print ( '' )
  print ( 'i4_modp_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_modp factors a number' )
  print ( '  into a multiple M and a positive remainder R.' )
  print ( '' )
  print ( '    Number   Divisor  Multiple Remainder' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    r = i4_modp ( n, d )
    m = ( n - r ) // d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  print ( '' )
  print ( '  Repeat using Python % Operator:' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_modp_test' )
  print ( '  Normal end of execution.' )
  return

def i4_seed_advance ( seed ) :

#*****************************************************************************80
#
## i4_seed_advance() "advances" the seed.
#
#  Discussion:
#
#    This routine implements one step of the recursion
#
#      SEED = ( 16807 * SEED ) mod ( 2^31 - 1 )
#
#    This version of the routine does not check whether the input value of
#    SEED is zero.  If the input value is zero, the output value will be zero.
#
#    If we repeatedly use the output of SEED_advance as the next input,
#    and we start with SEED = 12345, then the first few iterates are:
#
#         Input      Output
#          SEED        SEED
#
#         12345   207482415
#     207482415  1790989824
#    1790989824  2035175616
#    2035175616    77048696
#      77048696    24794531
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer SEED, the seed value.
#
#  Output:
#
#    integer SEED, the "next" seed.
#
  i4_huge = 2147483647

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'i4_advance_seed - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'i4_advance_seed - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  return seed

def i4_seed_advance_test ( ):

#*****************************************************************************80
#
## i4_seed_advance_test() tests i4_seed_advance().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_seed_advance_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_seed_advance advances the seed.' )
  print ( '' )
  print ( '  Step        SEED input       SEED output' )
  print ( '' )

  seed_new = 12345

  for step in range ( 1, 11 ):

    seed = seed_new
    seed_new = i4_seed_advance ( seed )

    print ( '  %4d  %16d  %16d' % ( step, seed, seed_new ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_seed_advance_test:' )
  print ( '  Normal end of execution.' )
  return

def i4_sign ( i ):

#*****************************************************************************80
#
## i4_sign() returns the sign of an integer.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose sign is desired.
#
#    integer VALUE, the sign of I.
#
  if ( i < 0 ):
    value = -1
  else:
    value = +1

  return value

def i4_sign_test ( ):

#*****************************************************************************80
#
## i4_sign_test() tests i4_sign().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 5

  i4_vec = np.array ( ( -10, -7, 0, 5, 9 ) )

  print ( '' )
  print ( 'i4_sign_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_sign returns the sign of an I4.' )
  print ( '' )
  print ( '    I4  i4_sign(I4)' )
  print ( '' )

  for test in range ( 0, test_num ):
    i4 = i4_vec[test]
    s = i4_sign ( i4 )
    print ( '  %4d  %11d' % ( i4, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_sign_test' )
  print ( '  Normal end of execution.' )
  return

def i4_uniform_0i ( seed ):

#*****************************************************************************80
#
## i4_uniform_0i() returns a pseudorandom I4.
#
#  Discussion:
#
#    SEED = SEED * (7^5) mod (2^31 - 1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer SEED, the integer "seed" used to generate
#    the output value.  SEED should not be 0.
#
#  Output:
#
#    integer SEED, a uniform random value between
#    1 and 2^31-1.
#
#  Local Input:
#
#    IA = 7^5
#    IB = 2^15
#    IB16 = 2^16
#    IP = 2^31-1
#
  ia = 16807
  ib15 = 32768
  ib16 = 65536
  ip = 2147483647
#
#  Don't let SEED be 0.
#
  if ( seed == 0 ):
    seed = ip
#
#  Get the 15 high order bits of SEED.
#
  ixhi = ( seed // ib16 )
#
#  Get the 16 low bits of SEED and form the low product.
#
  loxa = ( seed - ixhi * ib16 ) * ia
#
#  Get the 15 high order bits of the low product.
#
  leftlo = ( loxa // ib16 )
#
#  Form the 31 highest bits of the full product.
#
  iprhi = ixhi * ia + leftlo
#
#  Get overflow past the 31st bit of full product.
#
  k = ( iprhi // ib15 )
#
#  Assemble all the parts and presubtract IP.  The parentheses are
#  essential.
#
  seed = ( ( ( loxa - leftlo * ib16 ) - ip ) \
          + ( iprhi - k * ib15 ) * ib16 ) + k
#
#  Add IP back in if necessary.
#
  if ( seed < 0 ):
    seed = seed + ip

  return seed

def i4_uniform_0i_test ( ):

#*****************************************************************************80
#
## i4_uniform_0i_test() tests i4_uniform_0i().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  seed = 123456789

  print ( '' )
  print ( 'i4_uniform_Oi_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_uniform_0i computes pseudorandom integers' )
  print ( '  in the interval [1,(2^31)-1].' )

  print ( '' )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 11 ):
    seed = i4_uniform_0i ( seed )
    print ( '  %6d  %d' % ( i, seed ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_uniform_0i_test' )
  print ( '  Normal end of execution.' )
  return

def i4_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## i4_uniform_ab() returns a scaled pseudorandom I4.
#
#  Discussion:
#
#    The pseudorandom number will be scaled to be uniformly distributed
#    between A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer A, B, the minimum and maximum acceptable values.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    integer C, the randomly chosen integer.
#
#    integer SEED, the updated seed.
#
  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge; 

  if ( seed == 0 ):
    print ( '' )
    print ( 'i4_uniform_ab - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'i4_uniform_ab - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
  a = round ( a )
  b = round ( b )

  r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
    +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
  value = round ( r )

  value = max ( value, min ( a, b ) )
  value = min ( value, max ( a, b ) )
  value = int ( value )

  return value, seed

def i4_uniform_ab_test ( ):

#*****************************************************************************80
#
## i4_uniform_ab_test() tests i4_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'i4_uniform_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_uniform_ab computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 21 ):
    j, seed = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_uniform_ab_test:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print() prints an I4VEC.
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
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## i4vec_uniform_ab() returns a scaled pseudorandom I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer A, B, the minimum and maximum acceptable values.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    integer C(N), the randomly chosen integer vector.
#
#    integer SEED, the updated seed.
#
  import numpy as np

  i4_huge = 2147483647

  seed = int ( seed  )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'i4vec_uniform_ab - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'i4vec_uniform_ab - Fatal error!' )

  a = round ( a )
  b = round ( b )

  c = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    seed = ( seed % i4_huge )

    if ( seed < 0 ):
      seed = seed + i4_huge

    r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
    r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
      +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
    value = round ( r )

    value = max ( value, min ( a, b ) )
    value = min ( value, max ( a, b ) )

    c[i] = value

  return c, seed

def i4vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## i4vec_uniform_ab_test() tests i4vec_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 20
  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'i4vec_uniform_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_uniform_ab computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  v, seed = i4vec_uniform_ab ( n, a, b, seed )

  i4vec_print ( n, v, '  The random vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_uniform_ab_test:' )
  print ( '  Normal end of execution.' )
  return

def l4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## l4mat_print() prints an L4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    integer A(M,N), the matrix.
#
#    string TITLE, a title.
#
  l4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def l4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## l4mat_print_some() prints out a portion of an L4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 35

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%2d' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( a[i,j] == 0 ):
          print ( ' F', end = '' )
        else:
          print ( ' T', end = '' )
      print ( '' )

  return

def l4mat_uniform ( m, n, seed ):

#*****************************************************************************80
#
## l4mat_uniform() returns a pseudorandom L4MAT.
#
#  Discussion:
#
#    An L4MAT is a two dimensional array of LOGICAL values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer SEED, the "seed" value.
#
#  Output:
#
#    logical L4MAT(M,N), a pseudorandom logical matrix.
#
#    integer SEED, an updated seed.
#
  import numpy as np

  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'l4mat_uniform - Fatal error!' )
    print ( '  Input value of SEED = 0.' )
    raise Exception ( 'l4mat_uniform - Fatal error!' )

  l4mat = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):

    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      if ( seed < 0 ):
        seed = seed + i4_huge

      l4mat[i,j] = ( i4_huge_half < seed )

  return l4mat, seed

def l4mat_uniform_test ( ):

#*****************************************************************************80
#
## l4mat_uniform_test() tests l4mat_uniform().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'l4mat_uniform_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  l4mat_uniform computes a random L4MAT.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = l4mat_uniform ( m, n, seed )

  l4mat_print ( m, n, v, '  Random L4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4mat_uniform_test:' )
  print ( '  Normal end of execution.' )
  return

def l4_uniform ( seed ):

#*****************************************************************************80
#
## l4_uniform() returns a pseudorandom L4.
#
#  Discussion:
#
#    An L4 is a LOGICAL value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer SEED, the "seed" value, which should NOT be 0. 
#
#  Output:
#
#    bool VALUE, a pseudorandom logical value.
#
#    integer SEED, the updated seed value.
#
  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  seed = ( seed % i4_huge )

  if ( seed == 0 ):
    print ( '' )
    print ( 'l4_uniform - Fatal error!' )
    print ( '  Input value of SEED = 0.' )
    raise Exception ( 'l4_uniform - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  value = ( i4_huge_half < seed )

  return value, seed

def l4_uniform_test ( ):

#*****************************************************************************80
#
## l4_uniform_test() tests l4_uniform().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'l4_uniform_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  l4_uniform returns random logical values' )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):
    l4, seed = l4_uniform ( seed )
    print ( '  %d' % ( l4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4_uniform_test' )
  print ( '  Normal end of execution' )
  return

def l4vec_print ( n, a, title ):

#*****************************************************************************80
#
## l4vec_print() prints an L4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    bool A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    if ( a[i] == 0 ):
      print ( '%6d  F' % ( i ) )
    else:
      print ( '%6d  T' % ( i ) )

  return

def l4vec_uniform ( n, seed ):

#*****************************************************************************80
#
## l4vec_uniform() returns a pseudorandom L4VEC.
#
#  Discussion:
#
#    An L4VEC is a vector of LOGICAL values.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer N, the order of the vector.
#
#    integer SEED, the "seed" value, which should NOT be 0.
#
#  Output:
#
#    bool L4VEC(N), a pseudorandom logical vector.
#
#    integer SEED, the updated seed.
#
  import numpy as np

  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'l4vec_uniform - Fatal error!' )
    print ( '  Input value of SEED = 0.' )
    raise Exception ( 'l4vec_uniform - Fatal error!' )

  l4vec = np.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    l4vec[i] = ( i4_huge_half < seed )

  return l4vec, seed

def l4vec_uniform_test ( ):

#*****************************************************************************80
#
## l4vec_uniform_test() tests l4vec_uniform().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'l4vec_uniform_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  l4vec_uniform computes a random L4VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = l4vec_uniform ( n, seed )

  l4vec_print ( n, v, '  Random L4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'l4vec_uniform_test:' )
  print ( '  Normal end of execution.' )
  return

def lcrg_anbn ( a, b, c, n ):

#*****************************************************************************80
#
## lcrg_anbn() computes the "N-th power" of a linear congruential generator.
#
#  Discussion:
#
#    We are considering a linear congruential random number generator.
#    The LCRG takes as input an integer value called SEED, and returns
#    an updated value of SEED,
#
#      SEED(out) = ( a * SEED(in) + b ) mod c.
#
#    and an associated pseudorandom real value
#
#      U = SEED(out) / c.
#
#    In most cases, a user is content to call the LCRG repeatedly, with
#    the updating of SEED being taken care of automatically.
#
#    The purpose of this routine is to determine the values of AN and BN
#    that describe the LCRG that is equivalent to N applications of the
#    original LCRG.
#
#    One use for such a facility would be to do random number computations
#    in parallel.  If each of N processors is to compute many random values,
#    you can guarantee that they work with distinct random values
#    by starting with a single value of SEED, using the original LCRG to generate
#    the first N-1 "iterates" of SEED, so that you now have N "seed" values,
#    and from now on, applying the N-th power of the LCRG to the seeds.
#
#    If the K-th processor starts from the K-th seed, it will essentially
#    be computing every N-th entry of the original random number sequence,
#    offset by K.  Thus the individual processors will be using a random
#    number stream as good as the original one, and without repeating, and
#    without having to communicate.
#
#    To evaluate the N-th value of SEED directly, we start by ignoring
#    the modular arithmetic, and working out the sequence of calculations
#    as follows:
#
#      SEED(0)   =     SEED.
#      SEED(1)   = a * SEED      + b
#      SEED(2)   = a * SEED(1)   + b = a^2 * SEED           + a * b + b
#      SEED(3)   = a * SEED(2)   + b = a^3 * SEED + a^2 * b + a * b + b
#      ...
#      SEED(N-1) = a * SEED(N-2) + b
#
#      SEED(N) = a * SEED(N-1) + b = a^N * SEED
#                                    + ( a^(n-1) + a^(n-2) + ... + a + 1 ) * b
#
#    or, using the geometric series,
#
#      SEED(N) = a^N * SEED + ( a^N - 1) / ( a - 1 ) * b
#              = AN * SEED + BN
#
#    Thus, from any SEED, we can determine the result of N applications of the
#    original LCRG directly if we can solve
#
#      ( a - 1 ) * BN = ( a^N - 1 ) * b in modular arithmetic,
#
#    and evaluate:
#
#      AN = a^N
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Barry Wilkinson, Michael Allen,
#    Parallel Programming:
#    Techniques and Applications Using Networked Workstations and Parallel
#    Computers,
#    Prentice Hall,
#    ISBN: 0-13-140563-2,
#    LC: QA76.642.W54.
#
#  Input:
#
#    integer A, the multiplier for the LCRG.
#
#    integer B, the added value for the LCRG.
#
#    integer C, the base for the modular arithmetic.
#    For 32 bit arithmetic, this is often 2^31 - 1, or 2147483647.  It is
#    required that 0 < C.
#
#    integer N, the "index", or number of times that the
#    LCRG is to be applied.  It is required that 0 <= N.
#
#  Output:
#
#    integer AN, BN, the multiplier and added value for
#    the LCRG that represent N applications of the original LCRG.
#
  if ( n < 0 ):
    print ( '' )
    print ( 'lcrg_anbn - Fatal error!' )
    print ( '  Illegal input value of N = %d' % ( n ) )
    raise Exception ( 'lcrg_ANGN - Fatal error!' )

  if ( c <= 0 ):
    print ( '' )
    print ( 'lcrg_anbn - Fatal error!' )
    print ( '  Illegal input value of C = %d' % ( c ) )
    raise Exception ( 'lcrg_ANGN - Fatal error!' )

  if ( n == 0 ):
    an = 1
    bn = 0
  elif ( n == 1 ):
    an = a
    bn = b
  else:
#
#  Compute A^N.
#
    an = power_mod ( a, n, c );
#
#  Solve
#    ( a - 1 ) * BN = ( a^N - 1 ) mod B
#  for BN.
#
    am1 = a - 1
    anm1tb = ( an - 1 ) * b

    bn, ierror = congruence ( am1, c, anm1tb )

    if ( ierror != 0 ):
      print ( '' )
      print ( 'lcrg_anbn - Fatal error!' )
      print ( '  An error occurred in the congruence routine.' )
      print ( '  The error code was IERROR = %d' % ( ierror ) )
      raise Exception ( 'lcrg_ANGN - Fatal error!' )

  return an, bn

def lcrg_anbn_test ( ):

#*****************************************************************************80
#
## lcrg_anbn_test() tests lcrg_anbn().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lcrg_anbn_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  lcrg_anbn determines a linear congruential random' )
  print ( '  number generator equivalent to N steps of a given one.' )
#
#  These parameters define the old (1969) IBM 360 random number generator:
#
  a = 16807
  b = 0
  c = 2147483647

  print ( '' )
  print ( '  LCRG Input:' )
  print ( '' )
  print ( '  A  = %d' % ( a ) )
  print ( '  B  = %d' % ( b ) )
  print ( '  C  = %d' % ( c ) )

  print ( '' )
  print ( '             N             A             B' )
  print ( '' )

  for n in range ( 0, 11 ):
    an, bn = lcrg_anbn ( a, b, c, n )
    print ( '  %12d  %12d  %12d' % ( n, an, bn ) )


  print ( '' )
  print ( '                           N            In           Out' )
  print ( '' )

  k = 0
  u = 12345
  print ( '                %12d                %12d' % ( k, u ) )
  for k in range ( 1, 12 ):
    v = lcrg_evaluate ( a, b, c, u )
    print ( '                %12d  %12d  %12d' % ( k, u, v ) )
    u = v
#
#  Now try to replicate these results using N procesors.
#
  n = 4

  an, bn = lcrg_anbn ( a, b, c, n )

  print ( '' )
  print ( '  LCRG Input:' )
  print ( '' )
  print ( '  AN = %d' % ( an ) )
  print ( '  BN = %d' % ( bn ) )
  print ( '  C  = %d' % ( c ) )
  print ( '' )
  print ( '             J             N            In           Out' )
  print ( '' )

  x = np.zeros ( n )

  x[0] = 12345;
  for j in range ( 1, n ):
    x[j] = lcrg_evaluate ( a, b, c, x[j-1] )

  for j in range ( 0, n ):
    print ( '  %12d  %12d                %12d' % ( j, j, x[j] ) )

  y = np.zeros ( n )

  for k in range ( n, 12, n ):
    for j in range ( 0, n ):
      y[j] = lcrg_evaluate ( an, bn, c, x[j] )
      print ( '  %12d  %12d  %12d  %12d' % ( j, k+j, x[j], y[j] ) )
      x[j] = y[j];
#
#  Terminate.
#
  print ( '' )
  print ( 'lcrg_anbn_test' )
  print ( '  Normal end of execution.' )
  return

def lcrg_evaluate ( a, b, c, x ):

#*****************************************************************************80
#
## lcrg_evaluate() evaluates an LCRG, y = ( A * x + B ) mod C.
#
#  Discussion:
#
#    This routine cannot be recommended for production use.  Because we want
#    to do modular arithmetic, but the base is not a power of 2, we need to
#    use "double precision" integers to keep accuracy.
#
#    If we knew the base C, we could try to avoid overflow while not changing
#    precision.
#
#    If the base C was a power of 2, we could rely on the usual properties of
#    integer arithmetic on computers, in which overflow bits, which are always
#    ignored, don't actually matter.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the multiplier for the LCRG.
#
#    integer B, the added value for the LCRG.
#
#    integer C, the base for the modular arithmetic.
#    For 32 bit arithmetic, this is often 2^31 - 1, or 2147483647.  It is
#    required that 0 < C.
#
#    integer X, the value to be processed.
#
#  Output:
#
#    integer Y, the processed value.
#
  y = ( ( a * x + b ) % c )

  if ( y < 0 ):
    y = y + c

  return y

def lcrg_seed ( a, b, c, n, seed ):

#*****************************************************************************80
#
## lcrg_seed() computes the N-th seed of a linear congruential generator.
#
#  Discussion:
#
#    We are considering a linear congruential random number generator.
#    The LCRG takes as input an integer value called SEED, and returns
#    an updated value of SEED, 
#
#      SEED(out) = a * SEED(in) + b, mod c.
#
#    and an associated pseudorandom real value
#
#      U = SEED(out) / c.
#
#    In most cases, a user is content to call the LCRG repeatedly, with
#    the updating of SEED being taken care of automatically.
#
#    The purpose of this routine is to determine the value of SEED that
#    would be output after N successive applications of the LCRG.  This
#    allows the user to know, in advance, what the 1000-th value of
#    SEED would be, for instance.  Obviously, one way to do this is to
#    apply the LCRG formula 1,000 times.  However, it is possible to
#    do this in a more direct and efficient way.
#
#    One use for such a facility would be to do random number computations
#    in parallel.  If each processor is to compute 1,000 values, you can
#    guarantee that they work with distinct random values by starting the
#    first processor with SEED, the second with the value of SEED after 
#    1,000 applications of the LCRG, and so on.
#
#    To evaluate the N-th value of SEED directly, we start by ignoring 
#    the modular arithmetic, and working out the sequence of calculations
#    as follows:
#
#      SEED(0) =     SEED.
#      SEED(1) = a * SEED      + b
#      SEED(2) = a * SEED(1)   + b = a^2 * SEED + a * b + b
#      SEED(3) = a * SEED(2)   + b = a^3 * SEED + a^2 * b + a * b + b
#      ...
#      SEED(N) = a * SEED(N-1) + b = a^N * SEED 
#                                    + ( a^(n-1) + a^(n-2) + ... + a + 1 ) * b
#
#    or, using the geometric series,
#
#      SEED(N) = a^N * SEED + ( a^N - 1) / ( a - 1 ) * b
#
#    Therefore, we can determine SEED(N) directly if we can solve
#
#      ( a - 1 ) * BN = ( a^N - 1 ) * b in modular arithmetic,
#
#    and evaluated:
#
#      AN = a^N
#
#    Using the formula:
#
#      SEED(N) = AN * SEED + BN, mod c
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the multiplier for the LCRG.
#
#    integer B, the added value for the LCRG.
#
#    integer C, the base for the modular arithmetic.  For 32 bit
#    arithmetic, this is often 2^31 - 1, or 2147483647.  It is required
#    that 0 < C.
#
#    integer N, the "index", or number of times that the LCRG
#    is to be applied.  It is required that 0 <= N.
#
#    integer SEED, the starting value of SEED.  It is customary
#    that 0 < SEED.
#
#  Output:
#
#    integer SEED_LCRG, the value of SEED that would be output
#    if the LCRG were applied to the starting value N times.
#
  if ( n < 0 ):
    print ( '' )
    print ( 'lcrg_seed - Fatal error!' )
    print ( '  Illegal input value of N = %d' % ( n ) )
    raise Exception ( 'lcrg_seed - Fatal error!' )

  if ( c <= 0 ):
    print ( '' )
    print ( 'lcrg_seed - Fatal error!' )
    print ( '  Illegal input value of C = %d' % ( c ) )
    raise Exception ( 'lcrg_seed - Fatal error!' )

  if ( n == 0 ):
    seed_lcrg = ( seed % c )
    if ( seed_lcrg < 0 ):
      seed_lcrg = seed_lcrg + c
    return seed_lcrg
#
#  Get A^N.
#
  an = power_mod ( a, n, c )
#
#  Solve ( a - 1 ) * BN = ( a^N - 1 ) for BN.
#
#  The LCRG I have been investigating uses B = 0, so this code
#  has not been properly tested yet.
#
  bn, ierror = congruence ( a - 1, c, ( an - 1 ) * b )

  if ( ierror != 0 ):
    print ( '' )
    print ( 'lcrg_seed - Fatal error!' )
    print ( '  An error occurred in the congruence routine.' )
    print ( '  The error code was IERROR = %d' % ( ierror ) )
    raise Exception ( 'lcrg_seed - Fatal error!' )
#
#  Set the new SEED.
#
  value2 = an * seed + bn

  value2 = ( value2 % c )
#
#  Guarantee that the value is positive.
#
  if ( value2 < 0 ):
    value2 = value2 + c

  seed_lcrg = value2

  return seed_lcrg

def lcrg_seed_test ( ):

#*****************************************************************************80
#
## lcrg_seed_test() tests lcrg_seed().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'lcrg_seed_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  lcrg_seed directly computes the updated value of a' )
  print ( '  seed used by an linear congruential random number' )
  print ( '  generator.' )
  print ( '' )
  print ( '       I          SEED          SEED          SEED    U' )
  print ( '                 Input        Output          LCRG' )
  print ( '' )
#
#  These parameters define the old (1969) IBM 360 random number generator:
#
  a = 16807
  b = 0
  c = 2147483647
#
#  This seed value was used in Pierre L'Ecuyer's article.
#
  seed_start = 12345

  seed = seed_start
#
#  Compute 1000 random numbers "the hard way", that is, sequentially.
#  Every now and then, call lcrg_seed to compute SEED directly.
#
  for i in range ( 1, 1001 ):

    seed_in = seed
    u, seed = r4_uniform_01 ( seed )
    seed_out = seed

    if ( i <= 10 or i == 100 or i == 1000 ):

      seed_lcrg = lcrg_seed ( a, b, c, i, seed_start )

      print ( '  %6d  %12d  %12d  %12d  %14f' \
        % ( i, seed_in, seed_out, seed_lcrg, u ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'lcrg_seed_test' )
  print ( '  Normal end of execution.' )
  return

def power_mod ( a, n, m ):

#*****************************************************************************80
#
## power_mod() computes mod ( A^N, M ).
#
#  Discussion:
#
#    Some programming tricks are used to speed up the computation, and to
#    allow computations in which A**N is much too large to store in a
#    real word.
#
#    First, for efficiency, the power A**N is computed by determining
#    the binary expansion of N, then computing A, A**2, A**4, and so on
#    by repeated squaring, and multiplying only those factors that
#    contribute to A**N.
#
#    Secondly, the intermediate products are immediately "mod'ed", which
#    keeps them small.
#
#    For instance, to compute mod ( A^13, 11 ), we essentially compute
#
#       13 = 1 + 4 + 8
#
#       A^13 = A * A^4 * A^8
#
#       mod ( A^13, 11 ) = mod ( A, 11 ) * mod ( A^4, 11 ) * mod ( A^8, 11 ).
#
#    Fermat's little theorem says that if P is prime, and A is not divisible
#    by P, then ( A^(P-1) - 1 ) is divisible by P.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A, the base of the expression to be tested.
#    A should be nonnegative.
#
#    integer N, the power to which the base is raised.
#    N should be nonnegative.
#
#    integer M, the divisor against which the expression is tested.
#    M should be positive.
#
#    integer X, the remainder when A^N is divided by M.
#
  if ( a < 0 ):
    x = -1
    return x

  if ( int ( a ) != a ):
    x = -1
    return x

  if ( n < 0 ):
    x = -1
    return x

  if ( int ( n ) != n ):
    x = -1
    return x

  if ( m <= 0 ):
    x = -1
    return x

  if ( int ( m ) != m ):
    x = -1
    return x
#
#  A contains the successive squares of A.
#
  x = 1

  while ( 0 < n ):

    d = ( n % 2 )

    if ( d == 1 ):
      x = ( ( x * a ) % m )

    a = ( ( a * a ) %  m )
    n = ( ( n - d ) // 2 )
#
#  Ensure that 0 <= X.
#
  while ( x < 0 ):
    x = x + m

  return x

def power_mod_test ( ):

#*****************************************************************************80
#
## power_mod_test() tests power_mod().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'power_mod_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  power_mod computes the remainder of a power' )
  print ( '  of an integer modulo another integer.' )

  a = 7
  n = 50
  m = 11

  x = power_mod ( a, n, m )

  print ( '' )
  print ( '  A = %d' % ( a ) )
  print ( '  N = %d' % ( n ) )
  print ( '  M = %d' % ( m ) )
  print ( '  mod ( A^N, M ) = %d' % ( x ) )

  a = 3
  n = 118
  m = 119

  x = power_mod ( a, n, m )

  print ( '' )
  print ( '  A = %d' % ( a ) )
  print ( '  N = %d' % ( n ) )
  print ( '  M = %d' % ( m ) )
  print ( '  mod ( A^N, M ) = %d' % ( x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'power_mod_test:' )
  print ( '  Normal end of execution.' )
  return

def r4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r4mat_print() prints an R4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r4mat_print_some() prints out a portion of an R4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r4mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## r4mat_uniform_01() returns a unit pseudorandom R4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    integer SEED, the integer "seed" used to generate
#    the output random number.
#
#  Output:
#
#    real R(M,N), an array of random values between 0 and 1.
#
#    integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'r4mat_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r4mat_uniform_01 - Fatal error!' )

  r = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = seed * 4.656612875E-10

  return r, seed

def r4mat_uniform_01_test ( ):

#*****************************************************************************80
#
## r4mat_uniform_01_test() tests r4mat_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'r4mat_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r4mat_uniform_01 computes a random R4MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r4mat_uniform_01 ( m, n, seed )

  r4mat_print ( m, n, v, '  Random R4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r4mat_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def r4mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## r4mat_uniform_ab() returns a scaled pseudorandom R4MAT.
#
#  Discussion:
#
#    An R4MAT is an array of R4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A, B, the range of the pseudorandom values.
#
#    integer SEED, the integer "seed" used to generate
#    the output random number.
#
#  Output:
#
#    real R(M,N), an array of random values between 0 and 1.
#
#    integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'r4mat_uniform_ab - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r4mat_uniform_ab - Fatal error!' )

  r = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r4mat_uniform_ab_test ( ):

#*****************************************************************************80
#
## r4mat_uniform_ab_test() tests r4mat_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'r4mat_uniform_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r4mat_uniform_ab computes a random R4MAT.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r4mat_uniform_ab ( m, n, a, b, seed )

  r4mat_print ( m, n, v, '  Uniform R4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r4mat_uniform_ab_test:' )
  print ( '  Normal end of execution.' )
  return

def r4_uniform_01 ( seed ):

#*****************************************************************************80
#
## r4_uniform_01() returns a unit pseudorandom R4.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      r4_uniform_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#  Output:
#
#    real R, a random value between 0 and 1.
#
#    integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#

  i4_huge = 2147483647

  if ( seed == 0 ):
    print ( '' )
    print ( 'r4_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r4_uniform_01 - Fatal error!' )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r4_uniform_01_test ( ):

#*****************************************************************************80
#
## r4_uniform_01_test() tests r4_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r4_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r4_uniform_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  r4_uniform_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r4_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789

  print ( '' )
  print ( '  SEED  r4_uniform_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r4_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r4_uniform_01_test' )
  print ( '  Normal end of execution.' )
  return

def r4_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## r4_uniform_ab() returns a scaled pseudorandom R4.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    real A, B, the minimum and maximum values.
#
#    integer SEED, a seed for the random number generator.
#
#    real R, the randomly chosen value.
#
#    integer SEED, an updated seed for the random number generator.
#
  i4_huge = 2147483647

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'r4_uniform_ab - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r4_uniform_ab - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r4_uniform_ab_test ( ):

#*****************************************************************************80
#
## r4_uniform_ab_test() tests r4_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = 10.0
  b = 20.0

  print ( '' )
  print ( 'r4_uniform_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r4_uniform_ab returns random values in a given range:' )
  print ( '  [ A, B ]' )
  print ( '' )
  print ( '  For this problem:' )
  print ( '  A = %f' % ( a ) )
  print ( '  B = %f' % ( b ) )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):
    r, seed = r4_uniform_ab ( a, b, seed )
    print ( '  %f' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r4_uniform_ab_test' )
  print ( '  Normal end of execution' )
  return

def r4vec_print ( n, a, title ):

#*****************************************************************************80
#
## r4vec_print() prints an R4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
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
    print ( '%6d  %12g' % ( i, a[i] ) )

def r4vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## r4vec_uniform_01() returns a unit pseudorandom R4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
#    integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'r4vec_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r4vec_uniform_01 - Fatal error!' )

  x = np.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r4vec_uniform_01_test ( ):

#*****************************************************************************80
#
## r4vec_uniform_01_test() tests r4vec_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'r4vec_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r4vec_uniform_01 computes a random R4VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r4vec_uniform_01 ( n, seed )

  r4vec_print ( n, v, '  Uniform R4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r4vec_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def r4vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## r4vec_uniform_ab() returns a scaled pseudorandom R4VEC.
#
#  Discussion:
#
#    Each dimension ranges from A to B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Springer Verlag, pages 201-202, 1983.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, pages 362-376, 1986.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, pages 136-143, 1969.
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the range of the pseudorandom values.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
#    integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'r4vec_uniform_ab - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r4vec_uniform_ab - Fatal error!' )

  x = np.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = a + ( b - a ) * seed * 4.656612875E-10

  return x, seed

def r4vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## r4vec_uniform_ab_test() tests r4vec_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'r4vec_uniform_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r4vec_uniform_ab computes a random R4VEC.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r4vec_uniform_ab ( n, a, b, seed )

  r4vec_print ( n, v, '  Uniform R4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r4vec_uniform_ab_test:' )
  print ( '  Normal end of execution.' )
  return

def r8col_uniform_abvec ( m, n, a, b ):

#*****************************************************************************80
#
## r8col_uniform_abvec() returns a random matrix with row ranges.
#
#  Discussion:
#
#    An R8COL is an array of R8 values, regarded as a set of column vectors.
#
#    The user specifies a minimum and maximum value for each row.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in
#    the array.
#
#    real A(M), B(M), the lower and upper limits.
#
#  Output:
#
#    real R(M,N), the array of pseudorandom values.
#
  import numpy as np

  r = np.random.rand ( m, n )

  for i in range ( 0, m ):
    r[i,0:n] = a[i] + ( b[i] - a[i] ) * r[i,0:n]

  return r

def r8col_uniform_abvec_test ( ):

#*****************************************************************************80
#
## r8col_uniform_abvec_test() tests r8col_uniform_abvec().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  a = np.array ( ( -1.0, 0.0, 50.0, 100.0, 17.0 ) )
  b = np.array ( ( +1.0, 1.0, 55.0, 100.1, 20.0 ) )

  print ( '' )
  print ( 'r8col_uniform_abvec_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8col_uniform_abvec() computes a random scaled R8COL.' )
  print ( '' )
  print ( '   Col         Min         Max' )
  print ( '' )

  for i in range ( 0, m ):
    print ( '  %4d  %10g  %10g' % ( i, a[i], b[i] ) )

  v = r8col_uniform_abvec ( m, n, a, b )

  r8mat_print ( m, n, v, '  Random R8COL:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8col_uniform_abvec_test():' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## r8mat_uniform_01() returns a unit pseudorandom R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    integer SEED, the integer "seed" used to generate
#    the output random number.
#
#  Output:
#
#    real R(M,N), an array of random values between 0 and 1.
#
#    integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'r8mat_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r8mat_uniform_01 - Fatal error!' )

  r = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = seed * 4.656612875E-10

  return r, seed

def r8mat_uniform_01_test ( ):

#*****************************************************************************80
#
## r8mat_uniform_01_test() tests r8mat_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'r8mat_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_uniform_01 computes a random R8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8mat_uniform_01 ( m, n, seed )

  r8mat_print ( m, n, v, '  Random R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## r8mat_uniform_ab() returns a scaled pseudorandom R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A, B, the range of the pseudorandom values.
#
#    integer SEED, the integer "seed" used to generate
#    the output random number.
#
#  Output:
#
#    real R(M,N), an array of random values between 0 and 1.
#
#    integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'r8mat_uniform_ab - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r8mat_uniform_ab - Fatal error!' )

  r = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8mat_uniform_ab_test ( ):

#*****************************************************************************80
#
## r8mat_uniform_ab_test() tests r8mat_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'r8mat_uniform_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_uniform_ab computes a random R8MAT.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8mat_uniform_ab ( m, n, a, b, seed )

  r8mat_print ( m, n, v, '  Random R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_uniform_ab_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_uniform_abvec ( m, n, a, b ):

#*****************************************************************************80
#
## r8mat_uniform_abvec() returns a random matrix with row ranges.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A(M), B(M), the range of the pseudorandom values.
#
#  Output:
#
#    real R(M,N), an array of random values between 0 and 1.
#
  import numpy as np

  r = np.random.rand ( m, n )

  for i in range ( 0, m ):
    r[i,0:n] = a[i] + ( b[i] - a[i] ) * r[i,0:n]

  return r

def r8mat_uniform_abvec_test ( ):

#*****************************************************************************80
#
## r8mat_uniform_abvec_test() tests r8mat_uniform_abvec().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 December 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  a = np.array ( [  2.0, 0.0, -1.0, 100.0, 0.1 ] )
  b = np.array ( [ 10.0, 1.0,  0.0, 110.0, 0.2 ] )

  print ( '' )
  print ( 'r8mat_uniform_abvec_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_uniform_abvec computes a random R8MAT.' )

  r8vec2_print ( a, b, '  Lower and upper row limits:' )

  v = r8mat_uniform_abvec ( m, n, a, b )

  r8mat_print ( m, n, v, '  Random R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_uniform_abvec_test:' )
  print ( '  Normal end of execution.' )
  return

def r8row_uniform_abvec ( m, n, a, b ):

#*****************************************************************************80
#
## r8row_uniform_abvec() returns a random matrix with column ranges.
#
#  Discussion:
#
#    An R8ROW is an array of R8 values, regarded as a set of row vectors.
#
#    The user specifies a minimum and maximum value for each column.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in
#    the array.
#
#    real A(N), B(N), the lower and upper limits.
#
#  Output:
#
#    real R(M,N), the array of pseudorandom values.
#
  import numpy as np

  r = np.random.rand ( m, n )

  for j in range ( 0, n ):
    r[0:m,j] = a[j] + ( b[j] - a[j] ) * r[0:m,j]

  return r

def r8row_uniform_abvec_test ( ):

#*****************************************************************************80
#
## r8row_uniform_abvec_test() tests r8row_uniform_abvec().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  a = np.array ( ( -1.0, 0.0, 50.0, 100.0 ) )
  b = np.array ( ( +1.0, 1.0, 55.0, 100.1 ) )

  print ( '' )
  print ( 'r8row_uniform_abvec_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8row_uniform_abvec computes a random scaled R8ROW.' )
  print ( '' )
  print ( '   Col         Min         Max' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %10g  %10g' % ( i, a[i], b[i] ) )

  v = r8row_uniform_abvec ( m, n, a, b )

  r8mat_print ( m, n, v, '  Random R8ROW:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8row_uniform_abvec_test:' )
  print ( '  Normal end of execution.' )
  return

def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## r8_uniform_01() returns a unit pseudorandom R8.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r8_uniform_01 = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      r8_uniform_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#  Output:
#
#    real R, a random value between 0 and 1.
#
#    integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'r8_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r8_uniform_01 - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## r8_uniform_01_test() tests r8_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_uniform_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  r8_uniform_01(SEED)' )
  print ( '' )
  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789
  print ( '' )
  print ( '  SEED  r8_uniform_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_uniform_01_test' )
  print ( '  Normal end of execution.' )
  return

def r8_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## r8_uniform_ab() returns a scaled pseudorandom R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    real A, B, the minimum and maximum values.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    real R, the randomly chosen value.
#
#    integer SEED, an updated seed for the random number generator.
#
  i4_huge = 2147483647

  if ( seed == 0 ):
    print ( '' )
    print ( 'r8_uniform_ab - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r8_uniform_ab - Fatal error!' )

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8_uniform_ab_test ( ):

#*****************************************************************************80
#
## r8_uniform_ab_test() tests r8_uniform_ab().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = 10.0
  b = 20.0

  print ( '' )
  print ( 'r8_uniform_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_uniform_ab returns random values in a given range:' )
  print ( '  [ A, B ]' )
  print ( '' )
  print ( '  For this problem:' )
  print ( '  A = %f' % ( a ) )
  print ( '  B = %f' % ( b ) )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):
    r, seed = r8_uniform_ab ( a, b, seed )
    print ( '  %f' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_uniform_ab_test' )
  print ( '  Normal end of execution' )
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

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## r8vec_uniform_01() returns a unit pseudorandom R8VEC.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
#    integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'r8vec_uniform_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r8vec_uniform_01 - Fatal error!' )

  x = np.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## r8vec_uniform_01_test() tests r8vec_uniform_01().
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

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'r8vec_uniform_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_uniform_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_uniform_01_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## r8vec_uniform_ab() returns a scaled pseudorandom R8VEC.
#
#  Discussion:
#
#    Each dimension ranges from A to B.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Springer Verlag, pages 201-202, 1983.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, pages 362-376, 1986.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, pages 136-143, 1969.
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the range of the pseudorandom values.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
#    integer SEED, an updated seed for the random number generator.
#
  import numpy

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'r8vec_uniform_ab - Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r8vec_uniform_ab - Fatal error!' )

  x = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = a + ( b - a ) * seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## r8vec_uniform_ab_test() tests r8vec_uniform_ab().
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

  n = 10
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'r8vec_uniform_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_uniform_ab computes a random R8VEC.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_ab ( n, a, b, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_uniform_ab_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_abvec ( n, a, b ):

#*****************************************************************************80
#
## r8vec_uniform_ab() returns a random vector with a range for each entry.
#
#  Discussion:
#
#    Dimension I ranges from A(I) to B(I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), B(N), the range of the pseudorandom values.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
  import numpy as np

  x = np.random.rand ( n )
  x = a + ( b - a ) * x

  return x

def r8vec_uniform_abvec_test ( ):

#*****************************************************************************80
#
## r8vec_uniform_abvec_test() tests r8vec_uniform_abvec().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  a = np.array ( (  0.0, 0.20, 10.0, 52.0, -1.0 ) )
  b = np.array ( ( +1.0, 0.25, 20.0, 54.0, +1.0 ) )
 
  print ( '' )
  print ( 'r8vec_uniform_abvec_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_uniform_abvec computes a random R8VEC.' )

  v = r8vec_uniform_abvec ( n, a, b )

  print ( '' )
  print ( '   I         A         X         B' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %10g  %10g  %10g' % ( i, a[i], v[i], b[i] ) )
  print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_uniform_abvec_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

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

  return None

def uniform_test ( ):

#*****************************************************************************80
#
## uniform_test() tests uniform().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'uniform_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test uniform().' )
#
#  Support functions:
#
  congruence_test ( )
  get_seed_test ( )
  i4_gcd_test ( )
  i4_huge_test ( )
  i4_modp_test ( )
  i4_seed_advance_test ( )
  i4_sign_test ( )
  l4mat_uniform_test ( )
  lcrg_anbn_test ( )
  lcrg_seed_test ( )
  power_mod_test ( )
#
#  Main UNIFORM functions.
#
  bvec_uniform_test ( )

  c4_uniform_01_test ( )
  c4mat_uniform_01_test ( )
  c4vec_uniform_01_test ( )

  c8_uniform_01_test ( )
  c8mat_uniform_01_test ( )
  c8vec_uniform_01_test ( )

  ch_uniform_ab_test ( )

  i4_uniform_0i_test ( )
  i4_uniform_ab_test ( )
  i4mat_uniform_ab_test ( )
  i4vec_uniform_ab_test ( )

  l4_uniform_test ( )
  l4mat_uniform_test ( )
  l4vec_uniform_test ( )

  r4_uniform_01_test ( )
  r4_uniform_ab_test ( )
  r4mat_uniform_01_test ( )
  r4mat_uniform_ab_test ( )
  r4vec_uniform_01_test ( )
  r4vec_uniform_ab_test ( )
  r4vec_uniform_01_test ( )
  r4vec_uniform_ab_test ( )

  r8_uniform_01_test ( )
  r8_uniform_ab_test ( )
  r8mat_uniform_01_test ( )
  r8mat_uniform_ab_test ( )
  r8vec_uniform_01_test ( )
  r8vec_uniform_ab_test ( )

  r8col_uniform_abvec_test ( )
  r8mat_uniform_abvec_test ( )
  r8row_uniform_abvec_test ( )
  r8vec_uniform_abvec_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'uniform_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  uniform_test ( )
  timestamp ( )
 
