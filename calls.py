from functions import *
import hashlib
from link import intergrates, config
import json
import os
from utils import writer, reader, writer_mem


def job(json_data_filepath, new_file_name, config):
    
    #this param was sneaked in from jobs.py
    since_db_file_name = config['since_db_file_name']
    signature_look_back = config['signature_look_back']
    since_db = f"{since_db_file_name}.db"
    #memory_db = f"{since_db_file_name}.mem"
    
    #if db file does not exits, create and put my name in it
    if os.path.exists(since_db):pass
    else:writer(since_db," ")
    
    
    
    
    #opening file to read
    #we open the file to start the enrichment process
    with open(json_data_filepath, "r") as read_file:
        file_to_read = read_file.readlines()

    #to compute the current state of file write
    len_of_signatures = 0
    len_of_signatures = len([sig for sig in reader(since_db) if sig != " " ])
    if len_of_signatures == 0:signature_look_back = 0
    else:signature_look_back = signature_look_back
    signature_file_pointer = len_of_signatures-signature_look_back
    
    #file reading loop
    line_counter=signature_file_pointer
    for row in file_to_read[signature_file_pointer:]:
        
        row=json.loads(row)
                
        #we check the state before moving on
        signature  = hashlib.md5(bytes(str(row), 'utf-8')).hexdigest()
        #loading the db of stored hashes
        stored_signatures = reader(since_db)
        if signature not in stored_signatures:             
            enrichment_output=[]
            #enrichment conf from configs
            print ("")
            print (f"[ Enrichment jobs >>>:")
            print (f"[ Data source: {json_data_filepath}")
            print (f"[ Progress counter: {line_counter}") 
            for enrich in config["enrichments"]:
                for enrichment_params in enrich:
                    enrichment_params_value = enrich[enrichment_params]
                    
                    try:
                        #enrichment settings/params
                        enrichment_type = enrichment_params_value['enrichment_type']
                        key_in_json_data_to_enrich = enrichment_params_value['key_in_json_data_to_enrich']
                        #print (f"[  ")                                                                     
                        print (f"[+] Calling<<< {enrichment_type} on {key_in_json_data_to_enrich}")
                    except:
                        print (f"""
[+] If the above fields are empty, 
    the enrichment action: {enrichment_type}, 
    might be adding a value to the event
""")
                    
                    #reading file rows loop
                    for fxn in intergrates:
                    
                        #here fxn is the enrichment function that appears as a string
                        #so we can check what to enrich
                        if enrichment_type in fxn:
                            print (f"[+] Applying<<< function: {fxn}")
                            
                            #params extracted from config, for function
                            params={}
                            params['json_data'] = row
                            params['key_in_json_data_to_enrich'] = key_in_json_data_to_enrich
                            params['fxn_name'] = fxn
                            
                            #function call
                            outp = eval(fxn)(params)
                            enrichment_output.append(outp)
                        else:
                            #print (f"[+] Trying to locate enrichment of type: {enrichment_type}")
                            pass
                            

            row['enrichment']=enrichment_output
            #print (row)
            writer(new_file_name, json.dumps(row))
            #line_counters
            line_counter=line_counter+1
            #write to since db
            writer(since_db, f"{signature}")        
        else:
            print (f"""[+] {signature} exists ..., 
    Hence:
[   Signature len   : {len_of_signatures}
[   Link pointer    : {line_counter}
[   Look back value : {signature_look_back}
[ ---------------------------------------------""")

