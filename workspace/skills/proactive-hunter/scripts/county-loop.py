#!/usr/bin/env python3
import json, sys
try:
    with open('../../config/florida-counties.json') as f:
        counties = json.load(f)['counties']
except:
    counties = ['Miami-Dade', 'Broward']  # fallback
for c in counties[:5]:
    print(f"Hunt {c}")
