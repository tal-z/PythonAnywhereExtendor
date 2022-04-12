## About

This repo holds a module which automatically renews a PythonAnywhere project, 
so that I don't have to click the button every three months. It also renews itself, which is good.

## How It Works

Automation is powered by Python Selenium, running a headless chrome browser.

The module offers a really simple interface to navigate the browser, with a function for renewing tasks and a function for renewing web apps:

```python
# Renews a task (NOTE: only tested on accounts that have a single task configured.)
renew_task('user_varname', 'password_varname')

# Renews a webapp
renew_webapp('user_varname', 'password_varname')
```

Please note that the `'user_varname'` and `'password_varname'` referenced above refer to environment variable names. Pass in the names of environment variables, not the actual credentials to be used.