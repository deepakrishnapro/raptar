from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from raptar.data_service.handler.starttest_handler import StartTestCaseHandler
from raptar.data_service.handler.finishtest_handler import FinishTestCaseHandler
import json
import logging

logger = logging.getLogger(__name__)


class StartTestCaseView(generics.CreateAPIView):

    def post(self, request):
        try:
            logger.info("Request received : {}".format(request.data))
            testid = StartTestCaseHandler.handlestarttestcase(request.data)
            return Response(
                data=testid,
                status=status.HTTP_200_OK
            )

        except Exception as ex:
            logger.error(" Exception : {}".format(ex))

class TestCaseRUDView(generics.RetrieveUpdateDestroyAPIView):

    def get(self, request):
        pass

    def put(self, request):
        try:
            logger.info("Request received : {}".format(request.data))
            testid = FinishTestCaseHandler.handlefinishtestcase(request.data)

            if (testid is not None):
                return Response(
                    data=testid,
                    status=status.HTTP_200_OK
                )
            else :
                return Response(
                    data=testid,
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as ex:
            logger.error("Exception while update operation in Finish Testcase View : {}".format(ex))

    def delete(self, request):
        pass