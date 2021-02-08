'''
///////////////////////////////////YUNYOO.CN////////////////////////////////////
//                                                                             *
// A64Dbg PLUGIN MACHINE REGISTERS PYTHON INTERFACE FILE                       *
//                                                                             *
// Copyright(C) 2021 YunYoo Corp., ALL RIGHTS RESERVED.                        *
//                                                                             *
// Internet: yunyoo.cn                                                         *
//                                                                             *
// This code is distributed "as is", part of A64Dbg and without warranty of    *
// any kind, expressed or implied, including, but not limited to warranty of   *
// fitness for any particular purpose. In no event will A64Dbg be liable to    *
// you for any special, incidental, indirect, consequential or any other       *
// damages caused by the use, misuse, or the inability to use of this code,    *
// including anylost profits or lost savings, even if A64Dbg has been advised  *
// of the possibility of such damages.                                         *
//                                                                             *
///////////////////////////////////////*////////////////////////////////////////
'''

import _adp

# entry for register get/set
def register_proc(name, value = None):
    if value is None:
        return _adp.adp_entry({'action':'getreg', 'name':name})
    _adp.adp_entry({'action':'setreg', 'name':name, 'value':value})
    return 0

# base register get/set
class register_base:
    def __get_csp_property__(self):
        return register_proc('csp')
    def __set_csp_property__(self, value):
        return register_proc('csp', value)
    sp = property(__get_csp_property__, __set_csp_property__)

    def __get_cip_property__(self):
        return register_proc('cip')
    def __set_cip_property__(self, value):
        return register_proc('cip', value)
    pc = property(__get_cip_property__, __set_cip_property__)

