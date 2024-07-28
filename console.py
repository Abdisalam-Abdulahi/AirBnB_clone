#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        cmd class
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
