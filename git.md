# Git Commands

> List of useful git commands in case I need to reference.

+ `git branch -a`
  - List all branches, including remote branches.

+ `git branch -D`
  - Force-delete a local branch.

+ `git checkout {branch-name} -- {file}`
  - Checkout a file from another branch into the current branch.

+ `git clean -d [-i|-f]`
  - Remove untracked files. `-n` for dry run. `-i` for interactively. `-f` for bulk removal.

+ `git remote prume origin`
  - Remove branches no longer being tracked upstream.

+ `git reset --hard`
  - Reset local directory to the last committed state. This will leave untracked files.

+ `git show {COMMIT}`
  - Show changes from a specific commit

+ `git stash --all`
  - Stash **ALL** files, even those in *.gitignore*.

+ `git stash --include-untracked`
  - Stash untracked files, but exclude files in *.gitignore*.

+ `git stash clear`
  - Drop all stashes.

+ `git stash drop`
  - Drop latest stash.
