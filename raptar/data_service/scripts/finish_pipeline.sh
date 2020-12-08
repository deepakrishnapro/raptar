#!/bin/bash -e

echo "Start of finish pipeline"
PIPELINE_ID=`cat /var/lib/jenkins/envVars.properties`
echo "$PIPELINE_ID"

result_jenkins=$(curl -X GET --header "Accept: */*" "http://deepa:11a093986adee54e2c5cc2b1f0cfdab6fb@ec2-54-189-234-66.us-west-2.compute.amazonaws.com:8080/job/$JOB_BASE_NAME/$BUILD_NUMBER/api/json?pretty=true")

test_report=$(curl -X GET --header "Accept: */*" "http://deepa:11a093986adee54e2c5cc2b1f0cfdab6fb@ec2-54-189-234-66.us-west-2.compute.amazonaws.com:8080/job/$JOB_BASE_NAME/$BUILD_NUMBER/testReport/api/json?pretty=true")


status=$(jq -r '.result' <<< "${result_jenkins}")
#duration=$(jq -r '.duration' <<< "${result_jenkins}")
start_time=$(jq -r '.timestamp' <<< "${result_jenkins}")
cur_time=$(date +%s%3N)
duration=`expr $cur_time - $start_time`
end_time=`expr $start_time + $duration`
fail_count=$(jq -r '.failCount' <<< "${test_report}")
skip_count=$(jq -r '.skipCount' <<< "${test_report}")
pass_count=$(jq -r '.passCount' <<< "${test_report}")
total_count=`expr $fail_count + $skip_count + $pass_count`


template2='{
    "pipelineid" : '$PIPELINE_ID',
    "duration": '$duration',
    "endtime": '$end_time',
    "result":"'$status'",
    "totaltestcase":'$total_count',
    "testcasepassed":'$pass_count',
    "testcasefailed":'$fail_count',
    "testcaseskipped":'$skip_count'
}'

echo " point 3 $template2"



http_response=$(curl -i \
-H "Accept: application/json" \
-H "Content-Type:application/json" \
-w "%{http_code}" \
-X PUT --data "$template2" --url http://ec2-54-189-234-66.us-west-2.compute.amazonaws.com:8001/pipeline/finish)

statuscode=$(echo "$http_response" |  grep HTTP |  awk '{print $2}')

if [ $statuscode -eq 200 ]; then
	echo "Server returned:"
    http_response=(${http_response[@]}) # convert to array
    code=${http_response[-1]} # get last element (last line)
    echo "$code"
else
    echo "Server did not return HTTP 200 OK"
fi