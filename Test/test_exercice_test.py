import unittest
import os
from exercice_test import multiply_by_42_then_pow, min_divide , pick_a_letter , write_file

class TestAddWithUnittest(unittest.TestCase):
       
    def test_multiply_by_42_then_pow(self):
        self.assertEqual(multiply_by_42_then_pow(2,4), 49787136)
        with self.assertRaises(TypeError):
            multiply_by_42_then_pow('a',2)
        with self.assertRaises(TypeError):
            multiply_by_42_then_pow('a','b')
        self.assertEqual(multiply_by_42_then_pow(4,-5), 7.472287811932173e-12)
        self.assertEqual(multiply_by_42_then_pow(0,0), 1)
        
    def test_min_divide(self):
         list1 = {3, 5, 7, 85}
         list2 = {"a" , "b" , "c" , "d"}
         self.assertEqual(min_divide(list1, 8), 2.6666666666666665)
         self.assertEqual(min_divide(list1, 0), 0.0)
         with self.assertRaises(TypeError):
            min_divide(list2, 0)
            
    def test_pick_a_letter(self):
         self.assertIsInstance(pick_a_letter("thomas"), str)
         with self.assertRaises(TypeError):
            pick_a_letter(3343)
            
    def test_write_file(self):
        write_file("test.txt","cc")
        self.assertTrue(os.path.exists("test.txt")) # vérifie si le fichier a été créé
        with open("test.txt", "r") as fichier:
            content = fichier.read()
            self.assertEqual(content, "cc") # vérifie si le contenu du fichier est celui attendu
         
     
         
        
        
    