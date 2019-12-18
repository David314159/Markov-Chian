import random
import os
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def file_list_parse(filename):
	out = []
	with open(filename, "r") as f:
		for lineIdx, line in enumerate(f):
			out.append([])
			for word in line.split():
				out[lineIdx].append(word);
	return out

def list_map_parse(flist):
	out = {}
	for line in flist:
		for idx, word in enumerate(line):
			if word not in out:
				out[word] = {}
			try:
				nextWord = line[idx+1]
				if nextWord not in list(out[word].keys()):
					out[word][nextWord] = 1
				else:
					out[word][nextWord] += 1
			except IndexError:
				pass
	return out

def choose(myMap):
	choices = []

	for key in myMap:
		for i in range(myMap[key]):
			choices.append(key)

	random.shuffle(choices)

	return choices[0]

def main(filename, times):
	clear()
	for i in range(times):
		print('Sentence #' + str(i+1))
		myMap = list_map_parse(file_list_parse(filename))
		curr = file_list_parse(filename)[0][0]
		while True:
			try:
				print(curr + " ", end = "")
				curr = choose(myMap[curr])
			except IndexError:
				break

		print('\n')

main("data.txt", 5)
			 
