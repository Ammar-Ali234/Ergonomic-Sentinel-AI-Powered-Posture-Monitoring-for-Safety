from roboflow import Roboflow
rf = Roboflow(api_key="USE YOU API KEY")
project = rf.workspace("ammar-ali-mjlhi").project("ppe-qyupq-xqj3i")
version = project.version(1)
dataset = version.download("yolov11")
                