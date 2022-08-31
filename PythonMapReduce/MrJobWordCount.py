from mrjob.job import MRJob

class WordCount(MRJob):
    def mapper(self, key, value):
        words = value.split()
        for word in words:
            yield(word, 1)

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    WordCount.run()

# Homework
# Q1. find out how many words starts with 'h'
# Q2. find out word with max count
# Q3. find out word with max length
