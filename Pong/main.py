#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:23:24 2020

@author: brian
"""
from kivy.app import App
from kivy.uix.image import Image


class MainApp(App):
    def build(self):
        img = Image(source='/home/brian/Documents/es_prod/ncr_logo.jpg',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})

        return img
    
if __name__ == '__main__':
    app = MainApp()
    app.run()