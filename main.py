#!/usr/bin/python
import os, sys
from GT.growing_tree import GrowingTree

def main():
	gt = GrowingTree(10,10)
	gt.generate()
	print gt.as_array()

if __name__ == "__main__":
	main()