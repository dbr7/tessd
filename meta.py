import astor
import sys

def convert_str(before, after):
	root = astor.parse_file(before)
	
	after_file = open(after, "w")
	after_file.write(astor.to_source(root))

def main():
	convert_str(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()