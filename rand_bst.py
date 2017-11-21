#!/usr/bin/python

###############################################
# module: rand_bst.py
# description: starter code for HW09 w/ unit  tests
# Silvia Smith
# A01396094
###############################################

from BSTNode import BSTNode
from BSTree import BSTree
import random
#import matplotlib.pyplot as plt
#import numpy as np

def gen_rand_bst(num_nodes, a, b):
    #generate random BSTs a, b = range
    tree=BSTree()
    for x in xrange(num_nodes):
        while not tree.insertKey(random.randint(a, b)):
            #nothin' to do here...
            a = a
    return tree        

def estimate_list_prob_in_rand_bsts_with_num_nodes(num_trees, num_nodes, a, b):
    #returns probability of random BST being a list
    #generate num_trees each with num_nodes in a,b
    num_lists=0
    listlist=[]
    for x in xrange(num_trees):
        tree=gen_rand_bst(num_nodes, a, b)
        if tree.isList():
            num_lists +=1
            listlist.append(tree)
    prob = float(num_lists)/num_trees
    return(prob, listlist)

def estimate_list_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_trees, a, b):
    d = {}
    for num_nodes in xrange(num_nodes_start, num_nodes_end+1):
        d[num_nodes] = estimate_list_prob_in_rand_bsts_with_num_nodes(num_trees, num_nodes, a, b)
    return d

def estimate_balance_prob_in_rand_bsts_with_num_nodes(num_trees, num_nodes, a, b):
    num_lists=0
    listlist=[]
    for x in xrange(num_trees):
        tree=gen_rand_bst(num_nodes, a, b)
        if tree.isBalanced():
            num_lists +=1
            listlist.append(tree)
    prob = float(num_lists)/num_trees
    return(prob, listlist)

def estimate_balance_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_trees, a, b):
    d = {}
    for num_nodes in xrange(num_nodes_start, num_nodes_end+1):
        d[num_nodes] = estimate_balance_prob_in_rand_bsts_with_num_nodes(num_trees, num_nodes, a, b)
    return d

def plot_rbst_lin_probs(num_nodes_start, num_nodes_end, num_trees):
    ## your code
    pass

def plot_rbst_balance_probs(num_nodes_start, num_nodes_end, num_trees):
    ## your code
    pass

### ========== UNIT TESTS =============

## unit_test_01 tests BSTNode constructor
##           5
##          /  \
##         3    10
def unit_test_01():
    r = BSTNode(key=5)
    lc = BSTNode(key=3)
    rc = BSTNode(key=10)
    print('root=%s, lc=%s, rc=%s' % (r, lc, rc))
    r.setLeftChild(lc)
    r.setRightChild(rc)
    assert ( r.getLeftChild().getKey()   == 3 )
    assert ( r.getRightChild().getKey() == 10 )

## unit_test_01() contstructs two bst's.
## bst
##        10
##       /  \
##      3   20
##
## bst2
##        5
##       /
##     3
##       \
##        4
def unit_test_02():
    bst = BSTree()
    bst.insertKey(10)
    bst.insertKey(3)
    bst.insertKey(20)
    assert ( bst.isBalanced() )
    assert ( bst.heightOf() == 1 )
    assert ( not bst.isList() )
    print('displaying bst')
    bst.displayInOrder()
    print('-------')

    bst2 = BSTree()
    bst2.insertKey(5)
    bst2.insertKey(3)
    bst2.insertKey(4)
    assert ( not bst2.isBalanced() )
    assert ( bst2.heightOf() == 2 )
    assert ( bst2.isList() )
    print('displaying bst2')
    bst2.displayInOrder()

def unit_test_03():
    rbst = gen_rand_bst(5, 0, 10)
    print('root=' + str(rbst.getRoot()))
    rbst.displayInOrder()
    print('is list? = ' + str(rbst.isList()))
    print('height = ' + str(rbst.heightOf()))
    print('is bal? = ' + str(rbst.isBalanced()))

def unit_test_04():
    print(estimate_list_prob_in_rand_bsts_with_num_nodes(100, 5, 0, 1000))

def unit_test_05():
    d = estimate_list_probs_in_rand_bsts(5, 20, 1000, 0, 1000000)
    for k, v in d.iteritems():
        print('probability of linearity in rbsts with %d nodes = %f' % (k, v[0]))

def unit_test_06(from_num_nodes, upto_num_nodes):
    d = estimate_list_probs_in_rand_bsts(from_num_nodes, upto_num_nodes, 1000, 0, 1000000)
    for k, v in d.iteritems():
        print('probability of linearity in rbsts with %d nodes = %f' % (k, v[0]))

def unit_test_07(num_nodes_start, num_nodes_end):
    d = estimate_balance_probs_in_rand_bsts(num_nodes_start, num_nodes_end, 1000, 0, 1000000)
    for k, v in d.iteritems():
        print('probability of balance in rbsts with %d nodes = %f' % (k, v[0]))



    