# arm/arm64 base register get/set
class arm_base(register_base):
    def __get_clr_property__(self):
        return register_proc('clr')
    def __set_clr_property__(self, value):
        return register_proc('clr', value)
    lr = property(__get_clr_property__, __set_clr_property__)

    def __get_N_property__(self):
        return register_proc('N')
    def __set_N_property__(self, value):
        return register_proc('N', value)
    N = property(__get_N_property__, __set_N_property__)

    def __get_Z_property__(self):
        return register_proc('Z')
    def __set_Z_property__(self, value):
        return register_proc('Z', value)
    Z = property(__get_Z_property__, __set_Z_property__)

    def __get_C_property__(self):
        return register_proc('C')
    def __set_C_property__(self, value):
        return register_proc('C', value)
    C = property(__get_C_property__, __set_C_property__)

    def __get_V_property__(self):
        return register_proc('V')
    def __set_V_property__(self, value):
        return register_proc('V', value)
    V = property(__get_V_property__, __set_V_property__)

    def __get_q0_property__(self):
        return register_proc('q0')
    def __set_q0_property__(self, value):
        return register_proc('q0', value)
    q0 = property(__get_q0_property__, __set_q0_property__)

    def __get_q1_property__(self):
        return register_proc('q1')
    def __set_q1_property__(self, value):
        return register_proc('q1', value)
    q1 = property(__get_q1_property__, __set_q1_property__)

    def __get_q2_property__(self):
        return register_proc('q2')
    def __set_q2_property__(self, value):
        return register_proc('q2', value)
    q2 = property(__get_q2_property__, __set_q2_property__)

    def __get_q3_property__(self):
        return register_proc('q3')
    def __set_q3_property__(self, value):
        return register_proc('q3', value)
    q3 = property(__get_q3_property__, __set_q3_property__)

    def __get_q4_property__(self):
        return register_proc('q4')
    def __set_q4_property__(self, value):
        return register_proc('q4', value)
    q4 = property(__get_q4_property__, __set_q4_property__)

    def __get_q5_property__(self):
        return register_proc('q5')
    def __set_q5_property__(self, value):
        return register_proc('q5', value)
    q5 = property(__get_q5_property__, __set_q5_property__)

    def __get_q6_property__(self):
        return register_proc('q6')
    def __set_q6_property__(self, value):
        return register_proc('q6', value)
    q6 = property(__get_q6_property__, __set_q6_property__)

    def __get_q7_property__(self):
        return register_proc('q7')
    def __set_q7_property__(self, value):
        return register_proc('q7', value)
    q7 = property(__get_q7_property__, __set_q7_property__)

    def __get_q8_property__(self):
        return register_proc('q8')
    def __set_q8_property__(self, value):
        return register_proc('q8', value)
    q8 = property(__get_q8_property__, __set_q8_property__)

    def __get_q9_property__(self):
        return register_proc('q9')
    def __set_q9_property__(self, value):
        return register_proc('q9', value)
    q9 = property(__get_q9_property__, __set_q9_property__)

    def __get_q10_property__(self):
        return register_proc('q10')
    def __set_q10_property__(self, value):
        return register_proc('q10', value)
    q10 = property(__get_q10_property__, __set_q10_property__)

    def __get_q11_property__(self):
        return register_proc('q11')
    def __set_q11_property__(self, value):
        return register_proc('q11', value)
    q11 = property(__get_q11_property__, __set_q11_property__)

    def __get_q12_property__(self):
        return register_proc('q12')
    def __set_q12_property__(self, value):
        return register_proc('q12', value)
    q12 = property(__get_q12_property__, __set_q12_property__)

    def __get_q13_property__(self):
        return register_proc('q13')
    def __set_q13_property__(self, value):
        return register_proc('q13', value)
    q13 = property(__get_q13_property__, __set_q13_property__)

    def __get_q14_property__(self):
        return register_proc('q14')
    def __set_q14_property__(self, value):
        return register_proc('q14', value)
    q14 = property(__get_q14_property__, __set_q14_property__)

    def __get_q15_property__(self):
        return register_proc('q15')
    def __set_q15_property__(self, value):
        return register_proc('q15', value)
    q15 = property(__get_q15_property__, __set_q15_property__)

    def __get_q16_property__(self):
        return register_proc('q16')
    def __set_q16_property__(self, value):
        return register_proc('q16', value)
    q16 = property(__get_q16_property__, __set_q16_property__)

    def __get_q17_property__(self):
        return register_proc('q17')
    def __set_q17_property__(self, value):
        return register_proc('q17', value)
    q17 = property(__get_q17_property__, __set_q17_property__)

    def __get_q18_property__(self):
        return register_proc('q18')
    def __set_q18_property__(self, value):
        return register_proc('q18', value)
    q18 = property(__get_q18_property__, __set_q18_property__)

    def __get_q19_property__(self):
        return register_proc('q19')
    def __set_q19_property__(self, value):
        return register_proc('q19', value)
    q19 = property(__get_q19_property__, __set_q19_property__)

    def __get_q20_property__(self):
        return register_proc('q20')
    def __set_q20_property__(self, value):
        return register_proc('q20', value)
    q20 = property(__get_q20_property__, __set_q20_property__)

    def __get_q21_property__(self):
        return register_proc('q21')
    def __set_q21_property__(self, value):
        return register_proc('q21', value)
    q21 = property(__get_q21_property__, __set_q21_property__)

    def __get_q22_property__(self):
        return register_proc('q22')
    def __set_q22_property__(self, value):
        return register_proc('q22', value)
    q22 = property(__get_q22_property__, __set_q22_property__)

    def __get_q23_property__(self):
        return register_proc('q23')
    def __set_q23_property__(self, value):
        return register_proc('q23', value)
    q23 = property(__get_q23_property__, __set_q23_property__)

    def __get_q24_property__(self):
        return register_proc('q24')
    def __set_q24_property__(self, value):
        return register_proc('q24', value)
    q24 = property(__get_q24_property__, __set_q24_property__)

    def __get_q25_property__(self):
        return register_proc('q25')
    def __set_q25_property__(self, value):
        return register_proc('q25', value)
    q25 = property(__get_q25_property__, __set_q25_property__)

    def __get_q26_property__(self):
        return register_proc('q26')
    def __set_q26_property__(self, value):
        return register_proc('q26', value)
    q26 = property(__get_q26_property__, __set_q26_property__)

    def __get_q27_property__(self):
        return register_proc('q27')
    def __set_q27_property__(self, value):
        return register_proc('q27', value)
    q27 = property(__get_q27_property__, __set_q27_property__)

    def __get_q28_property__(self):
        return register_proc('q28')
    def __set_q28_property__(self, value):
        return register_proc('q28', value)
    q28 = property(__get_q28_property__, __set_q28_property__)

    def __get_q29_property__(self):
        return register_proc('q29')
    def __set_q29_property__(self, value):
        return register_proc('q29', value)
    q29 = property(__get_q29_property__, __set_q29_property__)

    def __get_q30_property__(self):
        return register_proc('q30')
    def __set_q30_property__(self, value):
        return register_proc('q30', value)
    q30 = property(__get_q30_property__, __set_q30_property__)

    def __get_q31_property__(self):
        return register_proc('q31')
    def __set_q31_property__(self, value):
        return register_proc('q31', value)
    q31 = property(__get_q31_property__, __set_q31_property__)

    def __get_d0_property__(self):
        return register_proc('d0')
    def __set_d0_property__(self, value):
        return register_proc('d0', value)
    d0 = property(__get_d0_property__, __set_d0_property__)

    def __get_d1_property__(self):
        return register_proc('d1')
    def __set_d1_property__(self, value):
        return register_proc('d1', value)
    d1 = property(__get_d1_property__, __set_d1_property__)

    def __get_d2_property__(self):
        return register_proc('d2')
    def __set_d2_property__(self, value):
        return register_proc('d2', value)
    d2 = property(__get_d2_property__, __set_d2_property__)

    def __get_d3_property__(self):
        return register_proc('d3')
    def __set_d3_property__(self, value):
        return register_proc('d3', value)
    d3 = property(__get_d3_property__, __set_d3_property__)

    def __get_d4_property__(self):
        return register_proc('d4')
    def __set_d4_property__(self, value):
        return register_proc('d4', value)
    d4 = property(__get_d4_property__, __set_d4_property__)

    def __get_d5_property__(self):
        return register_proc('d5')
    def __set_d5_property__(self, value):
        return register_proc('d5', value)
    d5 = property(__get_d5_property__, __set_d5_property__)

    def __get_d6_property__(self):
        return register_proc('d6')
    def __set_d6_property__(self, value):
        return register_proc('d6', value)
    d6 = property(__get_d6_property__, __set_d6_property__)

    def __get_d7_property__(self):
        return register_proc('d7')
    def __set_d7_property__(self, value):
        return register_proc('d7', value)
    d7 = property(__get_d7_property__, __set_d7_property__)

    def __get_d8_property__(self):
        return register_proc('d8')
    def __set_d8_property__(self, value):
        return register_proc('d8', value)
    d8 = property(__get_d8_property__, __set_d8_property__)

    def __get_d9_property__(self):
        return register_proc('d9')
    def __set_d9_property__(self, value):
        return register_proc('d9', value)
    d9 = property(__get_d9_property__, __set_d9_property__)

    def __get_d10_property__(self):
        return register_proc('d10')
    def __set_d10_property__(self, value):
        return register_proc('d10', value)
    d10 = property(__get_d10_property__, __set_d10_property__)

    def __get_d11_property__(self):
        return register_proc('d11')
    def __set_d11_property__(self, value):
        return register_proc('d11', value)
    d11 = property(__get_d11_property__, __set_d11_property__)

    def __get_d12_property__(self):
        return register_proc('d12')
    def __set_d12_property__(self, value):
        return register_proc('d12', value)
    d12 = property(__get_d12_property__, __set_d12_property__)

    def __get_d13_property__(self):
        return register_proc('d13')
    def __set_d13_property__(self, value):
        return register_proc('d13', value)
    d13 = property(__get_d13_property__, __set_d13_property__)

    def __get_d14_property__(self):
        return register_proc('d14')
    def __set_d14_property__(self, value):
        return register_proc('d14', value)
    d14 = property(__get_d14_property__, __set_d14_property__)

    def __get_d15_property__(self):
        return register_proc('d15')
    def __set_d15_property__(self, value):
        return register_proc('d15', value)
    d15 = property(__get_d15_property__, __set_d15_property__)

    def __get_d16_property__(self):
        return register_proc('d16')
    def __set_d16_property__(self, value):
        return register_proc('d16', value)
    d16 = property(__get_d16_property__, __set_d16_property__)

    def __get_d17_property__(self):
        return register_proc('d17')
    def __set_d17_property__(self, value):
        return register_proc('d17', value)
    d17 = property(__get_d17_property__, __set_d17_property__)

    def __get_d18_property__(self):
        return register_proc('d18')
    def __set_d18_property__(self, value):
        return register_proc('d18', value)
    d18 = property(__get_d18_property__, __set_d18_property__)

    def __get_d19_property__(self):
        return register_proc('d19')
    def __set_d19_property__(self, value):
        return register_proc('d19', value)
    d19 = property(__get_d19_property__, __set_d19_property__)

    def __get_d20_property__(self):
        return register_proc('d20')
    def __set_d20_property__(self, value):
        return register_proc('d20', value)
    d20 = property(__get_d20_property__, __set_d20_property__)

    def __get_d21_property__(self):
        return register_proc('d21')
    def __set_d21_property__(self, value):
        return register_proc('d21', value)
    d21 = property(__get_d21_property__, __set_d21_property__)

    def __get_d22_property__(self):
        return register_proc('d22')
    def __set_d22_property__(self, value):
        return register_proc('d22', value)
    d22 = property(__get_d22_property__, __set_d22_property__)

    def __get_d23_property__(self):
        return register_proc('d23')
    def __set_d23_property__(self, value):
        return register_proc('d23', value)
    d23 = property(__get_d23_property__, __set_d23_property__)

    def __get_d24_property__(self):
        return register_proc('d24')
    def __set_d24_property__(self, value):
        return register_proc('d24', value)
    d24 = property(__get_d24_property__, __set_d24_property__)

    def __get_d25_property__(self):
        return register_proc('d25')
    def __set_d25_property__(self, value):
        return register_proc('d25', value)
    d25 = property(__get_d25_property__, __set_d25_property__)

    def __get_d26_property__(self):
        return register_proc('d26')
    def __set_d26_property__(self, value):
        return register_proc('d26', value)
    d26 = property(__get_d26_property__, __set_d26_property__)

    def __get_d27_property__(self):
        return register_proc('d27')
    def __set_d27_property__(self, value):
        return register_proc('d27', value)
    d27 = property(__get_d27_property__, __set_d27_property__)

    def __get_d28_property__(self):
        return register_proc('d28')
    def __set_d28_property__(self, value):
        return register_proc('d28', value)
    d28 = property(__get_d28_property__, __set_d28_property__)

    def __get_d29_property__(self):
        return register_proc('d29')
    def __set_d29_property__(self, value):
        return register_proc('d29', value)
    d29 = property(__get_d29_property__, __set_d29_property__)

    def __get_d30_property__(self):
        return register_proc('d30')
    def __set_d30_property__(self, value):
        return register_proc('d30', value)
    d30 = property(__get_d30_property__, __set_d30_property__)

    def __get_d31_property__(self):
        return register_proc('d31')
    def __set_d31_property__(self, value):
        return register_proc('d31', value)
    d31 = property(__get_d31_property__, __set_d31_property__)

