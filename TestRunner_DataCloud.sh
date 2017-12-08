#!/bin/sh

find_dir=`pwd | awk -F "/" 'BEGIN {ORS=" "}{for (I=1;I<=NF;I++) if($I == "dc_integ_auto") for (J=I-1;J>=1;J--) print $(J)}' | awk 'BEGIN {ORS=" "}{ for (i=NF; i>=1; i--) print($i)}'`
path="${find_dir// //}"
test_path="/""$path""dc_integ_auto/tests"

path1="${find_dir// //}"
report_path="/""$path1""dc_integ_auto/DC_X_Test_ExecutionReport.html"

path2="${find_dir// //}"
sendmail_path="/""$path2""dc_integ_auto/miscutils/sendmail_utils.py"

echo "Executing Test Cases"
pytest "$test_path" --metadata Environment DC_X_Stage --html="$report_path" --self-contained-html --junitxml results.xml || sleep 5s && python "$sendmail_path"
