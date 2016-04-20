from yhat import Yhat, YhatModel , preprocess
import os
USERNAME = os.environ["USERNAME"]
APIKEY = os.environ["APIKEY"]
URL = os.environ["PROD_URL"]

class HelloWorld(YhatModel):
    @preprocess(in_type=dict, out_type=dict)
    def execute(self, data):
        me = data['name']
        greeting = "Hello " + str(me) + "!"
        return { "greeting": greeting }

yh = Yhat(USERNAME, APIKEY, URL)
yh.deploy("Gitmodel", HelloWorld, globals(),True)