# arm register get/set
class arm(arm_base):
    def __get_T_property__(self):
        return register_proc('T')
    def __set_T_property__(self, value):
        return register_proc('T', value)
    T = property(__get_T_property__, __set_T_property__)

    def __get_r0_property__(self):
        return register_proc('r0')
    def __set_r0_property__(self, value):
        return register_proc('r0', value)
    r0 = property(__get_r0_property__, __set_r0_property__)

    def __get_r1_property__(self):
        return register_proc('r1')
    def __set_r1_property__(self, value):
        return register_proc('r1', value)
    r1 = property(__get_r1_property__, __set_r1_property__)

    def __get_r2_property__(self):
        return register_proc('r2')
    def __set_r2_property__(self, value):
        return register_proc('r2', value)
    r2 = property(__get_r2_property__, __set_r2_property__)

    def __get_r3_property__(self):
        return register_proc('r3')
    def __set_r3_property__(self, value):
        return register_proc('r3', value)
    r3 = property(__get_r3_property__, __set_r3_property__)

    def __get_r4_property__(self):
        return register_proc('r4')
    def __set_r4_property__(self, value):
        return register_proc('r4', value)
    r4 = property(__get_r4_property__, __set_r4_property__)

    def __get_r5_property__(self):
        return register_proc('r5')
    def __set_r5_property__(self, value):
        return register_proc('r5', value)
    r5 = property(__get_r5_property__, __set_r5_property__)

    def __get_r6_property__(self):
        return register_proc('r6')
    def __set_r6_property__(self, value):
        return register_proc('r6', value)
    r6 = property(__get_r6_property__, __set_r6_property__)

    def __get_r7_property__(self):
        return register_proc('r7')
    def __set_r7_property__(self, value):
        return register_proc('r7', value)
    r7 = property(__get_r7_property__, __set_r7_property__)

    def __get_r8_property__(self):
        return register_proc('r8')
    def __set_r8_property__(self, value):
        return register_proc('r8', value)
    r8 = property(__get_r8_property__, __set_r8_property__)

    def __get_r9_property__(self):
        return register_proc('r9')
    def __set_r9_property__(self, value):
        return register_proc('r9', value)
    r9 = property(__get_r9_property__, __set_r9_property__)

    def __get_r10_property__(self):
        return register_proc('r10')
    def __set_r10_property__(self, value):
        return register_proc('r10', value)
    r10 = property(__get_r10_property__, __set_r10_property__)

    def __get_r11_property__(self):
        return register_proc('r11')
    def __set_r11_property__(self, value):
        return register_proc('r11', value)
    r11 = property(__get_r11_property__, __set_r11_property__)

    def __get_r12_property__(self):
        return register_proc('r12')
    def __set_r12_property__(self, value):
        return register_proc('r12', value)
    r12 = property(__get_r12_property__, __set_r12_property__)

