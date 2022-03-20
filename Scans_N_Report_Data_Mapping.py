import os 
from itertools import product
import shutil 
# for (dirpath, dirnames, filenames) in walk("F:/Medical_AI/VRH_Pune/V3/X_RAY"):
#     f.extend(filenames)

SCANS = os.listdir("F:/Medical_AI/VRH_Pune/V3/Report_N_Scans/X_RAY")
REPORTS = os.listdir("F:/Medical_AI/VRH_Pune/V3/Report_N_Scans/X ray report_1")

for i in range(1):

    for (dirnames, Report_Files) in product(SCANS, REPORTS):
        Scans_PID = dirnames.split('_')[1]
        Scans_PID_Sex = dirnames.split('_')[-1]

        Reports_PID = Report_Files.split('_')[3]

        if Scans_PID == Reports_PID:
            # print("Scans_PID: ",Scans_PID, Scans_PID_Sex)
            # print("Reports_PID: ",Reports_PID)

            for i in REPORTS:
                if Scans_PID in Report_Files:
                    for z in REPORTS: 
                        shutil.copy(f"F:/Medical_AI/VRH_Pune/V3/Report_N_Scans/X ray report_1/{Report_Files}", 
                        f"F:/Medical_AI/VRH_Pune/V3/Report_N_Scans/X_RAY/PID_{Scans_PID}_Age_Y_Sex_{Scans_PID_Sex}")

                    # print("Segregated: ",Scans_PID, Report_Files, Scans_PID_Sex)

                # final_list = [nm for ps in Reports_PID for nm in full_list if ps in nm]

        else: 
            print("Match not found")


                
       


