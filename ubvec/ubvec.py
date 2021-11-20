#! /usr/bin/env python3
#
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

def ksubset_colex_unrank ( rank, k, n ):

#*****************************************************************************80
#
## ksubset_colex_unrank() computes the K subset of given colex rank.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer RANK, the rank of the K subset.
#
#    integer K, the number of elements each K subset must
#    have.  0 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#  Output:
#
#    integer T(K), describes the K subset of the given
#    rank.  T(I) is the I-th element.  The elements must be listed in
#    DESCENDING order.
#
  from scipy.special import comb
  import numpy as np
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'ksubset_colex_unrank - Fatal error!' )
    print ( '  The input N = %d is illegal.' % ( n ) )
    raise Exception ( 'ksubset_colex_unrank - Fatal error!' )

  if ( k == 0 ):
    t = np.zeros ( k )
    return t

  if ( k < 0 or n < k ):
    print ( '' )
    print ( 'ksubset_colex_unrank - Fatal error!' )
    print ( '  The input K = %d is illegal.' % ( k ) )
    raise Exception ( 'ksubset_colex_unrank - Fatal error!' )

  nksub = ksubset_enum ( k, n )

  if ( rank < 0 or nksub < rank ):
    print ( '' )
    print ( 'ksubset_colex_unrank - Fatal error!' )
    print ( '  The input RANK = %d is illegal.' % ( rank ) )
    raise Exception ( 'ksubset_colex_unrank - Fatal error!' )
 
  t = np.zeros ( k, dtype = np.int32 )

  x = n

  for i in range ( 0, k ):

    while ( rank < comb ( x, k - i ) ):
      x = x - 1

    t[i] = x + 1
    rank = rank - comb ( x, k - i )

  return t

def ksubset_colex_unrank_test ( ):

