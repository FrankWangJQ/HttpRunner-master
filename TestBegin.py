from httprunner import HttpRunner
import time


kwargs = {
    "failfast":False,
    #"dot_env_path": "/path/to/.env"
}
runner = HttpRunner(**kwargs)

runner.run("/Users/wangjianqing/PycharmProjects/HttpRunner-master/tests/testcases/Test/T_Login.yml")

runner.gen_html_report(html_report_name="reportTest",html_report_template="/Users/wangjianqing/PycharmProjects/HttpRunner-master/httprunner/templates/default_report_template.html")