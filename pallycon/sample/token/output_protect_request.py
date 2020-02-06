class OutputProtectRequest:

    def __init__(self, allow_external_display=None, control_hdcp=None):
        
        if isinstance(allow_external_display, bool):
            self.__allow_external_display = allow_external_display
        if isinstance(control_hdcp, int):
            self.__control_hdcp = control_hdcp
        
        if allow_external_display is None:
            self.__allow_external_display = False
        if control_hdcp is None:
            self.__control_hdcp = 150

    @property
    def allow_external_display(self):
        return self.__allow_external_display

    @property
    def control_hdcp(self):
        return self.__control_hdcp

    @allow_external_display.setter
    def allow_external_display(self, allow_external_display):
        self.__allow_external_display = allow_external_display

    @control_hdcp.setter
    def control_hdcp(self, control_hdcp):
        self.__control_hdcp = control_hdcp

    def output_protect_dict(self):
        output_protect = {
            'allow_external_display' : self.__allow_external_display,
            'control_hdcp' : self.__control_hdcp
        }
        return output_protect