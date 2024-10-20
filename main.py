import sys
sys.path.insert(0, './Introduction')
sys.path.insert(0, './Selenium')
sys.path.insert(0, './Requests')
sys.path.insert(0, './BeautifulSoup')

import intro_main as proc_1
import Scrape_Simple_Text_with_Selenium as proc_2
import Automate_Login as proc_3
import Login_and_Scrape as proc_4
import Access_titan22 as proc_5
import Download_Stock_Data as proc_6
import Scrape_RealTime_Currency_Rate as proc_7

# --- Set run status
proc_1_run = 0
proc_2_run = 0
proc_3_run = 0
proc_4_run = 0
proc_5_run = 0
proc_6_run = 0
proc_7_run = 1

# --- Trigger main function
proc_1.main(proc_1_run)
proc_2.main(proc_2_run)
proc_3.main(proc_3_run)
proc_4.main(proc_4_run)
proc_5.main(proc_5_run)
proc_6.main(proc_6_run)
proc_7.main(proc_7_run)