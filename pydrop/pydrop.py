#! /usr/bin/env python

import argparse,os,getpass,csv
from os.path import expanduser
from doread import dropletread
from doaction import doaction
from dodelete import dropdelete
from doreset import dropreset
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def do_key_entry(key=None):
    if key is not None:
        dohome=os.path.join(os.path.expanduser('~'), 'dokey.csv')
        try:
            with open(dohome,'w') as completed:
                writer=csv.writer(completed,delimiter=',',lineterminator='\n')
                writer.writerow([key])
            print('API Key saved')
        except Exception as e:
            print(e)
    else:
        dohome=os.path.join(os.path.expanduser('~'), 'dokey.csv')
        print("Enter your Digital Ocean API Key")
        password=getpass.getpass()
        try:
            with open(dohome,'w') as completed:
                writer=csv.writer(completed,delimiter=',',lineterminator='\n')
                writer.writerow([password])
            print('API Key saved')
        except Exception as e:
            print(e)
def do_key_from_parser(args):
    do_key_entry(key=args.key)

def dropinfo_from_parser(args):
    dropletread(tag=args.tag)

def dropdelete_from_parser(args):
    dropdelete(idn=args.id,name=args.name)

def dropreset_from_parser(args):
    dropreset(idn=args.id,name=args.name)

def dropaction_from_parser(args):
    doaction(idn=args.id,name=args.name,action=args.action,rname=args.rename)

spacing="                               "
def main(args=None):
    parser = argparse.ArgumentParser(description='Digital Ocean API Python CLI')

    subparsers = parser.add_subparsers()
    parser_do_key = subparsers.add_parser('dokey', help='Enter your Digital Ocean API Key')
    optional_named = parser_do_key.add_argument_group('Optional named arguments')
    optional_named.add_argument('--key', help='Your Digital Ocean API Key')
    parser_do_key.set_defaults(func=do_key_from_parser)

    parser_dropletread = subparsers.add_parser('dropinfo', help='Prints information about all your droplets')
    optional_named = parser_dropletread.add_argument_group('Optional named arguments')
    optional_named.add_argument('--tag', help='Use a tag to refine your search',default=None)
    parser_dropletread.set_defaults(func=dropinfo_from_parser)

    parser_dropdelete = subparsers.add_parser('dropdelete', help='Permanently deletes the droplet ')
    optional_named = parser_dropdelete.add_argument_group('Optional named arguments')
    optional_named.add_argument('--id', help='Use an image ID to delete droplet',default=None)
    optional_named.add_argument('--name', help='Use an image name to delete droplet',default=None)
    parser_dropdelete.set_defaults(func=dropdelete_from_parser)

    parser_dropreset = subparsers.add_parser('dropreset', help='Resets password for the droplet ')
    optional_named = parser_dropreset.add_argument_group('Optional named arguments')
    optional_named.add_argument('--id', help='Use an image ID to reset password on droplet',default=None)
    optional_named.add_argument('--name', help='Use an image name to reset password on droplet',default=None)
    parser_dropreset.set_defaults(func=dropreset_from_parser)

    parser_doaction = subparsers.add_parser('dropaction', help='Performs an action on your droplets')
    optional_named = parser_doaction.add_argument_group('Optional named arguments')
    optional_named.add_argument('--id', help='Use an image ID to perform action',default=None)
    optional_named.add_argument('--name', help='Use an image name to perform action',default=None)
    optional_named.add_argument('--action', help='Action type |shutdown="graceful shutdown"|power_off="hard shutdown"|power_on="power on"|rename="rename',default=None)
    optional_named.add_argument('--rename', help='Incase you are renaming droplet you can provide new name',default=None)
    parser_doaction.set_defaults(func=dropaction_from_parser)

    args = parser.parse_args()

    #ee.Initialize()
    args.func(args)

if __name__ == '__main__':
    main()
