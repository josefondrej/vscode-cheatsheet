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

| Shortcut                                                          | What it does                                                                   |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------|
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
| ``Ctrl + ` ``  / `Ctrl + J`                                       | Open Terminal                                                                  |
| ``Ctrl + Shift + ` ``                                             | New Terminal                                                                   |
| `Ctrl + Shift + 5`                                                | Split Terminal                                                                 |
| `Shift + Alt + .`                                                 | Quick Fix                                                                      |
| `Ctrl + K + J` | Expand All Lines of Code |
| `Ctrl + K + 1/2/...` | Fold Code at Level n |

## Terminal

- To start the terminal press ``Ctrl + ` ``
- You can change color / name of the terminal window

## Tasks

- To create a task: `Ctrl + Shift + P` > `Configure Default Build Task`
- To run it: `Ctrl + Shift + P` > `Run Task`

## Git

- To open Git press `Shift + Ctrl + G` + `G`
- In the dropdown menu `...` we get a list of all possible Git commands
- `GitLens` extension is really useful
- `Remote Repositories` extension > Click the `><` button in the left bottom corner > Open Remote Repository

## Useful Plugins

- `Remote Developement` - to connect to a remote server / to use a Docker container as your dev environment etc.
- `Black Formatter` - format Python code

## Custom Snippets

- To configure new snippet use: `Ctrl + Shift + P` > `Configure User Snippets`
- To insert snippet `Ctrl + Shift + P` > `Insert Snippet`
- Often snippets can be installed as extensions

## Code Formatting

- To format document use: `Ctrl + Shift + I`
- To configure multiple formatters, use the [Multiple Formatters](https://marketplace.visualstudio.com/items?itemName=Jota0222.multi-formatter) extension

## TODO

- New file at a location in explorer
- Move to left / right tab in editor
- What is and how to use `settings.json`
- What is and how to use `*.code-workspace`
- Rename a variable / class / function
- Move a variable / class / function
- Find all usages of class / function
- Python: Optimize imports
- Python: Format code
- Show Options ()
- How to persist project settings (like wrapping lines in editor)
