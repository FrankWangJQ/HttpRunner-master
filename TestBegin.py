from httprunner import HttpRunner
import time


kwargs = {
    "failfast":False,
    #"dot_env_path": "/path/to/.env"
}
runner = HttpRunner(**kwargs)

runner.run("/Users/wangjianqing/PycharmProjects/HttpRunner-master/tests/testcases/Test/T_Login.yml")