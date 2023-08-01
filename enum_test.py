#!/usr/bin/env python3
"""This is an enum test. 

Goal:
    Load a config file if avialable and set config values in an enum
    config priority is:
        1. Command Line argument
        2. Environment Variable
        3. Configuration File
        4. Default Value

Notes:
    - An Enum is essentially a constant.
        1. Have a function load the config values correctly into normal vars
        2. Create the enum in the function with the vars
        3. Return the enum


Requirements:
    python3-yaml
"""

from enum_conf.config   import generate_config , load_env


if __name__ == '__main__':
    load_env()