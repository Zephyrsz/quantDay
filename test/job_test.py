from strategy import stratgy_lib
from utilities.file_util import dataReader
from entity.entity import Data

data1 = Data(
    uri="/Users/roger.wei/app/qdata/jqdata/history_dir/history_000001.XSHE.csv",
    column_list=["date", "open", "close", "high", "low", "volume", "money"]
)

data2 = Data(
    uri="/Users/roger.wei/app/qdata/jqdata/history_dir/history_000006.XSHE.csv",
    column_list=["date", "open", "close", "high", "low", "volume", "money"]
)

df1 = dataReader(data1)
df2 = dataReader(data2)

# for i in range(-100,101):
#     print(stratgy_lib.shift_relate_pct(df1,df2,i))

# shift_range, relate_list = stratgy_lib.shift_relate_pct(df1, df2, 0)

# for i in relate_list[0]:
#     print(type(i))

# print(relate_list)
# print(len(relate_list))
# for i in range(len(relate_list)):
#     if relate_list[i] > 0.55:
#         if i == 0:
#             print(f"pos :{relate_list[i]}")
#         elif i ==1:
#             print(f"neg :{relate_list[i]}")

# for i in range(-100,101):
#     stratgy_lib.shift_relate_pct(df1,df2,i)

# shift_range, relate_list = stratgy_lib.shift_relate_pct(df1, df2, 0)
# dic = stratgy_lib.relate_filter(shift_range,relate_list,threshold=0.5)


dict_collect = {}
for i in range(-100, 101):
    shift_range, relate_list = stratgy_lib.shift_relate_pct(df1, df2, i)
    dict_i = stratgy_lib.relate_filter(shift_range, relate_list, threshold=0.55)
    if len(dict_i) > 0:
        for i in dict_i:
            dict_collect[i] = dict_i[i]

print(dict_collect)
