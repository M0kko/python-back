def play(words: list[str]) -> list[int]:
	err = []
	s = words[0]
	for i in range(1, len(words)):
		if words[i] in words[:i] or s[-1] != words[i][0]:
			err.append(i+1)
		else:
			s = words[i]
	return err