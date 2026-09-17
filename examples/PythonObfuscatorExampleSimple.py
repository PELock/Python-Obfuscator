#!/usr/bin/env python

###############################################################################
#
# Python Obfuscator WebApi interface usage example.
#
# In this example we will obfuscate sample source with default options.
#
# Version        : v1.0.0
# Language       : Python
# Author         : Bartosz Wójcik
# Web page       : https://www.pelock.com
#
###############################################################################

#
# include Python Obfuscator module
#
from pythonobfuscator import PythonObfuscator

#
# if you don't want to use Python module, you can import directly from the file
#
#from pelock.pythonobfuscator import PythonObfuscator

#
# create Python Obfuscator class instance (we are using our activation key)
#
myPythonObfuscator = PythonObfuscator("ABCD-ABCD-ABCD-ABCD")

#
# source code in Python format
#
scriptSourceCode = """label = 'SecretKey'
port = 443

def get_sum(a, b):
    return a + b

print(label, port)
r = get_sum(11, 31)
print(r)
"""

#
# by default all obfuscation options are enabled, so we can just simply call
#
result = myPythonObfuscator.obfuscate_script_source(scriptSourceCode)

#
# it's also possible to pass a Python script file path instead of a string with the source e.g.
#
# result = myPythonObfuscator.obfuscate_script_file("/path/to/project/script.py")

#
# result[] array holds the obfuscation results as well as other information
#
# result["error"]         - error code
# result["output"]        - obfuscated code
# result["demo"]          - demo mode (empty/invalid key); strategy flags ignored; always integers_to_arrays, mba_binops, encrypt_strings (no virt; 1000 char limit)
# result["license_expiration"] - license end date (Y-m-d), empty if none
# result["usages_total"]  - total obfuscations for this activation code
#
if result and "error" in result:

    # display obfuscated code
    if result["error"] == PythonObfuscator.ERROR_SUCCESS:

        # format output code for HTML display
        print(result["output"])

    else:
        print(f'An error occurred, error code: {result["error"]}')

else:
    print("Something unexpected happen while trying to obfuscate the code.")
