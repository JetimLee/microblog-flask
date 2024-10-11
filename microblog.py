import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

# With a regular interpreter session, the app symbol is not known unless it is
# explicitly imported, but when using flask shell, the command pre-imports the application instance, and pushes its application context for you.
# The nice thing about flask shell is not only that it pre-imports app,
# but that you can also configure a "shell context", which is a list of other symbols to pre-import.

# The following function in microblog.py creates a shell context that adds the database instance and models to the shell session:

# The app.shell_context_processor decorator registers the function as a shell context function.
# When the flask shell command runs, it will invoke this function and register the items returned by it in the shell session.
# The reason the function returns a dictionary and not a list is that for each item you have to also provide a name under which it will be referenced in the shell,
#    which is given by the dictionary keys.

# After you add the shell context processor function you can work with database entities without having to import them:


# Run flask shell
@app.shell_context_processor
def make_shell_context():
    return {"sa": sa, "so": so, "db": db, "User": User, "Post": Post}


# Need to use export FLASK_APP=microblog (the main file) for this to work in dev