# arm64 register get/set
class arm64(arm_base):
    def __get_x0_property__(self):
        return register_proc('x0')
    def __set_x0_property__(self, value):
        return register_proc('x0', value)
    x0 = property(__get_x0_property__, __set_x0_property__)

    def __get_x1_property__(self):
        return register_proc('x1')
    def __set_x1_property__(self, value):
        return register_proc('x1', value)
    x1 = property(__get_x1_property__, __set_x1_property__)

    def __get_x2_property__(self):
        return register_proc('x2')
    def __set_x2_property__(self, value):
        return register_proc('x2', value)
    x2 = property(__get_x2_property__, __set_x2_property__)

    def __get_x3_property__(self):
        return register_proc('x3')
    def __set_x3_property__(self, value):
        return register_proc('x3', value)
    x3 = property(__get_x3_property__, __set_x3_property__)

    def __get_x4_property__(self):
        return register_proc('x4')
    def __set_x4_property__(self, value):
        return register_proc('x4', value)
    x4 = property(__get_x4_property__, __set_x4_property__)

    def __get_x5_property__(self):
        return register_proc('x5')
    def __set_x5_property__(self, value):
        return register_proc('x5', value)
    x5 = property(__get_x5_property__, __set_x5_property__)

    def __get_x6_property__(self):
        return register_proc('x6')
    def __set_x6_property__(self, value):
        return register_proc('x6', value)
    x6 = property(__get_x6_property__, __set_x6_property__)

    def __get_x7_property__(self):
        return register_proc('x7')
    def __set_x7_property__(self, value):
        return register_proc('x7', value)
    x7 = property(__get_x7_property__, __set_x7_property__)

    def __get_x8_property__(self):
        return register_proc('x8')
    def __set_x8_property__(self, value):
        return register_proc('x8', value)
    x8 = property(__get_x8_property__, __set_x8_property__)

    def __get_x9_property__(self):
        return register_proc('x9')
    def __set_x9_property__(self, value):
        return register_proc('x9', value)
    x9 = property(__get_x9_property__, __set_x9_property__)

    def __get_x10_property__(self):
        return register_proc('x10')
    def __set_x10_property__(self, value):
        return register_proc('x10', value)
    x10 = property(__get_x10_property__, __set_x10_property__)

    def __get_x11_property__(self):
        return register_proc('x11')
    def __set_x11_property__(self, value):
        return register_proc('x11', value)
    x11 = property(__get_x11_property__, __set_x11_property__)

    def __get_x12_property__(self):
        return register_proc('x12')
    def __set_x12_property__(self, value):
        return register_proc('x12', value)
    x12 = property(__get_x12_property__, __set_x12_property__)

    def __get_x13_property__(self):
        return register_proc('x13')
    def __set_x13_property__(self, value):
        return register_proc('x13', value)
    x13 = property(__get_x13_property__, __set_x13_property__)

    def __get_x14_property__(self):
        return register_proc('x14')
    def __set_x14_property__(self, value):
        return register_proc('x14', value)
    x14 = property(__get_x14_property__, __set_x14_property__)

    def __get_x15_property__(self):
        return register_proc('x15')
    def __set_x15_property__(self, value):
        return register_proc('x15', value)
    x15 = property(__get_x15_property__, __set_x15_property__)

    def __get_x16_property__(self):
        return register_proc('x16')
    def __set_x16_property__(self, value):
        return register_proc('x16', value)
    x16 = property(__get_x16_property__, __set_x16_property__)

    def __get_x17_property__(self):
        return register_proc('x17')
    def __set_x17_property__(self, value):
        return register_proc('x17', value)
    x17 = property(__get_x17_property__, __set_x17_property__)

    def __get_x18_property__(self):
        return register_proc('x18')
    def __set_x18_property__(self, value):
        return register_proc('x18', value)
    x18 = property(__get_x18_property__, __set_x18_property__)

    def __get_x19_property__(self):
        return register_proc('x19')
    def __set_x19_property__(self, value):
        return register_proc('x19', value)
    x19 = property(__get_x19_property__, __set_x19_property__)

    def __get_x20_property__(self):
        return register_proc('x20')
    def __set_x20_property__(self, value):
        return register_proc('x20', value)
    x20 = property(__get_x20_property__, __set_x20_property__)

    def __get_x21_property__(self):
        return register_proc('x21')
    def __set_x21_property__(self, value):
        return register_proc('x21', value)
    x21 = property(__get_x21_property__, __set_x21_property__)

    def __get_x22_property__(self):
        return register_proc('x22')
    def __set_x22_property__(self, value):
        return register_proc('x22', value)
    x22 = property(__get_x22_property__, __set_x22_property__)

    def __get_x23_property__(self):
        return register_proc('x23')
    def __set_x23_property__(self, value):
        return register_proc('x23', value)
    x23 = property(__get_x23_property__, __set_x23_property__)

    def __get_x24_property__(self):
        return register_proc('x24')
    def __set_x24_property__(self, value):
        return register_proc('x24', value)
    x24 = property(__get_x24_property__, __set_x24_property__)

    def __get_x25_property__(self):
        return register_proc('x25')
    def __set_x25_property__(self, value):
        return register_proc('x25', value)
    x25 = property(__get_x25_property__, __set_x25_property__)

    def __get_x26_property__(self):
        return register_proc('x26')
    def __set_x26_property__(self, value):
        return register_proc('x26', value)
    x26 = property(__get_x26_property__, __set_x26_property__)

    def __get_x27_property__(self):
        return register_proc('x27')
    def __set_x27_property__(self, value):
        return register_proc('x27', value)
    x27 = property(__get_x27_property__, __set_x27_property__)

    def __get_x28_property__(self):
        return register_proc('x28')
    def __set_x28_property__(self, value):
        return register_proc('x28', value)
    x28 = property(__get_x28_property__, __set_x28_property__)

    def __get_x29_property__(self):
        return register_proc('x29')
    def __set_x29_property__(self, value):
        return register_proc('x29', value)
    x29 = property(__get_x29_property__, __set_x29_property__)

    def __get_w0_property__(self):
        return register_proc('w0')
    def __set_w0_property__(self, value):
        return register_proc('w0', value)
    w0 = property(__get_w0_property__, __set_w0_property__)

    def __get_w1_property__(self):
        return register_proc('w1')
    def __set_w1_property__(self, value):
        return register_proc('w1', value)
    w1 = property(__get_w1_property__, __set_w1_property__)

    def __get_w2_property__(self):
        return register_proc('w2')
    def __set_w2_property__(self, value):
        return register_proc('w2', value)
    w2 = property(__get_w2_property__, __set_w2_property__)

    def __get_w3_property__(self):
        return register_proc('w3')
    def __set_w3_property__(self, value):
        return register_proc('w3', value)
    w3 = property(__get_w3_property__, __set_w3_property__)

    def __get_w4_property__(self):
        return register_proc('w4')
    def __set_w4_property__(self, value):
        return register_proc('w4', value)
    w4 = property(__get_w4_property__, __set_w4_property__)

    def __get_w5_property__(self):
        return register_proc('w5')
    def __set_w5_property__(self, value):
        return register_proc('w5', value)
    w5 = property(__get_w5_property__, __set_w5_property__)

    def __get_w6_property__(self):
        return register_proc('w6')
    def __set_w6_property__(self, value):
        return register_proc('w6', value)
    w6 = property(__get_w6_property__, __set_w6_property__)

    def __get_w7_property__(self):
        return register_proc('w7')
    def __set_w7_property__(self, value):
        return register_proc('w7', value)
    w7 = property(__get_w7_property__, __set_w7_property__)

    def __get_w8_property__(self):
        return register_proc('w8')
    def __set_w8_property__(self, value):
        return register_proc('w8', value)
    w8 = property(__get_w8_property__, __set_w8_property__)

    def __get_w9_property__(self):
        return register_proc('w9')
    def __set_w9_property__(self, value):
        return register_proc('w9', value)
    w9 = property(__get_w9_property__, __set_w9_property__)

    def __get_w10_property__(self):
        return register_proc('w10')
    def __set_w10_property__(self, value):
        return register_proc('w10', value)
    w10 = property(__get_w10_property__, __set_w10_property__)

    def __get_w11_property__(self):
        return register_proc('w11')
    def __set_w11_property__(self, value):
        return register_proc('w11', value)
    w11 = property(__get_w11_property__, __set_w11_property__)

    def __get_w12_property__(self):
        return register_proc('w12')
    def __set_w12_property__(self, value):
        return register_proc('w12', value)
    w12 = property(__get_w12_property__, __set_w12_property__)

    def __get_w13_property__(self):
        return register_proc('w13')
    def __set_w13_property__(self, value):
        return register_proc('w13', value)
    w13 = property(__get_w13_property__, __set_w13_property__)

    def __get_w14_property__(self):
        return register_proc('w14')
    def __set_w14_property__(self, value):
        return register_proc('w14', value)
    w14 = property(__get_w14_property__, __set_w14_property__)

    def __get_w15_property__(self):
        return register_proc('w15')
    def __set_w15_property__(self, value):
        return register_proc('w15', value)
    w15 = property(__get_w15_property__, __set_w15_property__)

    def __get_w16_property__(self):
        return register_proc('w16')
    def __set_w16_property__(self, value):
        return register_proc('w16', value)
    w16 = property(__get_w16_property__, __set_w16_property__)

    def __get_w17_property__(self):
        return register_proc('w17')
    def __set_w17_property__(self, value):
        return register_proc('w17', value)
    w17 = property(__get_w17_property__, __set_w17_property__)

    def __get_w18_property__(self):
        return register_proc('w18')
    def __set_w18_property__(self, value):
        return register_proc('w18', value)
    w18 = property(__get_w18_property__, __set_w18_property__)

    def __get_w19_property__(self):
        return register_proc('w19')
    def __set_w19_property__(self, value):
        return register_proc('w19', value)
    w19 = property(__get_w19_property__, __set_w19_property__)

    def __get_w20_property__(self):
        return register_proc('w20')
    def __set_w20_property__(self, value):
        return register_proc('w20', value)
    w20 = property(__get_w20_property__, __set_w20_property__)

    def __get_w21_property__(self):
        return register_proc('w21')
    def __set_w21_property__(self, value):
        return register_proc('w21', value)
    w21 = property(__get_w21_property__, __set_w21_property__)

    def __get_w22_property__(self):
        return register_proc('w22')
    def __set_w22_property__(self, value):
        return register_proc('w22', value)
    w22 = property(__get_w22_property__, __set_w22_property__)

    def __get_w23_property__(self):
        return register_proc('w23')
    def __set_w23_property__(self, value):
        return register_proc('w23', value)
    w23 = property(__get_w23_property__, __set_w23_property__)

    def __get_w24_property__(self):
        return register_proc('w24')
    def __set_w24_property__(self, value):
        return register_proc('w24', value)
    w24 = property(__get_w24_property__, __set_w24_property__)

    def __get_w25_property__(self):
        return register_proc('w25')
    def __set_w25_property__(self, value):
        return register_proc('w25', value)
    w25 = property(__get_w25_property__, __set_w25_property__)

    def __get_w26_property__(self):
        return register_proc('w26')
    def __set_w26_property__(self, value):
        return register_proc('w26', value)
    w26 = property(__get_w26_property__, __set_w26_property__)

    def __get_w27_property__(self):
        return register_proc('w27')
    def __set_w27_property__(self, value):
        return register_proc('w27', value)
    w27 = property(__get_w27_property__, __set_w27_property__)

    def __get_w28_property__(self):
        return register_proc('w28')
    def __set_w28_property__(self, value):
        return register_proc('w28', value)
    w28 = property(__get_w28_property__, __set_w28_property__)

    def __get_w29_property__(self):
        return register_proc('w29')
    def __set_w29_property__(self, value):
        return register_proc('w29', value)
    w29 = property(__get_w29_property__, __set_w29_property__)

