#!/usr/bin/env python

import dothat.lcd as lcd
import dothat.backlight as backlight
import json
import urllib2

backlight.rgb(255, 255, 255)
lcd.clear()
contents = urllib2.urlopen("http://192.168.1.215/admin/api.php?summaryRaw").read()
parsed_json = json.loads(contents)
lcd.write(parsed_json["ads_blocked_today"])