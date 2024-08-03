import re
import yaml

with open(r"functions.py", "r") as funcs:
    data_f =funcs.read()  
intergrates=re.findall(r'def\s(\w+)\(',data_f)


with open(r"enrichment.yaml", "r") as stream:
    try:config=yaml.safe_load(stream)
    except yaml.YAMLError as exc:print(exc)
        
