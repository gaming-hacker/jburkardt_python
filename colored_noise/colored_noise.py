#! /usr/bin/env python3
#
def colored_noise_test ( ):

#*****************************************************************************80
#
## colored_noise_test() tests colored_noise().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2021
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'colored_noise_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test colored_noise().' )

  r8vec_sftf_test ( )

  n = 128
  q_d = 1.0
  alpha = 0.00

  for i in range ( 0, 9 ):
    alpha = 0.25 * float ( i )
    colored_noise_test01 ( n, q_d, alpha )

  alpha = 0.0
  colored_noise_test02 ( alpha, 'alpha_0.00_paths.png' )

  alpha = 0.5
  colored_noise_test02 ( alpha, 'alpha_0.50_paths.png' )

  alpha = 1.0
  colored_noise_test02 ( alpha, 'alpha_1.00_paths.png' )

  alpha = 1.5
  colored_noise_test02 ( alpha, 'alpha_1.50_paths.png' )

  alpha = 2.0
  colored_noise_test02 ( alpha, 'alpha_2.00_paths.png' )
#
#  Terminate.
#
  print ( '' )
  print ( 'colored_noise_test():' )
  print ( '  Normal end of execution.' )
  return

def colored_noise_test01 ( n, q_d, alpha ):

#*****************************************************************************80
#
## colored_noise_test01() calls f_alpha() with particular parameters.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the sequence 
#    to generate.
#
#    real Q_D, the variance of the sequence.
#
#    real ALPHA, the exponent of the power law.
#
  output_filename = 'alpha_%4.2f.txt' % ( alpha )
#
#  Report parameters.
#
  print ( '' )
  print ( 'colored_noise_test01():' )
  print ( '  Generating %d sample points.' % ( n ) )
  print ( '  1/F^ALPHA noise has ALPHA = %f' % ( alpha ) )
  print ( '  Variance is %f' % ( q_d ) )

  x = f_alpha ( n, q_d, alpha )
#
#  Print no more than 10 entries of the data.
#
  r8vec_print_some ( n, x, 10, '  Noise sample:' )
