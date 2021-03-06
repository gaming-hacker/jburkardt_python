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

def sort_rc_test ( ):

#*****************************************************************************80
#
## sort_rc_test() tests tests sort_rc().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sort_rc_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test sort_rc().' )

  sort_safe_rc_i4vec_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sort_rc_test():' )
  print ( '  Normal end of execution.' )
  return

def sort_safe_rc ( n, indx, isgn, i_save, j_save, k_save, l_save, n_save ):

#*****************************************************************************80
#
## sort_safe_rc() externally sorts a list of items into ascending order.
#
#  Discussion:
#
#    This is a version of test() tests which does not rely on
#    storing certain work variables internally to the function.  This makes
#    the function somewhat more awkward to call, but easier to program
#    in a variety of languages, and safe to use in a parallel programming
#    environment, or in cases where the sorting of several vectors is to
#    be carried out at more or less the same time.
#
#    The actual list of data is not passed to the routine.  Hence this
#    routine may be used to sort integers, reals, numbers, names,
#    dates, shoe sizes, and so on.  After each call, the routine asks
#    the user to compare or interchange two items, until a special
#    return value signals that the sorting is completed.
#
#  Example:
#
#    n = 100
#    indx = 0
#    isgn = 0
#    i_save = 0
#    j_save = 0
#    k_save = 0
#    l_save = 0
#    n_save = 0
#
#    while ( 1 )
#
#      indx, i, j, i_save, j_save, k_save, l_save, n_save = 
#        sort_safe_rc ( n, indx, isgn, i_save, j_save, k_save, l_save, n_save )
#
#      if ( indx < 0 )
#
#        isgn = 1
#        if ( a(i) <= a(j) )
#          isgn = -1
#        end
#
#      elseif ( 0 < indx )
#
#        k    = a(i)
#        a(i) = a(j)
#        a(j) = k
#
#      else
#
#        break
#
#      end
#
#    end
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    Original FORTRAN77 version by Albert Nijenhuis, Herbert Wilf.
#    MATLAB version by John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf.
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the number of items to be sorted.
#
#    integer INDX, the main communication signal.
#    The user must set INDX to 0 before the first call.
#    Thereafter, the user should set the input value of INDX
#    to the output value from the previous call.
#
#    integer ISGN, results of comparison of elements I and J.
#    (Used only when the previous call returned INDX less than 0).
#    ISGN <= 0 means I is less than or equal to J
#    0 <= ISGN means I is greater than or equal to J.
#
#    integer I_SAVE, J_SAVE, K_SAVE, L_SAVE, N_SAVE, workspace 
#    needed by the routine.  Before calling the function,
#    the user should declare variables to hold these values, but should
#    not change them, and need not ever examine them.
#
#  Output:
#
#    integer INDX, the main communication signal.
#    If INDX is
#    * greater than 0, the user should:
#      interchange items I and J
#      call again.
#    * less than 0, the user should:
#      compare items I and J
#      set ISGN = -1 if I < J, ISGN = +1 if J < I
#      call again.
#    * equal to 0, the sorting is done.
#
#    integer I, J, the indices of two items.
#    On return with INDX positive, elements I and J should be interchanged.
#    On return with INDX negative, elements I and J should be compared, and
#    the result reported in ISGN on the next call.
#
#    integer I_SAVE, J_SAVE, K_SAVE, L_SAVE, N_SAVE, workspace 
#    needed by the routine.  Before calling the function,
#    the user should declare variables to hold these values, but should
#    not change them, and need not ever examine them.
#

#
#  INDX = 0: This is the first call.
#
  if ( indx == 0 ):
      
    k_save = ( n // 2 )
    l_save = k_save
    n_save = n
#
#  INDX < 0: The user is returning the results of a comparison.
#
  elif ( indx < 0 ):

    if ( indx == -2 ):

      if ( isgn < 0 ):
        i_save = i_save + 1

      j_save = l_save
      l_save = i_save
      indx = -1
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save
 
    if ( 0 < isgn ):
      indx = 2
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save

    if ( k_save <= 1 ):

      if ( n_save == 1 ):
        i_save = 0
        j_save = 0
        indx = 0
      else:
        i_save = n_save
        n_save = n_save - 1
        j_save = 1
        indx = 1

      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save

    k_save = k_save - 1
    l_save = k_save
#
#  0 < INDX, the user was asked to make an interchange.
#
  elif ( indx == 1 ):

    l_save = k_save

  while ( True ):

    i_save = 2 * l_save

    if ( i_save == n_save ):
      j_save = l_save
      l_save = i_save
      indx = -1
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save
    elif ( i_save <= n_save ):
      j_save = i_save + 1
      indx = -2
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save

    if ( k_save <= 1 ):
      break

    k_save = k_save - 1
    l_save = k_save

  if ( n_save == 1 ):
    i_save = 0
    j_save = 0
    indx = 0
    i = i_save
    j = j_save
  else:
    i_save = n_save
    n_save = n_save - 1
    j_save = 1
    indx = 1
    i = i_save
    j = j_save

  return indx, i, j, i_save, j_save, k_save, l_save, n_save

def sort_safe_rc_i4vec_test ( ):

#*****************************************************************************80
#
## sort_safe_rc_i4vec_test() tests sort_safe_rc() on an integer vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 20

  print ( '' )
  print ( 'sort_safe_rc_i4vec_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  sort_save_rc() sorts objects externally.' )
  print ( '  This function does not use persistent memory.' )
#
#  Generate some data to sort.
#
  i4_lo = 1
  i4_hi = n
  a = np.random.random_integers ( i4_lo, i4_hi, size = n )
 
  i4vec_print ( n, a, '  Unsorted array:' )
#
#  Sort the data.
#
  indx = 0
  isgn = 0
  i_save = 0
  j_save = 0
  k_save = 0
  l_save = 0
  n_save = 0

  while ( True ):

    indx, i, j, i_save, j_save, k_save, l_save, n_save = \
      sort_safe_rc ( n, indx, isgn, i_save, j_save, k_save, l_save, n_save )
 
    if ( indx < 0 ):
      isgn = 1
      if ( a[i-1] <= a[j-1] ):
        isgn = -1
    elif ( 0 < indx ):
      k      = a[i-1]
      a[i-1] = a[j-1]
      a[j-1] = k
    else:
      break
#
#  Display the sorted data.
#
  i4vec_print ( n, a, '  Sorted array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'sort_save_rc_i4vec_test:' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  sort_rc_test ( )
  timestamp ( )

