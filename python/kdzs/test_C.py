import logging
import pytest
import allure

logging.basicConfig(level=logging.DEBUG)
def setup_module():
    logging.info('----------setup_module')

def teardown_module():
    logging.info('----------setup_module')

class TestClass:
    def setup(self)->None:
        pass

    @pytest.mark.run(order=3)
    def test_one(self):
        assert [1,2] == [1,3]

    @pytest.mark.run(order=2)
    def test_two(self):
        assert {"a":1,"name":"shi"} == {"a":1,"name":"huan"}

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,c",[(1,1,2),(1,-1,0),(10000,1,10001)])

    def test_add(self,a,b,c):
        allure.attach('这是一个allure的文本',attachment_type=allure.attachment_type.TEXT)
        allure.attach('<div class="sect3"><h4 id="_manual_installation"><a class="anchor" href="#_manual_installation"></a>2.1.4. Manual installation</h4><div class="olist arabic"><ol class="arabic"><li><p>Download the latest version as zip archive from<a href="http://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/">Maven Central</a>.</p></li><li><p>Unpack the archive to allure-commandline directory.</p></li><li><p>Navigate to<strong>bin</strong> directory.</p></li><li><p>Use<strong>allure.bat</strong> for Windows or<strong>allure</strong> for other Unix platforms.</p></li><li><p>Add<strong>allure</strong> to system PATH.</p></li></ol></div><div class="admonitionblock warning"><table><tbody><tr><td class="icon"><i class="fa icon-warning" title="Warning"></i></td><td class="content"><div class="paragraph"><p>To run commandline application, Java Runtime Environment must be installed.</p></div></td></tr></tbody></table></div><div class="admonitionblock note"><table><tbody><tr><td class="icon"><i class="fa icon-note" title="Note"></i></td><td class="content">Older releases (⇐ 2.8.0) are available on<a href="https://bintray.com/qameta/generic/allure2">bintray</a>.</td>', attachment_type=allure.attachment_type.HTML)
        assert self.calc.add(a,b) == c

class TestClass2:

    @classmethod
    def setup_class(cls):
        logging.info('------------setup_class')

    def setup_method(self):
        logging.info('------------setup')
    # def test_one(self):
    #     x = 'this'
    #     assert 'h' in x
    #
    # def test_needsfiles(tmpdir):
    #     print ('------------------',tmpdir)
    #     assert 1
    def setup_function(self):
        logging.info('------------setup_function')


    def test_three(self):
        assert 1==2

    @allure.title('第四个测试用例')
    def test_four(self):
        assert True == True

    def teardown_method(self):
        logging.info('------------teardown_function')
    def teardown_method(self):
        logging.info('------------teardown')
    @classmethod
    def teardown_class(cls):
        logging.info('------------teardown_calss')



