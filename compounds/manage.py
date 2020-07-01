import sys
import os

# BASE_DIR -> comp files
from compounds import create_app

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# sys.path python解释器搜寻包的路径（查找一个包的所在位置）
# python解释器查找一个包（模块）代码的位置的 流程：
# 1.  在当前启动文件 所在的目录中查找
# 2. 如果在目录代码中没有找到，去系统环境中查找安装过的标准库或扩展库
#    可以理解为 系统环境中能够保存库代码的目录  都存在sys.path中
#   sys.path 是一个列表， 其中保存了用于查找包所在的目录的名字
sys.path.insert(0, os.path.join(BASE_DIR, 'common'))

from flask import jsonify



from settings.default import DefaultConfig


# flask 工厂函数
app = create_app(DefaultConfig, enable_config_file=True)


@app.route('/')
def route_map():
    """
    主视图，返回所有视图网址
    """
    rules_iterator = app.url_map.iter_rules()
    return jsonify({rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')})
