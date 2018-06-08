# Webhook listener for Gitlab

This is a simple Python webserver that can be used for handling Gitlab webhooks. Currently, upon merging a merge requst, it calls two external scripts for cleaning up Sonar projects en Bigboat containers. The goal is to make this more generic.

## TODO

- separate Gitlab logic from webserver code
- remove project specific code
- create a generic mechanism for calling external scripts (based on which webhook is being called)
- add tests
