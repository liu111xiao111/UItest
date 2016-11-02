# -*- coding: utf-8 -*-


class DengLuXinXiPageConfigs():
    # 姓名
    resource_id_user = "com.feifan.bp:id/login_info_name";

    # 手机号
    resource_id_phone = "com.feifan.bp:id/login_info_phone";

    # 登录身份
    resource_id_identity = "com.feifan.bp:id/login_info_identity";

    # 所属商户
    resource_id_businessman = "com.feifan.bp:id/login_info_belongs_merchant";

    text_user = u"商户下的员工"
    test_phone = u"15624958068"
    test_identity = u"QA线上验证专用权限组"
    test_businessman = u"QA线上测试用普通商户"

    assert_timeout = 90

    def __init__(self):
        pass;