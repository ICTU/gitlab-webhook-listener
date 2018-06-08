#!/bin/sh

if [ $# -eq 0 ]; then
    echo "No instance name supplied"; exit 1;
fi

if [ -z "$1" ]; then
    echo "No instance name supplied"; exit 1;
fi

DASHBOARD_API_KEY="<insert dashboard api key>"

echo "[INFO] Stopping application instance ${1}"

curl --silent --include -XDELETE -H 'Content-Type: application/json' -H "api-key: $DASHBOARD_API_KEY" \
    "http://www.test-dashboard.bpbro.ictu/api/v2/instances/${1}"
