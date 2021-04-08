# WH01 - 500pts

## Briefing

> Access the site at <https://cfta-wh01.allyourbases.co> and find a way to get the flag from the CMS.

## Solution

1. Since the website looks pretty empty we can try some directory busting: `gobuster dir -u https://cfta-wh01.allyourbases.co/ -t 200 --exclude-length 16 --extensions txt,html -w /usr/share/wordlists/dirb/common.txt`. We use the common `dirb` list included with Kali and also check for files with `txt` or `html` extensions.

    `gobuster` output:

    ```
    [+] Url:                     https://cfta-wh01.allyourbases.co/
    [+] Method:                  GET
    [+] Threads:                 200
    [+] Wordlist:                /usr/share/wordlists/dirb/common.txt
    [+] Negative Status codes:   404
    [+] Exclude Length:          16
    [+] User Agent:              gobuster/3.1.0
    [+] Extensions:              txt,html
    [+] Timeout:                 10s
    ===============================================================
    2021/04/08 19:43:11 Starting gobuster in directory enumeration mode
    ===============================================================
    /admin.html           (Status: 304) [Size: 0]
    /index.html           (Status: 200) [Size: 616]
    /index.html           (Status: 200) [Size: 616]
    /readme.txt           (Status: 200) [Size: 154]
    /soap                 (Status: 200) [Size: 0]  
                                                
    ===============================================================
    2021/04/08 19:43:23 Finished
    ===============================================================
    ```

2. We find an interesting `/admin.html` file, which is empty, and `/readme.txt`. `/readme.txt` says the following:

    ```
    To use the CMS make sure to visit /admin.html from allowed IPs on the local network.

    Note: Tell engineering to stop moving the subnet from 192.168.0.0/24
    ```

3. So, `/admin.html` only works when a request comes from an IP on the local network. It's possible that the service is simply checking the `X-Forwarded-For` HTTP header so let's try that.

4. We can use a Python [script](./script.py) to loop through every possible IP and make a get request with the `X-Forwarded-For` set to the IP that is currently being tested. If the length of the response is greater than 0, we print the response. This finds the flag after a few seconds.

### Flag

`iPSpooFinGWiThHopHeaDers91918`
