#! /usr/bin/env python3
#
def laplace_matrix ( ):

#*****************************************************************************80
#
## laplace_matrix() analyzes a matrix sampled from the Laplace distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 February 2017
#
#  Author:
#
#    Original code by John D Cook.
#    Modifications by John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Heavy-tailed random matrices,
#    https://www.johndcook.com/blog/
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  N = 5000

  print ( '' )
  print ( 'LAPLACE_MATRIX' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Examine eigenvalue distribution of %dx%d matrix' % ( N, N ) )
  print ( '  with entries from Laplace distribution.' )

  A = np.random.laplace(0, np.sqrt(0.5), (N, N))
  for i in range ( 0, N ):
    A[i,0:i] = A[0:i,i]
  eigenvalues = np.linalg.eigvalsh(A) 

  print ( '' )
  print ( '  Eigenvalue range: [%g, %g]' % ( min(eigenvalues), max(eigenvalues) ) )

  plt.hist ( eigenvalues, bins = 70 )
  plt.title ( 'Laplace matrix' )
  filename = 'laplace_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename , '".' )
  plt.show ( block = False )
  plt.close ( )

  return

def normal_matrix ( ):

#*****************************************************************************80
#
## NORMAL_MATRIX analyzes a matrix sampled from the normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 February 2017
#
#  Author:
#
#    Original code by John D Cook.
#    Modifications by John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Heavy-tailed random matrices,
#    https://www.johndcook.com/blog/
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  N = 5000

  print ( '' )
  print ( 'NORMAL_MATRIX' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Examine eigenvalue distribution of %dx%d matrix' % ( N, N ) )
  print ( '  with entries from normal distribution.' )

  A = np.random.normal(0, 1, (N, N))    
  for i in range ( 0, N ):
    A[i,0:i] = A[0:i,i]
  eigenvalues = np.linalg.eigvalsh(A) 

  print ( '' )
  print ( '  Eigenvalue range: [%g, %g]' % ( min(eigenvalues), max(eigenvalues) ) )

  plt.hist ( eigenvalues, bins = 70 )
  plt.title ( 'Normal matrix' )
  filename = 'normal_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename , '".' )
  plt.show ( block = False )
  plt.close ( )

  return

def random_matrix_eigenvalues_test ( ):

#*****************************************************************************80
#
## random_matrix_eigenvalues_test tests random_matrix_eigenvalues().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 March 2021
#
#  Author:
#
#    John Burkardt.
#
  import platform

  print ( '' )
  print ( 'random_matrix_eigenvalues_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test random_matrix_eigenvalues()' )

  laplace_matrix ( )
  normal_matrix ( )
  student_matrix ( )
  uniform_matrix ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'random_matrix_eigenvalues_test:' )
  print ( '  Normal end of execution.' )
  return

def student_matrix ( ):

#*****************************************************************************80
#
## STUDENT_MATRIX analyzes a matrix sampled from the Student T distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 February 2017
#
#  Author:
#
#    Original code by John D Cook.
#    Modifications by John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Heavy-tailed random matrices,
#    https://www.johndcook.com/blog/
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  N = 5000

  print ( '' )
  print ( 'STUDENT_MATRIX' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Examine eigenvalue distribution of %dx%d matrix' % ( N, N ) )
  print ( '  with entries from the Student t distribution.' )

  A = np.random.standard_t(1.8, (N, N))
  for i in range ( 0, N ):
    A[i,0:i] = A[0:i,i]
  eigenvalues = np.linalg.eigvalsh(A) 

  print ( '' )
  print ( '  Eigenvalue range: [%g, %g]' % ( min(eigenvalues), max(eigenvalues) ) )

  plt.hist ( eigenvalues, bins = 70 )
  plt.title ( 'Student t matrix' )
  filename = 'student_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename , '".' )
  plt.show ( block = False )
  plt.close ( )

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

def uniform_matrix ( ):

#*****************************************************************************80
#
## UNIFORM_MATRIX analyzes a matrix sampled from the uniform distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 February 2017
#
#  Author:
#
#    Original code by John D Cook.
#    Modifications by John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Heavy-tailed random matrices,
#    https://www.johndcook.com/blog/
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  N = 5000

  print ( '' )
  print ( 'UNIFORM_MATRIX' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Examine eigenvalue distribution of %dx%d matrix' % ( N, N ) )
  print ( '  with entries from uniform distribution.' )

  A = np.random.random ( [ N, N ] )
  for i in range ( 0, N ):
    A[i,0:i] = A[0:i,i]
  eigenvalues = np.linalg.eigvalsh(A) 
  print ( '' )
  print ( '  Eigenvalue range: [%g, %g]' % ( min(eigenvalues), max(eigenvalues) ) )

  plt.hist ( eigenvalues, bins = 70 )
  plt.title ( 'Uniform matrix' )
  filename = 'uniform_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "', filename , '".' )
  plt.show ( block = False )
  plt.close ( )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  random_matrix_eigenvalues_test ( )
  timestamp ( )

