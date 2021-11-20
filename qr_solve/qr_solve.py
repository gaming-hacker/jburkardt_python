#! /usr/bin/env python3
#
def dqrank ( a, lda, m, n, tol ):

#*****************************************************************************80
#
## dqrank() QR factors a rectangular matrix and estimates its rank.
#
#  Discussion:
#
#    This routine is used in conjunction with dqrlss to solve
#    overdetermined, underdetermined and singular linear systems
#    in a least squares sense.
#
#    dqrank uses the LINPACK subroutine dqrdc to compute the QR
#    factorization, with column pivoting, of an M by N matrix A.
#    The numerical rank is determined using the tolerance TOL.
#
#    Note that on ABS ( A(1,1) ) / ABS ( A(KR,KR) ) is an estimate
#    of the condition number of the matrix of independent columns,
#    and of R.  This estimate will be <= 1/TOL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2016
#
#  Author:
#
#    Original FORTRAN77 version by Jack Dongarra, Cleve Moler, Jim Bunch, 
#    Pete Stewart.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch, Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979,
#    ISBN13: 978-0-898711-72-1,
#    LC: QA214.L56.
#
#  Input:
#
#    real A(LDA,N), the matrix whose decomposition is to be computed.  
#
#    integer LDA, the leading dimension of A, which must
#    be at least M.
#
#    integer M, the number of rows of A.
#
#    integer N, the number of columns of A.
#
#    real TOL, a relative tolerance used to determine the
#    numerical rank.  The problem should be scaled so that all the elements
#    of A have roughly the same absolute accuracy, EPS.  Then a reasonable
#    value for TOL is roughly EPS divided by the magnitude of the largest
#    element.
#
#  Output:
#
#    integer KR, the numerical rank.
#
#    integer JPVT(N), the pivot information from dqrdc.
#    Columns JPVT(1), ..., JPVT(KR) of the original matrix are linearly
#    independent to within the tolerance TOL and the remaining columns
#    are linearly dependent.
#
#    real QRAUX(N), will contain extra information defining
#    the QR factorization.
#
#    real A(LDA,N), information from dqrdc.
#    The triangular matrix R of the QR factorization is contained in the
#    upper triangle and information needed to recover the orthogonal
#    matrix Q is stored below the diagonal in A and in the vector QRAUX.
#
  import numpy as np

  jpvt = np.zeros ( n, dtype = np.int32 )
  job = 1

  a, qraux, jpvt = dqrdc ( a, lda, m, n, jpvt, job )

  kr = 0
  k = min ( m, n )

  for j in range ( 0, k ):
    if ( abs ( a[j,j] ) <= tol * abs ( a[0,0] ) ):
      break
    kr = j + 1

  return kr, jpvt, qraux, a

def dqrank_test ( ):

