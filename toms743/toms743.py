#! /usr/bin/env python3
#
def bisect ( xx, nb, l ):

#*****************************************************************************80
#
## bisect() approximates the W function using bisection.
#
#  Discussion:
#
#    The parameter TOL, which determines the accuracy of the bisection
#    method, is calculated using NBITS (assuming the final bit is lost
#    due to rounding error).
#
#    N0 is the maximum number of iterations used in the bisection
#    method.
#
#    For XX close to 0 for Wp, the exponential approximation is used.
#    The approximation is exact to O(XX^8) so, depending on the value
#    of NBITS, the range of application of this formula varies. Outside
#    this range, the usual bisection method is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2020
#
#  Author:
#
#    Original FORTRAN77 version by Andrew Barry, S. J. Barry, 
#    Patricia Culligan-Hensley.
#    This MATLAB version by John Burkardt.
#
#  Reference:
#
#    Andrew Barry, S. J. Barry, Patricia Culligan-Hensley,
#    Algorithm 743: WAPR - A Fortran routine for calculating real 
#    values of the W-function,
#    ACM Transactions on Mathematical Software,
#    Volume 21, Number 2, June 1995, pages 172-181.
#
#  Input:
#
#    real XX, the argument.
#
#    integer NB, indicates the branch of the W function.
#    0, the upper branch
#    nonzero, the lower branch.
#
#    integer L, the offset indicator.
#    1, XX represents the offset of the argument from -exp(-1).
#    not 1, XX is the actual argument.
#
#  Output:
#
#    real VALUE, the value of W(X), as determined
#
#    integer NER, the error flag.
#    0, success
#    1, the routine did not converge.  Perhaps reduce NBITS and try again.
#
  import numpy as np

  value = 0.0
  ner = 0

  n0 = 500
  nbits = 52

  if ( l == 1 ):
    x = xx - np.exp ( -1.0 )
  else:
    x = xx

  if ( nb == 0 ):

    test = 1.0 / ( 2.0 ** nbits ) ** ( 1.0 / 7.0 )

    if ( abs ( x ) < test ):

      value = x \
        * np.exp ( - x \
        * np.exp ( - x \
        * np.exp ( - x \
        * np.exp ( - x \
        * np.exp ( - x \
        * np.exp ( - x ))))))

      return value, ner

    else:

      u = crude ( x, nb ) + 0.001
      tol = abs ( u ) / 2.0 ** nbits
      d = max ( u - 0.002, -1.0 )

      for i in range ( 0, n0 ):

        r = 0.5 * ( u - d )
        value = d + r
#
#  Find root using w*exp(w)-x to avoid ln(0) error.
#
        if ( x < np.exp ( 1.0 ) ):

          f = value * np.exp ( value ) - x
          fd = d * np.exp ( d ) - x
#
#  Find root using ln(w/x)+w to avoid overflow error.
#
        else:

          f = np.log ( value / x ) + value
          fd = np.log ( d / x ) + d

        if ( f == 0.0 ):
          return value, ner

        if ( abs ( r ) <= tol ):
          return value, ner

        if ( 0.0 < fd * f ):
          d = value
        else:
          u = value

  else:

    d = crude ( x, nb ) - 0.001
    u = min ( d + 0.002, -1.0 )
    tol = abs ( u ) / 2.0 ** nbits

    for i in range ( 0, n0 ):

      r = 0.5 * ( u - d )
      value = d + r
      f = value * np.exp ( value ) - x

      if ( f == 0.0 ):
        return value, ner

      if ( abs ( r ) <= tol ):
        return value, ner

      fd = d * np.exp ( d ) - x

      if ( 0.0 < fd * f ):
        d = value
      else:
        u = value
#
#  The iteration did not converge.
#
  ner = 1

  return value, ner

def crude ( xx, nb ):

#*****************************************************************************80
#
## crude returns a crude approximation for the W function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2020
#
#  Author:
#
#    Original FORTRAN77 version by Andrew Barry, S. J. Barry, 
#    Patricia Culligan-Hensley.
#    This MATLAB version by John Burkardt.
#
#  Reference:
#
#    Andrew Barry, S. J. Barry, Patricia Culligan-Hensley,
#    Algorithm 743: WAPR - A Fortran routine for calculating real 
#    values of the W-function,
#    ACM Transactions on Mathematical Software,
#    Volume 21, Number 2, June 1995, pages 172-181.
#
#  Input:
#
#    real XX, the argument.
#
#    integer NB, indicates the desired branch.
#    * 0, the upper branch
#    * nonzero, the lower branch.
#
#  Output:
#
#    real VALUE, the crude approximation to W at XX.
#
  import numpy as np

  value = 0.0

  em = - np.exp ( -1.0 )
  em9 = - np.exp ( -9.0 )
  c13 = 1.0 / 3.0
  em2 = 2.0 / em
  s2 = np.sqrt ( 2.0 )
  s21 = 2.0 * s2 - 3.0
  s22 = 4.0 - 3.0 * s2
  s23 = s2 - 2.0