#*****************************************************************************80
#
## ksubset_colex_unrank_test() tests ksubset_colex_unrank().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_colex_unrank_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ksubset_colex_unrank unranks K-subsets of an N set,' )
  print ( '  using the colexicographic ordering:' )

  nksub = ksubset_enum ( k, n )
  rank = ( nksub // 2 )

  t = ksubset_colex_unrank ( rank, k, n )

  print ( '' )
  print ( '  The element of rank %d:' % ( rank ) )
  print ( '' )
  i4vec_print ( k, t, '  The element:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ksubset_colex_unrank_test:' )
  print ( '  Normal end of execution.' )
  return

def ksubset_enum ( k, n ):

#*****************************************************************************80
#
## ksubset_enum() enumerates the K element subsets of an N set.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer K, the number of elements each K subset must
#    have. 0 <= K <= N.
#
#    integer N, the number of elements in the master set.
#    0 <= N.
#
#  Output:
#
#    integer NKSUB, the number of distinct elements.
#
  from scipy.special import comb

  nksub = comb ( n, k )

  return nksub

def ksubset_enum_test ( ):

#*****************************************************************************80
#
## ksubset_enum_test() tests ksubset_colex_enum().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  k = 3
  n = 5

  print ( '' )
  print ( 'ksubset_enum_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ksubset_enum enumerates K-subsets of an N set.' )
#
#  Enumerate.
#
  print ( '' )
  print ( '      K:   0    1    2    3    4    5' )
  print ( '   N' )
  print ( '' )
  for n in range ( 0, 6 ):
    print ( '  %2d:  ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      nksub = ksubset_enum ( k, n )
      print ( '  %2d' % ( nksub ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ksubset_enum_test:' )
  print ( '  Normal end of execution.' )
  return

def morse_thue ( i ):

#*****************************************************************************80
#
## morse_thue() generates a Morse Thue number.
#
#  Discussion:
#
#    The Morse Thue sequence can be defined in a number of ways.
#
#    A) Start with the string containing the single letter '0' then
#       repeatedly apply the replacement rules '0' -> '01' and
#       '1' -> '10' to the letters of the string.  The Morse Thue sequence
#       is the resulting letter sequence.
#
#    B) Starting with the string containing the single letter '0',
#       repeatedly append the binary complement of the string to itself.
#       Thus, '0' becomes '0' + '1' or '01', then '01' becomes
#       '01' + '10', which becomes '0110' + '1001', and so on.
#
#    C) Starting with I = 0, the I-th Morse Thue number is determined
#       by taking the binary representation of I, adding the digits,
#       and computing the remainder modulo 2.
#
#  Example:
#
#     I  binary   S
#    --  ------  --
#     0       0   0
#     1       1   1
#     2      10   1
#     3      11   0
#     4     100   1
#     5     101   0
#     6     110   0
#     7     111   1
#     8    1000   1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the index of the Morse Thue number.
#    Normally, I is 0 or greater, but any value is allowed.
#
#  Output:
#
#    integer S, the Morse Thue number of index I.
#
  import numpy as np

  nbits = 32

  i_copy = np.abs ( i )
#
#  Expand I into binary form.
#
  b = ui4_to_ubvec ( i_copy, nbits )
#
#  Sum the 1's in the binary representation.
#
  s = np.sum ( b )
#
#  Take the value modulo 2.
#
  s = ( s % 2 )
  
  return s

def morse_thue_test ( ):

#*****************************************************************************80
#
## morse_thue_test() tests morse_thue().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 100

  print ( '' )
  print ( 'morse_thue_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  morse_thue computes the Morse Thue numbers.' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    s = morse_thue ( i )
    print ( '  %4d  %d' % ( i, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'morse_thue_test' )
  print ( '  Normal end of execution.' )
  return

def nim_sum ( i, j ):

#*****************************************************************************80
#
## nim_sum() computes the Nim sum of two integers.
#
#  Discussion:
#
#    If K is the Nim sum of I and J, then each bit of K is the exclusive
#    OR of the corresponding bits of I and J.
#
#  Example:
#
#     I     J     K     I base 2    J base 2    K base 2
#   ----  ----  ----  ----------  ----------  ----------
#      0     0     0           0           0           0
#      1     0     1           1           0           1
#      1     1     0           1           1           0
#      2     7     5          10         111         101
#     11    28    23        1011       11100       10111
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the integers to be Nim-summed.
#
#  Output:
#
#    integer K, the Nim sum of I and J.
#
  nbits = 32

  ivec = ui4_to_ubvec ( i, nbits )
  jvec = ui4_to_ubvec ( j, nbits )

  kvec = ubvec_xor ( nbits, ivec, jvec )

  k = ubvec_to_ui4 ( nbits, kvec )

  return k

def nim_sum_test ( ):

#*****************************************************************************80
#
## nim_sum_test() tests nim_sum().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 32
  ihi = 1000
  ilo = 0
  ntest = 5

  print ( '' )
  print ( 'nim_sum_test' )
  print ( '  nim_sum computes the Nim sum of two integers.' )
  print ( '' )
  print ( '    I    J    Nim(I+J)' )
  print ( '' )

  for i in range ( 0, ntest ):

    i1 = np.random.random_integers ( ilo, ihi )
    i1vec = ui4_to_ubvec ( i1, n )

    i2 = np.random.random_integers ( ilo, ihi )
    i2vec = ui4_to_ubvec ( i2, n )

    i3 = nim_sum ( i1, i2 )
    i3vec = ui4_to_ubvec ( i3, n )

    print ( '' )
    print ( '  I1, I2, I3 in decimal:' )
    print ( '' )
    print ( '  %3d' % ( i1 ) )
    print ( '  %3d' % ( i2 ) )
    print ( '  %3d' % ( i3 ) )
    print ( '' )
    print ( '  I1, I2, I3 in binary:' )
    print ( '' )
    ubvec_print ( n, i1vec, '' )
    ubvec_print ( n, i2vec, '' )
    ubvec_print ( n, i3vec, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'nim_sum_test:' )
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

def ubvec_add ( n, ubvec1, ubvec2 ):

#*****************************************************************************80
#
## ubvec_add() adds two unsigned binary vectors.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  UBVEC(1) is the units digit, UBVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Example:
#
#    N = 4
#
#     UBVEC1       +  UBVEC2       =  UBVEC3
#
#    ( 1 0 0 0 )   + ( 1 1 0 0 )   = ( 0 0 1 0 )
#
#      1           +   3           =   4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer UBVEC1(N), UBVEC2(N), the vectors to be added.
#
#  Output:
#
#    integer UBVEC3(N), the sum of the two input vectors.
#
  import numpy as np

  overflow = False

  ubvec3 = np.zeros ( n )
#
#  Add.
#
  for i in range ( 0, n ):
    ubvec3[i] = ubvec1[i] + ubvec2[i]
#
#  Carry.
#
  for i in range ( n - 1, -1, -1 ):
    while ( 2 <= ubvec3[i] ):
      ubvec3[i] = ubvec3[i] - 2
      if ( 0 < i ):
        ubvec3[i-1] = ubvec3[i-1] + 1
      else:
        overflow = True

  return ubvec3

def ubvec_add_test ( ):

#*****************************************************************************80
#
## ubvec_add_test() tests ubvec_add().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
 
  print ( '' )
  print ( 'ubvec_add_test' )
  print ( '  ubvec_add adds unsigned binary vectors representing' )
  print ( '  unsigned integers' )
  print ( '' )
  print ( '        I        J        K = I + J' )
  print ( '' )

  for test in range ( 0, 10 ):
    
    i = np.random.random_integers ( 0, 100 )
    j = np.random.random_integers ( 0, 100 )

    print ( '' )

    print ( '  %8d  %8d' % ( i, j ) )

    k = i + j

    print ( '  Directly:           %8d' % ( k ) )

    ubvec1 = ui4_to_ubvec ( i, n )
    ubvec2 = ui4_to_ubvec ( j, n )

    ubvec3 = ubvec_add ( n, ubvec1, ubvec2 )
    k = ubvec_to_ui4 ( n, ubvec3 )

    print ( '  ubvec_add           %8d' % ( k ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_add_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_and ( n, ubvec1, ubvec2 ):

#*****************************************************************************80
#
## ubvec_and() computes the AND of two unsigned binary vectors.
#
#  Discussion:
#
#    A UBVEC is a vector of N binary digits.
#
#    A UBVEC can be interpreted as a binary representation of an
#    unsigned integer, with the first entry being the coefficient of
#    2^(N-1) and the last entry the coefficient of 1.
#
#    UBVEC   #
#    -----  --
#    00000   0
#    00001   1
#    00010   2
#    10000  16
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer UBVEC1(N), UBVEC2(N), the vectors.
#
#  Output:
#
#    integer VALUE(N), the AND of the two vectors.
#
  import numpy as np

  value = np.zeros ( n )

  for i in range ( 0, n ):
    value[i] = min ( ubvec1[i], ubvec2[i] )

  return value

def ubvec_and_test ( ):

#*****************************************************************************80
#
## ubvec_and_test() tests ubvec_and().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
 
  print ( '' )
  print ( 'ubvec_and_test' )
  print ( '  ubvec_and computes the AND of two' )
  print ( '  unsigned binary vectors representing unsigned integers' )
  print ( '' )
  print ( '        I        J        K = I AND J' )
  print ( '' )

  for test in range ( 0, 10 ):
    
    i = np.random.random_integers ( 0, 100 )
    j = np.random.random_integers ( 0, 100 )

    ubvec1 = ui4_to_ubvec ( i, n )
    ubvec2 = ui4_to_ubvec ( j, n )
    ubvec3 = ubvec_and ( n, ubvec1, ubvec2 )

    k = ubvec_to_ui4 ( n, ubvec3 )

    print ( '  %8d  %8d  %8d' % ( i, j, k ) )

  return
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_and_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_check ( n, ubvec ):

#*****************************************************************************80
#
## ubvec_check() checks an unsigned binary vector.
#
#  Discussion:
#
#    The only check made is that the entries are all 0 or 1.
#
#    A UBVEC is a vector of N binary digits.
#
#    A UBVEC can be interpreted as a binary representation of an
#    unsigned integer, with the first entry being the coefficient of
#    2^(N-1) and the last entry the coefficient of 1.
#
#    UBVEC   #
#    -----  --
#    00000   0
#    00001   1
#    00010   2
#    10000  16
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer UBVEC(N), the vector to be checked.
#
#  Output:
#
#    bool VALUE, is True if the UBVEC is legal.
#
  value = True

  for i in range ( 0, n ):
    if ( ubvec[i] < 0 or 2 <= ubvec[i] ):
      value = False
      return value

  return value

def ubvec_check_test ( ):

#*****************************************************************************80
#
## ubvec_check_test() tests ubvec_check().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'ubvec_check_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_check check an unsigned binary vector.' )
  print ( '' )
  print ( '  CHECK?     UBVEC' )
  print ( '' )

  ubvec = np.array ( [ 1, 0, 0, 1, 1 ] )
  check = ubvec_check ( n, ubvec )
  print ( '  %5s:    ' % ( check ), end = '' )
  for j in range ( 0, n ):
    print ( '%d' % (ubvec[j] ), end = '' )
  print ( '' )

  ubvec = np.array ( [ 1, 0, 0, 1, 9 ] )
  check = ubvec_check ( n, ubvec )
  print ( '  %5s:    ' % ( check ), end = '' )
  for j in range ( 0, n ):
    print ( '%d' % (ubvec[j] ), end = '' )
  print ( '' )

  ubvec = np.array ( [ 1, 3, 0, 1, 1 ] )
  check = ubvec_check ( n, ubvec )
  print ( '  %5s:    ' % ( check ), end = '' )
  for j in range ( 0, n ):
    print ( '%d' % (ubvec[j] ), end = '' )
  print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_check_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_complement1 ( n, ubvec1 ):

#*****************************************************************************80
#
## ubvec_complement1() computes the one's complement of an unsigned binary vector.
#
#  Discussion:
#
#    A UBVEC is a vector of N binary digits.
#
#    A UBVEC can be interpreted as a binary representation of an
#    unsigned integer, with the first entry being the coefficient of
#    2^(N-1) and the last entry the coefficient of 1.
#
#    UBVEC   #
#    -----  --
#    00000   0
#    00001   1
#    00010   2
#    10000  16
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer UBVEC1(N), the vector to be complemented.
#
#  Output:
#
#    integer UBVEC2(N), the complemented vector.
#
  import numpy as np

  ubvec2 = np.zeros ( n )

  for i in range ( 0, n ):
    ubvec2[i] = 1 - ubvec1[i]

  return ubvec2

def ubvec_complement1_test ( ):

#*****************************************************************************80
#
## ubvec_complement1_test() tests ubvec_complement1().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'ubvec_complement1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_complement1 returns the 1\'s complement' )
  print ( '  of an unsigned binary vector.' )
  print ( '' )
  print ( '  UBVEC  Comp1' )
  print ( '' )

  for i in range ( 0, 5 ):
    ubvec1 = ubvec_random ( n )
    ubvec2 = ubvec_complement1 ( n, ubvec1 )
    print ( '  ', end = '' )
    for j in range ( 0, n ):
      print ( '%d' % ( ubvec1[j] ), end = '' )
    print ( '  ', end = '' )
    for j in range ( 0, n ):
      print ( '%d' % ( ubvec1[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_complement_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_enum ( n ):

#*****************************************************************************80
#
## ubvec_enum() enumerates the unsigned binary vectors of length N.
#
#  Discussion:
#
#    A UBVEC is a vector of N binary digits.
#
#    A UBVEC can be interpreted as a binary representation of an
#    unsigned integer, with the first entry being the coefficient of
#    2^(N-1) and the last entry the coefficient of 1.
#
#    UBVEC   #
#    -----  --
#    00000   0
#    00001   1
#    00010   2
#    10000  16
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#  Output:
#
#    integer VALUE, the number of binary vectors.
#
  value = 2 ** n

  return value

def ubvec_enum_test ( ):

#*****************************************************************************80
#
## ubvec_enum_test() tests ubvec_enum().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ubvec_enum_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_enum enumerates unsigned binary vectors' )
  print ( '  of N digits' )
  print ( '' )
  print ( '   N      Number' )
  print ( '' )

  for n in range ( 0, 11 ):
    
    n2 = ubvec_enum ( n )

    print ( '  %2d  %8d' % ( n, n2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_enum_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_next_gray ( n, t ):

#*****************************************************************************80
#
## ubvec_next_gray() computes the next UBVEC in the Gray code.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of digits in each element.
#    N must be positive.
#
#    integer T(N), an element of the Gray code, that is,
#    each entry T(I) is either 0 or 1.
#
#  Output:
#
#    integer T(N), the successor to the input value this
#    is an element of the Gray code, which differs from the input
#    value in a single position.
#
  import numpy as np

  weight = np.sum ( t )

  if ( ( weight % 2 ) == 0 ):

    if ( t[n-1] == 0 ):
      t[n-1] = 1
    else:
      t[n-1] = 0

    return t

  else:

    for i in range ( n - 1, 0, -1 ):
      if ( t[i] == 1 ):
        if ( t[i-1] == 0 ):
          t[i-1] = 1
        else:
          t[i-1] = 0
        return t
#
#  The final element was input.
#  Return the first element.
#
    for i in range ( 0, n ):
      t[i] = 0

  return t

def ubvec_next_gray_test ( ):

#*****************************************************************************80
#
## ubvec_next_gray_test() tests ubvec_next_gray().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'ubvec_next_gray_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_next_gray returns the next UBVEC in the Gray code.' )

  print ( '' )
  print ( '   K  UBVEC' )
  print ( '' )

  k = 0
  g = np.zeros ( n )

  while ( True ):

    print ( '  %2d  ' % ( k ), end = '' )
    for j in range ( 0, n ):
      print ( '%2d' % ( g[j] ), end = '' )
    print ( '' )

    k = k + 1
    g = ubvec_next_gray ( n, g )

    if ( np.sum ( g ) == 0 ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_next_gray_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_next_grlex ( n, ubvec ):

#*****************************************************************************80
#
## ubvec_next_grlex() generates the next UBVEC in GRLEX order.
#
#  Discussion:
#
#    N = 3
#
#    Input      Output
#    -----      ------
#    0 0 0  =>  0 0 1
#    0 0 1  =>  0 1 0
#    0 1 0  =>  1 0 0
#    1 0 0  =>  0 1 1
#    0 1 1  =>  1 0 1
#    1 0 1  =>  1 1 0
#    1 1 0  =>  1 1 1
#    1 1 1  =>  0 0 0
#
#    A UBVEC is a vector of N binary digits.
#
#    A UBVEC can be interpreted as a binary representation of an
#    unsigned integer, with the first entry being the coefficient of
#    2^(N-1) and the last entry the coefficient of 1.
#
#    UBVEC   #
#    -----  --
#    00000   0
#    00001   1
#    00010   2
#    10000  16
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension.
#
#    integer UBVEC(N), the binary vector whose 
#    successor is desired.
#
#  Output:
#
#    integer UBVEC(N), the successor to the input vector.
#
  import numpy as np
#
#  Initialize locations of 0 and 1.
#
  if ( ubvec[0] == 0 ):
    z = 0
    o = -1
  else:
    z = -1
    o = 0
#
#  Moving from right to left, search for a "1", preceded by a "0".
#
  for i in range ( n - 1, 0, -1 ):
    if ( ubvec[i] == 1 ):
      o = i
      if ( ubvec[i-1] == 0 ):
        z = i - 1
        break
#
#  UBVEC = 0
#
  if ( o == -1 ):

    ubvec[n-1] = 1
#
#  01 never occurs.  So for sure, B(0) = 1.
#
  elif ( z == -1 ):

    s = np.sum ( ubvec )

    if ( s == n ):
      for i in range ( 0, n ):
        ubvec[i] = 0
    else:
      for i in range ( 0, n - s - 1 ):
        ubvec[i] = 0
      for i in range ( n - s - 1, n ):
        ubvec[i] = 1
#
#  Found the rightmost "01" string.
#  Replace it by "10".
#  Shift following 1's to the right.
#
  else:

    ubvec[z] = 1
    ubvec[o] = 0
    s = 0
    for i in range ( o + 1, n ):
      s = s + ubvec[i]
    for i in range ( o + 1, n - s ):
      ubvec[i] = 0
    for i in range ( n - s, n ):
      ubvec[i] = 1

  return ubvec

def ubvec_next_grlex_test ( ):

#*****************************************************************************80
#
## ubvec_next_grlex_test() tests ubvec_next_grlex().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'ubvec_next_grlex_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_next_grlex computes unsigned binary vectors in GRLEX order.' )
  print ( '' )

  b = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, 17 ):
    print ( '  %2d:  ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( '%d' % ( b[j] ), end = '' )
    print ( '' )
    b = ubvec_next_grlex ( n, b )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_next_grlex_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_next ( n, ubvec ):

#*****************************************************************************80
#
## ubvec_next() generates the next UBVEC.
#
#  Discussion:
#
#    The vectors are produced in the order:
#
#    (0,0,...,0),
#    (0,0,...,1),
#    ...
#    (1,1,...,1)
#
#    and the "next" vector after (1,1,...,1) is (0,0,...,0).  That is,
#    we allow wrap around.
#
#    A UBVEC is a vector of N binary digits.
#
#    A UBVEC can be interpreted as a binary representation of an
#    unsigned integer, with the first entry being the coefficient of
#    2^(N-1) and the last entry the coefficient of 1.
#
#    UBVEC   #
#    -----  --
#    00000   0
#    00001   1
#    00010   2
#    10000  16
#
#  Example:
#
#    N = 3
#
#    Input      Output
#    -----      ------
#    0 0 0  =>  0 0 1
#    0 0 1  =>  0 1 0
#    0 1 0  =>  0 1 1
#    0 1 1  =>  1 0 0
#    1 0 0  =>  1 0 1
#    1 0 1  =>  1 1 0
#    1 1 0  =>  1 1 1
#    1 1 1  =>  0 0 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    integer UBVEC(N), a vector whose successor is desired.
#
#  Output:
#
#    integer UBVEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( ubvec[i] == 0 ):
      ubvec[i] = 1
      return ubvec

    ubvec[i] = 0

  return ubvec

def ubvec_next_test ( ):

#*****************************************************************************80
#
## ubvec_next_test() tests ubvec_next().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'ubvec_next_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_next computes the "next" unsigned binary vector.' )
  print ( '' )

  b = np.zeros ( n )

  for i in range ( 0, 17 ):
    ubvec_print ( n, b, '' )
    b = ubvec_next ( n, b )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_next_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_or ( n, ubvec1, ubvec2 ):

#*****************************************************************************80
#
## ubvec_or() computes the OR of two unsigned binary vectors.
#
#  Discussion:
#
#    A UBVEC is a vector of N binary digits.
#
#    A UBVEC can be interpreted as a binary representation of an
#    unsigned integer, with the first entry being the coefficient of
#    2^(N-1) and the last entry the coefficient of 1.
#
#    UBVEC   #
#    -----  --
#    00000   0
#    00001   1
#    00010   2
#    10000  16
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer UBVEC1(N), UBVEC2(N), the vectors.
#
#  Output:
#
#    integer VALUE(N), the OR of the two vectors.
#
  import numpy as np

  value = np.zeros ( n )

  for i in range ( 0, n ):
    value[i] = max ( ubvec1[i], ubvec2[i] )

  return value

def ubvec_or_test ( ):

#*****************************************************************************80
#
## ubvec_or_test() tests ubvec_or().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
 
  print ( '' )
  print ( 'ubvec_or_test' )
  print ( '  ubvec_or computes the OR of two' )
  print ( '  unsigned binary vectors representing unsigned integers' )
  print ( '' )
  print ( '        I        J        K = I OR J' )
  print ( '' )

  for test in range ( 0, 10 ):
    
    i = np.random.random_integers ( 0, 100 )
    j = np.random.random_integers ( 0, 100 )

    ubvec1 = ui4_to_ubvec ( i, n )
    ubvec2 = ui4_to_ubvec ( j, n )
    ubvec3 = ubvec_or ( n, ubvec1, ubvec2 )

    k = ubvec_to_ui4 ( n, ubvec3 )

    print ( '  %8d  %8d  %8d' % ( i, j, k ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_or_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_print ( n, ubvec, title ):

#*****************************************************************************80
#
## ubvec_print() prints a UBVEC, with an optional title.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  UBVEC(1) is the units digit, UBVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    integer UBVEC(N), the vector to be printed.
#
#    character ( len = * ) TITLE, a title to be printed first.
#    TITLE may be blank.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  for ihi in range ( n - 1, -1, -70 ):
    ilo = max ( ihi - 70 + 1, 0 )
    print ( '  ', end = '' )
    for i in range ( ihi, ilo - 1, -1 ):
      print ( '%1d' % ( ubvec[i] ), end = '' )
    print ( '' )

  return

def ubvec_print_test ( ):

#*****************************************************************************80
#
## ubvec_print_test() tests ubvec_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  ubvec = np.array ( [ 1, 0, 0, 1, 0, 1, 1, 1, 0, 0 ] )

  print ( '' )
  print ( 'ubvec_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_print prints an unsigned binary vector.' )

  ubvec_print ( n, ubvec, '  UBVEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_print_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_random ( n ):

#*****************************************************************************80
#
## ubvec_random() returns a pseudorandom BVEC.
#
#  Discussion:
#
#    A UBVEC is a vector of N binary digits.
#
#    A UBVEC can be interpreted as a binary representation of an
#    unsigned integer, with the first entry being the coefficient of
#    2^(N-1) and the last entry the coefficient of 1.
#
#    UBVEC   #
#    -----  --
#    00000   0
#    00001   1
#    00010   2
#    10000  16
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the vector.
#
#  Output:
#
#    integer UBVEC(N), a pseudorandom binary vector.
#
  import numpy as np

  ubvec = np.random.random_integers ( 0, 1, size = n )

  return ubvec

def ubvec_random_test ( ):

#*****************************************************************************80
#
## ubvec_random_test() tests ubvec_random().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'ubvec_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_random randomizes an unsigned binary vector.' )
  print ( '' )

  for i in range ( 0, 5 ):
    ubvec = ubvec_random ( n )
    ubvec_print ( n, ubvec, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_random_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_rank_gray ( n, ubvec ):

#*****************************************************************************80
#
## ubvec_rank_gray() ranks a UBVEC according to the Gray ordering.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    integer UBVEC(N), the vector to be printed.
#
#  Output:
#
#    integer RANK, the rank of the BVEC.
#
  ui4 = ubvec_to_ui4 ( n, ubvec )
  rank = ui4_rank_gray ( ui4 )

  return rank

def ubvec_rank_gray_test ( ):

#*****************************************************************************80
#
## ubvec_rank_gray_test() tests ubvec_rank_gray().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'ubvec_rank_gray_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_rank_gray ranks a UBVEC in the Gray ordering.' )
  print ( '' )
  print ( '  UBVEC   Rank' )
  print ( '' )
 
  for ui4 in range ( 0, 32 ):
    ubvec = ui4_to_ubvec ( ui4, n )
    rank = ubvec_rank_gray ( n, ubvec )
    print ( '  ', end = '' )
    for j in range ( 0, n ):
      print ( '%2d' % ( ubvec[j] ), end = '' )
    print ( '  %2d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_rank_gray_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_reverse ( n, ubvec1 ):

#*****************************************************************************80
#
## ubvec_reverse() reverses a UBVEC.
#
#  Discussion:
#
#    A UBVEC is a vector of N binary digits.
#
#    A UBVEC can be interpreted as a binary representation of an
#    unsigned integer, with the first entry being the coefficient of
#    2^(N-1) and the last entry the coefficient of 1.
#
#    UBVEC   #
#    -----  --
#    00000   0
#    00001   1
#    00010   2
#    10000  16
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer UBVEC1(N), the vector to be reversed.
#
#  Output:
#
#    integer UBVEC2(N), the reversed vector.
#
  import numpy as np

  ubvec2 = np.zeros ( n )

  for i in range ( 0, n ):
    ubvec2[i] = ubvec1[n-1-i]

  return ubvec2

def ubvec_reverse_test ( ):

#*****************************************************************************80
#
## ubvec_reverse_test() tests ubvec_reverse().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'ubvec_reverse_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_reverse reverses an unsigned binary vector.' )
  print ( '' )
  print ( '  UBVEC  Reversed' )
  print ( '' )

  for i in range ( 0, 5 ):
    ubvec1 = ubvec_random ( n )
    ubvec2 = ubvec_reverse ( n, ubvec1 )
    print ( '  ', end = '' )
    for j in range ( 0, n ):
      print ( '%d' % ( ubvec1[j] ), end = '' )
    print ( '  ', end = '' )
    for j in range ( 0, n ):
      print ( '%d' % ( ubvec2[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_reverse_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_test ( ):

#*****************************************************************************80
#
## ubvec_test() tests ubvec().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ubvec_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test ubvec().' )

  ksubset_colex_unrank_test ( )
  ksubset_enum_test ( )

  morse_thue_test ( )

  nim_sum_test ( )

  ubvec_add_test ( )
  ubvec_and_test ( )
  ubvec_check_test ( )
  ubvec_complement1_test ( )
  ubvec_enum_test ( )
  ubvec_next_test ( )
  ubvec_next_gray_test ( )
  ubvec_or_test ( )
  ubvec_print_test ( )
  ubvec_random_test ( )
  ubvec_rank_gray_test ( )
  ubvec_reverse_test ( )
  ubvec_to_ui4_test ( )
  ubvec_unrank_gray_test ( )
  ubvec_unrank_grlex_test ( )
  ubvec_xor_test ( )

  ui4_rank_gray_test ( )
  ui4_to_ubvec_test ( )
  ui4_unrank_gray_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_test:' )
  print ( '  Normal end of execution.' )
  return

def ubvec_to_ui4 ( n, ubvec ):

#*****************************************************************************80
#
## ubvec_to_ui4() makes an unsigned integer from an unsigned binary vector.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  UBVEC(1) is the units digit, UBVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Example:
#
#    N = 4
#
#        UBVEC   binary  I
#    ----------  -----  --
#    1  2  3  4
#    ----------
#    1, 0, 0, 0       1  1
#    0, 1, 0, 0      10  2
#    0, 0, 1, 1      11  3
#    0, 0, 1, 0     100  4
#    1, 0, 0, 1    1001  9
#    1, 1, 1, 1    1111 15
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer UBVEC(N), the binary representation.
#
#  Output:
#
#    integer VALUE, the integer.
#
  value = 0
  for i in range ( 0, n ):
    value = 2 * value + ubvec[i]

  return value

def ubvec_to_ui4_test ( ):

#*****************************************************************************80
#
## ubvec_to_ui4_test() tests ubvec_to_ui4().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'ubvec_to_ui4_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_to_ui4 converts an unsigned binary vector' )
  print ( '  to an unsigned integer' )
  print ( '' )
  print ( '  UI4 --> UBVEC  -->  UI4' )
  print ( '' )

  for ui4 in range ( 0, 11 ):
    ubvec = ui4_to_ubvec ( ui4, n )
    i2 = ubvec_to_ui4 ( n, ubvec )
    print ( '  %2d  ' % ( ui4 ), end = '' )
    for j in range ( 0, n ):
      print ( '%1d' % ( ubvec[j] ), end = '' )
    print ( '  %2d' % ( i2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_to_ui4_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_unrank_gray ( rank, n ):

#*****************************************************************************80
#
## ubvec_unrank_gray() unranks a UBVEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer RANK, the rank of the UBVEC.
#    0 <= RANK < 2^N.
#
#    integer N, the size of the UBVEC.
#
#  Output:
#
#    integer UBVEC(N), the UBVEC of given rank.
#
  ui4 = ui4_unrank_gray ( rank )
  ubvec = ui4_to_ubvec ( ui4, n )

  return ubvec

def ubvec_unrank_gray_test ( ):

#*****************************************************************************80
#
## ubvec_unrank_gray_test() tests ubvec_unrank_gray().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'ubvec_unrank_gray_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_unrank_gray unranks a UBVEC.' )
  print ( '' )
  print ( '  Rank  UBVEC' )
  print ( '' )
 
  for rank in range ( 0, 32 ):
    ubvec = ubvec_unrank_gray ( rank, n )
    print ( '  %4d  ' % ( rank ), end = '' )
    for j in range ( 0, n ):
      print ( '%2d' % ( ubvec[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_unrank_gray_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_unrank_grlex ( rank, n ):

#*****************************************************************************80
#
## ubvec_unrank_grlex() unranks a UBVEC using the GRLEX ordering.
#
#  Discussion:
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer RANK, the rank.
#    0 <= RANK < 2^N.
#
#    integer N, the size of the BVEC.
#
#  Output:
#
#    integer B(N), the UBVEC of the given rank.
#
  from scipy.special import comb
  import numpy as np

  mk = 0

  for k in range ( 0, n + 1 ):

    mk_old = mk
    mk_plus = comb ( n, k )
    mk = mk_old + mk_plus

    if ( rank < mk ):
      rank_k = rank - mk_old
      t = ksubset_colex_unrank ( rank_k, k, n )
      c = np.zeros ( n )
      for i in range ( 0, k ):
        c[t[i]-1] = 1
      
      b = ubvec_reverse ( n, c )
      return b
#
#  If we got here, the rank is too large.
#
  print ( '' )
  print ( 'ubvec_unrank_grlex - Fatal error!' )
  print ( '  Input value of rank is too high.' )
  raise Exception ( 'ubvec_unrank_grlex - Fatal error!' )

def ubvec_unrank_grlex_test ( ):

#*****************************************************************************80
#
## ubvec_unrank_grlex_test() tests ubvec_unrank_grlex().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'ubvec_unrank_grlex_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ubvec_unrank_grlex returns the UBVEC of given rank' )
  print ( '  in the graded lexicographical ordering.' )

  s = -1

  for rank in range ( 0, 16 ):
    b = ubvec_unrank_grlex ( rank, n )
    if ( s < np.sum ( b ) ):
      print ( '  --  --------' )
      s = np.sum ( b )
    print ( '  %2d  ' % ( rank ), end = '' )
    for j in range ( 0, n ):
      print ( '%2d' % ( b[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_unrank_grlex_test' )
  print ( '  Normal end of execution.' )
  return

def ubvec_xor ( n, ubvec1, ubvec2 ):

#*****************************************************************************80
#
## ubvec_xor() computes the exclusive OR of two UBVEC's.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  BVEC(1) is the units digit, BVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer UBVEC1(N), UBVEC2(N), the binary vectors to be XOR'ed.
#
#  Output:
#
#    integer UBVEC3(N), the exclusive OR of the two vectors.
#
  import numpy as np

  ubvec3 = np.zeros ( n )

  for i in range ( 0, n ):
    ubvec3[i] = ( ( ubvec1[i] + ubvec2[i] ) % 2 )

  return ubvec3

def ubvec_xor_test ( ):

#*****************************************************************************80
#
## ubvec_xor_test() tests ubvec_xor().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  test_num = 10

  print ( '' )
  print ( 'ubvec_xor_test' )
  print ( '  ubvec_xor exclusive-ors unsigned binary vectors representing' )
  print ( '  unsigned integers' )
  print ( '' )
  print ( '        I        J        K = I XOR J' )
  print ( '' )

  for test in range ( 0, 10 ):
    i = np.random.random_integers ( 0, 100 )
    j = np.random.random_integers ( 0, 100 )
    ubvec1 = ui4_to_ubvec ( i, n )
    ubvec2 = ui4_to_ubvec ( j, n )
    ubvec3 = ubvec_xor ( n, ubvec1, ubvec2 )
    k = ubvec_to_ui4 ( n, ubvec3 )
    print ( '  %8d  %8d  %8d' % ( i, j, k ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ubvec_xor_test' )
  print ( '  Normal end of execution.' )
  return

def ui4_rank_gray ( gray ):

#*****************************************************************************80
#
## ui4_rank_gray() ranks a Gray code.
#
#  Discussion:
#
#    This routine is entirely arithmetical,
#    and does not require access to bit testing and setting routines.
#
#    Given the number GRAY, its ranking is the order in which it would be
#    visited in the Gray code ordering.  The Gray code ordering begins
#
#    Rank  Gray  Gray
#          (Dec) (Bin)
#
#       0     0  0000
#       1     1  0001
#       2     3  0011
#       3     2  0010
#       4     6  0110
#       5     7  0111
#       6     5  0101
#       7     4  0100
#       8    12  0110
#       etc
#
#   This routine is given a Gray code, and has to return the rank.
#
#  Example:
#
#    Gray  Gray  Rank
#    (Dec) (Bin)
#
#     0       0     0
#     1       1     1
#     2      10     3
#     3      11     2
#     4     100     7
#     5     101     6
#     6     110     4
#     7     111     5
#     8    1000    15
#     9    1001    14
#    10    1010    12
#    11    1011    13
#    12    1100     8
#    13    1101     9
#    14    1110    11
#    15    1111    10
#    16   10000    31
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer GRAY, the Gray code to be ranked.
#
#  Output:
#
#    integer RANK, the rank of GRAY, and the integer
#    whose Gray code is GRAY.
#
  gray_copy = gray

  if ( gray_copy < 0 ):
    print ( '' )
    print ( 'ui4_rank_gray - Fatal error!' )
    print ( '  Input value of GRAY < 0.' )
    raise Exception ( 'ui4_rank_gray - Fatal error!' )

  if ( gray_copy == 0 ):
    rank = 0
    return rank
#
#  Find TWO_K, the largest power of 2 less than or equal to GRAY.
#
  k = 0
  two_k = 1
  while ( 2 * two_k <= gray_copy ):
    two_k = two_k * 2
    k = k + 1

  rank = two_k
  last = True
  gray_copy = gray_copy - two_k

  while ( 0 < k ):

    two_k = ( two_k // 2 )
    k = k - 1

    next = ( two_k <= gray_copy and gray_copy < two_k * 2 )

    if ( next ):
      gray_copy = gray_copy - two_k

    if ( next != last ):
      rank = rank + two_k
      last = True
    else:
      last = False

  return rank

def ui4_rank_gray_test ( ):

#*****************************************************************************80
#
## ui4_rank_gray_test() tests ui4_rank_gray().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'ui4_rank_gray_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ui4_rank_gray ranks a UI4 in the Gray ordering.' )
  print ( '' )
  print ( ' UI4  Rank  (binary)' )
  print ( '' )
 
  for ui4 in range ( 0, 32 ):
    rank = ui4_rank_gray ( ui4 )
    ubvec = ui4_to_ubvec ( ui4, n )
    print ( '  %2d    %2d  ' % ( ui4, rank ), end = '' )
    for j in range ( 0, n ):
      print ( '%2d' % ( ubvec[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ui4_rank_gray_test' )
  print ( '  Normal end of execution.' )
  return

def ui4_to_ubvec ( ui4, n ):

#*****************************************************************************80
#
## ui4_to_ubvec() makes a unsigned binary vector from an integer.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  BVEC(1) is the units digit, BVEC(N)
#    is the coefficient of 2**(N-1).
#
#    To guarantee that there will be enough space for any
#    value of I, it would be necessary to set N = 32.
#
#  Example:
#
#     I       BVEC         binary
#    --  ----------------  ------
#     1  1, 0, 0, 0, 0, 0       1
#     2  0, 1, 0, 0, 0, 0      10
#     3  1, 1, 0, 0, 0, 0      11
#     4  0, 0, 1, 0, 0, 0     100
#     9  1, 0, 0, 1, 0, 0    1001
#    -9  1, 1, 1, 0, 1, 1  110111
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer UI4, an integer to be represented.
#
#    integer N, the dimension of the vector.
#
#  Output:
#
#    integer BVEC(N), the unsigned binary representation.
#
  import numpy as np

  ubvec = np.zeros ( n )

  for i in range ( n - 1, -1, -1 ):
    ubvec[i] = ( ui4 % 2 )
    ui4 = ( ui4 // 2 )

  return ubvec

def ui4_to_ubvec_test ( ):

#*****************************************************************************80
#
## ui4_to_ubvec_test() tests ui4_to_ubvec().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'ui4_to_ubvec_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ui4_to_ubvec converts an unsigned integer to an' )
  print ( '  unsigned binary vector;' )
  print ( '' )
  print ( '  UI4 --> UBVEC  -->  UI4' )
  print ( '' )

  for i in range ( 0, 11 ):
    bvec = ui4_to_ubvec ( i, n )
    i2 = ubvec_to_ui4 ( n, bvec )
    print ( '  %2d  ' % ( i ), end = '' )
    for i in range ( 0, n ):
      print ( '%1d' % ( bvec[i] ), end = '' )
    print ( '  %2d' % ( i2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ui4_to_ubvec_test' )
  print ( '  Normal end of execution.' )
  return

def ui4_unrank_gray ( rank ):

#*****************************************************************************80
#
## ui4_unrank_gray() unranks a Gray code.
#
#  Discussion:
#
#    This routine is entirely arithmetical,
#    and does not require access to bit testing and setting routines.
#
#    The binary values of the Gray codes of successive integers differ in
#    just one bit.
#
#    The sequence of Gray codes for 0 to (2^N)-1 can be interpreted as a
#    Hamiltonian cycle on a graph of the cube in N dimensions.
#
#  Example:
#
#    Rank  Gray  Gray
#          (Dec) (Bin)
#
#     0     0       0
#     1     1       1
#     2     3      11
#     3     2      10
#     4     6     110
#     5     7     111
#     6     5     101
#     7     4     100
#     8    12    1100
#     9    14    1001
#    10    12    1010
#    11    13    1011
#    12     8    1100
#    13     9    1101
#    14    11    1110
#    15    10    1111
#    16    31   10000
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer RANK, the integer whose Gray code is desired.
#
#  Output:
#
#    integer GRAY, the Gray code of the given rank.
#
  if ( rank <= 0 ):
    gray = 0
    return gray

  rank_copy = rank
  k = 0
  two_k = 1
  while ( 2 * two_k <= rank_copy ):
    two_k = two_k * 2
    k = k + 1

  gray = two_k
  rank_copy = rank_copy - two_k
  next = True

  while ( 0 < k ):

    two_k = ( two_k // 2 )
    k = k - 1

    last = next
    next = ( two_k <= rank_copy and rank_copy <= two_k * 2 )

    if ( next != last ):
      gray = gray + two_k

    if ( next ):
      rank_copy = rank_copy - two_k

  return gray

def ui4_unrank_gray_test ( ):

#*****************************************************************************80
#
## ui4_unrank_gray_test() tests ui4_unrank_gray().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'ui4_unrank_gray_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ui4_unrank_gray unranks a Gray code.' )
  print ( '' )
  print ( '  Rank   I  (binary)' )
  print ( '' )
 
  for rank in range ( 0, 32 ):
    ui4 = ui4_unrank_gray ( rank )
    ubvec = ui4_to_ubvec ( ui4, n )
    print ( '  %2d    %2d  ' % ( rank, ui4 ), end = '' )
    for j in range ( 0, n ):
      print ( '%2d' % ( ubvec[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ui4_unrank_gray_test' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  ubvec_test ( )
  timestamp ( )
 
