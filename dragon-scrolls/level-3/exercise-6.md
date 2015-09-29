[Previous](exercise-5.md) |  [Next](exercise-7.md)
### Step 6: Create Program Skeleton
* Create a new python file: `[your_id]_box_api.py`
* Add the required docstring and script execution structure.
* Import the following libraries: `boxsdk`, `configuration_panda`, and `json`.

    ```python
    """
    This module will interact with the Box API and demonstrate how to integrate
    with OAUTH2 based APIs - the current standard in Web Services.
    """
    import json
    
    import boxsdk
    from configuration_panda import ConfigurationPanda
    ```
    
* Talk about why two different forms of the `import` statement are being used
in this example.