# Solver for truth tables

This project contains solver for truth table with multiple output columns. Program for solving truth tables uses library `pyeda` and provides only easy input and output for markdown tables. If you're using [markdown preview enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/) (_or something, that can manage it_), you can generate LaTeX output in markdown table

## How to use it

Program have four arguments, where first two is obligatory and two others are optionals as is described below.

### Arguments

1. Argument is path to file.
2. Argument is last letter of input variables for truth tables.
3. This argument is first line of truth table. If is empty, is taken first line.
4. This argument is last line of truth table. If is empty, is taken last line of file.

### Flags
- `-t`, `--text` - Create text output. If is disabled, output will be in LaTeX.
- `-m`, `--minimized` - Create minimalised output. Can be combined with `-u` to take both.
- `-u`, `--unminimized` - Create unminimized output. Can be combined with `-m` to take both.
- `-p`, `--print` - Print output to terminal. Can be combined with `-a` create both outputs.
- `-a`, `--append` - Add output to file with table under ruth table. Can be combined with `-p` create both outputs.
- `-l`, `--lines` - Flag require number of lines between names of variables and first line of truth table. Default is 1.

### Conclusion note
If someone finds some optimalizations or improvements, feel free to create pull request or create issue with description of improvement. Same if some find bugh, please creaate issue, to I can fix it. I'll be happy for any feedback or tips.