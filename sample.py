import pandas as pd
import os
from time import time



start_time = time()

path = r'C:\Users\admin\Downloads\listofpath'
dir_list = os.listdir(path)

table_list = []
data_frames = []

# Extract the file from the list
for file_name in dir_list:

    if file_name.endswith('.csv'):
        table_list.append(file_name[:-4])
        df = pd.read_csv(os.path.join(path, file_name))
        data_frames.append(df)


count = 1

def processData(constantDf, dynamicDf):
    global count
    firstdata_frame = data_frames[constantDf]
    for i in firstdata_frame.columns:
        first_column = firstdata_frame[i]
        if dynamicDf < len(data_frames):
            for j in data_frames[dynamicDf + 1].columns:
                core_logic(constantDf, dynamicDf, first_column, i, j, firstdata_frame)


def core_logic(constantDf, dynamicDf, first_column, i, j, firstdata_frame):
    global count
    second_data_frame = data_frames[dynamicDf + 1]
    second_column = second_data_frame[j]

    f_datatype = first_column.dtype
    s_datatype = second_column.dtype
    if f_datatype == s_datatype:
        matching_values = first_column.isin(second_column)
        # matching_values = firstdata_frame.merge(second_data_frame, how='inner', left_on=first_column, right_on=second_column)
        # no_of_rows = matching_values.shape[0]

        firstColumn_matching_percentage = (matching_values.sum() / len(first_column)) * 100
        secondColumn_matching_percentage = (matching_values.sum() / len(second_column)) * 100

        # firstColumn_matching_percentage = no_of_rows / first_column.shape[0]
        # secondColumn_matching_percentage = no_of_rows / second_column.shape[0]
        # if firstColumn_matching_percentage > 3 or secondColumn_matching_percentage > 3:

        print(os.linesep + "comparison_count:" + str(count))
        print("First Table :" + table_list[constantDf] + os.linesep + "Second Table:" + table_list[dynamicDf + 1])
        print("column 1:" + i + os.linesep + "column 2:" + j)
        print("Matching percentage first column to second is:" + str(firstColumn_matching_percentage))
        print("Matching percentage Second Column  to first is:" + str(secondColumn_matching_percentage))
    count += 1

for constantDf in range(len(data_frames) - 1):
    for DynamicDf in range(len(data_frames) - 1):
        processData(constantDf, DynamicDf)
print("********-----------------completed-----------------********")

end_time = time()
elapsed_time = end_time - start_time
print(elapsed_time)

print(f"Elapsed time: {elapsed_time:.2f} seconds")
