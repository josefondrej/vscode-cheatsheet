# VS Code Cheatsheet

## Inspired By

- [Fireship: 25 VS Code Productivity Tips and Speed Hacks](https://youtu.be/ifTF3ags0XI?feature=shared)

## Project & Files

Open a project in VSCode

```bash
code /path/to/project/directory
```

## Useful Shortcuts

To list all the shortcuts use `Ctrl + K, Ctrl + S`
Alternatively for the default values see [windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
or [linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf) cheatsheets online.

| Shortcut                                                          | What it does                                                                   |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `Ctrl + 1`                                                        | Focus Editor                                                                   |
| `Ctrl + Shift + I`                                                | Format Document                                                                |
| `Ctrl + P`                                                        | Go to File                                                                     |
| `Ctrl + P` + `>` / `Ctrl + Shift + P`                             | Show All Commands                                                              |
| `Ctrl + P` + `@` / `Ctrl + Shift + O` / `Ctrl + Shift + .`        | Go to Symbol in Editor                                                         |
| `Ctrl + P` + `#`  / `Ctrl + T`                                    | Go to Symbol in Workspace (for a class called MyAwesomeClass you can type MAC) |
| `Ctrl + P` + `:` / `Ctrl + G`                                     | Go to Line / Column                                                            |
| `Ctrl + -/+`                                                      | Zoom in / out                                                                  |
| `Ctrl + D`                                                        | Highlite All Occurences                                                        |
| `Ctrl + D` / `Alt + Left Click` / `Alt + Shift + Arrow Up / Down` | Multi Cursor                                                                   |
| `Ctrl + W`                                                        | Close Tab                                                                      |
| `Ctrl + X`                                                        | Cut Current Line                                                               |
| `Alt + Arrow Up / Down`                                           | Move Current Line Up / Down                                                    |
| `Ctrl + L`                                                        | Select Current Line                                                            |
| `Ctrl + /`                                                        | Un/Comment Selected Code                                                       |
| `Ctrl + Shift + 5`                                                | Split Terminal                                                                 |
| `Shift + Alt + .`                                                 | Quick Fix                                                                      |
| `Ctrl + K + J`                                                    | Expand All Lines of Code                                                       |
| `Ctrl + K + 1/2/...`                                              | Fold Code at Level n                                                           |
| `Ctrl + ,`                                                        | Search Settings                                                                |
| `Alt + Z`                                                         | Toggle Word Wrap                                                               |
| `Ctrl + Shift + Insert`                                           | Insert a New File                                                              |
| `Ctrl + Shift + V`                                                | Preview Markdown                                                               |
| `Ctrl + K` + `Ctrl + Page Up / Down`                              | Open Next / Previous Editor in Group                                           |
| ``Ctrl + ` ``  / `Ctrl + J`                                       | Open Terminal                                                                  |
| ``Ctrl + Shift + ` ``                                             | New Terminal                                                                   |

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

## Useful Plugins

- `Remote Developement` - to connect to a remote server / to use a Docker container as your dev environment etc.
- `Black Formatter` - format Python code
- `isort` - import sorting for Python
- `Git History` / `GitLens` - see the Git section
- `Remote Repositories` - see the Git section

## Custom Snippets

- To configure new snippet use: `Ctrl + Shift + P` > `Configure User Snippets`
- To insert snippet `Ctrl + Shift + P` > `Insert Snippet`
- Often snippets can be installed as extensions

## Code Formatting

- To format document use: `Ctrl + Shift + I`
- To configure multiple formatters, use the [Multiple Formatters](https://marketplace.visualstudio.com/items?itemName=Jota0222.multi-formatter) extension

## Useful Commands Not Bound to Any Shortcut or with a Difficult Shortcut

| Command                     |
|-----------------------------|
| Git                         |
| Git: Commit                 |
| Git: Push                   |
| Git: Revert Selected Ranges |
| Git: Pull Rebase            |
| Git: Show History           |
| Left / Right Tab            |
| File: New Folder            |

## Workspaces

Workspace = collection of 1 or more folders opened in VS Code.

- For 1 folder you don't have to do anything (just open it in VS Code)
- For more folders you need to create `<name>.code-workspace` file that lists the folders of the workspace

## Config Files

There are 2 levels at which various settings of the IDE can be configured:

- User Settings
- Workspace Settings

To modify the settings: `Ctrl + Shift + P` > `Preferences: Open User/Workspace Settings`

The settings can be viewed in UI or as a `settings.json` file that lives under `.vscode` in case of the workspace settings and
in the `~/.config/Code/User` in case of the user settings.

## TODO

### General Settings

- What is and how to use `settings.json` (and should you version control this? -- settings.json, launch.json, tasks.json yes but the rest in .vscode no)
- What is and how to use `*.code-workspace`
- How to persist project settings (like wrapping lines in editor)
- User vs Project settings

### Python Specific

- Rename a variable / class / function
- Move a variable / class / function
- Find all usages of class / function
- Python: Optimize imports
- Python: Format code
- Show Options (in code)
- Debugging
- Execute code in console
