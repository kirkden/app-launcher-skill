from mycroft import MycroftSkill, intent_file_handler


class AppLauncher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('launcher.app.intent')
    def handle_launcher_app(self, message):
        app = message.data.get('app')
        self.log.info("This is an info level log message.")

        self.speak_dialog('launcher.app', data={
            'app': app
        })


def create_skill():
    return AppLauncher()

