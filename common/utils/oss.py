import oss2
import uuid
from flask import current_app


class AliOss(object):
    def __init__(self):
        self.AccessKeyId = current_app.config['OSS_ACCESSKEYID']
        self.AccessKeySecret = current_app.config['OSS_ACCESSKEYSERCET']
        self.Endpoint = current_app.config['OSS_ENDPOINT']
        self.Bucker = current_app.config['OSS_BUCKET']
        self.base_image_url = current_app.config['OSS_BUCKET'] +'.'+current_app.config['OSS_ENDPOINT']
        self.auth = oss2.Auth(self.AccessKeyId, self.AccessKeySecret)
        self.bucket = oss2.Bucket(self.auth, self.Endpoint, self.Bucker)

    def upload(self, file,file_type):
        # 生成文件编号，如果文件名重复的话在oss中会覆盖之前的文件
        number = uuid.uuid4()
        # 生成文件名
        base_img_name = str(number) + '.' + file_type
        # 生成外网访问的文件路径
        image_name = 'https://' + self.base_image_url + '/'+ base_img_name
        # 这个是阿里提供的SDK方法 bucket是调用的4.1中配置的变量名
        res = self.bucket.put_object(base_img_name, file)
        # 如果上传状态是200 代表成功 返回文件外网访问路径
        # 下面代码根据自己的需求写
        if res.status == 200:
            return image_name , base_img_name
        else:
            return False
