import json , os

class Config:
    def update_config(self, new_config):
        open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.json'),"w+").write(json.dumps(new_config))

    def get_config(self):
        try:
            return json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.json'),'r'))
        except:
            return {}
