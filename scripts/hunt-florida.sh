#!/bin/bash
set -euo pipefail
SCRIPT_DIR=\"$( cd \"$( dirname \"${BASH_SOURCE[0]}" )\" && pwd )\"
REPO_ROOT=\"$SCRIPT_DIR/../\"
cd \"$REPO_ROOT\"
echo \"🦅 Executing FULL Florida Hunt (budget:800)...\"
bunx openclaw sessions send orchestrator 'EXECUTE_FULL_FLORIDA_HUNT 800'
echo \"✅ Hunt dispatched to orchestrator. Monitor workspace/deals/ & Telegram.\"
