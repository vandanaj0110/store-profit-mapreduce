#!/usr/bin/env python3
import sys
import json

def main():
    cc = None
    pc = 0
    lc = 0
    for line in sys.stdin:
        city, s, c = line.strip().split("\t")
        c = int(c)
        
        if cc and cc != city:
            print(json.dumps({"city": cc, "profit_stores": pc, "loss_stores": lc}))
            pc = 0
            lc = 0
        cc = city
        if s == "profit":
            pc += c
        elif s == "loss":
            lc += c

    # Print result for the last city
    if cc:
        print(json.dumps({"city": cc, "profit_stores": pc, "loss_stores": lc}))

if __name__ == "__main__":
    main()

