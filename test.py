#!/bin/env python

from optparse import OptionParser
import os
import subprocess
import sys

defaultProjectPath = os.getcwd()
defaultResultsPath = os.path.join(os.getcwd(), "testResults.xml")

parser = OptionParser()
parser.add_option("-u", "--unity", default="unity")                   # path to unity executable
parser.add_option("-p", "--projectPath", default=defaultProjectPath)  # path to unity project
parser.add_option("-r", "--resultsPath", default=defaultResultsPath)  # path to use for results file

(options, args) = parser.parse_args()

cmd = ("{unity} "
  "-runTests "
  "-testPlatform editMode "
  "-projectPath {projectPath} "
  "-testResults {resultsPath} "
  "-batchmode"
).format(
  unity=options.unity,
  projectPath=options.projectPath,
  resultsPath=options.resultsPath
)

try:
  subprocess.check_output(cmd, shell=True)
except subprocess.CalledProcessError as e:
  sys.exit(e.returncode)