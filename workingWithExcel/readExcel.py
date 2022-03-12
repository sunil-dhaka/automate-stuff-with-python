import openpyxl,json
import numpy as np
from sympy import EX

workbook=openpyxl.load_workbook('censuspopdata.xlsx')

sheet=workbook[workbook.sheetnames[0]]

print(f'working on sheet ... {sheet.title}')

state_pop={}
for i,row in enumerate(sheet.rows):
    # to avoid first row as that is simply column names
    if i>0:
        keys=state_pop.keys()
        if row[1].value in keys:
            county_keys=state_pop[row[1].value].keys()
            if row[2].value in county_keys:
                state_pop[row[1].value][row[2].value]['tract']+=1
                state_pop[row[1].value][row[2].value]['pop']+=row[3].value
                # state_pop[row[1].value].update({
                #     row[2].value:{
                #         'pop':row[3].value+state_pop[row[1].value][row[2].value]['pop'],
                #         'tract':1+state_pop[row[1].value][row[2].value]['tract']
                #     }
                # })
            else:
                state_pop[row[1].value].update({
                    row[2].value:{
                        'pop':row[3].value,
                        'tract':1
                    }
                })
        else:
            state_pop[row[1].value]={
                row[2].value:{
                    'pop':row[3].value,
                    'tract':1
                }
            }

print(state_pop['AK']['Anchorage']['tract'])
print(state_pop['AK']['Anchorage']['pop'])

with open('state_pop.json','w') as f:
    json.dump(state_pop,f)
