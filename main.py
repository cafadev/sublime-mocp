import sublime
import sublime_plugin
import subprocess


class Mocp(sublime_plugin.WindowCommand):

    def run(self, action):
        if action is None:
            return

        subprocess.Popen(['mocp', action], shell=False)
