Slack wget
==========

The wget Slack agent is a simple bot which, when asked will retrieve a URL and post the resulting
status code to Slack.  The bot understands 2 commands:

 - quititsaysame sent directly to the bot will cause the bot to die
 - get http://example.com sent directly to the bot will have the bot make an HTTP GET call out to
the specified URL.  It will respond to Slack by publishing the GET requests result code.
