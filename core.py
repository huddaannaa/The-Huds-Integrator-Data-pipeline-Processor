from link import intergrates, config
from utils import writer
from calls import job
import os
import glob

#file_path from configs
json_data_filepaths = glob.glob(config["source_file_paths"])
destination_file_paths = config["destination_file_paths"]
since_db_directory = config['since_db_directory']

for file_path in json_data_filepaths:
    
    #hence, for every path globbed we need to create a new file name for the storage
    new_file_name = os.path.join(destination_file_paths, os.path.basename(file_path).replace(".","_"), os.path.basename(file_path))
    since_db_file_name = os.path.join(since_db_directory, os.path.basename(file_path).replace(".","_"), os.path.basename(file_path).replace(".","_"))
    config['since_db_file_name'] = since_db_file_name
    
    #create dst path if it does not exists
    try:os.makedirs(os.path.dirname(new_file_name))
    except:pass
    
    #create since path if it does not exists
    try:os.makedirs(os.path.dirname(since_db_file_name))
    except:pass
    
    print (f"[+] Operation on: {file_path}")
    print ("""   NOTE:  
                        if an operation exists past
                        it's signature look back time,
                        it simply means there are duplicates at the source.
                        the application uses the position of stored signatures 
                        to track events as pointers. These pointers are injected 
                        into the source file, to the the state of file 
                        read operations.                       
                        Hence, this enrichment tool will check for duplicates 
                        form the source and will not write them
                 IMPORTANT:
                        This means that the tool will only display, the stats of an
                        existing documents the signature looo back amount of time.
                        i.e, if loop back is 1, you will see only, 1 stat of an existing
                        document. Otherwise will mean duplicates exists
""")
    job(file_path, new_file_name, config)