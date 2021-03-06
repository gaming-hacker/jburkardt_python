#! /usr/bin/env python3
#
def clock_test ( ) :

#*****************************************************************************80
#
## clock_test() tests clock() to time the numpy.random.random_sample() function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from time import clock

  n_log_min = 10
  n_log_max = 22
  n_min = 2 ** n_log_min
  n_max = 2 ** n_log_max
  n_rep = 5
  n_test = 1

  print ( '' )
  print ( 'clock_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  clock() times the RANDOM_SAMPLE function:' )
  print ( '' )
  print ( '    x = numpy.random.random_sample ( ( n, 1 ) );' )
  print ( '' )
  print ( '  Data vectors will be of minimum size %d' % ( n_min ) )
  print ( '  Data vectors will be of maximum size %d' % ( n_max ) )
  print ( '  Number of repetitions of the operation: %d' % ( n_rep ) )
  print ( '' )
  print ( '  Timing results in seconds:' )
  print ( '' )
  print ( '      Size         Rep #1         Rep #2         Rep #3        ' ),
  print ( 'Rep #4         Rep #5' )
  print ( '' )

  for n_log in range ( n_log_min, n_log_max + 1 ):

    n = 2 ** ( n_log )

    print ( '  %8d' % ( n ) ),

    for i_rep in range ( 0, n_rep ):

      seconds = clock ( )

      x = np.random.random_sample ( ( n, 1 ) );

      seconds = clock ( ) - seconds

      print ( '  %12f' % ( seconds ) ),

    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'clock_test:' )
  print ( '  Normal end of execution.' )
  return

def time_test ( ) :

#*****************************************************************************80
#
## time_test() tests time() to time the numpy.random.random_sample() function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from time import time

  n_log_min = 10
  n_log_max = 22
  n_min = 2 ** n_log_min
  n_max = 2 ** n_log_max
  n_rep = 5
  n_test = 1

  print ( '' )
  print ( 'time_test()' )
  print ( '  time() times the RANDOM_SAMPLE function:' )
  print ( '' )
  print ( '    x = numpy.random.random_sample ( ( n, 1 ) );' )
  print ( '' )
  print ( '  Data vectors will be of minimum size %d' % ( n_min ) )
  print ( '  Data vectors will be of maximum size %d' % ( n_max ) )
  print ( '  Number of repetitions of the operation: %d' % ( n_rep ) )
  print ( '' )
  print ( '  Timing results in seconds:' )
  print ( '' )
  print ( '      Size         Rep #1         Rep #2         Rep #3        ' ),
  print ( 'Rep #4         Rep #5' )
  print ( '' )

  for n_log in range ( n_log_min, n_log_max + 1 ):

    n = 2 ** ( n_log )

    print ( '  %8d' % ( n ) ),

    for i_rep in range ( 0, n_rep ):

      seconds = time ( )

      x = np.random.random_sample ( ( n, 1 ) );

      seconds = time ( ) - seconds

      print ( '  %12f' % ( seconds ) ),

    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'time_test():' )
  print ( '  Normal end of execution.' )
  return

def timer_test ( ):

#*****************************************************************************80
#
## timer_test() tests timer().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'timer_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test timers.' )

  clock_test ( )
  time_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'timer_test():' )
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
  timer_test ( )
  timestamp ( )

