
# Import all Job Configuration service apis
from datacloud.jobconfiguration.jobconfig_del import DeleteConfigAPI
from datacloud.jobconfiguration.jobconfig_post import CreateConfigAPI
from datacloud.jobconfiguration.jobtemplate_del import DeleteTemplateAPI
from datacloud.jobconfiguration.jobtemplate_entrypoints_get import GetEntryPointsAPI
from datacloud.jobconfiguration.jobtemplate_files_get import GetTemplateFilesAPI
from datacloud.jobconfiguration.jobtemplate_files_post import CreateTemplateFilesAPI
from datacloud.jobconfiguration.jobtemplate_get import GetTemplateAPI
from datacloud.jobconfiguration.jobtemplate_post import CreateTemplateAPI
from datacloud.jobconfiguration.jobtemplate_put import UpdateTemplateAPI


__all__ = ['DeleteConfigAPI', 'CreateConfigAPI', 'DeleteTemplateAPI', 'GetEntryPointsAPI',
           'GetTemplateFilesAPI', 'CreateTemplateFilesAPI', 'GetTemplateAPI', 'CreateTemplateAPI', 'UpdateTemplateAPI']
