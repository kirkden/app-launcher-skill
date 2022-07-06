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
            self.speak_dialog('launcher.app', data={
                'app': app
            })
            subprocess.call("{} &".format(app), shell=True)
        else:
            self.speak_dialog('launcher.app.not.exist', data={
                'app': app})
            print("Does not Exist")

    @intent_file_handler('launcher.app.close.intent')
    def handle_launcher_app_close(self, message):
        app = message.data.get('app')

        self.log.info("Closing app %s", app)
        
def create_skill():
    return AppLauncher()

