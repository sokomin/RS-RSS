@echo off
git pull origin main > log/exec.log

If not exist log mkdir log

python get_timestamp.py >> log/exec.log

git add timestamp.txt
git commit -m "[auto commit]timestamp updated."

rem "git push origin main"
git push origin main >> log/exec.log
