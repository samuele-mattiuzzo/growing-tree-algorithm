#!/usr/bin/python
import os, sys
from GT.growing_tree import GrowingTree

def main():
	gt = GrowingTree(10,10)
	gt.generate()
	for l in gt.as_matrix():
		print " ".join([str(s) for s in l])

if __name__ == "__main__":
	main()