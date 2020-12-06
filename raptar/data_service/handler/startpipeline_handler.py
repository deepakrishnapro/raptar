from datetime import datetime
from raptar.data_service.serializers.pipeline_serializer import PipelineSerializer
import logging
from raptar.data_service.models.product import Product
from raptar.data_service.models.project import Project

logger = logging.getLogger(__name__)

class StartPipelineHandler:

    @staticmethod
    def handlestartpipeline(pipelinerequest):
        productinstance, created = Product.objects.get_or_create(productname=pipelinerequest['productname'], productversion=pipelinerequest['productversion'])
        logger.info("product instance is newly create : {} ".format(created))
        logger.info("Product-ID is : {}".format(productinstance.productid))

        projectinstance, exists = Project.objects.get_or_create(projectname=pipelinerequest['projectname'],
                                                                defaults={'projectowner': pipelinerequest['projectowner'],
                                                                          'repositoryurl': pipelinerequest['repositoryurl'],
                                                                          'environment': pipelinerequest['environment'],
                                                                           'product':productinstance})
        logger.info("Project instance is newly create : {} ".format(exists))
        logger.info("Project-ID is : {}".format(projectinstance.projectid))


        datetime_time = datetime.fromtimestamp(pipelinerequest['starttime']/1000)

        logger.info("datetime_time is : {}".format(datetime_time))
        pipeline_data = {
            "url": pipelinerequest['url'],
            "commitid": pipelinerequest['commitid'],
            "jobid": pipelinerequest['jobid'],
            "starttime": datetime_time,
            "projectid": projectinstance
        }

        pipeline_serializer = PipelineSerializer()
        pipelineinstance = pipeline_serializer.create(pipeline_data)
        logger.info("pipeline id created : {} ".format(pipelineinstance.pipelineid))

        return pipelineinstance.pipelineid

    @staticmethod
    def handleget():
        pass