#!/usr/bin/env python3


import os
import json
import requests

URL = 'http://ec2-54-189-234-66.us-west-2.compute.amazonaws.com:8001/'

def get_environ(name):
    if name in os.environ:
        return os.environ[name]
    else:
        print("Exception occurred while getting environment variable - {} ".format(name))
        exit(0)

BUILD_NUMBER= get_environ('BUILD_NUMBER')
JOB_BASE_NAME= get_environ('JOB_BASE_NAME')


def check_http(result):
    if result.status_code < 200 or result.status_code > 202:
        if result.text:
            raise requests.HTTPError(result.text)
        result.raise_for_status()

def start_testsuite( area_name, triage_owners=None):
    try:
        result = requests.post(URL + 'testsuite/add', json={
            'testsuitename': area_name,
            'owner': triage_owners
            })
        check_http(result)
        return result.text
    except Exception as exception:
            print("Exception occurred during start_testsuite for   area_name - {},"
                                "Exception details : {}".format(area_name,str(exception)))

def start_test(pipeline_id, test_name, suite_id, starttime):
    try:
        result = requests.post(URL + 'testcase/start', json={
            'pipelineid': pipeline_id,
            'testcasename': test_name,
            'testsuiteid': suite_id,
            'starttime': starttime
            })
        check_http(result)
        return result.text
    except Exception as exception:
            print("Exception occurred during start_test for pipelineid - {} and testname - {},"
                                "Exception details : {}".format(pipeline_id,test_name,str(exception)))

def finish_test(test_id, result,test_duration, data={}, state_dump_collect=False):
    try:
        error_message = None
        error_status = None
        if state_dump_collect:
            error_message = data['errorDetails']
            error_status = "infra_error or Test case Failed"
        finish_test_data = {
            'testid': test_id,
            'result': result,
            'duration':test_duration,
            'errormessage':error_message,
            'errorstatus':error_status
            }

       # finish_test_data.update(data)
        result = requests.put(URL + 'testcase/finish', json=finish_test_data)
        check_http(result)
        return result.text
    except Exception as exception:
        print("Exception occurred during finish_test for testid - {},"
                                        "Exception details : {}".format(test_id,str(exception)))

def upload_tests(pipeline_id):
    try:
        testreport_url = "http://deepa:11a093986adee54e2c5cc2b1f0cfdab6fb@ec2-54-189-234-66.us-west-2.compute.amazonaws.com:8080/job/"+JOB_BASE_NAME+"/"+BUILD_NUMBER+"/testReport/api/json?pretty=true"
        job_url = "http://deepa:11a093986adee54e2c5cc2b1f0cfdab6fb@ec2-54-189-234-66.us-west-2.compute.amazonaws.com:8080/job/"+JOB_BASE_NAME+"/"+BUILD_NUMBER+"/api/json?pretty=true"
        response = requests.get(testreport_url)
        response2 = requests.get(job_url)

        my_json = json.loads(response.content.decode('utf8'))
        my_json2 = json.loads(response2.content.decode('utf8'))
        start_time = int(my_json2['timestamp'])
        for suites in my_json['suites']:
            print("inside suite")
            for test in suites['cases']:
                print("inside test case")
                state_dump_collect= False
                start_time = start_time + test['duration']
                suite_id = start_testsuite( test['className'],"Deepa Krishna")
                test['id'] = start_test(pipeline_id, test['name'], suite_id,start_time)
                print('Start test id: %s view at %s/testcase/start/%s' %
                      (test['id'], URL, test['id']))
                test_id = test['id']
                del test['id']
                if test['status'] != 'PASSED' and test['status'] != 'SKIPPED':
                    state_dump_collect = True
                finish_test_id = finish_test(test_id, test['status'],test['duration'], test, state_dump_collect)
                print('Finish test id: %s' % finish_test_id)
    except Exception as exception:
        print("Exception occurred during upload_tests for pipelineid - {}  - {},"
                     "Exception details : {}".format(pipeline_id,str(exception)))

def main():
    try:
        print('Calling a function upload tests ')

        PIPELINE_ID = open('/var/lib/jenkins/envVars.properties', 'r').read()
        print("PIPELINE_ID =  {}".format(PIPELINE_ID))
        BUILD_URL=get_environ('BUILD_URL')
        print("build URL {} ".format(BUILD_URL))
        upload_tests(PIPELINE_ID)

    except Exception as exception:
        print("Exception occurred during running upload results  for pipeline-id - Exception details : {}".format(str(exception)))
        pass

if __name__ == "__main__":
    main()
