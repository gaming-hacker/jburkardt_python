#! /usr/bin/env python3
#
def normalize ( n, x ):

#****************************************************************************80
#
## normalize() scales a vector X so its entries sum to 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2016
#
#  Author:
#
#    Original C version by Warren Smith.
#    Python version by John Burkardt.
#
#  Input:
#
#    integer N, indicates the size of X.
#
#    real X[N+2], the vector to be normalized.
#
#  Output:
#
#    real X[N+2], the normalized vector.

#
#  Sum X.
#
  sum = 0.0
  for i in range ( 1, n + 1 ):
    sum = sum + abs ( x[i] )
#
#  Normalize so that the new sum of X will be 1.
#
  for i in range ( 1, n + 1 ):
    x[i] = x[i] / sum

  return x

def normalize_test ( ):

#*****************************************************************************80
#
## normalize_test() tests normalize().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'NORMALIZE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMALIZE normalizes entries 1 through N of a vector' )
  print ( '  of length N+2.' )

  n = 5
  x = np.random.rand ( n + 2 )
  r8vec_print ( n + 2, x, '  Initial X:' )

  x_norm = 0.0
  for i in range ( 1, n + 1 ):
    x_norm = x_norm + abs ( x[i] )
  print ( '' )
  print ( '  Initial L1 norm of X(1:%d) = %10.6g' % ( n, x_norm ) )

  x = normalize ( n, x )

  r8vec_print ( n + 2, x, '  Normalized X:' )

  x_norm = 0.0
  for i in range ( 1, n + 1 ):
    x_norm = x_norm + abs ( x[i] )
  print ( '' )
  print ( '  Final L1 norm of X(1:%d) = %10.6g' % ( n, x_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMALIZE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_indicator0 ( n ):

#*****************************************************************************80
#
## r8vec_indicator0() sets an R8VEC to the indicator vector (0,1,2,...).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i

  return a

def r8vec_indicator0_test ( ):

#*****************************************************************************80
#
## r8vec_indicator0_test() tests r8vec_indicator0().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_INDICATOR0_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_INDICATOR0 returns an indicator matrix.' )

  n = 10
  a = r8vec_indicator0 ( n )

  r8vec_print ( n, a, '  The indicator0 vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_INDICATOR0_TEST' )
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

def random_permutation ( n, x ):

#****************************************************************************80
#
## random_permutation() applies a random permutation to an array.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2016
#
#  Author:
#
#    Original C version by Warren Smith.
#    Python version by John Burkardt.
#
#  Input:
#
#    integer N, indicates the size of X.
#
#    real X[N+2], the vector to be permuted.
#
#  Output:
#
#    real X[N+2], the permuted vector.
#
  import numpy as np

  for i in range ( 1, n + 1 ):

    j = np.random.random_integers ( i, n )

    t    = x[i]
    x[i] = x[j]
    x[j] = t      
  
  return x

def random_permutation_test ( ):

#*****************************************************************************80
#
## random_permutation_test() tests random_permutation().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'RANDOM_PERMUTATION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RANDOM_PERMUTATION randomly permutes entries 1 through N of' )
  print ( '  a vector X[0:N+1].' )

  n = 5
  x = r8vec_indicator0 ( n + 2 )
  r8vec_print ( n + 2, x, '  Initial X:' )
  x = random_permutation ( n, x )
  r8vec_print ( n + 2, x, '  Permuted X:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'RANDOM_PERMUTATION_TEST' )
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

  return None

def walker_build ( n, x ):

#****************************************************************************80
#
## walker_build() sets up the data for a Walker sampler.
#
#  Discussion:
#
#    From the probability vector X, this function creates the Y and A 
#    vectors used by the Walker sampler.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2016
#
#  Author:
#
#    Original C version by Warren Smith.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Warren Smith,
#    How to sample from a probability distribution,
#    April 18, 2002.
#
#  Input:
#
#    integer N, indicates the size of X.
#
#    real X[N+2], contains in X[1] through X[N] the
#    probabilities of outcomes 1 through N.
#
#  Output:
#
#    real [N+2], the Walker threshold vector.
#
#    integer int A[N+2], the Walker index vector.
#
  import numpy as np
#
#  Initialize A.
#
  a = np.zeros ( n + 2, dtype = np.int32 )
  for i in range ( 0, n + 2 ):
    a[i] = i
#
#  Initialize B to the "stay here" value, and set sentinel values at the ends.
#
  b = np.zeros ( n + 2, dtype = np.int32 )

  for i in range ( 0, n + 2 ):
    b[i] = a[i]
#
#  Copy X into Y.
#  Scale the probability vector and set sentinel values at the ends.
#
  y = np.zeros ( n + 2, dtype = np.float64 )

  y[0] = 0.0
  for i in range ( 1, n + 1 ):
    y[i] = x[i] * float ( n )
  y[n+1] = 2.0

  i = 0
  j = n + 1

  while ( True ):
#
#  Find i so Y[B[i]] needs more.
#
    while ( True ):
      i = i + 1
      if ( 1.0 <= y[b[i]] ):
        break
#
#  Find j so Y[B[j]] wants less.
#
    while ( True ):
      j = j - 1
      if ( y[b[j]] < 1.0 ):
        break

    if ( j <= i ):
      break
#
#  Swap B[i] and B[j].
#
    k    = b[i]
    b[i] = b[j]
    b[j] = k

  i = j
  j = j + 1

  while ( 0 < i ):
#
#  Find J such that Y[B[j]] needs more.
#
    while ( y[b[j]] <= 1.0 ):
      j = j + 1
#
#  Meanwhile, Y[B[i]] wants less.
#
    if ( n < j ):
      break
#
#  B[i] will donate to B[j] to fix up.
#
    y[b[j]] = y[b[j]] - ( 1.0 - y[b[i]] )     
    a[b[i]] = b[j]             
# 
#  Y[B[j]] now wants less so readjust ordering.
#
    if ( y[b[j]] < 1.0 ):
      k    = b[i]
      b[i] = b[j]
      b[j] = k
      j = j + 1
    else:
      i = i - 1

  return y, a

def walker_build_test ( ):

#*****************************************************************************80
#
## walker_build_test() tests walker_build().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import comb
  import numpy as np
  import platform

  print ( '' )
  print ( 'WALKER_BUILD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WALKER_BUILD builds the Walker sampler data vectors Y and A,' )
  print ( '  given a probability vector X.' )

  n = 5
  x = np.zeros ( n + 2, dtype = np.float64 )
  for i in range ( 1, n + 1 ):
    x[i] = float ( comb ( n - 1, i - 1 ) ) / float ( 2 ** ( n - 1 ) )
  r8vec_print ( n + 2, x, '  Binomial PDF (ignore first and last entries):' )

  y, a = walker_build ( n, x )
  print ( '' )
  print ( '   I    A[I]    Y[i] (ignore first and last entries)' )
  print ( '' )
  for i in range ( 0, n + 2 ):
    print ( '  %2d  %2d  %10.4g' % ( i, a[i], y[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'WALKER_BUILD_TEST' )
  print ( '  Normal end of execution.' )
  return

def walker_sampler ( n, y, a ):

#****************************************************************************80
#
## walker_sampler() returns a random sample i=1..N with prob X[i].
#
#  Discussion:
#
#    Implementation of algorithm for sampling from a discrete
#    probability N-vector X[1], X[2], ..., X[N].  (N>=1.)
#    Runs on O(1) worst case time per sample,
#    and uses one integer and one real N-element array for storage.
#    Preprocessing consumes O(N) time and temporarily uses one 
#    additional integer array (B[0..N+1]) for bookkeeping. 
#    X[0] and X[N+1] are also used as sentinels in the Build() algorithm.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2016
#
#  Author:
#
#    Original C version by Warren Smith.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Warren Smith,
#    How to sample from a probability distribution,
#    April 18, 2002.
#
#  Input:
#
#    integer N, indicates the size of the probability vector X.
#
#    real Y[N+2], the Walker threshold vector.
#
#    integer A[N+2], the Walker index vector.
#
#  Output:
#
#    integer I, a sample value between 1 and N,
#    selected according to the probability vector X.
#
  import numpy as np
  import random as rn
# 
#  Let i = random uniform integer from {1,2,...N}  
#
  i = 1 + int ( np.fix ( float ( n ) * rn.random ( ) ) )

  r = rn.random ( )

  if ( y[i] < r ):
    i = a[i]

  return i
 
def walker_sampler_test ( ):

#****************************************************************************80
#
## walker_sampler_test() tests walker_sampler().
#
#  Discussion:
#
#    A Zipf-type probability vector is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2016
#
#  Author:
#
#    Original C version by Warren Smith.
#    Python version by John Burkardt.
#
#  Input:
#
#    integer N, indicates the size of the probability vector X.
#
#    real P, the value of the Zipf parameter
#    1 <= P.
#
  import numpy as np
  import platform
  import random as rn

  n = 10
  p = 2.0

  print ( '' )
  print ( 'WALKER_SAMPLER_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WALKER_SAMPLER creates Walker sample vectors Y and A' )
  print ( '  for efficient sampling of a discrete probability vector.' )
  print ( '  Test the Walker sampler with a Zipf-type probability.' )
#
#  Generate a standard Zipf probability vector for cases 1 - N,
#  with parameter P.
#
  x = zipf_probability ( n, p )

  print ( '' )
  print ( '  Zipf probabilities' )
  print ( '  for N = %d' % ( n ) )
  print ( '  and parameter P = %g' % ( p ) )
  print ( '' )
  print ( '     I     X[I]' )
  print ( '' )
  for i in range ( 1, n + 1 ):
    print ( '  %4d  %16g' % ( i, x[i] ) )
#
#  For better testing, randomly scramble the probabilities.
#
  x = random_permutation ( n, x )

  print ( '' )
  print ( '  Randomly permuted X:' )
  print ( '' )
  print ( '     I     X[I]' )
  print ( '' )
  for i in range ( 1, n + 1 ):
    print ( '  %4d  %16g' % ( i, x[i] ) )
#
#  Build the Walker sampler.
#
  y, a = walker_build ( n, x )

  print ( '' )
  print ( '  Built the sampler' )
  print ( '  i Y[i] A[i]:' )
  print ( '' )

  for i in range ( 0, n + 2 ):
    print ( '  %3d  %16g  %4d' % ( i, y[i], a[i] ) )
#
#  Prepare to count the frequency of each outcome.
#
  count = np.zeros ( n + 2, dtype = np.int32 )
#
#  Call the sampler many times.
#
  for i in range ( 0, 100000 ):
    j = walker_sampler ( n, y, a )
    count[j] = count[j] + 1
#
#  Compare normalized sample frequencies to the original probabilities in X.
#
  v = 0.0
  print ( '' )
  print ( '  100000 samples:' )
  print ( '  prob   #samples:' )
  print ( '' )

  for i in range ( 1, n + 1 ):
    print ( '  %16g  %6d' % ( x[i], count[i] ) )
    expval = x[i] * 100000
    t = expval - count[i]
    v = v + t * t / expval

  v = v / ( float ) ( n )

  print ( '' )
  print ( '  sumvar = %g, (should be about 1)' % ( v ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'WALKER_SAMPLER_TEST' )
  print ( '  Normal end of execution.' )
  return

def walker_sample_test ( ):

#*****************************************************************************80
#
## walker_sample_test() tests walker_sample().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'WALKER_SAMPLE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test WALKER_SAMPLE()' )

  normalize_test ( )
  r8vec_indicator0_test ( )
  random_permutation_test ( )
  walker_build_test ( )
  walker_sampler_test ( )
  walker_verify_test ( )
  zipf_probability_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'WALKER_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def walker_verify ( n, x, y, a ):

#****************************************************************************80
#
## walker_verify() verifies a Walker Sampler structure.
#
#  Discussion:
#
#    This test applies the sampling algorithms to a Zipfian distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2016
#
#  Author:
#
#    Original C version by Warren Smith.
#    Python version by John Burkardt.
#
#  Input:
#
#    integer N, indicates the size of X.
#
#    real X[N+2], contains in X[1] through X[N] the
#    probabilities of outcomes 1 through N.
#
#    real Y[N+2], the Walker threshold vector.
#
#    integer A[N+2], the Walker index vector.
#
#  Output:
#
#    real V, the sum of the absolute value of discrepancies.
#
  import numpy as np

  z = np.zeros ( n + 2, dtype = np.float64 )
#
#  Reverse the scaling.
#
  for i in range ( 0, n + 2 ):
    z[i] = y[i] / float ( n )
#
#  Add back the adjustments.
#
  for i in range ( 1, n + 1 ):
    z[a[i]] = z[a[i]] + ( 1.0 - y[i] ) / float ( n )
#
#  Check for discrepancies between Z and X.
#
  v = 0.0
  for i in range ( 1, n + 1 ):
    v = v + abs ( z[i] - x[i] )

  return v

def walker_verify_test ( ):

#*****************************************************************************80
#
## walker_verify_test() tests walker_verify().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'WALKER_VERIFY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WALKER_VERIFY verifies the Walker sampler data vectors Y and A,' )
  print ( '  for a given probability vector X.' )

  n = 9
  x = np.zeros ( n + 2, dtype = np.float64 )
  for i in range ( 1, n + 1 ):
    x[i] = np.log ( 1.0 + 1.0 / float ( i ) ) / np.log ( float ( n + 1 ) )
  r8vec_print ( n + 2, x, '  Benford PDF (ignore first and last entries):' )

  y, a = walker_build ( n, x )

  print ( '' )
  print ( '   I    A[I]    Y[i] (ignore first and last entries)' )
  print ( '' )
  for i in range ( 0, n + 2 ):
    print ( '  %2d  %2d  %10.4g' % ( i, a[i], y[i] ) )

  v = walker_verify ( n, x, y, a )

  print ( '' )
  print ( '  The verification sum = %g' % ( v ) )
  print ( '  It should be very close to zero.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'WALKER_VERIFY_TEST' )
  print ( '  Normal end of execution.' )
  return

def zipf_probability ( n, p ):

#****************************************************************************80
#
## zipf_probability() sets up a Zipf probability vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2016
#
#  Author:
#
#    Original C version by Warren Smith.
#    Python version by John Burkardt.
#
#  Reference:
#
#    George Zipf,
#    The Psychobiology of Language,
#    1935.
#
#  Input:
#
#    integer N, indicates the size of X.
#
#    real P, the Zipf parameter.
#    1.0 < P.
#
#  Output:
#
#    real X[N+2], contains in X[1] through X[N] the
#    probabilities of outcomes 1 through N.
#
  import numpy as np

  x = np.zeros ( n + 2 )

  for i in range ( 1, n + 1 ):
    x[i] = i ** ( - p )

  x = normalize ( n, x )

  return x

def zipf_probability_test ( ):

#*****************************************************************************80
#
## zipf_probability_test() tests zipf_probability().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ZIPF_PROBABILITY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ZIPF_PROBABILITY sets up a probablity vector X of N+2 elements' )
  print ( '  containing in X[1:N] the probabilities of outcomes 1 through N' )
  print ( '  in a Zipf distribution with parameter P.' )

  n = 5
  p = 1.0
  x = zipf_probability ( n, p )
  r8vec_print ( n + 2, x, '  X for N = 5, P = 1.0' )

  n = 5
  p = 2.0
  x = zipf_probability ( n, p )
  r8vec_print ( n + 2, x, '  X for N = 5, P = 2.0' )

  n = 10
  p = 2.0
  x = zipf_probability ( n, p )
  r8vec_print ( n + 2, x, '  X for N = 10, P = 2.0' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ZIPF_PROBABILITY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  walker_sample_test ( )
  timestamp ( )

