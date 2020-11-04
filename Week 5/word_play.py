""""word_play.py
author: Chase Lewis
created: September 2017
CSCI-141"""

def repeat(curword, word):
    """repeat is to make sure no duplicate words would be printed that have double letters"""
    if len(curword) != len(word)-1:
        return False
    else:
        for i in range (1, len(word)):
            if curword == word[:i-1] + word[i:]:
                return True
        if curword == word[:len(word)-1]:
            return True
        if curword == word[1:]:
            return True
        for i in range (1, len(word)):
            if curword == word[:i-1] + word[i:]:
                return True
    return False

def check_deletions(file, word):
    """check_deletions takes a word and removes only one letter from the word in different variations to see if another word will be made"""
    if word == "":
        print ("No word was entered.")
    else:
        fd = open(file)
        num = 0
        for line in fd:
            curword = line.strip()
            if repeat(curword,word):
                num += 1
                print (num, curword)
        fd.close()
    return num



def main():
    """main runs check_deletions and prompts the user for their inputs
    Example word: track
    Expected deletions words: rack, tack
    File name: test_words.txt"""
    word = input("Enter a word")
    file = input("Enter file name to check words:")
    print("Word Deletions:", check_deletions(file, word))


main()
