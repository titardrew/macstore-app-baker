#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

import os, sys
import argparse
import subprocess
import shlex

script_dir = os.path.dirname(os.path.realpath(__file__)) 

def failed():
    sys.exit("Execution failed...")

def refine_entitlements(args):
    """ If entitlements argument is set to 'gen' value, changes its value to output value without spaces."""
    if args.entitlements == 'gen':
        args.entitlements = args.app.replace(" ", "") + '.entitlements'

def ch_mod(args):
    """ Changes permissions recursivly to readable and executable for all user groups. """
    command = 'chmod -R a+xr "{}.app"'.format(args.app)
    print('$', command)
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, cwd=script_dir)
    output, error = process.communicate()
    if process.returncode == 0:
        print(output.decode("utf-8"))
    else:
        failed()

def sign(args):
    """ Uses codesign. """
    command = 'codesign -f --deep -s "3rd Party Mac Developer Application: {}" --entitlements "{}" "{}.app"'
    command = command.format(args.name, args.entitlements, args.app)
    print('$', command)
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, cwd=script_dir)
    output, error = process.communicate()
    if process.returncode == 0:
        print(output.decode("utf-8"))
    else:
        failed()

def build(args):
    """ Uses productbuild. """
    command = 'productbuild --component "{0}".app /Applications --sign "3rd Party Mac Developer Installer: {1}" "{0}.pkg"'
    command = command.format(args.app, args.name)
    print('$', command)
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, cwd=script_dir)
    output, error = process.communicate()
    if process.returncode == 0:
        print(output.decode("utf-8"))
    else:
        failed()

if __name__ == "__main__":

    # Setting up the argument parser.
    parser = argparse.ArgumentParser(description='Signs and builds the app.', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-n', '--name', type=str, default="Maxim Titarenko",
                    help='Developer\'s name \n(default: %(default)s)')
    parser.add_argument('-a', '--app', type=str, default="Football World Cup 2018 Russia",
                    help='Application name. \n(default: %(default)s)')
    parser.add_argument('-e', '--entitlements', type=str, default="FootballWorldCup2018Russia.entitlements",
                    help='Entitlements filename. Type "gen" to set its value to output name without spaces. \n(default: %(default)s)')

    # Parsing agruments.
    args = parser.parse_args()

    # Refining arguments.
    refine_entitlements(args)
    
    # Executing commands.
    print('-'*50)

    ch_mod(args)
    sign(args)
    build(args)

    print('-'*50)

    print('Success, {}! Generated "{}.pkg" at {}\n'.format(args.name.split()[0], args.app, script_dir))

