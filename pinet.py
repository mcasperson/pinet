#!/usr/bin/env python

import dothat.lcd as lcd
import dothat.backlight as backlight
import json
import urllib2
import speedtest

backlight.rgb(255, 255, 255)
lcd.clear()

contents = urllib2.urlopen("http://192.168.1.215/admin/api.php?summaryRaw").read()
parsed_json = json.loads(contents)
lcd.write("PI-HOLE!")
lcd.set_cursor_position(0, 1)
lcd.write("Blocked " + str(parsed_json["ads_blocked_today"][:8]))
lcd.set_cursor_position(0, 2)
lcd.write("Ads %   " + str(parsed_json["ads_percentage_today"][:8]))

servers = []
s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()

results_dict = s.results.dict()
speedMbps = results_dict["download"] / 1000000

if speedMbps > 40:
    backlight.rgb(0, 255, 0)
elif speedMbps > 30:
    backlight.rgb(255, 255, 0)
else:
    backlight.rgb(255, 0, 0)