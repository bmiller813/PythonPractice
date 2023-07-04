from abc import ABC, abstractmethod
# Walks like a duck and quacks like a duck. its a duck
# Line 16 only looks for the draw method

class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


