#!/usr/bin/env python3
from openpyxl import Workbook
import os, glob, json
wb = Workbook()
ws = wb.active
ws.append(["Deal", "ARV", "MAO", "Status"])
deals_dir = "../../../deals"
for f in glob.glob(os.path.join(deals_dir, "*.json")):
    try:
        with open(f) as fd:
            deal = json.load(fd)
        ws.append([deal.get("address", ""), deal.get("arv", 0), deal.get("mao", 0), deal.get("status", "")])
    except:
        pass
wb.save("deals-report.xlsx")
print("Generated deals-report.xlsx")
