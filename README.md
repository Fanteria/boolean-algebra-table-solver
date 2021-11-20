 # Truth table solver

This project contains a solver for a truth tables with multiple output columns. The program for solving truth tables uses a library `pyeda` and provides input and output only for markdown tables. If you're using [markdown preview enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/) (_or something, that can manage LaTeX math_), you can generate LaTeX output in the markdown table.

## How to use it

The program has four arguments, where the first two are obligatory and the last two are optional as is described below.

### Arguments

1. A path to the input file.
2. The last letter of input variables for the truth table.
3. Nuber of the first line of the truth table. Default is the first line of the file.
4. The last line of the truth table. Default is the last line of the file.

### Flags
- `-t`, `--text` - If enabled, creates text style output. If disabled, the output will be in LaTeX. The default value is disabled.
- `-m`, `--minimized` - This flag minimizes the logic functions on the output. Can be combined with `-u` to output both. The default value is enabled.
- `-u`, `--unminimized` - Create unminimized output. Can be combined with `-m` to output both.The default is disabled.
- `-p`, `--print` - Print the output to the terminal. Can be combined with `-i` to create both outputs. The default is enabled.
- `-i`, `--insert` - Insert the result table after the last line specified in the 4th argument. Can be combined with `-p` to create both outputs. The default is disabled.
- `-l`, `--lines` - Defines the number of lines between the line with variable names and the first line of the truth table. If used, a value must be specified. The default value is 1.

### Conclusion note
If someone finds some optimizations or improvements, feel free to create a pull request or create an issue with a description of the improvement. Same if you find some bugs, please create an issue, so that I can fix them. I'll be happy for any feedback or tips.