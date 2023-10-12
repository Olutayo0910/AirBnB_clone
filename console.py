#!/usr/bin/python3
""" The console of Console application"""
import cmd
import sys
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


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
        for command in commands:
            self.onecmd(command)

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

    def emptyline(self):
        """ Overriding method to do nothing"""
        pass

    def do_quit(self, *arg):
        """ Command to quit the console """
        return True

    def do_EOF(self, *arg):
        """ For handling of EOF """
        self.emptyline()
        return True


if __name__ == '__main__':
    hbnb_command = HBNBCommand()

    """Check if input is coming from a pipe (non-interactive mode)"""
    if not sys.stdin.isatty():
        """Read commands from standard input"""
        commands = sys.stdin.read().splitlines()
        hbnb_command.process_commands(commands)
    else:
        hbnb_command.cmdloop()
