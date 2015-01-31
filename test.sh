#!/bin/bash

#Runs the first two arguments, then takes stderr and inputs to script echo.py
$1 $2 2>&1 test | python echo.py