from datetime import datetime
from raptar.data_service.serializers.testcase_serializer import TestCaseSerializer
import logging
from raptar.data_service.models.pipeline import Pipeline
from raptar.data_service.models.testsuite import TestSuite

logger = logging.getLogger(__name__)

class StartTestCaseHandler:

    @staticmethod
    def handlestarttestcase(testcaserequest):
        pipelineinstance = Pipeline.objects.get(pipelineid=testcaserequest['pipelineid'])
        logger.debug("Pipeline instance is exits and its  Id : {} ".format(pipelineinstance.pipelineid))
        testsuiteinstance = TestSuite.objects.get(testsuiteid=testcaserequest['testsuiteid'])
        logger.debug("Test suite instance is exits and its  Id : {} ".format(testsuiteinstance.testsuiteid))

        datetime_time = datetime.fromtimestamp(testcaserequest['starttime'])

        logger.info("datetime_time is : {}".format(datetime_time))
        testcase_data = {
            "testsuiteid": testsuiteinstance,
            "testcasename":testcaserequest['testcasename'],
            "starttime": datetime_time,
            "pipelineid": pipelineinstance
        }

        testcase_serializer = TestCaseSerializer()
        testcaseinstance = testcase_serializer.create(testcase_data)

        return testcaseinstance.testid

    @staticmethod
    def handleget():
        pass