# x86 register get/set
class x86(register_base):
    def __get__c_property__(self):
        return register_proc('_c')
    def __set__c_property__(self, value):
        return register_proc('_c', value)
    CF = property(__get__c_property__, __set__c_property__)

    def __get__p_property__(self):
        return register_proc('_p')
    def __set__p_property__(self, value):
        return register_proc('_p', value)
    PF = property(__get__p_property__, __set__p_property__)

    def __get__a_property__(self):
        return register_proc('_a')
    def __set__a_property__(self, value):
        return register_proc('_a', value)
    AF = property(__get__a_property__, __set__a_property__)

    def __get__z_property__(self):
        return register_proc('_z')
    def __set__z_property__(self, value):
        return register_proc('_z', value)
    ZF = property(__get__z_property__, __set__z_property__)

    def __get__s_property__(self):
        return register_proc('_s')
    def __set__s_property__(self, value):
        return register_proc('_s', value)
    SF = property(__get__s_property__, __set__s_property__)

    def __get__t_property__(self):
        return register_proc('_t')
    def __set__t_property__(self, value):
        return register_proc('_t', value)
    TF = property(__get__t_property__, __set__t_property__)

    def __get__i_property__(self):
        return register_proc('_i')
    def __set__i_property__(self, value):
        return register_proc('_i', value)
    IF = property(__get__i_property__, __set__i_property__)

    def __get__d_property__(self):
        return register_proc('_d')
    def __set__d_property__(self, value):
        return register_proc('_d', value)
    DF = property(__get__d_property__, __set__d_property__)

    def __get__o_property__(self):
        return register_proc('_o')
    def __set__o_property__(self, value):
        return register_proc('_o', value)
    OF = property(__get__o_property__, __set__o_property__)

    def __get_eax_property__(self):
        return register_proc('eax')
    def __set_eax_property__(self, value):
        return register_proc('eax', value)
    eax = property(__get_eax_property__, __set_eax_property__)

    def __get_ecx_property__(self):
        return register_proc('ecx')
    def __set_ecx_property__(self, value):
        return register_proc('ecx', value)
    ecx = property(__get_ecx_property__, __set_ecx_property__)

    def __get_edx_property__(self):
        return register_proc('edx')
    def __set_edx_property__(self, value):
        return register_proc('edx', value)
    edx = property(__get_edx_property__, __set_edx_property__)

    def __get_ebx_property__(self):
        return register_proc('ebx')
    def __set_ebx_property__(self, value):
        return register_proc('ebx', value)
    ebx = property(__get_ebx_property__, __set_ebx_property__)

    def __get_ebp_property__(self):
        return register_proc('ebp')
    def __set_ebp_property__(self, value):
        return register_proc('ebp', value)
    ebp = property(__get_ebp_property__, __set_ebp_property__)

    def __get_esi_property__(self):
        return register_proc('esi')
    def __set_esi_property__(self, value):
        return register_proc('esi', value)
    esi = property(__get_esi_property__, __set_esi_property__)

    def __get_edi_property__(self):
        return register_proc('edi')
    def __set_edi_property__(self, value):
        return register_proc('edi', value)
    edi = property(__get_edi_property__, __set_edi_property__)

    def __get_mm0_property__(self):
        return register_proc('mm0')
    def __set_mm0_property__(self, value):
        return register_proc('mm0', value)
    mm0 = property(__get_mm0_property__, __set_mm0_property__)

    def __get_mm1_property__(self):
        return register_proc('mm1')
    def __set_mm1_property__(self, value):
        return register_proc('mm1', value)
    mm1 = property(__get_mm1_property__, __set_mm1_property__)

    def __get_mm2_property__(self):
        return register_proc('mm2')
    def __set_mm2_property__(self, value):
        return register_proc('mm2', value)
    mm2 = property(__get_mm2_property__, __set_mm2_property__)

    def __get_mm3_property__(self):
        return register_proc('mm3')
    def __set_mm3_property__(self, value):
        return register_proc('mm3', value)
    mm3 = property(__get_mm3_property__, __set_mm3_property__)

    def __get_mm4_property__(self):
        return register_proc('mm4')
    def __set_mm4_property__(self, value):
        return register_proc('mm4', value)
    mm4 = property(__get_mm4_property__, __set_mm4_property__)

    def __get_mm5_property__(self):
        return register_proc('mm5')
    def __set_mm5_property__(self, value):
        return register_proc('mm5', value)
    mm5 = property(__get_mm5_property__, __set_mm5_property__)

    def __get_mm6_property__(self):
        return register_proc('mm6')
    def __set_mm6_property__(self, value):
        return register_proc('mm6', value)
    mm6 = property(__get_mm6_property__, __set_mm6_property__)

    def __get_mm7_property__(self):
        return register_proc('mm7')
    def __set_mm7_property__(self, value):
        return register_proc('mm7', value)
    mm7 = property(__get_mm7_property__, __set_mm7_property__)

    def __get_xmm0_property__(self):
        return register_proc('xmm0')
    def __set_xmm0_property__(self, value):
        return register_proc('xmm0', value)
    xmm0 = property(__get_xmm0_property__, __set_xmm0_property__)

    def __get_xmm1_property__(self):
        return register_proc('xmm1')
    def __set_xmm1_property__(self, value):
        return register_proc('xmm1', value)
    xmm1 = property(__get_xmm1_property__, __set_xmm1_property__)

    def __get_xmm2_property__(self):
        return register_proc('xmm2')
    def __set_xmm2_property__(self, value):
        return register_proc('xmm2', value)
    xmm2 = property(__get_xmm2_property__, __set_xmm2_property__)

    def __get_xmm3_property__(self):
        return register_proc('xmm3')
    def __set_xmm3_property__(self, value):
        return register_proc('xmm3', value)
    xmm3 = property(__get_xmm3_property__, __set_xmm3_property__)

    def __get_xmm4_property__(self):
        return register_proc('xmm4')
    def __set_xmm4_property__(self, value):
        return register_proc('xmm4', value)
    xmm4 = property(__get_xmm4_property__, __set_xmm4_property__)

    def __get_xmm5_property__(self):
        return register_proc('xmm5')
    def __set_xmm5_property__(self, value):
        return register_proc('xmm5', value)
    xmm5 = property(__get_xmm5_property__, __set_xmm5_property__)

    def __get_xmm6_property__(self):
        return register_proc('xmm6')
    def __set_xmm6_property__(self, value):
        return register_proc('xmm6', value)
    xmm6 = property(__get_xmm6_property__, __set_xmm6_property__)

    def __get_xmm7_property__(self):
        return register_proc('xmm7')
    def __set_xmm7_property__(self, value):
        return register_proc('xmm7', value)
    xmm7 = property(__get_xmm7_property__, __set_xmm7_property__)

    def __get_xmm8_property__(self):
        return register_proc('xmm8')
    def __set_xmm8_property__(self, value):
        return register_proc('xmm8', value)
    xmm8 = property(__get_xmm8_property__, __set_xmm8_property__)

    def __get_xmm9_property__(self):
        return register_proc('xmm9')
    def __set_xmm9_property__(self, value):
        return register_proc('xmm9', value)
    xmm9 = property(__get_xmm9_property__, __set_xmm9_property__)

    def __get_xmm10_property__(self):
        return register_proc('xmm10')
    def __set_xmm10_property__(self, value):
        return register_proc('xmm10', value)
    xmm10 = property(__get_xmm10_property__, __set_xmm10_property__)

    def __get_xmm11_property__(self):
        return register_proc('xmm11')
    def __set_xmm11_property__(self, value):
        return register_proc('xmm11', value)
    xmm11 = property(__get_xmm11_property__, __set_xmm11_property__)

    def __get_xmm12_property__(self):
        return register_proc('xmm12')
    def __set_xmm12_property__(self, value):
        return register_proc('xmm12', value)
    xmm12 = property(__get_xmm12_property__, __set_xmm12_property__)

    def __get_xmm13_property__(self):
        return register_proc('xmm13')
    def __set_xmm13_property__(self, value):
        return register_proc('xmm13', value)
    xmm13 = property(__get_xmm13_property__, __set_xmm13_property__)

    def __get_xmm14_property__(self):
        return register_proc('xmm14')
    def __set_xmm14_property__(self, value):
        return register_proc('xmm14', value)
    xmm14 = property(__get_xmm14_property__, __set_xmm14_property__)

    def __get_xmm15_property__(self):
        return register_proc('xmm15')
    def __set_xmm15_property__(self, value):
        return register_proc('xmm15', value)
    xmm15 = property(__get_xmm15_property__, __set_xmm15_property__)

    def __get_ymm0_property__(self):
        return register_proc('ymm0')
    def __set_ymm0_property__(self, value):
        return register_proc('ymm0', value)
    ymm0 = property(__get_ymm0_property__, __set_ymm0_property__)

    def __get_ymm1_property__(self):
        return register_proc('ymm1')
    def __set_ymm1_property__(self, value):
        return register_proc('ymm1', value)
    ymm1 = property(__get_ymm1_property__, __set_ymm1_property__)

    def __get_ymm2_property__(self):
        return register_proc('ymm2')
    def __set_ymm2_property__(self, value):
        return register_proc('ymm2', value)
    ymm2 = property(__get_ymm2_property__, __set_ymm2_property__)

    def __get_ymm3_property__(self):
        return register_proc('ymm3')
    def __set_ymm3_property__(self, value):
        return register_proc('ymm3', value)
    ymm3 = property(__get_ymm3_property__, __set_ymm3_property__)

    def __get_ymm4_property__(self):
        return register_proc('ymm4')
    def __set_ymm4_property__(self, value):
        return register_proc('ymm4', value)
    ymm4 = property(__get_ymm4_property__, __set_ymm4_property__)

    def __get_ymm5_property__(self):
        return register_proc('ymm5')
    def __set_ymm5_property__(self, value):
        return register_proc('ymm5', value)
    ymm5 = property(__get_ymm5_property__, __set_ymm5_property__)

    def __get_ymm6_property__(self):
        return register_proc('ymm6')
    def __set_ymm6_property__(self, value):
        return register_proc('ymm6', value)
    ymm6 = property(__get_ymm6_property__, __set_ymm6_property__)

    def __get_ymm7_property__(self):
        return register_proc('ymm7')
    def __set_ymm7_property__(self, value):
        return register_proc('ymm7', value)
    ymm7 = property(__get_ymm7_property__, __set_ymm7_property__)

    def __get_ymm8_property__(self):
        return register_proc('ymm8')
    def __set_ymm8_property__(self, value):
        return register_proc('ymm8', value)
    ymm8 = property(__get_ymm8_property__, __set_ymm8_property__)

    def __get_ymm9_property__(self):
        return register_proc('ymm9')
    def __set_ymm9_property__(self, value):
        return register_proc('ymm9', value)
    ymm9 = property(__get_ymm9_property__, __set_ymm9_property__)

    def __get_ymm10_property__(self):
        return register_proc('ymm10')
    def __set_ymm10_property__(self, value):
        return register_proc('ymm10', value)
    ymm10 = property(__get_ymm10_property__, __set_ymm10_property__)

    def __get_ymm11_property__(self):
        return register_proc('ymm11')
    def __set_ymm11_property__(self, value):
        return register_proc('ymm11', value)
    ymm11 = property(__get_ymm11_property__, __set_ymm11_property__)

    def __get_ymm12_property__(self):
        return register_proc('ymm12')
    def __set_ymm12_property__(self, value):
        return register_proc('ymm12', value)
    ymm12 = property(__get_ymm12_property__, __set_ymm12_property__)

    def __get_ymm13_property__(self):
        return register_proc('ymm13')
    def __set_ymm13_property__(self, value):
        return register_proc('ymm13', value)
    ymm13 = property(__get_ymm13_property__, __set_ymm13_property__)

    def __get_ymm14_property__(self):
        return register_proc('ymm14')
    def __set_ymm14_property__(self, value):
        return register_proc('ymm14', value)
    ymm14 = property(__get_ymm14_property__, __set_ymm14_property__)

    def __get_ymm15_property__(self):
        return register_proc('ymm15')
    def __set_ymm15_property__(self, value):
        return register_proc('ymm15', value)
    ymm15 = property(__get_ymm15_property__, __set_ymm15_property__)

