# Import our entire file into this file

import hello

# Going to this location, and importing this thing from this file
from project_1.object_code.secret_file import secret
# If you need to import everything (bad practice)
from project_1.object_code.secret_file import *

print(hello.greeting("Dean"))

print(secret())