#
#  Crude Wp.
#
  if ( nb == 0 ):

    if ( xx <= 20.0 ):
      reta = s2 * np.sqrt ( 1.0 - xx / em )
      an2 = 4.612634277343749 * np.sqrt ( np.sqrt ( reta + 1.09556884765625 ) )
      value = reta / ( 1.0 + reta / ( 3.0 \
        + ( s21 * an2 + s22 ) * reta / ( s23 * ( an2 + reta )))) - 1.0
    else:
      zl = np.log ( xx )
      value = np.log ( xx / np.log ( xx \
        / zl ** np.exp ( -1.124491989777808 / \
        ( 0.4225028202459761 + zl ))))

  else:
#
#  Crude Wm.
#
    if ( xx <= em9 ):
      zl = np.log ( -xx )
      t = - 1.0 - zl
      ts = np.sqrt ( t )
      value = zl - ( 2.0 * ts ) / ( s2 + ( c13 - t \
        / ( 270.0 + ts * 127.0471381349219 ) ) * ts )
    else:
      zl = np.log ( -xx )
      eta = 2.0 - em2 * xx
      value = np.log ( xx / np.log ( - xx / ( ( 1.0 \
        - 0.5043921323068457 * ( zl + 1.0 ) ) \
        * ( np.sqrt ( eta ) + eta / 3.0 ) + 1.0 ) ) )

  return value

def nbits_compute ( ):

#*****************************************************************************80
#
## nbits_compute computes the mantissa length minus one.
#
#  Discussion:
#
#    NBITS is the number of bits (less 1) in the mantissa of the
#    floating point number number representation of your machine.
#    It is used to determine the level of accuracy to which the W
#    function should be calculated.
#
#    Most machines use a 24-bit matissa for single precision and
#    53-56 bits for real. The IEEE standard is 53
#    bits. The Fujitsu VP2200 uses 56 bits. Long word length
#    machines vary, e.g., the Cray X/MP has a 48-bit mantissa for
#    single precision.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2020
#
#  Author:
#
#    Original FORTRAN77 version by Andrew Barry, S. J. Barry, 
#    Patricia Culligan-Hensley.
#    This MATLAB version by John Burkardt.
#
#  Reference:
#
#    Andrew Barry, S. J. Barry, Patricia Culligan-Hensley,
#    Algorithm 743: WAPR - A Fortran routine for calculating real 
#    values of the W-function,
#    ACM Transactions on Mathematical Software,
#    Volume 21, Number 2, June 1995, pages 172-181.
#
#  Output:
#
#    integer NBITS, the mantissa length, in bits, minus one.
#
  nbits = 0

  b = 1.0

  while ( True ):

    b = b / 2.0
    v = b + 1.0

    if ( v == 1.0 ):
      return nbits

    nbits = nbits + 1

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
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

def toms743_test01 ( nbits ):

#*****************************************************************************80
#
## toms743_test01 compares WAPR to stored values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2020
#
#  Author:
#
#    Original FORTRAN77 version by Andrew Barry, S. J. Barry, 
#    Patricia Culligan-Hensley.
#    Python version by John Burkardt.
#
#  Input:
#
#    integer NBITS, the number of bits in the mantissa.
#
  import numpy as np
