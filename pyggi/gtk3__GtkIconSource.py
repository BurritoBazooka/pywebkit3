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
from gtk3_enums import *
from gtk3_types import *
from gtk3_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GtkLabel = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkRegionFlags = POINTER(c_int)
_GAsyncResult = POINTER(c_int)
_cairo_matrix_t = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GClosure = POINTER(c_int)
_GIcon = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_GFileEnumerator = POINTER(c_int)
_GtkDialog = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GtkSymbolicColor = POINTER(c_int)
_void = POINTER(c_int)
_GtkStyleProperties = POINTER(c_int)
_GtkIconInfo = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkNumerableIcon = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GObject = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GtkSymbolicColor = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GAppLaunchContext = POINTER(c_int)
_PangoAttrIterator = POINTER(c_int)
_GFileAttributeMatcher = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkIconTheme = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAccelLabel = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_GFileAttributeMatcher = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_GdkPoint = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GSource = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GSource = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_GFileInfo = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_GEmblemedIcon = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
_GScanner = POINTER(c_int)
_GFileAttributeInfoList = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkEventKey = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GFileIOStream = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GCond = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_cairo_surface_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_GActionGroup = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_WebKitNetworkRequest = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_GFile = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
_GFileInputStream = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_GError = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GWeakRef = POINTER(c_int)
_GdkPixbufAnimationIter = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkEventButton = POINTER(c_int)
_GCancellable = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_GMount = POINTER(c_int)
_PangoRectangle = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GFile = POINTER(c_int)
_GDrive = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_GMutex = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkPrintOperation = POINTER(c_int)
_GtkThemingEngine = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GFileInfo = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_GTimeVal = POINTER(c_int)
_GSourceFuncs = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_GFileIOStream = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_GtkStylePropertyParser = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkPixbufAnimation = POINTER(c_int)
_GEmblem = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GVolume = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GPollFD = POINTER(c_int)
_GFileOutputStream = POINTER(c_int)
_WebKitDOMNode = POINTER(c_int)
_GtkStyleProperties = POINTER(c_int)
_WebKitWebNavigationAction = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GParameter = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GIcon = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkGradient = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GMountOperation = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GSourceCallbackFuncs = POINTER(c_int)
_GtkTargetEntry = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GByteArray = POINTER(c_int)
_GdkPixbufSimpleAnim = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
"""Enumerations"""
GdkWindowType = c_int
GdkWindowWindowClass = c_int
GdkWindowHints = c_int
GdkGravity = c_int
GdkWindowEdgeh = c_int
GdkWindowTypeHint = c_int
GdkWindowAttributesType = c_int
GdkFilterReturn = c_int
GdkModifierType = c_int
GdkWMDecoration = c_int
GdkWMFunction = c_int
GdkCursorType = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GdkVisualType = c_int
GdkByteOrder = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GtkIconSize = c_int
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
cairo_extend_t = c_int
cairo_filter_t = c_int
CairoPatternype_t = c_int
WebKitLoadStatus = c_int
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitEditingBehavior = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GApplicationFlags = c_int
GtkDialogFlags = c_int
GtkResponseType = c_int
WebKitWebNavigationReason = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
GMountMountFlags = c_int
GMountUnmountFlags = c_int
GDriveStartFlags = c_int
GDriveStartStopType = c_int

try:
    libgtk3.gtk_icon_source_get_pixbuf.restype = _GdkPixbuf
    libgtk3.gtk_icon_source_get_pixbuf.argtypes = [_GtkIconSource]
except:
   pass
try:
    libgtk3.gtk_icon_source_get_size_wildcarded.restype = gboolean
    libgtk3.gtk_icon_source_get_size_wildcarded.argtypes = [_GtkIconSource]
except:
   pass
try:
    libgtk3.gtk_icon_source_set_direction.restype = None
    libgtk3.gtk_icon_source_set_direction.argtypes = [_GtkIconSource,GtkTextDirection]
except:
   pass
try:
    libgtk3.gtk_icon_source_free.restype = None
    libgtk3.gtk_icon_source_free.argtypes = [_GtkIconSource]
except:
   pass
try:
    libgtk3.gtk_icon_source_get_direction.restype = GtkTextDirection
    libgtk3.gtk_icon_source_get_direction.argtypes = [_GtkIconSource]
except:
   pass
try:
    libgtk3.gtk_icon_source_set_state_wildcarded.restype = None
    libgtk3.gtk_icon_source_set_state_wildcarded.argtypes = [_GtkIconSource,gboolean]
except:
   pass
try:
    libgtk3.gtk_icon_source_get_state_wildcarded.restype = gboolean
    libgtk3.gtk_icon_source_get_state_wildcarded.argtypes = [_GtkIconSource]
except:
   pass
try:
    libgtk3.gtk_icon_source_set_direction_wildcarded.restype = None
    libgtk3.gtk_icon_source_set_direction_wildcarded.argtypes = [_GtkIconSource,gboolean]
