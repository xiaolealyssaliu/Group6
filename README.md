
Group 6: Content Intended for Tools for Analytics Class
zz2570, xl2863

What is it?

This set of code extracts the given information from the songs and lyrics, including its name, id and singer. At the same time, the code contains analysis on the lyrics (contents).It aims to generate a separate score (from 0.0 to 1.0 with step 0.1) in terms of its length, mood, kid-safety,love expressions and choice of vocalulary.

Main Features and algorithm explanation:
Length: The longer the sone, the higher the socre will be within 0.0 and 1.0 range. We split the lyrics and count the words. Given predetermined score for different length ranges (eg. <80, 80-100 and so on), different scores were assigned to lyrics with various length.

Love: We use textblob to remove stopwords. Given a prefixed set of love words, if the lyric contains more words in the set, it receives a higher score. We then normalize the score to 0 to 1.

Mood: We Use textblob to conduct sentiment analysis and then normalize the score.
Complexity: We Use textstat package to determine the readability of the lyrics. The higher socre indicates less easiness to read.

Kid_Safe: We Use textblob to get rid of stop word. Given a prefixed set of dirty words, the higher score indicates fewer use of the words. We then normalize the score to 0 to 1.

Where to get it:
The Sourcecode is currently hold on GitHub at: git@github.com:xiaolealyssaliu/Group6.git




