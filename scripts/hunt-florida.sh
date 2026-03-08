#!/bin/bash
set -euo pipefail
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT="$SCRIPT_DIR/../"
CONFIG="$REPO_ROOT/config/florida-counties.json"
counties=$(jq -r '.counties[]' "$CONFIG" | head -10)
for county in $counties; do
  echo "🦅 Hunting $county..."
  cd "$REPO_ROOT"
  # Invoke openclaw skill or docker exec
  docker exec -it openclaw openclaw skill proactive-hunter -- "county: $county, filters: distressed,fsbo,max_deals:10" || true
  sleep 30
done
echo "✅ Hunt complete"
