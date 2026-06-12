# Tasker Reference: Scenes

This file provides detailed documentation on Tasker Scenes concepts, options, and workflows.

## Table of Contents

- [Tasker: Scenes](#tasker-scenes)
- [Tasker: Scene Edit](#tasker-scene-edit)
- [Tasker: Scene Properties Edit](#tasker-scene-properties-edit)
- [Tasker: Scene Element Edit](#tasker-scene-element-edit)
- [Tasker: Scene Element: Button](#tasker-scene-element-button)
- [Tasker: Scene Element: Button](#tasker-scene-element-button)
- [Tasker: Scene Element: Doodle](#tasker-scene-element-doodle)
- [Tasker: Scene Element: Image](#tasker-scene-element-image)
- [Tasker: Scene Element: Map](#tasker-scene-element-map)
- [Tasker: Scene Element: Menu](#tasker-scene-element-menu)
- [Tasker: Scene Element: Number Picker](#tasker-scene-element-number-picker)
- [Tasker: Scene Element: Oval / Rectangle](#tasker-scene-element-oval--rectangle)
- [Tasker: Scene Element: Slider](#tasker-scene-element-slider)
- [Tasker: Scene Element: Spinner](#tasker-scene-element-spinner)
- [Tasker: Scene Element: Text](#tasker-scene-element-text)
- [Tasker: Scene Element: TextEdit](#tasker-scene-element-textedit)
- [Tasker: Scene Element: Toggle](#tasker-scene-element-toggle)
- [Tasker: Scene Element: Video](#tasker-scene-element-video)
- [Tasker: Scene Element: Web](#tasker-scene-element-web)

---

## Tasker: Scenes



##
Scenes

### Introduction

A scene is a graphical user-interface consisting of a collection of elements to which tasks can be attached to be run when the user interacts with them e.g. by tapping them.

Tasker uses scenes for things like popup dialogs, menus and getting input from the
user but scenes can actually be displayed by the user whenever desired, meaning
they can be used for things like creating simple user-designed applications or showing extra controls over the top of (selected) existing applications.

Scenes are completely user-customisable via a drag-and-drop graphical editor [editor](activity_sceneedit.html) .

### Displaying Scenes

#### Actions: Enter Key, HTML Popup, Lock, Menu, Popup, Popup Task Buttons and
Variable Query

These actions use a built-in scene with the same name as their action.
After creating a task with such an action, the associated scene can be found
under the Scenes tab on the main Tasker screen. That scene can be edited so that
e.g. all Popup actions have the same style because they all use the same scene.

The parameters specified in the action are applied to the scene before it
is show. For instance, if the scene has a Title element it will be
set to the title specified in the action and the scene resized appropriately.

It might be desirable to have a different style for e.g. some Popup actions, in which case:

- clone the built-in scene long-clicking on it in the Scenes tab

- edit the clone to change the contents

- in a Popup action, specify that the cloned scene should be used
by clicking on the Layout parameter in the action edit screen.

#### Scene Category Actions: Create Scene, Show Scene, Hide Scene, Destroy Scene

These allow a completely free hand over when a scene should be displayed and it's
life-cycle. They all act on scenes pre-designed in the Scenes tab.

Usually, only Show Scene and Destroy Scene will be
used, however sometimes it's useful for a scene to be created but not visible to
the user:

- by hiding a scene instead of completely destroying it, the settings of the elements
are retained for next time it is shown

- the values of the elements in the scene can be changed to track certain
events so that the scene can be immediately displayed when required without any
configuration

### Scene Elements

Each scene is comprised of a number of elements.

An element has three main components:

#### Geometry

It's size and position on the screen. An element's geometry is specified in
the scene editor [scene editor](activity_sceneedit.html) .

#### Content

How it looks on the screen.

Specified under the UI tab in the element editor. Some
elements also have a Background tab. A Menu element has an additional Items tab.

#### Event Tasks

What should happen when the user interacts with the element.

Specified under the right-most tabs after clicking on the element in the element editor.
There are different events depending on the type of element. For instance, a Button has
tap and long-tap events while a Slider has a value-set event.

Event tasks are run at priority one higher than the task which displayed the scene

Local variables set by event tasks are visible to all tasks in the same scene.

### Scene Element Actions

In the Scenes action category, there are several actions for setting
the properties of scene elements. You can use these for a wide variety
of purposes e.g.

- when a slider value is set, change the zoom of an associated map element

- set the size of an element depending on current light level

- animate elements around a scene

Note that actions that affect scene elements can only be used when the scene has
already been created (via Create Scene or Show Scene).
The scene does not have to be visible.



---

## Tasker: Scene Edit



##
Scene Edit

The scene editor is used for designing custom scenes.

The editor consists of three areas:

### Display Area

The main part of the editor, where the position and size of elements are arranged.
The display area has two modes dependent on the setting of the magnifying glass icon in the corner.

#### Preview Mode

This mode shows the scene as it will appear when displayed.

- Click-and-drag on the edge of the scene to resize it

#### Editing Mode

This mode is zoomed to make editing easier.

- Long-click on an empty area to create a new element positioned there

- Long-click on an element to get options for the element

- Click on an element to edit it.

- Click-and-drag on the centre of an element to move it

- Click-and-drag on the edge of an element to resize it

When moving and resizing, the sides of elements are snapped to a grid to make alignment
easier. The grid size is unique to each scene and can be changed via Menu / Grid Size.

### Tool Bar

#### Touch Mode

There are four touch modes which decide the effect of taps on the
display area.

Normal Mode is described above. Edit Mode is the same as
Normal Mode except that all controls except the
Touch Mode selector are hidden to allow access to small controls along the scene edges.
Move Mode is intended to make it easier to reposition elements. Resize mode
is for making resizing easier.

#### Element Picker

Allows selection of an element by name. This is most useful when an element is
difficult to directly click on due to other elements or because it's very small.

Both short and long clicks on the element names behave the same as short and long
clicks on the element itself.

#### Undo

Allows undo of all operations, up to 20 steps in the past.

#### New Element

Create a new element in the middle of the scene. Useful if the scene is already
cluttered with a lot of elements so there is no free space.

### Menu Options

#### Background Colour

A complex background can be set by long-tapping an element and specifying it as
the background element [background element](#back) . If a uniform colour is sufficient, it can also
be specified with this menu option.

However, there is a special case where it's a good idea to specify a background colour even
if you already have a background element. A scene is resized to fit the container
into which it's placed, but in some cases (e.g. when it is shown as a full screen activity) there will be margins left on one
side of the container because the aspect ration of the scene
(the relative size of its width and height) of a scene is never changed. In such a
case, the margins are coloured with the background colour specified here.

### Element Long-Click Options

#### Set Background

An element which is set as the scene background is resized to always fill the whole scene
and interferes less with selection of other elements. To reverse this, long-tap on it and
select Set Foreground.

#### Pin

When an element is positioned satisfactorily, it can be pinned to make it easier to
select and manipulate other elements. To reverse this, long-tap on it and select
Unpin.

#### Set Depth

Each element has a particular depth which is unique to it. Deeper elements are obscured
by shallower elements which overlap them.

### Orientation

The geometry (position and size) of each element can be configured independently for
portrait and landscape display orientations by rotating the device to the desired
orientation in the editor.

If no geometry is configured for a particular orientation when the scene is displayed, Tasker will attempt to
fit the elements into the scene based on the geometry of the elements in the other orientation.



---

## Tasker: Scene Properties Edit



##
Scene Properties Edit

Allows configuration of the general properties of a scene.
The different types of property are divided into tabs.

Each basic type of scene (Overlay, Dialog and Activity)
has a different set of relevant properties. The Property Type
parameter in the UI tab determines which properties are shown
for configuration.

- UI [UI](#ui)

- Actions [Actions](#actions)

- Event [Event](#event)

- Key [Key](#key)

- Home Tap [Home Tap](#hometap)

- Tab Tap [Tab Tap](#tabtab)

### UI

Configures the visual style and content of the scene.

Geometry (not shown in Beginner Mode [Beginner Mode](beginner.html) ) allows precise
specifiction of the pixel size of the scene in portrait and/or landscape modes.

Orientation determines how to make the decision about whether the scene
should be displayed in portrait or landscape mode.
The
Android
developer guide [Android
developer guide](https://developer.android.com/reference/android/R.attr.html#screenOrientation)  explains the various options.

The Action Bar Style, Title, Subtitle, Icon and Tab Labels are only relevant
to Activity scenes and refer to properties of the action bar.

Icon refers to the home icon in the top-left of
the action bar. When clixked it generates a Home Tap [Home Tap](#hometap)
event.

Tab Labels is a comma-separated list of tabs to show in
the action bar. When a tab is selected it generates a Tab Tap [Tab Tap](#tabtap)
event.

### Actions

Only relevant for Activity scenes.

Each row configures an action item in the action bar. Starting from the left, the controls
are:

- icon button
the icon to show for the item

- label text
the label to show for the item

- action button
an action to run when the item is tapped

To add an item, click the plus button at the bottom of the screen. Items
can be rearranged and deleted by click-and-dragging at the right hand side.

Whether the items are shown in the main bar or the Overflow Menu (accessed via the 3 dots in the top right of the action bar) is decided using the following rules:

- items with just an icon will always be shown in the main bar

- items with icon and label will be shown if there is room

- items with just a label will always be in the overflow menu

### Event Tabs

Event tabs stipulate what Tasker should do when the user interacts with the
scene in some way. Most consist only of a task to specify but some
allow a filter specification so that the task only runs if the event matches
the filter.

To help the task to decide what to do with the event and to allow a single
task to handle many different events if desired, Tasker sets certain
local variables which give specific information about it. The variables
are easily accessible by clicking the usual variable tag icon in any action
in the task.

The following variables are available in all such tasks:

- %scene_name
the name of the scene containing the element

- %event_type
the name of the event (e.g. Tab Tap)

#### Key

Available only for Dialog and Activity scenes.

Occurs when a key has been pressed which has not been dealt with elsewhere.
Note that EditText elements with focus will absorb key presses and they won't
generate a separate Key event.

The filter part of the Key event acts as follows:

- Keys: a slash-separated (/) list limiting the keys to handle, other
keys will be passed on to the system to handle. When no keys are specified,
all keys will be handled.

The keys can be specified via code or name e.g. back/78/a

- Stop Event: if checked, any keys handled by the scene will
not be passed on to the system. Example use: prevent a user leaving the
scene via the back key.

The following variables are available in tasks triggered by Key events:

- %key_code
the unique numeric identifier

- %key_name
the human name of the key

Key codes and their names can be found on the Android KeyEvent [KeyEvent](https://developer.android.com/reference/android/view/KeyEvent.html)  reference page. Note that
Tasker removes the KEYCODE prefix in keynames to save typing.

#### Home Tap

Available only for Activity scenes and when an Icon has been specified in
the UI tab.

The event is triggered when the user taps the home icon in the top left
of the action bar.

#### Tab Tap

Available only for Activity scenes and when one or more Tab Labels have been
specified in the UI tab.

The event is triggered when the user taps a tab in the action bar.

The following variables are available in tasks triggered by Tab Tap events:

- %tap_index
the tab number, starting at 1

- %tap_label
the tab label, as specified in the Tab Labels parameter of the UI tab



---

## Tasker: Scene Element Edit



##
Scene Element Edit

Allows configuration of the properties of a scene element. The different
types of property are divided into tabs.

- UI [UI](#ui)

- Items [Items](#items)

- Background [Background](#background)

- Event [Event](#event)

- Change [Change](#checkchange)

- Focus [Focus](#focus)

- Tap, Long Tap [Tap, Long Tap](#tap)

- Item Select [Item Select](#itemselect)

- Value Selected [Value Selected](#value)

- Item Tap [Item Tap](#itemtap)

- Stroke [Stroke](#stroke)

- Text Changed [Text Changed](#text)

- Link Tap [Link Tap](#linktap)

- Page Loaded [Page Loaded](#pageloaded)

- Video [Video](#video)

Not all elements have all tabs.

### UI

For the most part, configures the visual style of the element.

### Items

Only relevant to Menu and Spinner elements.

Each row configures an item in the menu/spinner. Starting from the left, the controls
are:

- selection checkbox
this is only present when Selection Mode is set to Single or Multi. It stipulates whether the item will be shown as selected when the menu is displayed.

- icon button
the icon to show for the item. If you don't want to show an icon, hide the icon element in the Layout parameter in the UI tab

- label text
the label to show for the item. If you don't want to show a label, hide the label element in the Layout parameter in the UI tab

- action button
an action to run when the item is tapped

To add an item, click the plus button at the bottom of the screen.
Items can be rearranged and deleted by click-and-dragging at the right hand side.

### Background

Configures a rectangle shape to be used as the background for the element
when it is displayed. The background will be stretched to fit the size of
the element.

If you want to use an image for a background, create a separate Image element and
place it underneath.

### Event Tabs

Event tabs stipulate what Tasker should do when the user interacts with the
element in some way. When the scene is showing, the event will also occur
if an action (probably Element Value) sets the element.

Most events consist only of a task to specify but some
allow a filter specification so that the task only runs if the event matches
the filter.

To help the task to decide what to do with the event and to allow a single
task to handle many different events if desired, Tasker sets certain
local variables which give specific information about it. The variables
are easily accessible by clicking the usual variable tag icon in any action
in the task.

The following variables are available in all such tasks:

- %scene_name
the name of the scene containing the element

- %element_name
the name of the element that the user interacted with (e.g. Button1)

- %element_type
the type of element (e.g. Button)

- %event_type
the name of the event (e.g. Tap)

#### Text Changed

Elements: TextEdit

This event is triggered whenever the text changes e.g. because a
letter key has been pressed while the element had focus.

- %new_val
the new text

- %old_val
the old text

Text entry is buffered so that it may be up to 1 or 2 seconds before
new input is seen, and that input may include several accumulated
changes.

#### Change

Elements: CheckBox, Toggle

- %new_val
the new state of the element (on or off)

- %old_val
the last state (on or off)

#### Focus

This event is triggered when the element gains or loses focus, probably
because the user has tapped it or another focusable element.

Elements: TextEdit

- %focused
whether the element now has focus (true) or not (false)

#### Tap, Long Tap

Elements: Button, Doodle, Image, Map, Oval, Rectangle, Text

In a Map element, the following variables are available:

- %coord
the latitute,longitude of the tapped location on the map

- %label
the label of the tapped GeoMarker (if any). You can add GeoMarkers to a Map element with the action Scene / Element Add GeoMarker

#### Value Selected

Elements: Number Picker, Slider

- %new_val
the new value of the element (e.g. 50)

- %old_val
the last selected value (e.g. 43)

#### Item Tap, Item Long Tap

Elements: Menu

- %select_indices
a comma-separated list of currently selected items in the list (e.g. 3,4)

- %select_labels
a comma-separated list of the labels of currently selected items in the list (e.g. Blue,Yellow)

- %tap_index
the index of the item that was tapped to cause this event (e.g. 3)

- %tap_label
the label of the item that was tapped to cause this event (e.g. Blue)

#### Stroke

Elements: Doodle, Image, Oval, Rectangle, Text

A stroke has two filter parameters.

- Direction
the direction from the start point of the stroke to the end point

- Length
minimum distance in (approximate) pixels from the start point of the stroke to the end point

If either of these parameters don't match the event, the task will not run.

- %stroke_dir
Direction, as described above

- %stroke_len
Length, as described above

#### Item Select

Elements: Spinner

Occurs when a new item is selected.

- %tap_index
the index of the item that was selected

- %tap_label
the label of the item that was selected

#### Link Tap

Elements: WebView

A Link Tap has two filter parameters:

- URL
the URL of the tapped link. If entered, the tapped URL must match [match](matching.html)  the entry (e.g. http://*.fruit.com) for the task to run

- Stop Event
whether to stop the WebView following the link

- %url
URL as described above

#### Page Loaded

Elements: WebView

- %url
the URL of the page (e.g. http://i.hate.fruit/except/mangos.html)

#### Video

Elements: Video

Occurs when the state of the video playback changes.

- %event_subtype
the type of the video event, possible values being: Prepared, BufferStart, BufferEnd, RenderStart, Lagging, Finished

Note that the Finished event will never occur if the Video element
has the Loop parameter checked.



---

## Tasker: Scene Element: Button



##
Scene Element: Button

#### About

A standard Android button enhanced to allow display of an icon, text or
both.

#### Parameter: Position

If both a Label and Icon are specified, the Position parameter refers to
the position of the Label. The Icon is then placed opposite the Label.

#### Events

- Tap, Long Tap [Tap, Long Tap](activity_elementedit.html#tap)

#### Related Actions

- Element Image

- Element Text [Element Text](help/ah_scene_element_text.html)

- Element Text Colour [Element Text Colour](help/ah_scene_element_text_colour.html)

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Focus

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

## Tasker: Scene Element: Button



##
Scene Element: CheckBox

#### About

A standard Android checkbox to indicate e.g. an item selection state.

#### Events

- Change [Change](activity_elementedit.html#checkchange)

#### Related Actions

- Element Value [Element Value](help/ah_scene_element_value.html)

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

## Tasker: Scene Element: Doodle



##
Scene Element: Doodle

#### About

A Doodle is an image created by the user with a simple finger-painting
screen.

Click the Doodle parameter to edit the doodle.

Doodles are stored on external storage in the directory /sdcard/Tasker/cache/doodles
in case they are masterpieces which demand publishing.

#### Events

- Tap, Long Tap [Tap, Long Tap](activity_elementedit.html#tap) ,

- Stroke [Stroke](activity_elementedit.html#stroke)

#### Related Actions

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Focus

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

## Tasker: Scene Element: Image



##
Scene Element: Image

#### Events

- Tap, Long Tap [Tap, Long Tap](activity_elementedit.html#tap)

- Stroke [Stroke](activity_elementedit.html#stroke)

#### Related Actions

- Element Image

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

## Tasker: Scene Element: Map



##
Scene Element: Map

#### About

A Map element is a view onto the same kind of map window used by Google Maps
but is much more automateable than the standalone app.

Map elements cannot appear in Overlay scenes.

When shown with the display type Dialog, Dim Behind or Dialog, Dim Behind Heavy
the map will also be dimmed starting with Tasker 4.5, an unfortunate side-effect of the
dimming method.

#### Related Actions

- Element Add GeoMarker [Element Add GeoMarker](help/ah_scene_element_add_geomarker.html)

- Element Delete Geomarker [Element Delete Geomarker](help/ah_scene_element_delete_geomarker.html)

- Element Map Control [Element Map Control](help/ah_scene_element_map_control.html)

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### Events

-  Tap, Long Tap [Tap, Long Tap](activity_elementedit.html#tap)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

## Tasker: Scene Element: Menu



##
Scene Element: Menu

#### About

A menu displays a variable selection of items and can have a separate action, text and
icon defined for each item in the list.

#### Parameter: Source

Items can either be filled manually or from a variable array. In the case of an array,
the list shows all the items starting at the first index; %var(1) %var(2) etc.

In the case of manual specification, click on the Items tab in the element editor
to specify the items.

#### Parameter: Selection Mode

There are three selection modes:

- single: tapping an item deselects any other item selected

- multi: several items can be selected at the same time

- none: tapping an item never selects it

Selected items are highlighted. There are two ways to find out the selected
items:

- assign a task under the Item Tap element event tab. Every time an item is
tapped, the selected items are available in the local variable %select_indices

- query the selected items at any time using the action Element Get Value

#### Parameter: Item Layout

Specifies how each item within the list will be displayed. Each item has exactly the same layout. To change the layout, click on it. Each Menu element has it's own unique item layout.

There are two pre-defined layouts you can choose from (click the magnifying glass icon). 'Icon and Text' is the default.

#### Events

- Item Tap, Item Long Tap [Item Tap, Item Long Tap](activity_elementedit.html#tap)

#### Related Actions

- Menu [Menu](help/ah_menu.html)

allows easy display of a dialog with a title and showing a single menu
element.

When using the Menu action, items are configured in the action itself
rather than in the Menu element.

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)



---

## Tasker: Scene Element: Number Picker



##
Scene Element: Number Picker

#### About

Allows selection of a numeric value from a specified range. Above
and below the selected number the element can be long-clicked to
advance the number series, or the number can be scrolled or flung up or
down by touch.

#### Events

- Value Selected [Value Selected](activity_elementedit.html#value)

Note that the Value Selected event will only fire when scrolling
has finished i.e. when the user has lifted their finger
and the Number Picker has come to rest.

In contrast, long-clicking will produce an event for each
number that is cycled through.

#### Related Actions

- Element Value [Element Value](help/ah_scene_element_value.html)

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.
The Slider Element [Slider Element](element_slider.html)  screen.



---

## Tasker: Scene Element: Oval / Rectangle



##
Scene Element: Oval / Rectangle

#### About

Shape elements are intended mostly for decoration but can also be used
as invisible 'launchpads' for e.g. stroke events.

#### Events

- Tap, Long Tap [Tap, Long Tap](activity_elementedit.html#tap)

- Stroke [Stroke](activity_elementedit.html#stroke)

#### Related Actions

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

## Tasker: Scene Element: Slider



##
Scene Element: Slider

#### About

A standard Android 'seek bar' enhanced to allow specification of the
thumb icon and display indicators for the min, max and current values.

#### Events

- Value Selected [Value Selected](activity_elementedit.html#value)

#### Related Actions

- Element Value [Element Value](help/ah_scene_element_value.html)

- Element Focus

- Element Image [Element Image](help/ah_scene_element_image.html)

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

- Element Editor [Element Editor](activity_elementedit.html)  screen.

- Number Picker Element [Number Picker Element](element_picker.html)  screen.



---

## Tasker: Scene Element: Spinner



##
Scene Element: Spinner

#### About

A spinner allows selection of a single item from a menu. Only the currently
selected item is displayed. When tapped, the menu is shown, when an item is
selected, the menu is hidden again.

#### Parameter: Source

Items can either be filled manually or from a variable array. In the case of an array,
the list shows all the items starting at the first index; %var(1) %var(2) etc.

In the case of manual specification, click on the Items tab in the element editor
to specify the items. The default (initially showing item) is selectable via the checkboxes
on the left.

Note that by default, a spinner is text only. To show also icons, long-click the
icon element in the Item Layout (see below) and select Show.

#### Parameter: Item Layout

Specifies how each item within the list will be displayed.
Each item has exactly the same layout. To change the layout, click on it. Each Spinner element has it's own unique item layout.

#### Parameter: Popup Background Colour

Specifies the background colour of the window which displays the possible
spinner values when the spinner is clicked.

#### Events

- Item Select [Item Select](activity_elementedit.html#itemselect)

#### Related Actions

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Element Value [Element Value](help/ah_scene_element_value.html)

- Test Element [Test Element](help/ah_scene_element_test.html)



---

## Tasker: Scene Element: Text



##
Scene Element: Text

#### About

Displays non-editable text for labels etc.

#### Parameter: Position

Where to place the text within its box

#### Parameter: Text Width Scale

A horizontal scaling factor to squash up
(negative values) or stretch (positive values) the text.

#### Parameter: Font

Specifies a custom font file to use for the text instead of the system
default. Many thousands of free font files (with the filename ending in
.ttf are available for download on the Internet.

#### Parameter: Vertical Fit Mode

What to do when the height of the text to display is greater than
the height of the element.

#### Parameter: Text Format

Specifies how the text should be displayed.

- Plain Text
just show the text as-is

- Text With Links
things that look like links are clickable (though not in the scene editor) e.g. URLs, email addresses, phone numbers

- HTML
interpret the text as a piece of HTML. Only simple tags are interpreted and no images are displayable.

#### Events

- Tap, Long Tap [Tap, Long Tap](activity_elementedit.html#tap)

- Stroke [Stroke](activity_elementedit.html#stroke)

#### Related Actions

- Element Text

- Element Text Colour [Element Text Colour](help/ah_scene_element_text_colour.html)

- Element Border [Element Border](help/ah_scene_element_border.html)

- Element Back Colour [Element Back Colour](help/ah_scene_element_background_colour.html)

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

## Tasker: Scene Element: TextEdit



##
Scene Element: TextEdit

#### About

A standard Android box for text entry.

TextEdit elements cannot appear in Overlay scenes.

#### Parameter: Text

This is the initial text to show in the element, with any variables replaced.

Note that if Text contains a variable, any changes in the variable
value once the element have been shown will not be reflected in the
visible contents of the text box. The reason for this limitation is that
the user can change the text box contents by typing at any time so it is
not possible to track where the variable contents should be, or even if
they are still there at all.

#### Parameter: Position

Where to place the text within its box

#### Parameter: Text Width Scale

Horizontal scaling factor to squash up (negative values) or stretch (positive values) the text.

#### Events

Text Changed [Text Changed](activity_elementedit.html#text)
Focus [Focus](activity_elementedit.html#focus)

#### Related Actions

- Element Text

- Element Text Colour [Element Text Colour](help/ah_scene_element_text_colour.html)

- Element Border [Element Border](help/ah_scene_element_border.html)

- Element Back Colour [Element Back Colour](help/ah_scene_element_background_colour.html)

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

## Tasker: Scene Element: Toggle



##
Scene Element: Toggle

#### About

A button with two states with an indicator light and a label for each state.

#### Events

- Change [Change](activity_elementedit.html#checkchange)

#### Related Actions

- Element Value [Element Value](help/ah_scene_element_value.html)

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

## Tasker: Scene Element: Video



##
Scene Element: Video

#### About

Displays a video from file or URI.

The playback state is maintained during rotation or
hiding of the scene.

#### Parameters: Source

Determines where to acquire the content for the video.

A source which starts with a / or does not contain a :
is treated as a local file path.

Anything else is treated as a URI.

#### Parameter: Start Automatically

If checked, whenever a new video is loaded it will begin play
immediately. If not checked, the video must be started via
the Element Video Control [Element Video Control](help/ah_element_video_control.html)
action.

#### Parameter: Loop

If checked, the video will start playing again from the start when
the end is reached.

#### Parameter: Adapt To Fit

What to do when the video size does not exactly match the element size.

- Stretch

The video is stretched (or shrunk) to fill the element, probably changing the aspect
ratio in the process

- Scale

The video is scaled up or down while maintaining the aspect ratio until
it horizontally or vertically matches the element size. As a result, the video will not completely
fill the element on the other side.

#### Events

- Tap, Long Tap [Tap, Long Tap](activity_elementedit.html#tap)

- Stroke [Stroke](activity_elementedit.html#stroke)

- Video [Video](activity_elementedit.html#video)

#### Related Actions

- Element Video Control [Element Video Control](help/ah_scene_element_video_control.html)

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

Note on Test Element: testing the element Value returns the
current playback position in Milliseconds, Maximum Value returns the duration of the current video.
In both cases, the video must be already in the 'Prepared' (see the
Video event [Video event](activity_elementedit.html#video) ) state before running the test.

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

## Tasker: Scene Element: Web



##
Scene Element: Web

#### About

A Web element is like a browser window.

#### Parameters: Mode / Source

These parameters determine how the content for the WebView is to be acquired.

- URI: the Source parameter refers to a URI
(e.g. http://) from which the WebView should retrieve content.

- File: the Source parameter contains a local
file path from which the WebView should retrieve content.

- Direct: the Source parameter directly specifies
the HTML and/or JavaScript content to load

#### Parameter: Allow Phone Access

If checked, the content in the WebView is allowed access to local device files,
data stores, and can run JavaScript, including Tasker's JavaScript Interface functions [JavaScript Interface functions](javascript.html) .

This is a very powerful feature, since it allows a WebView to
present a complex and highly functional interface, but
should only be enabled if you entirely trust the source of
the specified content.

Note that references to local files must be absolute (include the directory)
even when the WebView source is specified as a file e.g. /sdcard/myfiles/scripts.js

#### Parameter: Self Handle Links

If checked, links will be handled by the WebView itself, otherwise they
will be passed to the system for handling e.g. by the default web browser.

#### Parameter: Support Popups

If this parameter is not checked, HTML elements which generate a popup window, for instance
selection elements in forms, will crash the scene when they are activated.

If this parameter is checked, when the scene is hidden and reshown, some of its state
will be lost e.g. which part of the page was being displayed, zoom level.

#### Events

Link Tap [Link Tap](activity_elementedit.html#linktap) ,
Page Loaded [Page Loaded](activity_elementedit.html#pageloaded)

#### Related Actions

- Element Web Control [Element Web Control](help/ah_scene_element_web_control.html)

- Element Focus

- Element Position [Element Position](help/ah_scene_element_position.html)

- Element Size [Element Size](help/ah_scene_element_size.html)

- Element Visibility [Element Visibility](help/ah_scene_element_visibility.html)

- Element Depth [Element Depth](help/ah_scene_element_depth.html)

- Test Element [Test Element](help/ah_scene_element_test.html)

#### See Also

The Element Editor [Element Editor](activity_elementedit.html)  screen.



---

