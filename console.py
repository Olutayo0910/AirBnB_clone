#!/usr/bin/python3
""" The console of Console application"""
import cmd


class hbnb(cmd.Cmd):
    """ subclass console of the cmd class """
    prompt = '(hbnb) '

    def default(self, arg):
        """ Overriding method to do nothing"""
        pass

    def do_quit(self, *arg):
        """ Command to quit the console """
        return True

    def do_EOF(self, *arg):
        """ For handling of EOF """
        return True

if __name__ == "__main__":
    hbnb().cmdloop()
