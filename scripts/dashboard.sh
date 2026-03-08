#!/bin/bash
set -euo pipefail
echo '=== Wholesale Pipeline Dashboard ==='
find workspace/deals -name '*.md' | wc -l | xargs printf 'Total deals: %s\n'
find workspace/deals -name '*Miami-Dade*' | wc -l | xargs printf 'Miami-Dade: %s\n'
# Add jq/grep for equity/status stats
echo 'Status breakdown:'
find workspace/deals -name '*.md' -exec grep -o 'status: [a-z]*' {} \; | sort | uniq -c | sort -nr
echo 'High equity (>50k):' $(find workspace/deals -name '*.md' -exec grep -l 'equity.*[5-9][0-9]k' {} \; | wc -l)
