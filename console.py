#!/usr/bin/python3
"""This defines the HBnB console"""
import cmd
import sys
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User


def parse(arg):
    """Parse function for accessing complex argument"""
    curly_brace = re.search(r"\{(.*?)\}", arg)
    parenthesis = re.search(r"\[(.*?)\]", arg)
    if curly_brace is None:
        if parenthesis is None:
            return [i.strip(",") for i in split(arg)]
        else:
            slex = split(arg[:parenthesis.span()[0]])
            retl = [i.strip(",") for i in slex]
            retl.append(parenthesis.group())
            return retl
    else:
        slex = split(arg[:curly_brace.span()[0]])
        retl = [i.strip(",") for i in slex]
        retl.append(curly_brace.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    Define the Airbnb clone command interpreter.
    Attr:
    prompt (str): Command prompt
    """
    prompt = "(hbnb) "
    __classnames = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
    }

    def process_commands(self, commands):
        """Process a list of commands"""
        print(self.prompt)
        self.cmdqueue.extend(commands)

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        usage:
        $ create BaseModel
        """
        argc = parse(arg)
        if len(argc) == 0:
            print("** class name missing **")
        elif argc[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
        else:
            print(eval(argc[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = parse(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_update(self, arg):
        """ Updates and instance based on the class name and id """
        argu = parse(arg)
        obj_dict = storage.all()
        if len(argu) == 0:
            print("** class name missing **")
        elif argu[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
        elif len(argu) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argu[0], argu[1]) not in obj_dict:
            print("** no instance found **")
        elif len(argu) == 2:
            print("** attribute name missing **")
        elif len(argu) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(argu[0], argu[1])
            arg_dict = obj_dict[key].to_dict()
            arg_dict[argu[2]] = argu[3]
            obj_ins = eval(argu[0])(**arg_dict)
            obj_ins.save()
            storage.save()

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file"""
        argd = parse(arg)
        obj_dict = storage.all()
        if len(argd) == 0:
            print("** class name missing **")
        elif argd[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
        elif len(argd) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argd[0], argd[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(argd[0], argd[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        argal = parse(arg)
        if len(argal) > 0 and argal[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
        else:
            obj_all = []
            for obj in storage.all().values():
                if len(argal) > 0 and argal[0] == obj.__class__.__name__:
                    obj_all.append(obj.__str__())
                elif len(argal) == 0:
                    obj_all.append(obj.__str__())
            print(obj_all)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_EOF(self, arg):
        """End of file signal to exit the program"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
