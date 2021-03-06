#! /usr/bin/env python3
#
def hdf5_test01 ( ):

#*****************************************************************************80
#
## hdf5_test01() tests HDF5 by creating a writeable file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 February 2017
#
#  Author:
#
#    John Burkardt
#
  import h5py

  print ( '' )
  print ( 'hdf5_test01:' )
  print ( '  Python version' )
  print ( '  Create a writeable file "test01.h5".' )
#
#  Get the file id.
#
  file_name = 'test01.h5'
  file_id = h5py.File ( file_name, 'w' )
#
#  Close the file.
#
  file_id.close ( )

  return

def hdf5_test02 ( ):

#*****************************************************************************80
#
## hdf5_test02() creates a dataset.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 February 2017
#
#  Author:
#
#    John Burkardt
#
  import h5py
  import numpy as np

  print ( '' )
  print ( 'hdf5_test02:' )
  print ( '  Python version' )
  print ( '  Create a file "test02.h5" containing a dataset.' )
#
#  Get the file id.
#
  file_name = 'test02.h5'
  file_id = h5py.File ( file_name, 'w' )
#
#  Create the dataset
#
  dset_name = 'dset02'
  dset_dims = np.array ( [ 4, 6 ] )
  dataset = file_id.create_dataset ( dset_name, dset_dims, h5py.h5t.STD_I32BE )

  return

def hdf5_test03 ( ):

#*****************************************************************************80
#
## hdf5_test03() creates a dataset and actually puts data into it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 February 2017
#
#  Author:
#
#    John Burkardt
#
  import h5py
  import numpy as np

  print ( '' )
  print ( 'hdf5_test03:' )
  print ( '  Python version' )
  print ( '  Create a file "test03.h5" containing a dataset' )
  print ( '  and store data in the dataset.' )
#
#  Get the file id.
#
  file_name = 'test03.h5'
  file_id = h5py.File ( file_name, 'w' )
#
#  Get the data set id.
#
  dset_name = 'dset03'
  dset_dims = np.array ( [ 4, 6 ] )
  dset_id = file_id.create_dataset ( dset_name, dset_dims, h5py.h5t.STD_I32BE )
#
#  Create the data.
#
  dset_data = np.zeros ( [ 4, 6 ] )

  print ( '' )
  print ( '  Dataset written to file "test03.h5":' )
  print ( '' )
  for i in range ( 0, 4 ):
    for j in range ( 0, 6 ):
      dset_data[i,j] = i * 6 + j + 1
      print ( '  dset_data[%d,%d] = %d' % ( i, j, dset_data[i,j] ) )
#
#  Write data to the dataset.
#
  dset_id[...] = dset_data

  return

def hdf5_test04 ( ):

#*****************************************************************************80
#
## hdf5_test04() reads data from a dataset.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 February 2017
#
#  Author:
#
#    John Burkardt
#
  import h5py
  import numpy as np

  print ( '' )
  print ( 'hdf5_test04:' )
  print ( '  Python version' )
  print ( '  Open the file "test03.h5";' )
  print ( '  Open a dataset' )
  print ( '  read data from the dataset.' )
#
#  Get the file id.
#
  file_name = 'test03.h5'
  file_id = h5py.File ( file_name, 'r' )
#
#  Get the data set data.
#
  dset_name = 'dset03'
  dset_data = file_id [ dset_name ]
#
#  Print the data.
#
  print ( '' )
  print ( '  Dataset read from file "test03.h5":' )
  print ( '' )
  for i in range ( 0, 4 ):
    for j in range ( 0, 6 ):
      print ( '  dset_data[%d,%d] = %d' % ( i, j, dset_data[i,j] ) )

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

def hdf5_test ( ):

#*****************************************************************************80
#
## hdf5_test() tests hdf5().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 February 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hdf5_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test hdf5().' )

  hdf5_test01 ( )
  hdf5_test02 ( )
  hdf5_test03 ( )
  hdf5_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hdf5_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  hdf5_test ( )
  timestamp ( )
