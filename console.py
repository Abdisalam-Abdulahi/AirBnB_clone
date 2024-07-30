#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models
import sys
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
        cmd class
    """

    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel,  'User': User}
    """
    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City}
    """

    def do_quit(self, inst):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, inst):
        """
        Exit the program
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        if len(args) == 0:
            print("** class name missing **")
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            getCls = getattr(sys.modules[__name__], args)
            inst = getCls()
            print(inst.id)
            models.storage.save()
        return

    def do_show(self, args):
        li = [args]
        li = li[0].split()
        if len(li) == 0:
            print("** class name missing **")
        elif li[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(li) == 1:
            print("** instance id missing **")
        else:
            dicti = models.storage.all()
            nameID = li[0] + "." + str(li[1])
            if nameID in dicti:
                print(dicti[nameID])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, args):
        li = [args]
        li = li[0].split()
        if len(li) == 0:
            print("** class name missing **")
        elif li[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(li) == 1:
            print("** instance id missing **")
        else:
            dicti = models.storage.all()
            nameID = li[0] + "." + str(li[1])
            if nameID in dicti:
                del dicti[nameID]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        tkn = [args]
        tkn = tkn[0].split()
        li = []
        dicti = models.storage.all()
        if args not in self.classes:
            print("** class doesn't exist **")
        elif len(tkn) == 0:
            for val in dicti:
                middleCls = str(dicti[val])
                li.append(middleCls)
            print(li)
            return

        else:
            # Representation for a specific class
            middleCls = ""
            for key in dicti:
                className = key.split('.')
                if className[0] == tkn[0]:
                    # This form doesn't work
                    # listI.append(dic[key])
                    middleCls = str(dicti[key])
                    li.append(middleCls)
            # if listI:
            print(li)

    def do_update(self, args):
        li = [args]
        li = li[0].split()
        if len(li) == 0:
            print("** class name missing **")
        elif li[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(li) == 1:
            print("** instance id missing **")
        elif len(li) == 2:
            print("** attribute name missing **")
        elif len(li) == 3:
            print("** value missing **")
        else:
            dicti = models.storage.all()
            nameId = li[0] + "." + str(li[1])
            if nameId in dicti:
                t = dicti[nameId]
                att = li[2]
                value = li[3]
                setattr(t, att, value)
                # print(li[2], li[3])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
