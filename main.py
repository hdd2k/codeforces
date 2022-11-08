# Fuzzy search (FZF) prompt. https://github.com/nk412/pyfzf.
from pathlib import Path
from pyfzf.pyfzf import FzfPrompt
fzf = FzfPrompt()

# TODO: fetch all directories
p = Path(".")
problem_dirs = [x for x in p.iterdir() if x.is_dir()
                and not x.name.startswith(".")]
print(problem_dirs)

selected = fzf.prompt(problem_dirs)
print(selected)