#
#  Exact results for Wp(x).
#
#  X close to -exp(-1).
#
  dx1 = np.array ( [ \
           1.E-40,2.E-40,3.E-40,4.E-40,5.E-40,6.E-40,7.E-40,8.E-40, \
           9.E-40,1.E-39,1.E-30,2.E-30,3.E-30,4.E-30,5.E-30,6.E-30, \
           7.E-30,8.E-30,9.E-30,1.E-29,1.E-20,2.E-20,3.E-20,4.E-20, \
           5.E-20,6.E-20,7.E-20,8.E-20,9.E-20,1.E-19,1.E-10,2.E-10, \
           3.E-10,4.E-10,5.E-10,6.E-10,7.E-10,8.E-10,9.E-10,1.E-9,1.E-5, \
           2.E-5,3.E-5,4.E-5,5.E-5,6.E-5,7.E-5,8.E-5,9.E-5,1.E-4,2.E-4, \
           3.E-4,4.E-4,5.E-4,6.E-4,7.E-4,8.E-4,9.E-4,1.E-3,2.E-3,3.E-3, \
           4.E-3,5.E-3,6.E-3,7.E-3,8.E-3,9.E-3,1.E-2 ] )

  wp1 = np.array ( [ \
           -.9999999999999999999766835601840287579665, \
           -.9999999999999999999670255745859974370634, \
           -.9999999999999999999596147415871158855702, \
           -.9999999999999999999533671203680575159335, \
           -.9999999999999999999478628555782056161596, \
           -.9999999999999999999428866198325571498809, \
           -.9999999999999999999383104987875354650364, \
           -.9999999999999999999340511491719948741275, \
           -.9999999999999999999300506805520862739007, \
           -.9999999999999999999262669432552936235556, \
           -.9999999999999976683560184028776088243496, \
           -.9999999999999967025574585997473306784697, \
           -.9999999999999959614741587115939935280812, \
           -.9999999999999953367120368057588420244704, \
           -.9999999999999947862855578205706768098859, \
           -.9999999999999942886619832557258611080314, \
           -.9999999999999938310498787535591888253966, \
           -.999999999999993405114917199501910108482, \
           -.9999999999999930050680552086436996003626, \
           -.9999999999999926266943255293804772564852, \
           -.9999999997668356018584094585181033975713, \
           -.9999999996702557458962181283375794922681, \
           -.9999999995961474159255244922555603070484, \
           -.9999999995336712037530626747373742782638, \
           -.9999999994786285558726655558473617503914, \
           -.9999999994288661984343027719079710168757, \
           -.9999999993831049880022078023099082447845, \
           -.9999999993405114918649237720678678043098, \
           -.9999999993005068056839596486461928553989, \
           -.9999999992626694327341550240404575805522, \
           -.9999766837414008807143234266407434345965, \
           -.9999670259370180970391011806287847685011, \
           -.9999596152852334187587360603177913882165, \
           -.9999533678452277190993205651165793258207, \
           -.9999478637616504968301143759542621752943, \
           -.9999428877071168268324462680980110604599, \
           -.999938311767283189655618359697592754013, \
           -.999934052598878483932035240348113191731, \
           -.9999300523114688962155368933174163936848, \
           -.9999262687553819399632780281900349826094, \
           -.9926447551971221136721993073029112268763, \
           -.9896086425917686478635208903220735023288, \
           -.9872831094708759013315476674998231771112, \
           -.9853253899681719161468126266199947992874, \
           -.9836027178149637071691226667555243369797, \
           -.9820470029764667038452666345865058694192, \
           -.9806177971936827573257045283891513709368, \
           -.97928874641099293421931043027104578327, \
           -.9780415451927629881943028498821429186059, \
           -.9768628655744219140604871252425961901255, \
           -.967382626983074241885253344632666448927, \
           -.9601485420712594199373375259293860324633, \
           -.9540768694875733222057908617314370634111, \
           -.9487478690765183543410579996573536771348, \
           -.9439462911219380338176477772712853402016, \
           -.9395442782590063946376623684916441100361, \
           -.9354585313336439336066341889767099608018, \
           -.9316311953818583253420613278986500351794, \
           -.9280201500545670487600430252549212247489, \
           -.8991857663963733198571950343133631348347, \
           -.8774287170665477623395641312875506084256, \
           -.8593275036837387237312746018678000939451, \
           -.8435580020488052057849697812109882706542, \
           -.8294416857114015557682843481727604063558, \
           -.8165758053803078481644781849709953302847, \
           -.8046981564792468915744561969751509934994, \
           -.7936267540949175059651534957734689407879, \
           -.7832291989812967764330746819464532478021] )
#
#  x close to 0.
#
  x2 = np.array ( [ \
           1.E-9,2.E-9,3.E-9,4.E-9,5.E-9,6.E-9,7.E-9,8.E-9,9.E-9,1.E-8, \
           1.E-2,2.E-2,3.E-2,4.E-2,5.E-2,6.E-2,7.E-2,8.E-2,9.E-2,1.E-1] )

  wp2 = np.array ( [ \
           9.999999990000000014999999973333333385417E-10, \
           1.9999999960000000119999999573333335E-9, \
           2.999999991000000040499999784000001265625E-9, \
           3.999999984000000095999999317333338666667E-9, \
           4.999999975000000187499998333333349609375E-9, \
           5.999999964000000323999996544000040499999E-9, \
           6.99999995100000051449999359733342086979E-9, \
           7.999999936000000767999989077333503999997E-9, \
           8.999999919000001093499982504000307546869E-9, \
           9.999999900000001499999973333333854166656E-9, \
           9.901473843595011885336326816570107953628E-3, \
           1.961158933740562729168248268298370977812E-2, \
           2.913845916787001265458568152535395243296E-2, \
           3.848966594197856933287598180923987047561E-2, \
           4.767230860012937472638890051416087074706E-2, \
           5.669304377414432493107872588796066666126E-2, \
           6.555812274442272075701853672870305774479E-2, \
           7.427342455278083997072135190143718509109E-2, \
           8.284448574644162210327285639805993759142E-2, \
           9.127652716086226429989572142317956865312E-2, \
           -1.000000001000000001500000002666666671875E-9, \
           -2.000000004000000012000000042666666833333E-9, \
           -3.000000009000000040500000216000001265625E-9, \
           -4.000000016000000096000000682666672E-9, \
           -5.000000025000000187500001666666682942709E-9, \
           -6.000000036000000324000003456000040500001E-9, \
           -7.000000049000000514500006402666754203126E-9, \
           -8.000000064000000768000010922666837333336E-9, \
           -9.000000081000001093500017496000307546881E-9, \
           -1.000000010000000150000002666666718750001E-8, \
           -1.010152719853875327292018767138623973671E-2, \
           -2.041244405580766725973605390749548004159E-2, \
           -3.094279498284817939791038065611524917276E-2, \
           -4.170340843648447389872733812553976786256E-2, \
           -5.270598355154634795995650617915721289428E-2, \
           -6.396318935617251019529498180168867456393E-2, \
           -7.548877886579220591933915955796681153525E-2, \
           -8.729772086157992404091975866027313992649E-2, \
           -9.940635280454481474353567186786621057821E-2, \
           -1.118325591589629648335694568202658422726E-1] )
