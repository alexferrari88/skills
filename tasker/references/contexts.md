# Tasker Reference: Contexts

This file provides detailed documentation on Tasker Contexts concepts, options, and workflows.

## Table of Contents

- [Tasker: Application Context](#tasker-application-context)
- [Tasker: Time Context](#tasker-time-context)
- [Tasker: Day Context](#tasker-day-context)
- [Tasker: Location Context](#tasker-location-context)
- [Tasker: Location Edit](#tasker-location-edit)
- [Tasker: State Context](#tasker-state-context)
- [Tasker: Event Edit](#tasker-event-edit)
- [Tasker: Event Context](#tasker-event-context)
- [Tasker: Location Without Tears](#tasker-location-without-tears)

---

## Tasker: Application Context



##
Application Context

An Application Context is activated when selected parts of one or more application are
running.

Important: in Android versions after (and including) L, app detection is much less accurate.
For some apps it may not work at all, for others it may activate and never deactivate.

#### Controls

App button

When checked, indicates that the context will become active if any of the selected applications
is in the foreground, meaning it is currently being displayed to the user.

Services button

When checked, indicates that the context will also become active if a service
associated with any of the selected applications is running.

Note that services other than the obvious ones may be running. For example,
the default Play Music app may have a download service running even when not playing
music at a particular time.

Invert button

When the context is inverted, it will become active when any
application apart from the selected ones is matched

All button

Usually only applications are shown for selection which would usually be shown
in the launcher. The All button shows certain other launchable activities.

This button in no way affects how the context behaves.

#### Application Checking

When any profiles have application contexts specified, Tasker checks frequently
to see if one of those applications has been launched. The default is every
1.5 seconds.

If you would like quicker response, or you suspect this is severely increasing
your battery usage, you can change this value in preferences
(select Menu / Preferences / Monitor from the main screen).



---

## Tasker: Time Context



##
Time Context

A Time Context specifies a particular range, or one (or more) points in time.
There are three major components, at least one of which must be selected (by enabling
its checkbox on the left):

- From Time: the starting time of the range. If it's not specified,
00:00 is assumed.

- To Time: the end time of the range, inclusive. The context will deactivate
after the end of the specified minute.
If To Time is not specified then
23:59 is assumed i.e. the context deactivates at midnight.

- Repeat: if no repeat is selected, the context is assumed to be
a continuous range which starts at From Time and ends at To Time.
If a repeat is specified, the first occurrence is at From Time and then
every X hours or minutes until End Time.

When not in Beginner Mode [Beginner Mode](beginner.html) , it's possible to specify a global user variable [global user variable](variables.html)  as the source of the From Time or To Time by
clicking on one of the rotating-arrow icons.

The variable contents must specify the hours and minutes in 24-hour format and
separated by a period (dot) or colon e.g. 13.45. Leading 0s can be ommited
e.g. 9.7 for seven-minutes-past-nine-in-the-morning.

Alternatively, the time can be specified in seconds-since-the-epoch format, in which case
only the hour and minute part of the specification are used.

When the variable value changes, the time context is reevaluated which may result in
it activating or deactivating. If the variable value does not specify a valid time then the profile will
deactivate (if it's already activated).

Note: in some cases it may be wise to disable the profile (via the Profile Status action) before
changing the associated variable values. For example, if your time context is from 16.00 to 16.00 (i.e. acting
as an event) and it should be changed to 17.00,17.00, if you don't disable it first then as soon as
you change the first value the time context will become a 23 hour range (17.00-16.00) and probably
activate.

Notes:

- to specify a precise time, set From and To times the same. In that case, the context is treated as an instant event,
it it only active for a fraction of a second, so no setting restoration is done.

- each repeat (if Repeat is set) is also treated like an instant event.



---

## Tasker: Day Context



##
Day Context

A Day Context allows specification of one or more months and/or days of the
week/month.

#### Month Specification

The months are listed at the top, any of which can be selected. Selecting no
month has the same meaning as selecting every month i.e. has no restriction
on when the profile will become active.

#### Day of Week/Month Specification

Days of the week (Sunday, Monday etc) and/or month (1st, 9th etc) can be selected
independently with the pulldown centre-right. This will initially be for Week Days if
there are any defined, otherwise Month Days.

Selecting no day has the same meaning as selecting every day.

If you select both days of the week and days of the month, it requires both
conditions to be fulfilled for the profile to become active
e.g. selecting Mon,Tue and 11th means the profile will become active when the
day is a Mon or Tuesday and simultaneously the 11th day of the month.

If you are unsure if you have specified the day(s) you require, click the Done
button and you will see a verbal description at the top of the Profile Edit screen.
You can click on this to try again if it's not correct.



---

## Tasker: Location Context



##
Location Context

A location context specifies a circular geographical area in which
it is active. It is formed by a centre point (latitude, longitude) plus
a radius around that point.

#### Location Providers

A location provider is a method of supplying geographical coordinates. Tasker must
use one or more location providers to be able to decide when a location context
should become active or inactive.

GPS

The most accurate provider available (around +-10m), but its performance degrades quickly
indoors and it uses a relatively large amount of power.

To set the frequency of GPS fixes, see Menu / Preferences / Monitor.
GPS Check Time determines the check frequency in seconds while the device
is awake, Off Check Time while the device is asleep.

GPS will only be used for a particular context if it is specified in the location
edit screen.

Network

This provider uses a combination of cell-towers
and WiFi information (if wifi is enabled) to determine the device's geographical location. It is
less power-hungry than GPS, but also less accurate (sometimes +- several kilometres)
and requires data network availability.

Network will only be used for a particular context if it is specified in the location
edit screen.

Note: despite being network based, this still gives Tasker access to your location, so location on your device has to be enabled for this to work.

See also:

- Location Edit Screen [Location Edit Screen](activity_locselect.html)

- Location Without Tears [Location Without Tears](loctears.html)  (guidance for choosing a location method)



---

## Tasker: Location Edit



##
Location Edit

This screen allows configuration of a Location Context [Location Context](loccontext.html) .

#### Map Display

The map shows the location (base of the flag icon), radius and names of all defined location contexts

The location currently being defined has a yellow base, other location contexts have a blue base.

#### Map Controls

- long-click on the map to select a location for this context.

- long-click then drag on the flag for the current location to drag it

Use the pull-down selector under the map to specify the radius for this context.

Important: if your radius is too small compared to the accuracy of
the fixes you are receiving, your context may never go active. If you can't get
a fix, try increasing the radius. Typically, a good radius would be around twice the
accuracy of the fixes you are receiving.

If you have no internet available in order to retrieve the map tiles, you can still use
the Get Fix button (see below) to specify your current location.

#### Action Bar Options

Grab ('My Location') Button

Acquires a location fix using the enabled and available providers (make sure the GPS
Button is clicked first if you want to use GPS).

Once a fix is acquired, the latitude, longitude and radius of this location context
are set according to it. If you reduce the radius after a fix, Tasker may no longer
accurately detect whether you are in or out of the context.

When trying to determine current location, Tasker will keep going with fixes until they stop improving (e.g. as the
GPS locks on to more satellites). If you get impatient you can press the Get Fix button
again to stop the process (its label is changed to Stop while a fix is being
acquired).

Address Menu Item

Allows entry of an address for which this location context should be active.

#### Bottom Buttons

Net Button

The Net toggle button specifies whether to use the
Network [Network](loccontext.html#net)  location provider
to monitor for this location

GPS Button

The GPS toggle button specifies whether to use
GPS [GPS](loccontext.html#gps)
to monitor for this location
(assuming it is available on the device). If GPS is not used, the network will need
to be available in order to query for location fixes based on cell-towers or WiFi
data.



---

## Tasker: State Context



##
State Context

A State Context allows specification of the continuing state
of a software or hardware entity.

The State Edit screen allows configuration of the state and its
parameters.

#### State Name

The name of the state is given at the top of the screen.
Clicking on it allows changing to another state type.

Next to the name is a button to show help for the
displayed state type and its parameters. Be sure to check the
help text if you have trouble with a particular state.

#### State Parameters

General Parameters

All states have parameters to specify more details about the state.

Text parameters are treated as pattern matches [pattern matches](matching.html) .

Invert Parameter

All states have an invert parameter, which specifies that the context should
become active when it would usually be inactive, and vice-versa.



---

## Tasker: Event Edit



##
Event Edit

This screen allows configuration of an Event Context [Event Context](eventcontext.html) .

#### Event Name

The name of the event is given at the top of the screen.
Clicking on it allows changing to another event type.

In the top right is a button to show help for the
displayed event type.

#### Priority

Only present for relevant events.

Selects the priority at which this event will be detected.
An event can be processed by other Tasker Profiles, other
installed applications and system processes.

If priority is high, then this profile will be more likely
to detect the event before other processes, and vice versa.

#### Stop Event

Only present for relevant events.

If checked, then once this profile has dealt with the event,
other user or system applications will no longer be able to
see it.

You can achieve different effects by combining Priority
and Stop Event. For instance, if you want to show a Tasker menu
when the camera button is pressed, you would set Priority High
and check the Stop Flag, because you do not want the
camera application to appear afterwards.

#### Event Parameters

Some events have paramaters to specify more details about the event.
To get help on particular parameters, click the question-mark icon
at top right.

Text parameters are treated as pattern matches [pattern matches](matching.html) .

If you would like to make more complex comparions (e.g. mathematical expressions), leave the event parameter
blank and instead put a condition [condition](flowcontrol.html#condition)  on the first
action of the task you execute with the profile.



---

## Tasker: Event Context



##
Event Context

An Event Context allows specification of an event
which is needed to activate its profile e.g. SMS received,
screen has gone off.

Events are a little different to other contexts because they
are instantaneous whereas other contexts usually have
a duration.

This means that it is nonsensical to specify that e.g. the
screen brightness should be set to X for the duration of the
event, so Tasker assumes that all settings [settings](settings.html)
actions should persist beyond the event.

For more information about specifying events, see
the Event Edit screen [Event Edit screen](activity_eventedit.html) .

#### Event Parameters

When a task is triggered by an event, the parameters of the event that
ocurred are passed to the task so that it can make decisions based
on the event details.

The parameters are passed in the array [array](variables.html#arrays)
%evtprm.

The order of elements of the array have values which match the order
of the parameters of the event.

Example: if an event's second parameter is an Application, %evtprm2
in the launched task will be set to the label of the application
which triggered the event.



---

## Tasker: Location Without Tears



##
Location Without Tears

This is an overview guide to choosing a method for fixing your location with Tasker. At the end are
some advanced power-saving strategies [advanced power-saving strategies](#adv) .

## Power / Accuracy Comparison

Method			Power Usage Acc Network Wifi BT

State: Cell Near [State: Cell Near](#cell) 		* 		*

State: BT Near [State: BT Near](#btnear) 	** 		*****   Y

State: Wifi Near [State: Wifi Near](#near) 	** 		*****  Y

Location: Net [Location: Net](#net) 		** 		** Y

Location: Net & Wifi [Location: Net & Wifi](#netwifi) *** */***** Y Y

Location: GPS [Location: GPS](#gps) 		***** 		***** Y

More stars mean higher power usage or higher accuracy (Acc).

## Detail Comparison

### State: Cell Near

Setup

Create a state context, select Phone then Cell Near. Click Update and walk around a bit to scan for cell towers nearby.

About

Uses information about the cell towers the phone uses for telephony to record and match a location.

When the display is off, frequency of checks is controlled by Prefs / Monitor / Display Off All Checks.

If your profile keeps deactivating, go back to the Cell Near state and click the magnifying glass icon to check
for cells you may have missed in your scan.

Plus / Minus

- (+) virtually no extra power on top of power needed for normal phone service

- (+) when the display is on, context updates as soon as the tower is visible

- (+) when the display is off, only one check period is needed to determine context exit

- (-) highly inaccurate

- (-) must be physically at the location in order to record it

Other Settings

- Monitor / General Monitoring / Use New Cell API: if you're not seeing any cells at all when scanning on a modern device, try checking this

- Monitor / Display Off Monitoring / Cell Workaround: if things aren't working when the display is off

- Monitor / Display Off Monitoring / Cell Wake Screen: second possible workaround when the display is off

### State: BT Near

Setup

Create a State context, click BT Near (in the Net category), fill in the name or address of a bluetooth device near the location you want to identify.

About

BT Near does regular bluetooth Scans and will activate when it recognizes a device  you have configured
is nearby. Note: you don't have to connect to the device, so it doesn't have to be a device you own.

Frequency of checks is controlled by Prefs / Monitor / BT Scan Seconds (screen on) and Prefs / Monitor / Display Off All Checks (screen off).

Check the BT Toggle box if you don't want bluetooth enabled all the time. It will then be toggled when Tasker needs to do a scan.

If your target device is a low-energy device, deselect Standard Devices to reduce energy usage. If you can pair with the target device, you can have a major reduction in power usage and scan times by not selecting Non-Paired Devices.

Plus / Minus

- (+) very good accuracy, reliability

- (+) modest power usage, especially for paired devices

- (+) works indoors too

- (-) need a known device nearby

Other Settings

- Prefs / Monitor / Display Off Monitoring / Motion Detection: if available on your device, will need to be disabled if you wish to detect a nearby BT device that may move or turn off or on

### Location: Net

Setup

Create a location context, and deselect GPS.

About

Net location accuracy varies greatly. It's very important that you create a large radius around
the spot you wish to detect.

Frequency of checks is controlled by Prefs / Monitor / Network Location Check (screen on)
and Prefs / Monitor / Display Off All Checks.

Note: despite being network based, this still gives Tasker access to your location, so location on your device has to be enabled for this to work.

More Info [More Info](loccontext.html) .

Plus / Minus

- (+) extremely low (extra) power (IF network is available anyway)

- (-) requires network and phone service

- (-) highly inaccurate and variable fixes

### Location: Net & Wifi

Setup

Create a location context and deselect GPS. Make sure your device's Wifi is turned on
when you want a more accurate location fix.

About

Net location can be assisted by nearby access points when Wifi is turned on (Google has
a map of APs for many areas).

Turn Wifi off when not needed to conserve power e.g. use a Time context to turn wifi off at night.

Plus / Minus

- (+) very good accuracy in built-up areas for relatively low power usage

- (-) must be physically at the location in order to record it

### State: Wifi Near

Setup

Create a State context, click Wifi Near (in the Net category), fill in the SSID of an Access Point (AP)
with the best signal near where you want to identify.

About

Wifi Near does regular Wifi Scans and will activate when it recognizes an AP you have configured
is nearby. Note: you don't have to connect to the AP. You could configure e.g. the neighbours AP
if the signal is strong enough.

Frequency of checks is controlled by Prefs / Monitor / Wifi Scan Seconds (screen on) and Prefs / Monitor / Display Off All Checks (screen off).

Check the Wifi Toggle box if you don't want wifi on all the time. It will then be toggled when Tasker needs to do a scan. This isn't needed in
In Android 4.4+ if you select Scanning Always Available in Advanced Wifi Settings and will save power.

Plus / Minus

- (+) very good accuracy and reliability

- (+) less power than GPS

- (+) works indoors too

- (-) need an AP nearby

Other Settings

- Prefs / Monitor / Display Off Monitoring / Motion Detection: if available on your device, will need to be disabled if you wish to detect an AP
that may turn off and on.

- Android location settings: basic location needs to be enabled for Android 8.1+.

Location: GPS

Setup

Create a location context, and deselect Net.

About

Frequency of GPS checks is controlled by Prefs / Monitor / GPS Check (screen on)
and Prefs / Monitor / Display Off All Checks. Higher frequencies mean
more battery usage but that location changes will be noticed more quickly.

When indoors, GPS will try a long time to get a signal, using a lot of battery. Adjust
it at Prefs / Monitor / GPS Timeout. Make the
timeout as low as you can until you start losing effectiveness.

More Info [More Info](loccontext.html) .

Plus / Minus

- (+) highly accurate in the open air

- (-) functions very poorly or not at all indoors. A bad side effect is that if you enter a building e.g. office while between the check times, it may never detect
your new location until you leave.

- (-) extreme power usage

- (-) needs network to get a first fix

Other Settings

- Prefs / Monitor / Display Off Monitoring / Motion Detection: if available on your device, will need to be disabled if you wish to detect changes of location
on the order of a few meters.

### Advanced Strategies

Motion Detection

Some devices have a low-power accelerometer that can be active while the rest of
the device is sleeping.

For such devices, Tasker will not do location checks with the display off unless
it detects that significant movement has taken place since the last check, resulting
in lower power usage and faster response times when the device does eventually move.

Multiple Contexts

Tasker does not check high-power contexts until all lower-power contexts in the same profile are active.
You can use this to reduce power consumption. For instance, if you use the Wifi Near state to
detect coming home, you could add a Location: Net context to the same profile, so that wifi scanning
will only take place when you are in the right neighbourhood.

Location Control

Disable GPS/Net location when they're not needed by creating a separate profile with e.g. a Time context which disables GPS during the night.

This works because Location contexts assume you are in the same location until there is a fix which says otherwise.



---

