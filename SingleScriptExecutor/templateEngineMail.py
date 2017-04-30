#!/usr/bin/env python

import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

import argparse
parser = argparse.ArgumentParser(description='This program was developed by Sooraj Antony to perform terminal level integration of the Template generator Jinja server')
parser.add_argument('-r','--recipient',help='Recipient Full Name', required=True)
args = parser.parse_args()
## show values ##
recipientArg = args.recipient


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
    fname = "output.html"
    recipient = recipientArg
    sender = "Hirrr.com"
    context = {
        'recipient': recipient,
        'sender': sender
    }
    #
    with open(fname, 'w') as f:
        html = render_template('mail.html', context)
        f.write(html)


def main():
    create_index_html()

#############################################################################

if __name__ == "__main__":
    main()
