#!/usr/bin/env python

###############################################################################
#
# Python Obfuscator WebApi interface usage example.
#
# In this example we will verify our activation key status.
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
# login to the service
#
result = myPythonObfuscator.login()

#
# result[] array holds the information about the license
#
# result["demo"]          - demo mode (empty/invalid key); strategy flags ignored; always integers_to_arrays, mba_binops, encrypt_strings (no virt; 1000 char limit)
# result["license_expiration"] - license end date (Y-m-d), empty if none
# result["usages_total"]  - total obfuscations for this activation code
# result["string_limit"]  - max. source code size allowed (it's 1000 bytes for demo mode)
#
if result:

    print(f'Demo version status - {"True" if result["demo"] else "False"}')
    print(f'License expiration - {result.get("license_expiration")}')
    print(f'Total obfuscations - {result.get("usages_total")}')
    print(f'Max. source code size - {result["string_limit"]}')

else:
    print("Something unexpected happen while trying to login to the service.")
