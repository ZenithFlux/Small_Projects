# Small Projects repository

All of my small programs will go here. No pull request will be accepted for this repository.

# Useful Git Commands

**1. git init -b main**

Initializes current folder as local git repository and adds default branch 'main'. 

**2. git remote add origin \<online repo link>**

Sets an online repo as origin of local one.

**3. git push -u origin main**

Sets 'main' branch as upstream branch and pushes all commited changes. It is required to use `git commit` before this command.

**4. git add --all**

Set all of the changes made in repository for commit.

**5. git commit -m 'message'**

Commit added files with this message. It is required to use `git add` before this command.

**6. git push**

If upstream branch is already set, push all commited changes in current branch to online repo.

**7. git clone \<repo link>**

Clone an online repo in the current folder.

**8. git pull**

Pull all changes from online repo to local one. It is required to commit all changes before this.

**9. git reset head\~n**

Move back by n commits. All commits in between are deleted. You can use commit code instead of 'head~n'.

**10. git revert head\~n**

Revert the changes done by nth last commit as a new commit. You can use commit code instead of 'head~n'.

**11. git log**

Shows log of all commits.

**12. git gc --aggressive --prune=now**

Reduce the size of repo by cleaning all garbage data.

## Branch commands

**12. git branch \<name>**

Create new branch

**13. git branch**

List all branches of current repository.

**14. git checkout \<branch>**

Switch branches

**15. git push --all**

Push all branches together

**16. git merge --squash \<branch>**

Copy last state of `<branch>` into current branch. Must be followed by `git commit` to commit the changes.

**17. git branch -d \<name>**

Delete branch locally.

# Miscellaneous

[Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/)