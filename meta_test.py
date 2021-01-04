import meta

BEFORE = "target.py"
AFTER = "target_converted.py"

def test_convert():
	before_count = 0
	after_count = 0
	meta.convert_str(BEFORE, AFTER)
	with open(BEFORE, "r") as f:
		for line in f.readlines():
			if line.lower().find("hello") >= 0:
				before_count += 1
	with open("target_converted.py", "r") as f:
		for line in f.readlines():
			if line.lower().find("hiya") >= 0:
				after_count += 1
	assert before_count == after_count
