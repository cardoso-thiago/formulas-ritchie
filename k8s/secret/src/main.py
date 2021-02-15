#!/usr/bin/python3
import os

from formula import formula

name = os.environ.get("RIT_INPUT_NAME")
namespace = os.environ.get("RIT_INPUT_NAMESPACE")
user = os.environ.get("RIT_INPUT_USER")
password = os.environ.get("RIT_INPUT_PASSWORD")
formula.Run(name, namespace, user, password)