# 2020-09-08 - Mathias Berggren - Siemens TM
import os
from shutil import copyfile
from progress.bar import IncrementalBar

# ------ Project specifics ------ 
source_dir = '..\..\..\..\GabrielLindman\Summer2020\HEEDS_final\HEEDS_dataForML\HEEDS_v6_Study_3\HEEDS_0'
dest_dir = '.\ML-data\\'
missing_files = 'missing_files.txt'
files = ['exporter.inp', 'Disc_MI_steady_state.dat', 
            'Disc_MI_steady_state.odb', 'SMax_CAX6.txt', 'SMax_CAX8.txt']

f_design_variables = '\design_variable_and_parameter_values'
copyfile(source_dir + '\\Design1\\' + f_design_variables, dest_dir + \
            f_design_variables)
# ------------------------------ 

# Progress Bar
bar = IncrementalBar('  Fetching files', 
        max=len(os.listdir(source_dir))*len(files),\
        suffix='%(index)4i/%(max)i files processed : estimated time left '\
        + '%(eta_td)s : %(percent).1f%%')

# Avoid extra \n
first = True

for _map in os.listdir(source_dir):
    try: 
        os.mkdir(dest_dir + _map)
    except OSError:
        if(not os.path.exists(dest_dir + _map)):
            with open(missing_files, 'a') as out:
                out.write(_map + "\n")

    for f in files:

        try: 
            source = f'{source_dir}\\{_map}\\abaqus\\{f}'
            destination = dest_dir + _map + '\\' + f
            copyfile(source, destination)
        except: 
            with open(missing_files, 'a') as out:
                if (first):
                    first = False
                else: 
                    out.write("\n")
                out.write(f'{_map}\\abaqus\\{f}')

        bar.next()

bar.finish()

if(os.path.isfile(missing_files)):
    print(f"Some files couldn't be loaded, for information see {missing_files}")
