from datetime import datetime
from raptar.data_service.serializers.pipeline_serializer import PipelineSerializer
from raptar.data_service.serializers.testreport_serializer import TestReportSerializer
import logging
from raptar.data_service.models.pipeline import Pipeline
from raptar.data_service.models.project import Project

logger = logging.getLogger(__name__)

class FinishPipelineHandler:

    @staticmethod
    def handlefinishpipeline(pipelinerequest):
        try:
            pipelineinstance = Pipeline.objects.get(pipelineid=pipelinerequest['pipelineid'])
            logger.info("Pipeline instance is exits Pipeline Id : {} ".format(pipelineinstance.pipelineid))
            datetime_time = datetime.fromtimestamp(pipelinerequest['endtime']/1000)
            logger.debug("end datetime_time is : {}".format(datetime_time))

            pipeline_data = {
                "endtime": datetime_time,
                "duration": pipelinerequest['duration'],
                "result": pipelinerequest['result'],
            }
            testreport_data = {
                "totaltestcase": pipelinerequest['totaltestcase'],
                "testcasepassed": pipelinerequest['testcasepassed'],
                "testcasefailed": pipelinerequest['testcasefailed'],
                "testcaseskipped": pipelinerequest['testcaseskipped'],
                "passpercent": pipelinerequest['passpercent'],
                "pipelineid": pipelineinstance
            }
            pipeline_serializer = PipelineSerializer()
            pipelineinstance = pipeline_serializer.update(pipelineinstance, pipeline_data)
            testreport_serializer = TestReportSerializer()
            testreport_serializer.create(testreport_data)

        except Pipeline.DoesNotExist:
            logger.info("Pipeline id does not exists")
            pipelineinstance = None

        return pipelineinstance.pipelineid

    @staticmethod
    def handleget():
        pass