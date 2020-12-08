from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_TEXT
from business_rules.variables import BaseVariables, numeric_rule_variable, \
    string_rule_variable, select_rule_variable
from django.utils import timezone
from django_business_rules.business_rule import BusinessRule
from raptar.data_service.utils import sendmail
from raptar.data_service.models.pipeline import Pipeline
from raptar.data_service.models.project import Project
import logging

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
        logging.info("Action Triggered - executing send email to {}".format(email_id))

        subject = 'Alert! Pass Percentage'
        body = ' *** This is an automated message triggered by the raptar rule engine ***' + \
               '\n' + 'Pass Percentage has been breached.' +\
               '\n' + 'Pass Percentage for the pipeline is at {}'.format(self.testreport.passpercent)
        to_addr_list = []
        to_addr_list.append(email_id)
        #sendmail(subject,body,to_addr_list)


class TestReportBusinessRule(BusinessRule):
    name = 'Test Report rules'
    variables = TestReportVariables
    actions = TestReportActions