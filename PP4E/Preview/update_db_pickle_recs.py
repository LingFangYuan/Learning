#!/usr/bin/env python3
# -*- conding: utf-8 -*-

import pickle

suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *= 1.10

suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()