[Previous](exercise-4.md) |  [Next](exercise-6.md)
### Step 5: Using an OAuth2 based API
Now let's experiment with using an OAuth2 based API.  I'm not going to lie to
you, using OAuth2 is painful, but it allows something valuable: allowing
a given application limited access to a user's account in another application
without having access to that user's credentials.

OAuth2 can be so painful to implement directly that API providers like Box, 
Google, etc are developing SDKs - software development kits - to ease the 
pain. 

These SDKs (perhaps as a side effect) also provide a facade interface to their 
APIs.  There are upsides and downsides to this:
* Upside: Easier to use.
* Downside: You have to become familiar with individual SDKs rather than relying 
on the common RESTful HTTP interfaces.  Becoming conversant on this level takes 
more work but makes it possible for you to interact with almost any web API.

#### Box API Setup
I couldn't think of a way to not make everyones head explode doing OAuth2 
directly so we'll be using the Box SDK which allows use to interact with the Box 
API in class today.

When using SDKs, you have to become familiar with the [documentation](https://github.com/box/box-python-sdk).

1. You'll need to upgrade your Box account to a developer account in order to use
their API.  You can do so by simple [registering your intent to create an 
application](https://www.box.com/developers/services).  I **think** that you 
can use your ND account if you want, but I suggest that you create separate 
new account so that you keep your ND account nice and safe.

1. When registering your new application, you'll need to pick up a "developer
token" in order to authenticate with OAuth2.  Make sure to talk through about
how this is really a short-circuit version of OAuth2 for convenience.

1. Install the Box SDK into your Python environment by running 
`pip install -r requirements.txt` from inside the 
`/vagrant/trainee-area/level-2/using-web-services` directory.