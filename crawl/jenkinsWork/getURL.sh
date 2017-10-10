#!/bin/bash

# << Swami Shreeji >>
# @nishantpatel ; 10 Oct 2017
# Create properly formed URL from jenkins plugin IDs

cut -f 1 -d ":" jenkPlug.fail | sed 's/^/https:\/\/plugins.jenkins.io\//' > URLsList.txt