#
#  Write the data to a file.
#
  output = open ( output_filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g\n' % ( x[i] )
    output.write ( s )

  output.close ( )

  print ( '  Data written to file "%s".' % ( output_filename ) )

  return

def colored_noise_test02 ( alpha, filename ):

#*****************************************************************************80
#
## colored_noise_test02() calls f_alpha() repeatedly.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real ALPHA, the exponent of the power law.
#
#    string FILENAME, the output filename.
#
#  Local:
#
#    integer N, the number of elements of the sequence 
#    to generate.
#
#    real Q_D, the variance of the sequence.
#
#    real X(N), the sequence.
#
  import matplotlib.pyplot as plt
  import numpy as np

  n_reals = 100
  n = 64
  q_d = 1.0
#
#  Report parameters.
#
  print ( '' )
  print ( 'colored_noise_test02():' )
  print ( '  Generating %d realizations' % ( n_reals ) )
  print ( '  Generating %d sample points.' % ( n ) )
  print ( '  1/F^ALPHA noise has ALPHA = %f' % ( alpha ) )
  print ( '  Variance is %f' % ( q_d ) )
#
#  To get 1, 2, ..., N, Python makes you follow their atrocious
#  off by one convention.
#
  x = np.arange ( 1, n + 1 )

  yave = np.zeros ( n )

  for i in range ( 0, n_reals ):
    y = f_alpha ( n, q_d, alpha )
    yave = yave + y
    if ( i < 5 ):
      plt.plot ( x, y, linewidth = 1, color = 'b' ) 
  yave = yave / float ( n_reals )
  plt.plot ( x, yave, linewidth = 2, color = 'k' )
  plt.grid ( True )
  s = 'ALPHA = %g,    5 realizations (blue), 100 averaged realizations (black)' % ( alpha )
  plt.title ( s )

  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def f_alpha ( n, q_d, alpha ):

#*****************************************************************************80
#
## f_alpha() generates a 1/F^ALPHA noise sequence.
#
#  Discussion:
#
#    Thanks to Miro Stoyanov for pointing out that the second half of
#    the data returned by the inverse Fourier transform should be
#    discarded, 24 August 2010.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2021
#
#  Author:
#
#    Original C version by Todd Walter.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jeremy Kasdin,
#    Discrete Simulation of Colored Noise and Stochastic Processes
#    and 1/f^a Power Law Noise Generation,
#    Proceedings of the IEEE,
#    Volume 83, Number 5, 1995, pages 802-827.
#
#  Input:
#
#    integer N, the number of samples to generate.
#
#    real Q_D, the variance of the noise.
#
#    real ALPHA, the exponent for the noise.
#
#  Output:
#
#    real X(N), a sequence sampled with the given power law.
#
  import numpy as np
#
#  Set the deviation of the noise.
#
  q_d = np.sqrt ( q_d )
#
#  Generate the coefficients Hk.
#
  hfa = np.zeros ( 2 * n )

  hfa[0] = 1.0 
  for i in range ( 1, n ):
    hfa[i] = hfa[i-1] * ( 0.5 * alpha + float ( i - 1 ) ) / float ( i )
#
#  Fill Wk with white noise.
#
  wfa = np.zeros ( 2 * n )
  for i in range ( 0, n ):
    wfa[i] = np.random.normal ( 0.0, 1.0 )
    wfa[i] = wfa[i] * q_d
#
#  Perform the discrete Fourier transforms of Hk and Wk.
#
  h_azero, h_a, h_b = r8vec_sftf ( 2 * n, hfa )

  w_azero, w_a, w_b = r8vec_sftf ( 2 * n, wfa )
#
#  Multiply the two complex vectors.
#
  w_azero = w_azero * h_azero

  for i in range ( 0, n ):
    wr = w_a[i]
    wi = w_b[i]
    w_a[i] = wr * h_a[i] - wi * h_b[i]
    w_b[i] = wi * h_a[i] + wr * h_b[i]
#
#  This scaling is introduced only to match the behavior
#  of the Numerical Recipes code...
#
  w_azero = w_azero * 2 * n

  for i in range ( 0, n - 1 ):
    w_a[i] = w_a[i] * float ( n )
    w_b[i] = w_b[i] * float ( n )

  w_a[n-1] = w_a[n-1] * float ( 2 * n )
  w_b[n-1] = w_b[n-1] * float ( 2 * n )
#
#  Take the inverse Fourier transform of the result.
#
  xlong = r8vec_sftb ( 2 * n, w_azero, w_a, w_b )
#
#  Discard the second half of the inverse Fourier transform.
#
  x = xlong[0:n]

  return x

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an r8vec.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2021
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
## r8vec_print_test() tests r8vec_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2021
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

def r8vec_print_some ( n, a, max_print, title ):

#*****************************************************************************80
#
## r8vec_print_some() prints "some" of an R8VEC.
#
#  Discussion:
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_PRINT, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(N), the vector to be printed.
#
#    integer MAX_PRINT, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '  %6d  %14g' % ( i, a[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    print ( '  ......  ..............' )
    i = n - 1
    print ( '  %6d  %14g' % ( i, a[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    i = max_print - 1
    print ( '  %6d  %14g  ...more entries...' % ( i, a[i] ) )

  return

def r8vec_print_some_test ( ):

#*****************************************************************************80
#
## r8vec_print_some_test() tests r8vec_print_some().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_print_some_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_print_some() prints some of an R8VEC.' )

  n = 100
  a = np.linspace ( 1.0, 100.0, n )

  max_print = 10

  r8vec_print_some ( n, a, max_print, '  No more than 10 lines of this vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_print_some_test():' )
  print ( '  Normal end of execution.' )
  return

def r8vec_sftb ( n, azero, a, b ):

#*****************************************************************************80
#
## r8vec_sftb() computes a "slow" backward Fourier transform of real data.
#
#  Discussion:
#
#    SFTB and SFTF are inverses of each other.  If we begin with data
#    AZERO, A, and B, and apply SFTB to it, and then apply SFTF to the
#    resulting R vector, we should get back the original AZERO, A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data values.
#
#    real AZERO, the constant Fourier coefficient.
#
#    real A(N/2), B(N/2), the Fourier coefficients.
#
#  Output:
#
#    real R(N), the reconstructed data sequence.
#
  import numpy as np

  r = np.zeros ( n )
  r[0:n] = azero

  for i in range ( 0, n ):
    k_hi = int ( n / 2 )
    for k in range ( 0, k_hi ):
      theta = float ( k * i * 2 ) * np.pi / float ( n )
      r[i] = r[i] + a[k] * np.cos ( theta ) + b[k] * np.sin ( theta )

  return r

def r8vec_sftf ( n, r ):

#*****************************************************************************80
#
## r8vec_sftf() computes a "slow" forward Fourier transform of real data.
#
#  Discussion:
#
#    SFTF and SFTB are inverses of each other.  If we begin with data
#    R and apply SFTB to it, and then apply SFTB to the resulting AZERO, 
#    A, and B, we should get back the original R.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data values.
#
#    real R(N), the data to be transformed.
#
#  Output:
#
#    real AZERO, = sum ( 1 <= I <= N ) R(I) / N.
#
#    real A(N/2), B(N/2), the Fourier coefficients.
#
  import numpy as np

  azero = np.sum ( r ) / float ( n )
  nhalf = int ( n / 2 )
  a = np.zeros ( nhalf )
  b = np.zeros ( nhalf )

  for i in range ( 0, nhalf ):

    for j in range ( 0, n ):
      theta = float ( 2 * ( i + 1 ) * j ) * np.pi / float ( n )
      a[i] = a[i] + r[j] * np.cos ( theta )
      b[i] = b[i] + r[j] * np.sin ( theta )

    a[i] = a[i] / float ( n )
    b[i] = b[i] / float ( n )

    if ( ( n % 2 ) == 1 or i < nhalf - 1 ):
      a[i] = 2.0 * a[i]
      b[i] = 2.0 * b[i]

  return azero, a, b

def r8vec_sftf_test ( ):

#*****************************************************************************80
#
## r8vec_sftf_test() tests r8vec_sftf().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_sftf_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_sftf() computes the "slow" Fourier transform (forward)' )
  print ( '  of a vector of real data.' )

  n = 15

  r = np.random.rand ( n )

  azero, a, b = r8vec_sftf ( n, r )
  nhalf = int ( n / 2 )
  
  print ( '' )
  print ( '  Fourier coefficients:' )
  print ( '' )
  print ( '  %10f' % ( azero ) )
  for i in range ( 0, nhalf ):
    print ( '  %10f  %10f' % ( a[i], b[i] ) )

  r2 = r8vec_sftb ( n, azero, a, b )

  print ( '' )
  print ( '  Compare data R and recovered data R2:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %10f  %10f' % ( r[i], r2[i] ) )  
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_sftf_test():' )
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
#    03 September 2021
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
  colored_noise_test ( )
  timestamp ( )
 
