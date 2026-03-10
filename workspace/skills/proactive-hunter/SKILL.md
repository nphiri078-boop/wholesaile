**proactive-hunter** Proactive Florida wholesale lead hunter.

Trigger when: EXECUTE_FULL_FLORIDA_HUNT, florida hunt, find distressed FL properties.

Context: Wholesale real estate deals (cash/seller-finance). Target motivated sellers, high equity (>30k), price <300k, FL counties from config/florida-counties.json (top10 budget<1000, all67 budget high).

Procedure:
1. Parse budget from message (default 800 leads/max scrape $).
2. Load counties = jq config/florida-counties.json .top10[].name (or .all if budget>2000).
3. For each county (parallel if possible):
   - browser_agent reset=true 'New session, go to batchdata.com search FL $county distressed pre-foreclosure tax delinquent, scrape table addresses prices owners phones, end task'
   - browser_agent 'Continue, xleads.com $county FL motivated FSBO auction, scrape listings, end task'
   - Parse scraped text: address city zip price beds baths sqFt arv est equity= arv*0.7-price, owner phone notes='distressed $county $source'
4. Validate raw leads with @wholesaile/deal-db LeadSchema.parse({id:uuid, ..., source:'batchdata', status:'new', createdAt:new Date})
5. Save valid leads: code_execution_tool terminal 'cat > workspace/deals/${county}-${Date.now()}.md' with markdown table | equity | status
6. Telegram summary: code_execution_tool terminal 'curl telegram bot send table #leads total_equity top3 deals per county'

Use camofox-browser skill if detect blocks. Prioritize high equity. End with 'Hunt complete: X leads saved, Y equity total.'

## Level 3 Helper
Use scripts/county-loop.py for priority_zips looping.
