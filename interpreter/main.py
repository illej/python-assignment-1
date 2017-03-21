from controller import Controller
from cmdview import CmdView
from fileview import FileView
from _parser import _Parser
from validator import Validator
from database import Database
from visualiser import Visualiser


if __name__ == "__main__":
    parser = _Parser()
    cmd_view = CmdView()
    file_view = FileView()
    validator = Validator()
    db = Database("test.db")
    vis = Visualiser()

    con = Controller(cmd_view, file_view, parser, validator, db, vis)
    cmd_view.set_controller(con)

    # run program
    cmd_view.cmdloop()

# TODO: Work in progress

# [x] 3. help commands TODO: finish all
# [x] 5. validation
    # TODO: age / date
    # TODO: use other data sets
# [x] 8. Raise exceptions
    # TODO: implement all
# [x] 9. Amount of error trapping & handling TODO: implement all
# [x] 10. doctests (at least 3)
    # TODO:
        # fileview 2
        # parser 4
# [x] 11. unittests (at least 3)
    # TODO:
        # parser 3
        # db 1
# [x] 12. breadth of test coverage (10 combined doc + unit)



# FINISHED
# [x] 1. command-line arguments TODO: implement -g -v -c (get, validate and commit)
# [x] 2. cmd module
# [x] 4. change options TODO: implement all
# [x] 6. object persistence / object serialization
# [x] 7. load data from file
    # TODO: serialized
# [x] 13. directories and file locations
# [x] 14. charts
# [x] 15. save and read to and from database
    # TODO: inherit from View (low prio)










