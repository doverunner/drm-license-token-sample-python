OUTPUT_CONTROL = (0,1,2,3)

HDCP_NONE = OUTPUT_CONTROL[0]  # 'HDCP_NONE : not restricted'
HDCP_V1_4 = OUTPUT_CONTROL[1]  # 'HDCP_V1.4 or later'
HDCP_V2_2 = OUTPUT_CONTROL[2]  # 'HDCP_V2.2 or later'
HDCP_RESTRICTED = OUTPUT_CONTROL[3]  # 'HDCP_RESTRICTED'

def check(output_control):
    return output_control in OUTPUT_CONTROL