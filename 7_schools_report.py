"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
import json

infile = open("school_data.json",'r')

schools = json.load(infile)

print(type(schools))

conference_schools = [372,108,107,130]

for school in schools:
    school_name = school['instnm']
    ncaa = school['NCAA']["NAIA conference number football (IC2020)"]
    if ncaa in conference_schools:
        grad_w = school["Graduation rate  women (DRVGR2020)"]
        if grad_w > 50:
            print(grad_w)