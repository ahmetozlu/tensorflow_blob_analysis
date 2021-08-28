#!/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------
# author      : Ahmet Ozlu
# mail        : ahmetozlu93@gmail.com
# date        : 17.05.2021
# -----------------------------------------

import cv2
import backbone

image = cv2.imread('input.png')

backbone.predict(image)
