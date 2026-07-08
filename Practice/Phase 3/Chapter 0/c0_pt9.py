'''
Chapter0, topic - requirements.txt vs requirements-dev.txt
'''
'''
Task 1 (Easy): Create a blank folder workspace. Write a requirements.txt file 
containing requests==2.31.0. Then, create a requirements-dev.txt file and cleanly 
include the link pointer to the core file at the top.
'''
# DONE 
'''
Task 2 (Medium): Add a development tool named black==23.11.0 below the pointer inside 
your requirements-dev.txt file. Run a pip install -r requirements-dev.txt command in 
your terminal to see pip fetch both files in one go.
'''
# DONE 
'''
Task 3 (Hard): Run pip list to confirm everything is present. Then build a completely 
separate fresh environment (env_prod), activate it, and run only pip install -r 
requirements.txt to prove that the development tools (black) are successfully locked 
out of your production sandbox!
'''
# DONE 