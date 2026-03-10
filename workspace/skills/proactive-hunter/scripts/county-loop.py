#!/usr/bin/env python3
import json
zips = json.loads('''$PRIORITY_ZIPS''')
for zip in zips:
    print(f"Hunt ZIP: {zip}")