#
#  Other Wp results.
#
  x3 = np.array ( [ \
    1.E+01,1.E+02,1.E+03,1.E+04,1.E+05,1.E+06,1.E+07,1.E+08,1.E+09,1.E+10] )

  wp3 = np.array ( [ \
           1.745528002740699383074301264875389911535, \
           3.385630140290050184888244364529726867492, \
           5.249602852401596227126056319697306282521, \
           7.231846038093372706475618500141253883968, \
           9.284571428622108983205132234759581939317, \
           11.38335808614005262200015678158500428903, \
           13.5143440103060912090067238511621580283, \
           15.66899671545096218719628189389457073619, \
           17.84172596742146918254060066535711011039, \
           20.02868541330495078123430607181488729749] )
#
#  Exact results for Wm(x).
#
#  X close to -exp(-1).
#
  wm1 = np.array ( [ \
           -1.000000000000000000023316439815971242034, \
           -1.000000000000000000032974425414002562937, \
           -1.000000000000000000040385258412884114431, \
           -1.000000000000000000046632879631942484068, \
           -1.000000000000000000052137144421794383842, \
           -1.000000000000000000057113380167442850121, \
           -1.000000000000000000061689501212464534966, \
           -1.000000000000000000065948850828005125875, \
           -1.000000000000000000069949319447913726103, \
           -1.000000000000000000073733056744706376448, \
           -1.000000000000002331643981597126015551422, \
           -1.000000000000003297442541400259918073073, \
           -1.000000000000004038525841288416879599233, \
           -1.000000000000004663287963194255655478615, \
           -1.00000000000000521371444217944744506897, \
           -1.000000000000005711338016744295885146596, \
           -1.000000000000006168950121246466181805002, \
           -1.000000000000006594885082800527084897688, \
           -1.000000000000006994931944791388919781579, \
           -1.000000000000007373305674470655766501228, \
           -1.000000000233164398177834299194683872234, \
           -1.000000000329744254176269387087995047343, \
           -1.00000000040385258418320678088280150237, \
           -1.000000000466328796391912356113774800963, \
           -1.000000000521371444308553232716574598644, \
           -1.00000000057113380178315977436875260197, \
           -1.000000000616895012251498501679602643872, \
           -1.000000000659488508425026289634430354159, \
           -1.000000000699493194642234170768892572882, \
           -1.000000000737330567628282553087415117543, \
           -1.000023316621036696460620295453277856456, \
           -1.000032974787857057404928311684626421503, \
           -1.000040385802079313048521250390482335902, \
           -1.00004663360452259016530661221213359488, \
           -1.0000521380505373899860247162705706318, \
           -1.000057114467508637629346787348726350223, \
           -1.000061690769779852545970707346938004879, \
           -1.000065950300622136103491886720203687457, \
           -1.00006995095046930174807034225078340539, \
           -1.000073734868993836022551364404248563489, \
           -1.007391489031309264813153180819941418531, \
           -1.010463846806564696239430620915659099361, \
           -1.012825626038880105597738761474228363542, \
           -1.014819592594577564927398399257428492725, \
           -1.016578512742400177512255407989807698099, \
           -1.018170476517182636083407324035097024753, \
           -1.019635932177973215702948823070039007361, \
           -1.021001233780440980009663527189756124983, \
           -1.022284686760270309618528459224732558767, \
           -1.023499619082082348038906498637836105447, \
           -1.033342436522109918536891072083243897233, \
           -1.040939194524944844012076988438386306843, \
           -1.047373634492196231421755878017895964061, \
           -1.053065496629607111615572634090884988897, \
           -1.058230030703619902820337106917657189605, \
           -1.06299509412938704964298950857825124135, \
           -1.067443986111355120560366087010834293872, \
           -1.071634561663924136735470389832541413862, \
           -1.07560894118662498941494486924522316597, \
           -1.108081880631165502564629660944418191031, \
           -1.133487001006868638317076487349933855181, \
           -1.155245851821528613609784258821055266176, \
           -1.174682608817289477552149783867901714817, \
           -1.192475850408615960644596781702366026321, \
           -1.209028378276581220769059281765172085749, \
           -1.224602449817731587352403997390766826335, \
           -1.239380103200799714836392811991400433357, \
           -1.253493791367214516100457405907304877145] )
