#!/usr/bin/python3
"""doc"""
import cmd
from models import storage


class sprntr(cmd.Cmd):
    """doc"""
    prompt = 'sprntr '

    def emptyline(self, arg):
        """empty line"""
        pass

    def do_EOF(self, arg):
        """EOF"""
        return True

    def do_create(self, arg):
        """create"""
        if self.checkClassName(arg) is False:
            return False

        args = arg.split()
        className = args[0]
        model = globals()[className]()
        model.save()
        print(model.id)

        return True

    def do_all(self, arg):
        """all"""
        args = arg.split()
        instances = []
        className = args[0]

        if className not in globals():
            print("** class doesn't exist **")
            return False

        for key, value in storage.all().items():
                if value.__class__.__name__ == className:
                    instances.append(value.__str__())


if __name__ == '__main__':
    sprntr().cmdloop()
