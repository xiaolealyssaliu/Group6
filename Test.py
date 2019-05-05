
import unittest
import love
import complexity
import length
import mood
import kid_safe
 
class Test(unittest.TestCase):
    def test_kid_safe(self): #test for kid_safe
        word1='having sex should receive clear consent; otherwise, doing so may raise legal issues'
        self.assertEqual(kid_safe.kid_safe(word1),0.1)
        word2='there is no trigger word in this sentence'
        self.assertEqual(kid_safe.kid_safe(word2),0.9)
        
    def test_love(self): #test for love function
        word3='I really really really like you. Wonder if you are the same.'
        self.assertEqual(love.love(word3),0.8)
        word4='Hatred is the thing causes inharmony and dispute.'
        self.assertEqual(love.love(word4),0.0)
        
    def test_length(self): #test for length
        word5 ='it is a beautiful night'
        self.assertEqual(length.length(word5),0.0)
        
    def test_mood(self): #test for mood
        word6='I am happy because of the nice weather and fantasitc experience'
        self.assertEqual(mood.mood(word6),0.8)
        word7='I am depressed and i felt so sad'
        self.assertEqual(mood.mood(word7),0.2)
        
    def test_complexity(self): #test for complexity
        word8='this text is simple and short'
        self.assertEqual(complexity.complexity(word8),0.0)
        word9='whether longer sentences or more words indicate greater complexity'
        self.assertEqual(complexity.complexity(word9),0.1)
        
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
# Run each test in suite
unittest.TextTestRunner().run(suite)