#
#  X close to 0
#
  wm2 = np.array ( [ \
           -96.67475603368003636615083422832414231073, \
           -95.97433737593292677679699834708774152264, \
           -95.56459382507349364043974513871359837914, \
           -95.27386489130628866261760496192716897551, \
           -95.0483515329550645558378163981346085731, \
           -94.86408948075132603599669916724611501067, \
           -94.70829516116125928735505687861553800851, \
           -94.57333777268864473984718625104978190798, \
           -94.45429521137271454134108055166168787618, \
           -94.34780665137385269060032461028588648619, \
           -73.37311031382297679706747875812087452918, \
           -72.67033891766978907253811160121558649554, \
           -72.25920015786413889986246462168541066725, \
           -71.9674726772681844325410195162521230103, \
           -71.74117979478106456261839111929684980709, \
           -71.55627755942675731851469544735603279342, \
           -71.39993966508440988906136771384270319452, \
           -71.26450969134836299738230265916604879247, \
           -71.14504894849287026061378869987876478469, \
           -71.03818524971357411174259539994036186653, \
           -49.96298427667447244531514297262540669957, \
           -49.25557728489066973476436802404294348267, \
           -48.84167348449764278180827692232244878061, \
           -48.54795966722336777861228992424053274064, \
           -48.32011181512544381639923088992262632623, \
           -48.13392971864323755677656581326964166718, \
           -47.97650308277095858785998266172487372203, \
           -47.84012504158555569017852884133421231303, \
           -47.71982419568730714141619502661365943996, \
           -47.61220592218922310708330388890925734186, \
           -26.29523881924692569411012882185491823773, \
           -25.57429135222126159950976461862116397347, \
           -25.15218334705420805339928870686463192335, \
           -24.85251554543232259250342343156454440592, \
           -24.61997095867949438248843689371454503831, \
           -24.42989922074834124324823589226341161866, \
           -24.26914663885402405126372567664280388966, \
           -24.12985944288624210229238972590881794092, \
           -24.00697058168597098928369714836882130512, \
           -23.8970195845316574350263109196222825525, \
           -14.16360081581018300910955630361089957762, \
           -13.41624453595298662833544556875899262976, \
           -12.97753279184081358418630625949303360266, \
           -12.66551396826200331850774017793451747947, \
           -12.42304039760186078066171146072124458063, \
           -12.22461776385387453853455424320739669321, \
           -12.05663003490708840623665404674007291018, \
           -11.91094134143842011964821167497982287763, \
           -11.78229922740701885487699061601349928173, \
           -11.66711453256635441837882744697047370583, \
           -10.90655739570090676132157335673785028979, \
           -10.45921112040100393534625826514848865968, \
           -10.14059243262036578763968437893562720385, \
           -9.892699522704254067620287857665824159861, \
           -9.689637966382397752838283301312347921626, \
           -9.517569762038614935107630230444563521109, \
           -9.368222172408836799233763466046500781388, \
           -9.236251966692597369166416348621131600216, \
           -9.11800647040274012125833718204681427427, \
           -8.335081377982507150789361715143483020265, \
           -7.872521380098708883395239767904984410792, \
           -7.541940416432904084217222998374802941589, \
           -7.283997135099081646930521042317118095276, \
           -7.072162048994701667487346245044653243434, \
           -6.892241486671583156187212318718730022068, \
           -6.735741661607793269808533725369490789074, \
           -6.597171733627119347342347717832724288261, \
           -6.472775124394004694741057892724488037104] )
#
#  Compare the approximations of WAPR with the given exact values.
#
  print ( '' )
  print ( 'toms743_test01' )
  print ( '  Compare WAPR(X) to stored values.' )
#
#  Wp results for x near -exp(-1).
#
  print ( '' )
  print ( '  Wp results for x near -exp(-1)' )
  print ( '' )
  print ( '   Offset x    W(x) (WAPR)     W(x) (EXACT)   Digits Correct' )
  print ( '' )

  for i in range ( 0, 68 ):

    if ( dx1[i] == 0.0 ):
      em = - np.exp ( -1.0 )
      w, nerror = wapr ( em, 0, 0 )
    else:
      w, nerror = wapr ( dx1[i], 0, 1 )

    if ( w == wp1[i] ):
      nd = np.floor ( np.log10 ( 2.0 ** nbits ) + 0.5 )
    else:
      nd = np.floor ( np.log10 ( abs ( wp1[i] / ( w - wp1[i] ))) + 0.5 )

    print ( '%17.8g      %17.8g      %17.8g      %3d' \
      % (  dx1[i], w, wp1[i], nd ) )
#
#  Wp results for x near 0.
#
  print ( '' )
  print ( '  Wp results for x near 0' )
  print ( '' )
  print ( '      x    W(x) (WAPR)     W(x) (EXACT)   Digits Correct' )
  print ( '' )

  for i in range ( 0, 20 ):
    w, nerror = wapr ( x2[i], 0, 0 )
    if ( w == wp2[i] ):
      nd = np.floor ( np.log10 ( 2.0 ** nbits ) + 0.5 )
    else:
      nd = np.floor ( np.log10 ( abs ( wp2[i] / ( w - wp2[i] ))) + 0.5 )
    print ( '%17.8g      %17.8g      %17.8g      %3d' \
      % ( x2[i], w, wp2[i], nd ) )

  for i in range ( 0, 20 ):
    w, nerror = wapr ( -x2[i], 0, 0 )
    if ( w == wp2[20+i] ):
      nd = np.floor ( np.log10 ( 2.0 ** nbits ) + 0.5 )
    else:
      nd = np.floor ( np.log10 ( abs ( wp2[20+i] / ( w - wp2[20+i] ) ) ) + 0.5 )
    print ( '%17.8g      %17.8g      %17.8g      %3d' \
      % (  -x2[i], w, wp2[20+i], nd ) )
