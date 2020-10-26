from datetime import datetime
from raptar.data_service.serializers.testsuite_serializer import TestSuiteSerializer

import logging
from raptar.data_service.models.pipeline import Pipeline
from raptar.data_service.models.testcase import TestCase
from raptar.data_service.models.testsuite import TestSuite

logger = logging.getLogger(__name__)

class TestSuiteHandler:

    @staticmethod
    def handletestsuite(testsuiterequest):
        testsuite_data = {
            "testsuitename": testsuiterequest['testsuitename'],
            "owner": testsuiterequest['owner']
        }

        testsuite_serializer = TestSuiteSerializer()
        testsuiteinstance = testsuite_serializer.create(testsuite_data)

        return testsuiteinstance.testsuiteid

    @staticmethod
    def handleget():
        pass