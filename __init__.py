from mycroft import MycroftSkill, intent_file_handler
import subprocess

class AppLauncher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('launcher.app.intent')
    def handle_launcher_app(self, message):
        app = message.data.get('app')

        exists = subprocess.Popen("which {}".format(app),
                                    stdout=subprocess.PIPE,
                                    shell=True).stdout.read()

        exists = exists.decode("utf-8")
        self.log.info("Starting app %s", exists)
        
        if(exists != ''):
            subprocess.call("{} &".format(app), shell=True)
        else:
            print("Does not Exist")

        self.speak_dialog('launcher.app', data={
            'app': app
        })




def create_skill():
    return AppLauncher()

