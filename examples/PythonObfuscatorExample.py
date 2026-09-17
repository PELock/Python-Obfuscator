#!/usr/bin/env python

###############################################################################
#
# Python Obfuscator WebApi interface usage example.
#
# In this example we will obfuscate sample source with every public option
# set, so you can see the full client surface and turn flags on or off.
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
from pythonobfuscator import CodeVirtualization, PythonObfuscator, RenameStyle

#
# if you don't want to use Python module, you can import directly from the file
#
#from pelock.pythonobfuscator import PythonObfuscator

#
# create Python Obfuscator class instance (we are using our activation key)
#
myPythonObfuscator = PythonObfuscator("ABCD-ABCD-ABCD-ABCD")

#
# should the source code be compressed (both input & compressed)
#
myPythonObfuscator.enable_compression = False

#
# globals
#
# fixed random seed for reproducible obfuscation output (optional)
#
myPythonObfuscator.seed = None

#
# randomization density / intensity (0-100)
#
myPythonObfuscator.randomization_density = None

#
# identifier renaming style: RenameStyle.IL, O0, CONFUSABLE, HEX, HOMOGLYPH, or MANGLED
#
myPythonObfuscator.rename_style = RenameStyle.IL

#
# code virtualization (exactly one): VM, FSA, or FLAT
# set to None to skip virtualization
#
myPythonObfuscator.code_virtualization = CodeVirtualization.VM

#
# protection (opt-in on the service for --all; shown enabled here so every flag is visible)
#
# protection against tampering with protected code (integrity verification)
#
myPythonObfuscator.self_defending = True

#
# protection linker (decoy call graph; requires self_defending)
#
myPythonObfuscator.protection_linker = True

#
# insert anti-debugging detections
#
myPythonObfuscator.detect_debugger = True

#
# insert virtual machine (anti-VM) detections
#
myPythonObfuscator.anti_vm = True

#
# insert anti-sandbox detections
#
myPythonObfuscator.anti_sandbox = True

#
# insert anti-emulators (CPU) detections
#
myPythonObfuscator.anti_emulator = True

#
# renaming
#
# rename variable names to random string values
#
myPythonObfuscator.rename_variables = True

#
# rename parameter names to random string values
#
myPythonObfuscator.rename_parameters = True

#
# rename function names to random string values
#
myPythonObfuscator.rename_functions = True

#
# rename function call references consistently with renamed functions
#
myPythonObfuscator.rename_function_calls = True

#
# shuffle function order in the output source
#
myPythonObfuscator.shuffle_functions = True

#
# fold/resolve constant expressions at obfuscation time
#
myPythonObfuscator.resolve_constants = True

#
# strings
#
# split strings into concatenated chunks
#
myPythonObfuscator.split_strings = True

#
# apply light transformations/mutations to string literals
#
myPythonObfuscator.modify_strings = True

#
# encrypt strings using randomly generated polymorphic encryption algorithms
#
myPythonObfuscator.encrypt_strings = True

#
# store string fragments in char-code array vaults
#
myPythonObfuscator.string_char_array_vault = True

#
# numeric
#
# encrypt integers
#
myPythonObfuscator.encrypt_integers = True

#
# encrypt floating point numbers
#
myPythonObfuscator.encrypt_floating = True

#
# replace binary operators with mixed boolean-arithmetic (MBA) equivalents
#
myPythonObfuscator.mba_binops = True

#
# represent integers via floating-point math
#
myPythonObfuscator.integers_to_floating = True

#
# move integers to arrays
#
myPythonObfuscator.integers_to_arrays = True

#
# move floats to arrays
#
myPythonObfuscator.floats_to_arrays = True

#
# apply redundant xor / affine integer masks
#
myPythonObfuscator.affine_integer_mask = True

#
# encrypted array literals
#
# encrypt integer array literals
#
myPythonObfuscator.array_int_crypt = True

#
# encrypt character array literals
#
myPythonObfuscator.array_char_crypt = True

#
# encrypt floating-point array literals
#
myPythonObfuscator.array_double_crypt = True

#
# encrypt string array literals
#
myPythonObfuscator.array_string_crypt = True

#
# decoy value pools
#
# insert a shared bucket of random noise values used by other strategies
#
myPythonObfuscator.insert_random_value_bucket = True

#
# populate the random value bucket with decoy integers
#
myPythonObfuscator.random_bucket_integers = True

#
# populate the random value bucket with decoy arrays
#
myPythonObfuscator.random_bucket_arrays = True

#
# populate the random value bucket with decoy functions
#
myPythonObfuscator.random_bucket_functions = True

#
# populate the random value bucket with decoy characters
#
myPythonObfuscator.random_bucket_characters = True

#
# populate the random value bucket with anti-regex decoy noise
#
myPythonObfuscator.random_bucket_anti_regex = True

#
# populate the random value bucket with autostart decoy stubs
#
myPythonObfuscator.random_bucket_autostart = True

#
# opaque predicates & noise
#
# rewrite selected statements using ternary operators
#
myPythonObfuscator.insert_ternary_operators = True

#
# replace boolean conditions with equivalent complex expressions
#
myPythonObfuscator.complexify_booleans = True

#
# insert opaque predicate branches
#
myPythonObfuscator.opaque_branches = True

#
# insert opaque mixer chains into control flow
#
myPythonObfuscator.opaque_mixer_chain = True

#
# insert dead code
#
myPythonObfuscator.insert_dead_code = True

#
# wrap code in try/finally blocks with dead noise
#
myPythonObfuscator.try_finally_noise = True

#
# decoys
#
# insert decoy functions
#
myPythonObfuscator.decoy_functions = True

#
# insert decoy lambda expressions
#
myPythonObfuscator.lambda_decoys = True

#
# insert literal padding noise
#
myPythonObfuscator.literal_padding = True

#
# insert fake import statement markers
#
myPythonObfuscator.fake_import_markers = True

#
# use dynamic getattr()-based indirect calls
#
myPythonObfuscator.dynamic_getattr_calls = True

#
# rewrite absolute imports into __import__ / getattr
#
myPythonObfuscator.obfuscate_imports = True

#
# insert dead callback/event registration stubs
#
myPythonObfuscator.callback_registration_stubs = True

#
# other
#
# strip comments from the output source
#
myPythonObfuscator.remove_comments = True

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
