# Fuzzy search (FZF) prompt. https://github.com/nk412/pyfzf.
import os
from pathlib import Path
from pyfzf.pyfzf import FzfPrompt
fzf = FzfPrompt()

# fetch all directories + show in fuzzy FZF search.
p = Path(".")
problem_dirs = [x for x in p.iterdir() if x.is_dir()
                and not x.name.startswith(".")]
print(problem_dirs)

# Pick 1 folder / problem to run.
selected = fzf.prompt(problem_dirs)
print(selected)
assert len(selected) == 1, f"Expected 1 selected, got {len(selected)}"
selected = selected[0]

# Run selected folder. Assume "main.py" + "input.in" exists.
inputFile = Path(".") / selected / "input.in"
pyFile = Path(".") / selected / "main.py"

assert inputFile.exists(), f"Input file {inputFile} does not exist"
assert pyFile.exists(), f"Python file {pyFile} does not exist"

# Run shell command
cmdStr = f"cat {inputFile} | python {pyFile}"
print(f"Running command: {cmdStr}")
os.system(cmdStr)
