#!/usr/bin/env python

###############################################################################
#
# Python Obfuscator is a source code obfuscator for the Python programming
# language. Obfuscate and protect your Python source code and algorithms
# against analysis, reverse engineering and technology theft.
#
# Python Obfuscator provides advanced Python source code parsing based on
# AST trees, multiple advanced obfuscation, virtualization and protection
# strategies are available.
#
# Version      : Python SDK v1.0.0
# Python       : Python v3
# Dependencies : requests (https://pypi.python.org/pypi/requests/)
# Author       : Bartosz Wójcik (support@pelock.com)
# Project      : https://www.pelock.com/products/python-obfuscator
# Homepage     : https://www.pelock.com
#
###############################################################################

import zlib
import base64
from enum import Enum

# required external package - install with "pip install requests"
import requests


class CodeVirtualization(str, Enum):
    """Public virtualization mode posted as ``code_virtualization``."""

    VM = "vm"
    FSA = "fsa"
    FLAT = "flat"


class RenameStyle(str, Enum):
    """Identifier alphabet posted as ``rename_style``."""

    IL = "il"
    O0 = "o0"
    CONFUSABLE = "confusable"
    HEX = "hex"
    HOMOGLYPH = "homoglyph"
    MANGLED = "mangled"


def _api_value(value):
    """Return the wire string for an enum member or a plain value."""
    if isinstance(value, Enum):
        return value.value
    return value


