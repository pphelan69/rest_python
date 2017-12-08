import smtplib
import file_utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = "alerts.datacloudautomation@gmail.com"
toaddr = "atul.dadhich@actian.com, swarnahowri.m@actian.com, satish.rn@actian.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Data Cloud Hybrid Integration Manager Automation Test Report"

body = "Please Refer the Attached Html Report"

msg.attach(MIMEText(body, 'plain'))

filename = "DC_X_Test_ExecutionReport.html"
filepath = file_utils.get_auto_loc_root() + "/dc_integ_auto/"
reportfile = filepath + filename
attachment = open(reportfile, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "w3lc0m301*")
text = msg.as_string()
server.sendmail(fromaddr, toaddr.split(","), text)
print 'Execution Report Sent'
server.quit()
