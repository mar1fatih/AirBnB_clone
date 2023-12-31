#!/usr/bin/python3
"""class cmd console.py"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parse(args):
    """parsing commandes to use it as commande"""
    return [arg for arg in shlex.split(args)]


class HBNBCommand(cmd.Cmd):
    """class cmd attributes : prompt"""

    __classes = {
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"}
    prompt = "(hbnb) "

    def emptyline(self):
        """dont do anything just press enter"""
        pass

    def do_EOF(self, line):
        """EOF to exit the program\n"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, classname):
        """Usage: create <class>
        create a new instance
        """
        if not classname:
            print("** class name missing **")
            return
        args = parse(classname)
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        print(eval(args[0])().id)
        storage.save()

    def do_show(self, classname):
        """Usage: show <class> <id>
        Prints the string representation of an instance
        """
        if not classname:
            print("** class name missing **")
            return
        args = parse(classname)
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objects = storage.all()
        if "{}.{}".format(args[0], args[1]) in objects:
            print(objects["{}.{}".format(args[0], args[1])])
        else:
            print("** no instance found **")

    def do_destroy(self, classname):
        """Usage: destroy <class> <id>
        Deletes an instance based on the class name and id
        """
        if not classname:
            print("** class name missing **")
            return
        args = parse(classname)
        objects = storage.all()
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects.keys():
            print("** no instance found **")
        else:
            del objects["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, classname):
        """Usage: all or all <class>
        Prints all string representation
        """
        objects = storage.all()
        args = parse(classname)
        if not classname:
            obj = []
            for v in objects.values():
                obj.append(v.__str__())
            print(obj)
        elif len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = []
            for v in objects.values():
                if v.__class__.__name__ == args[0]:
                    obj.append(v.__str__())
            print(obj)

    def do_update(self, classname):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Updates an instance based on the class name and id
        """
        args = parse(classname)
        objects = storage.all()
        if not classname:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        elif args[2] in ["id", "created_at", "updated_at"]:
            pass
        else:
            obj = objects["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                typ = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = typ(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
