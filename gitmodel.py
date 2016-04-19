from yhat import Yhat, YhatModel , preprocess

class HelloWorld(YhatModel):
    @preprocess(in_type=dict, out_type=dict)
    def execute(self, data):
        me = data['name']
        greeting = "Hello " + str(me) + "!"
        return { "greeting": greeting }

yh = Yhat("colin", "2463b3c71264ef61de1f6af8338d22e7", "https://sandbox.yhathq.com/")
yh.deploy("Gitmodel", HelloWorld, globals(),True)