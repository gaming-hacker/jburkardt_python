#! /usr/bin/env python3
#
def file_column_count ( filename ):

#*****************************************************************************80
#
## file_column_count() counts the number of words in a typical column of a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file.
#
#  Output:
#
#    integer COLUMN_COUNT, the number of words in a typical column.
#
  column_count = -1

  input = open ( filename, 'r' )

  column_count = 0

  for line in input:

    if ( line[0] == '#' ):
      continue
    else:

      wc = 0
      for word in line.strip().split():
         wc = wc + 1

      if ( wc == 0 ):
        continue
      elif ( column_count == 0 ):
        column_count = wc
        break

  input.close ( )

  return column_count

def file_column_count_test ( ):

#*****************************************************************************80
#
## file_column_count_test() tests file_column_count().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'file_column_count_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Count the number of columns in a typical text file line.' )

  filename = 'r8mat_write_test.txt'
  column_count = file_column_count ( filename )

  print ( '' )
  print ( '  Number of columns in "%s" is %d' % ( filename, column_count ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'file_column_count_test:' )
  print ( '  Normal end of execution.' )
  return

def file_row_count ( filename ):

#*****************************************************************************80
#
## file_row_count() counts the number of rows (lines) in a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file.
#
#  Output:
#
#    integer ROW_COUNT, the number of rows in the file.
#
  row_count = -1

  input = open ( filename, 'r' )

  row_count = 0

  for line in input:

    if ( line[0] == '#' ):
      continue
    else:

      wc = 0
      for word in line.strip().split():
         wc = wc + 1

      if ( wc == 0 ):
        continue
      else:
        row_count = row_count + 1

  input.close ( )

  return row_count

def file_row_count_test ( ):

#*****************************************************************************80
#
## file_row_count_test() tests file_row_count().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'file_row_count_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Count the number of rows in a text file.' )

  filename = 'i4mat_write_test.txt'
  row_count = file_row_count ( filename )

  print ( '' )
  print ( '  Number of rows in "%s" is %d' % ( filename, row_count ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'file_row_count_test:' )
  print ( '  Normal end of execution.' )
  return

def florida_centroid_geo ( g_lon, g_lat, sample_num ):

#*****************************************************************************80
#
## florida_centroid_geo() estimates geometric centroids of Voronoi regions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Input:
#
#    real G_LON(*), G_LAT(*), the longitude and latitude 
#    of generators to be displayed on a map of Florida.
#
#    integer SAMPLE_NUM, the number of samples to use.
#
#  Output:
#
#    real C_LON(*), C_LAT(*), the longitude and latitude 
#    of the centroids of the Voronoi regions.
#
  import numpy as np
#
#  Get the longitude and latitudes of the vertices of the Florida polygon.
#
  f_lon, f_lat = florida_shape_read ( )
#
#  Determine the bounding box.
#
  f_lon_min = min ( f_lon )
  f_lon_max = max ( f_lon )
  f_lat_min = min ( f_lat )
  f_lat_max = max ( f_lat )
#
#  Initialize the counts for each generator.
#
  n = len ( g_lon )
  c_lat = np.zeros ( n )
  c_lon = np.zeros ( n )
  c_count = np.zeros ( n )
#
#  Choose random LL points in the bounding box.
#  Accept them only if they are contained in the Florida polygon.
#
  s = 0

  while ( s < sample_num ):

    lon = f_lon_min + ( f_lon_max - f_lon_min ) * np.random.rand ( )
    lat = f_lat_min + ( f_lat_max - f_lat_min ) * np.random.rand ( )
 
    inside = polygon_contains_point ( lon, lat, f_lon, f_lat )

    if ( inside ):

      s = s + 1

      d_min = np.Inf
      i_min = -1
      for i in range ( 0, n ):
        d = ( lat - g_lat[i] ) ** 2 + ( lon - g_lon[i] ) ** 2
        if ( d < d_min ):
          d_min = d
          i_min = i

      c_lat[i_min] = c_lat[i_min] + lat
      c_lon[i_min] = c_lon[i_min] + lon
      c_count[i_min] = c_count[i_min] + 1
#
#  Set the centroid estimates.
#
  for i in range ( 0, n ):
    if ( c_count[i] == 0 ):
      c_lon[i] = g_lon[i]
      c_lat[i] = g_lat[i]
    else:
      c_lon[i] = c_lon[i] / float ( c_count[i] )
      c_lat[i] = c_lat[i] / float ( c_count[i] )

  return c_lon, c_lat

def florida_centroid_geo_test ( ):

#*****************************************************************************80
#
## florida_centroid_geo_test() tests florida_centroid_geo().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'florida_centroid_geo_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_centroid_geo can estimate the centroids of' )
  print ( '  the Voronoi cells associated with a set of points' )
  print ( '  within the boundaries of Florida,' )
  print ( '  expressed as longitudes and latitudes.' )
#
#  Set the data.
#
  name = [ \
  'Pensacola', \
  'Tallahassee', \
  'Jacksonville', \
  'Tampa', \
  'Gainesville', \
  'Orlando', \
  'Miami' ]

  g_lon = np.array ( [ \
    -87.20, \
    -84.25, \
    -81.66, \
    -82.48, \
    -82.32, \
    -81.30, \
    -80.21 ] )

  g_lat = np.array ( [ \
   30.43, \
   30.46, \
   30.34, \
   27.97, \
   29.65, \
   28.42, \
   25.78 ] )
#
#  Estimate the centroids.
#
  sample_num = 5000
  print ( '' )
  print ( '  Centroids estimated using %d sample points.' % ( sample_num ) )

  c_lon, c_lat = florida_centroid_geo ( g_lon, g_lat, sample_num )
#
#  List the generators and centroids.
#
  print ( '' )
  print ( '   I  City             G Lon     G Lat     C Lon     C Lat' )
  print ( '' )
  n = len ( g_lon )
  for i in range ( 0, n ):
    print ( '  %2d  %-12s  %8.2f  %8.2f  %8.2f  %8.2f' \
      % ( i, name[i], g_lon[i], g_lat[i], c_lon[i], c_lat[i] ) )
#
#  Show generators, centroids, and Voronoi region together.
# 
  filename = 'florida_centroid_geo.png'
  plot_title = 'Geometric centroids (red) of Voronoi cells for cities (black).'
  florida_voronoi_display ( g_lon, g_lat, c_lon, c_lat, filename, plot_title )

  return

def florida_cvt_geometric ( gen_lon, gen_lat ):

#*****************************************************************************80
#
## florida_cvt_geometric() estimates a CVT for Florida based on geometric data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real GEN_LON(N), GEN_LAT(N), points to be used as the initial
#    generators.
#
#  Output:
#
#    real GEN_LON(N), GEN_LAT(N), improved estimates of the CVT
#    generators.
#

#
#  We use N points within the Florida polygon as generators.
#
  n = len ( gen_lon )
#
#  Display the points.
#
  filename = ''
  plot_title = 'Initial generators'
  florida_point_display ( gen_lon, gen_lat, filename, plot_title )
#
#  Prepare for random sampling.
#
  sample_num = 5000

  for step in range ( 0, 10 ):

    cen_lon, cen_lat = florida_centroid_geo ( gen_lon, gen_lat, sample_num )

    plot_title = ( 'CVT Step %d' % ( step ) )
    florida_voronoi_display ( gen_lon, gen_lat, cen_lon, cen_lat, '', plot_title )

    filename = ''
    plot_title = ( 'Generators after step %d' % ( step ) )
    florida_point_display ( cen_lon, cen_lat, filename, plot_title )

    gen_lon = cen_lon
    gen_lat = cen_lat

  return gen_lon, gen_lat

def florida_cvt_geometric_test ( ):

#*****************************************************************************80
#
## florida_cvt_geometric_test() tests florida_cvt_geometric().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'florida_cvt_geometric_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_cvt_geometric can estimate the geometric centroidal' )
  print ( '  Voronoi tessellation (CVT) of a set of points' )
  print ( '  within the boundaries of Florida,' )
  print ( '  expressed as longitudes and latitudes.' )
#
#  Set the data.
#
  name = [ \
  'Pensacola', \
  'Tallahassee', \
  'Jacksonville', \
  'Tampa', \
  'Gainesville', \
  'Orlando', \
  'Miami' ]

  g_lon = np.array ( [ \
    -87.20, \
    -84.25, \
    -81.66, \
    -82.48, \
    -82.32, \
    -81.30, \
    -80.21 ] )

  g_lat = np.array ( [ \
   30.43, \
   30.46, \
   30.34, \
   27.97, \
   29.65, \
   28.42, \
   25.78 ] )
#
#  Estimate the CVT.
#
  g_lon, g_lat = florida_cvt_geometric ( g_lon, g_lat )
#
#  Estimate the centroids.
#
  sample_num = 5000

  c_lon, c_lat = florida_centroid_geo ( g_lon, g_lat, sample_num )
#
#  Show generators, centroids, and Voronoi region together.
# 
  filename = 'florida_cvt_geo.png';
  plot_title = 'Estimated 7-Generator geometric CVT for Florida'

  florida_voronoi_display ( g_lon, g_lat, c_lon, c_lat, filename, plot_title )

  return

def florida_district_reader ( filename ):

#*****************************************************************************80
#
## florida_district_reader() reads Florida Congressional District data.
#
#  Discussion:
#
#    This function reads a comma separated value (CSV) file that
#    contains data about the 27 congressional districts in Florida,
#    * the index (1 through 27);
#    * the tag (for now, just the index as a string);
#    * a city (usually the home of the representative);
#    * 'N' or 'S' (for the latitude);
#    * Dlat, Mlat, Slat, for the degrees, minutes and seconds of latitude;
#    * 'E' or 'W' (for the longitude);
#    * Dlon, Mlon, Slon, for the degrees, minutes and seconds of longitude.
#
#    In both MATLAB and Python, reading CSV files containing mixed types
#    of data seems surprisingly awkward to do, and I have had to be
#    satisfied with finding something that just barely works.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file to be read.
#
#  Output:
#
#    real LON[N], LAT[N], the longitude and latitude for 
#    representative cities in each congressional district.
#
#    string NAME[N], the name of the city.
#
#    string TAG[N], the tag for the district.
#
  import csv
  import numpy as np

  f = open ( filename, 'rt' )

  reader = csv.reader ( f, delimiter = ',', skipinitialspace = True )
  rownum = 0

  tag_list = []
  name_list = []
  lat_list = []
  lon_list = []

  for row in reader:

    if ( rownum == 0 ):

      header = row

    else:

      tag_list.append ( row[1] )

      name_list.append ( row[2] )

      t = int ( row[4] ) + int ( row[5] ) / 60.0 + int ( row[6] ) / 3600.0
      lat_list.append ( t ) 
#
#  The "W" in the longitude designation indicates that it is negative.
#  Rather than deal with it honorably, we'll just assume it's negative.
#
      t = int ( row[8] ) + int ( row[9] ) / 60.0 + int ( row[10] ) / 3600.0
      lon_list.append ( - t ) 

    rownum = rownum + 1

  f.close ( )
#
#  Convert lists to NP arrays.
#
  lat = np.asarray ( lat_list )
  lon = np.asarray ( lon_list )

  return lon, lat, name_list, tag_list

def florida_district_reader_test ( ):

#*****************************************************************************80
#
## florida_district_reader_test() tests florida_district_reader().
#
#  Discussion:
#
#    Request that the file "florida_district.txt" be read, and the
#    longitude, latitude, and tag for each city be returned.
#
#    Print and plot the data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  filename = 'florida_district.txt'

  print ( '' )
  print ( 'florida_district_reader_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_district_reader reads a file "%s"' % ( filename ) )
  print ( '  and returns the longitude, latitude, and name of a city in' )
  print ( '  each Florida congressional district.' )
#
#  Read the longitude, latitude and name of each city.
#
  d_lon, d_lat, name, tag = florida_district_reader ( filename )
#
#  Get the size of the data.
#
  n = len ( d_lon )
#
#  Print the data.
#
  print ( '' )
  print ( ' #  City                      Longitude       Latitude' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%2d  %-18s  %14.6f  %14.6f' % ( i, name[i], d_lon[i], d_lat[i] ) )
#
#  Plot the cities.
#
  filename = 'florida_district.png'
  plot_title = 'A city in each Florida Congressional District'
  florida_point_display ( d_lon, d_lat, filename, plot_title )

  return

def florida_point_display ( p_lon, p_lat, filename, plot_title ):

#*****************************************************************************80
#
## florida_point_display() displays points within the boundaries of Florida.
#
#  Discussion:
#
#    The points are assumed to be given in terms of longitude and latitude.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Input:
#
#    real P_LON(*), P_LAT(*), the longitude and latitude of the points.
#
#    string FILENAME, a name for the graphics file.
#    If FILENAME is '', the plot is not saved.
#
#    string PLOT_TITLE, a title for the plot.
#
  import matplotlib.pyplot as plt

  f_lon, f_lat = florida_shape_read ( )

  plt.plot ( f_lon, f_lat, linewidth = 2, color = 'g' )

  plt.plot ( p_lon, p_lat, 'ro', markersize = 15 )

  plt.axis ( 'equal' )
  plt.grid ( 'on' )
  plt.xlabel ( 'Longitude' )
  plt.ylabel ( 'Latitude' )
  plt.title ( plot_title )
  if ( 0 < len ( filename ) ):
    plt.savefig ( filename )
    print ( '' )
    print ( '  Graphics data saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def florida_point_display_test ( ):

#*****************************************************************************80
#
## florida_point_display_test() tests florida_point_display().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'florida_point_display_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_point_display can display a set of points' )
  print ( '  within the boundaries of Florida,' )
  print ( '  expressed as longitudes and latitudes.' )

  name = [ \
  'Pensacola', \
  'Tallahassee', \
  'Jacksonville', \
  'Tampa', \
  'Gainesville', \
  'Orlando', \
  'Miami' ]

  p_lat = np.array ( [ \
   30.43, \
   30.46, \
   30.34, \
   27.97, \
   29.65, \
   28.42, \
   25.78 ] )

  p_lon = np.array ( [ \
    -87.20, \
    -84.25, \
    -81.66, \
    -82.48, \
    -82.32, \
    -81.30, \
    -80.21 ] )

  filename = 'florida_point_display.png'
  plot_title = 'Seven Florida Cities'
  florida_point_display ( p_lon, p_lat, filename, plot_title )

  return

def florida_sample_geo ( sample_num ):

#*****************************************************************************80
#
## florida_sample_geo() produces geometrically random sample points in Florida.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Input:
#
#    integer SAMPLE_NUM, the number of sample points desired.
#
#  Output:
#
#    real S_LON(SAMPLE_NUM), S_LAT(SAMPLE_NUM), sample points.
#
  import numpy as np
#
#  Get the longitude and latitudes of the vertices of the Florida polygon.
#
  f_lon, f_lat = florida_shape_read ( )
#
#  Determine the bounding box.
#
  f_lon_min = min ( f_lon )
  f_lon_max = max ( f_lon )
  f_lat_min = min ( f_lat )
  f_lat_max = max ( f_lat )
#
#  Choose random LL points in the bounding box.
#  Accept them only if they are containined in the Florida polygon.
#
  s_lon = np.zeros ( sample_num )
  s_lat = np.zeros ( sample_num )

  i = 0
  j = 0

  while ( i < sample_num ):

    lon = f_lon_min + ( f_lon_max - f_lon_min ) * np.random.rand ( )
    lat = f_lat_min + ( f_lat_max - f_lat_min ) * np.random.rand ( )
    inside = polygon_contains_point ( lon, lat, f_lon, f_lat )

    if ( inside ):
      s_lon[i] = lon
      s_lat[i] = lat
      i = i + 1

  return s_lon, s_lat

def florida_sample_geo_test ( ):

#*****************************************************************************80
#
## florida_sample_geo_test() tests florida_sample_geo().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'florida_sample_geo_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_sample_geo returns a given number of random' )
  print ( '  sample points within the boundaries of Florida,' )
  print ( '  expressed as longitudes and latitudes.' )

  sample_num = 100

  print ( '' )
  print ( '  Requesting %d sample points:' % ( sample_num ) )

  s_lon, s_lat = florida_sample_geo ( sample_num )

  print ( '' )
  print ( '  florida_point_display can display the sample points.' )

  filename = 'florida_sample_geo.png'
  plot_title = 'Sample Points in Florida'
  florida_point_display ( s_lon, s_lat, filename, plot_title )

  return

def florida_shape_display ( lon, lat, filename, plot_title ):

#*****************************************************************************80
#
## florida_shape_display() displays the shape of Florida.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Input:
#
#    real LON(*), LAT(*), the longitude and latitude of the points.
#
#    string FILENAME, a name for the graphics file.
#
#    string PLOT_TITLE, a title for the plot.
#
  import matplotlib.pyplot as plt

  plt.plot ( lon, lat, linewidth = 2, color = 'r' )
  plt.axis ( 'equal' )
  plt.grid ( 'on' )
  plt.xlabel ( 'Longitude' )
  plt.ylabel ( 'Latitude' )
  plt.title ( plot_title )
  if ( 0 < len ( filename ) ):
    plt.savefig ( filename )
    print ( '' )
    print ( '  Plot saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def florida_shape_display_test ( ):

#*****************************************************************************80
#
## florida_shape_display_test() tests florida_shape_display().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  
  print ( '' )
  print ( 'florida_shape_display_test:' )
  print ( '  florida_shape_display displays the shape of Florida.' )

  filename = 'florida_shape.txt'
  m = r8vec2_header_read ( filename )
  lon, lat = r8vec2_data_read ( filename, m )

  filename = 'florida_shape_display.png'
  plot_title = 'The shape of Florida'

  florida_shape_display ( lon, lat, filename, plot_title )

  return

def florida_shape_read ( ):

#*****************************************************************************80
#
## florida_shape_read() extracts the low resolution Florida polygon.
#
#  Discussion:
#
#    The MATLAB Mapping Toolbox includes information about high and
#    low resolution polygonal models of US States.  We want to examine
#    the low resolution polygonal model of Florida.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Output:
#
#    real LON(*), LAT(*), the longitude and latitude of the
#    polygonal vertices, listed in counterclockwise order.
#
  filename = 'florida_shape.txt'
  m = r8vec2_header_read ( filename )
  lon, lat = r8vec2_data_read ( filename, m )

  return lon, lat

def florida_shape_read_test ( ):

#*****************************************************************************80
#
## florida_shape_read_test() tests florida_shape_read().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'florida_shape_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_shape_read returns informaition defining' )
  print ( '  a low-resolution polygonal model of Florida.' )

  lon, lat = florida_shape_read ( )
#
#  Print some of the information.
#
  n = len ( lon )
  r8vec2_print_some ( n, lon, lat, 10, \
    '  Longitude/Latitude, Florida Polygon Vertices:' ) 
#
#  Show generators, centroids, and Voronoi region together.
# 
  filename = 'florida_shape_read.png';
  plot_title = 'Low resolution polygonal outline of Florida';
  florida_shape_display ( lon, lat, filename, plot_title );

  return

def florida_voronoi_display ( g_lon, g_lat, p_lon, p_lat, filename, plot_title ):

#*****************************************************************************80
#
## florida_voronoi_display() displays generators, and their Voronoi diagram.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 November 2016
#
#  Input:
#
#    real G_LON(*), G_LAT(*), the longitude and latitude of 
#    generators to be displayed on a map of Florida, using black dots.
#
#    real P_LON(*), P_LAT(*), additional points, to be shown using
#    red dots.
#
#    string FILENAME, a name for the graphics file.
#    If FILENAME is '', the plot is not saved.
#
#    string PLOT_TITLE, a title for the plot.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import scipy.spatial as spatial
#
#  Determine the Voronoi diagram for the generators.
#
  g_num = len ( g_lon )
  g = np.zeros ( [ g_num, 2 ] )
  g[:,0] = g_lon[:]
  g[:,1] = g_lat[:]

  vor = spatial.Voronoi ( g )
#
#  Plot the Voronoi diagram.
#
  spatial.voronoi_plot_2d ( vor )
#
#  Get the Florida information.
#
  f_lon, f_lat = florida_shape_read ( )
#
#  Draw the outline of Florida.
#
  plt.plot ( f_lon, f_lat, linewidth = 2, color = 'g' )
#
#  Include the auxilliary points.
#
  plt.plot ( p_lon, p_lat, 'ro', markersize = 15 )
#
#  More plot stuff.
#
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.xlabel ( 'Longitude' )
  plt.ylabel ( 'Latitude' )
  plt.title ( plot_title )
  if ( 0 < len ( filename ) ):
    plt.savefig ( filename )
    print ( '' )
    print ( '  Graphics data saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def florida_voronoi_display_test ( ):

#*****************************************************************************80
#
## florida_voronoi_display_test() tests florida_voronoi_display().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'florida_voronoi_display_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  florida_voronoi_display can display a set of points' )
  print ( '  within the boundaries of Florida,' )
  print ( '  expressed as longitudes and latitudes,' )
  print ( '  and the Voronoi diagram they generate.' )

  name = [ \
  'Pensacola', \
  'Tallahassee', \
  'Jacksonville', \
  'Tampa', \
  'Gainesville', \
  'Orlando', \
  'Miami' ]

  g_lon = np.array ( [ \
    -87.20, \
    -84.25, \
    -81.66, \
    -82.48, \
    -82.32, \
    -81.30, \
    -80.21 ] )

  g_lat = np.array ( [ \
   30.43, \
   30.46, \
   30.34, \
   27.97, \
   29.65, \
   28.42, \
   25.78 ] )

  p_lon = []
  p_lat = []

  filename = 'florida_voronoi_display.png'
  plot_title = 'Voronoi diagram for 7 Florida cities'

  florida_voronoi_display ( g_lon, g_lat, p_lon, p_lat, filename, plot_title )

  return

def polygon_contains_point ( x, y, px, py ):

#*****************************************************************************80
#
## polygon_contains_point() finds if a point is inside a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the coordinates of the point to be tested.
#
#    real PX(N), PY(N), the coordinates of the vertices of the polygon.
#
#  Output:
#
#    logical INSIDE, is TRUE if the point is inside the polygon.
#
  n = len ( px )
  inside = False

  px1 = px[0]
  py1 = py[0]
  xints = x - 1.0
  for i in range ( 0, n + 1 ):
    px2 = px[i%n]
    py2 = py[i%n]
    if ( min ( py1, py2 ) < y ):
      if ( y <= max ( py1, py2 ) ):
        if ( x <= max ( px1, px2 ) ):
          if ( py1 != py2 ):
            xints = ( y - py1 ) * ( px2 - px1 ) / ( py2 - py1 ) + px1
          if ( px1 == px2 or x <= xints ):
            inside = not inside
    px1 = px2
    py1 = py2

  return inside

def polygon_contains_point_test ( ):

#*****************************************************************************80
#
## polygon_contains_point_test() tests polygon_contains_point().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  test_num = 4

  x_test = np.array ( [ 1.0, 3.0, 0.0, 0.5 ] )

  y_test = np.array ( [ 1.0, 4.0, 2.0, -0.25 ] )

  px = np.array ( [ 0.0, 1.0, 2.0, 1.0, 0.0 ] )
 
  py = np.array ( [ 0.0, 0.0, 1.0, 2.0, 2.0 ] )

  print ( '' )
  print ( 'polygon_contains_point_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  polygon_contains_point determines if' )
  print ( '  a point is in a polygon.' )

  print ( '' )
  print ( '  The polygon vertices:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %8.4f  %8.4f' % ( i, px[i], py[i] ) )

  print ( '' )
  print ( '        X         Y     Inside?' )
  print ( '' )

  for test in range ( 0, test_num ):
 
    x = x_test[test]
    y = y_test[test]
 
    inside = polygon_contains_point ( x, y, px, py )

    print ( '  %8.2f  %8.2f    %s' % ( x, y, inside ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_contains_point_test' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_data_read ( filename, m ):

#*****************************************************************************80
#
## r8vec2_data_read() reads the data from an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is an pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#    integer M, the number of rows in the file.
#
#  Output:
#
#    real X(M), Y(M), the data.
#
  import numpy as np

  input = open ( filename, 'r' )

  x = np.zeros ( m )
  y = np.zeros ( m )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      data = line.split ( )
      x[i] = data[0]
      y[i] = data[1]
      i = i + 1

  input.close ( )

  return x, y

def r8vec2_data_read_test ( ):

#*****************************************************************************80
#
## r8vec2_data_read_test() tests r8vec2_data_read().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8vec2_data_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_data_read reads data from an R8VEC2.' )

  m = 5
  filename = 'r8vec2_write_test.txt'
  x, y = r8vec2_data_read ( filename, m )
  r8vec2_print ( m, x, y, '  Data read from file:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_data_read_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_header_read ( filename ):

#*****************************************************************************80
#
## r8vec2_header_read() reads the header from an R8VEC2 file.
#
#  Discussion:
#
#    An R8VEC2 is a pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the input file.
#
#  Output:
#
#    integer M, the number of rows in the file.
#
  n = file_column_count ( filename )

  if ( n != 2 ):
    print ( '' )
    print ( 'r8vec2_header_read - Fatal error!' )
    print ( '  The number of columns is not 2, but %d.' % ( n ) )
    raise Exception ( 'r8vec2_header_read - Fatal error!' )

  m = file_row_count ( filename )

  return m

def r8vec2_header_read_test ( ):

#*****************************************************************************80
#
## r8vec2_header_read_test() tests r8vec2_header_read().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_header_read_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_header_read counts rows in a file containing an R8VEC2.' )

  filename = 'r8vec2_write_test.txt'
  m = r8vec2_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows.' % ( filename, m ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_header_read_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_print ( n, a1, a2, title ):

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
#    27 June 2015
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
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_print_some ( n, x1, x2, max_print, title ):

#*****************************************************************************80
#
## r8vec2_print_some() prints "some" of an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is two R8VEC's.
#
#    An R8VEC is a vector of R8 values.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vectors, is no more than MAX_print, then
#    the entire vectors are printed, one entry of each per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vectors.
#
#    real X1(N), X2(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines to print.
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
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    print ( '......  ..............  ..............' )
    i = n - 1
    print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    i = max_print - 1
    print ( '%6d: %14g  %14g  ...more entries...' % ( i, x1[i], x2[i] ) )

  return

def r8vec2_print_some_test ( ):

#*****************************************************************************80
#
## r8vec2_print_some_test() tests r8vec2_print_some().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 100
  a = np.zeros ( n )
  b = np.zeros ( n )

  for i in range ( 0, n ):
    x = float ( i + 1 )
    a[i] = x * x
    b[i] = np.sqrt ( x )

  print ( '' )
  print ( 'r8vec2_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print_some prints some of a pair of R8VEC\'s.' )

  r8vec2_print_some ( n, a, b, 10, '  Square and square root:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_write ( filename, n, a, b ):

#*****************************************************************************80
#
## r8vec2_write() writes an R8VEC2 to a file.
#
#  Discussion:
#
#    An R8VEC2 is a pair of vectors of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer N, the number of entries in A.
#
#    real A(N), B(N), the vectors.
#
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g  %g\n' % ( a[i], b[i] )
    output.write ( s )

  output.close ( )

  return

def r8vec2_write_test ( ):

#*****************************************************************************80
#
## r8vec2_write_test() tests r8vec2_write().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_write_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test r8vec2_write, which writes an R8VEC2 to a file.' )

  filename = 'r8vec2_write_test.txt'
  n = 5
  a = np.array ( [ 1.1, 1.2, 1.3, 1.4, 1.5 ] )
  b = np.array ( [ 1.2, 2.2, 3.2, 4.2, 5.2 ] )
  r8vec2_write ( filename, n, a, b )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec2_write_test:' )
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

def florida_cvt_geo_test ( ):

#*****************************************************************************80
#
## florida_cvt_geo_test() tests florida_cvt_geo().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'florida_cvt_geo_test()' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test florida_cvt_geo().' )

  florida_centroid_geo_test ( )
  florida_cvt_geometric_test ( )
  florida_district_reader_test ( )
  florida_point_display_test ( )
  florida_sample_geo_test ( )
  florida_shape_display_test ( )
  florida_shape_read_test ( )
  florida_voronoi_display_test ( )
  polygon_contains_point_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'florida_cvt_geo_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  florida_cvt_geo_test ( )
  timestamp ( )
 
