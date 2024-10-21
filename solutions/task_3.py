from random import choice
def learn(dataset: list[str]):
	w = dict()
	w["$"] = []
	for s in dataset:
		words = s.split()
		w["$"].append(words[0])
		for i in range(len(words)-1):
			if words[i] not in w:
				w[words[i]] = []
			w[words[i]].append(words[i+1])
		if words[i+1] not in w:
			w[words[i+1]] = []
		w[words[i+1]].append("^")
	return w


def generate(state) -> str:
	sentence = []
	s = choice(state["$"])
	while s != "^":
		sentence.append(s)
		s = choice(state[s])
	return " ".join(sentence[:])