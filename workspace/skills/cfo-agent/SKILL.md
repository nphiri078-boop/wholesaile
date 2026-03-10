**cfo-agent** Daily financial/CFO report for wholesale pipeline.

Trigger when: daily report, pipeline summary, cfo report.

Procedure:
1. Scan workspace/deals/*.md for leads/deals (parse tables with zod LeadSchema).
2. Compute metrics: total leads, by status, total equity sum, avg price/arv, stale (>3d contacted, >7d under-contract).
3. Terminal table: county | #new | #stale | total_equity | top_deal_price
4. Alerts: stale deals list with follow-up suggestions.
5. Telegram daily summary.
6. Save report to memory as REPORT-${date}.md

Use code_execution_tool terminal 'find workspace/deals -name *.md | xargs cat | jq stats' or parse.
End with dashboard table.

## Level 3 Helper
Use scripts/report-gen.py for XLSX deals reports.
