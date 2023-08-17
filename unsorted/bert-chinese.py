#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : bert-chinese.py
# @Time    : 8/10/23 14:30
# @Author  : zlhhh
# @Description :

import tensorflow as tf

model_path = "/path/to/bert-base-chinese-tf_model.h5"
model = tf.keras.models.load_model(model_path)