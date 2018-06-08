#!/bin/sh

if [ $# -eq 0 ]; then
    echo "[ERROR] No branch name supplied"; exit 1;
fi

if [ -z "$1" ]; then
    echo "[ERROR] No branch name supplied"; exit 1;
fi

TOKEN="<insert sonar api token>"

remove_project () {
  echo "[INFO] Removing project $1"
  curl --silent --include -u ${TOKEN}: \
    -XPOST \
    http://www.sonarqube.bpbro.ictu:9000/api/projects/delete?project=$1
}

remove_project "bpbro-backend%3A${1}"
remove_project "bpbro-frontend%3A${1}"
