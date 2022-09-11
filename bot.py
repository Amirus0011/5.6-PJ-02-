import re
import reque
import time

class Telebot(object):

    def __init__(self, import_name):
        self.import_name = import_name
        self.update_rules = list()
        self.config = dict(
            api_key=None,
            requests_kwargs=dict(
                timeout=60,
            ),
        )
        self.offset = 0
        self.whoami = None

    def add_update_rule(self, rule, endpoint=None, view_func=None, **options):
        self.update_rules.append(dict(
            rule=re.compile(rule),
            endpoint=endpoint,
            view_func=view_func,
            options=dict(**options),
        ))

    def route(self, rule, **options):