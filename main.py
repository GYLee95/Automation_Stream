import sys
sys.path.insert(0, './Introduction')
sys.path.insert(0, './Selenium')

import intro_main as proc_1
import Scrape_Simple_Text_with_Selenium as proc_2
import Automate_Login as proc_3
import Login_and_Scrape as proc_4
import Access_titan22 as proc_5

# --- Set run status
proc_1_run = 0
proc_2_run = 0
proc_3_run = 0
proc_4_run = 0
proc_5_run = 1

proc_1.main(proc_1_run)
proc_2.main(proc_2_run)
proc_3.main(proc_3_run)
proc_4.main(proc_4_run)
proc_5.main(proc_5_run)

