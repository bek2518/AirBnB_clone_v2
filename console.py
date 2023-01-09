#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def _parser(self, args):
        new_dict = dict()
        for arg in args:
            if "=" in arg:
                key_value = arg.split('=', 1)
                key = key_value[0]
                value = key_value[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
            else:
                try:
                    value = int(value)
                except:
                    try:
                        value = float(value)
                    except:
                        continue
            new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """ Create an object of any class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in HBNBCommand.classes:
            new_dict = self._parser(args[1:])
            new_instance = HBNBCommand.classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return
        print(new_instance.id)
        new_instance.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        '''
        Prints the string representation of an instance
        Based on the class name and the id
        '''
        args = args.split()
        if not args or len(args) == 0 or args[0] == "":
            print("** class name missing **")

        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(args) == 1 or args[1] == "":
            print("** instance id missing **")

        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        '''
        Deletes an instance based on the class name and id
        '''
        args = args.split()
        if not args or len(args) == 0 or args[0] == "":
            print("** class name missing **")

        elif args[0] not in class_list:
            print("** class doesn't exist **")

        elif len(args) == 1 or args[1] == "":
            print("** instance id missing **")

        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        '''
        Prints all representation of all instances
        based or not on the class name'''
        args = args.split()
        objects = storage.all()
        if not args:
            value_list = []
            for key, value in objects.items():
                value_list.append(str(objects[key]))
            if value_list:
                print(value_list)
        else:
            value_list = []
            for key, value in objects.items():
                if value.__class__.__name__ == args[0]:
                    value_list.append(str(objects[key]))
            if value_list:
                print(value_list)
            else:
                print("** class doesn't exist **")

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        '''
        Updates an instance based on the class name and id
        by adding or updating an attribute
        '''
        args = args.split()
        objects = storage.all()

        if not args or len(args) == 0 or args[0] == "":
            print("** class name missing **")

        elif args[0] not in class_list:
            print("** class doesn't exist **")

        elif len(args) == 1 or args[1] == "":
            print("** instance id missing **")

        elif len(args) == 2 or args[2] == "":
            print("** attribute name missing **")

        elif len(args) == 3 or args[3] == "":
            print("** value missing **")

        else:
            for key, value in objects.items():
                existing_key = args[0] + "." + args[1]
                if key == existing_key:
                    attribute = args[3].split('"')
                    t = value_type(attribute[1])
                    objects[existing_key].__dict__[args[2]] = (t)(attribute[1])
                    objects[existing_key].updated_at = datetime.now()
                    storage.save()
                    return
                else:
                    print("** no instance found **")

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

    def default(self, args):
        command = {
            'all': self.do_all,
            'count': self.do_count,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update
        }
        args = args.replace("(", ".")
        args = args.replace(")", ".")
        args = args.replace('"', "")
        args = args.replace(",", "")
        args = args.split(".")

        if args[0] not in class_list:
            print("** class doesn't exist **")

        elif args[1] not in command:
            print("** command doesn't exist **")

        else:
            if len(args) == 4:
                cmd_arg = args[0] + " " + args[2]
                cmd = command[args[1]]
                cmd(cmd_arg)

            elif len(args) == 5:
                cmd_arg = args[0] + ", " + args[2] + ", " + args[3]
                cmd = command[args[1]]
                cmd(cmd_arg)

            elif len(args) == 6:
                cmd_arg = args[0] + " " + args[2]
                + " " + args[3] + " " + args[4]
                cmd = command[args[1]]
                cmd(cmd_arg)

    def do_count(self, args):
        count = 0
        objects = storage.all()
        for key, value in objects:
            temp = key.split('.', 1)
            if temp[0] == args:
                count += 1
        print(count)


def value_type(value):
    '''
    Determines the value type
    '''
    try:
        int(value)
        return (int)
    except ValueError:
        pass
    try:
        float(value)
        return (float)
    except ValueError:
        return (str)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
