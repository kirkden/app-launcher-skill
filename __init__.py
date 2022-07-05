from mycroft import MycroftSkill, intent_file_handler
import subprocess

class AppLauncher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('launcher.app.intent')
    def handle_launcher_app(self, message):
        app = message.data.get('app')

        self.speak_dialog('launcher.app', data={
            'app': app
        })

        self.log.info("Starting app %s", app)
        aa = subprocess.Popen(app, shell=True)


def create_skill():
    return AppLauncher()

