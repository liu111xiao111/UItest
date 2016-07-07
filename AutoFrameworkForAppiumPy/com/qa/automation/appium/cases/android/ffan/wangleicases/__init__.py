import sys,os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
	os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))))))

sys.path.append(root_dir)

if __name__ == "__main__":
	print("base dir name ",root_dir)