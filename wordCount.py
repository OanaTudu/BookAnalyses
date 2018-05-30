"""main function to count words in a file, with
implemented helper functions:
print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2

For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
by frequency"""

import sys

def words_from_file(filename):
    words = []
    f = open(filename, 'r')
    for line in f:
        
        words = words + line.lower().split()
    
    dict_words = {}
    for w in words:
        if w not in dict_words:
            dict_words[w] = 1;
        else:
            dict_words[w] += 1;
    f.close()
    return dict_words

def print_words(filename):
    this_dict = words_from_file(filename)
    #print(this_dict)
    for  (word,occurance)  in this_dict.items():
      print('{:15}{:3}'.format(word,occurance))

def print_top(filename):
    this_dict = words_from_file(filename)
    new_dict = sorted(this_dict.items(), key=lambda x: x[1],reverse = True )[:20]
    print(new_dict)
    for (word,occurance) in new_dict:
      print('{:15}{:3}'.format(word,occurance))



###

# Main function will call print_words() if the flag is --count, and 
# print_top() if the flag is --topcount

def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
