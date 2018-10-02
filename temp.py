
df['year_and_month'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
df['year_and_month'] = df['year_and_month'].astype('str').apply(lambda x: x[:7])

# 配件信息
part_infos = df[['part_id', 'part_name', 'year_and_month']]

part_infos = part_infos.reset_index()
part_infos = part_infos.drop_duplicates().set_index('date')

# 配件的统计信息
part_statics = df[['order_num', 'out_of_stock_num', 'delivery_num']]

def parse_date(str):
    return datetime.strptime(str, '%Y-%m-%d')

# 加载数据
data_path = "../../data/luggage_compartment_door.txt"
df = pd.read_csv(data_path, sep='\t')

# 重新命名列名
df.rename(columns={'物料编码': 'part_id', '物料描述': 'part_name', 
                   '订货数': 'order_num', '缺件数': 'out_of_stock_num', 
                   '受理数': 'delivery_num', '审核日期': 'date', '审核时间': 'time'}, inplace=True)

# 将`part_id`的数据类型设为字符串，方便后面进行重采样 
df['part_id'] = df['part_id'].astype('str')

# 重置索引
# df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
df['date'] = df['date'].apply(parse_date)
df.set_index('date', inplace=True)

# 按照时间排序
df.sort_index(inplace=True)

# 采样
df_day = df.resample('D').sum()

df_2018 = df_day['2018']