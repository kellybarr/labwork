#!/usr/bin/env python
from numpy import * 


data_1=[array([14.027331,13.759978,13.986927,11.968735,15.561129,13.412804,13.797495,15.122999,14.7244,14.543911,15.545787,6.851,13.310155]),
array([19.224271,18.402263,14.042041,15.239297,14.653939,13.732362,15.033684,15.466091,15.83435,14.488769,14.412278]),
array([15.942606,5.506349,15.866294,14.478406,13.506619,12.125226,13.975513,15.398883,15.63328,14.186628,5.053029,12.543215,14.830687,13.954188,15.659658,10.997241,12.725787,13.662052,14.824713,15.282726,13.032197,12.305999,14.841316,12.55246,15.715447,15.263077,10.817751,12.256407,5.608989,13.624518,14.207495,18.536385,14.767746,13.856329,15.609317,14.824608,13.755284,15.84476,11.478649,15.789387,15.249335,9.297463,14.394809,13.044446,6.12434,13.279613,15.942884,14.489033,5.972658,9.55649,14.975261]),
array([15.735331,14.446974,15.944287,16.32477,15.565579,14.508285,14.580906,15.421594,13.643015]),
array([14.700358]),
array([11.873207,14.303308,12.368265,11.299537,10.420094,10.604495,12.474163,18.977722,15.581494]),
array([13.492532,10.425228,13.354189,11.151524,13.8776,10.408714,9.636249,6.209684,10.429219,11.409446,10.389924,10.658882,12.416542,18.733144,11.139276,12.237461,9.014469,9.056515,9.266312,11.13783,14.349175,12.641759,11.699996,10.482973,11.511168,11.159636,12.223926,12.565406,6.397902,13.247327,12.998686,11.914005,13.126292,9.008943,11.407342,11.22012,12.977473,10.956512,8.156281,11.478747,11.443297,10.312227,10.588716,10.791196,10.829373,13.401599,12.609453,13.50218,11.872184,12.793426,10.690206,10.417519,13.461104,19.863915,12.652986,22.280447,12.54058,11.774352,11.962794,22.218907,10.728142,10.904718]),
array([17.125827]),
array([1.544344]),
array([1.07336,0.384343,0.11577,0.083594,0.032788,0.051683,0.003096,0.015514,0.002125,0.009466,0.008485]),
array([23.707569]),
array([33.121479,32.859348,29.14812,27.254462,27.327257,23.452711,28.320213,21.411709,29.693271,21.330669,22.860052,28.244939,30.79483,27.034688,29.829413,28.983737,27.278111,26.754152,27.70957,29.928876,27.163908,28.137033,26.612845,26.597391,26.239813,27.710099,21.07246]),
array([31.182426,31.696498,31.668649,32.793539,32.092162,32.216944,32.214437,22.583699,30.454965]),
array([22.56257,23.113968,23.223789,17.030349,16.337716,14.385862,13.667163,21.987586,11.833199,12.548192,15.471832,11.063426,14.841426,13.248948,15.078866,13.167006,13.515012,12.014608,10.426111,11.912118,14.123971,14.227132,10.972686,12.640875,16.140887,14.659528,11.53713,19.381956,7.904156,9.021664,5.99883,13.44571,12.964916,19.793592,18.228073,18.076642,8.119845,19.269232,17.544971,18.673262,20.308248,16.517187,17.792576,19.674469,5.634903,14.404355,15.73021,12.531907,10.756775,10.936013,11.602727,11.789887,12.203228,11.830576,14.00177,15.480901,14.593496,16.41328]),
array([9.963329,9.977074,5.375979,9.885994,9.975404,7.241483,9.585168,8.915356,9.101386,5.054349,4.952019,6.915076,9.676475,9.779666,6.649862,6.880442,5.30865,8.916719,8.007445,9.991455,7.727525,8.250995,3.488889,3.232679,2.964767,3.380778,2.760478,1.89419,2.523573,2.05532,1.993915,3.241156,7.604947]),
array([2.786087,2.675648,3.389036,3.230094,1.969132,4.130725,4.143246,4.658543,4.701682,4.811512,2.302239,4.787989,3.49378,4.317929,4.488782,4.363558,3.225018,2.357411,4.699743,4.89258,3.202754,4.776215,1.876891,2.510696,3.603567,3.784736,3.781741,2.857027]),
array([4.336187]),
array([5.363548,5.287453,6.344396,11.218982,15.231395,9.606215,6.49348,4.29201,9.99586,4.240077,4.309611,4.259517,3.341901,4.620764,3.271126,3.59383]),
array([11.319689,18.276438,11.866204,12.237853,12.415657,13.088325,23.00071,11.194792]),
array([6.396562,6.056895,5.180317]),
array([8.482871,6.843452,8.41012]),
array([7.470887,6.06,20.937356,9.731235,5.052374,9.168874,5.971494,16.883924,7.36645,7.843057,19.016663,8.850157,13.571756,5.318905,6.354793,7.268663,11.930347,12.498719]),
array([7.363533,15.210723,6.157611,7.63907,6.733276,8.016852,9.680839,9.889053,7.338513,9.278898,5.212465,10.378403,14.36453,18.045081,9.253703,8.559931,18.893878,9.160969,19.714284,11.562976,12.931269,6.593361,8.998915,7.980694,7.048535,8.109368,8.675562,7.638497,7.059042]),
array([29.655722]),
array([35.038889,34.700334,36.021865,33.70162,32.172139,26.903741,25.572505,25.249612,22.75905,29.066984,26.252891,26.178526,25.609972,21.489046,22.394065,27.922503,21.411731,20.172611,17.272928,16.426943,13.514153,11.835512,5.452933,20.67075,20.477179,11.717612,11.706245,4.914192,20.117159,12.117251,14.105022,15.166591,5.53201,14.580881,21.477376,7.031771,13.713633,13.672198,14.43739,20.712325,14.918513,9.370555,14.789503,15.025218,14.845191,6.664654,18.099106,4.649181,0.847662,3.351069,3.494102,4.297788,4.309098,3.10993,2.632916,3.992664,4.505917,1.430751,1.631731,0.441755,1.461909,0.480996,1.425675,0.909318,4.340427,17.227992,7.044464,12.229443,2.778759,1.601985,0.348955,2.971232,2.993384,1.810149,0.413678,2.149803,1.822981,2.520719,0.935329,0.072857,1.926316,0.573074,18.652645,4.337903,16.775124,2.971146,12.761709,1.719368,0.649696,0.282138,4.5957,2.848314,26.84783,4.89368,3.422442,6.244887,4.665734,0.584416,17.055554,0.655342,1.866212,0.373784,3.201999,3.623427,0.067793,0.125982,0.042708,0.170769,0.024866,0.08282,0.087027,0.058978,0.124944,5.129958,1.740016,3.584448,0.01913,0.120568,0.094457,20.706008,23.292584,23.675701,20.447482,7.897453,2.500461]),
array([24.939342,8.751239,22.642185,11.630079,12.47205,10.961179,11.377946,9.999724,15.872104,8.021767,11.660587,10.35362,11.610265,7.764486,12.108438,7.965194,6.074227,13.515951,11.113281,10.648716,10.553038,12.9249,11.814546,10.349704,12.358092,3.151922,0.091911,0.087885,0.944483]),
array([5.223888,6.233675,6.329871,2.654751,4.185124,4.620188,4.213242,2.268414,3.148647,2.61404]),
array([6.593409,8.849344,8.17525,3.152395,4.898967,1.904528,3.365539,4.689557,3.98701,4.606489,0.330403,0.330245,0.78504,1.274499,0.942649,1.379823,1.141831,1.026323,0.731113,0.893559,0.6095,0.798599,0.749857,0.011935,2.949158,2.686768,3.593581,3.008889,1.896735,3.452336,2.999008,3.25814,2.871408,2.73309,3.286819,1.219649,0.001724,0.750377,0.846439,10.745474,4.399712,2.10786,0.011343,0.008355,0.00221,0.432795,0.007193,0.005741,0.003967,0.483766,0.068195,2.783904,1.23658,1.935409,0.001557,0.00673,0.006971,0.005328,0.462998,0.002426,2.355851,2.167846,0.001791,17.220496,3.620679,2.465945,4.19067,0.151882,4.894182,2.014336,1.89274,1.492786,2.298545,1.447798,2.084775,0.461031,0.401963,0.445534,4.23668,0.086449,0.419032,5.279942,3.069428,1.66691,2.561676,2.336654,2.99643,1.938176,0.517782,2.050731,2.479509,2.275543,2.425343,2.241088,1.94304,1.296326,0.336848,1.954385,2.131923,0.888936,1.135729,0.591799,2.968291,0.20822,0.173399,0.120525,1.947808,3.174235,2.902223,2.989673,3.113727,1.341829,2.368374,2.178848,1.049285,0.540333,0.512225,4.802493,4.089102,2.571546,2.496943,2.31583,2.128324,1.306526,2.11607,0.044319,2.121691,1.430221,2.361685,2.910948,3.39197,0.954376,1.244006,3.887394,2.766183,3.164492,4.467805,2.355332,1.595308,2.576579,2.696616,3.800572,0.62907,7.730794,3.615789,2.398163,2.155299,1.98777,2.287998,2.456867,2.541737,0.485382,1.868215,0.320394,0.133291,0.375835,0.359084,0.220826,0.906389,0.208409,0.449652,0.558355,2.066286,0.800724,2.349702,2.265138,2.590196,2.971402,2.224116,1.605075,1.863724,0.862167,2.005805,0.337655,0.220034,0.443746,0.357738,0.146629,0.777229,0.374194,0.712346,0.322973,0.806527,3.112143,2.056845,2.105137,0.412018,1.541347,1.825906,0.537197,1.000051,1.640161,4.552732,4.42735,4.422915,3.272513,3.218918,3.973232,2.678296,4.637207,4.885902,2.176483,4.726778,2.093512,3.228038,0.091872,0.077183,0.017471,0.669554,1.830321,0.032481,0.011869,0.008087,0.116623,1.113343,2.824942,3.552361,1.772947,2.281843,1.372364,0.032528,0.114664,0.035517,0.110138,0.120521,0.043031,0.119662,0.92905,20.149407,2.611601,0.095419,0.122763,1.420165,0.082522,5.492277,0.03778,0.009166,1.611925,0.297245,0.007303,0.009123,0.011513,0.001673,10.067832]),
array([0.607326,0.514669,0.612821,0.060628,0.014569,0.752594,1.105566]),
array([0.003885,0.007965,0.574308,1.321479,3.3492,0.211811,0.44193,0.145873,0]),
array([1.465476,1.327539,0]),
array([2.056934]),
array([3.914525,0.900455,0.608113,0.443496,1.689879,1.666231,1.610288,1.522463,1.112574,0.834514,0.581365,1.295107,0.864364,0.08557,0.973655,0.45329,2.244121,1.625115]),
array([0.006229,0.962899,0.389334,0.057688,2.171026,0.007498,2.090448,1.464218,1.718739,2.635504,2.125937,0.396493,0.726214,0.006697,0]),
array([1.616539]),
array([0.390863,1.362387,1.151697,0.845462,0.414859,1.591178,0.927753,0.916226,0.949266,0.171985,0.73159,0.295834,1.661917,0.955486,0.855488,0.084747,0.017497,0.07306,0.039457,0.060901,0.063887,0.033628,0.150545,0.092161,0.058957,0.046664,0.098426,0.073653,0.026345,0.024066,0.133042,1.271249,0.096579,0.064974,0.096558,0.108296,0.023617,0.148109,0.104739,0.076603,0.102703,0.081547,0.178528,0.041135,0.232769,0.096125,0.0647,0.099343,0.035552,0.091313,2.090821,0.056371,0.124868,0.116802,0.07478,0.028736,0.091214,0.034515,0.042479,0.203233,0.090345,0.090486,0.123551,0.114082,0.075296,0.043902,0.097207,0.079327,0.062264,0.401517,1.635882]),
array([3.113782,4.00661,0.89922,1.237793,1.025499,0.789188,4.459284,1.248792,0.866618,0.373637,1.763787,1.500233,2.489714,0.619529,0.705137,1.777264,1.035232,1.303827,4.311999,4.061764,2.905515,2.750066,0.698832,0.495289,1.61462,0.681879,0.722555,0.9347,0.389249,9.69548,4.024245]),
array([0.010619,0.518334,0.004018,0.007892,0.011509,0.003785,0.00579,0.002184,0.004289,0.07703,0.001533,0.001727,0.003767,0.003347,0.008645,0.008757,0]),
array([7.342039,8.812992,8.638521,6.311273,2.162996,1.911161,3.900227,3.736493,3.120693,4.748913,2.146687,2.733222,6.374049,4.941834,9.282113,5.353505,2.192992]),
array([4.404021,3.612124,3.113993,2.71555,4.178612,3.670686,3.586113,4.147591,3.718074,3.249466,0.675418,1.402603,1.762257,0.590759,1.67235,1.249489,0.316671,1.452355,0.410265,1.333711,1.590555,1.63677,0.397351,1.329804,0.319939,1.188974,0.977982,0.732434,0.751573,1.793175,0.196523,1.452541,1.057006,1.763724,1.422963,1.766135,1.295157,1.183917,0.181437,1.758266,0.756201,1.447783,0.430362,1.77171,1.421174,0.012894,0.029914,0.111383,0.01587,0.096393,0.04102,0.020271,0.062597,0.115552,0.019174,0.023237,0.062548,0.025384,0.047438,0.118436,0.011543,0.111638,0.111418,0.026434,0.010726,0.702141,0.045307,0.067263,0.098273,0.092666,0.083815,0.123844,0.058565,0.037172,0.007384,0.012435,0.047204,0.021366,0.09894,0.029938,0.086081,0.044986,0.136615,0.142578,0.092121,0.084114,0.116067,0.062065,0.012664,1.635968,0.489883,0.793648,0.47159,0.824506,0.002915,0]),
array([5.785016,4.736127,2.799702,3.188422,3.293493,3.190472,4.838991,3.968246,2.026228,4.880178,3.160694,1.82222,3.071242,4.1957,4.202239,2.399643,2.122923,4.772269,4.846594,3.468769,3.642018,3.88896,3.72285,4.796374,4.761008,4.613642,2.1326,2.290605,3.755387,3.071325,3.223109,4.644635,2.994939,2.247864,2.652334,0.123955]),
array([0.491743,1.389021,0.378231,0.498732,0.114221,0.071827,0.018043,0.112869,2.439831,2.032109,0.95703,1.497493,0.266166,0.342257,2.666749,1.294299,0.405337,0.687645,0.696445,2.317013,0.271958,0.359506,0.534557,2.216253,1.296619,1.518634,0.466275,0.751912,0.433926,0.475938,0.063425,0.028876,0.049753,0.067967,0.016038,1.739209,0.334691,0.38039,0.754093,0.466037,0.242266,0.386028,0.706442,0.012525,0.448349,0.774132,0.285017,0.553992,0.12051,0.361758,0.351697,0.496235,0.327275,0.763988,0.198818,0.528124,1.337567,0.421837,0.755048,0.46781,2.21758,0.398843,0.00112,0.004928,1.0295,0.530944,2.62721,0.0231,0.066105,0.050464,0.057106,0.012461,0.032441,0.028465,0.092497,0.122277,0.004926,0.122903,0.058047,0.111918,0.242041,0.015061,0.048141,0.080606,0.098953,0.065098,0.06125,0.111969,0.017393,0.292966,0.125839,0.082948,0.068211,0.012186,0.009913,0.004253,0.001747,1.038514,0.036574,0]),
array([1.303043,4.476426,4.348492,0.002204,0.002676,2.969817,0.132953,1.742603,2.700371,1.916506,1.634536,0.002302,0.710829,1.255238,0.010455,1.603129,0.858461,0.869762,0.495393,1.877902,0.236277,0.178515,0.891383,2.486618,1.924616,2.189761,2.449796,0.343058,0.022402,2.515694,3.749175,1.899885,1.252067,1.278363,2.068589,2.047494,1.702425,4.132616,1.873553,4.728904,2.033798,1.633187,0.005104,0.05314,0.073111,2.266081,2.078461,0.089436,0.086269,0.687686,1.444029,2.442816,0]),
array([0.800773]),
array([2.384647,1.886751,3.898566,1.462002,2.202217,1.76676,0.111375,0]),
array([4.328296]),
array([15.103396,17.163393,13.750668]),
array([11.097914,11.290273,13.690813,14.377513,15.00237,14.565736,14.916675,14.786847,14.03882,15.163907,10.89155,14.676127,15.353411,14.371685,13.392676,15.655033,15.578801]),
array([6.565291,5.906376,8.651001]),
array([10.43785,12.037048,12.566431,10.881348,10.985329,13.475858,11.116604,11.187436,12.570304,20.870684,21.698619,12.046252]),
array([13.598653,10.560599,13.479601,11.458852,11.496778,13.591297,10.969221,10.346387,7.730403,13.883252,14.086159]),
array([2.676549,5.148629]),
array([6.327503,2.385582]),
array([0.009367,0.048979,0.002371]),
array([41.486611]),
array([0.202098]),
array([0.840719,0.638143]),
array([1.830404,2.17623]),
array([28.749542]),
array([28.185861,24.929008,28.306247,26.489065,24.680405,19.266248,15.81916,24.244918,25.259635,26.083077]),
array([29.642923,28.945282,23.889624,21.819112,22.472276]),
array([1.141356]),
array([0.719033,0.604813,0.398188,0.372386,0.371121,0.139869,0.709881,0.218967,0.275735,0.56325,0.338772,0.040622,0.538103]),
array([2.285649,0.378214,0.111006]),
array([22.881748,20.777975,22.930503,23.662284,23.838141,21.206338,17.159936,16.166062,19.675748,16.927958,18.277732,18.376019,18.919926,16.157184,16.809979,18.903339,20.040817,16.208319,16.281749,20.380555,16.989235,17.342407,20.083949,17.61983,19.397782,16.265913,20.417499,18.140246,14.055124,16.900996,17.476203,17.0835,18.365333,20.012011,20.024498,16.210737,18.368057,16.660458,16.097875,19.479157,16.521389,16.816865,14.81463,15.729907,14.274336,14.754538,23.030529]),
array([17.946895,18.302099]),
array([13.934753,17.586402]),
array([23.613756]),
array([25.882868,20.481105,26.941997,30.354927,30.149143,21.429349]),
array([21.92724,21.041837,23.779253,21.717507]),
array([30.56394,26.40804,30.770044,29.898214,27.117268,26.965254,29.360156,29.412237,29.434985]),
array([18.596057,18.79819]),
array([12.250507,14.775281,14.655383]),
array([10.585487,12.641783,18.746993,12.735054,11.917066,13.331126,12.045643,11.43187,11.130081,13.328106,15.440057,10.632438,13.596304,11.169962,6.838427,5.017231]),
array([14.003502,15.043426,15.211244]),
array([15.224365,17.547899]),
array([13.919087,13.719269,15.874061,15.326008,14.910254,14.367484,13.890885]),
array([12.448914,10.816714,12.569957]),
array([14.195157]),
array([24.506078]),
array([31.446469,31.802933,32.11907,32.58999,32.494875,31.371128,32.467538,32.851742,23.203668,26.300049,25.356532,23.101109,27.597931,26.734477]),
array([32.155776,30.054195,31.768694,47.495519,36.828252,37.324773,34.942804,49.79479,29.417735]),
array([36.337483,36.803325,36.571528,37.264341,34.959981]),
array([0.237836,0.445886,0.298466,0.222302,0.053011,3.360206]),
array([0.081123,0.736644,1.638859,0.181461]),
array([23.96457]),
array([17.824282,19.484773,17.5661,17.845266,19.329104,18.667212,16.506186,18.483185]),
array([23.283495,20.498375,21.621306,23.170511,22.100664,24.542349,23.257601,23.716048,27.798695,22.18843,24.124027,23.914426,21.091233,21.633084,23.043326,22.127219,24.274766,24.057599,23.360001,23.852718,23.81778,17.506039,19.439123,18.741986,18.415696,19.954038,16.917382,18.190508,17.693983,19.808308,26.852888,13.640495,17.936971]),
array([0.008518,0.004554,0.06994,1.330885,0.003684,0.005277,0.562306,0.085197]),
array([0.076491,0.777978,0.180452,0.064778,0.034876,0.057712,0.60515]),
array([1.620657]),
array([0.416055]),
array([31.960964,25.291365]),
array([21.3911]),
array([16.560759,16.923658,19.604425]),
array([32.672143,26.819854,29.669527,20.822995,27.686235,24.841575]),
array([20.705513]),
array([30.377204,24.386564,26.142816,26.667652,24.500843,21.61284,20.831187,22.978006]),
array([21.771723,27.999099,23.34657,26.077524,25.824413,29.315428,26.714223,28.290691,22.798535,25.101042]),
array([28.597168,25.614916]),
array([5.563783,7.030806,13.283934,5.64184,6.347723]),
array([9.032532]),
array([17.170313,8.660969,7.881701,13.889479,5.317282,5.362324,8.361262,10.466696,13.557968,11.042105,12.126682,9.090703,6.851547,13.277652,10.612116,12.489724,6.268085,11.734402,7.568764,13.580438,10.933884,13.337535,12.592004,5.779502,5.24893,11.181939,11.578751,6.707356,5.847781,7.714691,12.562859,10.124206,11.99209,13.115963,11.843369,8.236683,12.007603,6.130515,21.179403,21.505337,8.506735,9.322058,10.584114,7.892663,7.378578,7.453636,12.442319,12.512129,10.231696,15.399923,7.344022,11.693655,10.040386,5.589485,8.173398,12.402716,6.540626,13.041505,11.063883,7.488133,19.923862,13.37581,11.579292,12.25058,14.342394,10.233957,10.253468]),
array([13.310936,6.863055,5.455267,10.403137,11.937337,13.225137,12.607619,6.950521,8.351756,6.895672,13.23582,10.99949,13.215619,13.095252,10.614363,11.578418,11.314538,11.912274,13.59912,12.558785,11.284123,11.932582,10.926018,12.518333,11.784509,12.452867,10.949012,7.808523,8.709996,10.616533,10.261812,11.826246,13.329027,11.251602,10.874068,8.760516,12.210296,11.501581,11.350888,6.831904,12.891856,5.080641,10.544291,10.899129,8.238247,5.903519,9.478474,13.199504,10.427792,13.18172,11.775215,12.242861,11.029825,9.199635,4.934424,15.439907,14.072104,15.142014,14.333957,14.085569,14.784364,13.406007,18.990276,11.900983,9.186043,14.262578,13.150942,11.536867,7.361019,11.62777,13.193556,11.497974,12.790354,15.820058,10.097553,20.610088]),
array([8.266734,5.219313,11.210236]),
array([9.459388,10.221172,8.074348,5.664459,10.260046,7.897334,9.238789,8.088666,5.691893,6.458227,10.093391,9.272969,8.242802,5.25796,9.996122,9.661522,8.585025,2.079843,5.204975,9.226793,8.184348,7.337692,9.979039,8.622074,8.436016,10.218372,7.642746,10.164512]),
array([13.134115]),
array([13.910701,16.064349,18.02626,14.441252,14.406042,14.121716]),
array([20.109562]),
array([6.210475,12.97339]),
array([41.611028,38.795313,35.890167,36.298477,34.568449,36.844293,35.705284,35.206716,35.828781,34.796889,36.40161,35.820785,36.00635,36.966931,34.422164,36.199607,35.876571,33.591059,33.693862,33.741335,33.481242,33.702314,33.891584,33.596233,33.515071,33.618194,33.425207,28.053873,31.759824,31.816831,32.143181,32.32824,31.692606,28.575254]),
array([33.488901,33.674034]),
array([39.536663,35.590336,36.584719,34.227093,35.418614,34.244629,34.415671,35.456276,35.385367,35.488423,36.723958,36.482547,36.696452,37.073143,36.302468,34.823382,34.006755,35.456295,34.935617,36.039531,35.240402,36.765256,35.546827,34.144223,36.008751,35.449328,35.580573,34.727913,34.219244,35.555158,34.001596,35.998776,35.387389,36.776996,34.081055,36.686402,35.524536,35.058408,33.839686,33.592123,33.569657,33.810249,33.624517,33.343027,33.765517,33.435135,33.701558,33.32154,33.65386,33.498041,33.761784,33.705228,33.308842,33.30164,33.770967,33.719893,33.456305,33.805394,33.688441,33.514647,33.615447,33.384608,33.802424,33.796763,33.309434,33.714458,33.534499,33.728529,33.325349,33.480121,33.410413,33.551898,33.329388,33.640708,33.819488,33.379117,33.690773,33.620627,33.573464,33.757601,33.480271,33.818815,33.535431,33.678424,33.537019,33.333982,33.453569,33.753629,33.76207,33.65391,33.707201,33.678974,33.80312,33.43463,33.787777,33.319479,33.346144,33.722252,33.772707,33.669158,33.442729,33.44132,33.4429,33.691404,33.836414,33.758639,33.596978,33.538877,33.781518,33.406798,33.848276,33.666692,33.636998,33.309169,33.574221,33.409449,33.332825,33.402132,33.370075,33.639918,33.81736,33.755339,33.892786,32.861536,31.431087,32.191075,33.042749,31.811175,32.285122,30.940549,35.309809,36.721114,33.808865]),
array([26.391611,24.417007]),
array([24.406798,23.123135,15.901929,11.337848,14.519646,12.128686,10.688118,18.532638,15.365835,13.475967,15.273141,27.233993,14.521578]),
array([28.89721]),
array([28.721041,21.972309,25.827375,30.36418,29.204282]),
array([24.681409,24.135414,20.977809,23.070454,22.524132,21.842073]),
array([14.61694,17.634996,19.524785,17.955983,17.165426,24.391391,19.002925,19.004964,20.25678,16.666577,17.20779,18.046037,19.054649,18.47788,14.189428,14.484127,14.938908,14.508592,14.31234,13.993853,14.426618,15.57136,15.049831,15.104837]),
array([11.673195,12.216474,11.657405,12.319649,10.765058,13.539067,13.499764,12.183165,11.132271,13.20441,11.61358,12.034352,12.819569,10.469638,12.08936,11.613908,10.863971,12.101549]),
array([21.461781]),
array([12.106824]),
array([15.205857,14.789673,16.813161,10.377864,14.071184,14.513558,13.335739,15.924777,14.976316,14.114301,14.714409,14.787856,14.406042,15.73189,13.664874,14.29546,15.512103,11.507626,14.771886,15.244316,14.656353,12.06059,15.645034,12.552102,13.438667,14.413154,10.818944,11.096541,10.450856,14.129713,13.903631,14.136959,13.766569,14.358321,13.725584,12.023395,10.319731,12.646669,12.525749,13.160694,10.743539,13.18612,15.934844,11.100295,10.032856,7.15655,12.106844,11.604495,6.270321,13.09973,13.326826]),
array([21.703945,18.301347,24.302939,19.05927,20.350995,26.086528]),
array([1.667955,1.350943,1.164652,2.357531,0.079698,0.452105,2.610279]),
array([0.007546,2.340883,1.031087,0.314134,0.441769,1.947228,1.937958,0.867261,1.3377,0.084266]),
array([20.50505]),
array([20.747807,21.459545,25.665483,27.183331,24.602906]),
array([23.450613,22.836681]),
array([33.310523,32.929776,32.740598,32.724818,31.293932,32.340688,31.842745,32.634972,33.283351,32.028958,33.090505,31.561002,31.608621,32.702104,30.095063,27.156732,29.849052,28.913612,26.305677,20.99667,21.607221]),
array([8.133856]),
array([10.602618,8.325497,13.257888]),
array([5.045161,5.144703,7.545234,9.85273,12.06163,21.239021]),
array([18.354231]),
array([19.503054,18.274396,17.14043,16.971155,19.971584,16.41251,19.023577,18.5282,18.567437,17.294686,16.541232,18.266775,17.514422,18.60275,18.212847,17.542771,20.304786,19.442132,18.920614,19.869875,19.766929,13.519748,16.620083,17.703551,19.049504]),
array([16.288681,15.163905,18.579504,17.585814,20.265867,19.697859,16.96182,20.373946,15.386747,16.756992,19.816856,20.154017,14.822525,10.376554,13.931787,19.384545,15.438001,15.42464,15.17624,8.408579,14.757176,15.199306,14.637645,14.216544,14.090969,15.563943,14.066137,14.918644,14.458784,14.137051,14.451715,14.67622,15.961986,15.367507]),
array([44.02543]),
array([4.615155,1.840929,4.563568,3.094056,2.126277,2.615666,3.052233,0.538257,3.795321,5.292774,4.292653,3.820524,2.39272,3.448971,4.978654,4.83811,2.520796,3.917767,7.675367,3.500053,3.6388,3.604176,2.127358,3.010429,2.287876,2.077872,1.936921,2.2397,2.796335,2.560849,3.453639,0.829779,2.307976,4.231587,3.767198,3.091737,1.518288,1.353448]),
array([3.279827,3.516714]),
array([1.314292,0.124919,0.012429]),
array([22.808931,20.380129]),
array([15.760326,17.461113,17.708432,18.403724,19.669254,20.356264,19.168508,19.684442,18.754696,14.829772,15.10196,14.22135,15.522879,15.692177]),
array([19.018653,16.22925,16.782453,18.767373]),
array([33.768537,33.14506]),
array([18.742966,16.197062,18.558322]),
array([32.728561,31.811307,23.581288]),
array([30.213787]),
array([20.742527,21.757039,23.386447,21.172333,27.372115,29.672452]),
array([33.351332,33.758294]),
array([1.702582,0.207104,2.684636,1.102553,1.468102]),
array([0.006541,0.006513,0.11893,0.403798,0.684388,1.395293,0.056488]),
array([33.238812,31.949437]),
array([32.324353,32.908315,31.357277,32.569698]),
array([16.923857,18.131992,12.359649,19.24912,18.555478,7.500957,18.660785,20.419541,18.555248,19.076834,15.118088,15.103489,12.220152,20.991221,15.177949,14.998574,13.878928,13.880799]),
array([19.009959,19.67329,16.769354,15.100136,17.064877]),
array([26.941463,28.098372,27.001656,29.937801,30.304476,23.531315,22.464307,26.213297,23.433354,23.264439,23.189716,25.939344]),
array([23.091663,20.796194]),
array([24.099271,23.761282,22.225268,24.319805,21.131919,21.12671,30.155865,25.576045]),
array([11.1415,11.030607,12.220232,9.728405,12.961331,22.655887,12.973867,11.625953,14.157889,11.852938,10.408851,13.368634,12.310206,10.651919,13.508718,12.858007,13.575485,11.594431,13.377522,10.476311,10.842689,10.5366,12.227239,12.070281,13.451454,13.379954]),
array([15.356329,14.155551,14.653198,15.969495,15.850198,15.400043,15.687177,15.96838,15.150924,14.312045,14.68253,14.196972,14.105988,15.594357,13.672079,5.44984,14.609842,15.069004,14.862886,13.681222,15.851209,13.637596,14.765605,15.672443,15.487539,11.032305,13.683471,15.72305,15.15685,15.556317,14.643388,14.360621,15.518054,15.339165,14.812156,19.99405,16.514894,15.716962,14.138826,14.542987,14.588777,15.115767,14.02101,14.601116]),
array([26.105176,29.223635,27.041666,29.420933,29.403825,27.309952,27.917655,23.71548]),
array([22.910287,20.735003,17.487441,19.874389,22.691011,20.090715,16.925643,17.059568,25.837641]),
array([23.531893]),
array([20.869138,20.45153,21.48262,21.271874,23.57273,21.440001,22.668042,22.925655]),
array([32.981399,27.856748,21.194815]),
array([21.491883,23.703419,19.544772,19.296724,20.34177,19.612607,19.176344,20.310516,19.432653]),
array([17.623044]),
array([16.533262,19.111579,19.931754,19.88946,16.893159]),
array([28.502154,25.316799,24.213692,21.125925,21.392082,20.793687,21.745926,24.503178,24.397852,21.315945,21.76788,19.859939]),
array([24.493]),
array([25.31221,27.099168,23.231443,23.972145]),
array([16.713949]),
array([33.817151]),
array([15.317228,15.465484,14.5863,13.90079,15.060367]),
array([1.588475,2.174883,0.4022,1.483105,0.807342,0.02687,0.077917]),
array([0.227489]),
array([1.116809]),
array([0.226525,0.079489,0.120324,0.095439,1.244417,0.28597,0.024864,0.051235]),
array([16.550266,20.361178,16.785674,19.885473,16.813599,17.880543,18.861204,20.416725,17.008763,16.63405,17.374463,17.429882,16.379454,17.280495,18.524596,18.643951,19.020818,18.638748,17.30092,19.553681,13.615868,19.743205,16.502234,15.902854,13.896491,13.87586,20.522643]),
array([14.52829,17.020888,16.155228,13.762122]),
array([0.011281,1.526534,0.628768,0.45296,0]),
array([23.699407,27.400021,29.090482]),
array([1.331966]),
array([0.00739]),
array([23.215836,21.271515,28.181067,28.23692,27.048571]),
array([14.542161,14.416995,13.456787]),
array([0.106665,0.876654,1.176325]),
array([2.218221,1.893358]),
array([14.421382,15.221983,12.247385,14.930905,13.027447]),
array([16.678097,18.653752,20.162564,20.410573,15.517781,16.597911,17.586029,18.199265,16.970891,16.69573,18.392051,14.807854,19.957783,12.602664,16.039304,15.359838,15.801079,18.454765,20.386229,14.50902]),
array([17.928456,18.687238,18.656405,15.141419,19.090104,16.10458,16.561684,16.445783,16.251388,17.323603,19.631537,13.905023,19.220871,16.002314,20.303329,18.638274,15.848386,14.742267,13.75671,15.658054,14.430941,15.890616,15.22212,14.597998,13.769539,14.576829,14.838859,14.915519,15.402713,14.206576,13.970718,14.554065,13.628636,19.692391,15.522798]),
array([2.471109,0.490801,1.309322,1.32946,0.075383,0.021811,0.061831,0.053993,0.195081,10.378156]),
array([2.216699,0.938988,1.449769,0.946479,1.439584,1.459684,0.514719,0.104164,1.018273,0.053092,0.089138,0.076034,0.120644,0.124518,1.668993,0.062302,1.80969,0.054498,0.059852,0.064081,0.036122,2.134436,0.046414,0.084209,2.437932,0.02572,0.003005,0.053158,0.10536,0.021898,0.048344,0.028968,0.034553,0.075026]),
array([2.427813]),
array([3.249796,3.973099,3.68351,2.223128,1.937754]),
array([0.818474,0.632978]),
array([3.617265]),
array([5.625971]),
array([6.230874,9.398893,9.050299,10.143379,2.667057,1.623195,1.258128,0.575394,1.489967,1.646274,0.437698,1.545377,0.495313,0.457917,0.063072,0.204598,4.265474,5.007601,0.474745,0.848527,1.712416,3.490166,1.529313,1.4769,3.40645,4.90766,3.377407,1.407128,0.915526,1.42687,0.704809,0.20298,3.551037,0.388,2.959489,3.166694,0.014407,1.202129,1.345521,1.689114,1.888837,0.01186,3.205827,0.723116,2.377994,0.870843,3.097562,2.337789,3.146608,3.180125,2.838502,2.731589,2.605502,1.947046,2.059726,1.430637,1.946409,1.109033,0.61246,0.20543,0.080829,2.528784,2.506504,2.05223,0.460525,3.380697,0.091649,0.220754,1.411319,2.271924,0.943682,1.900821,3.041293,6.74035,4.122598,1.041687,1.127216,0.589709,3.798576,0.080426,0.065932,0.021998,0.127035,0.533764,2.133131,0.022025,0.345826,2.09416,0.304521,2.895958,1.857564,2.015306,0.516468,0.485421,0.74456,2.496214,0.372491,3.355527,3.289014,2.66785,2.262977,0.10801,0.045022,0.052501,3.565385,1.671061,3.613486,0.028933,0.032319,0.12422,0.015156,4.777697,1.5784,1.493814,0.022792,0.00333]),
array([0.039702]),
array([0.002143,0.390903,0.010348,1.171163,0.011068,0.009726,0.002957,2.291376,0.007765,0.007453,0.006079,0.863164,1.033119,0.667329,1.20353,1.03222,0.053129,2.333029,0.888933,1.420586]),
array([11.485101]),
array([4.518674]),
array([5.100066,8.199362,9.28676,9.471467,9.213295,6.81527,8.240904,6.996787,8.479932,9.481779,5.503979,0.502388,7.277632,5.353867,5.194126,6.460438,9.25757,6.948718,5.569268,8.947321,15.165773]),
array([4.663408,0.418386,1.603836,0.754519,0.47561,1.679949,1.222499,0.8591,1.265119,0.019794,0.053259,0.124236,0.111359,0.088192,0.054656]),
array([1.297608,1.053535,1.235904,0.900674,0.072217,0.026219,0.124768,0.470651,0.983466,2.454049,0.633663,0.61275,0.094894,0.186065,0.120171,0.342836,1.711221,0.727761,0.696922,3.169255,1.936586,0.061728,0.315063,0.61495,0.056458,0.310487,0.792475,0.555252,0.108752,0.179736,0.444596,0.176054,2.569024,2.38754,1.464133,0.062653,1.789611,0.563406,0.774708,0.161402,2.211851,0.441359,0.061531,0.103654,0.260258,0.017035,0.039423,0.106526,0.103663,0.106215,0.100127,0.024156,0.093627,0.100688,0.03289,0.054835,0.014839,0.094631,0.087661,0.863682,0.07119,0.008339,0.00346,0.003096,0.029068,2.515494,0.074783]),
array([0.05335]),
array([0.103043]),
array([0.489668,1.238417,2.184606]),
array([1.700589,1.379254,0.233323,1.108207,0.147211,1.424736,0.778773,2.364628,0.404918]),
array([1.171401])
]

