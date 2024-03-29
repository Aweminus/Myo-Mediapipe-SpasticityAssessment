#!/bin/bash

MY_PATH="`dirname \"$0\"`"              # relative
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"  # absolutized and normalized
if [ -z "$MY_PATH" ] ; then
  # error; for some reason, the path is not accessible
  # to the script (e.g. permissions re-evaled after suid)
  exit 1  # fail
fi
echo "$MY_PATH"

# Run Mediapipe GUI
cd "$MY_PATH"/mediapipeCV/v3_integratedCV
python login.py &
python myo_save_GUI.py &

# Run and start recording EMG data
#cd "$MY_PATH"/thalmicMyo/examples &
