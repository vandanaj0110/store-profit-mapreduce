#!/usr/bin/env python3
import sys
import json

def process_store(store):
    c = store["city"]
    sd = store["sales_data"]
    ctgr = store["categories"]
    nr = 0
    vd = False
    for i in ctgr:
        if i in sd:
            cd = sd[i]
            if "revenue" in cd and "cogs" in cd:
                r = cd["revenue"]
                cogs = cd["cogs"]
                nr += (r - cogs)
                vd = True
    if vd:
        if nr > 0:
            print(f"{c}\tprofit\t1")
        else:
            print(f"{c}\tloss\t1")

def main():
    for l in sys.stdin:
        l = l.strip() 
        l = l.strip(',') 
        if l=='[' or l==']':
        	continue
        if(not l):
        	continue
        try:
            s = json.loads(l)
            process_store(s)
        except json.JSONDecodeError as e:
            sys.stderr.write(f"Error decoding JSON: {e}\n")

if __name__ == "__main__":
    main()