#*****************************************************************************80
#
## dqrank_test() tests dqrank().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 4
  n = 4
  lda = n
  tol = 0.000001

  print ( '' )
  print ( 'dqrank_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dqrank factors a rectangular matrix and estimates its rank.' )

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i == j ):
        if ( i == 0 or i == m - 1 ):
          a[i,j] = 1.0 + 0.000000001
        else:
          a[i,j] = 2.0
      elif ( i == j + 1 or i == j - 1 ):
        a[i,j] = -1.0

  r8mat_print ( m, n, a, '  Matrix A:' )
        
  kr, jpvt, qraux, a = dqrank ( a, lda, m, n, tol )

  print ( '' )
  print ( ' Matrix rank estimated to be %d' % ( kr ) )

  r8mat_print ( m, n, a, '  QR factorization information in A:' )

  r8vec_print ( m, qraux, '  QR factorization informaiton in QRAUX:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'dqrank_test' )
  print ( '  Normal end of execution.' )
  return

def dqrdc ( a, lda, n, p, jpvt, job ):

#*****************************************************************************80
#
## dqrdc() computes the QR factorization of a real rectangular matrix.
#
#  Discussion:
#
#    dqrdc uses Householder transformations.
#
#    Column pivoting based on the 2-norms of the reduced columns may be
#    performed at the user's option.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 August 2016
#
#  Author:
#
#    Original FORTRAN77 version by Dongarra, Moler, Bunch, Stewart.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Dongarra, Moler, Bunch, Stewart,
#    LINPACK User's Guide,
#    SIAM, (Society for Industrial and Applied Mathematics),
#    3600 University City Science Center,
#    Philadelphia, PA, 19104-2688.
#    ISBN 0-89871-172-X
#
#  Input:
#
#    real A(LDA,P), the N by P matrix whose decomposition is to 
#    be computed.
#
#    integer LDA, the leading dimension of the array A.  LDA must
#    be at least N.
#
#    integer N, the number of rows of the matrix A.
#
#    integer P, the number of columns of the matrix A.
#
#    integer JPVT(P), integers that control the selection of the pivot 
#    columns.  The K-th column A(*,K) of A is placed in one of three classes 
#    according to the value of JPVT(K).
#      > 0, then A(K) is an initial column.
#      = 0, then A(K) is a free column.
#      < 0, then A(K) is a final column.
#    Before the decomposition is computed, initial columns are moved to
#    the beginning of the array A and final columns to the end.  Both
#    initial and final columns are frozen in place during the computation
#    and only free columns are moved.  At the K-th stage of the
#    reduction, if A(*,K) is occupied by a free column it is interchanged
#    with the free column of largest reduced norm.  JPVT is not referenced
#    if JOB == 0.  
#
#    integer JOB, initiates column pivoting.
#    0, no pivoting is done.
#    nonzero, pivoting is done.
#
#  Output:
#
#    real A(LDA,P), contains in its upper triangle the upper 
#    triangular matrix R of the QR factorization.  Below its diagonal 
#    A contains information from which the orthogonal part of the 
#    decomposition can be recovered.  Note that if pivoting has been 
#    requested, the decomposition is not that of the original matrix A 
#    but that of A with its columns permuted as described by JPVT.
#
#    real QRAUX(P), contains further information required
#    to recover the orthogonal part of the decomposition.
#
#    integer JPVT(P), JPVT(K) contains the index of the column of the
#    original matrix that has been interchanged into the K-th column, if
#    pivoting was requested.
#
  import numpy as np

  pl = 1
  pu = 0
  qraux = np.zeros ( p )
  work = np.zeros ( p )
#
#  If pivoting is requested, rearrange the columns.
#
  if ( job != 0 ):

    for j in range ( 0, p ):

      swapj = ( 0 < jpvt[j] )

      if ( jpvt[j] < 0 ):
        jpvt[j] = - ( j + 1 )
      else:
        jpvt[j] = ( j + 1 )

      if ( swapj ):

        if ( j + 1 != pl ):
          for i in range ( 0, n ):
            t = a[i,pl-1]
            a[i,pl-1] = a[i,j]
            a[i,j] = t

        jpvt[j] = jpvt[pl-1]
        jpvt[pl-1] = j + 1
        pl = pl + 1

    pu = p

    for j in range ( p - 1, -1, -1 ):

      if ( jpvt[j] < 0 ):

        jpvt[j] = - jpvt[j]

        if ( j + 1 != pu ):

          for i in range ( 0, n ):
            t = a[i,pu-1]
            a[i,pu-1] = a[i,j]
            a[i,j] = t

          jp = jpvt[pu-1]
          jpvt[pu-1] = jpvt[j]
          jpvt[j] = jp

        pu = pu - 1
#
#  Compute the norms of the free columns.
#
  for j in range ( pl - 1, pu ):
    t = 0.0
    for i in range ( 0, n ):
      t = t + a[i,j] ** 2
    qraux[j] = np.sqrt ( t )
    work[j] = qraux[j]
#
#  Perform the Householder reduction of A.
#
  lup = min ( n, p )

  for l in range ( 0, lup ):
#
#  Bring the column of largest norm into the pivot position.
#
    if ( pl <= l + 1 and l + 1 < pu ):

      maxnrm = 0.0
      maxj = l

      for j in range ( l, pu ):

        if ( maxnrm < qraux[j] ):
          maxnrm = qraux[j]
          maxj = j

      if ( maxj != l ):

        for i in range ( 0, n ):
          t         = a[i,l]
          a[i,l]    = a[i,maxj]
          a[i,maxj] = t

        qraux[maxj] = qraux[l]
        work[maxj] = work[l]

        jp = jpvt[maxj]
        jpvt[maxj] = jpvt[l]
        jpvt[l] = jp
#
#  Compute the Householder transformation for column L.
#
    qraux[l] = 0.0

    if ( l + 1 != n ):

      t = 0.0
      for i in range ( l, n ):
        t = t + a[i,l] ** 2
      nrmxl = np.sqrt ( t )

      if ( nrmxl != 0.0 ):

        if ( a[l,l] < 0.0 ):
          nrmxl = - abs ( nrmxl )
        elif ( 0.0 < a[l,l] ):
          nrmxl = abs ( nrmxl )

        for i in range ( l, n ):
          a[i,l] = a[i,l] / nrmxl

        a[l,l] = 1.0 + a[l,l]
#
#  Apply the transformation to the remaining columns, updating the norms.
#
        for j in range ( l + 1, p ):

          t = 0.0
          for i in range ( l, n ):
            t = t - a[i,l] * a[i,j]
          t = t / a[l,l]

          for i in range ( l, n ):
            a[i,j] = a[i,j] + t * a[i,l]

          if ( pl <= j and j <= pu ):

            if ( qraux[j] != 0.0 ):

              tt = 1.0 - ( abs ( a[l,j] ) / qraux[j] ) ** 2
              tt = max ( tt, 0.0 )
              t = tt
              tt = 1.0 + 0.05 * tt * ( qraux[j] / work[j] ) ** 2

              if ( tt != 1.0 ):
                qraux[j] = qraux[j] * np.sqrt ( t )
              else:
                t = 0.0
                for i in range ( l + 1, n ):
                  t = t + a[i,j] ** 2
                qraux[j] = np.sqrt ( t )
                work[j] = qraux[j]
#
#  Save the transformation.
#
        qraux[l] = a[l,l]
        a[l,l] = - nrmxl

  return a, qraux, jpvt

def dqrdc_test ( ):

#*****************************************************************************80
#
## dqrdc_test() tests dqrdc().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 3
  p = 3
  lda = n

  print ( '' )
  print ( 'dqrdc_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dqrdc computes the QR decomposition of a rectangular' )
  print ( '  matrix, but does not return Q and R explicitly.' )
  print ( '' )
  print ( '  Show how Q and R can be recovered using SQRSL.' )
#
#  Set the matrix A.
#
  a = np.array \
  ( [ \
    [ 1.0, 1.0, 0.0 ], \
    [ 1.0, 0.0, 1.0 ], \
    [ 0.0, 1.0, 1.0 ]  \
  ] )

  print ( '' )
  print ( '  The original matrix A:' )
  print ( '' )

  for i in range ( 0, n ):
    for j in range ( 0, p ):
      print ( '  %14.6g' % ( a[i,j] ) ),
    print ( '' )
#
#  Decompose the matrix.
#
  print ( '' )
  print ( '  Decompose the matrix.' )

  job = 0
  ipvt = np.zeros ( p, dtype = np.int32 )

  a, qraux, ipvt = dqrdc ( a, lda, n, p, ipvt, job )
#
#  Print out what dqrdc has stored in A...
#
  print ( '' )
  print ( '  The packed matrix A which describes Q and R:' )
  print ( '' )

  for i in range ( 0, n ):
    for j in range ( 0, p ):
      print ( '  %14.6g' % ( a[i,j] ) ),
    print ( '' )
#
#  ...and in QRAUX.
#
  print ( '' )
  print ( '  The QRAUX vector, containing some additional' )
  print ( '  information defining Q:' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %14.6g' % ( qraux[i] ) )
  print ( '' )
#
#  Print out the resulting R factor.
#
  r = np.zeros ( [ n, p ] )

  print ( '' )
  print ( '  The R factor:' )
  print ( '' )

  for i in range ( 0, n ):
    for j in range ( 0, p ):
      if ( i <= j ):
        r[i,j] = a[i,j]
      print ( '  %14.6g' % ( r[i,j] ) ),
    print ( '' )
#
#  Call dqrsl to extract the information about the Q matrix.
#  We do this, essentially, by asking dqrsl to tell us the
#  value of Q*Y, where Y is a column of the identity matrix.
#
  q = np.zeros ( [ n, n ] )

  job = 10000

  for j in range ( 0, n ):
#
#  Set the vector Y.
#
    y = np.zeros ( n )

    y[j] = 1.0
#
#  Ask dqrsl to tell us what Q*Y is.
#
    qy, qty, b, rsd, xb, info = dqrsl ( a, lda, n, p, qraux, y, job )

    if ( info != 0 ):
      print ( '  Error!  dqrsl returns INFO = %d' % ( info ) )
      return
#
#  Copy QY into the appropriate column of Q.
#
    for i in range ( 0, n ):
      q[i,j] = qy[i]
#
#  Now print out the Q matrix we have extracted.
#
  print ( '' )
  print ( '  The Q factor:' )
  print ( '' )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print ( '  %14.6g' % ( q[i,j] ) ),
    print ( '' )
#
#  Compute Q*R to verify that it equals A.
#
  b = np.dot ( q, r )
#
#  Print the result.
#
  print ( '' )
  print ( '  The product Q * R:' )
  print ( '' )

  for i in range ( 0, n ):
    for j in range ( 0, p ):
      print ( '  %14.6g' % ( b[i,j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'dqrdc_test' )
  print ( '  Normal end of execution.' )
  return

def dqrlss ( a, lda, m, n, kr, b, jpvt, qraux ):

#*****************************************************************************80
#
## dqrlss() solves a linear system in a least squares sense.
#
#  Discussion:
#
#    dqrlss must be preceded by a call to dqrank.
#
#    The system is to be solved is
#      A * X = B
#    where
#      A is an M by N matrix with rank KR, as determined by dqrank,
#      B is a given M-vector,
#      X is the N-vector to be computed.
#
#    A solution X, with at most KR nonzero components, is found which
#    minimizes the 2-norm of the residual (A*X-B).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2016
#
#  Author:
#
#    Original FORTRAN77 version by Dongarra, Moler, Bunch, Stewart.
#    Python version by John Burkardt.
#
#  Input:
#
#    real A(LDA,N), the QR factorization information
#    from dqrank.  The triangular matrix R of the QR factorization is
#    contained in the upper triangle and information needed to recover
#    the orthogonal matrix Q is stored below the diagonal in A and in
#    the vector QRAUX.
#
#    integer LDA, the leading dimension of A, which must
#    be at least M.
#
#    integer M, the number of rows of A.
#
#    integer N, the number of columns of A.
#
#    integer KR, the rank of the matrix, as estimated
#    by dqrank.
#
#    real B(M), the right hand side of the linear system.
#
#    integer JPVT(N), the pivot information from dqrank.
#    Columns JPVT(1), ..., JPVT(KR) of the original matrix are linearly
#    independent to within the tolerance TOL and the remaining columns
#    are linearly dependent.
#
#    real QRAUX(N), auxiliary information from dqrank
#    defining the QR factorization.
#
#  Output:
#
#    real X(N), a least squares solution to the
#    linear system.
#
#    real R(M), the residual, B - A*X.  RSD may
#    overwite B.
#
  import numpy as np
#
#  Solve the reduced system of rank KR.
#
  if ( 0 < kr ):
    job = 110
    qy, qty, x, r, ab, info = dqrsl ( a, lda, m, kr, qraux, b, job );
#
#  Reverse the pivoting to recover the original variable ordering.
#
  jpvt[0:n] = - jpvt[0:n]

  for j in range ( kr, n ):
    x = np.append ( x, 0.0 )

  for j in range ( 0, n ):

    if ( jpvt[j] <= 0 ):

      k = - jpvt[j]
      jpvt[j] = k

      while ( k != j + 1 ):

        t = x[j]
        x[j] = x[k-1]
        x[k-1] = t

        jpvt[k-1] = - jpvt[k-1]

        k = jpvt[k-1]

  return x, r

def dqrlss_test ( ):

#*****************************************************************************80
#
## dqrlss_test() tests dqrlss().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'dqrlss_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dqrlss solves a rectangular linear system A*x = b' )
  print ( '  with possibly non-full rank, in the least squares sense.' )
  print ( '  Compare a tabulated solution X1 to the computed result X2.' )
#
#  Set the matrix A.
#
  m = 6;
  n = 6;
  a = np.zeros ( [ m, n ] )
  b = np.zeros ( m )
  x1 = np.zeros ( n )
  
  for j in range ( 0, n ):
    x1[j] = float ( j + 1 )
    for i in range ( 0, m ):
      a[i,j] = 1.0 / float ( i + j + 1 )
      b[i] = b[i] + a[i,j] * x1[j]

  print ( '' )
  print ( '  The matrix A:' )
  print ( '' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      print ( '  %14.6g' % ( a[i,j] ) ),
    print ( '' )

  r8vec_print ( n, x1, '  Solution x1:' )
  r1 = b - np.dot ( a, x1 )
  r8vec_print ( m, r1, '  Residual b-A*x1:' )

  lda = m
  tol = 0.000001
#
#  Factor the matrix.
#
  a_qr = a.copy ( )
  kr, jpvt, qraux, a_qr = dqrank ( a_qr, lda, m, n, tol )

  print ( '' )
  print ( '  Matrix is of order m=%d by n=%d' % ( m, n ) )
  print ( '  Condition number tolerance is %g' % ( tol ) )
  print ( '  dqrank estimates rank as %d' % ( kr ) )
#
#  Solve the linear least squares problem.
#
  x2, r = dqrlss ( a_qr, lda, m, n, kr, b, jpvt, qraux )

  r8vec_print ( n, x2, '  Computed solution x2:' )
  r2 = b - np.dot ( a, x2 )
  r8vec_print ( m, r2, '  Residual b-A*x2:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'dqrlss_test' )
  print ( '  Normal end of execution.' )
  return

def dqrsl ( a, lda, n, k, qraux, y, job ):

#*****************************************************************************80
#
## dqrsl() computes transformations, projections, and least squares solutions.
#
#  Discussion:
#
#    dqrsl requires the output of dqrdc.
#
#    For K <= min(N,P), let AK be the matrix
#
#      AK = ( A(JPVT(1)), A(JPVT(2)), ..., A(JPVT(K)) )
#
#    formed from columns JPVT(1), ..., JPVT(K) of the original
#    N by P matrix A that was input to dqrdc.  If no pivoting was
#    done, AK consists of the first K columns of A in their
#    original order.  dqrdc produces a factored orthogonal matrix Q
#    and an upper triangular matrix R such that
#
#      AK = Q * (R)
#               (0)
#
#    This information is contained in coded form in the arrays
#    A and QRAUX.
#
#    The parameters QY, QTY, B, RSD, and AB are not referenced
#    if their computation is not requested and in this case
#    can be replaced by dummy variables in the calling program.
#    To save storage, the user may in some cases use the same
#    array for different parameters in the calling sequence.  A
#    frequently occuring example is when one wishes to compute
#    any of B, RSD, or AB and does not need Y or QTY.  In this
#    case one may identify Y, QTY, and one of B, RSD, or AB, while
#    providing separate arrays for anything else that is to be
#    computed.
#
#    Thus the calling sequence
#
#      call dqrsl ( a, lda, n, k, qraux, y, dum, y, b, y, dum, 110, info )
#
#    will result in the computation of B and RSD, with RSD
#    overwriting Y.  More generally, each item in the following
#    list contains groups of permissible identifications for
#    a single calling sequence.
#
#      1. (Y,QTY,B) (RSD) (AB) (QY)
#
#      2. (Y,QTY,RSD) (B) (AB) (QY)
#
#      3. (Y,QTY,AB) (B) (RSD) (QY)
#
#      4. (Y,QY) (QTY,B) (RSD) (AB)
#
#      5. (Y,QY) (QTY,RSD) (B) (AB)
#
#      6. (Y,QY) (QTY,AB) (B) (RSD)
#
#    In any group the value returned in the array allocated to
#    the group corresponds to the last member of the group.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 August 2016
#
#  Author:
#
#    Original FORTRAN77 version by Dongarra, Moler, Bunch, Stewart.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Dongarra, Moler, Bunch, Stewart,
#    LINPACK User's Guide,
#    SIAM, (Society for Industrial and Applied Mathematics),
#    3600 University City Science Center,
#    Philadelphia, PA, 19104-2688.
#    ISBN 0-89871-172-X
#
#  Input:
#
#    real A(LDA,P), contains the output of dqrdc.
#
#    integer LDA, the leading dimension of the array A.
#
#    integer N, the number of rows of the matrix AK.  It must
#    have the same value as N in dqrdc.
#
#    integer K, the number of columns of the matrix AK.  K
#    must not be greater than min(N,P), where P is the same as in the
#    calling sequence to dqrdc.
#
#    real QRAUX(P), the auxiliary output from dqrdc.
#
#    real Y(N), a vector to be manipulated by dqrsl.
#
#    integer JOB, specifies what is to be computed.  JOB has
#    the decimal expansion ABCDE, with the following meaning:
#      if A /= 0, compute QY.
#      if B /= 0, compute QTY.
#      if C /= 0, compute QTY and B.
#      if D /= 0, compute QTY and RSD.
#      if E /= 0, compute QTY and AB.
#    Note that a request to compute B, RSD, or AB automatically triggers
#    the computation of QTY, for which an array must be provided in the
#    calling sequence.
#
#  Output:
#
#    real QY(N), contains Q * Y, if requested.
#
#    real QTY(N), contains Q' * Y, if requested.
#
#    real B(K), the solution of the least squares problem
#      minimize norm2 ( Y - AK * B),
#    if its computation has been requested.  Note that if pivoting was
#    requested in dqrdc, the J-th component of B will be associated with
#    column JPVT(J) of the original matrix A that was input into dqrdc.
#
#    real RSD(N), the least squares residual Y - AK * B,
#    if its computation has been requested.  RSD is also the orthogonal
#    projection of Y onto the orthogonal complement of the column space
#    of AK.
#
#    real AB(N), the least squares approximation Ak * B,
#    if its computation has been requested.  AB is also the orthogonal
#    projection of Y onto the column space of A.
#
#    integer INFO, is zero unless the computation of B has
#    been requested and R is exactly singular.  In this case, INFO is the
#    index of the first zero diagonal element of R, and B is left unaltered.
#
  import numpy as np

  qy = np.zeros ( n )
  qty = np.zeros ( n )
  b = np.zeros ( k )
  rsd = np.zeros ( n )
  ab = np.zeros ( n )
#
#  Set info flag.
#
  info = 0
#
#  Determine what is to be computed.
#
  cqy =  int   ( job / 10000         ) != 0
  cqty =       ( job % 10000 )         != 0
  cb =   int ( ( job %  1000 ) / 100 ) != 0
  cr =   int ( ( job %   100 ) /  10 ) != 0
  cab =        ( job %    10 )         != 0

  ju = min ( k, n - 1 )
#
#  Special action when N = 1.
#
  if ( ju == 0 ):

    qy[0] = y[0]
    qty[0] = y[0]
    ab[0] = y[0]

    if ( a[0,0] == 0.0 ):
      info = 1
    else:
      b[0] = y[0] / a[0]

    rsd[0] = 0.0

    return qy, qty, b, rsd, ab, info
#
#  Set up to compute QY or QTY.
#
  for i in range ( 0, n ):
    qy[i] = y[i]
    qty[i] = y[i]
#
#  Compute QY.
#
  if ( cqy ):

    for j in range ( ju - 1, -1, -1 ):

      if ( qraux[j] != 0.0 ):
        ajj = a[j,j]
        a[j,j] = qraux[j]
        t = 0.0
        for i in range ( j, n ):
          t = t - a[i,j] * qy[i]
        t = t / a[j,j]
        for i in range ( j, n ):
          qy[i] = qy[i] + t * a[i,j]
        a[j,j] = ajj
#
#  Compute Q'*Y.
#
  if ( cqty ):

    for j in range ( 0, ju ):
      if ( qraux[j] != 0.0 ):
        ajj = a[j,j]
        a[j,j] = qraux[j]
        t = 0.0
        for i in range ( j, n ):
          t = t - a[i,j] * qty[i]
        t = t / a[j,j]
        for i in range ( j, n ):
          qty[i] = qty[i] + t * a[i,j]
        a[j,j] = ajj
#
#  Set up to compute B, RSD, or AB.
#
  for i in range ( 0, k ):
    b[i] = qty[i]
    ab[i] = qty[i]

  for i in range ( k, n ):
    rsd[i] = qty[i]
#
#  Compute B.
#
  if ( cb ):

    for j in range ( k - 1, -1, -1 ):

      if ( a[j,j] == 0.0 ):
        info = j + 1
        break

      b[j] = b[j] / a[j,j]

      if ( 0 < j ):
        t = - b[j]
        for i in range ( 0, j ):
          b[i] = b[i] + t * a[i,j]
#
#  Compute RSD or AB as required.
#
  if ( cr or cab ):

    for j in range ( ju - 1, -1, -1 ):

      if ( qraux[j] != 0.0 ):

        ajj = a[j,j]
        a[j,j] = qraux[j]

        if ( cr ):
          t = 0.0
          for i in range ( j, n ):
            t = t - a[i,j] * rsd[i]
          t = t / a[j,j]
          for i in range ( j, n ):
            rsd[i] = rsd[i] + t * a[i,j]

        if ( cab ):
          t = 0.0
          for i in range ( j, n ):
            t = t - a[i,j] * ab[i]
          t = t / a[j,j]
          for i in range ( j, n ):
            ab[i] = ab[i] + t * a[i,j]

        a[j,j] = ajj

  return qy, qty, b, rsd, ab, info

def dqrsl_test ( ):

#*****************************************************************************80
#
## dqrsl_test() tests dqrsl().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  p = 3
  lda = n

  print ( '' )
  print ( 'dqrsl_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dqrsl solves a rectangular linear system A*x=b in the' )
  print ( '  least squares sense after A has been factored by dqrdc.' )
#
#  Set the matrix A.
#
  a = np.array \
  ( [ \
    [ 1.0,  1.0,  1.0 ], \
    [ 1.0,  2.0,  4.0 ], \
    [ 1.0,  3.0,  9.0 ], \
    [ 1.0,  4.0, 16.0 ], \
    [ 1.0,  5.0, 25.0 ]  \
  ] )

  print ( '' )
  print ( '  The matrix A:' )
  print ( '' )

  for i in range ( 0, n ):
    for j in range ( 0, p ):
      print ( '  %14.6g' % ( a[i,j] ) ),
    print ( '' )
#
#  Decompose the matrix.
#
  print ( '' )
  print ( '  Decompose the matrix.' )

  job = 0
  ipvt = np.zeros ( n, dtype = np.int32 )

  a, qraux, ipvt = dqrdc ( a, lda, n, p, ipvt, job )
#
#  Call dqrsl to compute the least squares solution A*x=b.
#
  job = 110

  y = np.array \
  ( [ \
    1.0, \
    2.3, \
    4.6, \
    3.1, \
    1.2  \
  ] )  

  b2 = np.array \
  ( [ \
    -3.02, \
     4.4914286, \
    -0.72857143 
  ] )

  qy, qty, b, r, xb, info = dqrsl ( a, lda, n, p, qraux, y, job )

  if ( info != 0 ):
    print ( '' )
    print ( 'dqrsl_test - Warning!' )
    print ( '  dqrsl returns INFO = %d' % ( info ) )
    return

  print ( '' )
  print ( '      X          X(expected):' )
  print ( '' )

  for i in range ( 0, p ):
    print ( '  %14.6g  %14.6g' % ( b[i], b2[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'dqrsl_test' )
  print ( '  Normal end of execution.' )
  return

def drotg ( a, b ):

#*****************************************************************************80
#
## drotg() constructs a Givens plane rotation.
#
#  Discussion:
#
#    Given values A and B, this routine computes
#
#    SIGMA = sign ( A ) if abs ( A ) >  abs ( B )
#          = sign ( B ) if abs ( A ) <= abs ( B )
#
#    R     = SIGMA * ( A * A + B * B )
#
#    C = A / R if R is not 0
#      = 1     if R is 0
#
#    S = B / R if R is not 0,
#        0     if R is 0.
#
#    The computed numbers then satisfy the equation
#
#    (  C  S ) ( A ) = ( R )
#    ( -S  C ) ( B ) = ( 0 )
#
#    The routine also computes
#
#    Z = S     if abs ( A ) > abs ( B ),
#      = 1 / C if abs ( A ) <= abs ( B ) and C is not 0,
#      = 1     if C is 0.
#
#    The single value Z encodes C and S, and hence the rotation:
#
#    If Z = 1, set C = 0 and S = 1
#    If abs ( Z ) < 1, set C = sqrt ( 1 - Z * Z ) and S = Z
#    if abs ( Z ) > 1, set C = 1/ Z and S = sqrt ( 1 - C * C )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Input:
#
#    real A, B, the values A and B.
#
#  Output:
#
#    real C, S, the cosine and sine of the Givens rotation.
#
#    real R, Z, the values R and Z.
#
  import numpy as np

  if ( abs ( b ) < abs ( a ) ):
    roe = a
  else:
    roe = b

  scale = abs ( a ) + abs ( b )

  if ( scale == 0.0 ):
    c = 1.0
    s = 0.0
    r = 0.0
  else:
    r = scale * np.sqrt ( ( a / scale ) ** 2 + ( b / scale ) ** 2 )
    if ( roe < 0.0 ):
      r = - r
    c = a / r
    s = b / r

  if ( 0.0 < abs ( c ) and abs ( c ) <= s ):
    z = 1.0 / c
  else:
    z = s

  return c, s, r, z

def drotg_test ( ):

#*****************************************************************************80
#
## drotg_test() tests drotg().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 5

  print ( '' )
  print ( 'drotg_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  drotg generates a real Givens rotation' )
  print ( '    (  C  S ) * ( A ) = ( R )' )
  print ( '    ( -S  C )   ( B )   ( 0 )' )
  print ( '' )

  for test in range ( 0, test_num ):

    a = np.random.rand ( )
    b = np.random.rand ( )

    c, s, r, z = drotg ( a, b )

    print ( '' )
    print ( '  A =  %g  B =  %g' % ( a, b ) )
    print ( '  C =  %g  S =  %g' % ( c, s ) )
    print ( '  R =  %g  Z =  %g' % ( r, z ) )
    print ( '   C*A+S*B = %g' % (  c * a + s * b ) )
    print ( '  -S*A+C*B = %g' % ( -s * a + c * b ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'drotg_test' )
  print ( '  Normal end of execution.' )
  return

def drot ( n, x, incx, y, incy, c, s ):

#*****************************************************************************80
#
## drot() applies a plane rotation.
#
#  Discussion:
#
#    Note that the FORTRAN version of this function allowed users to pass in
#    X and Y data that was noncontiguous, (such as rows of a FORTRAN matrix).
#    The rotated data overwrote the input data, and so it might therefore
#    also be noncontiguous.
#
#    This function does not assume that the output overwrites the input,
#    and treats the output vectors as new items of length exactly N.
#
#    Note, moreover, that Python does NOT allow a matrix to be treated as a 
#    vector in quite the simple way that FORTRAN does.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Input:
#
#    integer N, the number of entries in the vectors.
#
#    real X(INCX*N), one of the vectors to be rotated.
#
#    integer INCX, the increment between successive entries of X.
#
#    real Y(INCX*N), one of the vectors to be rotated.
#
#    integer INCY, the increment between successive elements of Y.
#
#    real C, S, parameters (presumably the cosine and
#    sine of some angle) that define a plane rotation.
#
#  Output:
#
#    real XR(N), the rotated vector.
#
#    real YR(N), the rotated vector.
#
  import numpy as np

  xr = np.zeros ( n )
  yr = np.zeros ( n )

  if ( n <= 0 ):

    pass

  elif ( incx == 1 and incy == 1 ):

    xr[0:n] = c * x[0:n] + s * y[0:n]
    yr[0:n] = c * y[0:n] - s * x[0:n]

  else:

    if ( 0 <= incx ):
      ix = 0
    else:
      ix = ( - n + 1 ) * incx

    if ( 0 <= incy ):
      iy = 0
    else:
      iy = ( - n + 1 ) * incy

    for i in range ( 0, n ):
      xr[ix] = c * x[ix] + s * y[iy]
      yr[iy] = c * y[iy] - s * x[ix]
      ix = ix + incx
      iy = iy + incy

  return xr, yr

def drot_test ( ):

#*****************************************************************************80
#
## drot_test() tests drot().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 6
  x = np.zeros ( n )
  y = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
    y[i] = x[i] * x[i] - 12.0
 
  print ( '' )
  print ( 'drot_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  drot carries out a Givens rotation.' )
  print ( '' )
  print ( '  Vectors X and Y' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %14.6g  %14.6g' % ( i, x[i], y[i] ) )

  c = 0.5
  s = np.sqrt ( 1.0 - c * c )
  xr, yr = drot ( n, x, 1, y, 1, c, s )
  print ( '' )
  print ( '  xr, yr = drot ( n, x, 1, y, 1, %g, %g )' % ( c, s ) )
  print ( '' )
  print ( '  Rotated vectors XR and YR' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %14.6g  %14.6g' % ( i, xr[i], yr[i] ) )

  t = np.arctan2 ( y[0], x[0] )
  c = np.cos ( t )
  s = np.sin ( t )
  xr, yr = drot ( n, x, 1, y, 1, c, s )
  print ( '' )
  print ( '  xr, yr = drot ( n, x, 1, y, 1, %g, %g )' % ( c, s ) )
  print ( '' )
  print ( '  Rotated vectors XR and YR' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %14.6g  %14.6g' % ( i, xr[i], yr[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'drot_test' )
  print ( '  Normal end of execution.' )
  return

def dsvdc ( a, lda, m, n, ldu, ldv, job ):

#*****************************************************************************80
#
## dsvdc() computes the singular value decomposition of a real rectangular matrix.
#
#  Discussion:
#
#    This routine reduces an M by N matrix A to diagonal form by orthogonal
#    transformations U and V.  The diagonal elements S(I) are the singular
#    values of A.  The columns of U are the corresponding left singular
#    vectors, and the columns of V the right singular vectors.
#
#    The form of the singular value decomposition is then
#
#      A(MxN) = U(MxM) * S(MxN) * V(NxN)'
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2016
#
#  Author:
#
#    Original FORTRAN77 version by Dongarra, Moler, Bunch, Stewart.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Dongarra, Moler, Bunch and Stewart,
#    LINPACK User's Guide,
#    SIAM, (Society for Industrial and Applied Mathematics),
#    3600 University City Science Center,
#    Philadelphia, PA, 19104-2688.
#    ISBN 0-89871-172-X
#
#  Input:
#
#    real A(LDA,N), the M by N matrix whose singular 
#    value decomposition is to be computed.
#
#    integer LDA, the leading dimension of the array A.
#    LDA must be at least N.
#
#    integer M, the number of rows of the matrix.
#
#    integer N, the number of columns of the matrix A.
#
#    integer LDU, the leading dimension of the array U.
#    LDU must be at least M.
#
#    integer LDV, the leading dimension of the array V.
#    LDV must be at least N.
#
#    integer JOB, controls the computation of the singular
#    vectors.  It has the decimal expansion AB with the following meaning:
#      A =  0, for not compute the left singular vectors.
#      A =  1, return the M left singular vectors in U.
#      A >= 2, return the first min(M,N) singular vectors in U.
#      B =  0, for not compute the right singular vectors.
#      B =  1, return the right singular vectors in V.
#
#  Output:
#
#    real A(LDA,N), the matrix has been destroyed.  Depending on the 
#    user's requests, the matrix may contain other useful information.
#
#    real S(MM), where MM = max(M+1,N).  The first
#    min(M,N) entries of S contain the singular values of A arranged in
#    descending order of magnitude.
#
#    real E(MM), where MM = max(M+1,N), ordinarily contains zeros.
#    However see the discussion of INFO for exceptions.
#
#    real U(LDU,K).  If JOBA = 1 then K = M
#    if 2 <= JOBA, then K = min(M,N).  U contains the M by M matrix of
#    left singular vectors.  U is not referenced if JOBA = 0.  If M <= N
#    or if JOBA = 2, then U may be identified with A in the subroutine call.
#
#    real V(LDV,N), the N by N matrix of right singular
#    vectors.  V is not referenced if JOB is 0.  If N <= M, then V may be
#    identified with A in the subroutine call.
#
#    integer INFO, status indicator.
#    The singular values (and their corresponding singular vectors)
#    S(INFO+1), S(INFO+2),...,S(MN) are correct.  Here MN = min ( M, N ).
#    Thus if INFO is 0, all the singular values and their vectors are
#    correct.  In any event, the matrix B = U' * A * V is the bidiagonal
#    matrix with the elements of S on its diagonal and the elements of E on
#    its superdiagonal.  Thus the singular values of A and B are the same.
#
  import numpy as np

  maxit = 30
  mm = max ( m + 1, n )

  s = np.zeros ( mm )
  e = np.zeros ( mm )
  joba = ( job // 10 )
  if ( joba == 1 ):
    u = np.zeros ( [ ldu, m ] )
  elif ( 1 <= joba ):
    u = np.zeros ( [ ldu, min ( m, n ) ] )
  v = np.zeros ( [ ldv, n ] )
  work = np.zeros ( m )

  info = 0
#
#  Determine what is to be computed.
#
  wantu = 0
  wantv = 0
  jobu = int ( ( job % 100 ) / 10 )

  if ( 1 < jobu ):
    ncu = min ( m, n )
  else:
    ncu = m

  if ( jobu != 0 ):
    wantu = 1

  if ( ( job % 10 ) != 0 ):
    wantv = 1
#
#  Reduce A to bidiagonal form, storing the diagonal elements
#  in S and the super-diagonal elements in E.
#
  info = 0
  nct = min ( m - 1, n )
  nrt = max ( 0, min ( m, n - 2 ) )
  lu = max ( nct, nrt )

  for l in range ( 0, lu ):
#
#  Compute the transformation for the L-th column and
#  place the L-th diagonal in S(L).
#
    if ( l <= nct - 1 ):

      t = 0.0
      for i in range ( l, m ):
        t = t + a[i,l] ** 2
      t = np.sqrt ( t )
      s[l] = t

      if ( s[l] != 0.0 ):
        if ( a[l,l] < 0.0 ):
          s[l] = - s[l]
        for i in range ( l, m ):
          a[i,l] = a[i,l] / s[l]
        a[l,l] = 1.0 + a[l,l]

      s[l] = - s[l]

    for j in range ( l + 1, n ):
#
#  Apply the transformation.
#
      if ( l <= nct - 1 and s[l] != 0.0 ):
        t = 0.0
        for i in range ( l, m ):
          t = t - a[i,l] * a[i,j]
        t = t / a[l,l]
        for i in range ( l, m ):
          a[i,j] = a[i,j] + t * a[i,l]
#
#  Place the L-th row of A into E for the
#  subsequent calculation of the row transformation.
#
      e[j] = a[l,j]
#
#  Place the transformation in U for subsequent back multiplication.
#
    if ( wantu and l <= nct - 1 ):
      for i in range ( l, m ):
        u[i,l] = a[i,l]
#
#  Compute the L-th row transformation and place the
#  L-th superdiagonal in E(L).
#
    if ( l <= nrt - 1 ):

      t = 0.0
      for i in range ( l + 1, n ):
        t = t + e[i] ** 2
      e[l] = np.sqrt ( t )
      if ( e[l] != 0.0 ):
        if ( e[l+1] < 0.0 ):
          e[l] = - e[l]
        e[l+1:n] = e[l+1:n] / e[l]
        e[l+1] = 1.0 + e[l+1]
      e[l] = - e[l]
#
#  Apply the transformation.
#
      if ( l + 1 <= m - 1 and e[l] != 0.0 ):

        work[l+1:m] = 0.0

        for j in range ( l + 1, n ):
          for i in range ( l + 1, m ):
            work[i] = work[i] + e[j] * a[i,j]

        for j in range ( l + 1, n ):
          for i in range ( l + 1, m ):
            a[i,j] = a[i,j] - e[j] / e[l+1] * work[i]
#
#  Place the transformation in V for subsequent back multiplication.
#
      if ( wantv ):
        v[l+1:n,l] = e[l+1:n]
#
#  Set up the final bidiagonal matrix of order MN.
#
  mn = min ( m + 1, n )
  nctp1 = nct + 1
  nrtp1 = nrt + 1

  if ( nct < n ):
    s[nctp1-1] = a[nctp1-1,nctp1-1]

  if ( m < mn ):
    s[mn-1] = 0.0

  if ( nrtp1 < mn ):
    e[nrtp1-1] = a[nrtp1-1,mn-1]

  e[mn-1] = 0.0
#
#  If required, generate U.
#
  if ( wantu ):

    for j in range ( nctp1 - 1, ncu ):
      for i in range ( 0, m ):
        u[i,j] = 0.0

    for j in range ( nctp1 - 1, ncu ):
      u[j,j] = 1.0

    for l in range ( nct - 1, -1, -1 ):
 
      if ( s[l] != 0.0 ):

        for j in range ( l + 1, ncu ):
          t = 0.0
          for i in range ( l, m ):
            t = t - u[i,l] * u[i,j]
          t = t / u[l,l]
          for i in range ( l, m ):
            u[i,j] = u[i,j] + t * u[i,l]

        for i in range ( 0, l ):
          u[i,l] = 0.0
        for i in range ( l, m ):
          u[i,l] = - u[i,l]
        u[l,l] = 1.0 + u[l,l]

      else:

        for i in range ( 0, m ):
          u[i,l] = 0.0
        u[l,l] = 1.0
#
#  If it is required, generate V.
#
  if ( wantv ):

    for l in range ( n - 1, -1, -1 ):

      if ( l <= nrt - 1 and e[l] != 0.0 ):

        for j in range ( l + 1, n ):
          t = 0.0
          for i in range ( l + 1, n ):
            t = t - v[i,l] * v[i,j]
          t = t / v[l+1,l]
          for i in range ( l + 1, n ):
            v[i,j] = v[i,j] + t * v[i,l]

      for i in range ( 0, n ):
        v[i,l] = 0.0
      v[l,l] = 1.0
#
#  Main iteration loop for the singular values.
#
  mm = mn
  iter = 0

  while ( 0 < mn ):
#
#  If too many iterations have been performed, set flag and return.
#
    if ( maxit <= iter ):
      print ( '' )
      print ( 'dsvdc - Warning!' )
      print ( '  MAXIT = %d <= ITER = %d' % ( maxit, iter ) )
      info = mn
      return a, s, e, u, v, info
#
#  This section of the program inspects for
#  negligible elements in the S and E arrays.
#
#  On completion the variables KASE and L are set as follows:
#
#  KASE = 1     if S(MN) and E(L-1) are negligible and L < MN
#  KASE = 2     if S(L) is negligible and L < MN
#  KASE = 3     if E(L-1) is negligible, L < MN, and
#               S(L), ..., S(MN) are not negligible (QR step).
#  KASE = 4     if E(MN-1) is negligible (convergence).
#
    for l in range ( mn - 2, -2, -1 ):

      if ( l == -1 ):
        break

      test = abs ( s[l] ) + abs ( s[l+1] )
      ztest = test + abs ( e[l] )

      if ( ztest == test ):
        e[l] = 0.0
        break

    if ( l == mn - 2 ):

      kase = 4

    else:

      for ls in range ( mn - 1, l - 1, -1 ):

        if ( ls == l ):
          break

        test = 0.0
        if ( ls != mn - 1 ):
          test = test + abs ( e[ls] )

        if ( ls != l + 1 ):
          test = test + abs ( e[ls-1] )

        ztest = test + abs ( s[ls] )

        if ( ztest == test ):
          s[ls] = 0.0
          break

      if ( ls == l ):
        kase = 3
      elif ( ls == mn - 1 ):
        kase = 1
      else:
        kase = 2
        l = ls

    l = l + 1
#
#  Deflate negligible S(MN).
#
    if ( kase == 1 ):

      mm1 = mn - 1
      f = e[mn-2]
      e[mn-2] = 0.0

      for k in range ( mm1 - 1, l - 1, -1 ):
 
        t1 = s[k]
        cs, sn, t1, f = drotg ( t1, f )
        s[k] = t1

        if ( k != l ):
          f = - sn * e[k-1]
          e[k-1] = cs * e[k-1]

        if ( wantv ):
          v1, v2 = drot ( n, v[0:n,k], 1, v[0:n,mn-1], 1, cs, sn )
          for i in range ( 0, n ):
            v[i,k]    = v1[i]
            v[i,mn-1] = v2[i]
#
#  Split at negligible S(L).
#
    elif ( kase == 2 ):

      f = e[l-1]
      e[l-1] = 0.0

      for k in range ( l, mn ):

        t1 = s[k]
        cs, sn, t1, f = drotg ( t1, f )
        s[k] = t1
        f = - sn * e[k]
        e[k] = cs * e[k]
        if ( wantu ):
          u1, u2 = drot ( m, u[0:m,k], 1, u[0:m,l-1], 1, cs, sn )
          for i in range ( 0, m ):
            u[i,k] = u1[i]
            u[i,l-1] = u2[i]
#
#  Perform one QR step.
#
    elif ( kase == 3 ):
#
#  Calculate the shift.
#
      scale = max ( abs ( s[mn-1] ), \
              max ( abs ( s[mn-2] ), \
              max ( abs ( e[mn-2] ), \
              max ( abs ( s[l]    ), \
                    abs ( e[l] ) ) ) ) )

      sm = s[mn-1] / scale
      smm1 = s[mn-2] / scale
      emm1 = e[mn-2] / scale
      sl = s[l] / scale
      el = e[l] / scale
      b = ( ( smm1 + sm ) * ( smm1 - sm ) + emm1 * emm1 ) / 2.0
      c = sm  * sm * emm1 * emm1
      shift = 0.0

      if ( b != 0.0 or c != 0.0 ):
        shift = np.sqrt ( b * b + c )
        if ( b < 0.0 ):
          shift = - shift
        shift = c / ( b + shift )

      f = ( sl + sm ) * ( sl - sm ) - shift
      g = sl * el
#
#  Chase zeros.
#
      mm1 = mn - 1

      for k in range ( l, mm1 ):

        cs, sn, f, g = drotg ( f, g )

        if ( k != l ):
          e[k-1] = f

        f = cs * s[k] + sn * e[k]
        e[k] = cs * e[k] - sn * s[k]
        g = sn * s[k+1]
        s[k+1] = cs * s[k+1]

        if ( wantv ):
          v1, v2 = drot ( n, v[0:n,k], 1, v[0:n,k+1], 1, cs, sn )
          for i in range ( 0, n ):
            v[i,k] = v1[i]
            v[i,k+1] = v2[i]

        cs, sn, f, g = drotg ( f, g )
        s[k] = f
        f = cs * e[k] + sn * s[k+1]
        s[k+1] = - sn * e[k] + cs * s[k+1]
        g = sn * e[k+1]
        e[k+1] = cs * e[k+1]

        if ( wantu and k < m ):
          u1, u2 = drot ( m, u[0:m,k], 1, u[0:m,k+1], 1, cs, sn )
          for i in range ( 0, m ):
            u[i,k] = u1[i]
            u[i,k+1] = u2[i]

      e[mn-2] = f

      iter = iter + 1
#
#  Convergence.
#
    elif ( kase == 4 ):
#
#  Make the singular value nonnegative.
#
      if ( s[l] < 0.0 ):
        s[l] = - s[l]
        if ( wantv ):
          for i in range ( 0, n ):
            v[i,l] = - v[i,l]
#
#  Order the singular values.
#
      while ( True ):

        if ( l + 1 == mm ):
          break

        if ( s[l+1] <= s[l] ):
          break

        t = s[l]
        s[l] = s[l+1]
        s[l+1] = t

        if ( wantv and l < n - 1 ):
          for i in range ( 0, n ):
            t = v[i,l]
            v[i,l] = v[i,l+1]
            v[i,l+1] = t
 
        if ( wantu and l < m - 1 ):
          for i in range ( 0, m ):
            t = u[i,l]
            u[i,l] = u[i,l+1]
            u[i,l+1] = t
 
        l = l + 1

      iter = 0
      mn = mn - 1

  return a, s, e, u, v, info

def dsvdc_test ( ):

#*****************************************************************************80
#
## dsvdc_test() tests dsvdc().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 6
  n = 4

  print ( '' )
  print ( 'dsvdc_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  dsvdc computes the singular value decomposition' )
  print ( '  for an MxN matrix A in general storage.' )
  print ( '    A = U * S * V\'' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )
#
#  Set A.
#
  a = np.random.rand ( m, n )

  r8mat_print ( m, n, a, '  The matrix A:' )
#
#  Decompose the matrix.
#
  print ( '' )
  print ( '  Decompose the matrix.' )

  job = 11
  lda = m
  ldu = m
  ldv = n

  a, s, e, u, v, info = dsvdc ( a, lda, m, n, ldu, ldv, job )

  if ( info != 0 ):
    print ( '' )
    print ( 'dsvdc_test - Warning:' )
    print ( '  dsvdc returned nonzero INFO = %d' % ( info ) )
#   return

  r8vec_print ( min ( m, n ), s, '  Singular values S:' )

  r8mat_print ( m, m, u, '  Left Singular Vector Matrix U:' )

  r8mat_print ( n, n, v, '  Right Singular Vector Matrix V:' )

  sigma = np.zeros ( [ m, n ] )

  for i in range ( 0, min ( m, n ) ):
    sigma[i,i] = s[i]

  usv = np.dot ( u, np.dot ( sigma, v.transpose ( ) ) )

  r8mat_print ( m, n, usv, '  The product U * S * V\' (should equal A):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'dsvdc_test' )
  print ( '  Normal end of execution.' )
  return

def lstsq_solve_test ( ):

#*****************************************************************************80
#
## lstsq_solve_test() tests the numpy.linalg.lstsq() operator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lstsq_solve_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  The function x=np.linalg.lstsq(A,b)\n' )
  print ( '  solves a linear system A*x = b in the least squares sense.' )
  print ( '  Compare a tabulated solution X1 to the LSTSQ result X2.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = %d' % ( prob_num ) )
  print ( '' )
  print ( '  Index     M     N          ||B||   ||X1 - X2||' ),
  print ( '        ||X1||        ||X2||         ||R1||        ||R2||' )
  print ( '' )

  for prob in range ( 1, prob_num + 1 ):
#
#  Get problem size.
#
    m = p00_m ( prob )
    n = p00_n ( prob )
#
#  Retrieve problem data.
#
    a = p00_a ( prob, m, n )
    b = p00_b ( prob, m )
    x1 = p00_x ( prob, n )

    b_norm = np.linalg.norm ( b )
    x1_norm = np.linalg.norm ( x1 )
    r1 = np.dot ( a, x1 ) - b
    r1_norm = np.linalg.norm ( r1 )
#
#  Use NUMPY's LINALG.LSTSQ on the problem.
#
    x2, r, rank, s = np.linalg.lstsq ( a, b, rcond = None )

    x2_norm = np.linalg.norm ( x2 )
    r2 = np.dot ( a, x2 ) - b
    r2_norm = np.linalg.norm ( r2 )
#
#  Compare tabulated and computed solutions.
#
    x_diff_norm = np.linalg.norm ( x1 - x2 )
#
#  Report results for this problem.
#
    print ( '  %5d  %4d  %4d' % ( prob, m, n ), end = '' )
    print ( '  %12.4g  %12.4g' % ( b_norm, x_diff_norm ), end = '' )
    print ( '  %12.4g  %12.4g' % ( x1_norm, x2_norm ), end = '' )
    print ( '  %12.4g  %12.4g' % ( r1_norm, r2_norm ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'lstsq_solve_test' )
  print ( '  Normal end of execution.' )
  return

def normal_solve ( m, n, a, b ):

#*****************************************************************************80
#
## normal_solve() solves a linear system using the normal equations.
#
#  Discussion:
#
#    Given a presumably rectangular MxN system of equations A*x=b, this routine
#    sets up the NxN system A'*A*x=A'b.  Assuming N <= M, and that A has full
#    column rank, the system will be solvable, and the vector x that is returned
#    will minimize the Euclidean norm of the residual.
#
#    One drawback to this approach is that the condition number of the linear
#    system A'*A is effectively the square of the condition number of A, 
#    meaning that there is a substantial loss of accuracy.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    integer M, the number of rows of A.
#
#    integer N, the number of columns of A.
#    It must be the case that N <= M.
#
#    real A(M,N), the matrix.
#    The matrix must have full column rank.
#
#    real B(M), the right hand side.
#
#  Output:
#
#    real X(N), the least squares solution.
#
#    integer FLAG,
#    0, no error was detected.
#    1, an error occurred.
#
  import numpy as np

  flag = False

  x = np.zeros ( n )

  if ( m < n ):

    flag = True

  else:

    ata = np.dot ( a.transpose ( ), a )

    atb = np.dot ( a.transpose ( ), b )

    ata_c, flag = r8mat_cholesky_factor ( n, ata )

    if ( not flag ):

      x = r8mat_cholesky_solve ( n, ata_c, atb )

  return x, flag
 
def normal_solve_test ( ):

#*****************************************************************************80
#
## normal_solve_test() tests normal_solve().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'normal_solve_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  normal_solve is a function with a simple interface which' )
  print ( '  solves a linear system A*x = b in the least squares sense.' )
  print ( '  Compare a tabulated solution X1 to the normal_solve result X2.' )
  print ( '' )
  print ( '  normal_solve cannot be applied when N < M,' )
  print ( '  or if the matrix does not have full column rank.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = %d' % ( prob_num ) )
  print ( '' )
  print ( '  Index     M     N          ||B||   ||X1 - X2||' ),
  print ( '        ||X1||        ||X2||         ||R1||        ||R2||' )
  print ( '' )

  for prob in range ( 1, prob_num + 1 ):
#
#  Get problem size.
#
    m = p00_m ( prob )
    n = p00_n ( prob )
#
#  Retrieve problem data.
#
    a = p00_a ( prob, m, n )
    b = p00_b ( prob, m )
    x1 = p00_x ( prob, n )

    b_norm = np.linalg.norm ( b )
    x1_norm = np.linalg.norm ( x1 )
    r1 = np.dot ( a, x1 ) - b
    r1_norm = np.linalg.norm ( r1 )
#
#  Use normal_solve on the problem.
#
    x2, flag = normal_solve ( m, n, a, b )

    if ( flag ):

      print ( '  %5d  %4d  %4d' % ( prob, m, n ) ),
      print ( '  %12.4g  ------------' % ( b_norm ) ),
      print ( '  %12.4g  ------------' % ( x1_norm ) ),
      print ( '  %12.4g  ------------' % ( r1_norm ) )

    else:

      x2_norm = np.linalg.norm ( x2 )
      r2 = np.dot ( a, x2 ) - b
      r2_norm = np.linalg.norm ( r2 )
#
#  Compare tabulated and computed solutions.
#
      x_diff_norm = np.linalg.norm ( x1 - x2 )
#
#  Report results for this problem.
#
      print ( '  %5d  %4d  %4d' % ( prob, m, n ) ),
      print ( '  %12.4g  %12.4g' % ( b_norm, x_diff_norm ) ),
      print ( '  %12.4g  %12.4g' % ( x1_norm, x2_norm ) ),
      print ( '  %12.4g  %12.4g' % ( r1_norm, r2_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'normal_solve_test' )
  print ( '  Normal end of execution.' )
  return

def qr_solve ( m, n, a, b ):

#*****************************************************************************80
#
## qr_solve() solves a linear system in the least squares sense.
#
#  Discussion:
#
#    If the matrix A has full column rank, then the solution X should be the
#    unique vector that minimizes the Euclidean norm of the residual.
#
#    If the matrix A does not have full column rank, then the solution is
#    not unique; the vector X will minimize the residual norm, but so will
#    various other vectors.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    integer M, the number of rows of A.
#
#    integer N, the number of columns of A.
#
#    real A(M,N), the matrix.
#
#    real B(M), the right hand side.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  lda = m
  eps = 2.220446049250313E-016

  tol = 0.0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      tol = max ( tol, abs ( a[i,j] ) )
  tol = eps / tol
#
#  Factor the matrix.
#
  kr, jpvt, qraux, a = dqrank ( a, lda, m, n, tol )
#
#  Solve the least-squares problem.
#
  x, r = dqrlss ( a, lda, m, n, kr, b, jpvt, qraux )

  return x

def qr_solve_test ( ):

#*****************************************************************************80
#
## qr_solve_test() tests qr_solve().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'qr_solve_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  qr_solve is a function with a simple interface which' )
  print ( '  solves a linear system A*x = b in the least squares sense.' )
  print ( '  Compare a tabulated solution X1 to the qr_solve result X2.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = %d' % ( prob_num ) )
  print ( '' )
  print ( '  Index     M     N          ||B||   ||X1 - X2||' ),
  print ( '        ||X1||        ||X2||         ||R1||        ||R2||' )
  print ( '' )

  for prob in range ( 1, prob_num + 1 ):
#
#  Get problem size.
#
    m = p00_m ( prob )
    n = p00_n ( prob )
#
#  Retrieve problem data.
#
    a = p00_a ( prob, m, n )
    b = p00_b ( prob, m )
    x1 = p00_x ( prob, n )

    b_norm = np.linalg.norm ( b )
    x1_norm = np.linalg.norm ( x1 )
    r1 = np.dot ( a, x1 ) - b
    r1_norm = np.linalg.norm ( r1 )
#
#  Use qr_solve on the problem.
#  Since we want to compute residuals ourselves, we need
#  to keep the originals of A and B, so we make copies
#  to send to qr_solve.
#
    a_qr = a.copy ( )
    b_qr = b.copy ( )
    x2 = qr_solve ( m, n, a_qr, b_qr )

    x2_norm = np.linalg.norm ( x2 )
    r2 = np.dot ( a, x2 ) - b
    r2_norm = np.linalg.norm ( r2 )
#
#  Compare tabulated and computed solutions.
#
    x_diff_norm = np.linalg.norm ( x1 - x2 )
#
#  Report results for this problem.
#
    print ( '  %5d  %4d  %4d' % ( prob, m, n ) ),
    print ( '  %12.4g  %12.4g' % ( b_norm, x_diff_norm ) ),
    print ( '  %12.4g  %12.4g' % ( x1_norm, x2_norm ) ),
    print ( '  %12.4g  %12.4g' % ( r1_norm, r2_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'qr_solve_test' )
  print ( '  Normal end of execution.' )
  return

def qr_solve_tests ( ):

#*****************************************************************************80
#
## qr_solve_tests() tests qr_solve().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 September 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'qr_solve_testS' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the qr_solve library.' )

  lstsq_solve_test ( )
  normal_solve_test ( )
  qr_solve_test ( )
  svd_solve_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'qr_solve_tests' )
  print ( '  Normal end of execution.' )
  return

def r8mat_cholesky_factor ( n, a ):

#*****************************************************************************80
#
## r8mat_cholesky_factor() computes the Cholesky factor of a symmetric matrix.
#
#  Discussion:
#
#    The matrix must be symmetric and positive semidefinite.
#
#    For a positive semidefinite symmetric matrix A, the Cholesky factorization
#    is a lower triangular matrix L such that:
#
#      A = L * L'
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix A.
#
#    real A(N,N), the matrix.
#
#  Output:
#
#    real C(N,N), the N by N lower triangular Cholesky factor.
#
#    bool FLAG:
#    False, no error occurred.
#    True, the matrix is not positive definite.
#
  import numpy as np

  flag = False

  c = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      c[i,j] = a[i,j]

  for j in range ( 0, n ):

    c[0:j,j] = 0.0

    for i in range ( j, n ):

      sum2 = c[j,i]
      for k in range ( 0, j ):
        sum2 = sum2 - c[j,k] * c[i,k]

      if ( i == j ):
        if ( sum2 <= 0.0 ):
          flag = True
          return c, flag
        else:
          c[i,j] = np.sqrt ( sum2 )
      else:
        if ( c[j,j] != 0.0 ):
          c[i,j] = sum2 / c[j,j]
        else:
          c[i,j] = 0.0

  return c, flag

def r8mat_cholesky_factor_test ( ):

#*****************************************************************************80
#
## r8mat_cholesky_factor_test() tests r8mat_cholesky_factor().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8mat_cholesky_factor_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_cholesky_factor determines the' )
  print ( '  lower triangular Cholesky factorization' )
  print ( '  of a positive definite symmetric matrix,' )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( j == i - 1 or j == i + 1 ):
        a[i,j] = -1.0

  r8mat_print ( n, n, a, '  Matrix to be factored:' )
#
#  Compute a Cholesky factor.
#
  l, flag = r8mat_cholesky_factor ( n, a )
  r8mat_print ( n, n, l, '  Cholesky factor L:' )
  d = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, d, '  Product L * L\':' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_cholesky_factor_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_cholesky_solve ( n, l, b ):

#*****************************************************************************80
#
## r8mat_cholesky_solve() solves a Cholesky factored linear system A * x = b.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix A.
#
#    real L(N,N), the N by N Cholesky factor of the
#    system matrix A.
#
#    real B(N), the right hand side of the linear system.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#

#
#  Solve L * y = b.
#
  x = r8mat_l_solve ( n, l, b )
#
#  Solve L' * x = y.
#
  x = r8mat_lt_solve ( n, l, x )

  return x

def r8mat_cholesky_solve_test ( ):

#*****************************************************************************80
#
## r8mat_cholesky_solve_test() tests r8mat_cholesky_solve().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8mat_cholesky_solve_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_cholesky_solve solves a linear system' )
  print ( '  using the lower triangular Cholesky factorization,' )
  print ( '  for a positive definite symmetric matrix.' )
  
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( j == i - 1 or j == i + 1 ):
        a[i,j] = -1.0

  r8mat_print ( n, n, a, '  Matrix to be factored:' )
#
#  Compute a Cholesky factor.
#
  l, flag = r8mat_cholesky_factor ( n, a )
  r8mat_print ( n, n, l, '  Cholesky factor L:' )
  d = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, d, '  Product L * L\':' )
#
#  Solve a linear system.
#
  b = np.zeros ( n )
  b[n-1] = float ( n + 1 )
  r8vec_print ( n, b, '  Right hand side b:' )
  x = r8mat_cholesky_solve ( n, l, b )

  r8vec_print ( n, x, '  Computed solution x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_cholesky_solve_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_l_solve ( n, a, b ):

#*****************************************************************************80
#
## r8mat_l_solve() solves a lower triangular linear system.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of
#    the matrix A.
#
#    real A(N,N), the N by N lower triangular matrix.
#
#    real B(N), the right hand side of the linear system.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
  import numpy as np

  x = np.zeros ( n )
#
#  Solve L * x = b.
#
  for i in range ( 0, n ):
    x[i] = b[i]
    for j in range ( 0, i ):
      x[i] = x[i] - a[i,j] * x[j]
    x[i] = x[i] / a[i,i]

  return x

def r8mat_l_solve_test ( ):

#*****************************************************************************80
#
## r8mat_l_solve_test() tests r8mat_l_solve().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  a = np.array ( [ \
    [ 1.0,  0.0,  0.0,  0.0 ], \
    [ 2.0,  3.0,  0.0,  0.0 ], \
    [ 4.0,  5.0,  6.0,  0.0 ], \
    [ 7.0,  8.0,  9.0, 10.0 ] ] )

  b = np.array ( [ 1.0, 8.0, 32.0, 90.0 ] )

  print ( '' )
  print ( 'r8mat_l_solve_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_l_solve solves a lower triangular system.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  r8vec_print ( n, b, '  Right hand side b:' )

  x = r8mat_l_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( a, x ) - b

  rnorm = np.linalg.norm ( r )

  print ( '' )
  print ( '  Norm of A*x-b = %g' % ( rnorm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_l_solve_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_lt_solve ( n, a, b ):

#*****************************************************************************80
#
## r8mat_lt_solve() solves a transposed lower triangular linear system.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
#
#    Given the lower triangular matrix A, the linear system to be solved is:
#
#      A' * x = b
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns
#    of the matrix.
#
#    real A(N,N), the N by N lower triangular matrix.
#
#    real B(N,1), the right hand side of the linear system.
#
#  Output:
#
#    real X(N,1), the solution of the linear system.
#
  import numpy as np
#
#  Solve U' * x = b.
#
  x = np.zeros ( n )

  for i in range ( n - 1, -1, -1 ):
    x[i] = b[i]
    for j in range ( i + 1, n ):
      x[i] = x[i] - a[j,i] * x[j]
    x[i] = x[i] / a[i,i]

  return x

def r8mat_lt_solve_test ( ):

#*****************************************************************************80
#
## r8mat_lt_solve_test() tests r8mat_lt_solve().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  a = np.array ( [ \
    [ 1.0,  0.0,  0.0,  0.0 ], \
    [ 2.0,  3.0,  0.0,  0.0 ], \
    [ 4.0,  5.0,  6.0,  0.0 ], \
    [ 7.0,  8.0,  9.0, 10.0 ] ] )

  b = np.array ( [ 45.0, 53.0, 54.0, 40.0 ] )

  print ( '' )
  print ( 'r8mat_lt_solve_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_lt_solve solves a transposed lower triangular system.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  r8vec_print ( n, b, '  Right hand side b:' )

  x = r8mat_lt_solve ( n, a, b )

  r8vec_print ( n, x, '  Computed solution x:' )

  r = np.dot ( np.transpose ( a ), x ) - b

  rnorm = np.linalg.norm ( r )

  print ( '' )
  print ( '  Norm of A\'*x-b = %g' % ( rnorm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_lt_solve_test' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## r8mat_print_test() tests r8mat_print().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_print prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_print_test:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_print_some_test() tests r8mat_print_some().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_print_some_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_print_some prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8mat_print_some_test:' )
  print ( '  Normal end of execution.' )
  return

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop() returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real VALUE, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## r8_mop_test() tests r8_mop().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_mop_test' )
  print ( '  r8_mop evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_mop(I4)' )
  print ( '' )

  i4_min = -100;
  i4_max = +100;

  for test in range ( 0, 10 ):
    i4 = np.random.random_integers ( i4_min, i4_max )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_mop_test' )
  print ( '  Normal end of execution.' )
  return

def r8_sign ( x ):

#*****************************************************************************80
#
## r8_sign() returns the sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose sign is desired.
#
#  Output:
#
#    real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  else:
    value = +1.0
 
  return value

def r8_sign_test ( ):

#*****************************************************************************80
#
## r8_sign_test() tests r8_sign().
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

  test_num = 5

  r8_test = np.array ( [ -1.25, -0.25, 0.0, +0.5, +9.0 ] )

  print ( '' )
  print ( 'r8_sign_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sign returns the sign of an R8.' )
  print ( '' )
  print ( '     R8     r8_sign(R8)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_test[test]
    s = r8_sign ( r8 )
    print ( '  %8.4f  %8.0f' % ( r8, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_sign_test' )
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
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_print prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_print_test:' )
  print ( '  Normal end of execution.' )
  return

def svd_solve ( m, n, a, b ):

#*****************************************************************************80
#
## svd_solve() solves a linear system in the least squares sense.
#
#  Discussion:
#
#    The vector X returned by this routine should always minimize the 
#    Euclidean norm of the residual ||A*x-b||.
#
#    If the matrix A does not have full column rank, then there are multiple
#    vectors that attain the minimum residual.  In that case, the vector
#    X returned by this routine is the unique such minimizer that has the 
#    the minimum possible Euclidean norm, that is, ||A*x-b|| and ||x||
#    are both minimized.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    integer M, the number of rows of A.
#
#    integer N, the number of columns of A.
#
#    real A(M,N), the matrix.
#
#    real B(M), the right hand side.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np
#
#  Get the SVD.
#
  a_copy = a
  lda = m
  ldu = m
  ldv = n
  job = 11

  a_copy, sdiag, e, u, v, info = dsvdc ( a_copy, lda, m, n, ldu, ldv, job )

  if ( info != 0 ):
    print ( '' )
    print ( 'svd_solve - Fatal error!' )
    print ( '  The SVD could not be calculated.' )
    print ( '  LINPACK routine dsvdc returned a nonzero' )
    print ( '  value of the error flag, INFO = %d' % ( info ) )
    raise Exception ( 'svd_solve - Fatal error!' )

  ub = np.dot ( u.transpose ( ), b )

  sub = np.zeros ( n )
#
#  For singular problems, there may be tiny but nonzero singular values
#  that should be ignored.  This is a reasonable attempt to avoid such 
#  problems, although in general, the user might wish to control the tolerance.
#
  smax = max ( sdiag )
  eps = 2.220446049250313E-016
  if ( smax <= eps ):
    smax = 1.0

  stol = eps * smax

  for i in range ( 0, n ):
    if ( i <= m ):
      if ( stol <= sdiag[i] ):
        sub[i] = ub[i] / sdiag[i]

  x = np.dot ( v, sub )

  return x

def svd_solve_test ( ):

#*****************************************************************************80
#
## svd_solve_test() tests svd_solve().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'svd_solve_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  svd_solve is a function with a simple interface which' )
  print ( '  solves a linear system A*x = b in the least squares sense' )
  print ( '  using the singular value decomposition (SVD).' )
  print ( '  Compare a tabulated solution X1 to the qr_solve result X2.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = %d' % ( prob_num ) )
  print ( '' )
  print ( '  Index     M     N          ||B||   ||X1 - X2||' ),
  print ( '        ||X1||        ||X2||         ||R1||        ||R2||' )
  print ( '' )

  for prob in range ( 1, prob_num + 1 ):
#
#  Get problem size.
#
    m = p00_m ( prob )
    n = p00_n ( prob )
#
#  Retrieve problem data.
#
    a = p00_a ( prob, m, n )
    b = p00_b ( prob, m )
    x1 = p00_x ( prob, n )

    b_norm = np.linalg.norm ( b )
    x1_norm = np.linalg.norm ( x1 )
    r1 = np.dot ( a, x1 ) - b
    r1_norm = np.linalg.norm ( r1 )
#
#  Use svd_solve on the problem.
#  Since we want to compute residuals ourselves, we need
#  to keep the originals of A and B, so we make copies
#  to send to svd_solve.
#
    a_qr = a.copy ( )
    b_qr = b.copy ( )
    x2 = svd_solve ( m, n, a_qr, b_qr )

    x2_norm = np.linalg.norm ( x2 )
    r2 = np.dot ( a, x2 ) - b
    r2_norm = np.linalg.norm ( r2 )
#
#  Compare tabulated and computed solutions.
#
    x_diff_norm = np.linalg.norm ( x1 - x2 )
#
#  Report results for this problem.
#
    print ( '  %5d  %4d  %4d' % ( prob, m, n ) ),
    print ( '  %12.4g  %12.4g' % ( b_norm, x_diff_norm ) ),
    print ( '  %12.4g  %12.4g' % ( x1_norm, x2_norm ) ),
    print ( '  %12.4g  %12.4g' % ( r1_norm, r2_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'svd_solve_test' )
  print ( '  Normal end of execution.' )
  return

def p00_a ( prob, m, n ):

#*****************************************************************************80
#
## p00_a() returns the matrix A for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  if ( prob == 1 ):
    a = p01_a ( m, n )
  elif ( prob == 2 ):
    a = p02_a ( m, n )
  elif ( prob == 3 ):
    a = p03_a ( m, n )
  elif ( prob == 4 ):
    a = p04_a ( m, n )
  elif ( prob == 5 ):
    a = p05_a ( m, n )
  elif ( prob == 6 ):
    a = p06_a ( m, n )
  else:
    print ( '' )
    print ( 'p00_a - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    raise Exception ( 'p00_a - Fatal error!' )

  return a

def p00_b ( prob, m ):

#*****************************************************************************80
#
## p00_b() returns the right hand side B for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  if ( prob == 1 ):
    b = p01_b ( m )
  elif ( prob == 2 ):
    b = p02_b ( m )
  elif ( prob == 3 ):
    b = p03_b ( m )
  elif ( prob == 4 ):
    b = p04_b ( m )
  elif ( prob == 5 ):
    b = p05_b ( m )
  elif ( prob == 6 ):
    b = p06_b ( m )
  else:
    print ( '' )
    print ( 'p00_b - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    raise Exception ( 'p00_b - Fatal error!' )

  return b

def p00_m ( prob ):

#*****************************************************************************80
#
## p00_m() returns the number of equations M for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#  Output:
#
#    integer M, the number of equations.
#
  if ( prob == 1 ):
    m = p01_m ( )
  elif ( prob == 2 ):
    m = p02_m ( )
  elif ( prob == 3 ):
    m = p03_m ( )
  elif ( prob == 4 ):
    m = p04_m ( )
  elif ( prob == 5 ):
    m = p05_m ( )
  elif ( prob == 6 ):
    m = p06_m ( )
  else:
    print ( '' )
    print ( 'p00_m - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    raise Exception ( 'p00_m - Fatal error!' )

  return m

def p00_n ( prob ):

#*****************************************************************************80
#
## p00_n() returns the number of variables N for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#  Output:
#
#    integer N, the number of variables.
#
  if ( prob == 1 ):
    n = p01_n ( )
  elif ( prob == 2 ):
    n = p02_n ( )
  elif ( prob == 3 ):
    n = p03_n ( )
  elif ( prob == 4 ):
    n = p04_n ( )
  elif ( prob == 5 ):
    n = p05_n ( )
  elif ( prob == 6 ):
    n = p06_n ( )
  else:
    print ( '' )
    print ( 'p00_n - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    raise Exception ( 'p00_n - Fatal error!' )

  return n

def p00_prob_num ( ):

#*****************************************************************************80
#
## p00_prob_num() returns the number of least squares problems.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real prob_num, the number of problems.
#
  prob_num = 6

  return prob_num

def p00_x ( prob, n ):

#*****************************************************************************80
#
## p00_x() returns the least squares solution X for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  if ( prob == 1 ):
    x = p01_x ( n )
  elif ( prob == 2 ):
    x = p02_x ( n )
  elif ( prob == 3 ):
    x = p03_x ( n )
  elif ( prob == 4 ):
    x = p04_x ( n )
  elif ( prob == 5 ):
    x = p05_x ( n )
  elif ( prob == 6 ):
    x = p06_x ( n )
  else:
    print ( '' )
    print ( 'p00_x - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    raise Exception ( 'p00_x - Fatal error!' )

  return x

def p01_a ( m, n ):

#*****************************************************************************80
#
## p01_a() returns the matrix A for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    a[i,0] = 1.0
    for j in range ( 1, n ):
      a[i,j] = a[i,j-1] * float ( i + 1 )

  return a

def p01_b ( m ):

#*****************************************************************************80
#
## p01_b() returns the right hand side B for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 1.0, 2.3, 4.6, 3.1, 1.2 ] )

  return b

def p01_m ( ):

#*****************************************************************************80
#
## p01_m() returns the number of equations M for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 5

  return m

def p01_n ( ):

#*****************************************************************************80
#
## p01_n() returns the number of variables N for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 3

  return n

def p01_x ( n ):

#*****************************************************************************80
#
## p01_x() returns the least squares solution X for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ -3.0200000, 4.4914286, -0.72857143 ] )

  return x

def p02_a ( m, n ):

#*****************************************************************************80
#
## p02_a() returns the matrix A for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625,
#    ebook: https://www.mathworks.com/moler/chapters.html
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    integer N, the number of variables.
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    a[i,n-1] = 1.0
    for j in range ( n - 2, -1, -1 ):
      a[i,j] = a[i,j+1] * float ( i ) / 5.0

  return a

def p02_b ( m ):

#*****************************************************************************80
#
## p02_b() returns the right hand side B for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 150.697, 179.323, 203.212, 226.505, 249.633, 281.422 ] )

  return b

def p02_m ( ):

#*****************************************************************************80
#
## p02_m() returns the number of equations M for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 6

  return m

def p02_n ( ):

#*****************************************************************************80
#
## p02_n() returns the number of variables N for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 3

  return n

def p02_x ( n ):

#*****************************************************************************80
#
## p02_x() returns the least squares solution X for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ 5.7013, 121.1341, 152.4745 ] )

  return x

def p03_a ( m, n ):

#*****************************************************************************80
#
## p03_a() returns the matrix A for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625,
#    ebook: https://www.mathworks.com/moler/chapters.html
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  a = np.array ( [ \
       [  1.0,  2.0,  3.0 ], \
       [  4.0,  5.0,  6.0 ], \
       [  7.0,  8.0,  9.0 ], \
       [ 10.0, 11.0, 12.0 ], \
       [ 13.0, 14.0, 15.0 ] ] )

  return a

def p03_b ( m ):

#*****************************************************************************80
#
## p03_b() returns the right hand side B for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 16.0, 17.0, 18.0, 19.0, 20.0 ] )

  return b

def p03_m ( ):

#*****************************************************************************80
#
## p03_m() returns the number of equations M for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 5

  return m

def p03_n ( ):

#*****************************************************************************80
#
## p03_n() returns the number of variables N for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 3

  return n

def p03_x ( n ):

#*****************************************************************************80
#
## p03_x() returns the least squares solution X for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ -7.5555556, 0.1111111, 7.7777778 ] )

  return x

def p04_a ( m, n ):

#*****************************************************************************80
#
## p04_a() returns the matrix A for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = float ( j + 1 ) ** i

  return a

def p04_b ( m ):

#*****************************************************************************80
#
## p04_b() returns the right hand side B for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 15.0, 55.0, 225.0 ] )

  return b

def p04_m ( ):

#*****************************************************************************80
#
## p04_m() returns the number of equations M for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 3

  return m

def p04_n ( ):

#*****************************************************************************80
#
## p04_n() returns the number of variables N for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 5

  return n

def p04_x ( n ):

#*****************************************************************************80
#
## p04_x() returns the least squares solution X for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )

  return x

def p05_a ( m, n ):

#*****************************************************************************80
#
## p05_a() returns the matrix A for problem 5.
#
#  Discussion:
#
#    A is the Hilbert matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = 1.0 / float ( i + j + 1 )

  return a

def p05_b ( m ):

#*****************************************************************************80
#
## p05_b() returns the right hand side B for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.zeros ( m )

  b[0] = 1.0

  return b

def p05_m ( ):

#*****************************************************************************80
#
## p05_m() returns the number of equations M for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 10

  return m

def p05_n ( ):

#*****************************************************************************80
#
## p05_n() returns the number of variables N for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 10

  return n

def p05_x ( n ):

#*****************************************************************************80
#
## p05_x() returns the least squares solution X for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  from scipy.special import comb
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = r8_mop ( i + 2 ) * float ( i + 1 ) \
      * comb ( n + i, n - 1 ) * comb ( n, n - i - 1 )

  return x

def p06_a ( m, n ):

#*****************************************************************************80
#
## p06_a() returns the matrix A for problem 6.
#
#  Discussion:
#
#    A is a symmetric, orthogonal matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#    integer N, the number of variables.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      angle = float ( i + 1 ) * float ( j + 1 ) * np.pi / float ( n + 1 )
      a[i,j] = np.sin ( angle )

  a[0:m,0:n] = a[0:m,0:n] * np.sqrt ( 2.0 / ( n + 1 ) )

  return a

def p06_b ( m ):

#*****************************************************************************80
#
## p06_b() returns the right hand side B for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of equations.
#
#  Output:
#
#    real B(M), the right hand side.
#
  import numpy as np

  b = np.zeros ( m )

  b[0] = 1.0

  return b

def p06_m ( ):

#*****************************************************************************80
#
## p06_m() returns the number of equations M for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the number of equations.
#
  m = 10

  return m

def p06_n ( ):

#*****************************************************************************80
#
## p06_n() returns the number of variables N for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables.
#
  n = 10

  return n

def p06_x ( n ):

#*****************************************************************************80
#
## p06_x() returns the least squares solution X for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#  Output:
#
#    real X(N), the least squares solution.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    x[i] = np.sin ( angle )

  x[0:n] = x[0:n] * np.sqrt ( 2.0 / float ( n + 1) )

  return x

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop() returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real VALUE, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## r8_mop_test() tests r8_mop().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8_mop_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_mop evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_mop(I4)' )
  print ( '' )

  i4_min = -100
  i4_max = +100

  for test in range ( 0, 10 ):
    i4 = np.random.random_integers ( i4_min, i4_max )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8_mop_test' )
  print ( '  Normal end of execution.' )
  return

def test_ls_test ( ):

#*****************************************************************************80
#
## test_ls_test() tests test_ls().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'test_ls_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test test_ls.' )

  ls_data_test ( )
  lstsq_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_ls_test' )
  print ( '  Normal end of execution.' )
  return

def lstsq_test ( ):

#*****************************************************************************80
#
## lstsq_test() tests the NUMPY LINALG least squares solver on the data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lstsq_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LSTSQ is the NUMPY LINALG least squares solver.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = %d' % ( prob_num ) )
  print ( '' )
  print ( '  Index     M     N         ||B||     ||X1-X2||         ||X1|| ' ),
  print ( '       ||X2||        ||R1||        ||R2||' )
  print ( '' )

  for prob in range ( 1, prob_num ):

    m = p00_m ( prob )
    n = p00_n ( prob )

    a = p00_a ( prob, m, n )
    b = p00_b ( prob, m )
    x1 = p00_x ( prob, n )

    r1 = np.dot ( a, x1 ) - b

    b_norm = np.linalg.norm ( b )
    x1_norm = np.linalg.norm ( x1 )
    r1_norm = np.linalg.norm ( r1 )

    [ x2, resids, rank, s ] = np.linalg.lstsq ( a, b )
    r2 = np.dot ( a, x2 ) - b
    x2_norm = np.linalg.norm ( x2 )
    r2_norm = np.linalg.norm ( r2 )

    x_diff_norm = np.linalg.norm ( x1 - x2 )

    print ( '  %5d  %4d  %4d  %12.4g  %12.4g  %12.4g  %12.4g  %12.4g  %12.4g' \
      % ( prob, m, n, b_norm, x_diff_norm, x1_norm, x2_norm, r1_norm, r2_norm ) )

  return

def ls_data_test ( ):

#*****************************************************************************80
#
## ls_data_test() summarizes the test data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ls_data_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Get each least squares test and compute the maximum residual.' )
  print ( '  The L2 norm of the residual MUST be no greater than' )
  print ( '  the L2 norm of the right hand side, else 0 is a better solution.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = %d' % ( prob_num ) )
  print ( '' )
  print ( '  Index     M     N         ||B||         ||X||         ||R||' )
  print ( '' )

  for prob in range ( 1, prob_num + 1 ):

    m = p00_m ( prob )
    n = p00_n ( prob )

    a = p00_a ( prob, m, n )
    b = p00_b ( prob, m )
    x = p00_x ( prob, n )

    r = np.dot ( a, x ) - b

    b_norm = np.linalg.norm ( b )
    x_norm = np.linalg.norm ( x )
    r_norm = np.linalg.norm ( r )

    print ( '  %5d  %4d  %4d  %12.4g  %12.4g  %12.4g' \
      % ( prob, m, n, b_norm, x_norm, r_norm ) )

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
  qr_solve_tests ( )
  timestamp ( )