#
#  Other Wp results.
#
  print ( '' )
  print ( '  Other Wp results' )
  print ( '' )
  print ( '      x     W(x) (WAPR)     W(x) (EXACT)   Digits Correct' )
  print ( '' )

  for i in range ( 0, 10 ):
    w, nerror = wapr ( x3[i], 0, 0 )
    if ( w == wp3[i] ):
      nd = np.floor ( np.log10 ( 2.0 ** nbits ) + 0.5 )
    else:
      nd = np.floor ( np.log10 ( abs ( wp3[i] / ( w - wp3[i] ))) + 0.5 )
    print ( '%17.8g      %17.8g      %17.8g      %3d' \
      % (  x3[i], w, wp3[i], nd ) )
#
#  Wm results for x near -exp(-1).
#
  print ( '' )
  print ( '  Wm results for x near 0' )
  print ( '' )
  print ( '      x    W(x) (WAPR)' )
  print ( '     W(x) (EXACT)   Digits Correct' )
  print ( '' )

  for i in range ( 0, 68 ):
    w, nerror = wapr ( dx1[i], 1, 1 )
    if ( w == wm1[i] ):
      nd = np.floor ( np.log10 ( 2.0 ** nbits ) + 0.5 )
    else:
      nd = np.floor ( np.log10 ( abs ( wm1[i] / ( w - wm1[i] ))) + 0.5 )
    print ( '%17.8g      %17.8g      %17.8g      %3d' 
      % (  dx1[i], w, wm1[i], nd ) )
#
#  Wm results for x near 0.
#  Check for underflow.
#
  print ( '' )
  print ( '  Wm results for x near -exp(-1)' )
  print ( '' )
  print ( '   Offset x    W(x) (WAPR)     W(x) (EXACT)   Digits Correct' )
  print ( '' )

  for i in range ( 0, 68 ):

    if ( 0.0 < dx1[i] ):
      w, nerror = wapr ( -dx1[i], 1, 0 )
      if ( w == wm2[i] ):
        nd = np.floor ( np.log10 ( 2.0 ** nbits ) + 0.5 )
      else:
        nd = np.floor ( np.log10 ( abs ( wm2[i] / ( w - wm2[i] ))) + 0.5 )
      print ( '%17.8g      %17.8g      %17.8g      %3d' \
        % ( -dx1[i], w, wm2[i], nd ) )

  return

def toms743_test02 ( nbits, dx, n ):

#*****************************************************************************80
#
## toms743_test02 tests WAPR(X) when X is the offset of the argument from -exp(-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2020
#
#  Author:
#
#    Original FORTRAN77 version by Andrew Barry, S. J. Barry, 
#    Patricia Culligan-Hensley.
#    Python version by John Burkardt.
#
#  Input:
#
#    integer NBITS, the number of bits in the mantissa.
#
#    real DX, the initial offset.
#
#    integer N, the number of offset arguments to generate.
#
  import numpy as np

  print ( '' )
  print ( 'toms743_test02' )
  print ( '  Input X is the offset from -exp(-1).' )

  l = 1
  ifmt = 0
  xmax = n * dx - np.exp ( -1.0 )
  xmin = 0.0

  if ( xmax <= 0.0 ):
    iw = 1
    print ( '  Both branches of the W function will be checked.' )
  else:
    iw = 0
    print ( '  Wp has been selected (maximum x is > 0)' )

  print ( '' )
  print ( '  Results for Wp(x):' )

  if ( ifmt == 0 ):
    print ( '' )
    print ( '   Offset x    W(x) (WAPR)     W(x) (BISECT)  Digits Correct' )
  else:
    print ( '' )
    print ( '     x     W(x) (WAPR)     W(x) (BISECT)  Digits Correct' )

  print ( '' )

  for i in range ( 1, n + 2 ):

    x = xmin + i * dx
    w, nerror = wapr ( x, 0, l )

    if ( nerror == 1 ):

      print ( '  The value of X = %g is out of range.' % ( x ) )

    else:

      we, ner = bisect ( x, 0, l )

      if ( ner == 1 ):
        print ( '' )
        print ( ' BISECT did not converge for x = %g' % ( x ) )
        print ( '  Try reducing NBITS.' )

      if ( w == we ):
        nd = np.floor ( np.log10 ( 2.0 ** nbits ) + 0.5 )
      else:
        nd = np.floor ( np.log10 ( abs ( we / ( w - we ) ) ) + 0.5 )

      print ( '%17.8g      %17.8g      %17.8g      %3d' % ( x, w, we, nd ) )

  if ( iw == 1 ):

    print ( '' )
    print ( '  Results for Wm(x):' )

    if ( ifmt == 0 ):
      print ( '' )
      print ( '   Offset x    W(x) (WAPR)     W(x) (BISECT)  Digits Correct' )
    else:
      print ( '' )
      print ( '     x     W(x) (WAPR)     W(x) (BISECT)  Digits Correct' )

    print ( '' )

    for i in range ( 1, n + 2 ):

      x = xmin + i * dx
      w, nerror = wapr ( x, 1, l )

      if ( nerror == 1 ):

        print ( '  The value of X = %g is out of range.' % ( x ) )

      else:

        we, ner = bisect ( x, 1, l )

        if ( ner == 1 ):
          print ( '' )
          print ( ' BISECT did not converge for x = %g' % ( x ) )
          print ( '  Try reducing NBITS.' )
  
        if ( w == we ):
          nd = np.floor ( np.log10 ( 2.0 ** nbits ) + 0.5 )
        else:
          nd = np.floor ( np.log10 ( abs ( we / ( w - we ) ) ) + 0.5 )

        print ( '%17.8g      %17.8g      %17.8g      %3d' \
          % ( x, w, we, nd ) )

  return

