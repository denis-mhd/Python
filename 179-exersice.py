import os 
import json 
import hcl 
import ast
from cognitive_complexity.api import get_cognitive_complexity
 

cfn = [".json", ".template", ".yaml", ".yml"] 
tf  = ["tf"] 
 
funcdef = ast.parse("""
def file_handler(dir): 
    for root, dirs, files in os.walk(dir):
        for file in files: 
            if file.endswith(tuple(cfn)):          
                with open(os.path.join(root, file), 'r') as fin: 
                    try: 
                        file = fin.read() 
                        if "AWSTemplateFormatVersion" in file: 
                            data = json.dumps(file) 
                            print(data) 
                    except ValueError as e: 
                        raise SystemExit(e)
            elif file.endswith(tuple(tf)): 
                with open(os.path.join(root, file), 'r') as file: 
                    try: 
                        obj  = hcl.load(file) 
                        data = json.dumps(obj) 
                        print(data) 
                    except ValueError as e: 
                        raise SystemExit(e) 
    return data
 """).body[0]   

print(f'Cognitive complexity equals to: {get_cognitive_complexity(funcdef)}')    


#Code refactoring

funcdef2 = ast.parse("""
def file_handler(dir): 
    for root, dirs, files in os.walk(dir):
        for file in files:
            action = check_file_extension(root, file)
            with open(os.path.join(root, file), 'r') as fin:    
                try:
                    if action == "reader":
                        file = fin.read() 
                        if "AWSTemplateFormatVersion" in file: 
                            obj = file
                            data = print_dumps_data(file) 
                    elif action == "loader":    
                        obj  = hcl.load(file) 
                        data = print_dumps_data(obj)
                except ValueError as e: 
                    raise SystemExit(e)                   
    return data


def check_file_extension(root,file):
    action = 0
    if file.endswith(tuple(cfn)):
        action = "reader"  
    elif file.endswith(tuple(tf)):
        action = "loader"
    return action   
    

def print_dumps_data(obj):
    data = json.dumps(obj) 
    print(data)
    return data             

""").body[0] 

directory = "C:/Users/denis.mehmed/OneDrive - Adastra, s.r.o/Desktop/Self-Training/Python/New folder"
print(f'Cognitive complexity on refactored code is equals to: {get_cognitive_complexity(funcdef2)}')    