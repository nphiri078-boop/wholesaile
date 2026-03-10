#!/usr/bin/env python3
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Pipeline Report"
ws.append(["Deal", "ARV", "MAO", "Status"])
ws.append(["123 Main", 300000, 150000, "Under Contract"])
wb.save("pipeline-report.xlsx")
print("Generated pipeline-report.xlsx")
