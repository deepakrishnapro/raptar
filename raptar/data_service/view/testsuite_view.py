from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from raptar.data_service.handler.testsuite_handler import TestSuiteHandler
import json
import logging

logger = logging.getLogger(__name__)


class TestSuiteView(generics.CreateAPIView):

    def post(self, request):
        try:
            logger.info("Request received : {}".format(request.data))
            testsuiteid = TestSuiteHandler.handletestsuite(request.data)
            return Response(
                data=testsuiteid,
                status=status.HTTP_200_OK
            )

        except Exception as ex:
            logger.error("Deepa Exception : {}".format(ex))

class TestSuiteRUDView(generics.RetrieveUpdateDestroyAPIView):

    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass