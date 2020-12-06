from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from raptar.data_service.handler.startpipeline_handler import StartPipelineHandler
from raptar.data_service.handler.finishpipeline_handler import FinishPipelineHandler
import logging

class StartPipelineView(generics.CreateAPIView):

    def post(self, request):
        try:
            logging.info("Request received : {}".format(request.data))
            pipelineid = StartPipelineHandler.handlestartpipeline(request.data)
            return Response(
                data=pipelineid,
                status=status.HTTP_200_OK
            )

        except Exception as ex:
            logging.error("Deepa Exception : {}".format(ex))

class StartPipelineRUDView(generics.RetrieveUpdateDestroyAPIView):

    def get(self, request):
        pass

    def put(self, request):
        try:
            logging.info("Request received : {}".format(request.data))
            pipelineid = FinishPipelineHandler.handlefinishpipeline(request.data)

            if (pipelineid is not None):
                return Response(
                    data=pipelineid,
                    status=status.HTTP_200_OK
                )
            else :
                return Response(
                    data=pipelineid,
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as ex:
            logging.error("Exception while update operation in startpipeline View : {}".format(ex))

    def delete(self, request):
        pass