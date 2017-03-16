from controller import Controller
from cmdview import CmdView
from _parser import _Parser
from validator import Validator
from database import Database
from visualiser import Visualiser

if __name__ == "__main__":
    parser = _Parser()
    cmd_view = CmdView()
    validator = Validator()
    db = Database("test.db")
    vis = Visualiser()
    con = Controller(cmd_view, parser, validator, db, vis)
    cmd_view.set_controller(con)
    # run program
    cmd_view.cmdloop()

# TODO: implement exception handling