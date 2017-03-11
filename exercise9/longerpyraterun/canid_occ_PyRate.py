#!/usr/bin/env python
from numpy import * 


data_1=[array([15.968686,14.836304,14.41041,7.054381,14.006788,5.407378,13.853455,14.22221,15.755603,14.785414,13.809648,9.264538,11.692771]),
array([16.809997,16.909156,15.589549,15.626374,14.947063,15.492257,15.239576,14.672837,13.719354,15.217069,13.836239]),
array([15.06094,19.90971,15.420459,15.91614,10.31812,13.01187,14.281461,14.517863,15.899289,15.489542,7.210576,10.383283,15.764264,13.938571,15.403199,12.295506,20.440622,15.862364,15.786746,15.519818,13.582223,11.765139,15.500286,13.596961,15.340142,14.24704,10.398317,12.259499,9.404976,14.738383,15.703124,10.20825,15.835327,15.836533,14.628424,15.50974,10.778526,14.637645,14.113158,14.202289,15.721564,21.766386,14.455195,13.021407,6.620215,22.557775,14.509956,13.956572,21.118524,9.730051,13.612423]),
array([14.379672,14.381403,15.019589,9.46388,14.057143,15.155435,14.918176,13.906199,14.110735]),
array([15.463277]),
array([10.601004,15.567331,12.209303,12.159353,11.965322,10.69402,12.422096,22.450793,14.871888]),
array([11.333284,11.015428,12.999534,11.908389,12.566996,11.444637,9.304974,21.016101,12.866488,12.681147,10.430505,12.566504,11.088145,16.286224,11.803058,10.459481,7.193415,16.007735,9.047234,10.708462,15.27592,11.68675,13.225138,11.132327,13.238941,11.728282,11.237342,10.472874,10.317871,12.540743,12.772487,7.815656,13.533918,11.107962,12.501277,10.332122,12.090802,10.745874,5.139066,13.07348,13.42266,11.07644,10.250513,11.361444,11.694576,10.687242,11.677649,11.188463,12.323286,12.938971,11.201978,10.875636,12.406921,23.029806,12.908508,12.678237,10.866942,11.810591,10.562667,16.070033,12.857981,12.725554]),
array([16.928918]),
array([1.126605]),
array([1.33398,1.413599,0.063705,0.065819,0.08987,0.053829,0.007913,0.120348,0.009915,0.001877,0.003092]),
array([22.164601]),
array([31.708931,32.356114,28.086654,29.137845,24.21955,22.815985,25.785984,21.977689,29.722049,26.781879,30.265695,22.675904,30.063781,28.35981,27.297973,26.705406,27.065973,29.649779,29.575824,29.068644,27.993537,29.10024,27.971447,26.554185,27.586172,26.928927,28.870536]),
array([33.27113,32.959206,32.094709,32.411167,31.878375,32.011398,33.167221,26.19166,28.225156]),
array([20.679654,20.838892,21.626483,20.143404,18.479932,15.557292,15.515367,15.312577,10.425731,13.09976,13.789158,12.211092,14.327172,10.956472,14.404948,10.526474,11.033658,10.503426,6.04536,11.508687,22.632821,15.41781,11.777175,12.329747,17.346544,14.861584,9.508769,12.207147,11.630986,9.870835,9.302116,13.524219,11.85991,19.823604,19.030819,20.089883,5.281977,19.364938,20.324037,19.075485,16.619227,16.606295,18.057458,17.614195,7.596812,14.439294,14.675224,13.319456,12.373432,10.405277,11.577445,12.265328,13.228126,10.55358,15.31197,14.081909,15.643276,17.332934]),
array([6.556615,6.379094,6.361472,7.221507,9.838797,9.663642,9.363907,9.671507,5.786585,6.008561,9.366343,8.807612,6.468762,5.977572,6.830177,9.180107,6.605228,7.067421,8.374311,5.382012,9.78621,7.899674,3.790963,3.795657,4.364389,3.201587,2.605216,4.896004,2.080084,2.622805,2.758258,2.440438,8.312546]),
array([4.86416,3.833446,1.829991,4.430489,4.288679,2.494949,4.463171,2.126336,3.20537,1.88021,4.073885,1.837684,2.482313,3.223681,4.862026,3.865372,3.15098,4.895348,2.749709,4.405077,4.405382,2.870834,3.011898,4.339882,2.186122,1.954632,3.966654,2.53491]),
array([3.878605]),
array([6.948954,8.044471,7.393455,7.322565,20.035689,6.913043,20.771188,4.176915,9.734761,2.254814,3.501765,3.913941,4.899,4.418371,3.411751,1.901514]),
array([13.331424,6.978389,11.060732,11.615869,10.574196,10.678126,7.183845,13.397714]),
array([8.78528,5.400164,4.379013]),
array([9.306317,6.63233,10.034232]),
array([7.943254,5.682081,13.876482,8.473987,9.547982,9.700428,7.759598,6.22854,22.179192,7.998714,17.774845,7.965408,11.581121,9.288517,7.23424,9.643419,11.720474,11.908463]),
array([8.019125,14.479299,8.235973,7.822003,6.55795,7.744787,5.740377,5.359774,6.863112,6.595595,7.612754,6.343258,22.767192,12.884781,12.068304,8.474563,20.104818,9.612638,5.726861,13.930311,11.495202,8.566686,6.846108,7.162998,8.261332,10.632324,8.902748,7.05707,7.774986]),
array([28.738422]),
array([36.196531,37.114906,33.92237,33.725572,32.237672,23.125154,25.456949,26.18076,24.529001,22.012812,26.169548,25.976714,24.963507,20.462762,22.520146,25.95912,24.440834,20.260874,18.002943,19.072384,11.811794,13.146113,10.911132,13.753099,20.621306,11.004954,12.164159,9.98698,5.470009,10.447441,15.543754,14.770361,6.468217,15.591844,12.73825,8.622435,14.595966,15.857086,15.110984,13.551885,13.643224,21.040981,18.048019,14.850527,14.180642,9.704783,6.305768,1.970203,1.769051,3.173074,2.87812,3.482898,3.762699,4.167528,1.936474,0.522683,4.264912,1.520735,1.417841,1.355162,1.778706,1.479065,1.213213,0.409495,4.03788,21.777218,6.76669,12.314768,2.791441,1.535613,0.539003,2.605983,3.083485,2.167221,0.770317,0.591892,1.994172,1.60569,1.39331,4.334306,2.314727,0.44447,15.44114,10.695917,18.059237,4.671488,17.305275,8.790568,0.293106,2.366463,4.317445,3.119582,25.857223,2.881113,3.280769,5.781476,4.157339,0.512405,19.159276,0.611751,6.628319,0.348494,2.612872,3.87321,0.101905,0.070739,0.069528,0.585685,0.063645,0.019967,0.019006,0.017514,0.078778,5.018277,2.217371,3.449687,0.074627,0.092572,0.084165,24.153519,23.405858,25.079976,21.987898,5.751253,2.509345]),
array([24.830428,8.863422,14.774415,10.417589,12.679427,13.382125,13.067979,9.285225,14.845771,6.19793,13.599093,11.714421,12.241159,7.304576,12.42668,9.756222,7.748228,12.293916,12.861281,10.678259,11.833911,13.014659,12.175665,11.29446,11.21315,2.923432,0.043354,0.098967,0.982471]),
array([6.759279,5.827183,5.477096,1.898107,2.121828,3.350733,4.240283,2.402277,2.386893,3.794095]),
array([8.178062,4.742521,5.137352,3.976553,2.124817,2.613252,2.976846,3.631849,3.891441,3.368261,1.4484,0.939259,0.53538,1.314164,1.039956,1.367507,1.358696,0.473876,0.557255,1.599706,0.454979,1.134806,1.618143,0.117947,3.384338,3.196114,2.944832,3.244509,2.436146,3.247051,3.238602,3.412611,2.908974,2.690789,2.711706,0.981178,0.005293,2.308106,0.408309,8.95281,4.997379,0.283804,0.00803,0.010647,0.00746,0.405047,0.001272,0.002236,0.005849,0.778341,0.240766,5.034008,1.627545,2.569612,0.005614,0.004954,0.00243,0.007879,0.00866,0.002165,0.516606,1.9068,0.009975,3.086804,4.887733,2.654332,4.458499,0.035229,4.714176,1.023099,1.863486,1.758329,1.46969,0.920022,1.601164,0.726516,0.460183,2.438085,5.235398,0.051334,0.456952,4.447745,3.473898,2.56092,2.550878,1.353597,1.412844,1.390185,3.19725,1.425425,1.343291,1.822695,2.083336,1.142324,1.348093,1.202907,1.889869,1.425981,1.729574,1.613761,2.561145,0.329813,3.14091,0.362145,0.445334,4.262837,0.565273,3.122291,3.093193,2.650439,2.633096,1.819648,1.425909,2.047507,1.764894,0.693222,0.157883,3.683634,4.192457,1.479937,0.88623,0.716523,0.457256,1.473824,1.249992,0.11425,2.245007,1.83103,3.767459,4.262856,2.721446,0.93708,1.431906,4.38766,4.411699,4.35611,5.256793,2.108466,1.034817,2.425261,1.436449,3.358965,0.305031,5.754239,4.250076,1.055707,1.076966,1.693913,1.584647,2.432574,1.649673,0.275814,1.326169,0.531167,0.545559,0.395788,0.353393,0.475673,1.184659,0.5124,0.407953,0.631105,1.995514,2.013607,1.938849,4.26546,2.609181,2.598582,2.368168,1.308659,1.789907,2.375553,1.023303,0.568297,0.453786,0.489844,0.314143,0.272326,0.198448,0.13526,0.770639,0.720239,0.46703,3.960128,2.125556,1.774554,0.50336,1.492145,2.369371,0.400976,1.312609,0.900743,4.578523,4.768711,3.233396,3.604511,3.933821,3.679658,4.170585,4.311546,4.395217,2.386246,0.730025,0.829581,1.46689,0.122178,0.018831,0.037071,1.847217,1.88277,0.055537,0.087624,0.010837,0.033101,2.464229,3.355408,3.259991,2.204449,1.705093,2.051138,0.065256,0.111579,0.102593,0.063902,0.111655,0.057549,0.576466,0.279448,17.556215,3.539093,0.099413,0.124696,2.180519,0.076325,3.609043,0.119731,0.009909,1.645107,0.368024,0.008283,0.002086,0.006779,0.004149,6.382036]),
array([0.456209,0.521692,0.269315,0.031701,0.097563,0.483135,1.4318]),
array([0.005993,0.001584,0.476155,0.482987,3.451032,2.584414,2.472918,0.5632,0]),
array([2.224505,2.150844,0]),
array([1.352689]),
array([3.720738,1.296227,0.59251,0.755615,0.534027,1.138404,1.073344,0.446794,0.387266,1.606376,0.422065,1.699329,1.094533,0.059501,1.199849,1.223943,1.27539,1.600713]),
array([0.005802,1.322556,1.58061,0.624631,1.844834,0.006766,1.954302,1.473603,0.267807,2.755273,0.137363,0.202581,0.691551,0.009685,0]),
array([0.807069]),
array([0.34855,1.297308,1.156265,0.374846,0.731209,1.074621,1.010856,0.90704,0.686449,0.215245,0.286882,0.015348,0.403452,0.996231,0.471303,0.084229,0.092532,0.07361,0.035435,0.080764,0.072954,0.091196,0.100434,0.074585,0.096528,0.076039,0.069303,0.080321,0.064216,2.316309,0.279575,1.193282,0.124526,0.113025,0.045633,0.073473,0.067579,1.257926,0.031368,0.079901,0.11441,0.031649,0.425582,0.013909,0.12296,0.073268,0.049689,0.063207,0.102405,0.09538,2.333947,0.03922,0.115678,0.028763,0.071587,0.121708,0.096151,0.099841,0.061447,0.136838,0.07565,0.016671,0.018925,0.030709,0.05911,0.039082,0.027925,0.069553,0.024235,0.504533,1.57949]),
array([2.36598,3.261483,1.695738,1.005033,1.554543,0.319962,1.914219,1.586705,1.335327,0.634242,0.64235,1.213351,4.06936,0.721029,0.472214,1.042527,0.806739,0.347923,3.336055,3.673575,3.691423,3.131143,0.701294,1.39784,1.770733,1.204478,1.770545,1.667993,1.106518,5.611383,3.43933]),
array([0.003125,1.807117,0.005342,0.005889,0.005692,0.011259,0.001016,0.005707,0.001038,0.059351,0.006403,0.009889,0.010661,0.008818,0.007605,0.005472,0]),
array([6.573295,8.884093,6.870515,9.877596,4.234356,2.923577,1.835164,2.660232,4.406059,2.889473,3.563304,3.339138,8.65403,6.944987,5.822711,7.138902,4.201396]),
array([2.494831,2.671383,3.802946,1.872656,2.149471,4.008996,3.603266,3.832181,3.352249,4.802585,1.210206,1.313406,0.53334,0.379583,1.709449,1.047366,1.398683,1.015599,1.432256,1.543678,0.996499,1.140492,1.561282,0.332325,1.413878,1.65191,1.071022,1.023038,0.661226,1.500899,1.076251,1.56458,1.702016,1.173368,0.339931,1.152038,1.737452,1.409142,0.045105,1.615506,0.489308,0.665307,1.373077,0.339453,0.350649,0.122852,0.032283,0.072225,0.102121,0.113022,0.075296,0.069216,0.012318,0.044493,0.103931,0.01297,0.027938,0.071308,0.091046,0.071607,0.001181,0.073213,0.080006,0.067549,0.010414,0.297865,0.123226,0.119905,0.026294,0.123011,0.058444,0.105247,0.107058,0.080951,0.015965,0.068622,0.007463,0.124023,0.122122,0.031484,0.117842,0.023879,0.045344,0.282108,0.017593,0.050196,0.025782,0.091587,0.098949,1.090317,1.729132,2.189677,0.392411,1.022277,0.001752,0]),
array([5.587688,4.638569,4.237304,2.909759,4.607814,4.62154,2.083394,3.769406,3.026662,4.886614,2.117093,2.549259,4.602353,2.194528,4.721777,4.61181,3.232086,3.880218,4.84628,2.445522,3.501677,4.83838,3.410209,4.887516,3.400034,2.442196,3.158453,2.692502,3.63345,4.801723,2.086706,4.031,2.411576,3.940749,4.672097,0.114736]),
array([1.537924,1.628732,1.796933,0.444732,0.06501,0.044431,0.013598,0.070809,0.968125,1.202257,1.147375,0.442339,0.347593,0.379092,2.974649,2.075238,1.296028,0.356432,0.634742,2.56651,0.731956,0.511086,0.412499,1.124225,1.467177,2.169541,0.607891,0.459281,0.462334,0.047121,0.114892,0.04977,0.02598,0.026702,0.083929,1.027886,0.253543,0.450079,0.40158,0.566333,0.669331,0.166413,0.478766,0.062503,0.386738,0.495001,0.467735,0.749617,0.055389,0.226467,0.680248,0.505679,0.412411,0.616663,0.26851,0.228258,1.942923,0.713983,0.585345,0.241501,0.887765,0.496093,0.003067,0.004048,1.183874,0.681939,2.604123,0.029505,0.044611,0.106992,0.102431,0.043467,0.093396,0.029777,0.121243,0.075136,0.002693,0.047073,0.068849,0.079191,0.644735,0.05367,0.104524,0.093124,0.02713,0.051134,0.019428,0.095862,0.078752,0.091386,0.120733,0.014941,0.021401,0.125431,0.001555,0.003518,0.001304,0.175326,0.059455,0]),
array([1.558755,3.684969,5.013781,0.002375,0.006859,2.771482,2.268131,1.021818,2.887828,1.927409,2.206701,0.011535,1.31598,2.067352,0.011557,0.409381,2.493952,1.114366,2.442551,2.195811,0.025076,0.203457,1.51101,2.186722,1.284931,1.05218,2.045207,1.93768,1.784004,3.151166,3.365428,0.745135,0.066646,1.350685,0.637702,1.334929,0.453164,1.567096,2.519047,5.06146,2.293904,1.086444,0.008369,0.093261,0.033533,1.633448,2.233188,0.115247,0.054668,0.754896,2.530356,0.525358,0]),
array([0.829701]),
array([4.644184,4.496145,1.875363,1.671716,1.472076,1.624237,0.109454,0]),
array([4.477146]),
array([15.030552,17.963488,14.534445]),
array([15.359362,14.539364,15.723367,14.715524,15.610766,15.542668,13.620892,14.469456,15.807653,14.464577,11.512089,15.68331,13.940484,15.614675,14.202841,13.939984,15.274083]),
array([7.153516,8.205519,5.307506]),
array([11.744938,11.947914,10.301773,12.707935,10.967556,10.351657,12.554483,10.904966,13.58586,19.629575,14.998019,10.722356]),
array([12.45787,11.816447,12.522751,12.41426,11.932502,13.564248,12.453811,10.539011,7.295728,15.286056,15.611077]),
array([1.922849,4.238101]),
array([9.528907,2.05682]),
array([0.004396,0.017048,0.053974]),
array([47.065036]),
array([0.705683]),
array([2.259087,0.22514]),
array([4.168796,2.453094]),
array([30.036099]),
array([26.325934,26.999902,28.440991,25.625959,20.7444,7.654845,19.766873,25.165654,24.854196,25.450886]),
array([25.712867,20.433982,24.345966,20.942607,21.530852]),
array([1.847311]),
array([0.326289,0.256415,0.77153,0.736024,0.568302,0.170729,0.671199,0.46087,0.743306,0.299708,0.57162,0.106618,0.32024]),
array([0.532458,0.44645,0.091765]),
array([21.883689,21.304447,23.392057,22.925611,22.303705,21.559365,19.258968,16.955378,19.462659,20.067976,18.092303,16.179219,16.485623,16.060306,19.734335,17.032751,20.307854,16.594113,16.934059,16.248324,17.04548,18.78909,19.123628,16.158326,18.400136,18.522869,18.698428,20.030662,13.730531,17.720546,18.568946,19.168309,18.565673,17.87024,19.859307,20.390881,16.941059,19.268686,16.035436,17.716118,19.609019,17.184349,14.619818,14.461674,14.999025,15.161642,20.728022]),
array([16.003538,19.775893]),
array([14.237873,19.372096]),
array([22.946837]),
array([24.918317,25.682407,21.384673,30.776452,27.143122,21.57592]),
array([21.149056,22.015248,23.099399,21.744253]),
array([21.067982,28.693611,26.392412,29.18293,30.144827,27.23305,27.451783,27.792962,27.986628]),
array([16.332429,17.85605]),
array([12.341952,15.486475,10.633208]),
array([11.53255,10.661579,19.507002,11.419251,12.95378,10.971368,12.283779,13.153932,11.332753,11.466988,10.017455,12.520271,13.144905,13.371687,6.440226,8.141334]),
array([15.07249,13.899649,14.932125]),
array([15.780403,17.191239]),
array([13.954103,13.782198,15.954418,15.103831,14.07784,14.575467,14.778036]),
array([12.238868,12.855039,10.472396]),
array([15.609862]),
array([24.708404]),
array([31.86415,31.401664,31.646814,32.508292,32.54707,31.40008,31.222266,31.806655,25.83433,29.459038,22.576515,28.654773,22.550889,26.616365]),
array([33.574987,32.60801,32.55868,46.466083,34.154708,36.543034,35.298378,49.653643,29.545314]),
array([34.286484,35.740049,34.301278,37.021658,35.511685]),
array([0.199065,0.503669,0.450566,0.39944,0.018975,1.013614]),
array([0.039444,0.583593,2.753775,0.615503]),
array([23.955323]),
array([19.150495,19.998072,16.176015,18.227436,18.966221,17.140932,17.282506,17.221449]),
array([21.06673,20.470883,24.786176,20.563575,21.294494,20.824767,22.522952,23.455444,25.221199,22.169139,22.196156,21.864858,21.51478,21.005666,22.811661,22.794123,24.772246,22.041983,21.601271,20.708885,21.366281,16.970266,18.895297,16.888316,20.211622,19.457214,18.026126,20.351693,16.585605,19.681315,24.291299,20.856996,17.60996]),
array([0.00614,0.003999,0.072575,1.448834,0.008948,0.011671,1.717374,0.088592]),
array([0.088284,0.343916,0.357342,0.056996,0.104897,0.074545,0.107364]),
array([0.517036]),
array([0.150977]),
array([31.717907,30.190112]),
array([23.213033]),
array([16.734266,19.818158,17.492702]),
array([32.520953,25.410606,21.161858,30.509992,24.92168,25.735861]),
array([20.815012]),
array([23.513103,20.656338,26.171121,27.10329,24.085994,23.680983,24.085363,21.290355]),
array([24.853929,28.482622,25.030183,25.309247,25.798575,27.740742,30.060821,29.9104,21.418681,26.17437]),
array([20.972064,24.210045]),
array([9.912003,9.47675,10.559575,5.752788,8.834118]),
array([5.13365]),
array([18.18797,5.578467,7.700975,20.726864,9.6504,5.541083,6.181925,12.987753,11.194846,11.671259,21.558319,4.9938,8.970231,13.153472,10.959422,12.906431,8.291142,10.546041,12.400038,13.353818,9.494839,11.601792,15.350398,6.282068,9.907536,13.012809,10.6701,6.592723,5.533472,9.302699,13.368984,18.644385,10.314819,10.354509,10.687728,9.76277,13.364051,8.588046,12.103571,10.131955,4.996803,5.418755,12.109731,8.042413,6.600321,8.154937,10.785871,14.028828,10.066853,16.089858,13.592778,11.301629,10.2172,8.73573,10.000912,11.362512,5.197877,12.095891,7.061618,13.331744,6.405044,14.494964,11.207669,11.005654,14.355108,8.623996,16.776671]),
array([10.768323,9.110706,5.527758,12.220494,12.529897,12.880803,10.591823,12.533389,8.040669,7.850908,11.275699,13.057544,11.529936,10.761483,13.333348,13.28094,12.37213,13.13747,12.454217,11.619853,12.280996,12.670644,12.905058,12.11599,13.447753,11.569638,11.646499,10.26861,6.235048,12.519827,9.265508,12.217249,12.923708,10.92782,11.67794,10.051685,11.601117,10.702571,13.322271,7.053256,10.755303,6.256528,10.605887,11.153062,10.87841,10.234884,20.005157,13.028497,11.637801,12.161317,11.27981,12.696811,10.553842,8.504055,12.402621,15.686452,14.613517,14.371472,14.414324,14.593348,14.837413,12.453581,5.618495,10.700315,4.935205,9.106461,10.413088,12.257182,6.950223,12.918039,11.971022,10.620737,11.920904,14.401257,9.573971,10.02406]),
array([8.894404,4.548447,5.695771]),
array([8.902141,8.004956,8.769696,10.090929,6.058474,8.782679,7.104661,8.786518,8.976388,22.913423,6.743792,7.558882,7.790973,9.999104,7.787615,5.487693,8.615145,2.566623,5.040826,6.228668,8.961564,7.010568,6.459798,9.883117,7.464673,5.666985,7.956165,9.822384]),
array([13.559691]),
array([14.582487,17.817733,16.385562,15.228521,13.676541,14.170328]),
array([18.015835]),
array([14.816499,13.091891]),
array([42.520189,37.565273,36.933586,36.841488,36.81961,36.291571,36.75609,34.04672,36.340659,34.369704,36.553089,37.140017,34.325375,34.367994,37.130709,34.405391,36.062945,33.872582,33.869339,33.425845,33.891379,33.491877,33.684248,33.530653,33.31686,33.418998,33.636072,32.41595,32.928063,32.593742,32.787958,31.487072,32.637021,27.220777]),
array([33.391124,33.334374]),
array([38.719364,35.006937,36.707771,35.078678,35.169333,33.934751,35.81345,34.04159,35.121105,36.938528,34.66503,35.402574,36.67047,36.531817,36.081481,36.44914,36.893076,34.615904,34.036313,36.743728,34.301864,35.306196,36.500971,37.010715,35.330287,35.514076,35.403053,35.433709,36.907129,35.815583,34.166321,34.55995,35.567714,36.185932,36.724327,34.309153,34.532253,36.063729,33.365885,33.717686,33.464889,33.763669,33.625432,33.667181,33.411845,33.74679,33.600792,33.870844,33.666868,33.685648,33.469339,33.788747,33.522465,33.611891,33.507008,33.54283,33.804078,33.848196,33.726335,33.606386,33.898846,33.592647,33.317728,33.884288,33.859827,33.547277,33.669835,33.769829,33.874591,33.866827,33.711208,33.50078,33.792862,33.848776,33.537372,33.828369,33.707625,33.312018,33.531315,33.307669,33.472207,33.370232,33.392179,33.793706,33.389169,33.705276,33.326087,33.536379,33.623447,33.416922,33.627345,33.580084,33.69029,33.371111,33.514941,33.544256,33.321544,33.886173,33.838868,33.86192,33.32742,33.556032,33.690552,33.672452,33.360698,33.870223,33.868545,33.609071,33.781035,33.500338,33.609837,33.349852,33.850974,33.791855,33.830813,33.78994,33.471595,33.423127,33.734995,33.447894,33.696463,33.858259,33.311032,31.364642,32.250133,31.952758,30.931234,31.53535,32.009643,30.992907,35.906816,35.788993,33.828768]),
array([27.676384,20.928254]),
array([23.420962,24.16127,14.443541,11.61189,15.841189,11.029503,11.740058,22.310677,13.670122,13.240753,22.507602,28.702802,14.960874]),
array([22.017806]),
array([28.843835,25.761793,23.056142,29.385612,22.161737]),
array([22.814435,23.91541,23.317145,24.042713,20.893005,23.698761]),
array([14.182115,15.974471,19.995557,16.967954,18.853859,23.451814,19.622508,17.053573,17.070007,18.612471,19.49116,19.790124,18.084791,19.975724,15.105662,15.477296,13.71217,15.850563,15.926252,15.451786,14.392451,15.820581,15.393217,15.610312]),
array([11.004755,12.483114,11.9354,12.159055,11.328654,13.384094,11.232455,11.997735,12.107187,12.363108,11.28899,11.372224,11.650101,11.103823,10.941572,11.470986,12.509088,11.867062]),
array([24.499786]),
array([12.439014]),
array([15.633166,15.527182,19.957483,10.904024,14.353275,15.84943,12.468677,15.411034,15.869153,14.43407,13.904122,15.879704,15.448388,15.12053,14.673657,14.424575,15.451745,12.149289,15.867105,15.143257,15.085997,13.167076,13.984785,10.806253,12.198587,11.061604,10.630018,10.660914,12.321098,14.687051,14.525533,15.470495,13.679271,14.18542,15.589102,12.209473,11.120983,11.512366,10.684254,13.327301,13.156419,12.011981,14.82713,20.97692,12.960897,18.119936,10.964385,8.106511,20.84754,12.664092,13.457983]),
array([22.718168,19.590835,27.288241,16.117621,16.744724,27.16644]),
array([2.213528,0.512283,2.503334,3.972682,2.497513,0.76057,2.776735]),
array([0.00937,0.153668,2.362213,0.252949,2.204919,0.050365,0.313748,1.95496,1.059745,0.061311]),
array([27.719112]),
array([30.767158,21.051545,29.782483,24.517717,20.897427]),
array([27.925849,24.808679]),
array([33.781342,31.240593,31.653963,31.796708,31.680649,33.257444,31.549485,32.011723,32.046743,32.030069,31.72712,31.690797,30.956112,31.945838,29.466959,27.175859,30.66561,30.092352,29.790715,29.554592,23.933587]),
array([6.263859]),
array([11.205885,17.327763,17.104081]),
array([8.322358,8.397819,22.53459,8.020952,10.57817,8.209651]),
array([6.617174]),
array([18.644605,19.625175,18.075298,16.984112,16.046793,17.715592,17.151914,19.739518,17.624245,19.123281,17.178044,16.109574,18.465981,16.837015,19.558519,19.18371,16.167099,17.509807,19.362332,18.657862,19.590935,21.24463,19.441802,18.786437,17.729837]),
array([17.535043,13.875535,19.044236,20.156753,16.541542,17.969431,18.971802,20.095574,14.433722,7.584531,13.827235,19.983104,15.706718,15.262538,15.775832,18.634348,14.611179,15.359936,15.707598,6.699414,14.814224,15.565886,14.540649,14.036367,14.739972,15.546399,6.720016,15.840921,15.625071,14.655421,14.866122,14.838694,14.397329,14.670184]),
array([41.346385]),
array([3.916302,1.999907,4.682633,3.528982,1.880273,2.857847,3.05783,2.265062,4.199751,4.957383,2.757608,5.164852,1.320538,3.286193,4.995415,4.900183,1.855873,5.025569,7.195585,5.09385,5.030788,3.870685,0.375748,2.771841,1.949193,2.089467,2.063582,1.946524,2.827582,2.16037,3.305978,1.553956,1.736293,3.686229,2.856195,4.779723,1.5194,1.691913]),
array([3.005796,3.4638]),
array([1.988815,0.093406,0.065247]),
array([21.497136,19.641217]),
array([14.096096,20.360965,16.103604,16.501246,16.665744,16.835999,18.066052,18.356967,19.279203,14.251843,14.666947,14.224753,13.930924,13.793094]),
array([18.164538,18.901323,18.398782,16.535571]),
array([33.591938,31.956254]),
array([18.227905,19.824884,18.580823]),
array([32.70278,32.746295,21.826566]),
array([22.044486]),
array([30.156082,25.435394,22.561826,23.599364,27.534676,29.568367]),
array([33.528163,33.884475]),
array([0.206549,0.034612,3.144302,1.694694,2.133232]),
array([0.003458,0.005902,0.298923,1.736156,1.136502,1.958486,0.115636]),
array([31.549238,30.811267]),
array([32.020856,32.754232,32.747691,33.259206]),
array([19.86607,16.185664,20.782793,19.179319,16.087818,18.826499,20.143815,18.159744,16.589513,17.151235,14.879703,15.375505,21.871966,19.103335,14.684593,16.394985,15.498696,15.379366]),
array([18.619842,16.511321,16.936327,13.832438,16.61364]),
array([25.889487,30.165001,21.344803,21.592914,25.638867,24.269028,21.478314,25.470136,23.904655,24.355253,22.348223,26.089892]),
array([21.882884,20.659591]),
array([23.636802,23.888574,23.738711,22.054394,24.702713,22.467162,27.855978,21.838772]),
array([12.182935,11.913181,12.457962,9.036107,11.404108,10.773815,11.772604,12.45612,14.136573,13.39098,11.71682,12.302116,11.020655,13.130525,11.488746,10.965605,13.093492,18.361393,11.959104,11.656819,13.395402,11.571253,11.65079,11.677459,13.517106,11.36125]),
array([13.979679,15.903563,15.336117,15.453956,15.309489,15.073597,14.380524,15.78796,15.050779,14.148836,15.681957,15.220437,15.510245,14.216729,15.324021,6.03666,13.740085,15.707662,17.565944,15.821784,14.64197,14.930059,15.554525,13.788438,14.086399,16.954631,14.6789,14.839054,14.089201,13.97518,15.08332,14.144973,11.251858,15.913835,14.173159,6.592728,14.0062,14.1423,15.088618,14.934104,13.943047,13.97958,14.308123,14.941173]),
array([22.027961,30.429924,27.026401,28.19154,29.555679,29.886728,26.497184,23.861394]),
array([24.623107,22.25248,19.762735,18.780774,23.777481,16.824283,18.013088,20.384197,30.660147]),
array([24.212776]),
array([20.841441,21.308292,21.469248,24.335137,23.708688,20.760109,23.592648,21.573087]),
array([32.356302,29.827227,26.151196]),
array([24.577575,22.1469,16.297516,16.614977,16.324165,20.329037,15.973778,17.091028,16.668134]),
array([16.326308]),
array([18.685223,16.241912,18.29867,16.169368,19.403634]),
array([20.63631,25.068985,21.124388,21.453116,20.992799,20.937844,22.013181,22.416875,20.606954,24.629507,21.524824,20.416901]),
array([20.964313]),
array([24.700912,25.700589,27.081024,20.986099]),
array([17.852579]),
array([33.77532]),
array([13.891517,14.586017,15.532824,14.133866,15.796136]),
array([2.485538,1.808076,0.075023,0.467771,1.059873,0.029333,0.023866]),
array([0.61862]),
array([1.867928]),
array([0.274984,0.01399,0.051008,0.123551,2.511832,0.23764,0.03984,0.105743]),
array([17.116508,17.60929,16.909212,18.334822,16.068356,19.612291,18.582611,19.554843,20.260698,19.578337,18.70098,17.193295,17.511092,17.79346,17.60975,17.045467,18.676507,19.39733,19.600017,17.817659,15.075497,16.892732,18.497736,18.730004,15.030638,14.985758,16.082573]),
array([14.535693,19.187101,19.543695,14.344713]),
array([0.002988,2.105454,0.66021,0.561308,0]),
array([30.198674,24.075938,27.911249]),
array([0.536972]),
array([0.009626]),
array([26.942259,27.684854,26.751523,29.296583,30.31832]),
array([15.854734,13.795705,13.125301]),
array([0.023346,1.205556,0.120309]),
array([2.230055,2.14268]),
array([14.342033,15.628926,16.009718,14.13976,13.047303]),
array([17.583027,20.267692,18.07927,17.768828,15.78973,17.689018,20.019297,18.377401,19.506755,17.84839,17.295183,15.067556,13.983752,15.821537,8.854744,13.752279,14.480139,16.509374,17.084423,13.719846]),
array([17.205763,19.427388,17.820188,15.040717,18.354983,19.13483,18.053347,20.234384,19.555121,16.25146,16.994944,14.391984,20.240562,19.306229,16.21702,16.539574,14.272216,15.162257,14.019069,15.918695,14.535968,15.542439,15.688335,14.567207,13.710928,13.64767,14.982896,14.147255,14.181496,15.490938,15.178487,15.234584,15.012839,21.769169,15.140104]),
array([4.195701,0.785097,0.322388,0.352268,0.076931,0.052324,0.013167,0.012005,0.168974,11.399239]),
array([4.379565,1.074285,1.444487,1.635049,0.890705,1.628306,0.928772,0.066746,1.122323,0.058411,0.06777,0.085356,0.11508,0.052832,0.97785,0.034045,2.097401,0.0739,0.114624,0.065041,0.037213,2.469423,0.079448,0.012573,1.296839,0.119159,0.003405,0.039177,0.026332,0.030408,0.048369,0.097712,0.051427,0.085753]),
array([3.458292]),
array([2.219756,2.258455,3.321038,3.558691,4.392531]),
array([1.367723,0.877493]),
array([4.068994]),
array([6.410207]),
array([5.476034,3.159785,9.795492,7.072158,4.678741,0.323389,1.442643,0.538193,0.440069,1.324276,0.916887,0.820291,1.253907,0.666824,0.095029,2.48878,3.930338,4.090359,2.189805,0.800732,0.779763,3.344633,0.941068,1.281681,2.989982,4.7974,2.99758,1.994342,0.885849,1.950826,0.304574,0.742125,4.604507,3.09958,2.627869,3.185809,2.07777,2.224538,0.893288,2.361149,1.742877,4.056201,4.690463,2.022323,2.085143,1.176321,2.888979,0.787052,2.973919,2.783838,2.841849,3.193241,3.108501,3.765182,1.781622,1.527663,2.276505,1.850438,0.431906,0.126123,0.550164,0.424738,1.846989,0.843296,0.697505,4.966278,0.088129,1.126265,0.230762,2.48134,2.011314,2.183203,2.357686,7.108858,4.530276,2.210183,1.547012,0.598458,5.135343,0.083993,0.014358,0.04693,0.609341,0.210779,1.86785,0.508086,0.430894,2.007769,3.081317,2.93342,1.993269,1.192146,0.526637,0.45509,0.404971,1.880949,0.365349,3.878906,3.607617,0.037022,0.601987,0.085509,0.056614,0.058246,3.409618,1.25328,3.387576,0.100145,0.060722,0.103991,2.294161,4.310781,0.899788,0.65037,0.0147,0.009129]),
array([0.012565]),
array([0.001893,0.029082,0.007075,0.256157,0.004857,0.008503,0.009255,0.237204,0.007779,0.004221,0.007041,0.083184,2.121469,1.938261,2.262661,1.222248,0.124279,1.50172,0.819131,1.123628]),
array([12.499215]),
array([3.683263]),
array([6.885801,6.61095,9.870742,8.63989,5.500895,7.011262,7.47326,5.083787,5.307203,5.881627,9.125474,0.956899,7.94342,10.128931,7.628034,8.939456,6.563007,5.60917,5.172276,7.691013,14.797223]),
array([2.734881,0.498319,0.402191,1.694375,1.759707,1.526086,0.473566,1.517137,1.496661,0.043378,0.069393,0.085143,0.067655,0.007701,0.056012]),
array([1.247351,1.787097,1.096424,0.426529,0.054515,0.101005,0.062802,0.058493,2.167044,0.137702,0.54929,0.164084,0.024522,0.142228,0.103957,0.358995,0.22336,0.593236,0.745676,3.184714,2.337164,0.119272,0.237905,0.712018,0.074097,0.276553,0.921755,0.49272,0.098355,0.422469,0.682477,0.642572,0.564873,1.832115,0.856848,0.032327,1.113596,0.480824,0.659377,0.646919,2.322704,0.285362,0.091121,0.088689,1.853715,0.052708,0.051158,0.030806,0.05114,0.059231,0.093353,0.115997,0.116673,0.027001,0.086194,0.071099,0.106126,0.039848,0.072074,2.369919,0.060856,0.003638,0.010269,0.008114,0.101839,0.460407,0.070935]),
array([0.050728]),
array([0.082908]),
array([0.26169,1.154372,2.014708]),
array([1.738577,1.850384,2.026114,1.903431,0.164651,2.445527,0.234035,2.117301,0.374387]),
array([1.313298])
]

