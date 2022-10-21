# -*- coding: utf-8-*-
"""
Module : QPanda3D_Translation_Modifiers
Author : Niklas Mevenkamp
Description :
    Contains a dictionary that translates QT keyboard events to panda3d
    keyboard events.
"""

# PyQt imports
from PySide6.QtCore import Qt


__all__ = ["QPanda3D_Modifier_Translation"]

QPanda3D_Modifier_Translation = {
    Qt.NoModifier: None,
    Qt.ShiftModifier: 'shift',
    Qt.ControlModifier: 'control',
    Qt.AltModifier: 'alt',
    Qt.MetaModifier: 'unknown',
    Qt.KeypadModifier: 'unknown',
    Qt.GroupSwitchModifier: 'unknown',
}
