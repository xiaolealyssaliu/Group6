import unittest
class Test(unittest.TestCase):
    def test_kid_safe(self):
        word1='having sex should receive clear consent; otherwise, doing so may raise legal issues'
        self.assertEqual(kid_safe(word1),0.1)
        word2='there is no trigger word in this sentence'
        self.assertEqual(kid_safe(word2),0.9)
    def test_love(self):
        word3='I really really really like you. Wonder if you are the same.'
        self.assertEqual(test_love(word3),0.8)
        word4='Hatred is the thing causes inharmony and dispute.'
        self.asserEqual(test_love(word4),0.0)
    def test_length(self):
        word5 ='it is a beautiful night'
        self.assertEqual(test_length(word5),0.0)
    def test_mood(self):
        word6='I am happy because of the nice weather and fantasitc experience'
        self.assertEqual(test_mood(word6),0.8)
        word7='I am depressed and i felt so sad'
        self.assertEqual(test_mood(word7),0.2)
    def test_complexity(self):
        word8='this text is simple and short'
        self.assertEqual(test_complexity(word8),0.0)
        word9='whether longer sentences or more words indicate greater complexity'
        self.assertEqual(test_complexity(word9),0.1)
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
# Run each test in suite
unittest.TextTestRunner().run(suite)