d=[data_1]
names=[ 'canid_occ_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Aelurodon','Aelurodon_asthenostylus','Aelurodon_ferox','Aelurodon_mcgrewi','Aelurodon_montanensis','Aelurodon_stirtoni','Aelurodon_taxoides','Aelurodon_wheelerianus','Alopex','Alopex_lagopus','Archaeocyon_falkenbachi','Archaeocyon_leptodus','Archaeocyon_pavidus','Borophaginae','Borophagus','Borophagus_diversidens','Borophagus_dudleyi','Borophagus_hilli','Borophagus_littoralis','Borophagus_orc','Borophagus_parvus','Borophagus_pugnator','Borophagus_secundus','Caedocyon_tedfordi','Canidae','Caninae','Canini','Canis','Canis_(Pseudalopex)','Canis_adustus','Canis_anthus','Canis_apolloniensis','Canis_armbrusteri','Canis_aureus','Canis_cedazoensis','Canis_dirus','Canis_edwardii','Canis_familiaris','Canis_ferox','Canis_latrans','Canis_lepophagus','Canis_lupus','Canis_mesomelas','Canis_proplatensis','Canis_rufus','Canis_thooides','Carpocyon','Carpocyon_compressus','Carpocyon_limosus','Carpocyon_robustus','Carpocyon_webbi','Cerdocyon_avius','Cerdocyon_texanus','Cerdocyon_thous','Chailicyon_crassidens','Chrysocyon','Chrysocyon_brachyurus','Chrysocyon_nearcticus','Cormocyon','Cormocyon_copei','Cormocyon_haydeni','Cubacyon_transversidens','Cuon','Cuon_alpinus','Cynarctoides_acridens','Cynarctoides_emryi','Cynarctoides_gawnae','Cynarctoides_harlowi','Cynarctoides_lemur','Cynarctoides_luskensis','Cynarctoides_roii','Cynarctoides_whistleri','Cynarctus','Cynarctus_crucidens','Cynarctus_galushai','Cynarctus_marylandica','Cynarctus_saxatilis','Cynarctus_voorhiesi','Cynarctus_wangi','Cynodesmus_martini','Cynodesmus_thooides','Cynodictis','Cynodictis_lacustris','Cynotherium','Cynotherium_sardous','Desmocyon','Desmocyon_matthewi','Desmocyon_thomsoni','Dusicyon','Dusicyon_avus','Dusicyon_culpaeus','Dusicyon_sechurae','Ectopocynus_antiquus','Ectopocynus_intermedius','Ectopocynus_simplicidens','Enhydrocyon','Enhydrocyon_basilatus','Enhydrocyon_crassidens','Enhydrocyon_pahinsintewakpa','Enhydrocyon_stenocephalus','Epicyon','Epicyon_aelurodontoides','Epicyon_haydeni','Epicyon_saevus','Eucyon','Eucyon_davisi','Eucyon_skinneri','Euoplocyon_brachygnathus','Euoplocyon_spissidens','Gobicyon','Hesperocyon','Hesperocyon_coloradensis','Hesperocyon_gregarius','Hesperocyoninae','Leptocyon','Leptocyon_delicatus','Leptocyon_douglassi','Leptocyon_gregorii','Leptocyon_leidyi','Leptocyon_matthewi','Leptocyon_mollis','Leptocyon_tejonensis','Leptocyon_vafer','Leptocyon_vulpinus','Lycaon','Lycaon_pictus','Mesocyon','Mesocyon_brachyops','Mesocyon_coryphaeus','Mesocyon_temnodon','Metalopex_bakeri','Metalopex_macconnelli','Metalopex_merriami','Metatomarctus','Metatomarctus_canavus','Microtomarctus_conferta','Neovulpavus_washakius','Nyctereutes','Nyctereutes_abdeslami','Nyctereutes_procyonoides','Osbornodon_brachypus','Osbornodon_fricki','Osbornodon_iamonensis','Osbornodon_renjiei','Osbornodon_scitulus','Osbornodon_sesnoni','Osbornodon_wangi','Otarocyon_cooki','Otarocyon_macdonaldi','Otocyon','Otocyon_megalotis','Oxetocyon','Oxetocyon_cuspidatus','Paracynarctus_kelloggi','Paracynarctus_sinclairi','Paraenhydrocyon_josephi','Paraenhydrocyon_robustus','Paraenhydrocyon_wallovianus','Paratomarctus_euthos','Paratomarctus_temerarius','Philotrox_condoni','Phlaocyon','Phlaocyon_achoros','Phlaocyon_annectens','Phlaocyon_latidens','Phlaocyon_leucosteus','Phlaocyon_mariae','Phlaocyon_marslandensis','Phlaocyon_minor','Phlaocyon_multicuspus','Phlaocyon_taylori','Phlaocyon_yatkolai','Protemnocyon_inflatus','Protepicyon_raki','Protocyon','Protocyon_orcesi','Protocyon_tarijensis','Protocyon_troglodytes','Protomarctus_optatus','Psalidocyon_marianae','Pseudalopex_gymnocercus','Rhizocyon_oregonensis','Speothos','Speothos_venaticus','Sunkahetanka_geringensis','Tephrocyon_rurestris','Theriodictis','Theriodictis_floridanus','Tomarctus','Tomarctus_brevirostris','Tomarctus_hippophaga','Urocyon','Urocyon_cinereoargenteus','Urocyon_citrinus','Urocyon_galushai','Urocyon_minicephalus','Urocyon_progressus','Urocyon_webbi','Vulpes','Vulpes_cascadensis','Vulpes_chama','Vulpes_kernensis','Vulpes_mathisoni','Vulpes_stenognathus','Vulpes_velox','Vulpes_vulpes','Vulpes_vulpes_macroura','Vulpini','Xenocyon','Xenocyon_lycaonoides','Xenocyon_texanus']
def get_taxa_names(): return taxa_names
