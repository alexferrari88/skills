# Tasker Reference: Advanced

This file provides detailed documentation on Tasker Advanced concepts, options, and workflows.

## Table of Contents

- [Tasker: Android System Power Management](#tasker-android-system-power-management)
- [Tasker: App Creation](#tasker-app-creation)
- [Tasker: Beginner Mode](#tasker-beginner-mode)
- [Tasker: CPU Control](#tasker-cpu-control)
- [Tasker: Encryption](#tasker-encryption)
- [Tasker: Gestures & Shaking](#tasker-gestures-&-shaking)
- [Tasker: Icons](#tasker-icons)
- [Tasker: Intents](#tasker-intents)
- [Tasker: Java Support](#tasker-java-support)
- [Tasker: JavaScript Support](#tasker-javascript-support)
- [Tasker: MIDI](#tasker-midi)
- [Tasker: Power Usage](#tasker-power-usage)
- [Tasker for Android](#tasker-for-android)
- [Tasker for Android](#tasker-for-android)
- [Tasker for Android](#tasker-for-android)
- [Tasker for Android](#tasker-for-android)
- [Tasker for Android](#tasker-for-android)

---

## Tasker: Android System Power Management



##
Android System Power Management

Starting with Android 5.0, many devices will act aggressively to try and
save system battery power. Unless certain steps are taken, Tasker may
not function as expected, either because Android is not sending it the
needed signals in order to save power or because Android is even killing
Tasker.

A commonly noticed symptom is that profiles with Time contexts don't activate
or deactivate at the expected time.

### Make Sure Tasker Is Not Killed By The OS

Making sure that Tasker is not killed by the system can be tricky because of all the restrictions Android applies to background apps, but in the majority of cases it's possible to do.

#### Please go through the list here [here](https://tasker.joaoapps.com/userguide/en/faqs/faq-problem.html#00)  for Tasker specific settings.

#### Also make sure to check out this page for vendor specific procedures: dontkillmyapp.com [dontkillmyapp.com](https://dontkillmyapp.com/?app=Tasker)



---

## Tasker: App Creation



##
App Creation

- Introduction [Introduction](#intro)

- Hello World Example [Hello World Example](#example)

- App Configuration [App Configuration](#config)

- Signing [Signing](#sign)

- Target Device Requirements [Target Device Requirements](#target)

- Miscellaneous [Miscellaneous](#misc)

- FAQ (External Link) [FAQ (External Link)](http://tasker.joaoapps.com/faq-appcreation.html)

### Introduction

Tasker allows creation of completely standalone apps (APK files) which have no
requirement for Tasker to be installed on the device they're used on.

The intention is to allow people to create their own apps for fun, for sale
or just to share with friends.  Or if you are concerned about all
the permissions Tasker needs you
can create an app that has only the permissions you require!

App creation is uncomplicated and takes only a few seconds once you're setup.

To create apps, you need the following on your device (not necessarily
on the device(s) the app will run on):

- Android 2.3+

- Tasker App Factory (free, see below)

- a device with an ARM or x86 processor (the vast majority of devices have one of those)

App creation is accessed by long-clicking on a project (not the base project) or task
and selecting Export then As App. Any
linked resources needed (e.g. other tasks, images) are included
as part of the new app.

To export anything except a single task, you need to create a project and put anything you
wish to export in the project.

### Hello World Example

Let's make a simple app that just pops up Hello World! when it's launched.

#### 1. Create A Task

- make a new task

click on the Tasks tab then click + to add a new task.
Give it a name Hello World.

- give the task an icon

click the grid icon at the bottom of the screen and pick any icon

- add the Popup action

click + in the bottom left to add an action, select category Alert and then action Popup. Fill in Hello World! in the Text parameter, then click the accept button bottom left to accept the action, then again to accept the task.

- ask Tasker to create an app

long-click on the task you just made, select Export then As App. A popup appears mentioning a Missing App.

#### 2. Install Tasker App Factory

To generate apps, Tasker needs a free helper app called Tasker App Factory.
It's available on Play Store and from the Tasker website.

Click the accept button on the popup to install the helper app.

#### 3. App Generation

Tasker should now start generating your app, which will take maybe 12 seconds
depending on your device.

If all goes well, the Cancel button will turn into an OK button meaning
your app is ready!

We can't run the app straight away though because it hasn't been installed.
Click on the rightmost bottom button with the Android icon to ask Android
to install your app.

Once Android is done installing, you can click it's Open button to
run the app, or you can simply go to the home screen and click on the app's
icon in the launcher.

You should see a Hello World popup!

### App Configuration

More usually, before an app is generated you will be presented
with a configuration screen which lets you specify various options
for the new app.

### App Signing

Android requires that all apps be signed i.e. that they certify who
created them. By default, Tasker uses an automatically-generated
insecure certificate to sign apps and doesn't bother mentioning it.

However, if you want to release an app via a public site
(Play Store for example), you will need to sign it with a
proper (secure) certificate.
That's done so the site knows that it's you that's giving
them the app each time you submit a new version.

Certificates are kept in a keystore which is protected
with a password. To generate a keystore with a secure certificate,
use Menu / More / Developer Options / Create Certificate.

Once you've generated the keystore, Tasker will often need to
ask you for the certificate password before app generation so that
it can be used to sign each new version of your app.

If Android's backup service is enabled in Android settings, Tasker
makes a backup of the keystore there.

Tasker also makes an automatic backup of the keystore to

/sdcard/Tasker/factory/keystore.user

when it is first created and when you backup your profile data
with Menu / Data / Backup. It's highly advisable
to make a copy of that file and keep it safe away from your device.

### Target Device Requirements

The device the child app is used on must meet the following requirements:

- the minimum SDK version specified in the Kid Config screen

- have hardware corresponding to features specified in the Kid Config screen

### Miscellaneous

#### Accessibility Service

Android accessibility support changed in Android 4.1 (JellyBean). If support is
needed for accessibility services in 4.1+, the Minimum Android Version in
the child Configuration screen must be set to 16 or higher. If support is required
pre-4.1, it must be set to less than 16.

In other words, to support both pre- and post-4.1 devices, two APKs must be
generated.

This applies to all features that rely on an Accessibility Service (events Notification, New Window, Button Widget Clicked, Notification Click, variables %NTITLE, %WIN, App Context from min version 20+)

Google Play Store allows publication of APKs targetting different Android versions
under the same package name, however this has not been tested by the developer
of Tasker.

#### Launch Task

When the specified launch task runs in the child app, the following local variables will be available
to it:

- %launch_data: the data (URI) in the intent that caused the child app to launch (often empty)

#### Monitor Service

Most child apps include a service which constantly monitors for events. If you know that you don't need
to monitor events anymore (in-between app launches) you can use the Disable action in the Tasker category to
stop it.

It will be automatically started again next time the app is launched.

#### Widgets / Shortcuts

- it's not possible in Android to auto-create widgets with any app

- it's not possible *currently* to offer the user child-app widgets,
that may be available in the future to some extent

#### Memory Problems

If you are having low memory problems during app generation, you can ask
the App Factory to use external storage for the generation process.
See Menu / Prefs / More / Factory.

#### Preferences

The new app does not take over any preferences from Tasker, all of the preferences in the child app are in their
default state, with a couples of exceptions.

Despite the misleading name, you can use the Set Tasker Pref action in the Tasker category
in the child app to change some of the child's preferences
when it is running.

#### Available Tasker Features

Obviously, the device the new app runs on may not have the same set of
available e.g. actions as the device the app is created on.

The Test action in the Misc category allows you to check
which Tasker features are available at run time (when the app
is being used).

#### Images

Referenced images (even scene doodles and photos from internal storage)
are bundled in with the app.

Tip: to include a dynamic image (e.g. which you download to a file path
via HTTP Get), put the image reference in a variable, and put the variable
in the relevant action.

#### Plugins

When the new app is launched, it checks that all referenced plugins
are installed on the device and prompts the user to install missing ones.

Some plugins may not work on other devices if they themselves store something about the
action to be performed, since that data will not be available on the
other device.

Plugin authors: see also here [here](http://tasker.joaoapps.com/plugins.html#gen) .

#### JavaScript actions

Scripts referenced by a JavaScript action are packaged with the new app
and run directly from there.

#### SL4A Scripts

Scripts referenced in a Run Script action are packaged with the new
app and unpacked to /sdcard/sl4a/scripts, prefixed with the
package name, on first run. Tasker automatically inserts the WRITE_EXTERNAL_STORAGE
permission for that purpose.

If SL4A is missing on the target device, the new app will prompt the user
to download when launched.

If a new version of the app is reinstalled on the target device, the new versions
of the scripts will be written if the length has changed.

#### Other External Components

The following external components are also checked for on launch of the new app where
necessary:

- Speech engines (Say, Say After)

- APNDroid (Mobile Data APN)

- Zoom (Zoom action category actions)

- apps for 3rd Party actions

- apps for 3rd Party events

#### Maps

The data for Maps is provided by Google and they require a maps key (v2) for
each developer that uses it. If you are using Map scene elements in your app, you need a key
from Google that can be included with your app.

Here are the steps to acquire a key:

- [if necessary] setup a Google Account [Google Account](http://www.google.com/accounts/)

- [if necessary] create a developer account [developer account](http://developer.android.com/distribute/index.html)

- [if necessary] create a signing keystore [signing keystore](#sign)

- get the SHA1 fingerprint of your certificate: Menu / More / Developer Options / Certificate Checksum

- Create an Google API Project [Google API Project](https://developers.google.com/maps/documentation/android/start#create_an_api_project_in_the_google_apis_console)

- Obtain the Maps key [Maps key](https://developers.google.com/maps/documentation/android/start#obtain_a_google_maps_api_key)

Enter the key in the App Configuration screen when generating your app. Note that the
box will only be presented if your app uses one or more Map scene elements.

Note that the device on which the created app is used needs Google's Play Services APK installed, otherwise
the map elements will not function.

#### Variables

The new app is completely independent of Tasker, so it also does
not share any variable values.

#### Permissions

Tasker attempts to reduce the set of permissions required by the new app to
the smallest set required for the functionality it contains. For example,
no Vibrate permission will be requested if there is no vibrate action
used.

The WAKE_LOCK permission is unfortunately always required for technical reasons.

#### App Size

Generated apps are minimally around 640K but are unlikely to be
significantly larger unless a lot of images are referenced.
It's possible that this minimum can be reduced in the future.

#### Encryption

Code for encryption is included in any app created by App Factory, however
if you don't use encryption features it's unlikely to be a problem
in terms of export restrictions. However, that is an opinion, it is not legal advice.

Note that code libraries for encryption are included with every Android device. Tasker
(and child apps) use these libraries to perform the encryption, they do not contain
encryption code themselves.

#### Licence

You are free to distribute and sell apps created by Tasker in any
way you wish. No licence fees to the developer of Tasker are necessary.
It would be courteous to reference Tasker and it's website
(http://tasker.joaoapps.com) somewhere in your new app if possible.

Please note that use of images from some Ipacks in commercial software
is prohibited by the licence terms of the image creators. You will need
to contact the image designer to request their assent in such cases.
(the origin of an Ipack's images is displayed in the Ipack image selection
screen).



---

## Tasker: Beginner Mode



##
Beginner Mode

When Tasker first starts, Beginner Mode is enabled.

In Beginner Mode, Tasker attempts to simplify things for inexperienced
users, mostly by UI elements which are unlikely to be needed by
inexperienced users.

Beginner Mode can be disabled by unchecking the option:

Menu / Prefs / UI / Beginner Mode

Some of the changes made in Beginner Mode are:

- main screen, Variables tab removed

- main screen, export options removed

- main screen, project tab not accessible

- task edit screen, task properties icon removed

- action edit screen, Label, Continue On Error parameters removed

- prefs screen, many options removed

- various places, variable selection not possible

In the userguide, when references are found to things which do not
appear on the screen. It's worth disabling Beginner Mode to see if that's
the problem.



---

## Tasker: CPU Control



##
CPU Control

Note: CPU control can damage your hardware e.g. by the CPU overheating. As for all Tasker
functions, you use it at your own risk!

### General

On a rooted device (only) Tasker is able to control the CPU frequency of an Android device to some extent. This
is usually done either to save battery or make the device more responsive depending on the circumstances.

The relevant control action is CPU in the Misc category.
You can monitor the current state with the variables %CPUFREQ and %CPUGOV.

There are two aspects which can be controlled, the Frequency Range and the
CPU Governor. You will need to experiment with combinations of these to achieve the best results.

### Frequency Range

You can set the minimum and maximum frequency which the CPU is allowed to run at. Only certain frequencies
are valid, depending on the CPU (click on the magnifying glass button to select a valid value).

The maximum frequency is probably initially set lower than the maximum frequency that the CPU can actually handle. If that is the case, you should be very cautious about setting it higher. Tasker will warn
you the first time you try to do configure an action to do that, assuming
you have not been using other apps to change the maximum frequency limit.

### CPU Governor

The active governor decides what the CPU frequency should be set to at a particular time, within the frequency
range you have set. Each has it's own unique strategy. Here are the most common governors:

- Performance
keeps the CPU frequency always at the maximum. Most power-hungry, most responsive.

- Powersave
keeps the CPU frequency always at the minimum. Least power-hungry, least responsive.

- Ondemand
when the CPU is needed, immediately sets it to maximum frequency. Slowly reduces the
frequency back down to the minimum as time passes. Responsive, reasonable power usage.

- Interactive
like Ondemand, but more responsive with slightly more battery usage.

- Conservative
when the CPU load is needed, slowly increases the frequency to maximum. When the CPU is
no longer needed, immediately drops back to the minimum. Less power-usage than Ondemand or Interactive, less responsive.

Not all governors are available on all ROM versions. Your device may also have a governor not described here. You can still set that governor with Tasker.

### CPU Action Not Available

Common problems are:

- root not recognized
Tasker decides that a device is rooted if /system/app/Superuser.apk is present and su is present in one of the directories of $PATH

- no available frequencies
Tasker needs to know what frequencies it can set the CPU to. It looks for the files /sys/devices/system/cpu/cpuX/cpufreq/scaling_available_frequencies, /sys/devices/system/cpu/cpuX/cpufreq/stats/time_in_state and /system/etc/scaling_available_frequencies (in that order). If you know what your CPU frequencies are, you could write them (space-separated, in numerical order) to the first (any number of CPUs) or last (1 CPU only) of those files.



---

## Tasker: Encryption



##
Encryption

Note: encryption functions are not available to new customers or
in Play Store versions of Tasker due to US export restrictions.

Tasker has the ability to encrypt and decrypt files. The relevant
actions are in the Encryption action category.

Since decryption can be automated, you have the possibility to
keep data files encrypted outside of certain times, locations,
applications etc.

Warning: make backups of your files while setting up encryption
until you understand how the system works and are sure the
encryption/decryption process does not cause any corruption.

Tip: Tasker does not give progress reports while it's doing
encryption, if you want to know when an long decryption operation
is finished, just put a Vibrate action or similar after the
Encrypt/Decrypt action.

#### Keys

Tasker uses a system of named keys. All of the encryption
actions can specify a key name so that you can use different keys
with different files (if desired).

If no key name is specified, default is used.

Once a passphrase for a key is entered, the ciphers it generated are stored in memory
until explicitly deleted. The deletion might be specified after an Encrypt/
Decrypt File action, or explicitly with the Clear Key action.

#### Setting Up Encryption

General Preferences

First thing to do is check whether the encryption preferences for
Encryption Iterations and Encryption Algorithm are
as you wish. Once you start encryping things, it's time consuming
to start again with new encryption preferences.

The preferences can be found at Menu / Prefs / Action.
Be sure to have a look at the help text for each item.

Initial Encryption

To start with, you probably want to encrypt some files which are in
a particular directory, which you can then decrypt as they are needed.

To do that, create a task called Encrypt or similar
and add one or more Encrypt File or Encrypt Dir actions to it.

By default, the
key is cleared once the file is encrypted, so click 'Leave Key'
for all but the last action, otherwise you'll have to enter your
passphrase for each file.

Next, create a Tasker shortcut [create a Tasker shortcut](app_widgets.html)  on the home screen, using the Encrypt
task. Tap the widget to encrypt your files. Notice how
you are only asked for the passphrase for the first one, because it
is stored until cleared.

The encrypted files will all receive an extension .tec
and the original files are deleted.

#### Decryption

Once you have a set of encrypted files, you need to setup the contexts
in which they will be decrypted.

Create another task called Decrypt or similar, and add Decrypt
actions to it to match the encrypt actions you setup previously.

Don't click Clear Key, otherwise you'll have to enter your
passphrase for every file (and at the start of encryption).

Now you can use your Encrypt and Decrypt tasks whenever you like. For instance,
you could create a profile with a Location Context and run your Decrypt task
when entering the location (assign Decrypt as the Enter task) and your Encrypt
task when leaving the location (assign Encrypt as the Exit task).

Important: when you use the Decrypt action, it recreates the original
file from the encrypted copy, but does not delete the encrypted version.

When you re-encrypt the file, if it has not changed it is simply deleted since we
already have an encrypted copy. If it has changed, it is re-encrypted.

The purpose of this method of operation is to:

- avoid the lengthy encryption process when unnecessary

- prevent accidental double-encryption (encrypting the same file twice)

#### Enter Key Action

It's not always convenient to enter the key at the point at which de- or encryption
takes place. This action allows you to specify the passphrase for a key
at a different point.

If you don't wish to double-enter a key when encrypting, you can also use this
action before an Encrypt action and not select Confirm.

#### Set Key Action

To allow full-automation of en/decryption, the passphrase for a key can also be set
without user interaction. However, this is much less secure tham Enter Key because:

- the passphrase (as part of the action) is stored in clear text in device memory and could be read by the root user if the device OS is compromised

- although the passphrase is itself encrypted when a backup is made to SD, the parameters for that encryption can be recovered from the java code in the Tasker apk file

#### Security

Algorithm

Tasker uses symmetric encryption, meaning the same passphrase is used both
to encrypt and decrypt the data.

The default algorithm is "PBEWithMD5And128BitAES-CBC-OpenSSL".
PBE stands for password-based encryption, see RFC 2898 [RFC 2898](http://www.ietf.org/rfc/rfc2898.txt) .

A salt is combined with the passphrase several hundreds of times using the MD5 algorithm
to produce a key which is used for the 128-bit (default setting) AES algorithm.

The number of iterations and algorithm can be set in Menu / Prefs / Action.

Pass Phrases

The longer the passphrase, the more secure the data. Minimally 8 characters of mixed
alphabetic, numeric and punctuation characters is recommended.

Clearing Keys

While a key's ciphers are in memory, anyone can use the key for
decryption or encryption if your device is lost or stolen, so it may be wise
to setup a Clear Key action e.g. when the device is turned off
(see Screen Off in the Event Context) or at a particular time (Time Context),
depending on what you are using the encryption for.

Manually Encrypting/Decrypting

You can use Tasker's file browser (action Browse Files) to encrypt/decrypt files
directly, via a long-click on the file.



---

## Tasker: Gestures & Shaking



##
Gestures & Shaking

#### General

Gestures are physical movements of the phone in space, which you first
record by creating a new Event of type Gesture (in the Misc category).

When you later redo the gesture while using your device, Tasker will carry out
the corresponding task(s) you have attached to its profile.

Like normal events, gestures are restricted by other contexts. For example,
if you define a profile with a Gesture (Event) and Application context, the
gesture will only be recognized while using that particular application.

Note: it might be a good idea to disable Tasker before setting up
new gestures, as otherwise you are likely to trigger previously defined ones.

#### Recording A Gesture

Gesture Points

First off, it's important to know that Tasker only records the particular points
(which we'll call inflection points) of a gesture that you tell it to.
For example, recording a gesture involving tilting the phone to the left and back
you would record three inflection points: the start, the tilted left position, and
the end (which is the same as the start in this case).

You can record as many points as you like, but in general it's best to record
only the points where the phone is not moving.

Recognized Movements

Tasker will only recognize changes in the angle of the phone i.e.
tilting to left or right, backwards or forwards, or rotating vertically.
Imagine three poles going through the device in the three dimensions.

Moving the phone backwards or forwards, up or down or side to side cannot
be recognized.

Procedure

- create a new Gesture Event and give it a name (so you can differentiate between
different gestures).

- put the phone in the position where you want the gesture to
start and press-and-hold the Call, Camera, Menu, Search or Volume hardware buttons
to record the point. The device will buzz.

- move to another (preferably not-moving) point on the path of your gesture, and
press the button again (not a long press). The device will buzz.

- on the final inflection point, press-and-hold the button
to mark the end of the gesture. The device will buzz again and the "Recorded."
message should now flash up.

- Press Done, and add a Vibrate action so you can hear when your
pattern matches when testing it.

#### Activation

Calibration

Before trying to match a pattern, you probably need to calibrate the hardware
in your device. Go to Menu / Prefs / Monitor / Gestures. Press
the Calibrate button and tilt your phone around in all directions.

Tasker now has some idea what kind of values the accelerometer in your
phone produces.

You only need to calibrate once.

#### Matching

Now exit Tasker and move your device through the points you previously defined
when recording. You should hear the device vibrate when it reaches the final
recorded point.

If not, try playing with the values in the Gesture Settings screen. For instance,
you could try raising the Match Radius (but be careful not to raise it too much
or you'll get a lot of matches by mistake).

#### Power Usage

Tasker does its best to limit power usage of gesture monitoring.

- monitoring for gestures only takes place when all the
other contexts in a profile are already active (and so the gesture might
have a chance of activating the profile). For example, if you combine an
Application and Gesture (Event) context, gesture monitoring will only
take place while using that particular application.

- Gesture monitoring is by default turned off when the display is off unless a power source is connected to the device,
unless specified otherwise in Menu / Prefs / Monitor / Display Off Monitoring

- updates from the accelerometer are at the minumum rate until the start of a gesture is detected.



---

## Tasker: Icons



##
Icons

Tasker can use four categories of icons:

Application [Application](#app) ,
Built-In [Built-In](#builtin) ,
Ipack [Ipack](#ipack) ,
User-Installed [User-Installed](#user) .

In some places it's also possible to use any image stored on local media as an icon.

#### Application Icons

These are taken from applications installed on the device.

Minor note: if the icon of the application changes, an update of previously created widgets/shortcuts can
be forced by creating a single widget with the new icon and then rebooting.

#### Built-In Icons

These come with Tasker and are kept in the device's memory.

#### Ipack Icon Sets

Ipack [Ipack](http://ipack.dinglisch.net)  is a free, open format for sharing of icon sets between Android applications.
Ipack icon sets can be either installed from Play Store [Play Store](http://market.android.com/search?q=ipack)  or from the Ipack website [Ipack website](http://ipack.dinglisch.net/download.html) .

When setting an icon, you will notice an item labelled Download More Icons. Clicking on it will use the appropriate source depending on which version of Tasker you have.

#### User-Installed Icons

You can also install your own icons directly into Tasker's icon directory
/sdcard/Tasker/.icn/. Make sure the icons are in a subdirectory.
The subdirectory should also only be one level deep (no subsubdirectories).

Icons must be in PNG format.

Example: a two-icon set called Christmas would have the two files
in these locations:

/sdcard/Tasker/.icn/Christmas/santa.png

/sdcard/Tasker/.icn/Christmas/snowman.png



---

## Tasker: Intents



##
Intents

Intents are Android's main method for allowing apps to communicate with each other and share data.
Intents are for advanced users. This document is not intended to explain how intents work, but
how to use Tasker's intent facilities.

### Sending Intents

You can find information about intents and details of several built-in Android intents on the Android SDK

Reference Site [Reference Site]( https://developer.android.com/reference/android/content/Intent.html) .

Tasker allows you to send arbitraty intents using the Send Intent action in the
Misc category. This allows
you to provoke behaviour in other apps, when you know the particular form of intent they
are designed to respond to.

#### Send Intent Parameters

Note that any parameter specified except Extras will reduce the set of possible receivers
of the intent.

Action

What the sender would like the receiver to do with the data.

Example: android.intent.action.VIEW

Cat

Gives additional information about the action.

Mime-Type

From the developer reference: "This is used to create intents that only specify a type and not data, for example to indicate the type of data to return."

Can't be used together with a Data specification.

Data

The main data specification in the form of a URI.

Can't be used together with a Mime-Type specification.

Extras

Any additional data to send with the intent.

The extras must be in the form of a single colon-separated key and value.

If the value can be parsed as an integer, long (integer ending in L), floating point number, double (float ending in D) or boolean (true/false) it will be treated as one.

The value can also be forced to a simple type (long etc) or Uri via casting.

The name of a Java object created via the Java Function action which is of type Parcelable can also be used (e.g. a Bundle)

If none of the above apply, the value will be treated as a String.

Examples:

- have_flowers:true
(boolean)

- this.is.an.integer.example:34
(int)

- this.is.a.double.example:34D
(int)

- address: (Uri) http://a.b
(Uri)

- bunchofvalues:mybundle (where mybundle is the name of a Java object of type Bundle)
(Parcelable)

- simple.string.example:hello there!
(String)

Package, Class

Allow specification of a particular package and/or class within the package to
restrict the broadcast to.

Target

The type of Android component which should receive the intent.

#### Finding App Intents

Many intents that an app listens for are declared in its package manifest
(called AndroidManifest.xml). You can view details of those intents
using the aapt tool that comes with the Android SDK like this:

aapt dump xmltree example.apk AndroidManifest.xml

Look for Intent Filter elements.

It's not (easily) possible to determine which intents an app listens
for dynamically (i.e. while the app is running).

### Receiving Intents

Tasker allows you to receive a large range of intents, sent by apps or the system, using the Intent Received event in the System category.

For each event you create, Tasker sets up a corresponding

Intent Filter [Intent Filter](https://developer.android.com/reference/android/content/IntentFilter.html)  object.

#### Limitations

- Tasker can only receive intents which
are sent to broadcast receiver components, not to activities
or services.

- some intent senders require that a corresponding intent filter is specified statically
(i.e. in an Android Manifest). Those intents cannot be received.

- intents which are broadcast with a specification of a particular
package component to receive it cannot be received.

#### Intent Received Parameters

Action

If specified, the received intent must have also that action specified.

Cat

Any categories specified in the received intent must also be specified
in the Tasker event. Note that this is logically different to the
situation for the Action parameter.

Scheme

If any schemes are included in the filter, then an Intent's data must be either one of these schemes or a matching data type. If no schemes are included, then an Intent will match only if it includes no data.

Mime Type

If a type is specified, then an Intent's data must be the same,
or match the Scheme parameter. If no Mime Type is specified,
then an Intent will only match if it specifies no Data.

Priority

If the intent is part of an ordered broadcast, then the priority
specified here will affect whether this event will receive the intent
before or after other listeners.

Stop Event

If the intent is part of an ordered broadcast, then specifying
Stop Event will prevent it being passed to other listeners after this one.

#### Accessing Intent Data

When an intent triggers an Intent Received event, the resulting
task(s) which are executed have access to many details of the
intent via local variables (where relevant and present):

- %intent_data: the data

- %evtprm1: the action

- %evtprm2: the first category

- %evtprm3: the second category

- %evtprm4: the URI scheme

- %evtprm5: the MIME type

In addition, any extras attached to the intent can be
accessed under their name, with the following modifications to
make them valid variable names:

- all letters will be converted to lower-case, then

- names of length less than 3 will have var_ prefixed

- non-letter-or-digit characters will be converted to _, then

- names not starting with a letter will have a prefixed, then

- names not ending with a letter or digit will have a affixed

- if the result is the name of another extra, _dup will be affixed until that is no longer the case

For example, an extra with key %SOUND_ON will be available as %sound_on, and an
extra with key package.SOUND_ON!, will be available via the local variable %package_sound_on_a

The following extra types are presented in Tasker as local arrays:
String [], Integer [], ArrayList, ArrayList.

Example:  a string array extra `named 'fruits' with values 'pear' and
'apple' will result in the local variables %fruits1 (=pear) and %fruits2 (=apple).



---

## Tasker: Java Support



##
Java Support

- Introduction [Introduction](#intro)

- The Java Function Action [The Java Function Action](#javafunction)

- Using The Action

- Parameters

- Return Values

- Objects [Objects](#objects)

- Creating An Object

- Object Naming, Local And Global

- Built-in Objects

- Assigning Values

- Other Actions Supporting Objects

- Other Topics [Other Topics](#other)

- Casting

- Constants

- Generic Classes

- Permissions

- Service Thread

- Static Fields

### Introduction

Android has hundreds of thousands of functions which apps can use. It's not possible
for Tasker to present all of those to the user, so Tasker allows the
advanced user to directly call those Java functions and work with Java objects themselves.

It does not allow you to 'write Java code'... but the combination of
Tasker's logic and flow control with direct access to the Android API is
sufficient for most automation purposes.

This page assumes you have a basic familiarity with the Java concepts
of objects and classes.

Developer information on the Android API is available from Google [Google](http://developer.google.com/develop) .

#### Example

- Variable Set, %service, wifi

- Java Function, wiman = CONTEXT.getSystemService( %service )

- Java Function, %enabled = wiman.isWifiEnabled()

- Java Function, wiman.setEnabled( true ), If %enabled eq false

This example task turns wifi on if it is not already enabled.

Action 2 demonstrates that Tasker variables can be used in Java function calls.
wiman is a Java object resulting from the function call which is stored
by Tasker for use in subsequent actions. CONTEXT is also such a variable
but is built-in and always accessible to Java Function.

Action 3 demonstrates that results of Java Function can also
be assigned to Tasker variables. Since all Tasker variables are strings,
some conversion needs to take place depending on what type of object the
Java function returns. In this case it's a boolean, and so %enabled will be
true or false.

Action 4 demonstrates taking a decision based on the result of previous
Java function call.

### The Java Function Action

#### Using The Action

- enter an object or class (to access static functions)
into the first parameter.

The magnifying glass icon will show a
class selector for classes known in the latest Android API. Some may
be coloured red, as not all classes are available on all devices.

The coffee-cup icon allows quick selection of known Java objects

The question mark icon will attempt to link to the relevant Android
reference page for the object or class.

- click the magnifying class next to the Function
parameter to select a function to execute appropriate to the object
or class from step 1.

In most cases, Tasker will be able to guess which class an object
is, and hence which functions are available, if not, see casting
[casting](#casting)  below.

Functions listed in red are private, meaning they can be used, but the
author didn't intend them to be.

- if the function returns a value, you can enter a Java object
name [object
name](names)  to assign it to, or a Tasker variable, see below [below](#return) .

- enter any parameters required for the function, see below [below](#params) .
The type of object the function expects for the parameter is displayed above the text entry
field. The magnifying glass will list any fields associated with the current
entry in the text box, where possible.

#### Parameters

If you don't enter a value for a parameter, null will be used for
that parameter when the function is called.

If you enter the name of a variable array, Tasker will attempt to convert
the array values into the type of object (an array or collection) which
the function expects.

Other Tasker variables will be replaced in the usual way.

Here can also be entered Java objects, or their fields, either built-in or created by
previous calls to Java Function (e.g. wiman or arr[0].length)

Note: To use a string as a parameter you need to enclose it in double quotes or else Tasker assumes that the value you're using is a new or existing Java object.

#### Return Values

When a Java function returns a value, it can be placed in either a Tasker variable or a Java object (or ignored).

If it's placed into a Tasker variable, it's converted to a piece of text and the object itself is lost
and can no longer be accessed. Note that if the Java object is an array or list, it will be assigned
to multiple Tasker variables in the usual way e.g. %val1, %val2...

When the returned value is placed into a Java object, you can access the object at a later time in another Java Function and some other (see later) actions.

Note that return value classes are inferred from the function, so
object names can refer to different classes at different times.
It's not recommended to reuse names in this way however!

### Objects

#### Creating An Object

New objects of most types can be created by filling in the class name,
hitting the function selector and selecting a function called new.

It's worth noting that many classes in the Android API have special static
functions for getting a new object of that class called e.g. getInstance
or similar.

Arrays (also multidimensional) can be created by adding [] to the
class name (or e.g. [][]).

Here's an example of creating a 3x5 string array:

- Java Function, arr = new String[][]( 3 )

- For, %rowno, 0:2

-    Java Function, arr[%rowno] = new String[]( 5 )

Creating an array is also possible natively via the newInstance function in the the class Array.

Array components can be accessed as in normal Java (arr[0][1])
wherever Java objects are supported [supported](#support) .

#### Object Naming, Local and Global

Object names can consist of any any combination of upper or lower case letters and underscore and, unlike Tasker
variable names, may start with underscore. The first letter
may not be upper-case, as this is a convention used to distinguish objects from classes.

Analogous to Tasker variables, Java objects are either local to the current task if their name is all
lower case, or global (available to any other task) if there are any upper-case characters in the name.
All-upper-case names represent final (fixed) global objects which cannot be modified.

There are three important things to remember about global Java objects:

- it's important to delete them  once they are no longer needed, because they can take up
a lot of memory.

- unlike global Tasker variables, they are lost when Tasker is killed e.g. because the device was restarted

- their names can only contain upper- or lower-case letters or underscore.

#### Built-in Objects

- Android Context (class Context)

CONTEXT

Many funtions in Android require a context object. In tasks running directly as a result of a scene element event,
this is the Activity object which is displaying the scene, otherwise it's Tasker's Application context.

- Image Buffer (class Bitmap)

IBUFFER
The object manipulated by functions in Tasker's Image action category.

#### Assigning Values

When writing Java code, to make a name refer to the same object as another
name, you would use something like:

String a = "hello";
String b = a;

Now both a and b refer to the same object.

To achieve that in Tasker, you use the special assignTo
function after selecting the object to assign.

Java Function, a, "hello", assign (or a = "hello".assign())
Java Function, b, a, assign (or b = a.assign())

#### Other Actions Supporting Objects

If

A Java object can be directly referenced in a condition. Null-value
objects are replaced with text representation null.

Examples:

If, arr[0][0] eq 45
If, arr[0].length > 3
If, lightlevel Equals null

You cannot make function calls e.g. str.charAt( 5 )

For

The Value parameter in the For action can include Java object
references as for If.

For, %value, arr

Will repeat once for each value in the array arr. This will
also work for string lists and simple objects (boolean etc)

### Other Topics

#### Casting

Casting in Tasker is used only to tell Tasker the type of
a particular object. That can be useful so that e.g. Tasker can
show functions which are appropriate to it.

In the example at the top of the page, the getSystemService
function returns an Object:

Java Function, wiman = CONTEXT.getSystemService( %service )

Since the object could be one of many kinds of managers, Tasker is
not able to list the WifiManager functions for easy selection
when creating the next Java Function action in the task.

You can tell Tasker the actual type by adding a cast in brackets
before the name:

Java Function, (WifiManager) wiman = CONTEXT.getSystemService( %service )

#### Constants

Tasker support the usual naming conventions for Java constants.

- L a long integer e.g. 300L

- F a floating-point number e.g. 45.6D

- D a double-length float e.g. 45.6D

- double quotes indicate a string e.g. "hello", though
in many cases Tasker will infer that a string was intended
anyway

- single quotes indicate a character e.g. 'x'

Tasker will attempt to convert numbers without affixes to a Java type in
the following order: int, long, float, double.

#### Generic Classes

Tasker only supports fully the following generic classes:

- ArrayList<String>

- ArrayList<View>

- ArrayList<Bundle>

- ArrayList<Integer>

- ArrayList<Long>

- ArrayList<Double>

- ArrayList<Float>

Create them by selecting their class in the class selector, clicking the
function selector and clicking new.

Generic classes mixed with arrays cannot be handled by Tasker, though
you can pass such objects around from function to function.

#### Permissions

For some function calls, Android requires that the calling app have declared
a permission otherwise the call will fail. This means that a
Java Function call will fail if the permission is not one of the
ones pre-declared by Tasker.

Unfortunately, Android does not allow permissions to be added dynamically, so
if you wish to use a function requiring a permission that Tasker
does not already have, the only option is to generate a child
app to run the function (see App Creation [App Creation](appcreation.html) ).
In the child configuration screen
you can add any permissions which your Java Function call
needs to the child app.

#### Service Thread

Java code is executed with a non-UI thread by a service.

Some implications are:

- things which require an activity will not work e.g. showing a dialog

- sending intents will in some cases require the flag Intent.FLAG_FROM_BACKGROUND
and possibly also Intent.FLAG_ACTIVITY_NEW_TASK

#### Static Fields

Static fields (e.g. ContentResolver.EXTRA_SIZE) are not currently supported
by Tasker.

A workaround is to use reflection to get (or set) the value:

res = CONTEXT.getContentResolver();
cls = res.getClass();
fld = cls.getField( EXTRA_SIZE );
%val = fld.get( null );



---

## Tasker: JavaScript Support



##
JavaScript Support

- Introduction [Introduction](#intro)

- Local Variables [Local Variables](#localvars)

- Global Variables [Global Variables](#globalvars)

- Arrays [Arrays](#array)

- Settings [Settings](#settings)

- Execution [Execution](#exe)

- Working Off-Device [Working Off-Device](#offdevice)

- Builtin Functions [Builtin Functions](#builtin)

alarmVol [alarmVol](#alarmVol)
audioRecord [audioRecord](#audioRecord)
audioRecordStop [audioRecordStop](#audioRecordStop)

btVoiceVol [btVoiceVol](#btVoiceVol)
browseURL [browseURL](#browseURL)
button [button](#button)

call [call](#call)
callBlock [callBlock](#callBlock)
callDivert [callDivert](#callDivert)
callRevert [callRevert](#callRevert)
callVol [callVol](#callVol)
carMode [carMode](#carMode)
clearKey [clearKey](#clearKey)
composeEmail [composeEmail](#composeEmail)
composeMMS [composeMMS](#composeMMS)
composeSMS [composeSMS](#composeSMS)
convert [convert](#convert)
createDir [createDir](#createDir)
createScene [createScene](#createScene)
cropImage [cropImage](#cropImage)

decryptDir [decryptDir](#decryptDir)
decryptFile [decryptFile](#decryptFile)
deleteDir [deleteDir](#deleteDir)
deleteFile [deleteFile](#deleteFile)
destroyScene [destroyScene](#destroyScene)
displayAutoBright [displayAutoBright](#displayAutoBright)
displayAutoRotate [displayAutoRotate](#displayAutoRotate)
displayTimeout [displayTimeout](#displayTimeout)
dpad [dpad](#dpad)
dtmfVol [dtmfVol](#dtmfVol)

elemBackColour [elemBackColour](#elemBackColour)
elemBorder [elemBorder](#elemBorder)
elemPosition [elemPosition](#elemPosition)
elemText [elemText](#elemText)
elemTextColour [elemTextColour](#elemTextColour)
elemTextSize [elemTextSize](#elemTextSize)
elemVisibility [elemVisibility](#elemVisibility)
enableProfile [enableProfile](#enableProfile)
encryptDir [encryptDir](#encryptDir)
encryptFile [encryptFile](#encryptFile)
endCall [endCall](#endCall)
enterKey [enterKey](#enterKey)
exit [exit](#exit)

filterImage [filterImage](#filterImage)
flash [flash](#flash)
flashLong [flashLong](#flashLong)
flipImage [flipImage](#flipImage)

getLocation [getLocation](#getLocation)
getVoice [getVoice](#getVoice)
global [global](#global)
goHome [goHome](#goHome)

haptics [haptics](#haptics)
hideScene [hideScene](#hideScene)

listFiles [listFiles](#listFiles)
loadApp [loadApp](#loadApp)
loadImage [loadImage](#loadImage)
local [local](#local)
lock [lock](#lock)

mediaControl [mediaControl](#mediaControl)
mediaVol [mediaVol](#mediaVol)
micMute [micMute](#micMute)
mobileData [mobileData](#mobileData)
musicBack [musicBack](#musicBack)
musicPlay [musicPlay](#musicPlay)
musicSkip [musicSkip](#musicSkip)
musicStop [musicStop](#musicStop)

nightMode [nightMode](#nightMode)
notificationVol [notificationVol](#notificationVol)

performTask [performTask](#performTask)
popup [popup](#popup)
profileActive [profileActive](#profileActive)
pulse [pulse](#pulse)

readFile [readFile](#readFile)
reboot [reboot](#reboot)
resizeImage [resizeImage](#resizeImage)
ringerVol [ringerVol](#ringerVol)
rotateImage [rotateImage](#rotateImage)

saveImage [saveImage](#saveImage)
say [say](#say)
scanCard [scanCard](#scanCard)
sendIntent [sendIntent](#sendIntent)
sendSMS [sendSMS](#sendSMS)
setAirplaneMode [setAirplaneMode](#setAirplaneMode)
setAirplaneRadios [setAirplaneRadios](#setAirplaneRadios)
setAlarm [setAlarm](#setAlarm)
setAutoSync [setAutoSync](#setAutoSync)
setBT [setBT](#setBT)
setBTID [setBTID](#setBTID)
setClip [setClip](#setClip)
setGlobal [setGlobal](#setGlobal)
setKey [setKey](#setKey)
setLocal [setLocal](#setLocal)
settings [settings](#settings)
setWallpaper [setWallpaper](#setWallpaper)
setWifi [setWifi](#setWifi)
shell [shell](#shell)
showScene [showScene](#showScene)
shutdown [shutdown](#shutdown)
silentMode [silentMode](#silentMode)
sl4a [sl4a](#sl4a)
soundEffects [soundEffects](#soundEffects)
speakerphone [speakerphone](#speakerphone)
statusBar [statusBar](#statusBar)
stayOn [stayOn](#stayOn)
stopLocation [stopLocation](#stopLocation)

systemLock [systemLock](#systemLock)
systemVol [systemVol](#systemVol)

takeCall [takeCall](#takeCall)
takePhoto [takePhoto](#takePhoto)
taskRunning [taskRunning](#taskRunning)
type [type](#type)

usbTether [usbTether](#usbTether)
unzip [unzip](#unzip)

vibrate [vibrate](#vibrate)
vibratePattern [vibratePattern](#vibratePattern)

wait [wait](#wait)
wifiTether [wifiTether](#wifiTether)
writeFile [writeFile](#writeFile)

zip [zip](#zip)

- Function Notes [Function Notes](#notes)

### Introduction

Tasker supports running JavaScript code in tasks or WebView [WebView](element_web.html)  scene elements.
Most Tasker actions can be accessed direct from the JavaScript.
JSON and XMLHTTPRequest are also directly available from the JavaScript code.

#### JavaScript in Tasks

JavaScript can be embedded inline in tasks via the JavaScriptlet (direct
specification of JavaScript to run) or JavaScript (load script from file)
actions.

In both cases, the JavaScript executes in sequence with the other actions in the task
and variables are transparently converted so pieces of JavaScript can be
interwoven throughout the task.

#### Embedded in HTML

WebView elements allow specification of mixed HTML and JS for the element
content.

<H1 onClick="setWifi( false )">ClickMeToTurnOffWifi</H1>

This allows a single WebView to present a complete user-interface.

### Local Variables

In JavaScript(let) actions, local variables (all lower case, e.g. %myvar) are directly accessible in the JavaScript without
the % sign (e.g. myvar). If the script changes the value, the new value is transparently
used by subsequent actions in the task.

The values of new (all lower case) variables declared in JavaScript (with the var keyword) are also available to subsequent actions,
with the exception of those which are chain-declared e.g. var one = 'aval', two = 'bval';

In JavaScript embedded in HTML, the functions local [local](#local)  and
setLocal [setLocal](#setLocal)  must be used to access variables local to the scene hosting the WebView.

If you're using a JavaScript or JavaScriptlet action and you disable Auto Exit, you have to set local variables with setLocal [setLocal](#setLocal) .

### Global Variables

Tasker global variables need to be accessed via global() [global()](#global)  and set via setGlobal() [setGlobal()](#setGlobal) .
Global arrays are not supported due to an Android limitation.

### Arrays

Local Tasker arrays are transparently available in Javascript(let)s and vice-versa.
They are not available in WebViews.

Arrays which are not existing Tasker arrays must be declared in the JS as such i.e. in
this case arr will not be visible to the remainder of the task:

var arr = getSomeArray();

Whereas in this case it will:

var arr = [];
arr = getSomeArray();

Note that:

- JavaScript array indices start at 0, whereas Tasker array indices start at 1

- JavaScript uses [] while Tasker uses ()

So, for example, %arr(1) (Tasker) is equivalent to arr[0] (JavaScript).

### Settings

Unlike normal Tasker actions, settings which are changed in JavaScript as part of a profile's
enter task are not restored when the profile exits.

### Execution

#### Execution Instances

Only one script can execute at one time. Once a piece of
JavaScript is executing, it cannot be interrupted by another
piece.

#### Working Off-Device

You might wish to develop long and/or complicated tasks off-device e.g. on a PC.

There are two strategies for that:

#### 1. JavaScript action

For off-device testing, use Menu / More / Developer / Save JS Library Template to get dummy
definitions for the built in functions. Include that file when developing on your PC.

To test in your JavaScript code whether you're on-device or not, use

var onAndroid = ( global( 'sdk' ) > 0 );

By using the JavaScript action rather than JavaScriptlet you can easily
access a file synced from PC to a file on the Android device.

#### 2. Using WebView

If you specify a website URL as the content for your WebView, then testing the
code on the target device is a simple matter of pushing the new version to your webserver and
reloading the WebView on the device (see action Element Web Control [Element Web Control](help/ah_scene_element_web_control.html) )

#### Builtin Function Execution

Calls to most Tasker builtin functions (see below) are
executed as normal single-action tasks and thus may be blocked
by other executing tasks.

They execute at the priority of the task that executed the JavaScript
plus two.

#### JavaScript(let): Alert,Confirm,Prompt

Scripts using these functions require a 'user-interface' and may cause
interference with the currently running app (though in most cases they
will not).

#### JavaScript(let): Auto Exit

By default, the JavaScript(let) action will end when the main execution
sequence is finished.

If you are using asynchronous code e.g. via setTimeout() or other callbacks,
you should deselect Auto Exit. You are then responsible yourself for telling
Tasker to continue the task by calling exit().

In any case, execution will stop when the timeout configured for the action is reached.

#### JavaScript(let): Libraries

You can specify as many libraries as you want in the Libraries parameter,
separated by newlines.

Several popular libraries are pre-selectable.

You may wish to download them manually to your local storage and change the http URL
to a file URL so that Internet is not required to run your script.

Warning: library code will have access to local files, data providers etc. on the device

Important: if you are using your own libraries developed on Windows, you may need to convert
CRLF style line endings to Unix style LF.

### Builtin Functions

Tasker makes most of it's actions available via functions which can be called directly via name
in JavaScript(let) actions and WebView elements.

Exceptions:

- in WebView content where mode is set to URL, the functions must be prefixed by tk e.g. tk.flash('Woo!')

- when executing code via eval the functions must be prefixed by tk.

alarmVol / btVoiceVol / callVol / dtmfVol / mediaVol / notificationVol / systemVol / ringerVol

var ok = alarmVol( int level, bool display, bool sound )

Set the relevant system volume to level.

If display is true, the new level will be flashed up on-screen.

If sound is true, a tone will sound at the new level.

audioRecord

var ok = audioRecord( str destPath, str source, str codec, str format )

- destPath: where to put the recording. Note that a file extension is not
necessary, it will correspond to the selected format.

- source: def, mic, call, callout or callin

- codec: amrn, amrw or aac

- format: mp4, 3gpp, amrn or amrw

The JavaScript does not wait for the audio recording to complete.

See also: audioRecordStop() [audioRecordStop()](#audioRecordStop) .

audioRecordStop

var ok = audioRecordStop()

Stop recording previously initiated by audioRecord() [audioRecord()](#audioRecord) .

browseURL

var ok = browseURL( str URL )

Open the default browser at the specifed URL.

button

var ok = button( str name )

Simulate a press of the named button.

name must be one of back, call, camera, endcall, menu, volup, voldown or search.

This function requires a rooted device.

call

var ok = call( str num, bool autoDial )

Make a phone call.

If autoDial is false, the phone app will be brought up with
the number pre-inserted, if true the number will also be dialed.

callBlock

var ok = callBlock( str numMatch, bool showInfo )

Block outgoing calls matching [matching](matching.html)  numMatch.

If showInfo is set, Tasker will flash a message when
a call is blocked.

callDivert

var ok = callDivert( str fromMatch, str to, bool showInfo )

Divert outgoing calls matching [matching](matching.html)  fromMatch
to the number to.

If showInfo is set, Tasker will flash a message when
a call is diverted.

callRevert

var ok = callRevert( str numMatch )

Stop blocking or diverting outgoing calls previously specified with
callBlock [callBlock](#callBlock)  or callDivert [callDivert](#callDivert) .

carMode

var ok = carMode( bool onFlag )

Turn on or off Android Car Mode.

clearKey

var ok = clearKey( str keyName  )

Clear the passphrase for the specified keyName.

See Also: Encryption [Encryption](encryption.html)  in the Userguide.

composeEmail

var ok = composeEmail( str to, str subject, str message  )

Show an email composition dialog with any specified fields pre-filled.

The JavaScript does not wait for the email to be sent before continuing.

composeMMS

var ok = composeMMS( str to, str subject, str message, str attachmentPath )

Show an MMS composition dialog with any specified fields pre-filled.

The JavaScript does not wait for the MMS to be sent before continuing.

composeSMS

var ok = composeSMS( str to, str message )

Show an SMS composition dialog with any specified fields pre-filled.

The JavaScript does not wait for the SMS to be sent before continuing.

convert

var result = convert( str val, str conversionType )

Convert from one type of value to another.

conversionType must be one of the string constants: byteToKbyte,
byteToMbyte, byteToGbyte, datetimeToSec, secToDatetime, secToDatetimeM, secToDatetimeL, htmlToText,
celsToFahr, fahrToCels, inchToCent, metreToFeet, feetToMetre, kgToPound, poundToKg, kmToMile,
mileToKm, urlDecode, urlEncode, binToDec, decToBin, hexToDec, decToHex, base64encode base64decode,
toMd5, toSha1, toLowerCase, toUpperCase, toUpperCaseFirst.

See also: action Variable Convert [Variable Convert](help/ah_convert_variable.html) .

createDir

var ok = createDir( str dirPath, bool createParent, bool useRoot )

Create the named dirPath. If createParent is specified and any
parent directory does not exist, it will also be created.

If useRoot is specified, the operation will be performed as the root user
(where available).

createScene

var ok = createScene( str sceneName )

Create the named scene [scene](scenes.html)  without displaying it.

cropImage

var ok = cropImage( int fromLeftPercent, int fromRightPercent, int fromTopPercent, int fromBottomPercent )

Crop an image in Tasker's image buffer previously loaded via loadImage [loadImage](#loadImage) .

decryptDir

var ok = decryptDir( str path, str key, bool removeKey )

As decryptFile() [decryptFile()](#decryptFile) , but decrypts each file in the specified directory
in turn.

decryptFile

var ok = decryptFile( str path, str key, bool removeKey )

Decrypt the specified file using the encryption parameters specified in Menu / Prefs / Action.

If removeKey is not set, the entered passphrase will be reapplied automatically to the
next encryption/decryption operation with the specified keyName.

See Also: Encryption [Encryption](encryption.html)  in the Userguide,
Decrypt File [Decrypt File](help/ah_decrypt_file.html)  action.

deleteDir

var ok = deleteDir( str dirPath, bool recurse, bool useRoot )

Delete the named dirPath.  recurse  must be specified if
the directory is not empty.

If useRoot is specified, the operation will be performed as the root user
(where available).

deleteFile

var ok = deleteFile( str filePath, int shredTimes, bool useRoot )

Delete the named filePath.

shredTimes has range 0-10.

If useRoot is specified, the operation will be performed as the root user
(where available).

See also: action Delete File [Delete File](help/ah_delete_file.html)

destroyScene

var ok = destroyScene( str sceneName )

Hide the named scene [scene](scenes.html)  if it's visible, then destroy it.

displayAutoBright

var ok = displayAutoBright( bool onFlag )

Whether the display brightness should automatically adjust to the ambient light or not.

displayAutoRotate

var ok = displayRotate( bool onFlag )

Whether the display orientation should change based on the physical orientation of the device.

displayTimeout

var ok = displayTimeout( int hours, int minutes, int seconds )

How long the period of no-activity should be before the display is turned off.

dpad

var ok = dpad( str direction, int noRepeats )

Simulate a movement or press of the hardware dpad (or trackball).

direction must be one of up, down, left, right or press.

This function requires a rooted device.

enableProfile

var ok = enableProfile( str name, boolean enable )

Enable or disable the named Tasker profile.

encryptDir

var ok = encryptDir( str path, str keyName, bool rememberKey, bool shredOriginal )

As encryptFile() [encryptFile()](#encryptFile) , but encrypts each file in the specified directory
in turn.

elemBackColour

var ok = elemBackColour( str scene, str element, str startColour, str endColour )

Set the background colour [colour](#colour)  of the specified scene [scene](scenes.html)  element.

See also: action Element Back Colour [Element Back Colour](help/ah_scene_element_background_colour.html) .

elemBorder

var ok = elemBorder( str scene, str element, int width, str colour )

Set the border colour [colour](#colour)  and width of the specified scene [scene](scenes.html)  element.

elemPosition

var ok = elemPosition( str scene, str element, str orientation, int x, int y, int animMS )

Move an element within it's scene.

orientation must be one of port or land. animMS indicates the duration of the corresponding animation in MS. A zero-value indicates no animation.

See also: action Element Position [Element Position](help/ah_scene_element_position.html) .

elemText

var ok = elemText( str scene, str element, str position, str text )

Set the text of the specified scene [scene](scenes.html)  element.

pos must be one of repl (replace existing text completely), start
(insert before existing text) or end (append after existing text).

See also: action Element Text [Element Text](help/ah_scene_element_text.html) .

elemTextColour

var ok = elemTextColour( str scene, str element, str colour )

Set the text  colour [colour](#colour)  of the specified scene [scene](scenes.html)  element.

See also: action Element Text Colour [Element Text Colour](help/ah_scene_element_text_colour.html) .

elemTextSize

var ok = elemTextSize( str scene, str element, int size )

Set the text size of the specified scene [scene](scenes.html)  element.

See also: action Element Text Size [Element Text Size](help/scene_element_text_size.html) .

elemVisibility

var ok = elemVisibility( str scene, str element, boolean visible, int animationTimeMS )

Make the specified scene [scene](scenes.html)  element visible or invisible.

See also: action Element Visibility [Element Visibility](help/ah_scene_element_visibility.html) .

endCall

var ok = endCall()

Terminate the current call (if there is one).

encryptFile

var ok = encryptFile( str path, str keyName, bool rememberKey, bool shredOriginal )

Encrypt the specified file using the encryption parameters specified in Menu / Prefs / Action.

If rememberKey is set, the entered passphrase will be reapplied automatically to the
next encryption/decryption operation with the specified keyName.

If shredOriginal is specified, the original file will be overwritten several
times with random bits if encryption is successful.

See Also: Encryption [Encryption](encryption.html)  in the Userguide,
Encrypt File [Encrypt File](help/ah_encrypt_file.html)  action.

enterKey

var ok = enterKey( str title, str keyName, bool showOverKeyguard, bool confirm, str background, str layout, int timeoutSecs )

Show a dialog to enter the passphrase for the specified keyName. The JavaScript waits
until the dialog has been dismissed or the timeout reached.

- confirm: if set, the passphrase must be entered twice to ensure it is correct.

- background: [optional] a file path or file URI to a background image.

- layout: the name of a user-created scene [scene](scenes.html)  to use in place of the built-in scene.

See Also: Encryption [Encryption](encryption.html)  in the Userguide

filterImage

bool ok = filterImage( str mode, int value )

Filter an image previously loaded into Tasker's image buffer via
loadImage() [loadImage()](#loadImage)

Possible values of mode are:

- bw: convert to black & white, using value as a threshold

- eblue: enhance blue values by value

- egreen: enhance green values by value

- ered: enhance red values by value

- grey: convert to greyscale, value is unused

- alpha: set pixel alpha (opposite of transparency) to value

value should be 1-254.

flipImage

bool ok = flipImage( bool horizontal )

Flip an image previously loaded into Tasker's image buffer via
loadImage() [loadImage()](#loadImage)

If horizontal is false, the image is flipped vertically.

exit

exit()

Stop execution of the JavaScript.

flash

flash( str message )

Flash a short-duration Android 'Toast' message.

flashLong

flashLong( str message )

Flash a long-duration Android 'Toast' message.

getLocation

var ok = getLocation( str source, bool keepTracking, int timeoutSecs )

Try to get a fix of the current device location.

source must be one of gps, net or any.

If keepTracking is set, the specified source(s) will be left tracking
with the purpose of providing a much quicker fix next time the function is
called.

Fix coordinates are stored in the global Tasker variables %LOC (GPS) and/or %LOCN (Net).
The value can be retrieved with the global [global](#global)  function. Several other
parameters of the fix are also available, see Variables [Variables](variables.html) .

Example

var lastFix = global( 'LOC' );
if (
getLocation( 'gps' ) &&
( global( 'LOC' ) != lastFix )
) {
flash( "New fix: " + global( 'LOC' ) );
}

See also: action Get Location [Get Location](help/ah_get_fix.html) , function stopLocation [stopLocation](#stopLocation) .

getVoice

str result = getVoice( str prompt, str languageModel, int timeout )

Get voice input and convert to text.

result is 'undefined' if the voice acquisition failed, otherwise
it's an array of possible matching texts.

prompt is a label for the dialog that is shown during voice acquisition.

languageMode gives the speech recognition engine a clue as to the
context of the speech. It must be one of web for 'web search' or
free for 'free-form'.

goHome

goHome( int screenNum )

Go to the Android home screen. screenNum is not supported by all
home screens.

haptics

var ok = haptics( bool onFlag )

Enable/disable system setting Haptic Feedback.

hideScene

var ok = hideScene( str sceneName )

Hide the named scene [scene](scenes.html)  if it's visible.

global

var value = global( str varName )

Retrieve the value of a Tasker global variable. Prefixing the name with % is optional.

Example:

flash( global( '%DogName' ) );

listFiles

str files = listFiles( str dirPath, bool hiddenToo )

List all files in the specified dirPath.

files is a newline-separated list of subfiles.

If no files or found or an error occurs, the returned value will be undef.

If hiddenToo is specified, files starting with period are
included, otherwise they are not.

Example:

var files = listFiles( '/sdcard' );
var arr = files.split( '\n' );
flash( 'Found ' + arr.length + ' files' );

loadApp

var ok = loadApp( str name, str data, bool excludeFromRecents )

Start up the named app.

Name can be a package name or app label, it's tested first against
known package names. Note: app label could be localized to another
language if the script is used in an exported app.

Data is in URI format and app-specific.

When excludeFromRecents is true, the app will not appear in the home screen
'recent applications' list.

loadImage

var ok = loadImage( str uri )

Load an image into Tasker's internal image buffer.

The following uri formats are currently supported:

- file:// followed by a local file path

See also Load Image [Load Image](help/ah_load_image.html)  action.

lock

var ok = lock( str title, str code, bool allowCancel, bool rememberCode, bool fullScreen, str background, str layout )

Show a lock screen, preventing user interaction with the covered part of the screen. The JavaScript waits until the
code has been entered or the lock cancelled (see below).

- code: the numeric code which must be entered for unlock

- allowCancel: show a button to remove the lockscreen, which causes a return to the Android home screen

- rememberCode: the code will be remembered and automatically entered when the lock screen is show in future,
until the display next turns off

- background: [optional] a file path or file URI to a background image.

- layout: the name of a user-created scene [scene](scenes.html)  to use in place of the built-in lock scene

local

var value = local( str varName )

Retrieve the value of a Tasker scene-local variable. The name should not be
prefixed with %.

This function is only for use by JavaScript embedded in HTML and accessed via
a WebView scene element.

mediaControl

var ok = mediaControl( str action )

Control media via simulation of hardware buttons.

Possible actions are next, pause, prev, toggle, stop or play.

micMute

var ok = micMute( bool shouldMute )

Mute or unmute the device's microphone (if present),

mobileData

var ok = mobileData( bool set )

Enable or disable the system Mobile Data setting.

See also: action Mobile Data [Mobile Data](help/ah_mobile_data_direct.html)

musicBack

var ok = musicBack( int seconds )

Skip back by seconds during playback of a music file previously started by musicPlay [musicPlay](#musicPlay) .

See also: musicSkip [musicSkip](#musicSkip) , musicStop [musicStop](#musicStop)

musicPlay

var ok = musicPlay( str path, int offsetSecs, bool loop, str stream )

Play a music file via Tasker's internal music player.

stream to which audio stream [audio stream](#streams)  the music should be played

This function does not not wait for completion.

The last 3 arguments may be ommitted, in which case they default to 0,
false and media respectively.

See also: musicStop [musicStop](#musicStop) , musicBack [musicBack](#musicBack) ,
musicSkip [musicSkip](#musicSkip)

musicSkip

var ok = musicSkip( int seconds )

Skip forwards by seconds during playback of a music file previously started by musicPlay [musicPlay](#musicPlay) .

See also: musicBack [musicBack](#musicBack) , musicStop [musicStop](#musicStop)

musicStop

var ok = musicStop()

Stop playback of a music file previously started by musicPlay [musicPlay](#musicPlay) .

See also: musicBack [musicBack](#musicBack) , musicSkip [musicSkip](#musicSkip)

nightMode

var ok = nightMode( bool onFlag )

Turn on or off Android Night Mode.

popup

var ok = popup( str title, str text, bool showOverKeyguard, str background, str layout, int timeoutSecs )

Show a popup dialog. The JavaScript waits until the popup has been dismissed or the timeout reached.

- background: [optional] a file path or file URI to a background image.

- layout: the name of a user-created scene [scene](scenes.html)  to use in place of the built-in popup scene.

performTask

var ok = performTask( str taskName, int priority, str parameterOne, str parameterTwo, str returnVariable, bool stop, bool variablePassthrough, str variablePassthroughList, bool resetReturnVariable )

Run the Tasker task taskName.

Note that the JavaScript does not wait for the task to complete.

profileActive

bool active = profileActive( str profileName )

Whether the named Tasker profile is currently active. Returns false if
the profile name is unknown.

pulse

bool ok = pulse( bool onFlag )

Enable or disable the Android Notification Pulse system setting.

readFile

var contents = readFile( str path )

Read the contents of a text file.

reboot

var ok = reboot( str type )

Reboot the device.

type is one of normal, recovery or bootloader.
It can be ommitted and defaults to normal.

Requires a rooted device.

See also: function shutdown [shutdown](#shutdown)

resizeImage

var ok = resizeImage( int width, int height )

Scale the current image in Tasker's image buffer to the specified dimensions.

rotateImage

var ok = rotateImage( str dir, int degrees )

Rotate the current image in Tasker's image buffer.

dir must be one of left or right.
degrees must be one of 45, 90, 135 or 180.

saveImage

var ok = saveImage( str path, int qualityPercent, bool deleteFromMemoryAfter  )

Save the current image in Tasker's image buffer to the specified file path.

Save Image [Save Image](help/ah_save_image.html)  action.

say

var ok = say( str text, str engine, str voice, str stream, int pitch, int speed )

Cause the device to say text out loud.

- engine: the speech engine e.g. com.svox.classic  Defaults to the system default (specify undefined for that)

- voice: the voice to use (must be supported by engine). Defaults to the current system language (specify undefined for that)

- stream: to which audio stream [audio stream](#streams)  the speech should be made

- pitch: 1-10

- speed: 1-10

The script waits for the speech to be finished.

sendIntent

var ok = sendIntent( str action, str targetComp, str package, str class, str category, str data, str mimeType, str[] extras );

Send an intent. Intents are Android's high-level application interaction system.

Any parameter may be specified as undefined.

- targetComp: the type of application component to target, one of receiver, activity or service.
Defaults to receiver.

- package: the application package to limt the intent to

- class: the application class to limit the intent to

- category: one of none, alt, browsable, cardock, deskdock, home, info, launcher, preference, selectedalt, tab or test,
defaults to none

- extras: extra data to pass, in the format key:value. May be undefined. Maximum length 2.

See also: action Send Intent [Send Intent](help/ah_send_intent.html) .

sendSMS

var ok = sendSMS( str number, str text, boolean storeInMessagingApp );

Send an SMS.

See also: action Send SMS [Send SMS](help/ah_send_sms.html)

setAirplaneMode

var ok = setAirplaneMode( bool setOn )

Enable or disable Airplane Mode.

Get the current value with:

var enabled = global( 'AIR' );

See also: function setAirplaneRadios [setAirplaneRadios](#setAirplaneRadios)

setAirplaneRadios

var ok = setAirplaneRadios( str disableRadios )

Specify the radios which will be disabled when the device enters
Airplane Mode.

disableRadios is a comma-separated list with radio names from
the following set: cell, nfc, wifi, wimax, bt.

Get the current value with:

var radios = global( 'AIRR' );

See also: function setAirplaneMode [setAirplaneMode](#setAirplaneMode)

setAlarm

var ok = setAlarm( int hour, int min, str message, bool confirmFlag )

Create an alarm in the default alarm clock app.

confirmFlag specifies whether the app should confirm that the alarm has been set.

message is optional.

Requires Android version 2.3+.

setAutoSync

var ok = setAutoSync( bool setOn )

Enable or disable the global auto-sync setting.

scanCard

var ok = scanCard( str path )

Force the system to scan the external storage card for new/deleted media.

If path is defined, only that will be scanned.

See also: action Scan Card [Scan Card](help/ah_scan_card.html)

setBT

var ok = setBT( bool setOn )

Enable or disable the Bluetooth radio (if present).

Test BT state with:

if ( global( 'BLUE' ) == "on" ) { doSomething(); }

setBTID

var ok = setBTID( str toSet )

Set the bluetooth adapter ID (the name as seen by other devices).

setGlobal

setGlobal( str varName, str newValue )

Set the value of a Tasker global user variable. Prefixing varName with % is optional.

Arrays are not supported due to limitations of the Android JS interface.

setKey

var ok = setKey( str keyName, str passphrase  )

Set the passphrase for the specified keyName.

See Also: Encryption [Encryption](encryption.html)  in the Userguide.

setLocal

setLocal( str varName, str newValue )

Set the value of a Tasker scene-local user variable. Variable names should not
be prefixed with %.

This function is only for use by JavaScript embedded in HTML and accessed via
a WebView scene element.

setClip

var ok = setClip( str text, bool appendFlag )

Set the global system clipboard.

Test the value with:

var clip = global( 'CLIP' );

settings

var ok = settings( str screenName )

Show an Android System Settings screen.

screenName must be one of all, accessibility, addacount, airplanemode,
apn, app, batteryinfo, appmanage
bluetooth, date, deviceinfo, dictionary, display, inputmethod, internalstorage,
locale, location, memorycard, networkoperator, powerusage, privacy, quicklaunch,
security, mobiledata, search, sound, sync, wifi, wifiip or wireless.

setWallpaper

var ok = setWallpaper( str path )

Set the system home screen wallpaper.

setWifi

var ok = setWifi( bool setOn )

Enable or disable the Wifi radio (if present).

Test wifi state with:

if ( global( 'WIFI' ) == "on" ) { doSomething(); }

shell

var output = shell( str command, bool asRoot, int timoutSecs )

Run the shell command command.

asRoot will only have effect if the device is rooted.

output is 'undefined' if the shell command failed. It's maximum size is
restricted to around 750K.

showScene

var ok = showScene( str name, str displayAs, int hoffset, int voffset, bool showExitIcon, bool waitForExit )

Show the named scene [scene](scenes.html) , creating it first if necessary.

- displayAs: options: Overlay, OverBlocking, OverBlockFullDisplay, Dialog, DialogBlur, DialogDim,
ActivityFullWindow, ActivityFullDisplay, ActivityFullDisplayNoTitle

- hoffset, voffset: percentage vertical and horizontal offset for the scene -100% to 100% (not relevant for
full screen/window display types)

- showExitIcon: display a small icon in the bottom right which destroys the scene when pressed

- waitForExit: whether to wait for the scene to exit before continuing the script

shutdown

var ok = shutdown()

Shutdown the device.

Requires a rooted device.

See also: reboot [reboot](#reboot)

silentMode

var ok = silentMode( str mode )

Set the system silent ('ringer') mode.

mode must be one of off, vibrate or on

sl4a

var ok = sl4a( str scriptName, boolean inTerminal )

Run a previously created SL4A [SL4A](https://code.google.com/p/android-scripting/)  script.

soundEffects

var ok = soundEffects( bool setTo )

Setting the system Sound Effects setting (sound from clicking on
buttons etc.

speakerphone

var ok = speakerPhone( bool setFlag )

Enable or disable the speakerphone function.

statusBar

var ok = statusBar( bool expanded )

Expand or contract the system status bar.

stayOn

var ok = stayOn( str mode )

Specify whether the device should remain on when power is connected.

Possible modes are never, ac, usb, any.

stopLocation

var ok = stopLocation()

Stop tracking a location provider. This is only relevant when a getLocation [getLocation](#getLocation)
function has been previously called with the keepTracking parameter set.

systemLock

var ok = systemLock()

Turn off the display and activate the keyguard.

Requires Tasker's Device Administrator to be enabled in Android settings.

taskRunning

bool running = taskRunning( str taskName )

Whether the named Tasker task is currently running. Returns false if
the task name is unknown.

takeCall

bool ok = takeCall();

Auto-accept an incoming call (if there is one).

takePhoto

bool ok = takePhoto( int camera, str fileName, str resolution, bool insertGallery )

Take a photo with the builtin camera.

- camera: 0 = rear camera, 1 = front camera

- resolution: format WxH e.g. 640x840

- insertGallery: whether to insert the resulting picture in the Android Gallery application

See also: action Take Photo [Take Photo](help/ah_take_photo.html)

type

var ok = type( str text, int repeatCount )

Simulate keyboard typing.

Requires a rooted device.

unzip

boolean ok = unzip( str zipPath, bool deleteZipAfter )

Unpack a Zip archive into the parent directory of the archive.

deleteZip causes the zip archive to be deleted after successful
unpacking.

usbTether

usbTether( bool set )

Enable or disable USB tethering.

See also: action USB Tether [USB Tether](help/ah_tether_usb.html)

vibrate

vibrate( int durationMilliseconds )

Cause the device to vibrate for the specified time.

vibratePattern

vibratePattern( str pattern )

Cause the device to vibrate following the specified pattern, which
consists of a sequence of off then on millisecond durations e.g.

500,1000,750,1000

wait for 500ms, vibrates 1000ms, wait for 750ms, then vibrate for 1000ms.

wait

wait( int durationMilliseconds )

Pause the script for the specified time.

Warning: may cause some preceeding functions not to complete in some situations.
If in doubt, use JavaScript setTimeout() instead.

wifiTether

var ok = wifiTether( bool set )

Enable or disable Wifi tethering.

See also: action Wifi Tether [Wifi Tether](help/ah_tether_wifi.html)

writeFile

var ok = writeFile( str path, str text, bool append )

Write text to file path.

If append is specified, the text will be attached to the
end of the existing file contents (if there are any).

zip

boolean ok = zip( str path, int level, bool deleteOriginalAfter )

Zip a file or directory.

level is the desired compression level from 1-9, with 9 resulting
in the smallest file and the longest compression time.

deleteOriginal causes path to be deleted if the zip operation
is successful.

### Notes

#### Audio Streams

Must be one of call, system, ringer, media, alarm or notification

#### Colours

Colours are specified in AARRGGBB hexadecimal format, with solid white being FFFFFFFF.

#### File Paths

File paths can be specified as either absolute (start with /) or
relative (don't start with /).

Relative file paths are relative to the root of the internal storage media.
So, for example, pics/me.jpg might resolve
to /sdcard/pics/me.jpg.



---

## Tasker: MIDI



##
MIDI

Tasker includes basic support for interacting with a (single) musical instrument which support the MIDI protocol.

You don't need to know anything about MIDI in order to play complex
tunes on an instrument via Tasker.

### Requirements and Setup

The Android ROM on the Android device must support the USB Host protocol.

A USB OTG (On The Go) adapter is required for the Android device.

If the MIDI device has a USB-To-Host connecter, a normal USB lead can then be used from the
OTG adapter to the MIDI device.

If the MIDI device has only MIDI inputs, a USB-To-MIDI adapter must be used from the OTG adapter
to the MIDI device.

When a connection has been established with the MIDI device, Android should ask whether permission
should be granted to Tasker to use the device. In order to make things easier and allow automation
without user-interaction, it's recommended that Always be selected.

### Action: MIDI Play

Tasker supports playing of notes in various voices and on multiple channels via the MIDI Play action in the Media category.

The Score parameter in the MIDI Play action uses a Tasker-specific format to hopefully allow even non-musicians to easily 'code' some music.

#### Examples:

- C

plays a single C note and stops

- D D

plays a D twice

- D . . C

plays a D, wait 2 beats, then plays a C

- CDA# or C,D,A#

plays a C, D and A# simultaneously

- D!10

plays a D very softly

- D!10 !100,C C C

plays a D very softly then a few loud Cs

- C2 C3 C4

Plays three Cs of increasing octaves (higher pitch)

- D*4

plays a D for 4 beats

- C#/4

plays a C for a quarter beat

- C#/4D

plays a C for a quarter beat and simultaneously a D for a full beat

- @1 C C C

Selects voice 1 then plays 3 Cs

- C@1,D@2 or C@1D@2

Plays a C with voice 1 and a D with voice 2

- @1 C
@2 E*4

Plays a C on the first channel with voice 1, while playing and holding
an E on the second channel with voice 2.

- C A

B D

Plays C A B D on channel zero. Note that just starting a new line
would mean creating a new channel.

- C A
A B

B D
C D

Plays C A B D on channel 0 while playing simultauously
A B C D on channel 1.

#### Note Specification

A note specification can be made up of several parts indicating different things about what and how to play. The note itself must be the first part, all other
parts are optional.

The Note

Possible notes for the English locale are C, C#, D, D#, E, F, F#, G, G#, A, A#, B. These represent the notes
starting at middle C on a piano, which are in the 4th octave. Flat
notes are also possible e.g. D_.

Deeper notes can be achieved
by specifying a lower octave e.g. E2 or A#3 and higher notes a higher octave
e.g. C6.

For convenience, lower case versions of the notes are an octave
deeper than the upper case versions e.g. c is equivalent
to C3.

Other locales may have different note naming conventions.

Note Duration (Optional)

A note is by default held for one beat. A * indicates the
note should be held longer e.g. C*6 holds a C for 6 beats.
A / indicates the note should be shorter e.g. C/2
indicates that the note should be played for half a beat.

Note Velocity

Velocity usually indicates to a MIDI instrument how hard to play the note. It's represented in Tasker via an
exclamation mark e.g. !6 means 'play this note with velocity 6'.

The lowest value is 0 and the highest 127.

Note Voice

Voice specifies which instrument to play a note with. It's represented in Tasker by an @ sign
e.g. C@1 'play a C using voice 1'.

The voice can be from 0 to 127.

Most MIDI instruments don't have more than 128 voices and so you
probably don't need to read any further in this section.

However, if your instrument has more voices you will probably
need to specify them using the values MSB and/or LSB
which you will need to find in the instrument's user manual.

Tasker allows specificaton of LSB and Program
(the name of the basic parameter) together e.g: B@3.1
specifies LSB 3 and Program 1.

To specify an MSB also, add it on the left e.g. D@6.5.3
specifies MSB 6, LSB 5 and Program 3.

#### Chords

Several notes can be played at the same time by grouping them
together (no whitespace) or separating them with
commas e.g. C,D and CD both play a C and a D.

#### Channels and Beats

A specification of a single note or chord is called a beat.

A channel consists of a set of beats separated by whitespace which are dealt with one-by-one at the same time as the corresponding
beats on other channels. In that way, it's possible to see which notes are going to be played simultaneously.

Beats usually consist purely of a few notes, but they can also
specify default values of velocity and voice for the channel.

For example, !10,C D E!100 F will play a quiet C,
a quiet D, a loud E then a quiet F. @2 C D E@3 F plays a C then a D in voice 2, an E in voice 3, then an F in voice 2 again.

When you reach the end of a line with a channel, do not go
further on the next line. If you do so, the next line will be treated
as a new channel. Instead, leave a blank line.

See the last two examples above.

A dash character - as the  whole beat means 'do nothing this beat'.

A dash followed by a number will rest for that number of beats. This will mess
up the channel alignment, but can be useful for channel which isn't used
very often.

#### Bars

A bar is a character that divides music into pieces of equal length.
Tasker totally ignores | characters so they do not
count as a beat.

#### Comments

The remainder of a line can be ignored by inserting a single quotation character '.
The line before the quotation mark, and subsequent lines, are unaffected.

The rest of a whole channel can be ignored by inserting a double quotation mark ".
The line before the quotation marks are unaffected.

Comments can be useful for testing specific parts of a score independently.

#### Variable Support

The Score parameter supports variable just like most other
places in Tasker.

That means you can e.g. specify a voice specification
with Variable Set and then use the name to make it easier to read
the music e.g. @%piano,C @%guitar,D (play a C
with piano then a D with guitar: assuming you've first set
the variables to a voice which matches their name on your
MIDI instrument)

You can also define variables with sequences of notes and then
define a song as being repeating names e.g. %intro %verse %chorus %verse %end.

#### Music 'Programming'

MIDI Play actions can of course be interspersed with other Tasker actions
so that you can do things like loops which play a piece of music at different
pitch levels, loudness, speed etc Here's a task which plays a long chord
with 10 different instrument and each instrument at 5 different velocities
(loudness levels).

For, %loudness, 20:100:20
For, %voice, 1:10
MIDI Play, @%voice,!%loudness C,E,G

### Tested Devices

Tasker has been tested with the following devices:

- Yamaha Clavinova 480

Please let the developer know if you can confirm it working on other
devices.



---

## Tasker: Power Usage



##
Power Usage

Internally, Tasker does its best to keep power usage down. Following are some macro-strategies to
achieve this.

#### Context Monitoring

When a profile contains multiple contexts, power is saved by only monitoring for changes in order of
the least-power-hungry first. For example, in a profile with a Time and App context, Tasker will not
decide that it needs to monitor for a changing application unless the Time context is active (because the
profile cannot become active until both contexts are active).

Tasker rates contexts for power-hungriness in the following (ascending) order:

- Other State

- Day / Time

- Calendar Entry State

- Cell Near State

- App

- BT Near State

- Network Location

- Wifi Near State

- GPS Location

- Temperature / Humidity / Proximity / Pressure / Magnetic Field / Light Sensor /  Gesture Event / Orientation State (accelerometer activation)

Items at the bottom of the list won't become eligible for monitoring until all items further up the
list are active.

#### Display-Off Checks

When the display is off, all necessary 'active' checks (GPS/Net Location, Wifi Near, App) are done at
the same time so that the device is awake for as short a time as possible. See Display Off Timings
in Menu / Prefs / Monitor for the frequency and maximum duration of these checks.



---

## Tasker for Android



body {
color: #FFF3E0
}

.change_title {
font-size: 110%;
font-weight: bold;
}

.video_demo {
font-size: 105%;
font-weight: bold;
}

Tasker

Home [Home](/index.html)

Direct Purchase [Direct Purchase](https://taskernet.com/?licenses)

Download [Download](/download.html)

TaskerNet [TaskerNet](/taskernet.html)

Home Automation [Home Automation](/home_automation.html)

Usage Examples [Usage Examples](exampleuses.html)

Pre-made Projects [Pre-made Projects](https://forum.joaoapps.com/index.php?resources/)

FAQs [FAQs](/faq.html)

Guides [Guides](/guides.html)

Reviews [Reviews](/reviews.html)

Wiki [Wiki](/wiki)

Plugin List [Plugin List](/pluginlist.html)

Forum

Forum/Support [Forum/Support](https://www.reddit.com/r/tasker/)

Legacy Forum [Legacy Forum](https://tasker.joaoapps.com/forum)

Userguide (5.0+)

Index:
en [en](/userguide/en/index.html)
es [es]( /userguide/es/index.html)
fr [fr](/userguide/fr/index.html)
zh [zh]( /userguide/zh/index.html)

1 Page:
en [en](/userguide_summary.html)

More

Join [Join](/join.html)

AutoApps [AutoApps](https://joaoapps.com/)

Developers [Developers](/developers.html)

History [History](/history.html)

Privacy Policy [Privacy Policy](/privacy.html)

Release Notes [Release Notes](/changes.html)

Next Version [Next Version](/changes/nextversion.html)

Feature Requests [Feature Requests](https://tasker.helprace.com/s1-general/ideas/new)

Report Issues [Report Issues](https://tasker.helprace.com/s1-general/problems/top)

Patreon [Patreon](/patreon.html)

##
FAQ: App Creation

- Does app creation support profiles and scenes ? [Does app creation support profiles and scenes ?](#c)

- Why is the app always shown as running ? [Why is the app always shown as running ?](#a)

- How do I do initialization on the first launch ? [How do I do initialization on the first launch ?](#b)

- How can my task tell if it is running in Tasker or a child app ? [How can my task tell if it is running in Tasker or a child app ?](#h)

- Why isn't my app detecting background events ? [Why isn't my app detecting background events ?](#d)

- How can I send the developer a short-term App Factory log ? [How can I send the developer a short-term App Factory log ?](#e)

- How can I send the developer a long-term App Factory log ? [How can I send the developer a long-term App Factory log ?](#e2)

- Can I include Google Play's licencing service in my app ? [Can I include Google Play's licencing service in my app ?](#f)

- Can I get the java source code from my created app ? [Can I get the java source code from my created app ?](#g)

#### Does app creation support profiles and scenes ?

Sure. You can export projects as apps and projects can contain
profiles, tasks and scenes.

For help accessing projects, see Menu / Info / Help This Screen
in the main screen.

#### Why is the app always shown as running ?

Tasker tries to detect when it's monitor service is no longer needed but that is
not always possible. You can put a Disable action from the Tasker
category at the end of your launch task to ensure that it happens.

The monitor will be started again automatically each time the app is lauched from the home
screen.

#### How do I do initialization on the first launch ?

Setup your launch task something like this:

If %LaunchCount = 0
...initialization actions...
Else
...normal actions...
Elsif
Variable Add, %LaunchCount, 1

#### How can my task tell if it is running in Tasker or a child app ?

Use the Test App action and select the mode This Package.

The resulting variable will contain the package identifier you specified in the
App Configuration screen if the task is running in a child app, otherwise
it will contain one of net.dinglisch.android.tasker or net.dinglisch.android.taskerm.

#### Why isn't my app detecting background events ?

One possible cause is: when an app has just been installed on Android it is in a 'frozen' state until
there is some user interaction with it (usually clicking the home screen icon
at least once).

#### How can I send the developer a short-term App Factory log ?

- download aLogcat, free from Android Market

- disable Tasker in the main screen bottom-left

- in the App Config screen, check Advanced Properties and then Debug

- create and install the new app *twice*

- launch the new app from the home screen

- reproduce whatever conditions cause the problem

- go to aLogCat, click Menu / Pause then Menu / Send

- the destination email is listed in Menu / Info / User Support in Tasker

- include at the top a brief description of the problem that the email concerns

Try to make the log as soon as possible after the problem occurs.

#### How can I send the developer a long-term App Factory log ?

- disable Tasker by long-clicking the icon top-left in the main screen

- in the App Config screen, check Advanced Properties and then Debug

- create and install the new app *twice*

- enable the Storage permission for the app in Android Settings if necessary

- launch the new app from the home screen

- reproduce whatever conditions cause the problem

- send the developer the log files in the directory NAMEOFAPP in the root directory of the SD card

- the destination email is listed in Menu / Info / User Support in Tasker

- include at the top a brief description of the problem that the email concerns

Try to make the log as soon as possible after the problem occurs.

#### Can I include Google Play's licencing service in my app ?

No, this is not possible.

Tasker's code does not include the licencing service because of continual problems
it caused. In any case, the licensing service is ineffectual for preventing
unauthorized code distribution.

If you really want to include licensing in your app, you could e.g. require the
user to enter their order code and check via the HTTP Get action on your
server if that is a valid number.

Setting up such a server to download Google order details and accept verification
requests is a lot of effort and requires some technical knowledge, however.

#### Can I get the java source code from my created app ?

Short answer: no.

Long answer: when a new app is created, Tasker doesn't create new java code to
implement the things in your task or project configuration. Instead, the existing
Tasker code is used with the new app and executed similarly to how it's executed
in Tasker, but in the shell of a new APK.



---

## Tasker for Android



body {
color: #FFF3E0
}

.change_title {
font-size: 110%;
font-weight: bold;
}

.video_demo {
font-size: 105%;
font-weight: bold;
}

Tasker

Home [Home](/index.html)

Direct Purchase [Direct Purchase](https://taskernet.com/?licenses)

Download [Download](/download.html)

TaskerNet [TaskerNet](/taskernet.html)

Home Automation [Home Automation](/home_automation.html)

Usage Examples [Usage Examples](exampleuses.html)

Pre-made Projects [Pre-made Projects](https://forum.joaoapps.com/index.php?resources/)

FAQs [FAQs](/faq.html)

Guides [Guides](/guides.html)

Reviews [Reviews](/reviews.html)

Wiki [Wiki](/wiki)

Plugin List [Plugin List](/pluginlist.html)

Forum

Forum/Support [Forum/Support](https://www.reddit.com/r/tasker/)

Legacy Forum [Legacy Forum](https://tasker.joaoapps.com/forum)

Userguide (5.0+)

Index:
en [en](/userguide/en/index.html)
es [es]( /userguide/es/index.html)
fr [fr](/userguide/fr/index.html)
zh [zh]( /userguide/zh/index.html)

1 Page:
en [en](/userguide_summary.html)

More

Join [Join](/join.html)

AutoApps [AutoApps](https://joaoapps.com/)

Developers [Developers](/developers.html)

History [History](/history.html)

Privacy Policy [Privacy Policy](/privacy.html)

Release Notes [Release Notes](/changes.html)

Next Version [Next Version](/changes/nextversion.html)

Feature Requests [Feature Requests](https://tasker.helprace.com/s1-general/ideas/new)

Report Issues [Report Issues](https://tasker.helprace.com/s1-general/problems/top)

Patreon [Patreon](/patreon.html)

##
FAQ: How Do I... / Can I... ?

- How can I contact the developer ?

- How can I send the developer a bug report ?

- How can I send the developer a long-term log ?

- Can I change an app's settings / press it's buttons ? [Can I change an app's settings / press it's buttons ?](#a)

- Can I control / respond to events in application X with Tasker ? [Can I control / respond to events in application X with Tasker ?](#o)

- How can I stop Tasker restoring a setting ? [How can I stop Tasker restoring a setting ?](#cx)

- Can Tasker detect volume button presses ? [Can Tasker detect volume button presses ?](#c)

- Can Tasker be used from an external SD card ? [Can Tasker be used from an external SD card ?](#d)

- Can I use Tasker to turn the screen on and off ? [Can I use Tasker to turn the screen on and off ?](#e)

- How do I create my default settings ? [How do I create my default settings ?](#f)

- How can I run more than one task when a profile goes active ? [How can I run more than one task when a profile goes active ?](#g)

- Can I hide the notification list entry when Tasker is running ? [Can I hide the notification list entry when Tasker is running ?](#h)

- Can I change or remove the status bar icon when Tasker is running ? [Can I change or remove the status bar icon when Tasker is running ?](#h2)

- What if I want a repeating time context, but I need to do something that takes a while ? [What if I want a repeating time context, but I need to do something that takes a while ?](#i)

- How can I do something every minute ? [How can I do something every minute ?](#j)

- How do I specify 9:30AM on Monday and 10AM on Tuesday with the same profile ? [How do I specify 9:30AM on Monday and 10AM on Tuesday with the same profile ?](#k)

- How do I specify weekend night-times ? [How do I specify weekend night-times ?](#k2)

- How do I stop the screen dimming when I have the display Stay On set to e.g. 'With AC' ? [How do I stop the screen dimming when I have the display Stay On set to e.g. 'With AC' ?](#l)

- How can I stop Wifi Near toggling wifi on-off when the phone is in Airplane Mode ? [How can I stop Wifi Near toggling wifi on-off when the phone is in Airplane Mode ?](#m)

- Can I divert incoming calls ? [Can I divert incoming calls ?](#n)

- How can I detect if Wifi is connected (not just enabled) ? [How can I detect if Wifi is connected (not just enabled) ?](#p)

- How can I import/export individual profiles, tasks or scenes ? [How can I import/export individual profiles, tasks or scenes ?](#q)

- How do I turn off the flashing notification LED ? [How do I turn off the flashing notification LED ?](#s)

- How do I put my phone in Silent or Vibrate mode ? [How do I put my phone in Silent or Vibrate mode ?](#t)

- Can I automate sending of an SMS / Call through Google Voice ? [Can I automate sending of an SMS / Call through Google Voice ?](#u)

- Can I change/remove the notification sounds for particular apps ? [Can I change/remove the notification sounds for particular apps ?](#v)

- Can I silence all notifications except from particular applications ?

- Can I change the input method ? [Can I change the input method ?](#w)

- How do I test whether I can reach the Internet (ping) ? [How do I test whether I can reach the Internet (ping) ?](#y)

- How can I use whitespace (newline, tab etc) in action parameters ? [How can I use whitespace (newline, tab etc) in action parameters ?](#y2)

- How can I run a task from a terminal login ? [How can I run a task from a terminal login ?](#y3)

- How can I silence the camera shutter sound ? [How can I silence the camera shutter sound ?](#y4)

#### How can I contact the developer ?

There is a contact email given at Menu / Info / Support. In
general, this is intended for order and validation help, which is
often confidential, and other private issues.

Please post Tasker usage queries/problems in the Tasker Forum [Tasker Forum](http://groups.google.com/group/tasker)  where the developer is very active.

Advantages:

- the user community has more experience than the developer with using Tasker

- other people can benefit if your problem is solved

- the developer has more time for fixing bugs and adding features, which benefits everyone

#### How can I send the developer a bug report ?

- go to Android Settings then About Phone

- tap 10 or more times on the Build Version entry

- go back one screen

- select Developer Options

- check the USB Debugging option if it's not already checked

- do whatever it is that causes the problem

- go back to Developer Options and tap Take Bug Report (the first entry)

- wait a short while until the bug report is ready (a notification will appear)

- share using an email application

- the destination email address is listed in Menu / Info / Support in Tasker

- include at the top of the email a brief description of the problem that the email concerns

- disable USB Debugging and Developer Options (switch at top)

Try to make the log as soon as possible after the problem occurs.

#### How can I send the developer a long-term log ?

- deselect Menu / Prefs / UI / Beginner Mode in Tasker

- enable Menu / Prefs / Misc / Debug to Internal Storage in Tasker

- when the problem has occured, email the file /sdcard/Tasker/log/tasker.txt
(and tasker.txt.1, if it exists)  to
the developer email listed at Menu / Info / Support

- include at the top a brief description of the problem that the log concerns

#### Can I change an app's settings / press it's buttons ?

Standard Android doesn't allow an app to change, poke, prod or peek at anything within another app,
including simulating keypresses and screen taps.

On a rooted device, you can use some of the actions in the Input
category to navigate around an app, click on UI elements and enter text automatically.

#### Can I control / respond to events in application X with Tasker ?

If a Tasker user wants to automate some aspect of another program they use, they just need to point the developer of the other app at the Tasker Developer Page [Tasker Developer Page](/developers.html)  and nag at him/her a bit.

#### How can I stop Tasker restoring a setting ?

Tasker will restore any setting which is changed in the Enter
task of a profile.

There are four ways to prevent this:

- deselect the Restore Settings in the Profile Properties
of the relevant profile.

- if you set the same setting in the Exit task of the profile
Tasker will take that as a hint that the previous value shouldn't be
restored.

- create a separate task to run the settings actions and
in the Enter task of the profile do a Perform Task action
(from the category Tasker) on that separate task. This trick is
known as Stefan's Setting Sidestep.

- you can use the corresponding Javascriptlet function
instead of the setting action. Settings made in Javascriptlets are
not restored.

#### Can Tasker detect volume button presses ?

No, sorry, that's not possible ATM.

The closest you can get is to detect changes in a volume variable
(e.g. %VOLR for the ringer volume) via event Variable Set.

#### Can Tasker be used from an external SD card ?

Prior to Android 6.0, that is not possible, even using apps2SD.

With Android 6.0+ if the external SD is being used as 'adoptable', 'flex' or 'internal'
(the wording varies) storage, there should be no issue.

#### Can I use Tasker to turn the screen on and off ?

Turning on, use the Display / Turn On action. Unfortunately, that action
is inaccessible with Android 2.3+.

For turning off, you can use the Display / System Lock action with Android 2.0+.

For Android 1.6, you can set the Display Timeout to it's minimum (around 7 seconds)
and then set it back to normal in response to a Display Off event.

#### How do I create my default settings ?

You don't have to configure 'default' settings in Tasker.
The 'default' settings are how your device is configured before any Tasker profile becomes
active. This 'default' is automatically restored as profiles become inactive.

Exception: changes to settings made in Exit tasks are not restored.

#### How can I run more than one task when a profile goes active ?

Add an action Perform Task from the category Tasker for
each task that you want to run (don't click the Stop button).

Warning:: settings in the called tasks will not be restored by Tasker,
only settings changed directly within the Enter task.

#### Can I hide the notification list entry when Tasker is running ?

If the notification is very annoying, it can be removed
on many devices by setting the icon transparent at
Menu / Prefs / Monitor / Notification Icon.

If that doesn't work, disable the Run In Foreground setting which can be found
at Menu / Prefs / Monitor / Run In Foreground

Please read the help text associated with this option first.

#### Can I change or remove the status bar icon when Tasker is running ?

You can change it with Menu / Prefs / Monitor / Notification Icon.

You can remove it with Menu / Prefs / Monitor / Show Notification Icon.

#### What if I want a repeating time context, but I need to do something that takes a while ?

- GPS On

- Wait 3 minutes

- GPS Off

#### How can I do something every minute ?

Set a repeat period of 2 minutes (the minumum allowed) and specify a task
like this:

- Perform Task, TaDa

- Wait 1 Minute

- Perform Task, TaDa

#### How do I specify 9:30AM on Monday and 10AM on Tuesday with the same profile ?

You can't, because the Time and Day subcontexts operate completely independent of
each other. You have to specify two profiles and run the same Task(s) with each of
them (by giving the task a name).

#### How do I specify weekend night-times ?

It's tempting to say:

Time: 23 - 09

Day: Friday or Saturday

But that won't work, because on Sunday at e.g. 3am the Day context (and hence the
whole profile) won't be active.

For this kind of situation, you need to specify a profile for which morning you want
to be active and another for which evenings. In the example, you want Friday and
Saturday night plus Saturday or Sunday morning:

Time: 23 - 24

Day: Friday or Saturday

Time: 00 - 09

Day: Saturday or Sunday

#### How do I stop the screen dimming when I have the display Stay On set to e.g. 'With AC' ?

The screen dims around 10 seconds before the current Screen Off Timeout value is
reached. You can set Screen Timeout (for the relevant context e.g. 'while docked')
to Never (set all sliders to maximum) if you don't like that behaviour.

#### How can I stop Wifi Near toggling wifi on-off when the phone is in Airplane Mode ?

Add a state Airplane Mode to your profile and click the Invert button, which
means if Airplane Mode is off.

#### Can I divert incoming calls ?

It's not possible to divert incoming calls via Android, but most Mobile Carriers accept special dialled
sequences to do it before the call reaches your phone.

You can then use Tasker's Phone / Call action (with Auto Dial checked) to setup
and cancel incoming call diversions.

The Wikipedia page on Call Forwarding [Wikipedia page on Call Forwarding](http://en.wikipedia.org/wiki/Call_forwarding)  is a good starting point.

#### How can I detect if Wifi is connected (not just enabled) ?

The 'standard' way is to use State Wifi Connected to set and clear your own variable with
an enter and exit task respectively.

An alternative trick is to match the word connected or connection in the %WIFII variable (the actual word and lower/upper case changes with Android version).

#### How can I import/export individual profiles, tasks or scenes ?

Import:

Go to the main screen, long click on the tab for the type of thing you want to import.

Export:

- ensure that Menu / Prefs / UI / Beginner Mode is unchecked

- go to the main screen

- long-click on the thing you want to export

#### How do I turn off the flashing notification LED ?

Use the Audio / Notification Pulse action.

If you're wondering what a flashing light is doing in the Audio section: ask Google,
that's where they put it in Android Settings.

#### >How do I put my phone in Silent or Vibrate mode ?

Use action Audio / Silent Mode.

Do not try to do it with Volume Ringer or Vibrate on Ringer.

#### Can I automate sending of an SMS / Call through Google Voice ?

Not directly through Tasker. However,
Steelgirder Developments [Steelgirder Developments](http://sites.google.com/site/steelgirderdevelopmentsite/home)  have
(non-free) plugins which you can easily use with Tasker to accomplish this.

Steelgirder and the author of Tasker are agreed on working together wherever further
integration of these plugins and Tasker is needed e.g. support for Tasker variables.

#### Can I change/remove the notification sounds for particular apps ?

Yes, but it's a little complicated, please see the
relevant forum post [relevant forum post](http://groups.google.com/group/tasker/browse_thread/thread/4a6b6ea8b4e4cc86) .

#### Can I silence all notifications except from particular applications ?

With Tasker versions from 1.0.10, you can try turning off all notifications
(e.g. via Silent Mode or setting the Notification Volume to 0) and then
using Tasker to do alerts for particular app notifications using the
Notification event in the UI category.

#### Can I change the input method ?

On a rooted phone, yes, using the free Secure Settings plugin.

Consider also starring this feature request [feature request](http://code.google.com/p/android/issues/detail?id=11677)  with Google.

#### How do I test whether I can reach the Internet (ping) ?

HTTP Get URL (a known webpage), Continue Task On Error
If [ %HTTPR = 200 ]
...
Endif

#### How can I use whitespace (newline, tab etc) in action parameters ?

Tasker trims the start and end of all parameters to prevent whitespace causing problems.
The only exception is the Variable Set action.

Therefore, if you want to use whitespace you should first assign it to a variable and then
use the variable where you want the whitespace to appear:

Variable Set, %white, THISISANEWLINE

Flash, Here's a newline: %white

#### How can I run a task from a terminal login ?

am broadcast -a net.dinglisch.android.tasker.ACTION_TASK -e task_name YOUR_TASK_NAME

That's only possible on a rooted phone because otherwise there will be a permission problem.

#### How can I silence the camera shutter sound ?

This varies per device.

Try creating a new profile with an App context
and select the Camera app. When asked to create a task,
add the following actions:

- Task / Wait, 2 seconds

- Audio / Sound Effects, off

- Audio / Media Volume, 0

- Audio / System Volume, 0

- Audio / Notification Volume, 0

- Audio / Silent Mode, on

Then go to the Camera app, wait a couple of seconds  and try taking a picture.

If you still hear the shutter
sound, go back to the Tasker UI, click on the task that you created and hit
the Play button bottom-left to run the task manually. Then go
back to the Camera app. If you still hear the shutter sound, then it's
not going to be possible for Tasker to disable it on your device.

Some manufacturers deliberately prevent disabling of the shutter sound,
perhaps for legal reasons.

Addendum

A user has reported that setting DTMF volume to 0 removes the focus sound
in the camera app.



---

## Tasker for Android



body {
color: #FFF3E0
}

.change_title {
font-size: 110%;
font-weight: bold;
}

.video_demo {
font-size: 105%;
font-weight: bold;
}

Tasker

Home [Home](/index.html)

Direct Purchase [Direct Purchase](https://taskernet.com/?licenses)

Download [Download](/download.html)

TaskerNet [TaskerNet](/taskernet.html)

Home Automation [Home Automation](/home_automation.html)

Usage Examples [Usage Examples](exampleuses.html)

Pre-made Projects [Pre-made Projects](https://forum.joaoapps.com/index.php?resources/)

FAQs [FAQs](/faq.html)

Guides [Guides](/guides.html)

Reviews [Reviews](/reviews.html)

Wiki [Wiki](/wiki)

Plugin List [Plugin List](/pluginlist.html)

Forum

Forum/Support [Forum/Support](https://www.reddit.com/r/tasker/)

Legacy Forum [Legacy Forum](https://tasker.joaoapps.com/forum)

Userguide (5.0+)

Index:
en [en](/userguide/en/index.html)
es [es]( /userguide/es/index.html)
fr [fr](/userguide/fr/index.html)
zh [zh]( /userguide/zh/index.html)

1 Page:
en [en](/userguide_summary.html)

More

Join [Join](/join.html)

AutoApps [AutoApps](https://joaoapps.com/)

Developers [Developers](/developers.html)

History [History](/history.html)

Privacy Policy [Privacy Policy](/privacy.html)

Release Notes [Release Notes](/changes.html)

Next Version [Next Version](/changes/nextversion.html)

Feature Requests [Feature Requests](https://tasker.helprace.com/s1-general/ideas/new)

Report Issues [Report Issues](https://tasker.helprace.com/s1-general/problems/top)

Patreon [Patreon](/patreon.html)

##
FAQ: Other

- Do you plan to include feature X ? [Do you plan to include feature X ?](#a)

- Should I worry about using Tasker's Accessibility service ? [Should I worry about using Tasker's Accessibility service ?](#b)

- What's the difference between a Widget and a Shortcut ? [What's the difference between a Widget and a Shortcut ?](userguide/en/app_widgets.html#diff)

- What's an Instant Profile ? [What's an Instant Profile ?](#instant)

#### Do you plan to include feature X ?

The developer has a large list of potential features and works through it according
to a mystical method based on star configurations. It's difficult to say what
will be done in advance, sorry.

#### Should I worry about using Tasker's Accessibility service ?

Not at all.

Although the Android warning says Tasker might read passwords, in fact:

- Android doesn't allow apps to see the contents of fields labelled Password

- Tasker doesn't even ask Android for data about text fields, only buttons, windows
and notifications

#### What's an Instant Profile ?

Most profiles have a duration. Their enter task fires, they are active for a while, then they go inactive and settings
may be restored or an exit task fired. However, profiles with

- an Event context, or

- a Time context where the From parameter is the same as the To parameter, or

- a Time context with a repeat value specified

are only active for an instant and hence it does not make sense to talk about an exit task and restoration of settings.

There's no point setting brightness from 200 to 30, and then a millisecond later back to 200,
therefore settings made by an instant profile stay at whatever value is specified.



---

## Tasker for Android



body {
color: #FFF3E0
}

.change_title {
font-size: 110%;
font-weight: bold;
}

.video_demo {
font-size: 105%;
font-weight: bold;
}

Tasker

Home [Home](/index.html)

Direct Purchase [Direct Purchase](https://taskernet.com/?licenses)

Download [Download](/download.html)

TaskerNet [TaskerNet](/taskernet.html)

Home Automation [Home Automation](/home_automation.html)

Usage Examples [Usage Examples](exampleuses.html)

Pre-made Projects [Pre-made Projects](https://forum.joaoapps.com/index.php?resources/)

FAQs [FAQs](/faq.html)

Guides [Guides](/guides.html)

Reviews [Reviews](/reviews.html)

Wiki [Wiki](/wiki)

Plugin List [Plugin List](/pluginlist.html)

Forum

Forum/Support [Forum/Support](https://www.reddit.com/r/tasker/)

Legacy Forum [Legacy Forum](https://tasker.joaoapps.com/forum)

Userguide (5.0+)

Index:
en [en](/userguide/en/index.html)
es [es]( /userguide/es/index.html)
fr [fr](/userguide/fr/index.html)
zh [zh]( /userguide/zh/index.html)

1 Page:
en [en](/userguide_summary.html)

More

Join [Join](/join.html)

AutoApps [AutoApps](https://joaoapps.com/)

Developers [Developers](/developers.html)

History [History](/history.html)

Privacy Policy [Privacy Policy](/privacy.html)

Release Notes [Release Notes](/changes.html)

Next Version [Next Version](/changes/nextversion.html)

Feature Requests [Feature Requests](https://tasker.helprace.com/s1-general/ideas/new)

Report Issues [Report Issues](https://tasker.helprace.com/s1-general/problems/top)

Patreon [Patreon](/patreon.html)

##
FAQ: Usage Problems

- Why doesn't Tasker work in the background on my device? [Why doesn't Tasker work in the background on my device?](#00)

- Why won't Android let me uninstall Tasker ? [Why won't Android let me uninstall Tasker ?](#0)

- Why isn't GPS coming on for my profile with Time And GPS Location contexts ? [Why isn't GPS coming on for my profile with Time And GPS Location contexts ?](#c)

- Why can't I select Tasker for an application context ? [Why can't I select Tasker for an application context ?](#d)

- Why does it take my Wifi Near state so long to exit ? [Why does it take my Wifi Near state so long to exit ?](#e)

- Why isn't Tasker detecting when my Location Context changes ? [Why isn't Tasker detecting when my Location Context changes ?](#f)

- Why does Tasker mess up the app launching when I have an Application Context for it ? [Why does Tasker mess up the app launching when I have an Application Context for it ?](#g)

- Why does my profile not do anything ? [Why does my profile not do anything ?](#h)

- Why aren't my settings restored ? [Why aren't my settings restored ?](#w)

- Why does nothing happen when I click a Tasker widget ?

- Why does Tasker crash when I try to create a Location Context ? [Why does Tasker crash when I try to create a Location Context ?](#j)

- Why can't I see any Tasker widgets in the home screen widget selector ? [Why can't I see any Tasker widgets in the home screen widget selector ?](#k)

- Why doesn't my repeating Time Context work ? [Why doesn't my repeating Time Context work ?](#l)

- Why aren't my exit tasks run / settings restored before the device shuts down ? [Why aren't my exit tasks run / settings restored before the device shuts down ?](#m)

- Why does my location exit task fire multiple times ? [Why does my location exit task fire multiple times ?](#n)

- Why does my Cell Near state keep going inactive ? [Why does my Cell Near state keep going inactive ?](#o)

- Why doesn't Notify LED work ? [Why doesn't Notify LED work ?](#p)

- Why do Tasker widgets disappear after a reboot on my Wildfire ? [Why do Tasker widgets disappear after a reboot on my Wildfire ?](#q)

- Why isn't my docking station detected ? [Why isn't my docking station detected ?](#r)

- Why aren't I getting any cell data for the Cell Near state ? [Why aren't I getting any cell data for the Cell Near state ?](#s)

- Why isn't there a green light for the On/Off radio button on the main screen ? [Why isn't there a green light for the On/Off radio button on the main screen ?](#t)

- Why does the action Display Brightness cause my keyboard or application to close ? [Why does the action Display Brightness cause my keyboard or application to close ?](#u)

- Why is the date in Tasker's notification list completely wrong ? [Why is the date in Tasker's notification list completely wrong ?](#v)

- Why won't Tasker install on my custom ROM ? [Why won't Tasker install on my custom ROM ?](#w)

- Why doesn't my Perform Task action work when I Test it ? [Why doesn't my Perform Task action work when I Test it ?](#x)

- Why doesn't my App Context work ? [Why doesn't my App Context work ?](#app)

- Why doesn't the Keyguard action work properly ? [Why doesn't the Keyguard action work properly ?](#keyguard)

- Why doesn't Tasker think my device is rooted ? [Why doesn't Tasker think my device is rooted ?](#root)

- Why doesn't Tasker show my Local Media images anymore ? [Why doesn't Tasker show my Local Media images anymore ?](#img)

#### Why don't Tasker or its plugins work in the background on my device?

To make sure Tasker and its plugins run in the foreground:

- make sure Tasker is enabled

- enable foreground notification in Tasker Preferences (this will be automatically enabled on Android 8+, so no need to worry if you have recent versions of Android)

- enable the "Use reliable alarms" option

- If you're on Android 10+ allow Tasker to draw over other apps: Open Tasker - Menu - More - Android Settings - Draw Over Other Apps and enable the permission.

- Check out dontkillmyapp.com [dontkillmyapp.com](https://dontkillmyapp.com/?app=Tasker) . This website will show, for your specific vendor, the best way to allow Tasker to work correctly in the background.

- Disable battery optimization for the apps

- Make sure the Android Settings -> Apps -> Tasker -> Battery -> Background activity option is enabled (this setting may be somewhere else on different OEMs, but it's a very important setting that might be disabled by default on some devices)

- If you want to use features while the screen is off make sure that the options in Preferences -> Monitor -> Display Off Monitoring are enabled for the conditions you want.

- Make sure that you disable any "battery saving" apps like Greenify, etc

- If you want to have Wifi and Cell based profiles work on Android 8+ make sure that location is enabled on your device and that Tasker has location permissions even when in the background. It's an Android requirement that Tasker can't work around.

- If you want accelerometer based profiles to work (like when using the Shake or Orientation conditions) while the screen is off, try setting the Tasker > Preferences > MONITOR tab > Display Off Monitoring > Accelerometer option to Yes, And Keep Android Awake

- On Samsung devices go to Android Settings -> Device Maintenance -> Battery -> Unmonitored apps -> add Tasker and all plugins

- On Xiaomi devices enable "Auto Start" for the apps and "Display on Lock Screen" under "Other Permissions"

- On Xiaomi devices disable automatic backup of apps because that process kills all running apps, including Tasker.

- On Xiaomi devices enable all available options in the Additional Permissions section of the app in System settings [Additional Permissions section of the app in System settings](xiaomi display popup.jpg) .

- On Huawei devices click the  lock in the recents menu [lock in the recents menu](huaweilock.jpg)  for all the plugins and Tasker

- On Huawei devices manage battery optimizations manually in battery settings [battery settings](huaweibatteryoptimizations.jpg)  for all the plugins and Tasker

- On Huawei devices disable Powergenie which stops apps from running in the background. Try going to Settings -> Battery, then tapping on the gear in the upper right corner. Disable "Close excessively power-intensive apps". Or use ADB:

- To disable powergenie use: adb shell pm disable-user com.huawei.powergenie

- To enable powergenie: adb shell pm enable com.huawei.powergenie

- On Lenovo devices (possibly others) you have to disable the "Disable Auto Start" ["Disable Auto Start"](lenovoapps.png)  options for Tasker and all AutoApps.

- If you plan on using plugins, disabling power saver mode may help with some issues

#### Why won't Android let me uninstall Tasker ?

It's probably because you're using an action which needs Tasker's device administrator function (e.g. Display / System Lock).

You can disable it by going to Android Settings / Location & Security / Device Administration.

#### Why isn't GPS coming on for my profile with Time And GPS Location contexts ?

In order to save power, Tasker only activates context detection as it is needed.
Therefore it will not attempt to fix your GPS location unless the Time context is
active.

See the Power Usage [Power Usage](userguide/en/power.html)  section of the userguide
for more details.

#### Why can't I select Tasker for an application context ?

This is considered too dangerous. A mistake could easily result in being unable
to enter Tasker and therefore being unable to rectify the mistake.

#### Why does it take my Wifi Near state so long to exit ?

Wifi Near requires two check periods to pass without seeing the Access Point before the
profile exits. This is intended to avoid the context activating and deactivating if the
AP is briefly not visible.

Note also that there are different check periods for when the device is on or off, and by default
the off-period is much longer than the on-period. See Menu / Preferences / Monitor/ Display On/Off Timings.

#### Why isn't Tasker detecting when my Location Context changes ?

Your radius is probably too small.

As an example, if you are not using GPS the accuracy of your fixes is probably
around += 2km, so your radius should be also minimally 2km.

If you *are* using GPS, the accuracy may still be only +-400m in built-up areas.

Here's a good way to create a location context:

- go to the geographical location you want a context for

- make a new location context

- deselect GPS if you don't want to use it

- press Grab Fix, and wait till it's done

This will set your radius appropriate to the accuracy of the location providers at that spot.

If there's still nothing happening:

- check GPS is on in Android Settings, if you're using GPS.

- check your device has a view of the sky, if you're using GPS

- network connectivity is often needed to get GPS started, and always needed for a Net location context.

- realize that location is only checked every 10 minutes by default when the Display is off (to save power).
You can check more often by changing Menu / Prefs / Monitor / Display Off Timings / All Checks

- try the general 'nothing happens' [general 'nothing happens'](#h)  tips

- look at other possibilities for detecting your location [other possibilities for detecting your location](/userguide/en/loctears.html)

#### Why does Tasker mess up the app launching when I have an Application Context for
it ?

Some applications are sensitive like this. Probably all you have to do is put as the
first action in the Enter task the action Wait and give as a
parameter e.g. 300ms. If that doesn't work keep increasing the value until it does.

That gives the application time to finish initializing before messing around
with the screen brightness etc.

#### Why aren't my settings restored ?

Some possibilities:

- if your profile sets setting x to on, then
if x is already on when the profile goes active, it will be left at 1 when the
profile exits. Test for this by putting an Alert / Notify action in the enter
task to see what the original value was.

- some other apps installed on the system can cause Tasker to be killed and
therefore the original settings being forgotten e.g. this has been reported to be
a problem with Titanium Backup.

- similarly, if the system is rebooted suddenly, some devices aren't fast enough
to save all the settings before the system turns off.

#### Why does my profile not do anything ?

Firstly, if are you using any of these other apps which have been reported as interfering
try disabling or temporarily uninstalling them:

- 'Task Killers'

- Quick System Info

- Autostarts

After that:

- is the profile enabled ? It should have a green tick next to it.

- have you clicked the On button in the Profile List screen [Profile List screen](userguide/en/activity_summary.html)  before leaving Tasker ?
It should be showing a green light.

- is the profile shown as active in the status bar pulldown ? If so, it's probably your task that's not working.

- make sure the Monitor service running in the foreground (see Menu / Prefs / Monitor)

- how's your available memory, see Android Settings / Application / Running Services / Available Memory. Are you maybe getting
Tasker's low-memory notifications ?

If your profile is activating but the task doesn't seem to do anything:

- perhaps you are running a pirated version of Tasker ?

- try enabling Menu / Prefs / More / Popup Warning/Errors to see if any errors are occuring (they may not be shown till you go back to the Tasker UI)

- look in Menu / More / Run Log to see if the task is being carried out.

- try a simple task like Alert / Vibrate or Alert / Flash

- perhaps another profile is interfering: do Menu / Data / Backup, then delete all other profiles except the one that's not working

#### Why does nothing happen when I click a Tasker widget ?

Usually this is due to Tasker not being enabled, see the On/Off button in the first UI screen.

#### Why does Tasker crash when I try to create a Location Context ?

The likely cause is that you are running a non-standard Android ROM which doesn't
contain the correct (or maybe any) Google Maps library.

#### Why can't I see any Tasker widgets in the home screen widget selector ?

This is almost always because you have Tasker installed on the SD card, which is just not
possible due to several reasons related to how Tasker works.

#### Why doesn't my repeating Time Context work ?

It's important to understand that a repeating time context is a series of instant events.

Trying to combine a repeating time context with another context that does
active monitoring usually won't work e.g.

Time: Repeating Every 5 Minutes

Task: Enable Wifi (no toggle)

State: Wifi Near

Task: XXX

Wifi Near is checked on a static schedule. You currently can't change the schedule dynamically,
so the above two profiles will only do XXX when the 5 minute repeat happens to coincide with
when Tasker is doing it's Wifi Near check.

#### Why aren't my exit tasks run / settings restored before the device shuts down ?

Android gives an app very little time to perform cleanup during shutdown, this is especially
a problem on slow devices.

Therefore (as of 1.0.9), Tasker only attempts to run Variable Set, Clear, Add and Subtract actions
when the device shuts down, since they take relatively little time.

In the future, Tasker will have some concept of default values which will then be restored when
it starts after the device has booted again.

On Android 1.5 devices, Tasker cannot do anything at shutdown because the system does not send a notification.

#### Why does my location exit task fire multiple times ?

Probably the location Android reports is bouncing between a point inside
your location radius and one outside. This is relatively unusual because Tasker
has some built-in mechanisms to try and prevent it.

A quick fix is to add a Cooldown to your profile. Click on a context,
select Profile then Properties and slide the Cooldown Time to 30 minutes.

The profile is then prevented from going active more than once every 30 minutes.

#### Why does my Cell Near state keep going inactive ?

Even when your phone is motionless, it will probably still often switch between
different cell towers. Going to a different room in your house may involve
a whole different set of cell towers.

When you notice your Cell Near state going inactive at your location (and assuming
you still have a signal), launch Tasker, click on the Cell Near context and edit
it. Click Scan and you should immediately see a new Cell added to the list.
Click Done and then Apply and your context should go active again.

Sometimes the new cell will only be visible for a few seconds and will not appear
when you press scan. In that case, press the Recent button and
select it manually from the list.

#### Why doesn't Notify LED work ?

From the action help (hint hint):

- not all devices support all colours. Many devices will only support red and green. In general, colours near the top of the list are more likely to be supported.

- some devices will only flash the LED when the device is off at the time the notification is received.

#### Why do Tasker widgets disappear after a reboot on my Wildfire ?

This is a bug on some Wildfire firmware version.

It's not possible for the Tasker developer to
work around, but is reported as fixed in version 1.25.405.1 of the firmware.

#### Why isn't my docking station detected ?

Some docking stations just aren't recognized as such (Android doesn't indicate that
a docking station has been connected).

Depending on other things you connect your device to, you might be able to use one of
the following as a workaround:

- State: USB connected

- State: Power

- State: BT Connected (if it's a BT dock)

#### Why aren't I getting any cell data for the Cell Near state ?

A user reports being able to fix this issue as follows:

I was able to fix this issue by going into the EPST menues using
##DATA# on the keypad and changing the EVDO Preferred mode from HDR to
Automatic.

It's possible that you will only be able to receive, not make, phone
calls as another symptom of this problem.

#### Why isn't there a green light for the On/Off radio button on the main screen ?

A user discovered that this happens when the DPI value of the Android build is set to
particulart values (e.g. 200,240 is OK, 220 the light disappears).

#### Why does the action Display Brightness cause my keyboard or application to close ?

Normally Android does not effect changes to brightness immediately, so Tasker has to
use a trick to make it happen. That trick can sometimes have the side effect that
e.g. some dialogs like the soft keyboard may close.

To avoid that, you can deselect the Immediate Effect checkbox in the Display Brightness action.

#### Why is the date in Tasker's notification list completely wrong ?

This occurs if you select a transparent Notification Icon at Menu / Prefs / Monitor,
but don't specify a Custom Notification Layout.

Changing to a non-transparent icon or a custom layout will fix the problem.

#### Why won't Tasker install on my custom ROM ?

The most likely reason is that you don't have Google Maps installed on the device. With
several custom ROMs that comes as a separate package.

#### Why doesn't my Perform Task action work when I Test it ?

When task (a) runs a Perform Task action to start task (b), the order in which the two tasks are executed depends on their relative priorities.

A feature of the Test button is that the tested task (a) runs at extremely high priority
to ensure that the task runs even if other tasks are running in the background.

So testing Perform Task with the Test button will only work as expected if in actual usage task (a) will always have higher priority than task (b) or the Perform Task action has Stop specified.

#### Why doesn't my App Context work ?

First, we need to find out which method Tasker is using to detect app changes on your device.

Disable Menu / Prefs / UI / Beginner Mode then look in
Menu / Prefs / Monitor to see if you have an entry App Check Method.
If you don't have such an entry, Tasker is using its Accessibility Service.

If Tasker is using Usage Stats for app detection, you need to ask Android to give Tasker
permission to do that, see Menu / More / Android Settings / App Usage Stats.
Otherwise, you need to make sure Tasker's Accessibility Service is enabled in Android Settings,
see Menu / More / Android Settings / Accessibility service.

Further tips:

- if Tasker offers you the choice to use different methods, try the other methods. Remember to give Tasker permission in Android settings for the new method (see above).

- If you are using Nova Launcher, set Settings / App & Widget Drawer / Advanced / Automatically Close to off.

- Some apps (very few) aren't detected by Tasker, usually due to their internal structure.

- Some custom Android ROMs also have special configurations which prevent Tasker's app detection working.

For the latter problem, there are a few things you can try:

- look for special settings in your ROM that relate to 'keeping the launcher in memory'. They should be disabled.

- change the build properties file. Look in /system/build.prop (or possibly /system/local.prop or /data/local.prop) for a line like:

ro.HOME_APP_ADJ=-17

Change it in a terminal program to look like this:

ro.HOME_APP_ADJ=1

If you didn't find an existing line, just add the new line as above.

Note: you will first need to make /system writeable. You can
do that e.g. with Tasker's Remount action. Remember to make it
not-writeable again after making the change.

- try detecting apps with a state using the %WIN (window title) variable; create a new state Variable Value, %WIN, Matches, TITLEwhere TITLE is the title of the window of the app you are interested in. For this solution to work, you also need to enable Tasker's Accessibility Service in Android Settings.

You can check what %WIN shows for the app you are interested in with this profile:

Event: Variable Set, %WIN

Alert / Flash, Win is now %WIN

#### Why doesn't the Keyguard action work properly ?

Android does not officially support toggling of the Keyguard by an app. The Keyguard
action was introduced in an early version of Tasker when a reliable workaround was
possible.

In more recent Android versions, the workaround is no longer so reliable due to
internal changes made within Android. If Keyguard works at all, there may be
disturbing side-effects.

The Keyguard action will likely be most reliablewhen the display is on and and the
Keyguard is already unlocked.

Some people have more luck with the same functionality provided by the
Secure Settings plugin [Secure Settings plugin](https://play.google.com/store/apps/details?id=com.intangibleobject.securesettings.plugin) . After install, you can find the
Secure Settings plugin in the Plugin action category. Note that a rooted
device is not needed to use this part of Secure Settings.

#### Why doesn't Tasker think my device is rooted ?

Tasker requires two things before root functionality is enabled:

- the su program must be in your path

- one of the following must be found:

- a superuser package

- the word modversion somewhere in the file /system/build.prop

If root is not being detected on your device but you are sure that root can be used by Tasker, you can therefore probably fix that by adding a line like:

# modversion this line enables Tasker root support

to the top of the file /system/build.prop.

#### Why doesn't Tasker show my Local Media images anymore ?

When you select a Local Media image, Android grants Tasker rights to keep using
it.

However, when you uninstall Tasker, Android forgets those rights and doesn't
reassign them when you install Tasker again. This is clearly a failing in
Android...  On some devices Android also forgets the rights when the device is rebooted, but this is very rare and almost certainly a problem with the particular device
involved.

To fix the problem, you wil unfortunately need to reselect the Local Media images
in the Tasker UI so that Android grants it access rights again.



---

## Tasker for Android



body {
color: #FFF3E0
}

.change_title {
font-size: 110%;
font-weight: bold;
}

.video_demo {
font-size: 105%;
font-weight: bold;
}

Tasker

Home [Home](/index.html)

Direct Purchase [Direct Purchase](https://taskernet.com/?licenses)

Download [Download](/download.html)

TaskerNet [TaskerNet](/taskernet.html)

Home Automation [Home Automation](/home_automation.html)

Usage Examples [Usage Examples](exampleuses.html)

Pre-made Projects [Pre-made Projects](https://forum.joaoapps.com/index.php?resources/)

FAQs [FAQs](/faq.html)

Guides [Guides](/guides.html)

Reviews [Reviews](/reviews.html)

Wiki [Wiki](/wiki)

Plugin List [Plugin List](/pluginlist.html)

Forum

Forum/Support [Forum/Support](https://www.reddit.com/r/tasker/)

Legacy Forum [Legacy Forum](https://tasker.joaoapps.com/forum)

Userguide (5.0+)

Index:
en [en](/userguide/en/index.html)
es [es]( /userguide/es/index.html)
fr [fr](/userguide/fr/index.html)
zh [zh]( /userguide/zh/index.html)

1 Page:
en [en](/userguide_summary.html)

More

Join [Join](/join.html)

AutoApps [AutoApps](https://joaoapps.com/)

Developers [Developers](/developers.html)

History [History](/history.html)

Privacy Policy [Privacy Policy](/privacy.html)

Release Notes [Release Notes](/changes.html)

Next Version [Next Version](/changes/nextversion.html)

Feature Requests [Feature Requests](https://tasker.helprace.com/s1-general/ideas/new)

Report Issues [Report Issues](https://tasker.helprace.com/s1-general/problems/top)

Patreon [Patreon](/patreon.html)

##
FAQ: Why... ?

- Why am I an idiot if I use a pirated copy of Tasker ? [Why am I an idiot if I use a pirated copy of Tasker ?](#f)

- Why is GPS often scanning when I unlock my device ? [Why is GPS often scanning when I unlock my device ?](#a)

- Why does Tasker need so many permissions ? [Why does Tasker need so many permissions ?](#b)

- Why does Tasker need the INTERNET permission ? [Why does Tasker need the INTERNET permission ?](#c)

- Why isn't Tasker shown in the Application Context list ? [Why isn't Tasker shown in the Application Context list ?](#d)

- Why does Tasker have it's own music player and controls for the system music player ? [Why does Tasker have it's own music player and controls for the system music player ?](#e)

- Why does a Cell Near context not become inactive when I turn on Airplane Mode ? [Why does a Cell Near context not become inactive when I turn on Airplane Mode ?](#g)

- Why can't I use a downloaded icon for my shortcut task / Notify action ? [Why can't I use a downloaded icon for my shortcut task / Notify action ?](#h)

- Why does my profile have 2 enter tasks ? Why can't I add an exit task ? [Why does my profile have 2 enter tasks ? Why can't I add an exit task ?](#i)

#### Why am I an idiot if I use a pirated copy of Tasker ?

The hacker can do virtually anything with your phone. Record your
calls and upload them to a website, SMS your location and all your
contacts, make calls automatically, wipe your SD card, secretely
record from your microphone any time etc etc

#### Why is GPS often scanning when I unlock my device ?

When the device wakes up, Tasker switches from a low-frequency GPS check schedule to a
higher-frequency one. Android's GPS software always does an immediate scan when
switching the check frequency.

It's not because Tasker is constantly scanning while the device is off

You can change the frequency in Menu / Prefs / Monitor.

#### Why does Tasker need so many permissions ?

Because it can do so much!

Unfortunately, Android requires that an app specify it's permissions even if they are
never used, which means that permissions for all of the things which the user could
potentially ask Tasker to do need to be specified.

If you are still concerned, consider that Tasker has over 25,000 downloads at the time of writing and any abuse taking place would quickly be discovered.

#### Why does Tasker need the INTERNET permission ?

The INTERNET permission is used solely for:

- google maps downloading map data, only for setting up a Location context

- to carry out HTTP Post/Get actions and other actions that require an Internet connection by their nature

- to verify the order number, and only until it has been successfully verified

- to check whether a new Tasker version is available, if configured in Preferences

Tasker never directly uses Internet access for anything else.

#### Why isn't Tasker shown in the Application Context list ?

Because it's easy to get into trouble firing tasks in Tasker. For example, if
a profile is setup with a Tasker Application Context and a task with Load App Calculator,
it will not be possible to enter Tasker anymore.

#### Why does Tasker have it's own music player and controls for the system music player ?

- the system music player is not guaranteed to be present or the same on all systems.

- finer control can be exercised over the Tasker player e.g. starting the track
from a preset seek point

- Tasker's player is more discrete, there is no notification bar icon.

- by having two players available you can do things like alternating audio from different
music sources or even playing simiultaneously.

#### Why does a Cell Near context not become inactive when I turn on Airplane Mode ?

Cell Near is sticky. That means that once active it stays active until a non-matching
Cell ID is seen. In Airplane Mode no Cell IDs are seen and so the context stays active.

Many people use Airplane Mode at night e.g. to save battery. If you also have a Cell Near
profile that detects when you are home, it would become inactive at night if Cell Near wasn't
sticky.

A couple of points:

- the Cell radio isn't being turned on by Tasker in Airplane Mode.

- if you want a profile to become inactive for Airplane Mode, just add an Inverted
state Airplane Mode to it.

#### Why can't I use a downloaded icon for my shortcut task / Notify action ?

Some things just weren't meant to be (i.e. Android doesn't allow it).

To solve the shortcut problem, you can always use a widget though.

For notifications:

- if you would like this to be possible one day, please star this
Android feature request [Android feature request](http://code.google.com/p/android/issues/detail?id=12302)

- it would be technically possible to create 'icon pack' APKs and that might happen one day

#### Why does my profile have 2 enter tasks ? Why can't I add an exit task ?

That's because it's an instant [instant](faq-other.html#instant)  profile.

As a convenience, the Exit task with such profiles is replaced by an extra Enter task in case
you have a lot to do with that profile.

Note that the tasks you specify execute in the order they are specified, their actions
do not alternate.



---

