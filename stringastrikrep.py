import sys

def censor(text, word):

	word_list = text.split()

	result = ''
	stars = '*' * len(word)
	index = 0;
	for i in word_list:
		if i == word:
			word_list[index] = stars
		index += 1

	result =' '.join(word_list)

	return result

if __name__== '__main__':

	print =("Enter your story :-) \n")
	msg = sys.stdin.readlines()
	hidden_word = input("Enter the word you want to hide:: \n")

	print("Your story without hidden: ", msg)
	print("The word you want to hide from the above story:  ", hidden_word)

	print("Your story after hidden word: ", censor(msg, hidden_word))
