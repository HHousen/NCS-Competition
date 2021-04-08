# WM02 - 250pts

## Briefing

> View the page at <https://cfta-wm02.allyourbases.co> and try to get the flag.

## Solution

1. Looking at the source code we see an `h1` tag with data attributes: `<h1 id="user" data-user-name="henrywhite" data-user-id="152874" data-user-ref="c897cd08c105c0eff5ca296f56eaa4ab">Hello henrywhite!</h1>`

2. Changing the `data-user-name` to `admin` changes the text to `User data error`.

3. Looking at `/site.js` we see that `checkUser()` is called every second using `setInterval` at the bottom of the file. The following `if` statement contains the logic we can take advantage of: `if (get("user").dataset['userRef'] === hash(get("user").dataset['userName'] + "_" + get("user").dataset['userId']).split("").reverse().join("")) {`. We can change the `data-user-name` to `admin` and then run `hash(document.getElementById("user").dataset['userName'] + "_" + document.getElementById("user").dataset['userId']).split("").reverse().join("")` to get the `data-user-ref` to be `1dc3b8bdbf88d16df8a767eacb86f14c`. However, pasting this in causes the site to say `Invalid user`.

4. The solution is to also change `data-user-id` so it equals `"0"`. The final HTML should look this this: `<h1 id="user" data-user-id="0" data-user-name="admin" data-user-ref="31f7934415f3d31c64359bd51d378177">Hello admin!</h1>` You can get the `data-user-ref` after changing `data-user-id="0" data-user-name="admin"` and then running `hash(document.getElementById("user").dataset['userName'] + "_" + document.getElementById("user").dataset['userId']).split("").reverse().join("")`.

5. Replacing the HTML as discussed above prints the flag.

### Flag

`epoch_wizard`
