[Previous](exercise-02.md) |  [Next](exercise-04.md)
## Exercise 3: Obtain and Github API Token
[Code Files](../../training/level-3-interacting-with-web-services/bfp-reference/exercise_02)

To make calls to the GitHub API, you'll need someway for your application to 
let GitHub know that it can be trusted.
  
Github uses OAuth for authenticating API calls, which is the most popular 
method currently in use.  It is beyond the scope of our class to get into 
the details of how OAuth works so we will only present what is necessary to 
get our program to work.

### There Is No Secret Ingredient: Getting & Storing a GitHub OAuth Token
- Head to your [user settings page](https://github.com/settings/profile) in GitHub.
- Go to `Personal access tokens` and `Generate new token`.  You can accept 
the default settings as they can be adjusted later.
- Create a file in `/home/vagrant` called `tokens.json` and put your token in 
it like this:
    ```json
    {
        "github": "your_token_here"
    }
    ```
    
    > ![Extra Information](../images/information.png) Notice that we are 
    > putting this file outside our class directory structure.  We do this to
    > protect against accidentally adding confidential information like 
    > tokens/usernames/passwords to git and then sharing them with the world
    > via Github.   
    > 
    > **You must be ever vigilant about this.** IDEs are especially 
    > prone to adding new files in your project directories to git on your 
    > behalf in an attempt to be helpful.  You might not even know that your
    > credential file(s) have be added and upload until its too late.
    
### There Is No Secret Ingredient: Securely Accessing your GitHub Token
So now we've stored our token in a space place - away from all our other
code. Great.  How are we going to access it?
  
This is where the other package that we installed, `configuration-panda` 
comes into play (what an awesome name!). Here's how it works: 
- The package provides a `ConfigurationPanda` class.  
- When you instantiate(create) an object from that class, you pass it a list of 
previously set environment variables that point to locations where you have 
stored JSON configuration files.  
- It will then go and read those files and made the data inside of them 
available to you.  
    - Each JSON file will become an attribute on the 
    ConfigurationPanda object that holds of dictionary of the 
    JSON from the file.

Let's demonstrate how this works from the command line:
```shell
export PROGRAM_CREDENTIALS=/home/vagrant
```
    
- We create the `PROGRAM_CREDENTIALS` environment variable as a reference 
to the directory in which we've store our `tokens.json` file.

We can now do the following from a Python terminal session:
```python
from configuration_panda import ConfigurationPanda

credentials = ConfigurationPanda(['PROGRAM_CREDENTIALS'])

print(credentials.tokens)
{'github': 'whatever_your_token_was'}
```

- If they were multiple files in the directory referenced by
`PROGRAM_CREDENTIALS`, each one would be accessible just like 
`credentials.tokens` is here.
- Add the `import` and object instantiation statements to `github_api.py`
and you'll be ready to move on to the next exercise.

| [Next Exercise](exercise-04.md)