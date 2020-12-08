#!/bin/bash


echo "My Build url is ----- $BUILD_URL"

result_jenkins=$(curl -X GET --header "Accept: */*" "http://deepa:11a093986adee54e2c5cc2b1f0cfdab6fb@ec2-54-189-234-66.us-west-2.compute.amazonaws.com:8080/job/$JOB_BASE_NAME/$BUILD_NUMBER/api/json?pretty=true")
#echo "my result data :  $result_jenkins  end"

start_time=$(jq -r '.timestamp' <<< "${result_jenkins}")


template2='{
    "productname" : "oscar",
    "productversion" : "1.1",
    "projectname":"'$JOB_BASE_NAME'",
    "environment":"Dev",
    "projectowner":"Deepa Krishna",
    "repositoryurl":"'$JOB_URL'",
    "url": "'$BUILD_URL'",
    "commitid": "5123",
    "jobid": "'$BUILD_NUMBER'",
    "starttime": '$start_time'
}'

echo "$template2"


http_response=$(curl -i \
-H "Accept: application/json" \
-H "Content-Type:application/json" \
-w "%{http_code}" \
-X POST --data "$template2" --url http://ec2-54-189-234-66.us-west-2.compute.amazonaws.com:8001/pipeline/start)

statuscode=$(echo "$http_response" |  grep HTTP |  awk '{print $2}')

if [ $statuscode -eq 200 ]; then
	echo "Server returned: Success"
    http_response=(${http_response[@]}) # convert to array
    code=${http_response[-1]} # get last element (last line)
    export PIPELINE_ID=${code%???}
    echo "PIPELINE_ID = ${code%???}"
    echo $PIPELINE_ID > /var/lib/jenkins/envVars.properties
    #echo $PIPELINE_ID

else
    echo "Server did not return HTTP 200 OK"
fi
