from controller import Controller
from cmdview import CmdView
from _parser import _Parser
from validator import Validator

if __name__ == "__main__":
    parser = _Parser()
    cmd_view = CmdView()
    validator = Validator()
    con = Controller(cmd_view, parser, validator)
    cmd_view.set_controller(con)
    # run program
    cmd_view.cmdloop()

    print()