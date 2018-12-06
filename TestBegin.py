from httprunner import HttpRunner
import time


kwargs = {
    "failfast":False,
    #"dot_env_path": "/path/to/.env"
}
runner = HttpRunner(**kwargs)

#入口

runner.run("/Users/wangjianqing/PycharmProjects/HttpRunner-master/tests/testcases/Release/账号管理-设置项.yml")

runner.gen_html_report(html_report_name="reportTestForBetaYunZS",html_report_template="/Users/wangjianqing/PycharmProjects/HttpRunner-master/httprunner/templates/default_report_template.html")

