# Python Obfuscator — Obfuscate, Virtualize & Protect Python Code

**[Python Obfuscator](https://www.pelock.com/products/python-obfuscator)** is a tool to obfuscate, virtualize & protect Python `.py` scripts against reverse engineering with a VM engine (or finite-state automata machine), self-defending integrity checks, polymorphic string encryption, anti-debugging, anti-vm, anti-emulation and 50+ total obfuscation strategies!

It's available for Windows & Linux, plus VSCode/Cursor extension:

* https://www.pelock.com/products/python-obfuscator/download

Multiple programming APIs available:

* https://www.pelock.com/products/python-obfuscator/api

An online obfuscator interface:

* https://www.pelock.com/python-obfuscator/

## Why Python scripts need obfuscation?

Scripts are typically distributed as plain `.py` files or bundled inside packages. That convenience means anyone with file access can read the full logic, hunt for credentials or API keys in strings, and steal your algorithms unless you take extra steps to hide intent.

[Python](https://www.python.org/) is one of the most popular general-purpose scripting languages. It is widely used for automation, backend services, data processing, tooling, and licensing/agent code that customers run on their own machines.

## Obfuscation strategies

Python Obfuscator comes with many advanced obfuscation, virtualization & protection strategies. You can easily tune protection versus size and performance.

![Python Obfuscation options](https://www.pelock.com/img/en/products/python-obfuscator/python-obfuscator-virtualizer-obfuscation-options.png)

### ![Obfuscation](https://www.pelock.com/img/en/icons/obfuscation-32.png) Powerful obfuscation

Polymorphic string encryption is the core of the string pipeline: each build generates a fresh decryptor so literals never share one static algorithm. Integers, floats, and decoy noise join that layer. The result conceals literals and structure while preserving tested runtime behaviour.

### ![Processor](https://www.pelock.com/img/en/icons/processor-32.png) Code virtualization

Code virtualization is the main control-flow defense. Selected statements are lifted into a randomly generated VM engine (or FSA / flattened dispatcher) with shuffled dispatch tables, decoy opcodes, and an obfuscated dispatcher loop. Analysts must interpret the virtual machine instead of reading plain Python.

### ![Node](https://www.pelock.com/img/en/icons/node-32.png) Finite-state automata (FSA)

Finite-state automata (FSA) obfuscation rewrites linear Python statement blocks into dual-state automata with opaque schedulers and shuffled dispatch handlers. Instead of reading code top to bottom, analysts must follow numeric states, transition tables, and decoy paths to reconstruct the original order.

### ![Bug](https://www.pelock.com/img/en/icons/bug-32.png) Anti-debugging

Anti-debugging protection inserts polymorphic probes that detect attached debuggers, tracing hooks, and related host signals, together with anti-VM, anti-sandbox and anti-emulator checks. When a check fires, the obfuscated script exits silently instead of revealing protected logic under interactive analysis.

### ![System monitor](https://www.pelock.com/img/en/icons/system-monitor-32.png) Self-integrity checks

Self-defending integrity checks verify that the obfuscated file has not been patched. A bootstrap probe hashes the on-disk script and sets a tamper key when it no longer matches the obfuscated build. String decryptors consume that key, so edited scripts return garbage instead of plaintext.

### ![Brick link](https://www.pelock.com/img/en/icons/brick-link-32.png) Protection linker

The protection linker adds decoy functions and fake calls so a copied fragment still looks like real program code. Hidden traps fire only if someone edits the file or runs a piece of it on its own. When the script starts normally, those extras stay silent and the program runs as usual.

## Before and after obfuscation

Look at this example — the same script becomes harder to read at a glance after obfuscation.

### Sample Python script before obfuscation

```python
label = 'SecretKey'
port = 443

def get_sum(a, b):
    return a + b

print(label, port)
r = get_sum(11, 31)
print(r)
```

### After obfuscation

![Obfuscated Python script](https://www.pelock.com/img/en/products/python-obfuscator/python-obfuscator-virtualizer-obfuscated-virtualized-python-code.png)

Would you still recognise the original intent if you only had the obfuscated text and no prior copy of the script?

### How does Python Obfuscator work?

The engine parses Python source into an AST tree, then applies selectable transforms. Code virtualization (VM, FSA, or flattening) rewrites execution so analysts cannot read the script top to bottom. Polymorphic string encryption hides literals; self-defending integrity probes detect patched files. Also available: identifier renaming, numeric encryption, noise and decoy insertion, the protection linker, and anti-debugging checks. Many techniques are specific to this product; some ideas are shared with our other protection tools.

![Python Obfuscator Pipeline](https://www.pelock.com/img/en/products/python-obfuscator/python-obfuscator-obfuscation-pipeline.png)

When all passes finish, the engine emits a new `.py` file. Edge cases in the Python grammar and hosting environments mean you should always test the output in your target runtime.

## Protect your Python scripts & algorithms

Take no chances, use **Python Obfuscator** to obfuscate, virtualize and protect your Python scripts and algorithms.

Our company has a long history in obfuscation technologies and code obfuscators (see our [PowerShell](https://www.pelock.com/products/powershell-pro-obfuscator), [Java](https://www.pelock.com/products/jobfuscator), [AutoIt](https://www.pelock.com/products/autoit-obfuscator), [x86 Assembly](https://www.pelock.com/products/obfuscator) &  obfuscators).

We actively bugfix, research and develop new obfuscation strategies for our tools.

You can count on our expertise and support in this field.

### Installation

The preferred way of WebApi interface installation is via [pip](https://pypi.org/project/pip/).

Run:

```
pip install pythonobfuscator
```

or

```
python3 -m pip install pythonobfuscator
```

And then add this import to your source code:

```python
from pythonobfuscator import PythonObfuscator
```

Installation package is available at https://pypi.org/project/pythonobfuscator/

### Example of obfuscating Python script source code using default options

```python
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

```

### An example of obfuscating Python script source code with customized obfuscation strategies

```python
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

```

### Check activation key status

```python
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

```

## Skip selected functions and classes

Use the [Python Obfuscator Decorator](https://github.com/PELock/Python-Obfuscator-Decorator) package to mark functions and classes that should skip chosen strategies. You need it only to **run original source**. The obfuscator reads `@obfuscator.skip` from the AST, applies the skip, then **strips** the decorator and unused `import obfuscator` lines. Obfuscated output has no runtime dependency on this package.

Package on PyPI: https://pypi.org/project/python-obfuscator-decorator/

### Installation

```
pip install python-obfuscator-decorator
```

or

```
python3 -m pip install python-obfuscator-decorator
```

Import package name: **`obfuscator`**. PyPI distribution name: **`python-obfuscator-decorator`**.

### Simple usage

```python
import obfuscator


@obfuscator.skip()
def handshake(secret: str) -> str:
    """Skip every mutating strategy on this function."""
    return secret
```

Also valid:

- `@obfuscator.skip(obfuscator.ENCRYPT_STRINGS, obfuscator.CODE_VIRTUALIZATION)` — skip listed strategies
- `@obfuscator.skip("encrypt_strings")` — string keys match engine strategy names
- `@obfuscator.skip` (bare, no call) — skip every mutating strategy on that construct
- `import obfuscator as alias` then `@alias.skip(...)`

`CODE_VIRTUALIZATION` skips all virtualization modes (VM, FSA, flatten) on that function or class.

## Use Python Obfuscator Online

Online interface for Python Obfuscator is available at:

https://www.pelock.com/python-obfuscator/

## Windows GUI client and command line version

You can download it at:

https://www.pelock.com/products/python-obfuscator/download

#### Python Obfuscator comes also with full GUI version for Windows

![Python Obfuscator Windows Client](https://www.pelock.com/img/en/products/python-obfuscator/python-obfuscator-virtualizer.png)

#### Obfuscation options

![Python Obfuscation options](https://www.pelock.com/img/en/products/python-obfuscator/python-obfuscator-virtualizer-obfuscation-options.png)

#### Command line interface aka CLI

Python Obfuscator ships with a command-line interface for Windows and Linux automation. Use it to integrate obfuscation into build servers, CI jobs, or batch packaging.

![Python Obfuscator command-line interface](https://www.pelock.com/img/en/products/python-obfuscator/python-obfuscator-virtualizer-obfuscation-from-command-line.png)

## Demo mode limitations

In demo mode the obfuscator always applies `integers_to_arrays`, `mba_binops`, and `encrypt_strings` (no code virtualization). Source size is limited to 1000 characters.

Bartosz Wójcik

* Visit my site at — https://www.pelock.com
* X — https://x.com/PELock
* GitHub — https://github.com/PELock
