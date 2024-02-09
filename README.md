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
| `Ctrl + D`                                                        | Highlight All Occurrences                                                      |
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

| Command                              | Shortcut                  | Note                                |
|--------------------------------------|---------------------------|-------------------------------------|
| Git                                  | Ctrl + Shift + G          | Need to remove the GitLens override |
| Git: Commit                          | Ctrl + Shift + G          | Need to remove the GitLens override |
| Git: Push                            | Ctrl + Alt + P            | User Defined                        |
| Git: Revert Selected Ranges          | Ctrl + Alt + Z            | User Defined                        |
| Git: Pull Rebase                     |                           |                                     |
| Git: Stage All Changes               | Ctrl + Alt + A            | Usef Defined                        |
| Git: Show History                    | Alt + 9                   | Usef Defined                        |
| Left / Right Tab                     | Ctrl + Fn + Arrow Up/Down |                                     |
| File: New Folder                     |                           |                                     |
| Python Remove Unused Imports         | Alt + Shift + O           | With the Ruff extension             |
| Re-run Last Run Config               |                           |                                     |
| Stage File Partially                 |                           |                                     |
| File Name Autocomplete in Commit Msg |                           |                                     |

## Useful Plugins

### Python

- `Python`
- `Jupyter` - Jupyter notebook support
- `Test Explorer UI` - Prettier tests
- `Ruff` - Linting, formatting and import sorting, faster (see `.vscode/settings.json` for examples)
- `Mypy Type Checker` - Type checking for Python files
- `Python Environment Manager` - Manage Python environments
- ~~`Black Formatter` - Format Python code~~
- ~~`isort` - Import sorting for Python~~
- ~~`Flake8` - Linting support for Python~~

### Docker

- `Docker`
- `Remote Development` - Connect to a remote server / to use a Docker container as your dev environment etc.

### Git

- `Git Graph` - View commit history
- `GitLens` - More advanced git features, paid
- `Remote Repositories` - See the Git section

### Databases

- `SQLTools` - Working with relational databases (+ `SQLTools PostgreSQL/Cockroach Driver`, `SQLTools Oracle Driver`)
- `MongoDB for VS Code` - Connect to MongoDB Atlas

### Code style

- `GitHub Copilot` - AI Autocompletion
- `autoDocstring` - Generate docstrings

- `Code Spell Checker` - Spelling checker for code
- `CodeSnap` - Beautiful screenshots of code

### Markdown

- `Markdown All in One` - Tools for writing Markdown
- `markdownlint` - Markdown linter

### Other

- `Local History` - Tracking of local history of files (similar functionality is already built in in the TIMELINE tab in explorer)
- `HTML CSS Support` - CSS Intellisense for HTML
- `Path Intellisense` - Autocompletion for paths
- `Scratchpads` - Create new scratch files
- ~~`Edit csv` - Editing of CSV files~~
  
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

### Different Ways to Run/Debug Python Files

- You can debug / run Python file using the config using `F5` / `Ctrl + F5`
  - In debug mode you can also evaluate in console
- You can run the Python file in terminal (small triangle in the top right of UI) without any settings
- Run selection in terminal using `Shift + Enter`

## Terminal

- To start the terminal press ``Ctrl + ` ``
- You can change color / name of the terminal window

## Tasks

- To create a task: `Ctrl + Shift + P` > `Configure Default Build Task`
- To run it: `Ctrl + Shift + P` > `Run Task`

## Custom Snippets

- To configure new snippet use: `Ctrl + Shift + P` > `Configure User Snippets`
- To insert snippet `Ctrl + Shift + P` > `Insert Snippet`
- Often snippets can be installed as extensions

## Code Appearance

- To format document use: `Ctrl + Shift + I`
- **Formatter**: [Black](https://github.com/psf/black) - actually formats the code, [isort](https://pycqa.github.io/isort/) - organizes imports
- **Linter**: [Flake8](https://github.com/PyCQA/flake8) - formatter can't take care of everything, this checks more issues than the formatter handles but it can't fix them automatically, just shows where the problem is
- There is a tool called [Ruff](https://github.com/astral-sh/ruff) that can replace Black, isort and flake8
- **Type Checker**: [Mypy](https://github.com/python/mypy) - checks that typing annotations are correct
- All the above mentioned tools are available as VSCode plugins (from Microsoft directly)
  - to use them, you can set the Editor > Format on Save setting (see `.vscode/settings.json` for example)
- Alternatively, a good idea for the formatting and also linting could be to set a pre-commit hook for them
  - a great tool to do this is [pre-commit](https://pre-commit.ci/)
  - it has support for [black](https://black.readthedocs.io/en/stable/integrations/source_version_control.html), [isort](https://pycqa.github.io/isort/docs/configuration/pre-commit.html), [flake8](https://flake8.pycqa.org/en/latest/user/using-hooks.html), [mypy](https://github.com/pre-commit/mirrors-mypy)
- To configure black use `pyproject.toml`, this unfortunately does not work with flake8, for that you need to use the `.flake8` file
- Of course all of these tools (in particular makes sense for flake8 and mypy) can be added also to CI

## Working with Multiple Python Projects

- Use the `.code-workspace` file
- To include the dependent package either
  - use `pip install -e .`
  - or specify the environment variable PYTHONPATH in the launch configs in the workspace settings

## Unresolved TODOs

- [x] Auto stage changes in already staged files - since [staged changes do not show up in diff](https://stackoverflow.com/questions/48881124/can-i-make-visual-studio-code-highlight-staged-changes), this would probably mean more complex fiddling with the settings

## TODO

- [ ] How to activate conda env when opening new terminal (issue only on Windows)
- [ ] Windows hotkeys
- [ ] Display the external libraries in explorer view similar to PyCharm
  - it sort of works with Python extension installed, but the structure of the libraries doesn't show up, it just opens in explorer as a single file
  - there is [not exactly a huge effort](https://github.com/microsoft/vscode-python/issues/15018) from VSCode dev team to get this working