except:
   pass
try:
    libgtk3.gtk_icon_source_copy.restype = _GtkIconSource
    libgtk3.gtk_icon_source_copy.argtypes = [_GtkIconSource]
except:
   pass
try:
    libgtk3.gtk_icon_source_set_state.restype = None
    libgtk3.gtk_icon_source_set_state.argtypes = [_GtkIconSource,GtkStateType]
except:
   pass
try:
    libgtk3.gtk_icon_source_get_size.restype = GtkIconSize
    libgtk3.gtk_icon_source_get_size.argtypes = [_GtkIconSource]
except:
   pass
try:
    libgtk3.gtk_icon_source_set_pixbuf.restype = None
    libgtk3.gtk_icon_source_set_pixbuf.argtypes = [_GtkIconSource,_GdkPixbuf]
except:
   pass
try:
    libgtk3.gtk_icon_source_get_icon_name.restype = c_char_p
    libgtk3.gtk_icon_source_get_icon_name.argtypes = [_GtkIconSource]
except:
   pass
try:
    libgtk3.gtk_icon_source_set_icon_name.restype = None
    libgtk3.gtk_icon_source_set_icon_name.argtypes = [_GtkIconSource,c_char_p]
except:
   pass
try:
    libgtk3.gtk_icon_source_get_direction_wildcarded.restype = gboolean
    libgtk3.gtk_icon_source_get_direction_wildcarded.argtypes = [_GtkIconSource]
except:
   pass
try:
    libgtk3.gtk_icon_source_set_size_wildcarded.restype = None
    libgtk3.gtk_icon_source_set_size_wildcarded.argtypes = [_GtkIconSource,gboolean]
except:
   pass
try:
    libgtk3.gtk_icon_source_set_size.restype = None
    libgtk3.gtk_icon_source_set_size.argtypes = [_GtkIconSource,GtkIconSize]
except:
   pass
try:
    libgtk3.gtk_icon_source_get_state.restype = GtkStateType
    libgtk3.gtk_icon_source_get_state.argtypes = [_GtkIconSource]
except:
   pass
import gobject__GObject
class GtkIconSource( gobject__GObject.GObject):
    """Class GtkIconSource Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_icon_source_new.restype = POINTER(c_int)
            
            libgtk3.gtk_icon_source_new.argtypes = []
            self._object = libgtk3.gtk_icon_source_new()

    """Methods"""
    def get_pixbuf(  self, ):

        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_source_get_pixbuf( self._object ) or POINTER(c_int)())

    def get_size_wildcarded(  self, ):

        
        return libgtk3.gtk_icon_source_get_size_wildcarded( self._object )

    def set_direction(  self, direction, ):

        
        libgtk3.gtk_icon_source_set_direction( self._object,direction )

    def free(  self, ):

        
        libgtk3.gtk_icon_source_free( self._object )

    def get_direction(  self, ):

        
        return libgtk3.gtk_icon_source_get_direction( self._object )

    def set_state_wildcarded(  self, setting, ):

        
        libgtk3.gtk_icon_source_set_state_wildcarded( self._object,setting )

    def get_state_wildcarded(  self, ):

        
        return libgtk3.gtk_icon_source_get_state_wildcarded( self._object )

    def set_direction_wildcarded(  self, setting, ):

        
        libgtk3.gtk_icon_source_set_direction_wildcarded( self._object,setting )

    def copy(  self, ):

        from gtk3 import GtkIconSource
        return GtkIconSource( obj=libgtk3.gtk_icon_source_copy( self._object ) or POINTER(c_int)())

    def set_state(  self, state, ):

        
        libgtk3.gtk_icon_source_set_state( self._object,state )

    def get_size(  self, ):

        
        return libgtk3.gtk_icon_source_get_size( self._object )

    def set_pixbuf(  self, pixbuf, ):
        if pixbuf: pixbuf = pixbuf._object
        else: pixbuf = POINTER(c_int)()

        
        libgtk3.gtk_icon_source_set_pixbuf( self._object,pixbuf )

    def get_icon_name(  self, ):

        
        return libgtk3.gtk_icon_source_get_icon_name( self._object )

    def set_icon_name(  self, icon_name, ):

        
        libgtk3.gtk_icon_source_set_icon_name( self._object,icon_name )

    def get_direction_wildcarded(  self, ):

        
        return libgtk3.gtk_icon_source_get_direction_wildcarded( self._object )

    def set_size_wildcarded(  self, setting, ):

        
        libgtk3.gtk_icon_source_set_size_wildcarded( self._object,setting )

    def set_size(  self, size, ):

        
        libgtk3.gtk_icon_source_set_size( self._object,size )

    def get_state(  self, ):

        
        return libgtk3.gtk_icon_source_get_state( self._object )