def toms743_test03 ( nbits, xmin, xmax, n ):

#*****************************************************************************80
#
## toms743_test03 tests WAPR(X) when X is the argument.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2020
#
#  Author:
#
#    Original FORTRAN77 version by Andrew Barry, S. J. Barry, 
#    Patricia Culligan-Hensley.
#    Python version by John Burkardt.
#
#  Input:
#
#    integer NBITS, the number of bits in the mantissa.
#
#    real XMIN, XMAX, the range.
#
#    integer N, the number of equally spaced values
#    in the range at which arguments are to be chosen.
#
  import numpy as np

  print ( '' )
  print ( 'toms743_test03' )
  print ( '  Input X is the argument.' )

  ifmt = 1
  l = 0

  if ( xmax < xmin ):
    temp = xmin
    xmin = xmax
    xmax = temp

  dx = ( xmax - xmin ) / n
  xmin = xmin - dx

  if ( xmax <= 0.0 ):
    iw = 1
    print ( '  Both branches of the W function will be checked.' )
  else:
    iw = 0
    print ( '  Wp has been selected (maximum x is > 0)' )

  print ( '' )
  print ( '  Results for Wp(x):' )

  if ( ifmt == 0 ):
    print ( '' )
    print ( '   Offset x    W(x) (WAPR)     W(x) (BISECT)  Digits Correct' )
  else:
    print ( '' )
    print ( '     x     W(x) (WAPR)     W(x) (BISECT)  Digits Correct' )

  print ( '' )

  for i in range ( 1, n + 2 ):

    x = xmin + i * dx
    w, nerror = wapr ( x, 0, l )

    if ( nerror == 1 ):

      print ( '  The value of X = %g is out of range.' % ( x ) )

    else:

      we, ner = bisect ( x, 0, l )

      if ( ner == 1 ):
        print ( '' )
        print ( ' BISECT did not converge for x = %g' % ( x ) )
        print ( '  Try reducing NBITS.' )

      if ( w == we ):
        nd = np.floor ( np.log10 ( 2.0 ** nbits ) + 0.5 )
      else:
        nd = np.floor ( np.log10 ( abs ( we / ( w - we ))) + 0.5 )

      print ( '%17.8g      %17.8g      %17.8g      %3d' % ( x, w, we, nd ) )

  if ( iw == 1 ):

    print ( '' )
    print ( '  Results for Wm(x):' )

    if ( ifmt == 0 ):
      print ( '' )
      print ( '   Offset x    W(x) (WAPR)     W(x) (BISECT)  Digits Correct' )
    else:
      print ( '' )
      print ( '     x     W(x) (WAPR)     W(x) (BISECT)  Digits Correct' )

    for i in range ( 1, n + 2 ):

      x = xmin + i * dx
      w, nerror = wapr ( x, 1, l )

      if ( nerror == 1 ):

        print ( '  The value of X = %g is out of range.' % ( x ) )

      else:

        we, ner = bisect ( x, 1, l )

        if ( ner == 1 ):
          print ( '' )
          print ( ' BISECT did not converge for x = %g' % ( x ) )
          print ( '  Try reducing NBITS.' )

        if ( w == we ):
          nd = np.log10 ( 2.0 ** nbits ) + 0.5
        else:
          nd = np.log10 ( abs ( we / ( w - we ))) + 0.5

        print ( '%17.8g      %17.8g      %17.8g      %3d' % ( x, w, we, nd ) )

  return

def toms743_test ( ):

#*****************************************************************************80
#
## toms743_test() tests toms743().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2020
#
#  Author:
#
#    Original FORTRAN77 version by Andrew Barry, S. J. Barry, 
#    Patricia Culligan-Hensley.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Andrew Barry, S. J. Barry, Patricia Culligan-Hensley,
#    Algorithm 743: WAPR - A Fortran routine for calculating real 
#    values of the W-function,
#    ACM Transactions on Mathematical Software,
#    Volume 21, Number 2, June 1995, pages 172-181.
#
  import platform

  print ( '' )
  print ( 'toms743_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test toms743().' )

  nbits = nbits_compute ( )
  print ( '' )
  print ( '  Number of bits in mantissa - 1 = #d', nbits )

  toms743_test01 ( nbits )

  dx = + 1.0E-09
  n = 10
  toms743_test02 ( nbits, dx, n )

  xmin = 0.0
  xmax = 1.0E+20
  n = 20
  toms743_test03 ( nbits, xmin, xmax, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'toms743_test():' )
  print ( '  Normal end of execution.' )

  return

def wapr ( x, nb, l ):

