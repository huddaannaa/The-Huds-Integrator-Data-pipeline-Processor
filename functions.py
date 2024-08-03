import pycountry
import json
import re

"""
To write and enrichment function use the format:
def name_of enrichment(params):
   
    NOTE: FUNCTION NAME SHOULD BE OF CONVENTIONS {ENRICHMENT_TYPE_NAME}_ENRICHMENT
    EXAMPLE:
        FOO_ENRICHMENT
        BAR_ENRICHMENT
 
    params = dict(params)
    json_data=params["json_data"]
    key_in_json_data_to_enrich=params["key_in_json_data_to_enrich"]

    text = json_data[key_in_json_data_to_enrich]    
    ## logic goes below    
    
    #enrichment results
    json_data['enrichment']={}
    json_data['enrichment'][#what to save enriched results as]=results
            
    return json_data  
"""





def country_enrichment(params):
    #https://datahub.io/core/geo-countries/datapackage.json
    """
    NOTE: FUNCTION NAME SHOULD BE OF CONVENTIONS {ENRICHMENT_TYPE_NAME}_ENRICHMENT
    EXAMPLE:
        FOO_ENRICHMENT
        BAR_ENRICHMENT
    """
    
    #variable must be of type dict
    #and must have a field json data
    #json_data=params["json_data"]
    #then any other custom fields will follow 
    #   (of type dict keys to index values in json_data)
    #    hence, what to search for
    
    #meta data
    params = dict(params)
    fxn_name = params['fxn_name'].replace("_enrichment","")
    
    json_data=params["json_data"]
    key_in_json_data_to_enrich=params["key_in_json_data_to_enrich"]
    
    #extra data
    #geo_country_data_file=r"db.json"
    #geo_country_data=open(geo_country_data_file)
    #geo_country_data_json=json.load(geo_country_data)
    
    results=[]
    try:
        text = json_data[key_in_json_data_to_enrich]   
        for country in pycountry.countries:
            if country.name in text:
                country_name_in_text =country.name
                results.append(country.name)
                
                """#adding geo data
                for country_data in geo_country_data_json:
                    country_name = list(country_data.values())[0]['country_name']
                    if country_name_in_text.lower() == country_name.lower():
                        geo_data = list(country_data.values())[0]
                        results.append(geo_data)"""
                
    except KeyError as er :
        print (f"""
[+] In the main enrichment function {key_in_json_data_to_enrich}
    appears to be null hence, Error: {er}
    but this is okay
    """)
        
    #enrichment results
    enrichment={}
    #enrichment[fxn_name]=list(set(results))
    enrichment[fxn_name]=results
    return enrichment
    

    
        
def tag_enrichment(params):
    """
    NOTE: FUNCTION NAME SHOULD BE OF CONVENTIONS {ENRICHMENT_TYPE_NAME}_ENRICHMENT
    EXAMPLE:
        FOO_ENRICHMENT
        BAR_ENRICHMENT
    """
    #variable must be of type dict
    #and must have a field json data
    #json_data=params["json_data"]
    #then any other custom fields will follow 
    #   (of type dict keys to index values in json_data)
    #    hence, what to search for
    
    #meta data
    params = dict(params)
    fxn_name = params['fxn_name'].replace("_enrichment","")
    
    json_data=""
    key_in_json_data_to_enrich="" 
    results=[]
    try:       
        tag="The Huds cyber Channel"
        results.append(tag)
    except KeyError as er :
        print (f"""
[+] In the main enrichment function {key_in_json_data_to_enrich}
    appears to be null hence, Error: {er}
    but this is okay
    """)
        
    #enrichment results
    enrichment={}
    enrichment[fxn_name]=results
    return enrichment
        
        
        
        
def cve_enrichment(params):
    """
    NOTE: FUNCTION NAME SHOULD BE OF CONVENTIONS {ENRICHMENT_TYPE_NAME}_ENRICHMENT
    EXAMPLE:
        FOO_ENRICHMENT
        BAR_ENRICHMENT
    """
    #variable must be of type dict
    #and must have a field json data
    #json_data=params["json_data"]
    #then any other custom fields will follow 
    #   (of type dict keys to index values in json_data)
    #    hence, what to search for
    
    #meta data
    params = dict(params)
    fxn_name = params['fxn_name'].replace("_enrichment","")
    
    json_data=params["json_data"]
    key_in_json_data_to_enrich=params["key_in_json_data_to_enrich"]
    results=[]
    try:
        text = json_data[key_in_json_data_to_enrich]          
        cve= re.findall(r"([cveCVE]{3}.\d{4}.\d{4,})", text, re.IGNORECASE)
        results=list(set(cve))   
    except KeyError as er :
        print (f"""
[+] In the main enrichment function {key_in_json_data_to_enrich}
    appears to be null hence, Error: {er}
    but this is okay
    """)
        
    #enrichment results
    enrichment={}
    enrichment[fxn_name]=results
    return enrichment
    
    
    

def threat_actor_enrichment(params):
    """
    NOTE: FUNCTION NAME SHOULD BE OF CONVENTIONS {ENRICHMENT_TYPE_NAME}_ENRICHMENT
    EXAMPLE:
        FOO_ENRICHMENT
        BAR_ENRICHMENT
    """
    #variable must be of type dict
    #and must have a field json data
    #json_data=params["json_data"]
    #then any other custom fields will follow 
    #   (of type dict keys to index values in json_data)
    #    hence, what to search for
    
    #meta data
    params = dict(params)
    fxn_name = params['fxn_name'].replace("_enrichment","")
    
    json_data=params["json_data"]
    key_in_json_data_to_enrich=params["key_in_json_data_to_enrich"]
    results=[]
    try:
        pattern=r"(TA[\s\d]{2,}|APT[\s\d]{2,}|TG[\s\d]{2,}|[\w]+\sdragon|[\w]+\sduke|[\w]+\sfalcon|[\w]+\scedar|[\w]+\sviper|[\w]+\slynx|[\w]+\spanda|[\w]+\sblossom|[\w]+\sbear|[\w]+\schollima)"
        text = json_data[key_in_json_data_to_enrich]          
        t_a= re.findall(pattern, text, re.IGNORECASE)
        results=list(set(t_a))  
    except KeyError as er :
        print (f"""
[+] In the main enrichment function {key_in_json_data_to_enrich}
    appears to be null hence, Error: {er}
    but this is okay
    """)
        
    #enrichment results
    enrichment={}
    enrichment[fxn_name]=results
    return enrichment
        