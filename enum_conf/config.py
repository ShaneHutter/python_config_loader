#!/usr/bin/env python3
"""
This module loads config files, sorts
config priority, and returns/manages config enums.
"""

from enum   import Enum , EnumType
from yaml   import safe_load
from os     import environ


### Set nested defaults Enum ###
class ConfigDefaultsBind( Enum ):
    host = "127.0.0.1"
    port = 8080
class ConfigDefaultsOptions( Enum ):
    name = "Default Name"
    enable_this = False
class ConfigDefaults( Enum ):
    bind = ConfigDefaultsBind
    options = ConfigDefaultsOptions
### ### ###


def load_env():
    # Check the values in nested Enums for 
    """ Convert to a good, recursive function
            * Each level of recursion should append obj.name to a list
            * The list can be joined by "." to show the string of the path
                and the path can likewise be split by "." to generate the list
            * The enviromnet varable is the path uppercase, with {APPNAME}_ prepended
                where APPNAME is the actualy name of the program using this config loader
                e.g.
                    APPNAME_BIND_PORT = bind.port
    """

    for obj in ConfigDefaults:
        print( obj.name , obj.value )
        print( type( obj.value ) )
        if type( obj.value ) == EnumType:
            for obj2 in obj.value:
                print( obj2.name , obj2.value )
    return


def load_config_file( filename ):
    with open( filename , "r" ) as config_file:
        config = safe_load( config_file.read() )
    return config


def set_config_enum( config_data ):
    class Config( Enum ):
        bind = config_data.get( "bind" )
        options = config_data.get( "option" )
    return Config

def generate_config( config_file ):
    """This function goes through all the steps to generate the
    configuration enum.  This is the main high level function you should
    call to generate the configuation data as a nested enum"""
    conf_file_data = load_config_file( config_file )

def get_confg_enum( path , config_enum ):
    """Get a value from config enum via a path
    e.g:
        bind.host = 127.0.0.1 by default
    """
    return
