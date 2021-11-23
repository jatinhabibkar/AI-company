from module import Process
import time
localtime = time.asctime( time.localtime(time.time()) )
fn="P00X000-2019092701422.xml"
im="P00X000-2019092701422.jpg"

ps=Process()


ps.get_data_xml(ps.read_xml_obj(fn), im,fn,localtime)