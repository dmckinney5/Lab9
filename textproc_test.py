#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")
        
    def test_isString(self):
        notText = 13579
        self.assertRaises(textproc.TextProcError, textproc.Processor, notText)
        
    def test_count(self):
        text =abcdef
        text1 = textproc.Processor(text).count()
        self.assertEqual(text1, 6, "Wrong Length")
        
    def test_count_alpha(self):
        tigers = "tigers555"
        tigers1 = textproc.Processor(tigers).count_alpha()
        self.assertEqual(tigers1, 6, "Wrong Length")
        
    def test_count_numeric(self):
        inverseTigers = "tigers555"
        tigers1 = textproc.Processor(tigers1).count_numeric()
        self.assertEqual(tigers1, 3, "Wrong Length") 
    
    def test_count_vowels(self):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha1 = textproc.Processor(alpha).count_vowels()
        self.assertEqual(alpha1, 5, "Wrong Vowels")
        
    def test_is_phonenumber(self):
        phone = "303-587-7030"
        phone1 = textproc.Processor(phone).is_phonenumber()
        self.assertTrue(phone1)

    # Add Your Test Cases Here...

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
