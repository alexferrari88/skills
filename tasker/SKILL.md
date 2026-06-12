---
name: tasker
description: Automating Android tasks, profiles, scenes, and actions using Tasker. Use this skill when the user wants to design, modify, or debug Tasker configurations, write JavaScriptlets or shell scripts for Tasker, handle Android intents, or use Tasker variables and matching logic.
---

# Tasker Automation

Tasker is a comprehensive automation app for Android that uses a trigger-action model to automate tasks based on contexts (conditions).

## Core Concepts

- **Profiles**: Connects triggers (**Contexts**) to tasks (**Enter Task** and optional **Exit Task**).
- **Contexts**: Triggers that can be based on **State** (persistent condition), **Event** (one-off occurrence), **Time**, **Day**, **Location**, or **Application** (foreground app).
- **Tasks**: A named sequence of **Actions** executed step-by-step.
- **Variables**: State holders starting with `%`.
  - **Global Variables**: Contain at least one capital letter (e.g., `%MyGlobal`). Persisted and shared across all Profiles and Tasks.
  - **Local Variables**: All lowercase (e.g., `%local_var`). Created and used only within the current execution of a Task.

## Reference Documentation

Detailed references are partitioned as follows to avoid context bloat:

- **Profiles & Contexts**: See [contexts.md](references/contexts.md) for details on Time, Day, Location, State, and Event contexts.
- **Tasks & Actions**: See [tasks.md](references/tasks.md) for detailed descriptions of Task parameters, Flow Control (If, Else, End If, For, Goto), Widgets, and specific actions.
- **Variables & Logic**: See [variables.md](references/variables.md) for built-in variables, custom variables, variable formatting, pattern matching, and mathematical expressions.
- **Scenes & UI**: See [scenes.md](references/scenes.md) for UI elements (buttons, sliders, text inputs), scene properties, and element actions.
- **Advanced Features**: See [advanced.md](references/advanced.md) for JavaScriptlets, Java Object creation, Android Intents, Midi control, and Power management.

## Tasker Development Workflow

When designing a Tasker automation, follow this workflow:

1. **Identify the Trigger**: Determine if the trigger is a State (e.g., connected to a specific Wi-Fi) or an Event (e.g., receiving an SMS).
2. **Design the Task**: List the actions needed. If stateful, decide if you need an Exit Task to revert settings when the state changes.
3. **Use Local Variables**: Keep intermediate states in local (all-lowercase) variables to prevent global namespace pollution.
4. **Error Handling**: Use the `%err` and `%errmsg` local variables after actions that might fail (e.g., HTTP request, file read) to gracefully handle failures.

## Scripting in Tasker

### JavaScript / JavaScriptlet Action
You can execute JavaScript within a task. In JavaScriptlets:
- Access local/global Tasker variables directly by name without the `%` (e.g., `local` variables as `localvar` and `global` as `GLOBALVAR`).
- Use `setLocal('varname', value)` to set local variables.
- Use `setGlobal('VARNAME', value)` to set global variables.
- Example:
  ```javascript
  var battery = global('BATT');
  if (battery < 20) {
      setLocal('low_power', 'true');
  }
  ```

### Shell Commands
Run shell commands via the `Run Shell` action.
- Ensure "Use Root" is checked only if root permissions are required.
- Store output in `%stdout` and errors in `%stderr`.

### Android Intents
Send broadcast, activity, or service intents using the `Send Intent` action.
- **Action**: The intent action (e.g., `android.intent.action.VIEW`).
- **Cat**: Category (e.g., `Default`).
- **Data**: Data URI (e.g., `https://example.com`).
- **Extra**: Key-value extras (e.g., `key:value`).

## Exporting & Importing Configurations

Tasker is highly sensitive to the structure of exported XML configurations.

### File Extensions
For Tasker to recognize the XML data during an import, files must end with specific double extensions:
- **Projects**: `.prj.xml`
- **Profiles**: `.prf.xml`
- **Tasks**: `.tsk.xml`
- **Scenes**: `.scn.xml`

### XML Root Structure
Tasker requires files to start directly with the `<TaskerData>` root tag. Including standard XML headers (like `<?xml version="1.0" encoding="utf-8"?>`) or other root wrappers will fail to parse and trigger errors.

### Matching Import Actions with UI Elements
Tasker's UI contains isolated import functions. Selecting a file that doesn't match the import context will trigger errors (e.g., "no Project found"):
- **Importing a Project**: Long-press on the Project/Home tab at the bottom of the screen and choose **Import Project**.
- **Importing a Profile/Task/Scene**: Tap the corresponding tab at the top, long-press the tab label, and choose **Import**.

