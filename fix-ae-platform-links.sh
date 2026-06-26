#!/usr/bin/env bash
# Fix broken "AE Platform Index" links across crown app pages.
# page-09.html never existed on the AE platform repo — the platform's
# actual root file is index.html. Two additional stale deep-links in
# finrisk-sentinel.html (page-09-m03.html, page-09-m05.html) pointed at
# a nonexistent AE-platform module index; both targets are actually on
# the Quote-to-Cash pillar's own repo, so they're corrected to absolute
# cross-repo URLs pointing at QTC's existing page-05.html.
#
# In-place edits only. No new files created. Run this from the directory
# containing the crown app HTML files (or pass paths as arguments).
#
# Usage:
#   ./fix-ae-platform-links.sh
#   ./fix-ae-platform-links.sh /path/to/crown-apps/*.html

set -euo pipefail

FILES=(
  "compliance-command-centre.html"
  "data-governance.html"
  "finrisk-sentinel.html"
  "strategy-dashboard.html"
  "greenops.html"
)

# If arguments are passed, use those instead of the default file list.
if [ "$#" -gt 0 ]; then
  FILES=("$@")
fi

QTC_BASE="https://raosiddharthp.github.io/The-Autonomous-Quote-to-Cash"

for f in "${FILES[@]}"; do
  if [ ! -f "$f" ]; then
    echo "skip (not found): $f"
    continue
  fi

  # 1. page-09.html -> index.html (the AE platform's real root page)
  sed -i.bak 's|href="page-09\.html"|href="index.html"|g' "$f"

  # 2. finrisk-sentinel.html-specific stale deep links to a module
  #    index that never existed on the AE platform repo. Both targets
  #    are Quote-to-Cash's own modules, so point at QTC's existing page.
  sed -i.bak "s|href=\"page-09-m03\.html\"|href=\"${QTC_BASE}/page-05.html\"|g" "$f"
  sed -i.bak "s|href=\"page-09-m05\.html\"|href=\"${QTC_BASE}/page-05.html\"|g" "$f"

  rm -f "${f}.bak"
  echo "fixed: $f"
done

echo ""
echo "Done. Verifying no remaining page-09 references:"
grep -l "page-09" "${FILES[@]}" 2>/dev/null && echo "  ^ still found above — check manually" || echo "  none found — clean"
