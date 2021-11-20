#! /usr/bin/env python3
#
def args_test ( ):

#*****************************************************************************80
#
## args_test() tests the sys.argv function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 March 2021
#
#  Author:
#
#    John Burkardt
#
  import platform
  import sys

  print ( '' )
  print ( 'args_test():' )
  print ( '  Python version %s' % ( platform.python_version ( )  ))
  print ( '  Count and print the arguments.' )
  print ( '' )
  print ( '  The number of arguments was ' + repr ( len ( sys.argv ) ) + '.' )
  print ( '' )
  print ( '  Arg[0] = the program name = ' + sys.argv[0] + '' )

  i = 1

  while 1 < len ( sys.argv ):
    print ( '  Arg[' + repr ( i ) + '] = ' + sys.argv[1] + '' )
    del sys.argv[1]
    i = i + 1

  function_args_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'args_test():' )
  print ( '  Normal end of execution.' )

  return

def function_args ( *args ):

#*****************************************************************************80
#
## function_args() accepts and prints an arbitrary number of arguments.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    *ARGS, an arbitrary number of arguments.
#
  print ( '' )
  print ( 'function_args():' )
  print ( '  Number of arguments on this call was %d' % ( len ( args ) ) )
  print ( '' )

  for count, thing in enumerate ( args ):
    print ( '  {0}. {1}'.format ( count, thing ) )

  return

def function_args_test ( ):

#*****************************************************************************80
#
## function_args_test() tests function_args().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'function_args_test():' )
  print ( '  function_args() demonstrates how to count and print function arguments' )
  print ( '  when the number of arguments may vary.' )

  function_args ( )
  function_args ( 1.1, - 2.2, 3.3 )
  function_args ( 1, 'two', 3.3, ( 4, 5 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'function_args_test():' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  args_test ( )
  timestamp ( )

