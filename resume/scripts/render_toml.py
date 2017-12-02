#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from collections import OrderedDict
from jinja2 import (Environment, FileSystemLoader, select_autoescape, Markup,
                    escape)
import toml
import re

LINKIFY_REGEX = re.compile('\[([^\]]+)\]\(([^\)]+)\)')


def filter_linkify(value):
    def replace(m):
        link = str(escape(m.group(1)))
        return '<a href="' + m.group(2) + '">' + link + '</a>'
    return Markup(LINKIFY_REGEX.sub(replace, value or ""))


def filter_basename(value):
    i = value.rfind('.')
    return value if i == -1 else value[:i]


def main():
    parser = argparse.ArgumentParser(description="Render a TOML file using "
                                                 "Jinja2 template.")
    parser.add_argument('--template', '-t', required=True,
                        help='Jinja2 template to render with')
    parser.add_argument('input', nargs=1, help='input toml')
    parser.add_argument('output', nargs=1, help='output file')
    args = parser.parse_args()

    with open(args.input[0], 'rb') as f:
        data = toml.loads(f.read().decode("utf-8"), _dict=OrderedDict)

    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['tmpl']))

    env.filters['linkify'] = filter_linkify
    env.filters['basename'] = filter_basename

    template = env.get_template(args.template)
    with open(args.output[0], "wb+") as f:
        f.write(template.render(data, output=args.output[0]).encode("utf-8"))


if __name__ == '__main__':
    main()
