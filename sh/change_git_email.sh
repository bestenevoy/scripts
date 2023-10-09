#!/bin/sh
# 更改 git email

git filter-branch --env-filter '

OLD_EMAIL="old_email"
CORRECT_NAME="new_name"
CORRECT_EMAIL="new_email@gmail.com"

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags

# 失败
# git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch Rakefile' HEAD

# 成功
# git push origin --force --all