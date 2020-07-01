class DefaultConfig(object):
    """
    Flask默认配置
    """
    ERROR_404_HELP = False

    # 日志
    LOGGING_LEVEL = 'DEBUG'
    LOGGING_FILE_DIR = '../logs'
    LOGGING_FILE_MAX_BYTES = 300 * 1024 * 1024
    LOGGING_FILE_BACKUP = 10

    # flask-sqlalchemy使用的参数
    SQLALCHEMY_DATABASE_URI = 'mysql://roots:chm022252120A@rm-2ze9n8x6y1g64nq74yo.mysql.rds.aliyuncs.com:3306/compounds'  # 数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 追踪数据的修改信号
    SQLALCHEMY_ECHO = True

    # Snowflake ID Worker 参数
    DATACENTER_ID = 0
    WORKER_ID = 0
    SEQUENCE = 0

    # OSS2 参数
    OSS_ACCESSKEYID = 'LTAI4FzQ1HKBx33GWeAKYecN'
    OSS_ACCESSKEYSERCET = 'oqnoaV1dbhSLi4JCu2R0kbMdI7uIIx'
    OSS_ENDPOINT = 'oss-cn-beijing.aliyuncs.com'
    OSS_BUCKET = 'compounds'

    # 文件上传路径
    UPLOAD_PATH = '../upload'
