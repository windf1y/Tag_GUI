import json
import tkinter as tk

# 准备数据
# 读取第一个json文件
with open('chinese.txt', 'r') as f1:
    data1 = json.loads(f1.read())
# 读取第二个json文件
with open('english.txt', 'r') as f2:
    data2 = json.loads(f2.read())
keys = [i for i in data1.keys()]

window = tk.Tk()
window.title('demo1')
window.geometry('1200x800')

# 设置全局变量
var_keys = tk.StringVar()
var_values_EN = tk.StringVar()
var_values_CN = tk.StringVar()
var_select = tk.StringVar()
selected_index = []

# 初始化
var_keys.set(keys)

# 函数
def select_key(event):
    index = event.widget.curselection()
    if index:
        item = event.widget.get(index)
        var_values_CN.set(data1[item])
        var_values_EN.set(data2[item])


def select_value(event):
    index = event.widget.curselection()
    if index:
        if len(index) < len(selected_index):
            for i in selected_index:
                if i not in index:
                    selected_index.remove(i)
        else:
            for i in index:
                if i not in selected_index:
                    selected_index.append(i)
        update_select(display_values_CN)
        update_select(display_values_EN)

def clear_listbox_select(item):
    item.selection_clear(0, item.size())

def update_select(item):
    index = selected_index[:]
    clear_listbox_select(item)
    for i in index:
        item.selection_set(i)

def update_result(event):
    if selected_index:
        key = display_key.get(display_key.curselection())
        value = []
        for i in selected_index:
            value.append(data1[key][i])
        var_select.set(value)


# 第一行
# 部件--frame框架
hor_1 = tk.Frame(window)
hor_1.place(x=0, y=0, height=70, width=1200)

button_insert_CN = tk.Button(hor_1)
button_insert_CN.place(x=50, y=10, width=500, height=40)
button_insert_CN.config(width=20, height=2, text='待定')
button_insert_EN = tk.Button(hor_1)
button_insert_EN.place(x=650, y=10, width=500, height=40)
button_insert_EN.config(width=20, height=2, text='待定')

# 第二行
hor_2 = tk.Frame(window)
hor_2.place(x=0, y=70, height=250, width=1200)

# 第一块（共三块，水平排布）
block_1 = tk.Frame(hor_2)
block_1.place(x=20, y=0, width=360, height=250)
display_key_label = tk.Label(block_1, text='键')
display_key_label.pack(side='top')
display_key_label.config(width=360, height=2)
display_key = tk.Listbox(block_1, listvariable=var_keys, selectmode='single')
display_key.pack(side='bottom')
display_key.config(width=360, height=250, exportselection = False)
display_key.bind("<<ListboxSelect>>", select_key)

# 第二块
block_2 = tk.Frame(hor_2)
block_2.place(x=420, y=0, width=360, height=250)
display_values_CN_label = tk.Label(block_2, text='值（中文）')
display_values_CN_label.pack(side='top')
display_values_CN_label.config(width=360, height=2)
display_values_CN = tk.Listbox(block_2, listvariable=var_values_CN, selectmode='multiple')
display_values_CN.pack(side='bottom')
display_values_CN.config(width=360, height=250)
display_values_CN.bind("<<ListboxSelect>>", select_value)

# 第三块
block_3 = tk.Frame(hor_2)
block_3.place(x=820, y=0, width=360, height=250)
display_values_EN_label = tk.Label(block_3, text='值（英文）')
display_values_EN_label.pack(side='top')
display_values_EN_label.config(width=360, height=2)
display_values_EN = tk.Listbox(block_3, listvariable=var_values_EN, selectmode='multiple')
display_values_EN.pack(side='bottom')
display_values_EN.config(width=360, height=250, exportselection = False)
display_values_EN.bind("<<ListboxSelect>>", select_value)

# 第三行
hor_3 = tk.Frame(window)
hor_3.place(x=0, y=360, height=240, width=1200)

# 第一块（共两块，分别是临时选中和最终结果）
block_4 = tk.Frame(hor_3)
block_4.place(x=20, y=0, width=360, height=250)
display_select_label = tk.Label(block_4, text='已选中')
display_select_label.pack(side='top')
display_select_label.config(width=360, height=2)
display_select = tk.Listbox(block_4, listvariable=var_select)
display_select.pack(side='top')
display_select.config(width=360, height=250)

# 第二块
block_5 = tk.Frame(hor_3)
block_5.place(x=420, y=0, width=760, height=250)
display_output_label = tk.Label(block_5, text='输出')
display_output_label.pack(side='top')
display_output_label.config(width=760, height=2)
display_output = tk.Text(block_5, )
display_output.pack(side='top')
display_output.config(width=760, height=15)

# 第四行
hor_4 = tk.Frame(window)
hor_4.place(x=0, y=700, height=80, width=1200)

button_add = tk.Button(hor_4)
button_add.place(x=50, y=10, width=300, height=40)
button_add.config(width=20, height=2, text='添加')
button_add.bind('<Button-1>', update_result)

button_del = tk.Button(hor_4)
button_del.place(x=450, y=10, width=300, height=40)
button_del.config(width=20, height=2, text='清空')

button_output = tk.Button(hor_4)
button_output.place(x=850, y=10, width=300, height=40)
button_output.config(width=20, height=2, text='输出')
# button_del.bind('<Button-1>', update_result)

# 部件--listbox
# var_lb = tk.StringVar()
# var_lb.set(keys)
# lb = tk.Listbox(window, listvariable=var_lb, width=10, height=5, selectmode='multiple', yscrollcommand=sb.set)
# lb.pack()
# sb.config(command=lb.yview)
# 判断是否选中
# print(listbox.select_includes(0))
# print(listbox.select_includes(2))

# 部件--scrollbar
# sb = tk.Scrollbar(window, orient='vertical') # orient参数是方向，X轴或Y轴
# sb.pack(side='right', fill='y')
# 部件--button
# b = tk.Button(window, text='读取', width=15, height=2)
# 部件--entry
# e = tk.Entry(window, show = None)
# 启动
window.mainloop()
