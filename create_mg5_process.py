#!/usr/bin/env python

import mg5_utils.mg5_utils as mg5

# - Standard Model
mg5.create_MG5_process_dir('sm',                'p p > z h',                       './mg5_processes/SM_qq_Zh/'     ) # - qq
mg5.create_MG5_process_dir('loop_sm_hZZ_added', 'g g > z h [noborn=QCD]',          './mg5_processes/SM_gg_Zh_SM/'  ) # - gg - SM
mg5.create_MG5_process_dir('loop_sm_hZZ_added', 'g g > z h [noborn=QCD] HZZ^2==0', './mg5_processes/SM_gg_Zh_box/' ) # - gg - box
mg5.create_MG5_process_dir('loop_sm_hZZ_added', 'g g > z h [noborn=QCD] HZZ^2==1', './mg5_processes/SM_gg_Zh_int/' ) # - gg - int
mg5.create_MG5_process_dir('loop_sm_hZZ_added', 'g g > z h [noborn=QCD] HZZ^2==2', './mg5_processes/SM_gg_Zh_tri/' ) # - gg - tri

# - 2HDM - Type-II
mg5.create_MG5_process_dir('2HDMtII_NLO_hZZ_added','p p > z h1 HZZ^2==2',                   './mg5_processes/2HDMtII_NLO_qq_Zh/'     ) # - qq
mg5.create_MG5_process_dir('2HDMtII_NLO_hZZ_added','g g > z h1 / h3 [noborn=QCD]',         './mg5_processes/2HDMtII_NLO_gg_Zh_SM/'  ) # - gg - SM
mg5.create_MG5_process_dir('2HDMtII_NLO_hZZ_added','g g > z h1 / h3 [noborn=QCD] HZZ^2==0','./mg5_processes/2HDMtII_NLO_gg_Zh_box/' ) # - gg - box
mg5.create_MG5_process_dir('2HDMtII_NLO_hZZ_added','g g > z h1 / h3 [noborn=QCD] HZZ^2==1','./mg5_processes/2HDMtII_NLO_gg_Zh_int/' ) # - gg - int
mg5.create_MG5_process_dir('2HDMtII_NLO_hZZ_added','g g > z h1 / h3 [noborn=QCD] HZZ^2==2','./mg5_processes/2HDMtII_NLO_gg_Zh_tri/' ) # - gg - tri
mg5.create_MG5_process_dir('2HDMtII_NLO_hZZ_added','g g > h3 > z h1 [noborn=QCD]',         './mg5_processes/2HDMtII_NLO_gg_Zh_A/'   ) # - gg - A
mg5.create_MG5_process_dir('2HDMtII_NLO_hZZ_added','g g > z h1 [noborn=QCD]',              './mg5_processes/2HDMtII_NLO_gg_Zh_all/' ) # - gg - all

# - Testing
#mg5.create_MG5_process_dir('loop_sm_hZZ_added', 'g g > z h [noborn=QCD]','./mg5_processes/SM_gg_zh_SM/'  ) # - gg - SM