d=[data_1]
names=[ 'canid_occ_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Aelurodon','Aelurodon_asthenostylus','Aelurodon_ferox','Aelurodon_mcgrewi','Aelurodon_montanensis','Aelurodon_stirtoni','Aelurodon_taxoides','Aelurodon_wheelerianus','Alopex','Alopex_lagopus','Archaeocyon_falkenbachi','Archaeocyon_leptodus','Archaeocyon_pavidus','Borophaginae','Borophagus','Borophagus_diversidens','Borophagus_dudleyi','Borophagus_hilli','Borophagus_littoralis','Borophagus_orc','Borophagus_parvus','Borophagus_pugnator','Borophagus_secundus','Caedocyon_tedfordi','Canidae','Caninae','Canini','Canis','Canis_(Pseudalopex)','Canis_adustus','Canis_anthus','Canis_apolloniensis','Canis_armbrusteri','Canis_aureus','Canis_cedazoensis','Canis_dirus','Canis_edwardii','Canis_familiaris','Canis_ferox','Canis_latrans','Canis_lepophagus','Canis_lupus','Canis_mesomelas','Canis_proplatensis','Canis_rufus','Canis_thooides','Carpocyon','Carpocyon_compressus','Carpocyon_limosus','Carpocyon_robustus','Carpocyon_webbi','Cerdocyon_avius','Cerdocyon_texanus','Cerdocyon_thous','Chailicyon_crassidens','Chrysocyon','Chrysocyon_brachyurus','Chrysocyon_nearcticus','Cormocyon','Cormocyon_copei','Cormocyon_haydeni','Cubacyon_transversidens','Cuon','Cuon_alpinus','Cynarctoides_acridens','Cynarctoides_emryi','Cynarctoides_gawnae','Cynarctoides_harlowi','Cynarctoides_lemur','Cynarctoides_luskensis','Cynarctoides_roii','Cynarctoides_whistleri','Cynarctus','Cynarctus_crucidens','Cynarctus_galushai','Cynarctus_marylandica','Cynarctus_saxatilis','Cynarctus_voorhiesi','Cynarctus_wangi','Cynodesmus_martini','Cynodesmus_thooides','Cynodictis','Cynodictis_lacustris','Cynotherium','Cynotherium_sardous','Desmocyon','Desmocyon_matthewi','Desmocyon_thomsoni','Dusicyon','Dusicyon_avus','Dusicyon_culpaeus','Dusicyon_sechurae','Ectopocynus_antiquus','Ectopocynus_intermedius','Ectopocynus_simplicidens','Enhydrocyon','Enhydrocyon_basilatus','Enhydrocyon_crassidens','Enhydrocyon_pahinsintewakpa','Enhydrocyon_stenocephalus','Epicyon','Epicyon_aelurodontoides','Epicyon_haydeni','Epicyon_saevus','Eucyon','Eucyon_davisi','Eucyon_skinneri','Euoplocyon_brachygnathus','Euoplocyon_spissidens','Gobicyon','Hesperocyon','Hesperocyon_coloradensis','Hesperocyon_gregarius','Hesperocyoninae','Leptocyon','Leptocyon_delicatus','Leptocyon_douglassi','Leptocyon_gregorii','Leptocyon_leidyi','Leptocyon_matthewi','Leptocyon_mollis','Leptocyon_tejonensis','Leptocyon_vafer','Leptocyon_vulpinus','Lycaon','Lycaon_pictus','Mesocyon','Mesocyon_brachyops','Mesocyon_coryphaeus','Mesocyon_temnodon','Metalopex_bakeri','Metalopex_macconnelli','Metalopex_merriami','Metatomarctus','Metatomarctus_canavus','Microtomarctus_conferta','Neovulpavus_washakius','Nyctereutes','Nyctereutes_abdeslami','Nyctereutes_procyonoides','Osbornodon_brachypus','Osbornodon_fricki','Osbornodon_iamonensis','Osbornodon_renjiei','Osbornodon_scitulus','Osbornodon_sesnoni','Osbornodon_wangi','Otarocyon_cooki','Otarocyon_macdonaldi','Otocyon','Otocyon_megalotis','Oxetocyon','Oxetocyon_cuspidatus','Paracynarctus_kelloggi','Paracynarctus_sinclairi','Paraenhydrocyon_josephi','Paraenhydrocyon_robustus','Paraenhydrocyon_wallovianus','Paratomarctus_euthos','Paratomarctus_temerarius','Philotrox_condoni','Phlaocyon','Phlaocyon_achoros','Phlaocyon_annectens','Phlaocyon_latidens','Phlaocyon_leucosteus','Phlaocyon_mariae','Phlaocyon_marslandensis','Phlaocyon_minor','Phlaocyon_multicuspus','Phlaocyon_taylori','Phlaocyon_yatkolai','Protemnocyon_inflatus','Protepicyon_raki','Protocyon','Protocyon_orcesi','Protocyon_tarijensis','Protocyon_troglodytes','Protomarctus_optatus','Psalidocyon_marianae','Pseudalopex_gymnocercus','Rhizocyon_oregonensis','Speothos','Speothos_venaticus','Sunkahetanka_geringensis','Tephrocyon_rurestris','Theriodictis','Theriodictis_floridanus','Tomarctus','Tomarctus_brevirostris','Tomarctus_hippophaga','Urocyon','Urocyon_cinereoargenteus','Urocyon_citrinus','Urocyon_galushai','Urocyon_minicephalus','Urocyon_progressus','Urocyon_webbi','Vulpes','Vulpes_cascadensis','Vulpes_chama','Vulpes_kernensis','Vulpes_mathisoni','Vulpes_stenognathus','Vulpes_velox','Vulpes_vulpes','Vulpes_vulpes_macroura','Vulpini','Xenocyon','Xenocyon_lycaonoides','Xenocyon_texanus']
def get_taxa_names(): return taxa_names
