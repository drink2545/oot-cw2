from command import Nocommand

class remote():
    def __init__(self):
        do_noting = Nocommand()
        self.on_slot = [do_noting,
                        do_noting,
                        do_noting,
                        do_noting,
                        do_noting]
        self.off_slot = [do_noting,
                        do_noting,
                        do_noting,
                        do_noting,
                        do_noting]
        self.undo_but = do_noting

    def set_command(self, slot_pos, on, off):
        self.on_slot[slot_pos] = on
        self.off_slot[slot_pos] = off

    def on_click(self, slot_pos):
        self.on_slot[slot_pos].execute()
        self.undo_but = self.on_slot[slot_pos]
    
    def off_click(self, slot_pos):
        self.off_slot[slot_pos].execute()
        self.undo_but = self.off_slot[slot_pos]

    def undo_click(self):
        self.undo_but.undo()
