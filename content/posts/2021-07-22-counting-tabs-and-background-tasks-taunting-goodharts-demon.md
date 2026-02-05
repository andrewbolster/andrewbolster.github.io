---
aliases:
- /2021/07/counting-tabs-and-background-tasks-taunting-goodharts-demon/
- /2021/07/counting-tabs-and-background-tasks-taunting-goodharts-demon.html
cover:
  image: img/counting-tabs-and-background-tasks-taunting-goodharts-demon.generated.png
date: 2021-07-22 10:58:00+00:00
tags:
- API
- Firefox
- Python
- Windows
title: 'Counting Tabs and Background Tasks: Taunting Goodharts Demon'
---
This was going to be a really quick post yesterday, but I've spent the guts of a day (between actual work) just getting the _simplest_ bit of this working.

## The intent

I was silly enough to say this to someone recently in work:

> It's a good day when I end up with fewer firefox tabs open than when I started

And a plan was hatched;

1. Find API to query Firefox for current number of open Tabs across all window instances
2. Send that value to my internal MQTT node (that has telegraf, influx, home assistant and grafana integrations too)
3. Repeat

Spoiler alert, number 3 was the bastard

## Getting the Tabs

First step I thought was going to be more complicated. Fortunately [`brotab`](https://github.com/balta2ar/brotab) beat me to it (although I'm not a fan of the name...)

Once `brotab` is installed the first step of this is easy, if under-documented

``` python
from brotab.main import create_clients
from brotab.api import MultipleMediatorsAPI

n_tabs = len(
	MultipleMediatorsAPI(
		create_clients()
		).list_tabs([])
	)
print(f'You have {n_tabs} open, you shameless procrastinator')
```
> You have 135 open, you shameless procrastinator

## Sending the Message

Thankfully, I've done this a few times in a few projects, so this is simple enough.

``` python
import paho.mqtt.client as mqtt
import socket

hostname = socket.gethostname()

c = mqtt.Client(client_id=hostname)
c.connect('maguire', port=1883) # this is the internal hostname of my MQTT service. And No, not Harry

c.publish(f"{hostname}/open_tabs",
          n_tabs,
          retain=True		# this asks the MQTT service to persist the value, so clients _after_ publish can see the last value.
)
```

Then you can use something like [MQTT Explorer](http://mqtt-explorer.com/) to validate that it all works as expected.

At this point you can go and play with Grafana or Influx boards or however you want to think about using the value longer term, however, we've still got step three to get to....

## Task Scheduler? More like Task Mangler, amirite?

In 'nix land, this is easy.

`crontab -e`

```
*/15 * * * * * /home/bolster/anaconda3/bin/python /home/bolster/bin/count_tabs.py
```

Job done, go home, happy days.

Unfortuantely that's not the case with Windows "Task Scheduler" (Accessible via the start menu)

I won't go into the full rant, but here's select issues I came across.

* Regularly forgetting what user it was supposed to run under, reverting to 'Medium Execution' role or something similar, but it only notices that issue when the next cycle goes around and then fires a "Task Scheduler did not launch task "\TabPing" because user "(NONE)" was not logged on when the launching conditions were met. User Action: Ensure user is logged on or change the task definition to allow launching when user is logged off."
* Everyone and their dog has a different, contradictory, solution to 'my task doesn't start when scheduled' on [SuperUser](https://superuser.com/search?q=%22task+scheduler%22+not+executing)
* The Task Scheduler execution environment _isn't_ a shell, so commands like "START" will raise the helpful `Additional Data: Error Value: 2147942402.` error, which actually means 'File not Found' but everyone loves guru compemplations.
* Windows _really_ doesn't like running things in the background; if you just go the 'traditional route' of 'python.exe' '<path to script file>', it'll helpfully pop up and persist that command window during execution, which would be annoying as hell. Helpfully, `conda` ships with `pythonw.exe`, specifically designed to launch headless programs.... however....
* You can't call that directly without calling up the appropriate Conda environment :facepalm:, so we need to wrap the whole pointless thing in a `.bat` file to run it.
* Any time you change _anything_ about the task, it 'resets' the schedule, so if you have it triggered daily @ 9am, and you update the task definition after that, nothing with kickoff until tomorrow 9am (fix is to just reset the start time to T+5mins or something)

So, yeah, here goes.

count_tabs.py (lives in C:\Users\me, so YMMV)

``` python
from brotab.main import create_clients
from brotab.api import MultipleMediatorsAPI
import paho.mqtt.client as mqtt
import socket

hostname = socket.gethostname()
mqtt_host = 'maguire'
c = mqtt.Client(client_id=hostname)

c.connect(mqtt_host, port=1883)
print(f'Connected to {mqtt_host}')
n_tabs = len(MultipleMediatorsAPI(create_clients()).list_tabs([]))
print(f'Got {n_tabs} tabs')
c.publish(f"{hostname}/open_tabs",
          n_tabs,
          retain=True
)
print('Published')
```

count_tabs.bat (also C:\Users\me)

``` bat
SET logfile="C:\Users\me\batch.log"
@echo off
@echo Starting Script at %date% %time% >> %logfile%
call C:\Users\me\anaconda3\condabin\conda.bat activate
C:\Users\me\anaconda3\pythonw.exe "C:\Users\me\count_tabs.py" "1>C:\stdout.txt" "2>C:\stderr.txt"
@echo finished at %date% %time% >> %logfile%
```

And finally, the actual task as an XML that you _might_ be able to import, no idea, good luck.

```xml
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2021-07-21T14:11:30.6608587</Date>
    <Author>GRANGER\me</Author>
    <URI>\TabPing</URI>
  </RegistrationInfo>
  <Triggers>
    <CalendarTrigger>
      <Repetition>
        <Interval>PT5M</Interval>
        <StopAtDurationEnd>false</StopAtDurationEnd>
      </Repetition>
      <StartBoundary>2021-07-22T09:00:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>REDACTED EVEN THOUGH I HAVE NO IDEA IF IT MATTERS</UserId>
      <LogonType>S4U</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>StopExisting</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>"C:\Users\me\count_tabs.bat"</Command>
    </Exec>
  </Actions>
</Task>
```

# Task Gotchas

* To run a command properly in the background, 'Run whether user is logged on or not' needs to be selected, but also check "Do not store password", because this has the helpful effect that **if you get queried for a password on saving the task; the task has forgotten who you are**, so pop back into the 'Change User of Group', select your user, and then go ahead.
* The 'Conditions' Tab should not have _anything_ checked; I got trapped in there for a good while.
* You will really want to enable **'Enable All Tasks History'** in the 'Actions' sidebar of the Task Scheduler
