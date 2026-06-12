# Tasker Reference: Tasks

This file provides detailed documentation on Tasker Tasks concepts, options, and workflows.

## Table of Contents

- [Tasker: Tasks](#tasker-tasks)
- [Tasker: Task Edit](#tasker-task-edit)
- [Tasker: Action Edit](#tasker-action-edit)
- [Tasker: Flow Control](#tasker-flow-control)
- [Tasker: Main Screen](#tasker-main-screen)
- [Tasker: Run Log](#tasker-run-log)
- [Tasker: Settings](#tasker-settings)
- [Tasker: Task / Shortcut Widgets](#tasker-task--shortcut-widgets)
- [Tasker: Widget Configure](#tasker-widget-configure)
- [Ah Adb Setup](#ah-adb-setup)
- [Ah Convert Variable](#ah-convert-variable)
- [Ah Decrypt File](#ah-decrypt-file)
- [Ah Delete File](#ah-delete-file)
- [Ah Encrypt File](#ah-encrypt-file)
- [Ah Get Fix](#ah-get-fix)
- [Ah Load Image](#ah-load-image)
- [Ah Menu](#ah-menu)
- [Ah Mobile Data Direct](#ah-mobile-data-direct)
- [Ah Run Task](#ah-run-task)
- [Ah Save Image](#ah-save-image)
- [Ah Scan Card](#ah-scan-card)
- [Ah Scene Element Add Geomarker](#ah-scene-element-add-geomarker)
- [Ah Scene Element Background Colour](#ah-scene-element-background-colour)
- [Ah Scene Element Border](#ah-scene-element-border)
- [Ah Scene Element Delete Geomarker](#ah-scene-element-delete-geomarker)
- [Ah Scene Element Depth](#ah-scene-element-depth)
- [Ah Scene Element Focus](#ah-scene-element-focus)
- [Ah Scene Element Image](#ah-scene-element-image)
- [Ah Scene Element Map Control](#ah-scene-element-map-control)
- [Ah Scene Element Position](#ah-scene-element-position)
- [Ah Scene Element Size](#ah-scene-element-size)
- [Ah Scene Element Test](#ah-scene-element-test)
- [Ah Scene Element Text](#ah-scene-element-text)
- [Ah Scene Element Text Colour](#ah-scene-element-text-colour)
- [Ah Scene Element Value](#ah-scene-element-value)
- [Ah Scene Element Video Control](#ah-scene-element-video-control)
- [Ah Scene Element Visibility](#ah-scene-element-visibility)
- [Ah Scene Element Web Control](#ah-scene-element-web-control)
- [Ah Secure Setting Grant](#ah-secure-setting-grant)
- [Ah Send Intent](#ah-send-intent)
- [Ah Send Sms](#ah-send-sms)
- [Actions | Variable Set](#actions-|-variable-set)
- [Ah Take Photo](#ah-take-photo)
- [Ah Test Tasker](#ah-test-tasker)
- [Ah Tether Usb](#ah-tether-usb)
- [Ah Tether Wifi](#ah-tether-wifi)
- [Ah Timer Widget Control](#ah-timer-widget-control)
- [Ah Timer Widget Set](#ah-timer-widget-set)
- [Tasker Help Files](#tasker-help-files)
- [Eh Timer Change](#eh-timer-change)

---

## Tasker: Tasks



##
Tasks

A task is simply a set of actions which are performed one after the other.

#### Named / Anonymous Tasks

A task can be given a name. This allows:

- the same task to be used in more than one profile

- easier identification of what the task does

- in the case of a task widget/shortcut task widget/shortcut ,
it provides a label	for the icon on the home screen.

When creating a profile, widget or shortcut,
often the associated task will consist only of one or two actions which will not
be reused. For this case, Tasker allows you to create a task without a name
(an Anonymous task).

#### Task Visibility

Anonymous tasks are only visible when editing the profile that they are associated
with.

Named tasks are visible on any screen that allows task editing.
Any changes made to the set of tasks in any screen is reflected in all the other
screens.

#### Task Icon

Each task has an associated icon, by default a question mark. The icon is used

- to represent the task on the home screen when it is used as a
widget or shortcut widget or shortcut

- when the task is turned into and app [turned into and app](appcreation.html)

- for easier identification of the task within the Tasker UI

#### Deleting Tasks

Named tasks can only be deleted via the Delete button on the
Task Edit [Task Edit](activity_taskedit.html)  screen. Unnamed tasks
are deleted automatically when the profile they are part of is deleted,
or a named task is selected for that profile.

Named tasks cannot be deleted while a profile still refers to them.

When a task is deleted that is referred to by a previously created named
widget or task, the widget will stop working.

Android does not allow Tasker to automatically remove the widget from the
Home Screen.

#### Task Scheduling

When there is a single task waiting to be executed, it's actions are executed one-by-one
until finished.

When there are several tasks in the queue at once, it's important to understand
how they are handled:

- only one action from the same action group [action group](#actiongroups)  can be executed at once to
prevent interference

- the task in the queue with the highest priority goes first and blocks lower priority tasks

- tasks with the same priority take turns executing an action
each, starting with the most recent addition to the queue unless one task is a child of the
other (started via Perform Task [Perform Task](help/ah_run_task.html) ), in which case the child executes first.

Task priority, 0 to 50 inclusive with 0 being lowest, is determined according to whatever causes the task to run.

- enter tasks run by profiles have the priority specified in Profile Properties, the default is 5.

- exit tasks run by profiles have the priority specified in Profile Properties plus 1001, the default is therefore 1016

- tasks run by widgets or shortcuts can be set in Task Properties when the widget/shortcut is created, the default is 7

- tasks run from scene elements have priority one more than the task which showed the scene

- tasks run from the Test button in the task edit screen have priority 100 by default, long-click the play buttin to choose a different one.

A couple of guidelines are:

- if you want a particular task to always interrupt other tasks that may be
executing, give it a high priority

- if you have a task that lasts for a while,
you probably want to give it a low priority so it doesn't block other tasks
from being executed.

#### Action Groups

Actions are divided into groups for scheduling based on how long the action takes to execute and what it
interferes with:

- Speech: Say, Say To File

- Javascript: Javascript

- Fix: Get Location

- Voice: Get Voice

- Proxy: Display Brightness, Query Action, Photo, Photo Series, Photo Series Time

- Proxy Scene Enter Key, Menu, Popup, Popup Task Buttons, Variable Query

- Other Scenes: the name of the scene being shown

- Normal: all other actions

#### Wait Actions

Wait and Wait Until are special cases. The rules for handling them are complicated
and try to do the 'best thing' dependent on the situation.

#### Same-Profile Tasks

Tasks launched by the same profile by default always execute in the order in which they are launched. Other tasks from the same profile remain completely inactive until any previous task from the same profile is complete. The main purpose of this rule is to correctly handle rapid changes in a profile's activation state.

This behaviour can be disabled by deselecting Enforce Task Order in the Profile Properties dialog.

Example

This example demonstrates the effect of Enforce Task Order and shows also how sub-tasks launched by
Perform Task [Perform Task](help/ah_run_task.html)  are handled.

Profile: Example
Enter Task: Enter1
Perform Task, Enter2
Exit Task: Exit1
Perform Task, Exit2

With Enforce Task Order:

Enter1 and Enter2 are both guaranteed to finish before either of Exit1 or Exit2. Whether Enter1 or
Enter2 finishes first depends on their relative priority. Same for Exit1 and Exit2.
All 4 tasks compete based on priority against tasks from other profiles. Exit tasks have a higher base
priority so will finish before Enter tasks.

Without Enforce Task Order:

If the profile goes active and inactive quickly, Enter1, Enter2, Exit1 and Exit2 will all compete
purely on priority. Since Exit tasks have higher base priority, Exit1 and Exit2 will probably finish first.

#### Collisions

Sometimes a task needs to be executed of which a copy is already executing.
This can happen quite often e.g. when a task widget button is pressed twice quickly,
or a task contains a Wait action or shows a dialog.

The way in which a collision is resolved is specified by the user. There are
3 options:

- the new task is ignored (the default)

- the existing task is aborted and the new one starts from its first action.
The current action of the previous task is finished if it is already being carried out.

- both tasks run simultaneously

Note that the last option can lead to several copies of a task all running at once.

#### Behaviour When Device Off

By default, after a few seconds of the screen being off Android will power down the device and thus running
tasks will be paused.

In the Task Properties dialog, it can be specified that a task should keep running.

Dialogs

An action that shows some kind of dialog (such as a lock screen, popup, menu)
blocks execution of any other action, even one of higher priority, until it is completed.

Wait / Wait Until

These are exceptions. A wait action can be interrupted by another task's action and
will resume (if necessary) when the other task's action is finished.

#### Killing Tasks

If you have a problem with a task that never ends, you can manually end tasks
with the Kill button in the Task Edit screen.



---

## Tasker: Task Edit



##
Task Edit

This dialog allows editing of the actions in a task, and various properties
of the task.

#### Action List

The main part of the screen is a list of the actions contained in the currently
selected task.

- Click on an action to edit it

- Long-click on an action to enter multi-select mode and for options

- Click-and-drag at the right hand side of the action to move it around e.g. to the trash bin

If a particular action is a setting [setting](settings.html) , that will be indicated on
the right-hand side of the action.

Condition and Block Colours

If an action has had a condition set for it, the condition is shown with
a red or green bar next to it; green indicates that the condition is currently met (the action will execute), red indicates the opposite. Of course, when the task is executed it could be that it changes things so that the condition is then met.

If an action is within an If / End If block it is displayed
indented with a red or green margin. The colours have the same significance
as for individual action conditions described above.

If an action is within a For loop [For loop](flowcontrol.html#for)  it
is displayed indented with a grey margin. If the For
action has a condition on it which is not met, the margin will be red
(because the actions in the loop will never execute, like an If / End If block).

#### Task Control Row

Directly underneath the action list is a row of buttons with icons.

Play/Step Buttons

Run the task.

The Play button will run the task right through till the end, the Step
button will run a single task each time it's pressed.

During tasting, the current action is shown with an arrow and
the next task with a faded arrow.

The success of each action is shown when it finishes with a
green (action OK) or red (action failed) circle.

Tasks run via the Play or Step button have priority 10.

Long-click the Play or Test button to manually set the priority
of the task when it runs
during the test.  Please be aware that
setting a lower priority can result in interference from other tasks running
which are e.g. triggered by profiles.

Tip: pressing the Step button while a task is playing will cause
the task to switch to stepping mode when the current action finishes.

Add Action Button

Add an action to the end of the task. When in multi-select mode, adds an action
after the current selected item, if only one item is selected.

Task Properties

Show extended properties for the task. Not visible in Beginner Mode [Beginner Mode](beginner.html) .

Task Icon

Shows the icon associated with the task. Clicking on it allows changing of the icon.

#### Menu Items

Action Labels

Toggle display of action labels (which are specified in the Action Edit [Action Edit](activity_actionedit.html)  screen).

Param Names

Toggle display of the name of each action parameter.

Icons

Toggle display of the setting/action indicator icon for each action.



---

## Tasker: Action Edit



##
Action Edit

This screen allows configuration of a single action in a Task.

#### General

At top left is the name of the action. Tapping on this allows it
to be changed.

Bottom-right is a help button. Please be sure to read the action help
of every action before you use it for the first time, there may be e.g. device specific restrictions you should know about.

#### Action Parameters

A parameter gives extra detail about how the action is to be carried out.

Text Parameters

- are sometimes optional: in that case the text Optional
will appear as a hint unless the entry box has already been filled in

- sometimes have a dialog to help you fill in a value
which you can access by clicking the magnifying glass icon next to them

- can have variables [variables](variables.html)  automatically inserted by clicking the tag
icon next to them.

Numeric Slider Parameters

Clicking the arrows icon next to numeric sliders allows you to specify the
number textually or use a variable [variable](variables.html)  for the parameter instead, if the value
will not be known until the action is actually executed.

If (Condition) Parameter

(most actions)

Allows specification of one or more conditions which must match if this action is to execute.

Single conditions consist of a left-hand side  (usually a variable name), an operator and a right-hand-side for example
%number, Equals, 1 indicates that the action will be executed
if the variable %number has the value 1.

When more than one condition is specified, they must be combined via And (all conditions
must be true), Or (at least one condition must be true) or Xor (exactly one must be true). These 'combiners' are called boolean operators.

Usually, 2 or 3 conditions will be combined with all Ands or all Ors, but in order to allow more complicated logic, Tasker also offers And and Or in high-precedence versions.
Of the 4 boolean operators which are available, the selection goes from low to high precedence ones.

The higher the precedence of a boolean operator, the further to the right it is shown. This enables the
logical groups to be visualised.

Examples:

True | False & True | False is the same as ( True | False ) & ( True | False )
so is True.

True & False | True & False is the same as True & ( False |  True ) & False
so is False.

True & False | True |+ False is the same as True & ( False | ( True | False ) )
so is True.

Note that the order of the conditions can mean that some conditions are never evaluated. For instance, when two conditions
are present and the one above an And is false then the condition below it will never be evaluated.
This can be advantageous if the second condition takes relatively more resources e.g. involves matching against
a lot of text.

Please see the section on Flow Control [Flow Control](flowcontrol.html)  for more information.

Continue Task After Error Parameter

(selected actions only)

By default, if an action fails with an error (e.g. the user specified to delete a file that doesn't exist)
Tasker will stop the task immediately and the remaining actions will never be executed.

This parameter specifies that the task should continue even if this action fails.

In addition, if it's checked, errors will be logged in the system log as diagnostics instead of errors
and error popups will be surpressed.

Label Parameter

(all actions)

A label for the action which is shown on the Task Edit screen. This parameter
could also be used to add comments to actions to help understand
how the task works.

Labels are also used with Goto actions to jump from one part of
the task to another.

#### Menu Options

Search

Search for and jump to a specified action. The entered term is searched against action
properties in the following order:

- the action number

- the action label if present

- the action name

- the action description, including the action parameter contents

The matching is case-insensitive. Searching starts from the current action and
wraps around. Only the header action (
- If or For) of closed
blocks is searched.



---

## Tasker: Flow Control



##
Flow Control

#### Overview

Task flow control is based on the following Tasker elements:

- variable [variable](variables.html)  values

- conditions [conditions](#condition)  on individual actions

- If / Else / Endif actions for conditional grouping of following actions

- For / End For to do a set of actions once for each of a set of elements

- Goto action (jumping around within a task).

- Perform Task action (calling other tasks as subroutines)

- Stop action (terminate task immediately)

On the Wiki there is a detailed example of
processing a file's content [processing a file's content](http://tasker.wikidot.com/fileproc)  [External Link].

Tip: if you accidentally create a task that never ends when experimenting
with loops, use the Kill button in the Task Edit screen to end it
manually.

Conditions

Every action can have a condition associated with
it (specify this in the Action Edit screen). If the condition does not match,
the action will be skipped.

A condition consists of an operator ('equals' etc) and two parameters.
The possible operators are:

- Equals (eq)

The left parameter is identical to the right parameter.

- Doesn't Equal (neq)

The left parameter is not identical to the right parameter.

- Matches (~)

The right parameter is a pattern which the left parameter is matched against [matched against](matching.html) .

- Not Matches (!~)

As above, but the match must fail for the action to be executed.

- Matches Regex (~R)

The right parameter is a regular expression which the left parameter is matched against [matched against](matching.html#regex) .

- Doesn't Match Regex (!~R)

As above, but the match must fail for the action to be executed.

- Maths: Less Than (<)

Both parameters (after variables are substitued) must be numbers or mathematical expressions and the first must be less than the second
e.g. 3 < 6. See Maths [Maths](maths.html)  for more info.

- Maths: Greater Than (>)

As above, but the first parameter must evaluate to more than the second.

- Maths: Equals (=)

As above, but the two parameters must be numerically equal.

- Maths: Isn't Equal To (!=)

As above, but the two parameters must be not numerically equal.

- Maths: Is Even (Even)

The left parameter is an even number.

- Maths: Is Odd (Odd)

The left parameter is an odd number.

- Is/Isn't Set (Set/!Set)

Whether the specified variable has a value or not.

Expressions which are not mathematically valid  e.g. I Am The Walrus > 5 give a warning and evaluate to false
when used with a mathematical operator.

#### Foreach Loop

Goal: perform a set of actions for each of apple, pear and banana.

1. For
%item
apple,pear,banana
Loop once for each of apple, pear and banana

2.   Action One

Example: Flash %item

3.   Action Two

...

4. End For

Return to action 1 if we havn't done all the items yet

Result: Action One and Action Two are performed three times. The first time, the variable %item is set to apple, the second time pear and the last time banana.

You can insert a Goto action in the loop with either Top of Loop (meaning continue, skip to the next item straight away) or End of Loop (meaning break, stop without doing any more items) specified.

In adition to simple text, the For action accepts any comma-separated combination of these Items:

- a numeric range e.g. 1:5 (= 1,2,3,4,5)

- a numeric range with a jump e.g. 8:2:-2 (= 8,6,4,2)

- a numeric range defined by variable values e.g. 2:%end:%skip, 1:%arr(#)

- a variable name (which is replaced) e.g. %fruit (= banana maybe)

- a variable array [variable array](variables.html#arrays)  part e.g. %arr(1:2) (= %arr1, %arr2 = apple,banana maybe)

A common case is to use %arr(), which performs a loop for each element in the array %arr.

Warning: the Values parameter in the loop is reevaluated with each iteration of the loop, meaning
that modifying array variables which appear there from within the loop can have unexpected effects. To workaround that,
it can be best to use the following sequence:
Variables Set, %values, %arrayWhichWillChange()
Variable Split, %values
For, %value, %values()
...

#### For Loop

Goal: perform a set of actions for each of a set of elements in turn.

Use the Foreach Loop as described above, with the Items parameter being a range specification e.g. 4:0, 100, 0:8:2 (= 4,3,2,1,0,100,0,2,4,6,8).

#### Until Loop

Goal: perform a Task X until some condition is met (at least once)

1. Action One

...

2. Action Two

...

3. Goto
1

If %qtime < 20
Return to action 1 if runtime < 20

Result: Action One and Action Two are performed until %QTIME contains the value 20 or more
i.e. until the task has been running for 20 seconds.

Note: %QTIME is a builtin local variable available in all tasks.

#### While Loop

Goal: perform a Task X while some condition is met.

1. Stop

If %fruit Not Matches Apple
Stop task if it's not crunchy, otherwise
go to next action

2. Action One

...

3. Action Two

...

4. Goto
1
Go back and see if we're still crunchy

Result: Action One and Action Two are performed while %fruit contains the value Apple.

#### Counter Loop

Goal: perform a Task X a set number of times.

1.
Variable Set
%count, 0
Initialize the counter

2. Action One
Label: LoopStart
...

3. Action Two

...

4. Variable Add
%count, 1
Add one to %count

5. Goto
LoopStart

If %count < 10
Return to action 2 if count < 10

Result: after initialization of %count to 0, the task loops around the actions
from 2-5 until
%count reaches 10, at which point the condition on the Goto fails
and the end of the task is reached.

Note that we used a Goto to a labelled action this time. In
all but the very simplest tasks it's better to use a label rather than a number. It's easier to work out what's happening and if you insert or delete actions before the loop starts, the Goto will still jump to the right place.

An alternative way to do this loop is to use a For action specified as 0:10.

#### If / Then / Else Condition

Goal: perform certain Tasks if conditions are met, otherwise perform a
different task.

1.
If

%fruit ~ Apple
~ is short for 'matches'

2.   Action One
...

3.   Action Two

...

4.
Else If

%fruit ~ Pear
an Else action with a condition

5.   Action Three
...

6.
Else

7.   Action Four

...

Result:  actions One and Two are executed if %fruit matches Apple, Action Three is executed if %fruit matches Pear, otherwise Action Four is executed.

Notes:

- you can have as many Else Ifs in a condition as you like

- if your condition is in the middle of a more complicated task, you need to tell Tasker where the condition ends with an End If action

#### Subroutines

To call another task, use the Perform Task action. To use it as
a subroutine, you just need to ensure that the priority of the calling
task is less than the priority of the called task (more info:
scheduling [scheduling](tasks.html#scheduling) ).

The parent can optionally pass values to the child and receive a result back:

Parent Task

1.   Perform Task

Child,

Priority, 10

%par1,  5,

Result Value Variable, %result

pass 5 to the child, expect a result in %result

2.   Variable Flash
Result: %result

what did we get back ?

Child Task

1.   Variable Set

%newval, %par1 + 1, Do Maths

add one to the value that was passed

1.   Return

%newval

set %result in the parent to the value of %newval in the child

Result: the parent flashes 6

Notes:

- changes made to %par1 and %par2 in the child task are not reflected by their changing in the parent task

- receiving a return value is optional for the parent, even if the child tries to give it one

- unlike Return statements in most computer languages, Tasker's does not necessarily stop the child task, so if the child and parent have the same priority they can both run together and the child return several results over time.



---

## Tasker: Main Screen



##
Main Screen

This is the first screen shown when you startup Tasker. It allows you
to organize and configure Tasker's four main 'building blocks':
Profiles, Tasks, Scenes and Variables.

- Main Tabs

- Profiles [Profiles](#profiles)

- Tasks [Tasks](#tasks)

- Scenes [Scenes](#scenes)

- Variables [Variables](#variables)

- Action Bar [Action Bar](#action)

- Menus [Menus](#menus)

- Projects [Projects](#projects)

### Main Tabs

Displayed in the action bar on most devices.

- Click on a tab to view a list of the relevant things

- Click on an already selected tab to get options for it

#### Profiles

Each item in the list represents a profile. The profile links contexts (conditions) on
the left to tasks which should be run on the right. The profile name is green if
the profile is active. There are three main parts to each profile.

1. Title Bar

This shows the profile name (or description if it has no name) and a
switch on the right shows whether the profile is enabled or not.

- Click on the name to expand / collapse the profile. When expanded, the contexts and tasks (described below), are visible.

- Long-click on the profile name to get profile options or to drag  profile(s) around

- Click on the switch to control whether the profile is enabled or not.

Important: the switch being set to on does not mean the profile is active
(will run its tasks), it means that the profile can become active
if its conditions are met.

2. Contexts

On the left hand side of the profile are an icon and text for each context in the
profile. The contexts dictate when the profile should become active. When all contexts
are active then the profile will be active.

- Click on the context to edit it

- Long-click to show management options, such as editing or adding a new context

You can configure what clicks and long-clicks on contexts do in Menu / Prefs / UI.

3. Tasks

On the right hand side of the profile are one or two tasks to
carry out based on its activation status.

- Click on the task to edit it

- Long-click to show management options.

A task indicated with a green, right-pointing arrow is an
entry task, executed when the profile first becomes active.

A task indicated with a red, left-pointing arrow is an
exit task, executed when the profile becomes inactive again.

Exception: a profile containing an event context or a repeating
or non-ranged time context has two green
arrows, to denote that both tasks are executed immediately because
the profile activation and deactivation is instantaneous.

Click on the Profiles tab when it is already selected for
general profile-related options such as sorting.

#### Tasks

The task list shows the named tasks [tasks](tasks.html)  which have been created.

- Click on a task to edit it

- Long-click for options or to drag task(s) around

Note that a profile can be assigned an anonymous task (one without
a name) which is not accessible in the task list, only via the
relevent profile in the profile list.

Click on the Tasks tab when it is already selected for
general task-related options such as sorting.

#### Scenes

The scene list shows the scenes [scenes](scenes.html)  which have been created.

- Click on a scene to edit it

- Long-click for options or to drag scene(s) around

Scenes with a green name have been created but may be invisible (hidden).

Click on the Scenes tab when it is already selected for
general scene-related options such as sorting.

#### Variables

The Variables tab is not shown if Beginner Mode [Beginner Mode](beginner.html)  is enabled.

By default, all global user-variables [user-variables](variables.html)  that Tasker knows about are listed, which includes any that have a value set or are mentioned somewhere in a profile, task or scene.

- Click on a variable to edit it

- Long-click for options

Note that variables whose names are all lower-case are local variables and not shown because they are only valid within the task that refers to them.

Click on the Vars tab when it is already selected for
general variable-related options such as sorting and filtering.

The filter controls function as follows:

- Indexed (button)
includes variables whose names end in a number e.g. %LOC3, otherwise they are excluded.

- Empty (button)
includes variables which have currently have no value assigned, deselect to show only variables that have a value.

- Referenced (button,home project only)
includes variables which are referenced in profiles, tasks or scenes.
Deselect to show only 'orphan' variables.

- Filter (textbox)
excludes variables which don't contain the specified text somewhere in their name (case-sensitive)

In a user-created project, only variables referenced by that project are shown.

Unlike most screens in Tasker, changes made in the variable list cannot be cancelled.

#### Action Bar

Apply Button

Save and apply any changes which have been made without
exiting the UI.

This is unnecessary prior to leaving the UI via
the back button or home key, it's just for convenience
when testing changes.

Not visible in Beginner Mode [Beginner Mode](beginner.html) .

Overflow Button

Click to access menu options if no menu hard-key is available on the device.

### Menus

#### Menu Item: Browse Examples

Links to websites with projects, profiles etc offering solutions for common
problems.  Important: once downloaded you need to import the file into
your active user data. For example, profiles are imported by long-clicking
the profile tab and selecting Import.

#### Menu Items: Data

Clear

Removes all data that has been created to that point. Does
not remove preferences (use Menu / Preferences and click Defaults for
that) or variables (long-click on the Variables tab for that).

Backup

Saves the existing user data to a backup file on external storage.

Restore

Options for restoring backups of various types.

### Projects

Tasker allows organisation of profiles, tasks, scenes and variables
into groups called Projects, each with a separate Project Tab.

The projects tabs are hidden in Beginner Mode [Beginner Mode](beginner.html) .

- Click on a project tab to switch to viewing only
things in that project

- Long-click  on a project tab for options, including
adding a new tab. Options can also be accessed by a single click on the
selected project tab.

- Long-click and Select, then drag to a project tab, any items you
want to move to that project

The first tab has a slightly special status, it cannot be removed
and anything which is not a member of another project is placed there.



---

## Tasker: Run Log



##
Run Log

The Run Log shows profile status changes and task/action execution to help when things aren't working as expected.
Log entries will only be recorded when the log is enabled by the switch in the top right.

Items are colour-coded according to what they refer to:

- purple: a task

- orange: a profile

- light blue: an action

- black/white: the monitor or execution service

Most items are long-clickable for options e.g. to view the corresponding item from the user configuration.

### Details Column

Displays the thing which the entry refers to. For example, MyTask.Wait refers to a Wait action in
the task MyTask.

Some notable details are:

- System refers to a task created by Tasker, usually to restore a setting [setting](settings.html)
when a profile deactivates.

- Anon refers to an anonymous task (has no name) which is the entry or exit task of
a profile.

- actions with a variable paramater show (after the action name) what the value of the variable was after the action has completed

### ID Column

Shows Tasker's internal ID for the thing which the entry refers to. This is most useful for actions e.g.
2.4 refers to the fourth action in the task with ID 2.

Some task or action ID entries may also have a number after a colon; since multiple copies
of a particular task can run at the same time, each task also receives
a unique execution ID to distinguish it from others with the same
data ID. The execution ID is shown with a colon e.g. a task with ID2:3 is the task with data ID 2 and execution ID 3.

Usually, the execution service will start up, run a task and then stop, so
most tasks have execution ID 1. The Run Log doesn't show the execution ID
in that case.

### Status Column

Describes the new status of whatever has changed which caused a log entry to be made. A status which is erronous (a problem occured) is displayed in red text.

Services

- Start
the service has started. Unexpected Start entries for the Monitor service are usually caused by Android killing the service because the Run In Foreground has been disabled in Tasker's Monitor preferences

- Stop
the service has stopped

- Restart
the service was restarted, usually because new data must be loaded due to the user changing the configuration.

Profiles

- Active
the profiles conditions were met so it became active

- Inactive
the profiles conditions were no longer all met, so became deactivated

- Instant
an instant profile [instant profile](faq-other.html#instant)  had a momentary activation

Tasks

- RejBad
task was rejected because it was malformed task e.g. had no actions

- RejCopy
task was rejected because it's a second copy of a task which has Abort New Task set for Collision Handling in its preferences

- RejMaxQ
the maximum number of queued tasks (determined in Action preferences) has been reached

- RejOff
Tasker was disabled at the time the task was submitted

- Running
the task has been entered in the run queue. Other tasks may still have their actions executed before this one (see Task Scheduling [Task Scheduling](tasks.html#scheduling) )

- ExitErr
the task has stopped after an error

- ExitOK
the task has finished all its actions and stopped

- ExitRep
the task has stopped because a second copy of it has arrived and Abort Existing Task s specified for its Collision Handling preferences

- ExitKill
the task has been stopped because the execution service is stopping

Actions

- Disabled
the action was disabled via the UI so was skipped

- Err
an error occurred while running the action, causing the task to stop

- ErrIgnore
an error occurred, but the task could continue (probably because Continue On Error was specified in the action parameters

- Exception
a totally unexpected error occurred (things like bugs in Tasker or Android), causing the action to fail and the task to stop

- OK: the action completed OK

### Pause/Play Indicator

The Pause/Play indicator shows whether the list of entries is updating. That's only the case when
the list is at the top i.e. the most recent chronological entries are showing.

### Filter Controls

Below the list of log entries are some filter controls.

Profiles, tasks and action entries are only
shown if the corresponding button is toggled on.

If a filter text is entered in the text box, entries
will only be displayed if they have text which matches the filter.

When an entry is excluded by the filter controls, it's shown as a small bar on the left side of the list.



---

## Tasker: Settings



##
Settings

#### What's A Setting ?

Settings are actions like Display Brightness and Ringer Volume
whose effects are reversed by Tasker when the profile(s) which applied them
are no longer active.

Setting actions have a double arrow icon next to them.

#### Single Profile

When a setting is applied by the profile's Enter Task, its value is restored
after the profile becomes inactive again. For example, if
the ringer volume is at 7 and is set to 0 in the Enter Task,
when the profile becomes inactive it is automatically set back to 7.

In other words, settings are only valid for the lifetime of their profiles.

#### Multiple Profiles

When multiple profiles that affect a setting are active simultaneously:

- the setting has the value from the most recently activated profile

- when all profiles are inactive, the setting has the value from before
any profile was active

#### Special Cases

- if a setting is changed by the Exit Task the profile will never save the setting's initial value.

- settings changed in an instant profile (one with an event context or repeating/non-ranged time context)  remain changed after the
event. The reasoning is that there is no point in changing the setting for the
half-second that the event lasts.

#### Notes

- settings are not actively maintained. If something else changes the setting
once the Enter task has run, it's not the case that this is detected and the
Enter task value automatically reapplied.

Complicated, huh ?



---

## Tasker: Task / Shortcut Widgets



##
Task / Shortcut Widgets

The standard way of running a Tasker task is by attaching it to a profile
which performs it when the profile becomes active. However, tasks can
be directly assigned to icons on the home screen called Widgets or
Shortcuts.

#### Standard Widgets / Shortcuts

These consist of an icon (the Task icon) with a label (the Task name)
underneath, and look identical to the normal application icons
in the home screen.

Clicking on the icon runs the associated Task.

#### Task Timer Widgets

This type consists of an icon and label, like the standard widgets,
but also has a countdown timer display which counts down Days, Hours,
Minutes and Seconds.

When the timer expires (reaches 0) the associated Task is run.

Tapping on the icon of the widget shows a configuration
screen where the timer can be configured.

Tapping on the timer section of the widget will pause,
restart or reset the timer, depending on its current state.

Note that the timer updates more rarely when it is still a long
way from expiry in order to minimize  power usage.

See Also:

- action Timer Widget Control [Timer Widget Control](help/ah_timer_widget_control.html)

- action Timer Widget Set [Timer Widget Set](help/ah_timer_widget_set.html)

- action Test Tasker [Test Tasker](help/ah_test_tasker.html)

- event Timer Change [Timer Change](help/eh_timer_change.html)

#### Creating a Widget / Shortcut

- Click and hold in an empty space on the Android home screen, until
a dialog appears.

- Select Widgets or Shortcuts

- Select Task or Task Timer (Widgets only)

- Pick an existing task or create a new one. When creating a new one, if
you do not expect to change the function of the widget/shortcut select
One-Time to avoid it cluttering your list of tasks.

- Use the Configuration Screen [Configuration Screen](activity_widget_configure.html)
to configure what should happen when the icon is clicked (or the timer
expires, in the case of a Task Timer widget). Take care to
select an appropriate name and icon for the task, as these will appear on
the home screen.

#### Changing a Widget / Shortcut

The function of widgets or shortcuts created from one-time tasks cannot be changed, it must be deleted and recreated.

On the other hand, if you associate a normal named task with a widget or shortcut then when the task is changed (via the Task Edit
screen) the function of the widget or shortcut also changes.

There are also some actions which will change the appearance of any widget:

- Tasker/Change Icon Set: changes the icon of a set of widgets to a different
style.

- Tasker/Set Widget Icon: changes the icon of a particular widget

- Tasker/Set Widget Label: changes the label of a particular widget

The latter two you could use to visually show the status of something e.g. WiFi.

#### Deleting a Widget / Shortcut

Click and hold on the icon in the Android home screen until the dustbin
icon appears. Drag the widget or shortcut icon to the dustbin icon and release.

#### Differences Between Widgets and Shortcuts

Advantages of Shortcuts

- they can be created in some places that widgets can't e.g. in home screen folders

- their layout probably better matches the default launcher layout

- long shortcut labels will scroll when selected in the default launcher

Advantages of Widgets

- their icon and label can be dynamically changed after creation
via the Set Widget Icon and Set Widget Label actions.

- timer widgets are possible

- they can be created without a label

So a shortcut should be used unless the extra configuration possibilities of a widget are necessary.

#### General

- you can create as many Tasker widgets and shortcuts as you like. You can even have several Timer widgets running at the same time.

- Timer Task widgets continue to update even when the screen is off.



---

## Tasker: Widget Configure



##
Widget / Shortcut Configuration

This screen allows selection and configuration of a task which will be performed when an
icon is clicked on the Android home screen or a timer elapses.

Please read about Task Widgets / Shortcuts [Task Widgets / Shortcuts](app_widgets.html)
before venturing further on this screen.

The layout of the Configuration screen is nearly identical to that of the
Task Edit [Task Edit](activity_taskedit.html)  screen.

When creating a Task Timer widget, you'll find a different button in
the bottom right which allows initialization of the timer. You can use this,
or wait till the widget is created and then click on the icon to configure the timer.



---

## Ah Adb Setup



#### ADB Setup

To use some features, Tasker needs to run someADB commands on your device through your PC

- Make sure that Tasker is installed on your Android device

- Enable Developer Mode: Go to Android Settings -> About Phone and look for the Build Number option. Touch it multiple times until developer mode is enabled.

- Enable USB Debugging: Go to Android Settings -> and look for the Developer Options option. In there, enable the USB debugging option.

- Install ADB on your PC: Check here [here](https://www.xda-developers.com/google-releases-separate-adb-and-fastboot-binary-downloads/)  for a quick way to do it.

- Connect device to PC: Connect your device to a PC and look on your phone. A prompt should show up asking you to allow your phone to be debugged by your PC. Accept this.

- Open the command prompt from the file folder that contains the extracted downloads. To do this, press the windows key and type cmd. When the prompt opens, type cd  followed by folder your downloaded ADB to.

- Grant permission: Open a command line a on your PC and write the needed commands (one at a time)

#### Notes:

- On MIUI devices you may have to open developer options and enable the USB debugging (Security Settings) setting (and the Disable permission Monitoring setting in some cases) to be able to run the above command.

- If you're having trouble with it saying that your device is not authorized, please check here [here](https://www.addictivetips.com/android/fix-adb-device-unauthorized-message-android/) .



---

## Ah Convert Variable



### Variable Convert

Convert the specified variable's value from one unit to another.

If a variable is specified for Store Result In, the new value is stored there and the original variable will not be changed.

If the conversion fails, no values will be unchanged.

Notes on particular conversions:

Date Time to Seconds
* date and time must be separated by whitespace e.g. 20110304 11.32
* date can be in YYYYMMDD format or xx-yy-zz, in which case the positions of day, month and year are determined by Android preferences
* if time is ommitted it is assumed to be 00:00
* time must be in 24hr format
* individual components of date and time can also be separated by a colon, slash etc.

Bytes
*Megabyte and Gigabyte conversions are human-readable rather than precise.


---

## Ah Decrypt File



### Decrypt File

Decrypt the specified SD card file which was previously encrypted with Tasker's Encrypt File action.

The path starts in the root directory of the SD card e.g. secret.txt, secret/recording.mp3.

Key Name is the name of the encryption key to use.

The key is not deleted unless Clear Key is set, since you will usually want to use the same key to encrypt the file again at some point.

There must be space left on the SD card at least equal to the size of the file before starting decryption.

See Encryption in the Userguide for details.


---

## Ah Delete File



### Delete File

Delete an SD card file.

The path starts in the root directory of the SD card.

If Shred Level is more than 0, the contents of the file are overwritten with random bytes the specified number of times before it is deleted.

The intention is to make it (much) harder to recover the contents than if the file was simply deleted.

Security note: shredding will only provide basic protection on 'journalling' filesystems, but most external storage uses FAT32 at the time of writing.


---

## Ah Encrypt File



### Encrypt File

Encrypt the specified SD card file.

The path starts in the root directory of the SD card e.g. secret.txt, secret/recording.mp3

Key Name is the name of the encryption key to use.

Usually the key is deleted after encryption, set Leave Key if you have more files to encrypt.

There must be space left on the SD card at least equal to the size of the file before starting encryption.

See Encryption in the Userguide for details.

You can also access Tasker's encryption features via File Magic, a Tasker-integrated file manager.


---

## Ah Get Fix



### Get Location

Get a location fix.

GPS: a value will be set when the accuracy stops improving. 'Use GPS Satellites' must be enabled in Android Location Settings.

Net: a value will returned upon the first fix.'Use Wireless Networks' must be enabled in Android Location Settings.

Continue Task Immediately: move on to the next action in the task as soon as the fixing has started.

Keep Tracking: don't stop tracking the location source(s) when a value is returned This will use more power but enables faster fixes after the first one. When using this option, tracking can be stopped by the action Stop Location or doing Get Location without the option checked.

It will stop automatically if at any time no tasks are left to execute or the Get Location times out.

Note: the fix data are stored in the relevant %LOC variables, see the Variables section of the userguide.


---

## Ah Load Image



### Load Image

Load an image into the image store, overwriting any image there previously.

The image store is an image held in the device memory on which all actions from the Image category act.

Once finished manipulating an image, it can be saved to a file with the Save Image action.

However, it could also be used to e.g. directly set an image element in a scene.

Max Width Or Height: if specified, the image is scaled as it is loaded so that no dimension is more than the specified number of pixels. Useful when memory is an issue.

Respect EXIF Orientation: if the specified image is JPG format, it will be automatically adjusted after loading dependent on the EXIF meta-data tag, if present.


---

## Ah Menu



### Menu

Show a selection dialog and perform a different action depending on which item the user selects.

The Layout parameter specifies the look of all the items. Click to edit it.

The Items parameter specifies the content of each item.

The selected item label and index are available in the resulting task in %tap_label and %tap_index respectively.

If the user does not explicity select an item then when the specified Timeout is reached the item with a checkmark will be automatically selected.

More info: Menu element in the Userguide.


---

## Ah Mobile Data Direct



### Mobile Data

Set mobile data status without affecting incoming calls.

This works reliably on rooted Android devices.

On non-rooted devices this action needs the WRITE_SECURE_SETTINGS permission [WRITE_SECURE_SETTINGS permission](https://tasker.joaoapps.com/userguide/en/help/ah_secure_setting_grant.html)  but may not always work.

On most devices the action simply changes the UI in Android Settings but doesn't really change the setting in the background.

It was found that on some Samsung devices if you connect to a Wifi network and then disconnect again that the setting will "stick" for real.

If you find another trick that will make the setting "stick" after using this action please let the developer know so that the trick can be applied for everyone! :) Thanks in advance!



---

## Ah Run Task



### Perform Task

More info about the parameters of this action here [here](https://github.com/joaomgcd/TaskerDocumentation/blob/master/en/help/perform%20task%20info.md) .

Run the selected Tasker task.

You can 'nest' as many tasks as you wish.

When this action is used as part of an Enter task, the settings it contains are *not* restored when the profile exits.

When a task is started from an existing task, the existing task continues unless the Stop parameter is set.

If you set the priority lower than the current task, the current task will finish before the new one starts.

If you set the priority the same or higher than the current task (a good way to do this is to specify '%priority+1'), the new task will completely execute before the current one resumes.

Values assigned to %par1 and %par2 are available in the child task as normal variables.

If the child does a Return action, the Return Value Variable in the parent task is set to the Value specified in that Return action, however note that the value will not be returned if the Perform Task is the last action of the parent.

See Flow Control in the Userguide for more info.

When you add an action in a task you can use the search field in the dialog to search for a task name directly and then select the Perform Task action to have the task name filled in automatically.
If you do this when adding a favorite action (long click the + button in task) you can have a direct shortcut to the specific task you searched for.

Check out a demo for this here [Check out a demo for this here](https://youtu.be/S9QG-e8Udok)


---

## Ah Save Image



### Save Image

Write the image currently in the image store to a file.

The file extension will only be respected for JPEG and WEBP (if available on the device); all other extensions will result in PNG output.

Higher Image Quality values will also result in greater file size and more chance of running out of memory. Image Quality is not relevant for PNG.

See also: Load Image.


---

## Ah Scan Card



### Scan Media

Force the system to scan the SD card for new/deleted media. This can save a lot of time removing and reinserting the physical card.

If a file is specified, only that file is scanned.
If a directory is specified, all of its contents will be scanned recursively.

Note: repeatedly scanning the same file will not update the thumbnail in Gallery.

On Android 4.4+, scanning the whole card or a directory only picks up *new* files and the task waits till the scan is finished.


---

## Ah Scene Element Add Geomarker



### Element Add GeoMarker

Add a marker to a scene Map element.

Spot Radius specifies the size of circle to place at the base of the market.

The scene must have been created first.

See also: Element Delete GeoMarker.


---

## Ah Scene Element Background Colour



### Element Back Colour

Set the background colour(s) of a scene element.

Applies to Text, TextEdit, Image, Menu, Oval and Rectangle elements.

End Colour is only relevant if the element's background has a Shader specified.

The scene must have been created first.


---

## Ah Scene Element Border



### Element Border

Set the width and colour of an element's border.

Applies to Text, TextEdit, Image, Menu, Oval and Rectangle elements.

The scene must have been created first.


---

## Ah Scene Element Delete Geomarker



### Element Delete GeoMarker

Delete a marker from a scene Map element.

The scene must have been created first.

See also: Element Add GeoMarker.


---

## Ah Scene Element Depth



### Element Depth

Set the depth of the specified element in the scene relative to all the other elements.


---

## Ah Scene Element Focus



### Element Focus

Give input focus to, or remove input focus from, the specified element.


---

## Ah Scene Element Image



### Element Image

Set the image of an Image scene element or the icon of a Button or Slider element.

The scene must have been created first.


---

## Ah Scene Element Map Control



### Element Map Control

Manipulate a Map scene element e.g. to zoom in or out

The scene must have been created first.

Note: Enable Compass: the compass is only shown when the map is tilted or rotated.


---

## Ah Scene Element Position



### Element Position

Move a scene element within it's scene.

The scene must have been created first.


---

## Ah Scene Element Size



### Element Size

Change the size of an element.

The scene must have been created first.


---

## Ah Scene Element Test



### Test Element

Test some property of the specified scene element e.g. it's position within the scene.

The scene must have been created first and in some cases already be displayed.

Not all tests apply to all elements.


---

## Ah Scene Element Text



### Element Text

Set the text of a scene element.

Applies to Button, Text and TextEdit elements only.

The scene must have been created first.

For TextEdit elements, the parameter Selection specifies a part of the text to select after it has been set.
The specification is either a range (e.g. 1:4 for characters 1 to 4 inclusive, or 3: to select everything from character 3 onwards) or a simple match e.g. v*e to select everything between a v and an e. Use : or * to select the whole text.


---

## Ah Scene Element Text Colour



### Element Text Colour

Set the text colour of a scene element

Applies only to Button, Text and TextEdit elements.

The scene must have been created first.


---

## Ah Scene Element Value



### Element Value

Set the value of a scene element.

Applies only to CheckBox, Number Picker, Slider, Spinner and Toggle  elements.

For a CheckBox, value should be 0 (off) or 1 (on).

For a Spinner, the value is the index of the item to set.

The scene must have been created first.

The action can only trigger a possible event associated with the element value if the scene is currently showing.

To set the value of a Text, EditText or Button element, use the Element Text action.


---

## Ah Scene Element Video Control



### Element Video Control

Manipulate a Video element in a scene.

Not all actions are possible at all times. For instance, Play is not possible until the video has loaded.

Tip: to simplify a manual load-and-start-video, specify in the element a variable as the source of the video and check Start Automatically. Then instead of using a Video Control action with Load Source, just set the variable.


---

## Ah Scene Element Visibility



### Element Visibility

Hide or show a scene element.

The scene must have been created first.


---

## Ah Scene Element Web Control



### Element Web Control

Manipulate a WebView scene element e.g. to page up or down

This action will not work until the scene has ben displayed at least once.


---

## Ah Secure Setting Grant



#### Write Secure Settings Permission

To use this, Tasker needs to be granted permission to Write Secure Settings on your device

Easy Way

Install the Tasker Permissions [Tasker Permissions](https://tasker.joaoapps.com/taskerpermissions.html)  app and follow the prompts.

Hard Way (don't bother with this if you were able to do it the easy way)

- Setup ADB on your PC as described here [here](ah_adb_setup.html) .

- Use these commands:

adb shell pm grant net.dinglisch.android.taskerm android.permission.WRITE_SECURE_SETTINGS

If you're on a mac write

./adb shell pm grant net.dinglisch.android.taskerm android.permission.WRITE_SECURE_SETTINGS

Note: On MIUI devices you may have to open developer options and enable the USB debugging (Security Settings) setting (and the Disable permission Monitoring setting in some cases) to be able to run the above command.



---

## Ah Send Intent



### Send Intent

Broadcast an ordered Intent.

This action is intended for advanced users.

See Intents in the Userguide for more info.


---

## Ah Send Sms



### Send SMS

Send an SMS without user interaction.

Multiple numbers can be specified by comma-separating them.

Email addresses are not supported.

Store in Messaging App: whether a record will be kept of the sent SMS in the standard messaging app (only available prior to Android 4.4).

Success or failure can be caught by creating an Event context SMS Success/Failure.

Maximum length of an SMS is 140 characters. In some character encodings that translates to 140 characters, in others to only 70 characters.


---

## Actions | Variable Set



# Variable Set

Set the variable Name to the value To.

Name can be any desired string, however it's advisable to make it a sequence that does not commonly occur in text otherwise it will match at unexpected times.

Names all in lower-case are local variables which are only visible in the current task.

If Recurse Variables is checked, all variables mentioned in the To parameter will be repeatedly replaced until there are no variable names left, otherwise only one round of variable replacement will take place.

If Append is checked, To is added to the existing value of the variable.

If Do Maths is checked then at the time of assignment the value of To will be evaluated as a mathematical expression.

Example:

Name: %FROG

To: %VOLC + 1

Assuming %VOLC is 8, if Do Maths is checked, %FROG will get the value '9', otherwise it will get the value '8 + 1'.

If To cannot be numerically evaluated (e.g. it is 'cat + 3') then the current task will terminate.

## See also

Variables [Variables](../variables.html)  section in the Userguide.



---

## Ah Take Photo



### Take Photo

Take a photo. The current activity will be interrupted for a couple of seconds.

If Discreet is checked, there will be no visible or audible sign of the picture being taken, and the device will not turn on if it is already off (except on Eclair devices).

Without Discreet, a small delay allows time for aiming.

Insert in Gallery: immediately insert a thumbnail in the Gallery application, otherwise it will not appear until the next time the SD card is scanned.

Naming Sequence: Series: photo names have an index number attached which increases with each one taken. Chronological: the date and time is attached to the filename.

Photos are in JPG format and stored in /sdcard/dcim/Tasker/. You should not attach the .jpg affix when specifying the filename prefix.

See also: Menu / Prefs / Action / Camera Delay.


---

## Ah Test Tasker



### Test Tasker

Test some aspect of Tasker's configuration.

The Global Var, Local Var, Profile, Scene and Task test types store their results as an array (%var1, %var2 etc).

The Global Var type doesn't include built-in variables.

The Profile and Task test types only list named profiles or tasks.


---

## Ah Tether Usb



### USB Tether

Turn on sharing of the device'ss Internet connection via USB cable.

On some devices, you may need to enable the USB tether once in Android settings before Tasker will be able to do it.


---

## Ah Tether Wifi



### WiFi Tether

Turn on sharing of the device's Internet connection via wifi.

If Wifi was on, it will be turned off, you will need to enable it manually after the tether.

If the action fails for you, saying that you need to the android.permission.TETHER_PRIVILEGED permission you can still make it work if you have a rooted device:

- Make a a backup of your Tasker setup

- Copy "/data/app/net.dinglisch.android.taskerm" folder to "/system/priv-app"

- Uninstall Tasker and reboot

- After the reboot Tasker should be installed as a System app.

- Restore Tasker data

Note: The current status/state of the Hotspot can be checked using the %TETHER Global Variable



---

## Ah Timer Widget Control



### Timer Widget Control

Control the operation of a previously-created Task Timer widget.

End: cause the timer to finish. The associated task will execute if the timer was previously running.

Resume: resume (or start, if not paused)) the countdown.

Reset: stop the countdown and set it to it's initial value.

Update: refresh the display of the remaining time, not usually necessary.


---

## Ah Timer Widget Set



### Timer Widget Set

Set the period of a previously-created Task Timer widget.

The elapsed time is set to 0.

If the timer was already running, it will continue to do so.


---

## Tasker Help Files



#filter {

background-color: #f2f2f2;

border-radius: 5px;

position: fixed;

right: 16px;

}

.version {

padding-left: 4px;

}

body {

font-family: Arial, sans-serif;

line-height: 1.6;

color: #333;

background-color: #f5f5f5;

padding: 10px;

}

#filter {

width: 200px;

height: 30px;

border: none;

padding: 5px;

margin: 20px 0;

font-size: 16px;

}

.type h2 {

color: #007BFF;

font-size: 26px;

margin-bottom: 10px;

}

.type ul {

list-style: none;

padding-left: 0;

}

.type ul li {

padding: 10px;

border-bottom: 1px solid #ddd;

}

.type ul li:last-child {

border-bottom: none;

}

.type ul li a {

color: #007BFF;

text-decoration: none;

}

.type ul li a:hover {

color: #0056b3;

text-decoration: underline;

}

.type ul li div {

display: flex;

justify-content: space-between;

align-items: center;

}

.version {

font-size: 14px;

color: #777;

}

@media (min-width: 768px) {

.type ul li div {

flex-direction: column;

align-items: flex-start;

}

#filter {

max-width: 500px;

}

}

.type h2 {

color: #FF9800;

}

.type ul li a {

color: #FF9800;

}

.type ul li a:hover {

color: #CC7A00;

}

.type[name='ah'] {

background-color: #f9f2e7;

border: 1px solid #FF9800;

padding: 10px;

margin-bottom: 20px;

}

.type[name='eh'] {

background-color: #e7f9f5;

border: 1px solid #00BCD4;

padding: 10px;

margin-bottom: 20px;

}

.type[name='sh'] {

background-color: #e7e7f9;

border: 1px solid #3F51B5;

padding: 10px;

margin-bottom: 20px;

}

var cachedNames = {};

var files = "";

var versions = null;

const groupBy = (arr, keyGetter) => {

const out = {};

for (let item of arr) {

const key = keyGetter(item);

out[key] ??= [];

out[key].push(item);

}

return out;

};

const TYPE_ACTION = "ah";

const TYPE_EVENT = "eh";

const TYPE_STATE = "sh";

const buildIndex = async () => {

const filterText = document.querySelector("#filter").value.toLowerCase();

const elementContent = document.querySelector("#content");

elementContent.innerHTML = "";

const parser = new DOMParser();

const getParsedNames = async (link) => {

if (cachedNames[link]) return cachedNames[link];

const names = await (await fetch(link)).text();

const parsedNames = parser.parseFromString(names, "text/xml");

cachedNames[link] = parsedNames;

return parsedNames;

}

if (!files) {

files = await (await fetch("./")).text();

}

if (!versions) {

versions = await (await fetch("./versions.json")).json();

}

const html = parser.parseFromString(files, "text/html");

const parsedActionNames = await getParsedNames("./action_names.xml");

const parsedEventNames = await getParsedNames("./event_names.xml");

const parsedStateNames = await getParsedNames("./state_names.xml");

const getParsedName = (type, id, parsed) => {

const typeForName = type.replace("h", "n");

const name = parsed.querySelector(`[name="${typeForName}_${id}"]`);

if (!name) return null;

return name.textContent;

}

const links = Array.from(html.querySelectorAll("td>a")).map(it => it.href).filter(it => it.indexOf("help/") >= 0);

const namesAndLinks = links.map(link => {

var name = link.substring(link.lastIndexOf("/") + 1, link.length - 5);

const originalName = name;

const id = name.substring(3);

const helpType = name.substring(0, 2);

name = id.replaceAll("_", " ");

const words = name.split(" ");

name = words.map((word) => {

if (!word) return "";

return word[0].toUpperCase() + word.substring(1);

}).join(" ");

return { id, name, link, helpType, originalName }

})

.filter(it => it.helpType === TYPE_ACTION || it.helpType === TYPE_EVENT || it.helpType === TYPE_STATE)

.filter(it => it.id != "index");

const groupedByType = groupBy(namesAndLinks, it => it.helpType);

const printType = (typeName, type) => {

const typeEntries = groupedByType[type];

const parsed = type == TYPE_ACTION ? parsedActionNames : (type == TYPE_EVENT ? parsedEventNames : parsedStateNames);

const typeDiv = document.createElement("div");

typeDiv.setAttribute("name", type);

typeDiv.classList.add("type");

typeDiv.innerHTML = `<h2>${typeName}</h2>`;

const typeList = document.createElement("ul");

var hasEntries = false;

typeEntries.forEach(it => {

const entry = document.createElement("li");

const entryDiv = document.createElement("div");

const link = document.createElement("a");

link.href = it.link;

const id = it.id;

var name = it.name;

const fromParsed = getParsedName(type, it.id, parsed);

if (fromParsed) {

name = fromParsed;

}

var newInVersion = versions.entityCodesNewInVersions[it.originalName];

if (newInVersion && typeof newInVersion == "number") {

newInVersion = versions.numbersToNames[newInVersion];

}

if (newInVersion) {

const newInVersionSplit = newInVersion.split(".");

if (newInVersionSplit.length > 2) {

newInVersion = newInVersionSplit[0] + "." + newInVersionSplit[1];

}

}

if (filterText) {

const matchesName = name.toLowerCase().indexOf(filterText) >= 0;

var matchesVersion = newInVersion && newInVersion.indexOf(filterText) >= 0;

if (!matchesName && !matchesVersion) return;

}

hasEntries = true;

link.innerHTML = name;

link.target = "_blank";

entryDiv.appendChild(link);

if (newInVersion) {

const entryVersion = document.createElement("span");

entryVersion.classList.add("version");

entryVersion.innerHTML = `(added/last updated in <a href="https://tasker.joaoapps.com/changes/changes${newInVersion}.html">v${newInVersion}</a>)`;

entryDiv.appendChild(entryVersion);

}

entry.appendChild(entryDiv);

typeList.appendChild(entry);

});

if (hasEntries) {

typeDiv.appendChild(typeList);

elementContent.appendChild(typeDiv);

return typeDiv;

}

return null;

}

const actionsDiv = printType("Actions", TYPE_ACTION);

const eventsDiv = printType("Events", TYPE_EVENT);

const statesDiv = printType("States", TYPE_STATE);

const hash = window.location.hash.substr(1);

if (hash) {

const type = hash.substring(0, 2);

const typeDiv = type == TYPE_ACTION ? actionsDiv : (type == TYPE_EVENT ? eventsDiv : statesDiv);

if (typeDiv) {

typeDiv.scrollIntoView();

}

}

if (!statesDiv && !eventsDiv && !actionsDiv) {

elementContent.innerHTML = "Nothing found";

}

}

buildIndex();



---

## Eh Timer Change



### Timer Change

The status of the Task Timer widget with the specified task name has changed.


---

