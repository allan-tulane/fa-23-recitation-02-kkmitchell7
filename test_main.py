from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 10) == 12
	assert simple_work_calc(20, 12, 2) == 25052
	assert simple_work_calc(30, 6, 2) == 2316
	assert simple_work_calc(40, 2, 2) == 224
	assert simple_work_calc(100, 1, 2) == 197
	assert simple_work_calc(45, 3, 2) == 750

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(40, 5, 2,lambda n: 1) == 3906
	assert work_calc(50, 2, 6, lambda n: n*n) == 2632
	assert work_calc(65, 2, 2, lambda n: n*n*n) == 361985