class PythonObfuscator(object):
    """Python Obfuscator module"""

    #
    # @var string default Python Obfuscator WebApi endpoint
    #
    API_URL = "https://www.pelock.com/api/python-obfuscator/v1"

    #
    # @var string WebApi key for the service
    #
    _api_key = ""

    #
    # @var bool should the source code be compressed
    #
    enable_compression = False

    #
    # @var int|None fixed random seed for reproducible obfuscation output (optional)
    #
    seed = None

    #
    # @var int|None randomization density / intensity (0-100)
    #
    randomization_density = None

    #
    # @var RenameStyle|str|None identifier renaming style (il, o0, confusable, hex, homoglyph, mangled)
    #
    rename_style = None

    #
    # @var CodeVirtualization public virtualization mode (vm, fsa, or flat)
    #
    code_virtualization = CodeVirtualization.VM

    #
    # @var bool protection against tampering with protected code (integrity verification)
    #
    self_defending = False

    #
    # @var bool protection linker (decoy call graph)
    #
    protection_linker = False

    #
    # @var bool rename variable names to random string values
    #
    rename_variables = True

    #
    # @var bool rename parameter names to random string values
    #
    rename_parameters = True

    #
    # @var bool rename function names to random string values
    #
    rename_functions = True

    #
    # @var bool rename function call references consistently with renamed functions
    #
    rename_function_calls = True

    #
    # @var bool shuffle function order in the output source
    #
    shuffle_functions = True

    #
    # @var bool fold/resolve constant expressions at obfuscation time
    #
    resolve_constants = True

    #
    # @var bool split strings into concatenated chunks
    #
    split_strings = True

    #
    # @var bool apply light transformations/mutations to string literals
    #
    modify_strings = True

    #
    # @var bool encrypt strings using randomly generated polymorphic encryption algorithms
    #
    encrypt_strings = True

    #
    # @var bool store string fragments in char-code array vaults
    #
    string_char_array_vault = True

    #
    # @var bool encrypt integers
    #
    encrypt_integers = True

    #
    # @var bool encrypt floating point numbers
    #
    encrypt_floating = True

    #
    # @var bool replace binary operators with mixed boolean-arithmetic (MBA) equivalents
    #
    mba_binops = True

    #
    # @var bool represent integers via floating-point math
    #
    integers_to_floating = True

    #
    # @var bool move integers to arrays
    #
    integers_to_arrays = True

    #
    # @var bool move floats to arrays
    #
    floats_to_arrays = True

    #
    # @var bool apply redundant xor / affine integer masks
    #
    affine_integer_mask = True

    #
    # @var bool encrypt integer array literals
    #
    array_int_crypt = True

    #
    # @var bool encrypt character array literals
    #
    array_char_crypt = True

    #
    # @var bool encrypt floating-point array literals
    #
    array_double_crypt = True

    #
    # @var bool encrypt string array literals
    #
    array_string_crypt = True

    #
    # @var bool insert a shared bucket of random noise values used by other strategies
    #
    insert_random_value_bucket = True

    #
    # @var bool populate the random value bucket with decoy integers
    #
    random_bucket_integers = True

    #
    # @var bool populate the random value bucket with decoy arrays
    #
    random_bucket_arrays = True

    #
    # @var bool populate the random value bucket with decoy functions
    #
    random_bucket_functions = True

    #
    # @var bool populate the random value bucket with decoy characters
    #
    random_bucket_characters = True

    #
    # @var bool populate the random value bucket with anti-regex decoy noise
    #
    random_bucket_anti_regex = True

    #
    # @var bool populate the random value bucket with autostart decoy stubs
    #
    random_bucket_autostart = True

    #
    # @var bool rewrite selected statements using ternary operators
    #
    insert_ternary_operators = True

    #
    # @var bool replace boolean conditions with equivalent complex expressions
    #
    complexify_booleans = True

    #
    # @var bool insert opaque predicate branches
    #
    opaque_branches = True

    #
    # @var bool insert opaque mixer chains into control flow
    #
    opaque_mixer_chain = True

    #
    # @var bool insert dead code
    #
    insert_dead_code = True

    #
    # @var bool wrap code in try/finally blocks with dead noise
    #
    try_finally_noise = True

    #
    # @var bool insert decoy functions
    #
    decoy_functions = True

    #
    # @var bool insert decoy lambda expressions
    #
    lambda_decoys = True

    #
    # @var bool insert literal padding noise
    #
    literal_padding = True

    #
    # @var bool insert fake import statement markers
    #
    fake_import_markers = True

    #
    # @var bool use dynamic getattr()-based indirect calls
    #
    dynamic_getattr_calls = True

    #
    # @var bool rewrite absolute imports into __import__ / getattr
    #
    obfuscate_imports = True

    #
    # @var bool insert dead callback/event registration stubs
    #
    callback_registration_stubs = True

    #
    # @var bool insert anti-debugging detections
    #
    detect_debugger = False

    #
    # @var bool insert virtual machine (anti-VM) detections
    #
    anti_vm = False

    #
    # @var bool insert anti-sandbox detections
    #
    anti_sandbox = False

    #
    # @var bool insert anti-emulators (CPU) detections
    #
    anti_emulator = False

    #
    # @var bool strip comments from the output source
    #
    remove_comments = True

    #
    # @var integer success
    #
    ERROR_SUCCESS = 0

    #
    # @var integer invalid size for source code (it's 1000 bytes max. for demo version)
    #
    ERROR_INPUT_SIZE = 1

    #
    # @var integer input source is empty
    #
    ERROR_INPUT = 2

    #
    # @var integer Python source code parsing error
    #
    ERROR_PARSING = 3

    #
    # @var integer Python parsed code obfuscation error
    #
    ERROR_OBFUSCATION = 4

    #
    # @var integer error while generating output code
    #
    ERROR_OUTPUT = 5

    def __init__(self, api_key=None, enable_all_obfuscation_options=True):
        """Initialize Python Obfuscator class

        :param api_key: Activation key. Empty or invalid keys run demo mode, which ignores strategy flags and always applies integers_to_arrays, mba_binops, and encrypt_strings (no virtualization; 1000 character limit).
        :param enable_all_obfuscation_options: Enable or disable all of the obfuscation options
        """

        self._api_key = api_key

        # compression stays disabled by default (API does not decompress today)
        self.enable_compression = False

        # global tuning options are left untouched (server side defaults apply)
        self.seed = None
        self.randomization_density = None
        self.rename_style = None
        self.code_virtualization = CodeVirtualization.VM if enable_all_obfuscation_options else None

        #
        # renaming & flow strategies
        #
        self.rename_variables = enable_all_obfuscation_options
        self.rename_parameters = enable_all_obfuscation_options
        self.rename_functions = enable_all_obfuscation_options
        self.rename_function_calls = enable_all_obfuscation_options
        self.shuffle_functions = enable_all_obfuscation_options
        self.resolve_constants = enable_all_obfuscation_options

        #
        # string strategies
        #
        self.split_strings = enable_all_obfuscation_options
        self.modify_strings = enable_all_obfuscation_options
        self.encrypt_strings = enable_all_obfuscation_options
        self.string_char_array_vault = enable_all_obfuscation_options

        #
        # numeric strategies
        #
        self.encrypt_integers = enable_all_obfuscation_options
        self.encrypt_floating = enable_all_obfuscation_options
        self.mba_binops = enable_all_obfuscation_options
        self.integers_to_floating = enable_all_obfuscation_options
        self.integers_to_arrays = enable_all_obfuscation_options
        self.floats_to_arrays = enable_all_obfuscation_options
        self.affine_integer_mask = enable_all_obfuscation_options

        #
        # array encryption strategies
        #
        self.array_int_crypt = enable_all_obfuscation_options
        self.array_char_crypt = enable_all_obfuscation_options
        self.array_double_crypt = enable_all_obfuscation_options
        self.array_string_crypt = enable_all_obfuscation_options

        #
        # entropy / random value bucket strategies
        #
        self.insert_random_value_bucket = enable_all_obfuscation_options
        self.random_bucket_integers = enable_all_obfuscation_options
        self.random_bucket_arrays = enable_all_obfuscation_options
        self.random_bucket_functions = enable_all_obfuscation_options
        self.random_bucket_characters = enable_all_obfuscation_options
        self.random_bucket_anti_regex = enable_all_obfuscation_options
        self.random_bucket_autostart = enable_all_obfuscation_options

        #
        # opaque predicate & decoy strategies
        #
        self.insert_ternary_operators = enable_all_obfuscation_options
        self.complexify_booleans = enable_all_obfuscation_options
        self.opaque_branches = enable_all_obfuscation_options
        self.opaque_mixer_chain = enable_all_obfuscation_options
        self.insert_dead_code = enable_all_obfuscation_options
        self.try_finally_noise = enable_all_obfuscation_options
        self.decoy_functions = enable_all_obfuscation_options
        self.lambda_decoys = enable_all_obfuscation_options
        self.literal_padding = enable_all_obfuscation_options
        self.fake_import_markers = enable_all_obfuscation_options
        self.dynamic_getattr_calls = enable_all_obfuscation_options
        self.obfuscate_imports = enable_all_obfuscation_options
        self.callback_registration_stubs = enable_all_obfuscation_options
        self.remove_comments = enable_all_obfuscation_options

        # protection strategies stay opt-in even in "full" mode
        self.self_defending = False
        self.protection_linker = False
        self.detect_debugger = False
        self.anti_vm = False
        self.anti_sandbox = False
        self.anti_emulator = False

    def login(self):
        """Login to the service and get the information about the current license limits

        :return: An array with the results or False on error
        :rtype: bool,dict
        """

        # parameters
        params = {"command": "login"}

        return self.post_request(params)

    def obfuscate_script_file(self, script_file_path):
        """Obfuscate Python script source code file using provided parameters

        :param script_file_path: Python compatible script *.py file path
        :return: An array with the results or False on error
        :rtype: bool,dict
        """

        source_file = open(script_file_path, 'r')
        source = source_file.read()
        source_file.close()

        if not source:
            return False

        return self.obfuscate_script_source(source)

    def obfuscate_script_source(self, script_source):
        """Obfuscate Python script source code using provided parameters

        :param script_source: Python compatible script *.py source code
        :return: An array with the results or False on error
        :rtype: bool,dict
        """

        # additional parameters
        params_array = {"command": "obfuscate", "source": script_source}

        return self.post_request(params_array)

    def post_request(self, params_array):
        """Send a POST request to the server

        :param params_array: An array with the parameters
        :return: An array with the results or false on error
        :rtype: bool,dict
        """

        # add activation key to the parameters array
        if self._api_key:
            params_array["key"] = self._api_key

        #
        # global tuning options
        #
        if self.seed is not None:
            params_array["seed"] = str(self.seed)
        if self.randomization_density is not None:
            params_array["randomization_density"] = str(self.randomization_density)
        if self.rename_style:
            params_array["rename_style"] = _api_value(self.rename_style)
        if self.code_virtualization:
            params_array["code_virtualization"] = _api_value(self.code_virtualization)

        #
        # obfuscation strategies
        #
        if self.self_defending:
            params_array["self_defending"] = "1"
        if self.protection_linker:
            params_array["protection_linker"] = "1"
        if self.rename_variables:
            params_array["rename_variables"] = "1"
        if self.rename_parameters:
            params_array["rename_parameters"] = "1"
        if self.rename_functions:
            params_array["rename_functions"] = "1"
        if self.rename_function_calls:
            params_array["rename_function_calls"] = "1"
        if self.shuffle_functions:
            params_array["shuffle_functions"] = "1"
        if self.resolve_constants:
            params_array["resolve_constants"] = "1"
        if self.split_strings:
            params_array["split_strings"] = "1"
        if self.modify_strings:
            params_array["modify_strings"] = "1"
        if self.encrypt_strings:
            params_array["encrypt_strings"] = "1"
        if self.string_char_array_vault:
            params_array["string_char_array_vault"] = "1"
        if self.encrypt_integers:
            params_array["encrypt_integers"] = "1"
        if self.encrypt_floating:
            params_array["encrypt_floating"] = "1"
        if self.mba_binops:
            params_array["mba_binops"] = "1"
        if self.integers_to_floating:
            params_array["integers_to_floating"] = "1"
        if self.integers_to_arrays:
            params_array["integers_to_arrays"] = "1"
        if self.floats_to_arrays:
            params_array["floats_to_arrays"] = "1"
        if self.affine_integer_mask:
            params_array["affine_integer_mask"] = "1"
        if self.array_int_crypt:
            params_array["array_int_crypt"] = "1"
        if self.array_char_crypt:
            params_array["array_char_crypt"] = "1"
        if self.array_double_crypt:
            params_array["array_double_crypt"] = "1"
        if self.array_string_crypt:
            params_array["array_string_crypt"] = "1"
        if self.insert_random_value_bucket:
            params_array["insert_random_value_bucket"] = "1"
        if self.random_bucket_integers:
            params_array["random_bucket_integers"] = "1"
        if self.random_bucket_arrays:
            params_array["random_bucket_arrays"] = "1"
        if self.random_bucket_functions:
            params_array["random_bucket_functions"] = "1"
        if self.random_bucket_characters:
            params_array["random_bucket_characters"] = "1"
        if self.random_bucket_anti_regex:
            params_array["random_bucket_anti_regex"] = "1"
        if self.random_bucket_autostart:
            params_array["random_bucket_autostart"] = "1"
        if self.insert_ternary_operators:
            params_array["insert_ternary_operators"] = "1"
        if self.complexify_booleans:
            params_array["complexify_booleans"] = "1"
        if self.opaque_branches:
            params_array["opaque_branches"] = "1"
        if self.opaque_mixer_chain:
            params_array["opaque_mixer_chain"] = "1"
        if self.insert_dead_code:
            params_array["insert_dead_code"] = "1"
        if self.try_finally_noise:
            params_array["try_finally_noise"] = "1"
        if self.decoy_functions:
            params_array["decoy_functions"] = "1"
        if self.lambda_decoys:
            params_array["lambda_decoys"] = "1"
        if self.literal_padding:
            params_array["literal_padding"] = "1"
        if self.fake_import_markers:
            params_array["fake_import_markers"] = "1"
        if self.dynamic_getattr_calls:
            params_array["dynamic_getattr_calls"] = "1"
        if self.obfuscate_imports:
            params_array["obfuscate_imports"] = "1"
        if self.callback_registration_stubs:
            params_array["callback_registration_stubs"] = "1"
        if self.detect_debugger:
            params_array["detect_debugger"] = "1"
        if self.anti_vm:
            params_array["anti_vm"] = "1"
        if self.anti_sandbox:
            params_array["anti_sandbox"] = "1"
        if self.anti_emulator:
            params_array["anti_emulator"] = "1"
        if self.remove_comments:
            params_array["remove_comments"] = "1"

        #
        # check if compression is enabled
        #
        if "source" in params_array and self.enable_compression and params_array["source"]:

            compressed_data = zlib.compress(bytes(params_array["source"], 'utf-8'), 9)
            base64_encoded_data = base64.b64encode(compressed_data).decode()

            params_array["source"] = base64_encoded_data
            params_array["compression"] = "1"

        response = requests.post(self.API_URL, data=params_array)

        # no response at all or an invalid response code
        if not response or not response.ok:
            return False

        # decode to json array
        result = response.json()

        # depack output code back into the string
        if "output" in result and self.enable_compression and result["error"] == self.ERROR_SUCCESS:

            result["output"] = str(zlib.decompress(base64.b64decode(result["output"])), "utf-8")

        # return original JSON response code
        return result
