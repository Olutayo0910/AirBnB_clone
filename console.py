#!/usr/bin/python3
""" The console of Console application"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ subclass console of the cmd class """
    prompt = '(hbnb) '

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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
