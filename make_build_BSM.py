#!/usr/bin/env python

import mg5_utils.mg5_utils as mg5
import apollon_utils.apollon_utils as apollon
import utils.utils as utils
import root_utils.root_utils as root_utils
import yaml
import shutil
import os


# - Tag
tag               = '2HDM_Epsilon_Point_C'

# - 
run_config_path   = './config/run_config/13_TeV.yml'
model_config_path = './config/models/2HDM.yml'
plot_config_path  = './config/plot_config/2HDM.yml'

# - Apollon
prog           = 'RunAnalysis-Zh-PartonLevel-with-cuts'
work_dir       = os.path.join( './results/', tag )
apollon_dir    = os.path.join( './results/', tag, 'apollon/' )
root_file_path = os.path.join( apollon_dir, 'ana.root' )
sample_dir     = os.path.join( './results/', tag, 'samples' )
comp_config    = os.path.join( apollon_dir, 'apollon.conf')
bin_config     = '/scratch/de3u14/2HDM-Zh/MadGraph/analysis-v2/apollon_config/bin_parton_level_with_cuts.conf'
nEvents        = -1

info_file_path  = os.path.join( sample_dir, 'info.dat')
process_prepath = '/scratch/de3u14/2HDM-Zh/MadGraph/analysis-v2/mg5_processes'

### --- Load in model config path
with open( model_config_path ) as f:
    model_config = yaml.safe_load(f)

### --- Load in model config path
with open( plot_config_path ) as f:
    plot_config = yaml.safe_load(f)

utils.mkdir_p( sample_dir  )
utils.mkdir_p( apollon_dir )

# - Do not overwrite
if not os.path.isfile(info_file_path):
    if model_config['param_pt']:
        shutil.copyfile( model_config['param_pt'], info_file_path )

#### --- Loop over the components
for component in model_config['components']:

    tag = '{}'.format( component )
    process_dir = os.path.join( process_prepath, "{}_{}".format( model_config['model_name'], component ) )

    mg5.generate_event_sample( tag, process_dir, run_config_path, sample_dir, info_file_path,
            model_config_path )

### --- Create Apollon component config

#apollon.create_component_config( work_dir, tag, model_config, info_file_path, info_file_index = 0 )

### --- Run Apollon

#apollon.launch_apollon( prog, apollon_dir, comp_config, bin_config, nEvents )

### --- Plot

#root_utils.plot_multiple_components( work_dir, root_file_path, plot_config, info_file_path )

#def plot_multiple_components( work_dir, root_file, plot_config, info_file_path, info_file_index=0 ):
