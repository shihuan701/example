from utils.pathBase import readYamlFile
class GetData():

    def __init__(self,filename):
        '''
        :param filename:
        获取文件中的参数
        根据配置，
        集合中第一个元素为公共配置
        请求配置配置均从第二个集合开始
        '''
        self.desc = ()
        self.params = ()
        self.validate = ()
        self.checks = []
        self._tuple = ()
        params = readYamlFile(filename)
        self.url = params[0].get('config').get('interface')
        self.method = params[0].get('config').get('method')
        _params = params[1:]
        for i in range(0,len(_params)):
            tuples = (_params[i]['app']['desc'],_params[i]['app']['params'],_params[i]['app']['validate'])
            self.checks.append(tuples)

        '''
        方法二：利用正则表达式进行重组
        
        import re
        dicts = {}
        lists = []
        str1 = re.finditer(r"'desc': '(?P<desc>.+?)',.'params': (?P<params>.+?,.+?),.'validate': (?P<validate>.+?})", data)
        for i in str1:
            tuples = ()
            tuples = (i.group("desc"), i.group("params"), i.group("validate"))
            lists.append(tuples)
        '''
