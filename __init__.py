# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class HelloWorldSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')

    @intent_handler(IntentBuilder('ThankYouIntent').require('ThankYouKeyword'))
    def handle_thank_you_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("welcome")

    @intent_handler('HowAreYou.intent')
    def handle_how_are_you_intent(self, message):
        """ This is a Padatious intent handler.
        It is triggered using a list of sample phrases."""
        self.speak_dialog("how.are.you")

    @intent_handler(IntentBuilder('HelloWorldIntent')
                    .require('HelloWorldKeyword'))
    def handle_hello_world_intent(self, message):
        """ Skills can log useful information. These will appear in the CLI and
        the skills.log file."""
        self.log.info("There are five types of log messages: "
                      "info, debug, warning, error, and exception.")
        self.speak_dialog("hello.world")
    
    @intent_handler('SchoolEvents.intent')
    def handle_school_events_intent(self, message):
        import random
        import datetime

        current_time = datetime.datetime.now()
        day = current_time.day
        month = current_time.month
        current_date = str(month)+'/'+str(day)
        schooleventslist = {
            '3/25': ['Today is a test date for this program'],
            '3/28': ['Today is Red and Blue Day'],
            '3/30': ['Today is the last day of the third marking period'],
            '4/13': ['Today is there is no school because it is the first day of spring break'],
            '4/14': ['Today there is no school because of spring break'],
            '4/15': ['Today there is no school because of spring break'],
            '4/18': ['Today there is no school because of spring break'],
            '4/27': ['Today there is an early dissmissal'],
            '5/3': ['Today there is no school'],
            '5/17': ['Today there is no school'],
            '5/30': ['Today there is no school']
        }


        try:
            todayevent = random.choice(schooleventslist[str(current_date)])
        except:
            todayevent = 'undefined'


        self.speak(todayevent)

    def stop(self):
        pass


def create_skill():
    return HelloWorldSkill()
