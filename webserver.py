#!/usr/bin/env python3

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from subprocess import run

hostName = ""
hostPort = 80
gitlab_token = "<insert token>"

class Webserver(BaseHTTPRequestHandler):
    def do_GET(self):
        if gitlab_token != self.headers["X-Gitlab-Token"]:
            self.send_error(401, "Invalid Gitlab token provided")
            return
            
        self.send_response(200)
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))

    def do_POST(self):
        if gitlab_token != self.headers["X-Gitlab-Token"]:
            self.send_error(401, "Invalid Gitlab token provided")
            return
        
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(time.asctime(), "[DEBUG] " + post_data.decode("utf-8"), flush=True)
        
        json_data = json.loads(post_data.decode("utf-8"))
        
        if "object_attributes" in json_data \
                and "state" in json_data["object_attributes"] \
                and "source_branch" in json_data["object_attributes"] \
                and "merged" == json_data["object_attributes"]["state"]:
            
            branch_name = json_data["object_attributes"]["source_branch"]
        
            instance_name = "bpbro-%s" % branch_name.split("_")[0]
            
            print(time.asctime(), "[INFO] Handling merge request event for branch: %s" % branch_name, flush=True)
            run(["sh", "./merge_request_hook/remove_sonar_project.sh", branch_name])
            run(["sh", "./merge_request_hook/remove_bigboat_containers.sh", instance_name])
        else:
            print(time.asctime(), "[INFO] Ignoring merge request event", flush=True)
        
        self.send_response(200)
        self.end_headers()

httpd = HTTPServer((hostName, hostPort), Webserver)
print(time.asctime(), "[INFO] Server Starts - %s:%s" % (hostName, hostPort), flush=True)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print(time.asctime(), "[INFO] Server Stops - %s:%s" % (hostName, hostPort), flush=True)
