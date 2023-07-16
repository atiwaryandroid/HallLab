from FPGA_Config import *
import datetime
import math

#Connect and proram FPGA
array_returned = FPGA_Config(r"C:\Users\Adjain\Documents\MATLAB\EIS_v1p1\EIS_V1p1\top_eis.bit") 
mlist = array_returned[0]
snlist = array_returned[1]
xem = array_returned[2]
xptr = array_returned[3]
print("==========================================\n")
print("Start testing " + datetime.now().hour() + ":" + datetime.now().minute() + ":" + datetime.now().second() + "\n")
print("==========================================\n")

#Setup parameter
t_measure = 1
test_scan_in = '0' #'1': test scan chain of test structure, '0': normal operation
load_source = '1' #'1': trigger one time asynchronous, '0': the same as S_CLK
en_clk_c = '0' #'1': enable, '0': disable
rst_pd = '1' #'1': normal operation, '0': reset phase detector
trimrf0 = '0' #'1': enable 7.5k Rf parallel resistor
trimrf1 = '0' #'1': enable 20k Rf parallel resistor
ref_sel = '0' #'1': ext                                                                                                                                                                                                                                                                                                           , '0': from ref pixel                            //Bypass ref pixel in test structure and array for characterization//
ref_sel_ext = '0' #'1': w/ inv chain, '0' w/o inv chain                     //Option for ext clock used when ref pixel bypassed in array//
no_col_readout = '0000' #'0000' to '1111' readout # of columns "no_col_readout+1" //Select how many columns to read, 1 to 16//

#TDC sampling frequency = Fclk/N, N>=21 (limited due to scan chain, it further dcreases when reading out rows
#% set ref clk frequency
f_ref_clk = 10000000 #unit: Hz, max: 100MHz
t_ref_clk = 50000000/f_ref_clk #f_clk = 100M/2/data_hr_sw
xem.SetWireInValue(t_ref_clk) #NOT SURE IF THIS IS RIGHT, THE MATLAB VERSION HAS 2 MORE ARGUMENTS

#% set scan clk frequency
f_scan_clk = 1000000 # unit: Hz, max: 10MHz
t_scan_clk = math.floor(12500000/f_scan_clk) # f_clk = 100M/2/data_hr_sw
xem.SetWireInValue(t_scan_clk) #NOT SURE IF THIS IS RIGHT, THE MATLAB VERSION HAS 2 MORE ARGUMENTS

f_scan_real = 12500000/(21 * t_scan_clk)
print("scan rate is set as {}\n".format(f_scan_real)) #%  //  Read the whole thing out - datalength = 21  //

pulsevals = 5
