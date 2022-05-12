#!/usr/bin/env python3
# Encoding: UTF-8
# By: Jorge L. Herrera

from .clr import c

version = 0.1

bn = lambda version: print(f"""\t___      _____  ___ _   _
	| \    // ____ |__ | \ |
	|_//o   \____/ |__ |  \| {c.red} {version} {c.cyan}
	=============================
""")
