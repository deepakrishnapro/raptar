from datetime import datetime
from raptar.data_service.serializers.testcase_serializer import TestCaseSerializer
from raptar.data_service.serializers.testreport_serializer import TestReportSerializer
import logging
from raptar.data_service.models.pipeline import Pipeline
from raptar.data_service.models.testcase import TestCase

logger = logging.getLogger(__name__)

class FinishTestCaseHandler:

    @staticmethod
    def handlefinishtestcase(testcaserequest):
        try:
            testinstance = TestCase.objects.get(testid=testcaserequest['testid'])
            logger.info("Test instance is exits and its  Id : {} ".format(testinstance.testid))

            test_data = {
                "duration": testcaserequest['duration'],
                "result": testcaserequest['result']
            }

            testcase_serializer = TestCaseSerializer()
            testinstance = testcase_serializer.update(testinstance, test_data)

        except testinstance.DoesNotExist:
            logger.info("Test id does not exists")
            testinstance = None

        return testinstance.testid

    @staticmethod
    def handleget():
        pass