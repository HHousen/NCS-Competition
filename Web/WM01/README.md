# WM01 - 250pts

## Briefing

> View the page at <https://cfta-wm01.allyourbases.co> and try to get the flag.

## Solution

1. When looking around for interesting files we can find an interesting comment in `/assets/js/site.js` that says `// Image slideshow. Moved in from /new-images when each is finalised`.

2. Navigating to `/new-images` shows a list of pictures. Checking each picture to see if the flag is hidden using steganography tricks yields nothing.

3. It took a lot of different ideas but eventually I tried using Google's reverse image search to see if any of the images in `/new-images` were unique. The image of the macbook with the screen showing "mii-home" got some matches, but none of them had the "mii-home" graphic. Going to `/mii-home` shows a login page.

4. The username and password for the login page at `/mii-home` are validated using `login.js`. We can deobfuscate it with [de4js](https://lelinhtinh.github.io/de4js/) to get the output in [login.js](./login.js). We can run lines 1-18 in the JS console (only if not already on `/mii-home`) and then define j to hl_b with `j = hl_b`. Finally, simply run line 28: `window[j(0x73)] = 'se' + 'curi' + 'ty-' + 'ca' + j(0x7d) + '/f' + j(0x70);`. This will redirect to `/mii-home/security-camera/feed/`.

5. We can look at the "Office" camera to see a note that says the WiFi password is `XGHEV7HGEV`, which is the flag.

### Flag

`XGHEV7HGEV`
