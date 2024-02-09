# VS Code Cheatsheet

## Inspired By

- [Fireship: 25 VS Code Productivity Tips and Speed Hacks](https://youtu.be/ifTF3ags0XI?feature=shared)

## Settings Sync

Most of the settings can by [synced to cloud](https://code.visualstudio.com/docs/editor/settings-sync)

## Useful Shortcuts

To open a project in VS Code, in terminal type `code /path/to/your/project`

To list all the shortcuts use `Ctrl + K, Ctrl + S`
Alternatively for the default values see [windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
or [linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf) cheatsheets online.

| Shortcut                                                          | What it does                                                                   |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **File Navigation**                                               |                                                                                |
| `Ctrl + Shift + E`                                                | Open File Explorer                                                             |
| `Ctrl + 1`                                                        | Focus Editor                                                                   |
| `Ctrl + P`                                                        | Go to File                                                                     |
| `Ctrl + P` + `>` / `Ctrl + Shift + P`                             | Show All Commands                                                              |
| `Ctrl + P` + `@` / `Ctrl + Shift + O` / `Ctrl + Shift + .`        | Go to Symbol in Editor                                                         |
| `Ctrl + P` + `#`  / `Ctrl + T`                                    | Go to Symbol in Workspace (for a class called MyAwesomeClass you can type MAC) |
| `Ctrl + P` + `:` / `Ctrl + G`                                     | Go to Line / Column                                                            |
| `Ctrl + -/+`                                                      | Zoom in / out                                                                  |
| `Ctrl + W`                                                        | Close Tab                                                                      |
| `Ctrl + Shift + Insert`                                           | Insert a New File                                                              |
| `Ctrl + K` + `Ctrl + Page Up / Down`                              | Open Next / Previous Editor in Group                                           |
| &nbsp;                                                            |                                                                                |
| **Code Navigation**                                               |                                                                                |
| `Ctrl + D`                                                        | Highlite All Occurences                                                        |
| `Ctrl + K + J`                                                    | Expand All Lines of Code                                                       |
| `Ctrl + K + 1/2/...`                                              | Fold Code at Level n                                                           |
| `Alt + Z`                                                         | Toggle Word Wrap                                                               |
| `F12`                                                             | Go to Definition / Show Implementations                                        |
| `Ctrl + Shift + -` / `Ctrl + Alt + -`                             | Navigate Forward / Backward                                                    |
| `Ctrl + Space`                                                    | Show Docstring                                                                 |
| `Ctrl + Shift + M`                                                | Show Problems in the Current File                                              |
| &nbsp;                                                            |                                                                                |
| **Git**                                                           |                                                                                |
| `Ctrl + Shift + G` + `G`                                          | Open Git                                                                       |
| &nbsp;                                                            |                                                                                |
| **Formatting / Refactoring**                                      |                                                                                |
| `Ctrl + Shift + I`                                                | Format Document                                                                |
| `Alt + Shift + O`                                                 | Optimize Imports                                                               |
| `Ctrl + D` / `Alt + Left Click` / `Alt + Shift + Arrow Up / Down` | Multi Cursor                                                                   |
| `Ctrl + X`                                                        | Cut Current Line                                                               |
| `Alt + Arrow Up / Down`                                           | Move Current Line Up / Down                                                    |
| `Ctrl + L`                                                        | Select Current Line                                                            |
| `Ctrl + /`                                                        | Un/Comment Selected Code                                                       |
| `Shift + Alt + .`                                                 | Quick Fix                                                                      |
| `F8`                                                              | Show Problems                                                                  |
| `F2`                                                              | Rename function / class / object                                               |
| &nbsp;                                                            |                                                                                |
| **Terminal**                                                      |                                                                                |
| `Ctrl + Shift + 5`                                                | Split Terminal                                                                 |
| `Ctrl + backtick` / `Ctrl + J`                                    | Open Terminal                                                                  |
| `Ctrl + Shift + backtick`                                         | New Terminal                                                                   |
| &nbsp;                                                            |                                                                                |
| **Settings**                                                      |                                                                                |
| `Ctrl + ,`                                                        | Search Settings                                                                |
| &nbsp;                                                            |                                                                                |
| **Run and Debug**                                                 |                                                                                |
| `Ctrl + Shift + D`                                                | Open Run and Debug Menu                                                        |
| `Ctrl + F5`                                                       | Run                                                                            |
| `Shift + F5`                                                      | Stop                                                                           |
| `F5`                                                              | Debug                                                                          |
| `Shift + F9`                                                      | Set line breakpoint                                                            |
| `Ctrl + .`                                                        | Show Actions                                                                   |
| `Shift + Enter`                                                   | Execute Selection in Console                                                   |
| &nbsp;                                                            |                                                                                |
| **Other**                                                         |                                                                                |
| `Ctrl + Shift + V`                                                | Preview Markdown                                                               |
| `Ctrl + Shift + X`                                                | Extensions                                                                     |

### Useful Commands without a (reasonable) Shortcut

| Command                              |
|--------------------------------------|
| Git                                  |
| Git: Commit                          |
| Git: Push                            |
| Git: Revert Selected Ranges          |
| Git: Pull Rebase                     |
| Git: Show History                    |
| Left / Right Tab                     |
| File: New Folder                     |
| Git Stage                            |
| Python Remove Unused Imports         |
| Re-run Last Run Config               |
| Stage File Partially                 |
| File Name Autocomplete in Commit Msg |

## Useful Plugins

- `Remote Developement` - Connect to a remote server / to use a Docker container as your dev environment etc.
- `Black Formatter` - Format Python code
- `isort` - Import sorting for Python
- `Flake8` - Linting support for Python
- `Git History` / `GitLens` - See the Git section
- `Remote Repositories` - See the Git section
- `Mypy Type Checker` - Type checking for Python files
- `SQLTools` - Working with relational databases (+ `SQLTools PostgreSQL/Cockroach Driver`, `SQLTools Oracle Driver`)
- `GitHub Copilot` - AI Autocompletion
- `Better Comments`
- `autoDocstring`
- `CodeSnap` - Beautiful screenshots of code
- `Edit csv` - Editing of CSV files
- `Code Spell Checker` - Spelling checker for code
- `Git Graph` - View commit history
- `HTML CSS Support` - CSS Intellisense for HTML
- `Jupyter` - Jupyter notebook support
- `Markdown All in One`, `markdownlint` - Tools for writing Markdown
- `MongoDB for VS Code` - Connect to MongoDB Atlas
- `Path Intellisense` - Autocompletion for paths
- `Python Environment Manager` - Manage Python environments
- `Scratchpads` - Create new scratch files
- `Test Explorer UI` - Prettier tests
  
## Workspaces

Workspace = collection of 1 or more folders opened in VS Code.

- For 1 folder you don't have to do anything (just open it in VS Code)
- For more folders you need to create `<name>.code-workspace` file that lists the folders of the workspace

It can be useful to set workspace file (or more) also for a single folder as different workspace files can
give different "views" on the folder

## IDE Settings

There are 2 levels at which various settings of the IDE can be configured:

- User Settings
- Workspace Settings

To modify the settings: `Ctrl + Shift + P` > `Preferences: Open User/Workspace Settings`

The settings can be viewed in UI or as a `settings.json` file that lives under `.vscode` in case of the workspace settings and
in the `~/.config/Code/User` in case of the user settings.

## Launch Configurations

Are specified in `.vscode/launch.json` file

## Terminal

- To start the terminal press ``Ctrl + ` ``
- You can change color / name of the terminal window

## Tasks

- To create a task: `Ctrl + Shift + P` > `Configure Default Build Task`
- To run it: `Ctrl + Shift + P` > `Run Task`

## Git

- To open Git press `Shift + Ctrl + G` + `G`
- In the dropdown menu `...` we get a list of all possible Git commands
- `Git History`, `GitLens` extension is really useful
- `Remote Repositories` extension > Click the `><` button in the left bottom corner > Open Remote Repository

## Custom Snippets

- To configure new snippet use: `Ctrl + Shift + P` > `Configure User Snippets`
- To insert snippet `Ctrl + Shift + P` > `Insert Snippet`
- Often snippets can be installed as extensions

## Code Appearance

- To format document use: `Ctrl + Shift + I`
- **Formatter**: [Black](https://github.com/psf/black) - actually formats the code, [isort](https://pycqa.github.io/isort/) -- organizes imports
- **Linter**: [Flake8](https://github.com/PyCQA/flake8) - formatter can't take care of everything, this checks more issues than the formatter handles but it can't fix them automatically, just shows where the problem is
- **Type Checker**: [Mypy](https://github.com/python/mypy) - checks that typing annotations are correct
- All the above mentioned tools are available as VSCode plugins (from Microsoft directly)
  - to use them, you can set the Editor > Format on Save setting (see `.vscode/settings.json` for example)
- Alternatively, a good idea for the formatting and also linting could be to set a pre-commit hook for them
  - a great tool to do this is [pre-commit](https://pre-commit.ci/)
  - it has support for [black](https://black.readthedocs.io/en/stable/integrations/source_version_control.html), [isort](https://pycqa.github.io/isort/docs/configuration/pre-commit.html), [flake8](https://flake8.pycqa.org/en/latest/user/using-hooks.html), [mypy](https://github.com/pre-commit/mirrors-mypy)
- To configure black use `pyproject.toml`, this unfortunately does not work with flake8, for that you need to use the `.flake8` file
- Of course all of these tools (in particular makes sense for flake8 and mypy) can be added also to CI

## TODO

- [ ] How to remove unused imports in python
- [ ] Display the external libraries in explorer view similar to PyCharm
- [ ] Working with multiple workspaces -- what is the correct way to add them to pythonpath and use them?
  - one option is the pip install -e
- [ ] Local file history
- [ ] Revert current change (shortcut) / revert selected ranges
- [ ] Auto stage changes in already staged files
- [ ] What are the different options to run python file
- [ ] How to activate conda env when opening new terminal
- [ ] How to share IDE settings
