# for @security_policy @wiseplay @security_level
SECURITY_LEVEL = (1, 2, 3)

SW_LEVEL_1 = SECURITY_LEVEL[0]  # 'LEVEL_150',
HW_LEVEL_2 = SECURITY_LEVEL[1]  # 'LEVEL_2000'
ENHANCED_HW_LEVEL_3 = SECURITY_LEVEL[2]  # 'LEVEL_3000'

def check(security_level) -> bool:
    return security_level in SECURITY_LEVEL
