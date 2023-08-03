#!/usr/bin/python3
"""
Implementing the console for the HBnB project.
"""
import cmd
import json
import shlex
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models

class HBNBCommand(cmd.Cmd):
    """
    Add comments later
    """

    prompt = ("(hbnb) ")
    def do_quit(self, args):
        """
        Add comments later
        """
        return True

    def do_EOF(self, args):
        """
        add comments later
        """
        return True

    def do_create(self, args):
        """add comments later"""
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            try:
                args = shlex.split(args)
                new_instance = eval(args[0])()
                new_instance.save()
                print(new_instance.id)

            except:
                print("** class doesn't exist **")
        else:
            try:
                args = shlex.split(args)
                name = args.pop(0)
                obj = eval(name)()
                for arg in args:
                    arg = arg.split('=')
                    if hasattr(obj, arg[0]):
                        try:
                            arg[1] = eval(arg[1])
                        except:
                            arg[1] = arg[1].replace('_',' ')
                        setattr(obj, arg[0], arg[1])

                obj.save()
            except:
                return
            print(obj.id)
    def do_show(self, args):
        """
        add comments later
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        #
        models.storage.reload()
        obj_dict = models.storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        add comments later
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        #
        models.storage.reload()
        obj_dict = models.storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        models.storage.save()

    def do_all(self, args):
        """
        adds comments later
        """
        obj_list = []
        models.storage.reload()
        objects = models.storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)

        print(obj_list)

    def do_update(self, args):
        """adds comments later"""
        models.storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = models.storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

    def emptyline(self):
        """adds comments later"""
        pass

    def do_count(self, args):
        """adds comments later"""
        obj_list = []
        models.storage.reload()
        objects = models.storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))

    def default(self, args):
        """
        adds comments later
        """
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except:
            print("*** Unknown syntax:", args[0])


if __name__ == "__main__":
    """
    adds comments later
    """
    HBNBCommand().cmdloop()