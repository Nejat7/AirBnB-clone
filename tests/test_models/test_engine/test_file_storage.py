#!/usr/bin/python3
<<<<<<< HEAD
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
=======
"""Module test_file_storage
This Module contains a tests for FileStorage Class
"""

import inspect
import json
import os
import unittest

import pycodestyle
from models.engine import file_storage
from tests.test_models.test_base_model import BaseModel

FileStorage = file_storage.FileStorage


class TestFileStorageDocsAndStyle(unittest.TestCase):
    """Tests FileStorage class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            [
                "models/engine/file_storage.py",
                "tests/test_models/test_engine/test_file_storage.py"
            ])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_methods_docstring(self):
        """Tests whether the class methods are documented"""
        funcs = inspect.getmembers(FileStorage, inspect.isfunction)
        for func in funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(FileStorage.__name__, "FileStorage")


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage Class"""

    def setUp(self):
        """initial configuration for tests"""
        self.file_path = "file.json"
        with open(self.file_path, 'w') as f:
            json.dump({}, f)
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """cleanup test files"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_a_dictionary(self):
        """tests wether the instance method 'all' returns a valid dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_instance_obj_to_dict_of_objects(self):
        """tests wether the instance method 'new' adds new object"""
        temp_obj = BaseModel()
        self.storage.new(temp_obj)
        key = f"{temp_obj.__class__.__name__}.{temp_obj.id}"
        self.assertIn(key, self.storage.all().keys())

    def test_save_method_saves_objects_to_file(self):
        """tests wether the save method saves objects to file"""
        expected_objects = {}
        for _ in range(4):
            bs_mdl = BaseModel()
            self.storage.new(bs_mdl)
            key = f"{bs_mdl.__class__.__name__}.{bs_mdl.id}"
            expected_objects[key] = bs_mdl.to_dict()

        self.storage.save()

        self.assertTrue(os.path.exists(self.file_path))
        self.assertGreater(os.path.getsize(self.file_path), 0)
        with open(self.file_path, 'r') as f:
            objects = {k: v
                       for k, v in json.load(f).items()}

        self.assertDictEqual(expected_objects, objects)

    def test_reload_method_reloads_saved_objects(self):
        """test wether the reload method correctly loads objects from file"""
        expected_objects = {}
        for _ in range(4):
            bs_mdl = BaseModel()
            self.storage.new(bs_mdl)
            key = f"{bs_mdl.__class__.__name__}.{bs_mdl.id}"
            expected_objects[key] = bs_mdl.to_dict()

        self.storage.save()
        self.storage.reload()
        saved_objects = self.storage.all()

        saved_objects_dict = {k: v.to_dict() for k, v in saved_objects.items()}
        self.assertEqual(expected_objects, saved_objects_dict)

    def test_reload_method_does_not_do_anything_for_non_existent_file(self):
        """reload does not do anything if the file does not exist"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        expected_objects = {}
        for _ in range(4):
            bs_mdl = BaseModel()
            self.storage.new(bs_mdl)
            key = f"{bs_mdl.__class__.__name__}.{bs_mdl.id}"
            expected_objects[key] = bs_mdl.to_dict()

        self.storage.reload()
        existing_objects = self.storage.all()

        existing_objects_dict = {k: v.to_dict()
                                 for k, v in existing_objects.items()}
        self.assertEqual(expected_objects, existing_objects_dict)
>>>>>>> master
