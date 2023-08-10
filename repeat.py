# def repeat(text, reps=2):
# 	return f"{text}\n" * reps
#
# text = input("Enter text:")
# print(repeat(text))

print("===============")

#using if __name__ == '__main__':
def repeat2(text, reps=2):
	return f"{text}\n" * reps

if __name__ == '__main__':

	text = input("Enter text:")
	print(repeat2(text))
