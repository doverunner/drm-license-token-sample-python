# for @security_policy @wiseplay @security_level
SECURITY_LEVEL = (1, 2, 3)

SW_LEVEL_1 = SECURITY_LEVEL[0]  # 'SW_LEVEL_1',
HW_LEVEL_2 = SECURITY_LEVEL[1]  # 'HW_LEVEL_2'
ENHANCED_HW_LEVEL_3 = SECURITY_LEVEL[2]  # 'ENHANCED_HW_LEVEL_3'

def check(security_level) -> bool:
    return security_level in SECURITY_LEVEL
