from time import sleep
import re
import requests
from slackclient import SlackClient

VERSION='0.1.0'

direct_chan_id = 'D0R1MD5JR'
slack_token = 'your-slack-token'
run_flag = True

http_get_rqst_pattern = re.compile ('^get\s+<(https?://([-\w\.]+)+(:\d+)?(/([\w/_\.]*(\?\S+)?)?)?)>$')
stop_pattern = re.compile ('^quititsaysame$')

sc = SlackClient (slack_token)

if sc.rtm_connect ():
    while run_flag:
        msgs = sc.rtm_read ()
        if len(msgs) == 0:
            sleep (1)
        else:
            for msg in msgs:
                if 'channel' in msg and msg['channel'] == direct_chan_id:
                    if 'text' in msg:

                        stop_match = stop_pattern.match (msg['text'])
                        http_get_rqst_match = http_get_rqst_pattern.match (msg['text'])

                        if stop_match is not None:
                            run_flag = False
                        elif http_get_rqst_match is not None:
                            uri = http_get_rqst_match.group (1)
                            rqst = requests.get (uri)
                            sc.rtm_send_message (direct_chan_id, "{0} reported status code {1}".format (uri, rqst.status_code))
                        else:
                            sc.rtm_send_message (direct_chan_id, 'Unknown command: '+ repr(msg['text']))
        
else:
    raise Exception ("Unable to connect to slack.com")