# x86_64 register get/set
class x86_64(x86):
    def __get_rax_property__(self):
        return register_proc('rax')
    def __set_rax_property__(self, value):
        return register_proc('rax', value)
    rax = property(__get_rax_property__, __set_rax_property__)

    def __get_rcx_property__(self):
        return register_proc('rcx')
    def __set_rcx_property__(self, value):
        return register_proc('rcx', value)
    rcx = property(__get_rcx_property__, __set_rcx_property__)

    def __get_rdx_property__(self):
        return register_proc('rdx')
    def __set_rdx_property__(self, value):
        return register_proc('rdx', value)
    rdx = property(__get_rdx_property__, __set_rdx_property__)

    def __get_rbx_property__(self):
        return register_proc('rbx')
    def __set_rbx_property__(self, value):
        return register_proc('rbx', value)
    rbx = property(__get_rbx_property__, __set_rbx_property__)

    def __get_rbp_property__(self):
        return register_proc('rbp')
    def __set_rbp_property__(self, value):
        return register_proc('rbp', value)
    rbp = property(__get_rbp_property__, __set_rbp_property__)

    def __get_rsi_property__(self):
        return register_proc('rsi')
    def __set_rsi_property__(self, value):
        return register_proc('rsi', value)
    rsi = property(__get_rsi_property__, __set_rsi_property__)

    def __get_rdi_property__(self):
        return register_proc('rdi')
    def __set_rdi_property__(self, value):
        return register_proc('rdi', value)
    rdi = property(__get_rdi_property__, __set_rdi_property__)

    def __get_r8_property__(self):
        return register_proc('r8')
    def __set_r8_property__(self, value):
        return register_proc('r8', value)
    r8 = property(__get_r8_property__, __set_r8_property__)

    def __get_r9_property__(self):
        return register_proc('r9')
    def __set_r9_property__(self, value):
        return register_proc('r9', value)
    r9 = property(__get_r9_property__, __set_r9_property__)

    def __get_r10_property__(self):
        return register_proc('r10')
    def __set_r10_property__(self, value):
        return register_proc('r10', value)
    r10 = property(__get_r10_property__, __set_r10_property__)

    def __get_r11_property__(self):
        return register_proc('r11')
    def __set_r11_property__(self, value):
        return register_proc('r11', value)
    r11 = property(__get_r11_property__, __set_r11_property__)

    def __get_r12_property__(self):
        return register_proc('r12')
    def __set_r12_property__(self, value):
        return register_proc('r12', value)
    r12 = property(__get_r12_property__, __set_r12_property__)

    def __get_r13_property__(self):
        return register_proc('r13')
    def __set_r13_property__(self, value):
        return register_proc('r13', value)
    r13 = property(__get_r13_property__, __set_r13_property__)

    def __get_r14_property__(self):
        return register_proc('r14')
    def __set_r14_property__(self, value):
        return register_proc('r14', value)
    r14 = property(__get_r14_property__, __set_r14_property__)

    def __get_r15_property__(self):
        return register_proc('r15')
    def __set_r15_property__(self, value):
        return register_proc('r15', value)
    r15 = property(__get_r15_property__, __set_r15_property__)