#*****************************************************************************80
#
## wapr() approximates the W function.
#
#  Discussion:
#
#    The call will fail if the input value X is out of range.
#    The range requirement for the upper branch is:
#      -exp(-1) <= X.
#    The range requirement for the lower branch is:
#      -exp(-1) < X < 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2020
#
#  Author:
#
#    Original FORTRAN77 version by Andrew Barry, S. J. Barry, 
#    Patricia Culligan-Hensley.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Andrew Barry, S. J. Barry, Patricia Culligan-Hensley,
#    Algorithm 743: WAPR - A Fortran routine for calculating real 
#    values of the W-function,
#    ACM Transactions on Mathematical Software,
#    Volume 21, Number 2, June 1995, pages 172-181.
#
#  Input:
#
#    real X, the argument.
#
#    integer NB, indicates the desired branch.
#    * 0, the upper branch
#    * nonzero, the lower branch.
#
#    integer L, indicates the interpretation of X.
#    * 1, X is actually the offset from -(exp-1), so compute W(X-exp(-1)).
#    * not 1, X is the argument compute W(X)
#
#  Output:
#
#    real WAPR, the approximate value of W(X).
#
#    integer NERROR, the error flag.
#    * 0, successful call.
#    * 1, failure, the input X is out of range.
#
  import numpy as np

  value = 0.0
  nerror = 0

  nbits = 52
  niter = 1

  em = - np.exp ( -1.0 )
  em9 = - np.exp ( -9.0 )
  c13 = 1.0 / 3.0
  c23 = 2.0 * c13
  em2 = 2.0 / em
  d12 = - em2
  tb = 0.5 ** nbits
  tb2 = np.sqrt ( tb )
  x0 = tb ** ( 1.0 / 6.0 ) * 0.5
  x1 = ( 1.0 - 17.0 * tb ** ( 2.0 / 7.0 ) ) * em
  an3 = 8.0 / 3.0
  an4 = 135.0 / 83.0
  an5 = 166.0 / 39.0
  an6 = 3167.0 / 3549.0
  s2 = np.sqrt ( 2.0 )
  s21 = 2.0 * s2 - 3.0
  s22 = 4.0 - 3.0 * s2
  s23 = s2 - 2.0

  if ( l == 1 ):

    delx = x

    if ( delx < 0.0 ):
      nerror = 1
      print ( '' )
      print ( 'WAPR - Fatal error!' )
      print ( '  The offset X is negative.' )
      print ( '  It must be nonnegative.' )
      raise Exception ( 'WAPR - Fatal error!' )

    xx = x + em

  else:

    if ( x < em ):
      nerror = 1
      return value, nerror
    elif ( x == em ):
      value = -1.0
      return value, nerror

    xx = x
    delx = xx - em

  if ( nb == 0 ):
#
#  Calculations for Wp.
#
    if ( abs ( xx ) <= x0 ):
      value = xx / ( 1.0 + xx / ( 1.0 + xx \
        / ( 2.0 + xx / ( 0.6 + 0.34 * xx ))))
      return value, nerror
    elif ( xx <= x1 ):
      reta = np.sqrt ( d12 * delx )
      value = reta / ( 1.0 + reta / ( 3.0 + reta / ( reta \
        / ( an4 + reta / ( reta * an6 + an5 ) ) + an3 ) ) ) - 1.0
      return value, nerror
    elif ( xx <= 20.0 ):
      reta = s2 * np.sqrt ( 1.0 - xx / em )
      an2 = 4.612634277343749 * np.sqrt ( np.sqrt ( reta + 1.09556884765625 ))
      value = reta / ( 1.0 + reta / ( 3.0 + ( s21 * an2 \
        + s22 ) * reta / ( s23 * ( an2 + reta )))) - 1.0
    else:
      zl = np.log ( xx )
      value = np.log ( xx / np.log ( xx \
        / zl ** np.exp ( -1.124491989777808 / \
        ( 0.4225028202459761 + zl ))))
#
#  Calculations for Wm.
#
  else:

    if ( 0.0 <= xx ):
      nerror = 1
      return value, nerror
    elif ( xx <= x1 ):
      reta = np.sqrt ( d12 * delx )
      value = reta / ( reta / ( 3.0 + reta / ( reta / ( an4 \
        + reta / ( reta * an6 - an5 ) ) - an3 ) ) - 1.0 ) - 1.0
      return value, nerror
    elif ( xx <= em9 ):
      zl = np.log ( - xx )
      t = -1.0 - zl
      ts = np.sqrt ( t )
      value = zl - ( 2.0 * ts ) / ( s2 + ( c13 - t \
        / ( 270.0 + ts * 127.0471381349219 )) * ts )
    else:
      zl = np.log ( - xx )
      eta = 2.0 - em2 * xx
      value = np.log ( xx / np.log ( -xx / ( ( 1.0 \
        - 0.5043921323068457 * ( zl + 1.0 ) ) \
        * ( np.sqrt ( eta ) + eta / 3.0 ) + 1.0 )))

  for i in range ( 0, niter ):
    zn = np.log ( xx / value ) - value
    temp = 1.0 + value
    temp2 = temp + c23 * zn
    temp2 = 2.0 * temp * temp2
    value = value * ( 1.0 + ( zn / temp ) * ( temp2 - zn ) \
      / ( temp2 - 2.0 * zn ) )

  return value, nerror

if ( __name__ == '__main__' ):
  timestamp ( )
  toms743_test ( )
  timestamp ( )

