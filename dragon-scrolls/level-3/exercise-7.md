[Previous](exercise-6.md) |  [Next](exercise-8.md)
### Step 7: Create and Access a JSON Configuration File
It is a big no-no to put credentials directly into your source code.  Don't do 
it. **Ever.**  Not even when you're just testing something? **NEVER!**  

This is because it is very easy for such files to be imported 
into your Git repo and end up on a public website in Github. You should store
credentials in a separate file that you access from your program.  It is best 
to keep these files outside the Git directory entirely to prevent accidental 
inclusion but at a minimum you should modify your `.gitignore` file to keep 
such files from being added to the repo accidentally.

* Create file called `credentials.json` in `/vagrant/trainee-area/level-2/using-web-services`.
It should have the following content:

    ```json
    {
      "clientID": "[your box application client id]",
      "clientSecret": "[your box application client secret]",
      "developerToken": "[your box temporary developer token]"
    }
    ```

* Make the contents of this file accessible in your program by creating 
a `ConfigurationPanda()` object.

    ```python
    ...
    import boxsdk
    from configuration_panda import ConfigurationPanda
    
    program_settings = ConfigurationPanda()
    ...
    ```
    
* Run the program using iPython and see what happens: `ipython [your_id]_box_api.py`  

* You should get the following error from the 
`ConfigurationPanda` constructor: 

    ```
    configuration_panda.exceptions.InvalidParameter: The environment variable 
    specified by the client (CONFIGURATION_PANDA) for use by the constructor 
    does not exist on the system.
    ```
    
* Create an environment variable at the Vagrant command-line to specify the 
location of your configuration file: 
`export CONFIGURATION_PANDA=/vagrant/trainee-area/level-2/using-web-services`

* Run the program in interact mode an inspect the `program_settings` object to 
get familiar with how to interact with the `ConfigurationPanda()` object.