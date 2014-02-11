def repeat(s, exclaim):
	"""This is a test comment. It won't be executed.
	"""
	"""This is another comment.
	"""

	result = s + s + s
	if exclaim:
		result = result + '!!!'
	return result

def main():
    print repeat('Yay', False)      ## YayYayYay
    print repeat('Woo Hoo', True)   ## Woo HooWoo HooWoo Hoo!!!

if __name__ == '__main__':
    main()