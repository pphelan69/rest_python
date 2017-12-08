import datacloud
import json
import os
import logging
import pytest
from miscutils import file_utils


# "JobTemplate" Fixtures
def jobtemplate_postdata():
    # Read the Request Payload for the Create Job Template API
    mypath = file_utils.get_auto_loc_root() + "/dc_integ_auto/config/payloads/jobtemplate_create_1.json"
    logging.info("Request Payload for POST Jobtemplate")
    logging.info(mypath)
    with open(mypath) as payload:
        reqpayload = json.load(payload)
        return reqpayload


def read_jobtemplatedata():
    # Read the Request Payload for the Create Job Template API
    mypath = file_utils.get_auto_loc_root() + "/dc_integ_auto/config/payloads/jobtemplate.json"
    logging.info("Info Related to a Newly Created Jobtemplate")
    logging.info(mypath)
    with open(mypath) as payload:
        templatedata = json.load(payload)
        logging.info(templatedata["id"])
        return templatedata["id"]


def upload_packagefile():
    mypath = file_utils.get_auto_loc_root() + "/dc_integ_auto/config/payloads/MyFirstPackage.1.0.djar"
    logging.info("Package file for Template")
    logging.info(mypath)
    filename = open(mypath, 'rb').name
    key = os.path.basename(filename)
    data = open(mypath, 'rb').read()
    return data, key


@pytest.fixture(scope="class")
def get_jobtemplate(request):
    return datacloud.jobconfiguration.GetTemplateAPI(request.cls.dc_host, request.cls.dc_token)


@pytest.fixture(scope="class")
def get_jobtemplate_byid(request):
    jobtemplateid = read_jobtemplatedata()
    return datacloud.jobconfiguration.GetTemplateAPI(request.cls.dc_host, request.cls.dc_token,
                                                     jobtemplateid=jobtemplateid)


@pytest.fixture(scope="class")
def create_jobtemplate(request):
    postdata = jobtemplate_postdata()
    return datacloud.jobconfiguration.CreateTemplateAPI(request.cls.dc_host, request.cls.dc_token, data=postdata)


@pytest.fixture(scope="class")
def update_jobtemplate(request):
    jobtemplateid = read_jobtemplatedata()
    jobtemplateobj = datacloud.jobconfiguration.GetTemplateAPI(request.cls.dc_host, request.cls.dc_token,
                                                               jobtemplateid=jobtemplateid)
    putdata = jobtemplateobj.get_jobtemplate_by_id()
    putdata["runtimeConfig"]["packageName"] = "integrationSpec/MyFirstPackage.1.0.djar"
    putdata["runtimeConfig"]["entryPoint"] = "MyFirstProject/MyFirstProcess.ip.xml"
    return datacloud.jobconfiguration.UpdateTemplateAPI(request.cls.dc_host, request.cls.dc_token, data=putdata,
                                                        jobtemplateid=jobtemplateid)


@pytest.fixture(scope="class")
def delete_jobtemplate(request):
    jobtemplateid = read_jobtemplatedata()
    return datacloud.jobconfiguration.DeleteTemplateAPI(request.cls.dc_host, request.cls.dc_token,
                                                        template_id=jobtemplateid)


@pytest.fixture(scope="class")
def get_jobtemplate_files(request):
    jobtemplateid = read_jobtemplatedata()
    return datacloud.jobconfiguration.GetTemplateFilesAPI(request.cls.dc_host, request.cls.dc_token,
                                                          jobtemplateid=jobtemplateid)


@pytest.fixture(scope="class")
def post_jobtemplate_files(request):
    jobtemplateid = read_jobtemplatedata()
    packagefile, key = upload_packagefile()
    print packagefile, key
    return datacloud.jobconfiguration.CreateTemplateFilesAPI(request.cls.dc_host, request.cls.dc_token,
                                                             jobtemplateid=jobtemplateid, data=packagefile, key=key)


@pytest.fixture(scope="class")
def get_package_entrypoints(request):
    jobtemplateid = read_jobtemplatedata()
    return datacloud.jobconfiguration.GetEntryPointsAPI(request.cls.dc_host, request.cls.dc_token,
                                                        jobtemplateid=jobtemplateid)


# "JobConfig" Fixtures
def jobconfig_postdata():
    # Read the Request Payload for the Create Job Config API
    mypath = file_utils.get_auto_loc_root() + "/dc_integ_auto/config/payloads/jobconfig_create_1.json"
    logging.info("Request Payload for POST JobConfig")
    logging.info(mypath)
    with open(mypath) as payload:
        reqpayload = json.load(payload)
        return reqpayload


def read_jobconfigdata():
    # Read the Response of the Create Job Config API
    mypath = file_utils.get_auto_loc_root() + "/dc_integ_auto/config/payloads/jobconfig.json"
    logging.info("Info Related to a Newly Created JobConfig")
    logging.info(mypath)
    with open(mypath) as payload:
        configdata = json.load(payload)
        logging.info(configdata["id"])
        return configdata["id"]


@pytest.fixture(scope="class")
def create_jobconfig(request):
    jobtemplateid = read_jobtemplatedata()
    postdata = jobconfig_postdata()
    postdata["template"]["id"] = jobtemplateid
    return datacloud.jobconfiguration.CreateConfigAPI(request.cls.dc_host, request.cls.dc_token, data=postdata)


@pytest.fixture(scope="class")
def delete_jobconfig(request):
    jobconfigid = read_jobconfigdata()
    return datacloud.jobconfiguration.DeleteConfigAPI(request.cls.dc_host, request.cls.dc_token, config_id=jobconfigid)
