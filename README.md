# CiscoAMP-Sumo
Script to pull events from Cisco AMP and forward them to an HTTP sumo collector

First run the create_event_stream.py from the CiscoSecuritty Github account found here at time of writing:
https://github.com/Ciscosecurity/amp-04-event-stream-creator

This should provide you with the necessary details for configuring this script, similar to below:

```
AMQP Credentials:
User Name:..... [API_USER]
Password:...... [API_PASS]
Host:.......... export-streaming.amp.cisco.com
Port:.......... 443
Queue Name:.... [QUEUE_NAME]
```

Edit the configuration portion of the amp-sumo.py script with these values, then run
