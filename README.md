# VS Code Cheatsheet

A brief overview of how I personally have my Visual Studio Code set up and how I use it.
Serves also as a quick cheatsheet.
Work in progress.

## IDE Customization

### Profiles

VSCode supports customization using so called profiles. You can create new one by `Ctrl + Shift + P` > `Profiles: Create Profile ...`
and customize different aspects of the IDE in this profile including IDE settings, keyboard shortcuts, user snippets, user tasks etc.

The profiles can be [synced to cloud](https://code.visualstudio.com/docs/editor/settings-sync) or exported / imported as e.g. GitHub gist.

### Workspaces

VSCode Workspace is a collection of 1 or more folders opened in VS Code.

- For 1 folder you don't have to do anything (just open it in VS Code and this is workspace)
- For more folders you need to create `<name>.code-workspace` file that lists the folders of the workspace

It can be useful to set workspace file (or more) also for a single folder as different workspace files can
give different "views" on the folder

#### Working with Multiple Python Projects

- Specify the paths to the projects in the `.code-workspace` file
- To include the dependent package(s) either
  - use `pip install -e .`
  - or specify the environment variable PYTHONPATH in the launch configs in the workspace settings
  - of course the previous 2 options only make sense when you want to modify the projects on which the main project depends

### IDE Settings

The IDE Settings control e.g. what code formatter should be used. Font size and type in editor etc.
There are 2 levels at which various settings of the IDE can be configured:

- User (=part of the profile) Settings (lives in e.g. `C:/Users/<username>/AppData/Roaming/Code/User/profiles/<profile>/settings.json`)
- Workspace Settings (lives in project dir `.vscode/settings.json`)

The `settings.json` files can be viewed as raw JSON or there is a UI that VSCode provides for conveniently viewing them.
To modify the settings (in UI): `Ctrl + ,`
The settings can also be specified in the `.code-workspace` file

#### Editor Appearance

- Install on your OS the [JetBrains Mono Font](https://www.jetbrains.com/lp/mono/) and set the `Editor > Font Family` to `'Jetbrains Mono', Consolas, 'Courier New', monospace`
- Nice color themes are e.g. [Atom One Light](https://marketplace.visualstudio.com/items?itemName=akamud.vscode-theme-onelight) or the [GitHub Themes](https://marketplace.visualstudio.com/items?itemName=GitHub.github-vscode-theme)

### Tasks

- Some predefined jobs - for example some build
- Like IDE Settings can also be User or Workspace specific
- To create a task: `Ctrl + Shift + P` > `Configure Task`
- To run it: `Ctrl + Shift + P` > `Run Task`

### Snippets

- Like IDE Settings can also be User or Workspace specific
- To configure new snippet use: `Ctrl + Shift + P` > `Configure User Snippets`
- To insert snippet `Ctrl + Shift + P` > `Insert Snippet`
- Often snippets can be installed as extensions

## Launch Configurations

You can specify how a Python (or other) program will be launched using launch configurations.
They are specified in `.vscode/launch.json` file and can contain e.g. environment variables to use for the run.

## Useful Keyboard Shortcuts

To open a project in VS Code, in terminal type `code /path/to/your/project`

To list all the shortcuts use `Ctrl + K, Ctrl + S`

Alternatively for the default values see [windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
or [linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf) cheatsheets online.

| Shortcut Windows                                    | What it does                                                                   |
|-----------------------------------------------------|--------------------------------------------------------------------------------|
| **File Navigation**                                 |                                                                                |
| `Ctrl + Shift + E`                                  | Open File Explorer                                                             |
| `Ctrl + 1`                                          | Focus Editor                                                                   |
| `Ctrl + P`                                          | Go to File                                                                     |
| `Ctrl + Shift + P`                                  | Show All Commands                                                              |
| `Ctrl + Shift + O` / `Ctrl + Shift + .`             | Go to Symbol in Editor                                                         |
| `Ctrl + T`                                          | Go to Symbol in Workspace (for a class called MyAwesomeClass you can type MAC) |
| `Ctrl + G`                                          | Go to Line / Column                                                            |
| `Ctrl + -/+`                                        | Zoom in / out                                                                  |
| `Ctrl + W`                                          | Close Tab                                                                      |
| `Ctrl + Shift + Insert`                             | Insert a New File                                                              |
| `Ctrl + Page Up / Down`                             | Open Next / Previous Editor in Group                                           |
| `Ctrl + Shift + F`                                  | Search In Files                                                                |
| &nbsp;                                              |                                                                                |
| **Code Navigation**                                 |                                                                                |
| `Ctrl + D`                                          | Highlight All Occurrences                                                      |
| `Ctrl + K + J`                                      | Expand All Lines of Code                                                       |
| `Ctrl + K + 0`                                      | Fold All Lines of Code                                                         |
| `Ctrl + Shift + ]`                                  | Unfold (Current Line)                                                          |
| `Alt + Z`                                           | Toggle Word Wrap                                                               |
| `F12`                                               | Go to Definition / Show Implementations                                        |
| `Alt + Right / Left Arrow`                          | Navigate Forward / Backward                                                    |
| `Ctrl + Space`                                      | Show Docstring                                                                 |
| `Ctrl + Shift + M`                                  | Show Problems in the Current File                                              |
| `Ctrl + F`                                          | Find in File                                                                   |
| `Ctrl + H`                                          | Replace in File                                                                |
| &nbsp;                                              |                                                                                |
| **Git**                                             |                                                                                |
| `Ctrl + Shift + G` + `G`                            | Open Git                                                                       |
| &nbsp;                                              |                                                                                |
| **Formatting / Refactoring**                        |                                                                                |
| `Alt + Shift + F`                                   | Format Document                                                                |
| `Alt + Shift + O`                                   | Optimize Imports                                                               |
| `Alt + Left Click` / `Alt + Ctrl + Arrow Up / Down` | Multi Cursor                                                                   |
| `Ctrl + X`                                          | Cut Current Line                                                               |
| `Alt + Arrow Up / Down`                             | Move Current Line Up / Down                                                    |
| `Ctrl + L`                                          | Select Current Line                                                            |
| `Ctrl + /`                                          | Un/Comment Selected Code                                                       |
| `Ctrl + .`                                          | Quick Fix                                                                      |
| `F8`                                                | Show Problems                                                                  |
| `F2`                                                | Rename function / class / object                                               |
| &nbsp;                                              |                                                                                |
| **Terminal**                                        |                                                                                |
| `Ctrl + Shift + backtick`                           | New Terminal                                                                   |
| `Ctrl + backtick` / `Ctrl + J`                      | Open Terminal                                                                  |
| `Ctrl + Shift + 5`                                  | Split Terminal                                                                 |
| &nbsp;                                              |                                                                                |
| **Settings**                                        |                                                                                |
| `Ctrl + ,`                                          | Search Settings                                                                |
| &nbsp;                                              |                                                                                |
| **Run and Debug**                                   |                                                                                |
| `Ctrl + Shift + D`                                  | Open Run and Debug Menu                                                        |
| `Ctrl + F5`                                         | Run                                                                            |
| `Shift + F5`                                        | Stop                                                                           |
| `F5`                                                | Debug                                                                          |
| `Shift + F9`                                        | Set Line Breakpoint                                                            |
| `F9`                                                | Remove Line Breakpoint                                                         |
| `Shift + Enter`                                     | Execute Selection in Console                                                   |
| `F10`                                               | Debugger: Step Over                                                            |
| &nbsp;                                              |                                                                                |
| **Other**                                           |                                                                                |
| `Ctrl + Shift + V`                                  | Preview Markdown                                                               |
| `Ctrl + Shift + X`                                  | Extensions                                                                     |

### Useful Commands without a (reasonable) Shortcut

| Command                                | My Custom Shortcut Windows | Note                                                         |
|----------------------------------------|----------------------------|--------------------------------------------------------------|
| Git                                    | `Ctrl + Shift + G`         | Need to remove the GitLens override                          |
| Git: Commit                            | `Ctrl + Shift + G`         | Need to remove the GitLens override                          |
| Git: Push                              | `Ctrl + Alt + P`           | User Defined                                                 |
| Git: Revert Selected Ranges            | `Ctrl + Alt + Z`           | User Defined (remove when expression)                        |
| Git: Stage All Changes                 | `Ctrl + Alt + A`           | Usef Defined                                                 |
| Git: Show History                      | `Alt + 9`                  | Usef Defined                                                 |
| Git: Pull Rebase                       |                            |                                                              |
| File: New Folder                       |                            |                                                              |
| Python Remove Unused Imports = Fix All | `Ctrl + S`                 | With the Ruff extension and onSave set as in `settings.json` |
| Re-run Last Run Config                 |                            |                                                              |
| Stage File Partially                   |                            |                                                              |
| File Name Autocomplete in Commit Msg   |                            |                                                              |
| Evaluate in Debug Console              | `Ctrl + Alt + E`           | User Defined                                                 |

## Plugins

### Python

- `Python`
- `Pylance` - auto imports for Python (and much more)
- `Jupyter` - Jupyter notebook support
- `Test Explorer UI` - Prettier tests
- `Ruff` - Linting, formatting and import sorting, faster (see `.vscode/settings.json` for examples)
- `Mypy Type Checker` - Type checking for Python files
- `Python Environment Manager` - Manage Python environments
- ~~`Black Formatter` - Format Python code - replaced by Ruff~~
- ~~`isort` - Import sorting for Python - replaced by Ruff~~
- ~~`Flake8` - Linting support for Python - replaced by Ruff~~

### Docker

- `Docker`
- `Remote Development` - Connect to a remote server / to use a Docker container as your dev environment

### Git

- `Git Graph` - View commit history
- `GitLens` - More advanced git features, paid
- `Gitignore` - default .gitignore templates for different languages / IDEs
- ~~`Remote Repositories`~~

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
- `Markdown Table Prettifier` - Prettify Markdown tables

### Other

- `Local History` - Tracking of local history of files (similar functionality is already built in in the TIMELINE tab in explorer), might be useful to include `**/.history` into your `Files: Exclude` and `Search: Exclude` settings
- `HTML CSS Support` - CSS Intellisense for HTML
- `Path Intellisense` - Autocompletion for paths
- `Scratchpads` - Create new scratch files
- ~~`Edit csv` - Editing of CSV files~~
  
## Python

### Different Ways to Run / Debug Python Files

- You can debug / run Python file using the launch configurations using `F5` / `Ctrl + F5`
  - For a useful python launch config see `.vscode/launch.json`
  - In debug mode you can also evaluate in console
- You can run the Python file in terminal (small triangle in the top right of UI) without any settings
- Run selection in terminal using `Shift + Enter`
- Set / unset breakpoints using `F9` / `Shift + F9`

### Python Code Formatting

- To format document use: `Ctrl + Shift + F`, to organize import `Ctrl + Shift + O`
- It is a good idea to set the auto-format and auto-organize imports on save (see `settings.json`)
- **Formatting & Linting & Import sorting**: [Ruff](https://github.com/astral-sh/ruff) - formatter actually formats the code, linter just shows where the problem is, historically established formatter was [Black](https://github.com/psf/black), established linter [Flake8](https://github.com/PyCQA/flake8) and for import sorting there was [isort](https://pycqa.github.io/isort/), but Ruff aims to replace them all (and as far as I can tell does it pretty well). For examples on how Black and Flake8 can be configured see `pyproject.toml` resp. `.flake8` files
- **Type Checker**: [Mypy](https://github.com/python/mypy) - checks that typing annotations are correct
- All the above mentioned tools are available as VSCode plugins (from Microsoft directly)
  - to use them, you can set the Editor > Format on Save setting (see `.vscode/settings.json` for example)
- Alternatively, a good idea for the formatting and also linting could be to set a pre-commit hook for them
  - a great tool to do this is [pre-commit](https://pre-commit.ci/)
  - it has support for [black](https://black.readthedocs.io/en/stable/integrations/source_version_control.html), [isort](https://pycqa.github.io/isort/docs/configuration/pre-commit.html), [flake8](https://flake8.pycqa.org/en/latest/user/using-hooks.html), [mypy](https://github.com/pre-commit/mirrors-mypy)
- To configure black use `pyproject.toml`, this unfortunately does not work with flake8, for that you need to use the `.flake8` file
- Of course all of these tools (in particular makes sense for flake8 and mypy) can be added also to CI

## Terminal

- To start the terminal press ``Ctrl + ` ``
- You can change color / name of the terminal window
- It can be useful to set [your custom terminal profile](https://code.visualstudio.com/docs/terminal/profiles) using for example the setting `terminal.integrated.profiles.windows`

## Unresolved TODOs

- [x] Auto stage changes in already staged files - since [staged changes do not show up in diff](https://stackoverflow.com/questions/48881124/can-i-make-visual-studio-code-highlight-staged-changes), this would probably mean more complex fiddling with the settings - now I set up hotkey for stage all, which makes this less of a pain point

## TODO

- [ ] Push current branch to arbitrary remote branch
- [ ] Display the external libraries in explorer view similar to PyCharm
  - it sort of works with Python extension installed, but the structure of the libraries doesn't show up, it just opens in explorer as a single file
  - there is [not exactly a huge effort](https://github.com/microsoft/vscode-python/issues/15018) from VSCode dev team to get this working
- [ ] Get VSCode working with [unclean git repo](https://stackoverflow.com/questions/51817479/vscode-please-clean-your-repository-working-tree-before-checkout)
- [ ] More specific instructions on how to configure User / Profile and Workspace tasks
- [ ] Show there is a search result or git diff even for folded code
- [ ] Convince Pylance to index all directories in workspace with multiple directories

