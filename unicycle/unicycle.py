#! /usr/bin/env python3
#
def i4_modp ( i, j ):

#*****************************************************************************80
#
## i4_modp() returns the nonnegative remainder of I4 division.
#
#  Discussion:
#
#    If
#      NREM = I4_MODP ( I, J )
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
#    On the other hand, I4_MODP(A,360) is between 0 and 360, always.
#
#  Example:
#
#        I     J     MOD  I4_MODP    Factorization
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
    print ( 'i4_modp(): Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    raise Exception ( 'i4_modp(): Fatal error!' )

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
  print ( 'i4_modp_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_modp() factors a number' )
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
  print ( 'i4_modp_test():' )
  print ( '  Normal end of execution.' )
  return

def i4vec_indicator1 ( n ):

#*****************************************************************************80
#
## i4vec_indicator1() sets an I4VEC to the indicator vector ( 1, 2, 3, ... ).
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
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
#    integer A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def i4vec_indicator1_test ( ):

#*****************************************************************************80
#
## i4vec_indicator1_test() tests i4vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4vec_indicator1_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_indicator1() returns an indicator vector.' )

  n = 10
  a = i4vec_indicator1 ( n )
  i4vec_print ( n, a, '  The indicator1 vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_indicator1_test():' )
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

def i4vec_print_test ( ):

#*****************************************************************************80
#
## i4vec_print_test() tests i4vec_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4vec_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_print() prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_print_test():' )
  print ( '  Normal end of execution.' )
  return

def i4vec_reverse ( n, a ):

#*****************************************************************************80
#
## i4vec_reverse() reverses the elements of an I4VEC.
#
#  Example:
#
#    Input:
#
#      N = 5,
#      A = ( 11, 12, 13, 14, 15 ).
#
#    Output:
#
#      A = ( 15, 14, 13, 12, 11 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    integer A(N), the array to be reversed.
#
#  Output:
#
#    integer A(N), the reversed array.
#
  for i in range ( 0, n // 2 ):
    j = n - i - 1
    t    = a[i]
    a[i] = a[j]
    a[j] = t

  return a

def i4vec_reverse_test ( ):

#*****************************************************************************80
#
## i4vec_reverse_test() tests i4vec_reverse().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2009
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  b = 0
  c = 3 * n

  print ( '' )
  print ( 'i4vec_reverse_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4vec_reverse() reverses a list of integers.' )

  a = np.random.random_integers ( b, c, size = n )

  i4vec_print ( n, a, '  Original vector:' )

  a = i4vec_reverse ( n, a )

  i4vec_print ( n, a, '  Reversed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4vec_reverse_test():' )
  print ( '  Normal end of execution.' )

  return

def i4_wrap ( ival, ilo, ihi ):

#*****************************************************************************80
#
## i4_wrap() forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    ILO = 4, IHI = 8
#
#    I   Value
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
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
#    integer IVAL, an integer value.
#
#    integer ILO, IHI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of IVAL.
#
  jlo = min ( ilo, ihi )
  jhi = max ( ilo, ihi )

  wide = jhi - jlo + 1

  if ( wide == 1 ):
    value = jlo
  else:
    value = jlo + i4_modp ( ival - jlo, wide )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## i4_wrap_test() tests i4_wrap().
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
  import platform

  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'i4_wrap_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  i4_wrap() forces an integer to lie within given limits.' )
  print ( '' )
  print ( '  ILO = %d' % ( ilo ) )
  print ( '  IHI = %d' % ( ihi ) )
  print ( '' )
  print ( '     I  I4_WRAP(I)' )
  print ( '' )

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print ( '  %6d  %6d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'i4_wrap_test()' )
  print ( '  Normal end of execution.' )
  return

def perm1_check ( n, p ):

#*****************************************************************************80
#
## perm1_check() checks a permutation of (1,...,N).
#
#  Discussion:
#
#    The routine verifies that each of the integers from 1 to
#    to N occurs among the N entries of the permutation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries.
#
#    integer P(N), the array to check.
#
#  Output:
#
#    bool CHECK:
#    True if P is a legal permutation of (1,...,N).
#    False if P is not a legal permutation of (1,...,N).
#
  check = True

  for value in range ( 1, n + 1 ):

    check = False

    for location in range ( 0, n ):
      if ( p[location] == value ):
        check = True
        break

    if ( not check ):
#     print ( '' )
#     print ( 'PERM1_check - Warning!' )
#     print ( '  Permutation is missing the value %d.' % ( value ) )
      return check

  return check

def perm1_check_test ( ):

#*****************************************************************************80
#
## perm1_check_test() tests perm1_check().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  p1 = np.array ( [ 5, 2, 3, 4, 1 ] )
  p2 = np.array ( [ 4, 1, 3, 0, 2 ] )
  p3 = np.array ( [ 0, 2, 1, 3, 2 ] )

  print ( '' )
  print ( 'perm1_check_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  perm1_check() checks a permutation of 1,...,N.' )

  perm1_print ( n, p1, '  Permutation 1:' )
  check = perm1_check ( n, p1 )
  if ( check ):
    print ( '  This is a permutation.' )
  else:
    print ( '  This is not a permutation.' )

  perm1_print ( n, p2, '  Permutation 2:' )
  check = perm1_check ( n, p2 )
  if ( check ):
    print ( '  This is a permutation.' )
  else:
    print ( '  This is not a permutation.' )

  perm1_print ( n, p3, '  Permutation 3:' )
  check = perm1_check ( n, p3 )
  if ( check ):
    print ( '  This is a permutation.' )
  else:
    print ( '  This is not a permutation.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'perm1_check_test():' )
  print ( '  Normal end of execution.' )
  return

def perm1_enum ( n ):

#*****************************************************************************80
#
## perm1_enum() enumerates the permutations on N digits.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of values being permuted.
#    N must be nonnegative.
#
#  Output:
#
#    integer VALUE, the number of distinct elements.
#
  import numpy as np

  value = np.math.factorial ( n )

  return value

def perm1_enum_test ( ):

#*****************************************************************************80
#
## perm1_enum_test() tests perm1_enum().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'perm1_enum_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  perm1_enum() enumerates the permutations of 1,...,N.' )
  print ( '' )
  print ( '         N      PERM1_enum' )
  print ( '' )

  for n in range ( 1, 11 ):

    value = perm1_enum ( n )

    print ( '  %8d  %12d' % ( n, value ) )   
#
#  Terminate.
#
  print ( '' )
  print ( 'perm1_enum_test():' )
  print ( '  Normal end of execution.' )
  return

def perm1_inverse ( n, p ):

#*****************************************************************************80
#
## perm1_inverse() computes the inverse of a 1-based permutation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
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
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#  Output:
#
#    integer P_INV(N), the inverse permutation.
#
  import numpy as np

  perm1_check ( n, p )

  p_inv = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    p_inv[p[i]-1] = i + 1

  return p_inv

def perm1_inverse_test ( ):

#*****************************************************************************80
#
## perm1_inverse_test() tests perm1_inverse().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7
  p1 = np.array ( [ 4, 3, 5, 1, 7, 6, 2 ] )

  print ( '' )
  print ( 'perm1_inverse_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  perm1_inverse() inverts a permutation of (1,...,N)' )

  perm1_print ( n, p1, '  The original permutation:' )
 
  p2 = perm1_inverse ( n, p1 )
 
  perm1_print ( n, p2, '  The inverted permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'perm1_inverse_test():' )
  print ( '  Normal end of execution.' )
  return

def perm1_is_unicycle ( n, p ):

#*****************************************************************************80
#
## perm1_is_unicycle() is TRUE if a 1-based permutation is a unicycle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects in the permutation.
#
#    integer P(N), the permutation.
#
#  Output:
#
#    bool VALUE, is TRUE if the permutation is a unicycle.
#
  check = perm1_check ( n, p )

  if ( not check ):
    value = False
    return value
#
#  From 1, you must be able to take N-1 steps without reaching 1...
#
  i = 1
  for j in range ( 1, n + 1 ):
    i = p[i-1]
    if ( i == 1 ):
      if ( j < n ):
        value = False
      else:
        value = True
      return value

  value = False

  return value

def perm1_is_unicycle_test ( ):

#*****************************************************************************80
#
## perm1_is_unicycle_test() tests perm1_is_unicycle().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5
  test_num = 10

  print ( '' )
  print ( 'perm1_is_unicycle_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  perm1_is_unicycle() determines whether a 1-based permutation' )
  print ( '  is a unicyle' )

  for test in range ( 0, test_num ):

    p = perm1_random ( n )

    value = perm1_is_unicycle ( n, p )

    if ( value ):

      perm1_print ( n, p, '  This permutation is a unicycle' )
      u = unicycle_index_to_sequence ( n, p )
      unicycle_print ( n, u, '  The permutation in sequence form' )

    else:

      perm1_print ( n, p, '  This permutation is NOT a unicycle' )
#
#  Terminate.
#
  print ( '' )
  print ( 'perm1_is_unicycle_test():' )
  print ( '  Normal end of execution.' )
  return

def perm1_lex_next ( n, p, rank ):

#*****************************************************************************80
#
## perm1_lex_next() computes the lexicographic permutation successor.
#
#  Example:
#
#    RANK  Permutation
#
#       0  1 2 3 4
#       1  1 2 4 3
#       2  1 3 2 4
#       3  1 3 4 2
#       4  1 4 2 3
#       5  1 4 3 2
#       6  2 1 3 4
#       ...
#      23  4 3 2 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
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
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), the input permutation.
#
#    integer RANK, the rank of the input permutation.
#    If RANK = -1, then the input permutation is ignored, and the
#    function returns the first permutation in the ordered list,
#    with RANK = 1.
#
#  Output:
#
#    integer P(N), the successor permutation.  
#    If the input permutation was the last in the ordered list,
#    then the output permutation is the first permutation.
#
#    integer RANK, the rank of the output permutation.
#

#
#  If RANK <= -1, return the first permutation.
#
  if ( rank <= -1 ):
    p = i4vec_indicator1 ( n )
    rank = 0
    return p, rank
#
#  Make sure the input permutation is legal.
#
  check = perm1_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM1_LEX_next - Fatal error!' )
    print ( '  PERM1_check failed.' )
    raise Exception ( 'PERM1_LEX_next - Fatal error!' )
#
#  Seek I, the highest index for which the next element is bigger.
#
  i = n - 2

  while ( True ):

    if ( i < 0 ):
      break

    if ( p[i] <= p[i+1] ):
      break

    i = i - 1
#
#  If no I could be found, then we have reach the final permutation,
#  N, N-1, ..., 2, 1.  Time to start over again.
#
  if ( i == -1 ):
    p = i4vec_indicator1 ( n )
    rank = -1
  else:
#
#  Otherwise, look for the the highest index after I whose element
#  is bigger than I's.  We know that I+1 is one such value, so the
#  loop will never fail.
#
    j = n - 1
    while ( p[j] < p[i] ): 
      j = j - 1
#
#  Interchange elements I and J.
#
    t    = p[i]
    p[i] = p[j]
    p[j] = t
#
#  Reverse the elements from I+1 to N-1.
#
    k_hi = ( n + i ) // 2

    for k in range ( i + 1, k_hi + 1 ):
      l = n + i - k
      t    = p[k]
      p[k] = p[l]
      p[l] = t

    rank = rank + 1

  return p, rank

def perm1_lex_next_test ( ):

#*****************************************************************************80
#
## perm1_lex_next_test() tests perm1_lex_next().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'perm1_lex_next_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  perm1_lex_next() generates 1-based permutations in lexicographic order.' )
  print ( '' )

  more = False
  p = np.zeros ( n, dtype = np.int32 )
  rank = -1

  while ( True ):

    p, rank = perm1_lex_next ( n, p, rank )

    if ( rank == -1 ):
      break

    print ( '  %2d:' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( p[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'perm1_lex_next_test():' )
  print ( '  Normal end of execution.' )
  return

def perm1_lex_rank ( n, p ):

#*****************************************************************************80
#
## perm1_lex_rank() computes the lexicographic rank of a 1-based permutation.
#
#  Discussion:
#
#    The original code altered the input permutation.  
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
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
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#  Output:
#
#    integer RANK, the rank of the permutation.
#
  import numpy as np
#
#  Check.
#
  check = perm1_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM1_LEX_rank - Fatal error!' )
    print ( '  PERM1_check failed!' )
    raise Exception ( 'PERM1_LEX_rank - Fatal error!' )

  rank = 0
  p2 = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    p2[i] = p[i]

  for j in range ( 0, n ):

    rank = rank + ( p2[j] - 1 ) * np.math.factorial ( n - j - 1 )

    for i in range ( j + 1, n ):
      if ( p2[j] < p2[i] ):
        p2[i] = p2[i] - 1

  return rank

def perm1_lex_rank_test ( ):

#*****************************************************************************80
#
## perm1_lex_rank_test() tests perm1_lex_rank().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'perm1_lex_rank_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  perm1_lex_rank() returns the lexicographic rank of' )
  print ( '  a permutation of (1,...,N).' )

  n = 4
  p = np.array ( [ 4, 1, 3, 2 ] )
  perm1_print ( n, p, '  A 1-based permutation:' )
  rank = perm1_lex_rank ( n, p )

  print ( '' )
  print ( '  Rank = %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'perm1_lex_rank_test():' )
  print ( '  Normal end of execution.' )
  return

def perm1_lex_unrank ( n, rank ):

#*****************************************************************************80
#
## perm1_lex_unrank() computes the 1-based permutation of given lexicographic rank.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
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
#    integer N, the number of values being permuted.
#    N must be positive.
#
#    integer RANK, the rank of the permutation.
#
#  Output:
#
#    integer P(N), describes the permutation.
#
  import numpy as np
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'PERM1_LEX_unrank - Fatal error!' )
    print ( '  Input N is illegal.' )
    raise Exception ( 'PERM1_LEX_unrank - Fatal error!' )

  nperm = perm1_enum ( n )

  if ( rank < 0 or nperm < rank ):
    print ( '' )
    print ( 'PERM1_LEX_unrank - Fatal error!' )
    print ( '  The input rank is illegal.' )
    raise Exception ( 'PERM1_LEX_unrank - Fatal error!' )
 
  p = np.zeros ( n, dtype = np.int32 )

  p[n-1] = 1

  for j in range ( 1, n ):

    d = ( rank % np.math.factorial ( j + 1 ) ) // np.math.factorial ( j )
    rank = rank - d * np.math.factorial ( j )
    p[n-j-1] = d + 1

    for i in range ( n - j + 1, n + 1 ):

      if ( d < p[i-1] ):
        p[i-1] = p[i-1] + 1

  return p

def perm1_lex_unrank_test ( ):

#*****************************************************************************80
#
## perm1_lex_unrank_test() tests perm1_lex_unrank().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'perm1_lex_unrank_test():' )
  print ( '  perm1_lex_unrank() returns the 1-based permutation' )
  print ( '  of given lexicographic rank.' )

  n = 4
  n_perm = perm1_enum ( n )

  rank = np.random.random_integers ( 0, n_perm )

  print ( '' )
  print ( '  Rank = %d' % ( rank ) )

  p = perm1_lex_unrank ( n, rank )
  perm1_print ( n, p, '  The corresponding permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'perm1_lex_unrank_test():' )
  print ( '  Normal end of execution.' )
  return

def perm1_print ( n, p, title ):

#*****************************************************************************80
#
## perm1_print() prints a permutation of (1,...,N).
#
#  Example:
#
#    Input:
#
#      P = 7 2 4 1 5 3 6
#
#    Printed output:
#
#      "This is the permutation:"
#
#      1 2 3 4 5 6 7
#      7 2 4 1 5 3 6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects permuted.
#
#    integer P(N), the permutation, in standard index form.
#
#    string TITLE, an optional title.
#    If no title is supplied, then only the permutation is printed.
#
  inc = 20

  if ( len ( title ) != 0 ):

    print ( '' )
    print ( title )

    for ilo in range ( 0, n, inc ):
      ihi = min ( n, ilo + inc )

      print ( '' )
      print ( '  ', end = '' )
      
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( i + 1 ), end = '' )
      print ( '' )

      print ( '  ', end = '' )
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( p[i] ), end = '' )
      print ( '' )

  else:

    for ilo in range ( 0, n, inc ):
      ihi = min ( n, ilo + inc )
      print ( '  ', end = '' )
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( p[i] ), end = '' )
      print ( '' )

  return

def perm1_print_test ( ):

#*****************************************************************************80
#
## perm1_print_test() tests perm1_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'perm1_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  perm1_print() prints a permutation of (1,...,N).' )

  n = 7
  p = np.array ( [ 7, 2, 4, 1, 5, 3, 6 ] )
  perm1_print ( n, p, '  A 1-based permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'perm1_print_test():' )
  print ( '  Normal end of execution.' )
  return

def perm1_random ( n ):

#*****************************************************************************80
#
## perm1_random() selects a random 1-based permutation of N objects.
#
#  Discussion:
#
#    An I4VEC is a vector of I4 values.
#
#    The algorithm is known as the Fisher-Yates or Knuth shuffle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#  Output:
#
#    integer P[N], a permutation of the digits 0 through N-1.
#
  import numpy as np

  p = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    p[i] = i + 1

  for i in range ( 0, n - 1 ):
    j = np.random.random_integers ( i, n - 1 )
    k    = p[i]
    p[i] = p[j]
    p[j] = k

  return p

def perm1_random_test ( ):

#*****************************************************************************80
#
## perm1_random_test() tests perm1_random().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'perm1_random_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  perm1_random() randomly selects a 1-based permutation.' )
  print ( '' )

  for test in range ( 0, 5 ):
    p = perm1_random ( n )
    perm1_print ( n, p, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'perm1_random_test():' )
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

def unicycle_check ( n, p ):

#*****************************************************************************80
#
## unicycle_check() checks that a vector represents a unicycle.
#
#  Discussion:
#
#    A unicycle is a permutation with a single cycle.  This might be called
#    a cyclic permutation, except that that name is used with at least two
#    other meanings.  So, to be clear, a unicycle is a permutation of N
#    objects in which each object is returned to itself precisely after
#    N applications of the permutation.
#
#    This routine verifies that each of the integers from 1
#    to N occurs among the N entries of the permutation.
#
#    Any permutation of the integers 1 to N describes a unicycle.
#    The permutation ( 3, 4, 2, 1 ) indicates that the unicycle
#    sends 3 to 4, 4 to 2, 2 to 1 and 1 to 3.  This is the sequential
#    description of a unicycle.
#
#    The standard sequence "rotates" the permutation so that it begins
#    with 1.  The above sequence becomes a standard sequence when
#    written as ( 1, 3, 4, 2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries.
#
#    integer P(N), the unicycle sequence vector.
#
#  Output:
#
#    bool CHECK, is TRUE if the sequence represents a unicycle.
#
  check = perm1_check ( n, p )

  if ( not check ):
#   print ( '' )
#   print ( 'unicycle_check - Warning!' )
#   print ( '  This is not a permutation!' )
    return check

  check = perm1_is_unicycle ( n, p )

  if ( not check ):
#   print ( '' )
#   print ( 'unicycle_check - Warning!' )
#   print ( '  Permutation is not a unicycle.' )
    return check

  return check

def unicycle_check_test ( ):

#*****************************************************************************80
#
## unicycle_check_test() tests unicycle_check().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  p1 = np.array ( [ 5, 2, 3, 4, 1 ] )
  p2 = np.array ( [ 4, 1, 3, 0, 2 ] )
  p3 = np.array ( [ 4, 2, 1, 3, 2 ] )
  p4 = np.array ( [ 2, 1, 4, 3, 5 ] )
  p5 = np.array ( [ 3, 4, 5, 1, 2 ] )

  print ( '' )
  print ( 'unicycle_check_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_check checks a unicycle.' )

  unicycle_print ( n, p1, '  Candidate 1:' )
  check = unicycle_check ( n, p1 )
  if ( check ):
    print ( '  This is a unicycle!' )
  else:
    print ( '  This is not a unicycle.' )

  unicycle_print ( n, p2, '  Candidate 2:' )
  check = unicycle_check ( n, p2 )
  if ( check ):
    print ( '  This is a unicycle!' )
  else:
    print ( '  This is not a unicycle.' )

  unicycle_print ( n, p3, '  Candidate 3:' )
  check = unicycle_check ( n, p3 )
  if ( check ):
    print ( '  This is a unicycle!' )
  else:
    print ( '  This is not a unicycle.' )

  unicycle_print ( n, p4, '  Candidate 4:' )
  check = unicycle_check ( n, p4 )
  if ( check ):
    print ( '  This is a unicycle!' )
  else:
    print ( '  This is not a unicycle.' )

  unicycle_print ( n, p5, '  Candidate 5:' )
  check = unicycle_check ( n, p5 )
  if ( check ):
    print ( '  This is a unicycle!' )
  else:
    print ( '  This is not a unicycle.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_check_test:' )
  print ( '  Normal end of execution.' )
  return

def unicycle_enum ( n ):

#*****************************************************************************80
#
## unicycle_enum() enumerates the unicycles.
#
#  Discussion:
#
#    Each standard sequence corresponds to a unique unicycle.  Since the
#    first element of a standard sequence is always 1, the number of standard
#    sequences, and hence the number of unicycles, is (n-1)!.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the unicyle.
#
#  Output:
#
#    integer VALUE, the number of unicycles.
#
  import numpy as np

  if ( n < 1 ):
    value = 0
  else:
    value = np.math.factorial ( n - 1 )

  return value

def unicycle_enum_test ( ):

#*****************************************************************************80
#
## unicycle_enum_test() tests unicycle_enum().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n_max = 10

  print ( '' )
  print ( 'unicycle_enum_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_enum enumerates the unicycles of N objects.' )
  print ( '' )
  print ( '  N    Number' )
  print ( '' )

  for n in range ( 0, n_max + 1 ):

    num = unicycle_enum ( n )
    print ( '  %3d  %8d' % ( n, num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_enum_test' )
  print ( '  Normal end of execution.' )
  return

def unicycle_index ( n, u ):

#*****************************************************************************80
#
## unicycle_index() returns the index form of a unicycle.
#
#  Example:
#
#    N = 4
#
#    U       = 1 3 4 2
#    U_index = 3 1 4 2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the unicycles.
#
#    integer U(N), the unicycle sequence vector.
#
#  Output:
#
#    integer U_index(N), the unicycle index vector.
#
  import numpy as np

  u_index = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    ip1 = i4_wrap ( i + 1, 0, n - 1 )
    u_index[u[i]-1] = u[ip1]

  return u_index

def unicycle_index_test ( ):

#*****************************************************************************80
#
## unicycle_index_test() tests unicycle_index().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 6
  test_num = 5

  print ( '' )
  print ( 'unicycle_index_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_index converts a unicycle to index form.' )

  for test in range ( 0, 5 ):

    u = unicycle_random ( n )

    unicycle_print ( n, u, '  The unicycle:' )

    u_index = unicycle_index ( n, u )
    
    unicycle_index_print ( n, u_index, '  The index form:' )

    u2 = unicycle_index_to_sequence ( n, u_index )

    unicycle_print ( n, u2, '  The unicycle recovered:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_index_test' )
  print ( '  unicycle_index converts a unicycle to index form.' )
  return

def unicycle_index_print ( n, u_index, title ):

#*****************************************************************************80
#
## unicycle_index_print() prints a unicycle given in index form.
#
#  Example:
#
#    Input:
#
#      U_index = 7 1 4 5 2 3 6
#
#    Printed output:
#
#      1 2 3 4 5 6 7
#      7 1 4 5 2 3 6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the unicycle.
#
#    integer U_index(N), the unicycle index vector.
#
#    string TITLE, a title.
#
  inc = 20

  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  for ilo in range ( 1, n, inc ):
    ihi = min ( n, ilo + inc - 1 )
    print ( '' )
    print ( '  ', end = '' )
    for i in range ( ilo, ihi + 1 ):
      print ( '%4d' % ( i ), end = '' )
    print ( '' )
    print ( '  ', end = '' )
    for i in range ( ilo, ihi + 1 ):
      print ( '%4d' % ( u_index[i-1] ), end = '' )
    print ( '' )

  return

def unicycle_index_print_test ( ):

#*****************************************************************************80
#
## unicycle_index_print_test() tests unicycle_index_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7

  print ( '' )
  print ( 'unicycle_index_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_index_print prints a unicyle given in index form;' )
  print ( '' )

  u_index = np.array ( [ 7, 1, 4, 5, 2, 3, 6 ] )

  unicycle_index_print ( n, u_index, '  The unicycle in index form:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_index_print_test' )
  print ( '  Normal end of execution.' )
  return

def unicycle_index_to_sequence ( n, u_index ):

#*****************************************************************************80
#
## unicycle_index_to_sequence() converts a unicycle from index to sequence form.
#
#  Example:
#
#    N = 4
#
#    U_index = 3 1 4 2
#    U       = 1 3 4 2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the unicycles.
#
#    integer U_index(N), the unicycle index vector.
#
#  Output:
#
#    integer U(N), the unicycle sequence vector.
#
  import numpy as np

  u = np.zeros ( n, dtype = np.int32 )

  u[0] = 1
  i = 1

  for j in range ( 1, n ):

    i = u_index[i-1]
    u[j] = i

    if ( i == 1 ):
      print ( '' )
      print ( 'unicycle_index_to_sequence - Fatal error!' )
      print ( '  The index vector does not represent a unicycle.' )
      print ( '  On step %d, u_index(%d) = 1.' % ( j, i ) )
      raise Exception ( 'unicycle_index_to_sequence - Fatal error!' )

  return u

def unicycle_index_to_sequence_test ( ):

#*****************************************************************************80
#
## unicycle_index_to_sequence_test() tests unicycle_index_to_sequence().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 6
 
  print ( '' )
  print ( 'unicycle_index_to_sequence_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_index_to_sequence converts an index to unicycle form.' )

  for test in range ( 0, 5 ):

    u = unicycle_random ( n )

    unicycle_print ( n, u, '  The unicycle:' )

    u_index = unicycle_index ( n, u )
    
    unicycle_index_print ( n, u_index, '  The index form:' )

    u2 = unicycle_index_to_sequence ( n, u_index )

    unicycle_print ( n, u2, '  The unicycle recovered:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_index_to_sequence_test' )
  print ( '  Normal end of execution.' )
  return

def unicycle_inverse ( n, u ):

#*****************************************************************************80
#
## unicycle_inverse() returns the inverse of a unicycle.
#
#  Example:
#
#    N = 4
#
#    U         = 1 3 4 2
#    U_inverse = 1 2 4 3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the unicycles.
#
#    integer U(N), the unicycle sequence vector.
#
#  Output:
#
#    integer U_inverse(N), the inverse unicycle.
#
  import numpy as np

  u_inverse = np.zeros ( n, dtype = np.int32 )

  u_inverse[0] = 1
  for i in range ( 1, n ):
    u_inverse[i] = u[n-i]

  return u_inverse

def unicycle_inverse_test ( ):

#*****************************************************************************80
#
## unicycle_inverse_test() tests unicycle_inverse().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7
  u = np.array ( [ 1, 7, 6, 2, 4, 3, 5 ] )

  print ( '' )
  print ( 'unicycle_inverse_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_inverse inverts a unicycle' )

  unicycle_print ( n, u, '  The original unicycle:' )
 
  u_inverse = unicycle_inverse ( n, u )

  unicycle_print ( n, u_inverse, '  The inverse unicycle:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_inverse_test' )
  print ( '  Normal end of execution.' )
  return

def unicycle_next ( n, u, rank ):

#*****************************************************************************80
#
## unicycle_next() generates unicycles in lexical order, one at a time.
#
#  Example:
#
#    N = 4
#
#    1   1 2 3 4
#    2   1 2 4 3
#    3   1 3 2 4
#    4   1 3 4 2
#    5   1 4 2 3
#    6   1 4 3 2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the unicycles.
#
#    integer U(N); on first call with MORE = FALSE,
#    this value is not used.  Otherwise, the input value is the previous
#    unicycle.
#
#    integer RANK, the rank.
#    If RANK = -1 on then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    integer U(N); the next unicycle.
#
#    integer RANK, the rank.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was in which
#    case the output value of RANK is -1.
#
  import numpy as np

  p = np.zeros ( n - 1, dtype = np.int32 )

  if ( rank == -1 ):
    u[0] = 1
  else:
    for i in range ( 0, n - 1 ):
      p[i] = u[i+1] - 1

  p, rank = perm1_lex_next ( n - 1, p, rank )

  for i in range ( 0, n - 1 ):
    u[i+1] = p[i] + 1

  return u, rank

def unicycle_next_test ( ):

#*****************************************************************************80
#
## unicycle_next_test() tests unicycle_next().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'unicycle_next_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_next generates unicycles in lex order.' )
  print ( '' )

  rank = -1
  u = np.zeros ( n, dtype = np.int32 )

  while ( True ):

    u, rank = unicycle_next ( n, u, rank )

    if ( rank == - 1 ):
      break

    print ( '  %3d:  ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '%2d' % ( u[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_next_test' )
  print ( '  Normal end of execution.' )
  return

def unicycle_print ( n, u, title ):

#*****************************************************************************80
#
## unicycle_print() prints a unicycle given in sequence form.
#
#  Example:
#
#    Input:
#
#      U = 7 1 4 5 2 3 6
#
#    Printed output:
#
#      7 1 4 5 2 3 6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the unicycle.
#
#    integer U(N), the unicycle sequence vector.
#
#    string TITLE, a title.
#
  inc = 20

  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
    print ( '' )

  for ilo in range ( 0, n, inc ):
    ihi = min ( n, ilo + inc )
    for i in range ( ilo, ihi ):
      print ( '  %4d' % ( u[i] ), end = '' )
    print ( '' )

  return

def unicycle_print_test ( ):

#*****************************************************************************80
#
## unicycle_print_test() tests unicycle_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'unicycle_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_print prints a unicyle;' )

  u = unicycle_random ( n )

  unicycle_print ( n, u, '  The unicycle:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_print_test' )
  print ( '  Normal end of execution.' )
  return

def unicycle_random ( n ):

#*****************************************************************************80
#
## unicycle_random() selects a random unicycle of N objects.
#
#  Discussion:
#
#    The routine assumes the objects are labeled 1, 2, ... N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms for Computers and Calculators,
#    Second Edition,
#    Academic Press, 1978,
#    ISBN: 0-12-519260-6,
#    LC: QA164.N54.
#
#  Input:
#
#    integer N, the number of objects to be permuted.
#
#  Output:
#
#    integer U(N), a unicycle in sequence form.
#
  import numpy as np

  u = i4vec_indicator1 ( n )

  for i in range ( 1, n ):
    j = np.random.random_integers ( i, n - 1 )
    t    = u[i]
    u[i] = u[j]
    u[j] = t

  return u

def unicycle_random_test ( ):

#*****************************************************************************80
#
## unicycle_random_test() tests unicycle_random().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'unicycle_random_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_random produces a random unicyle;' )
  print ( '  For this test, N = %d' % ( n ) )
  print ( '' )

  for i in range ( 0, 5 ):
    u = unicycle_random ( n )
    unicycle_print ( n, u, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_random_test' )
  print ( '  Normal end of execution.' )
  return

def unicycle_rank ( n, u ):

#*****************************************************************************80
#
## unicycle_rank() computes the rank of a unicycle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the order of the unicycle.
#
#    integer U(N), a unicycle in sequence form.
#
#  Output:
#
#    integer RANK, the rank of the unicycle.
#
  import numpy as np

  p = np.zeros ( n - 1, dtype = np.int32 )

  for i in range ( 0, n - 1 ):
    p[i] = u[i+1] - 1

  rank = perm1_lex_rank ( n - 1, p )

  return rank

def unicycle_rank_test ( ):

#*****************************************************************************80
#
## unicycle_rank_test() tests unicycle_rank().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  u = np.array ( [ 1, 5, 2, 3, 4 ] )

  print ( '' )
  print ( 'unicycle_rank_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_rank ranks a unicycle.' )

  unicycle_print ( n, u, '  The unicycle:' )
 
  rank = unicycle_rank ( n, u )
 
  print ( '' )
  print ( '  The rank is: %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_rank_test' )
  print ( '  Normal end of execution.' )
  return

def unicycle_unrank ( n, rank ):

#*****************************************************************************80
#
## unicycle_unrank() "unranks" a unicycle.
#
#  Discussion:
#
#    That is, given a rank, it computes the corresponding unicycle.
#
#    The value of the rank should be between 0 and (N-1)#-1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Input:
#
#    integer N, the number of elements in the set.
#
#    integer RANK, the desired rank of the permutation.
#
#  Output:
#
#    integer U(N), the unicycle.
#
  import numpy as np

  p = perm1_lex_unrank ( n - 1, rank )

  u = np.zeros ( n, dtype = np.int32 )

  u[0] = 1
  for i in range ( 1, n ):
    u[i] = p[i-1] + 1

  return u

def unicycle_unrank_test ( ):

#*****************************************************************************80
#
## unicycle_unrank_test() tests unicycle_unrank().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'unicycle_unrank_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  unicycle_unrank, given a rank, computes the' )
  print ( '  corresponding unicycle.' )
  print ( '' )

  rank = 6
  print ( '  The requested rank is %d' % ( rank ) )
 
  u = unicycle_unrank ( n, rank )
 
  unicycle_print ( n, u, '  The unicycle:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_unrank_test' )
  print ( '  Normal end of execution.' )
  return

def unicycle_test ( ):

#*****************************************************************************80
#
## unicycle_test() tests unicycle().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'unicycle_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test unicycle().' )

  i4_modp_test ( )
  i4_wrap_test ( )

  i4vec_indicator1_test ( )
  i4vec_print_test ( )
  i4vec_reverse_test ( )

  perm1_check_test ( )
  perm1_enum_test ( )
  perm1_inverse_test ( )
  perm1_lex_next_test ( )
  perm1_lex_rank_test ( )
  perm1_lex_unrank_test ( )
  perm1_print_test ( )
  perm1_random_test ( )

  perm1_is_unicycle_test ( )
  unicycle_check_test ( )
  unicycle_enum_test ( )
  unicycle_index_test ( )
  unicycle_index_print_test ( )
  unicycle_index_to_sequence_test ( )
  unicycle_inverse_test ( )
  unicycle_next_test ( )
  unicycle_random_test ( )
  unicycle_rank_test ( )
  unicycle_unrank_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'unicycle_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  unicycle_test ( )
  timestamp ( )
 
