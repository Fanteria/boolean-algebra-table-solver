 # Solver for truth tables

This project contains a solver for a truth table with multiple output columns. Program for solving truth tables uses library `pyeda` and provides only easy input and output for markdown tables. If you're using [markdown preview enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/) (_or something, that can manage it_), you can generate LaTeX output in the markdown table

## How to use it

The program has four arguments, where the first two is obligatory and two others are optional as is described below.

### Arguments

1. Argument is a path to file.
2. Argument is the last letter of input variables for truth tables.
3. This argument is the first line of a truth table. If it is empty, is taken the first line.
4. This argument is the last line of a truth table. If it is empty, is taken the last line of the file.

### Flags
- `-t`, `--text` - Create text output. If is disabled, the output will be in LaTeX.
- `-m`, `--minimized` - This flag is default and creates minimalised output. Can be combined with `-u` to take both.
- `-u`, `--unminimized` - Create unminimized output. Can be combined with `-m` to take both.
- `-p`, `--print` - This flag is the default print output to the terminal. Can be combined with `-a` create both outputs.
- `-a`, `--append` - Add output to file with a table under ruth table. Can be combined with `-p` to create both outputs.
- `-l`, `--lines` - Flag require a number of lines between names of variables and the first line of a truth table. Default is 1.

### Conclusion note
If someone finds some optimizations or improvements, feel free to create a pull request or create an issue with a description of improvement. Same if some find bugs, please create an issue, so I can fix it. I'll be happy for any feedback or tips.