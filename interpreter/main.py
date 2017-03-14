from controller import Controller
from cmdview import CmdView
from calculator import Calculator

if __name__ == "__main__":
    calc = Calculator()
    cmd_view = CmdView()
    con = Controller(cmd_view, calc)
    cmd_view.set_controller(con)
    # run program
    cmd_view.cmdloop()
