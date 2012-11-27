# Copyright, John Rusnak, 2012
    # This code binding is available under the license agreement of the LGPL with
    # an additional constraint described below,
    # and with the understanding that the webkit API is copyright protected
    # by Apple Computer, Inc. (see below).
    # There is an  additional constraint that any derivatives of this work aimed
    # at providing bindings to GObject, GTK, GDK, or WebKit be strictly
    # python-only bindings with no native code.
    # * THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY
    # * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    # * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    # * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
    # * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    # * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    # * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    # * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
    # * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    #
    # ******************************************************
    # For the API:
    # /*
    # * Copyright (C) 2006 Apple Computer, Inc.  All rights reserved.
    # *
    # * Redistribution and use in source and binary forms, with or without
    # * modification, are permitted provided that the following conditions
    # * are met:
    # * 1. Redistributions of source code must retain the above copyright
    # *    notice, this list of conditions and the following disclaimer.
    # * 2. Redistributions in binary form must reproduce the above copyright
    # *    notice, this list of conditions and the following disclaimer in the
    # *    documentation and/or other materials provided with the distribution.
    # *
    # * THIS SOFTWARE IS PROVIDED BY APPLE COMPUTER, INC. ``AS IS'' AND ANY
    # * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    # * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    # * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
    # * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    # * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    # * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    # * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
    # * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    # */
from ctypes import *
from gtk3_types import *
from gtk3_types import *
    
    
"""Derived Pointer Types"""
_PangoContext = c_void_p
_PangoFontMap = c_void_p
__PangoAttrList = c_void_p
__GList = c_void_p
__PangoAttrIterator = c_void_p
_GSList = c_void_p
__PangoRectangle = c_void_p
_char = c_void_p
__PangoGlyphString = c_void_p
_PangoLogAttr = c_void_p
_PangoLayoutIter = c_void_p
__PangoFontFamily = c_void_p
__PangoContext = c_void_p
_PangoFontset = c_void_p
__PangoFontDescription = c_void_p
__PangoFontMap = c_void_p
__PangoLanguage = c_void_p
_PangoAttrList = c_void_p
__gunichar = c_void_p
__PangoLogAttr = c_void_p
_PangoLayout = c_void_p
_PangoMatrix = c_void_p
__PangoAnalysis = c_void_p
_PangoFontDescription = c_void_p
_GList = c_void_p
_PangoLayoutRun = c_void_p
_PangoFont = c_void_p
_PangoLayoutLine = c_void_p
__PangoTabArray = c_void_p
__PangoLayout = c_void_p
__PangoMatrix = c_void_p
_PangoLanguage = c_void_p
_PangoTabArray = c_void_p
_PangoFontMetrics = c_void_p
"""Enumerations"""
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int

import _gobject_GBoxed
class PangoFontMetrics( _gobject_GBoxed.GBoxed):
    """Class PangoFontMetrics Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_approximate_digit_width(self, ):

        libgtk3.pango_font_metrics_get_approximate_digit_width.restype = int
        libgtk3.pango_font_metrics_get_approximate_digit_width.argtypes = [c_void_p]
        
        return libgtk3.pango_font_metrics_get_approximate_digit_width(self._object, )

    def get_strikethrough_position(self, ):

        libgtk3.pango_font_metrics_get_strikethrough_position.restype = int
        libgtk3.pango_font_metrics_get_strikethrough_position.argtypes = [c_void_p]
        
        return libgtk3.pango_font_metrics_get_strikethrough_position(self._object, )

    def get_strikethrough_thickness(self, ):

        libgtk3.pango_font_metrics_get_strikethrough_thickness.restype = int
        libgtk3.pango_font_metrics_get_strikethrough_thickness.argtypes = [c_void_p]
        
        return libgtk3.pango_font_metrics_get_strikethrough_thickness(self._object, )

    def get_underline_position(self, ):

        libgtk3.pango_font_metrics_get_underline_position.restype = int
        libgtk3.pango_font_metrics_get_underline_position.argtypes = [c_void_p]
        
        return libgtk3.pango_font_metrics_get_underline_position(self._object, )

    def ref(self, ):

        libgtk3.pango_font_metrics_ref.restype = _PangoFontMetrics
        libgtk3.pango_font_metrics_ref.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoFontMetrics
        return PangoFontMetrics(None, obj=libgtk3.pango_font_metrics_ref(self._object, )  or c_void_p())

    def get_approximate_char_width(self, ):

        libgtk3.pango_font_metrics_get_approximate_char_width.restype = int
        libgtk3.pango_font_metrics_get_approximate_char_width.argtypes = [c_void_p]
        
        return libgtk3.pango_font_metrics_get_approximate_char_width(self._object, )

    def unref(self, ):

        libgtk3.pango_font_metrics_unref.argtypes = [c_void_p]
        
        libgtk3.pango_font_metrics_unref(self._object, )

    def get_ascent(self, ):

        libgtk3.pango_font_metrics_get_ascent.restype = int
        libgtk3.pango_font_metrics_get_ascent.argtypes = [c_void_p]
        
        return libgtk3.pango_font_metrics_get_ascent(self._object, )

    def get_descent(self, ):

        libgtk3.pango_font_metrics_get_descent.restype = int
        libgtk3.pango_font_metrics_get_descent.argtypes = [c_void_p]
        
        return libgtk3.pango_font_metrics_get_descent(self._object, )

    def get_underline_thickness(self, ):

        libgtk3.pango_font_metrics_get_underline_thickness.restype = int
        libgtk3.pango_font_metrics_get_underline_thickness.argtypes = [c_void_p]
        
        return libgtk3.pango_font_metrics_get_underline_thickness(self._object, )
