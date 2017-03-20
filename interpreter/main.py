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

# TODO: implement exception handling
# TODO: do_function to query db
# TODO: merge parser and validator? what is parser even doing if the db is holding the data????

# [ ] 1. command-line arguments TODO: almost!
# [x] 2. cmd module
# [x] 3. help commands TODO: implement all
# [x] 4. change options TODO: implement all
# [x] 5. validation TODO: age / date
# [ ] 6. object persistence / object serialization
# [x] 7. load data from file
# [x] 8. Raise exceptions TODO: implement all
# [x] 9. Amount of error trapping & handling TODO: implement all
# [x] 10. doctests (at least 3) TODO: 1 / 3 done
# [ ] 11. unittests (at least 3)
# [ ] 12. breadth of test coverage (10 combined doc + unit)
# [ ] 13. directories and file locations
# [x] 14. charts TODO: hard coded -> make work better
# [x] 15. save and read to and from database TODO: finish reading from db
