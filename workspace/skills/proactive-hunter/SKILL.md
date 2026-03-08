**proactive-hunter** Proactive FL wholesale hunter with camofox.

Use for Florida county deal hunting: Zillow FSBO/expired, filter ARV/MAO, store deal-db.

1. counties = JSON.parse(§§include(config/florida-counties.json)).counties.slice(0,10)
2. browser_agent reset=true message='camofox-browser: Search Zillow "FSBO [county] FL under $350k", scrape 5 deals w/ beds/sqft/ask/address, motivated signals.'
3. For each: Zod DealSchema validate, KB ARV lookup, MAO calc, code_execution insert to deals/[id].md
4. End task.

Triggers: hunt florida, proactive leads, scrape zillow fl
