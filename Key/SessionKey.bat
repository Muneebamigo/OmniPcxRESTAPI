@echo off
echo Running SessionKey.py...
python SessionKey.py

echo Running siteSession.py...
python siteSession.py

echo Running siteSession.py again...
python siteSessionUser.py

echo Running UserSession.py...
python UserSession.py

echo All files executed successfully.
pause