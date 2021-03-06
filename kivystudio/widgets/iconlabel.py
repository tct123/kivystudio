from kivy.uix.label import Label
from kivy.uix.behaviors import ToggleButtonBehavior, ButtonBehavior
from kivy import properties as prop
from kivy.lang import Builder

from kivystudio.behaviors import HoverBehavior, HoverInfoBehavior

class IconLabel(HoverInfoBehavior, Label):
    icon = prop.StringProperty('')
    icon_size = prop.NumericProperty(16)

    def __init__(self, **k):
        super(IconLabel, self).__init__(**k)
        self.markup=True


class IconLabelButton(ButtonBehavior, IconLabel):
    pass

class IconToggleLabel(ToggleButtonBehavior, IconLabel):
    
    icon_down = prop.StringProperty()
    icon_normal = prop.StringProperty()
    
    def on_state(self, *args):
        if self.state=='down':
            self.icon = self.icon_down
        else:
            self.icon = self.icon_normal

Builder.load_string('''
<IconLabel>:
    text: '%s'%(icon(self.icon, self.icon_size)) if self.icon else ''

''')