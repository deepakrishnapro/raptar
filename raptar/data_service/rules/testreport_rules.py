from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_TEXT
from business_rules.variables import BaseVariables, numeric_rule_variable, \
    string_rule_variable, select_rule_variable
from django.utils import timezone
from django_business_rules.business_rule import BusinessRule
from raptar.data_service.utils import sendmail
from raptar.data_service.models.pipeline import Pipeline
from raptar.data_service.models.project import Project

class TestReportVariables(BaseVariables):

    def __init__(self, testreport):
        self.testreport = testreport

    @numeric_rule_variable
    def test_report_pass_percentage(self):
        return self.testreport.passpercent


class TestReportActions(BaseActions):

    def __init__(self, testreport):
        self.testreport = testreport

    @rule_action(params={"email_id": FIELD_TEXT})
    def send_email_pass_percentage(self, email_id):
        pipelineid = self.testreport.pipelineid
        pipelineobj = Pipeline.objects.get(pipelineid=pipelineid)
        projectobj = Project.objects.get(projectid=pipelineobj.projectid)

        subject = 'Alert! Pass Percentage for pipeline : {}'.format(projectobj.projectname)
        body = ' *** This is an automated message triggered by the raptar rule engine ***' + \
               '\n' + 'Pass Percentage for pipeline {} '.format(projectobj.projectname) + 'has been breached.' +\
               '\n' + 'Pass Percentage for the pipeline is at {}'.format(self.testreport.passpercent)
        from_addr = 'deepaprojecttest@gmail.com'
        to_addr_list = []
        to_addr_list.append(email_id)
        sendmail(subject,body,from_addr,to_addr_list)


class TestReportBusinessRule(BusinessRule):
    name = 'Test Report rules'
    variables = TestReportVariables
    actions = TestReportActions