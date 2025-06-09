import re
import json
from collections import Counter

# # 1. 测试1 实现一个函数 even_sum(lst)，输入一个整数列表，返回其中所有偶数的和
# def even_sum(lst):
#     a = []
#     for i in lst:
#         if i % 2 == 0:
#             a.append(i)
#     return sum(a)
# print(even_sum([1, 2, 3, 4, 5, 6])) # 结果是12

# # 2. 测试1升级版 统计字符串中出现频率最高的字符（忽略大小写和空格）
# def char_count(str):
#     str = re.sub(r'[^a-zA-Z0-9]', '', str)  # 用正则匹配所有不是字母或者数字的字符，替换成空字符, 也就是替换所有的标点符号和空格
#     str = str.lower()
#     count = {}
#     for i in str:
#         if i not in count:
#             count[i] = 1
#         else:
#             count[i] += 1

#     max_key = max(count, key=count.get) # 用max方法，来比较各个key对应的value，返回最大的那个key名字，如果有多个相同的最大值，返回第一个key
#     return max_key, count[max_key] # 返回key和对应的value
# print(char_count("Demonstrators clashed with police downtown over the weekend, with crowds spilling onto a highway and setting fire to driverless cars"))

# # 3. 测试1 升级排序版然后输出

# def char_count(str):
#     str = re.sub(r'[^a-zA-Z0-9]', '', str)  # 用正则匹配所有不是字母或者数字的字符，替换成空字符, 也就是替换所有的标点符号和空格
#     str = str.lower()
#     count = {}
#     for i in str:
#         count[i] = count.get(i, 0) + 1  # 等价上面的if，如果i不在字典中，return 默认值0

#     sort_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
#     return sort_count

# print(char_count("The California chapter of the Service Employees International Union planned for a rally before the arraignment of its president, David Huerta, who was arrested on Friday while protesting a raid by ICE agents in Los Angeles."))

# # 4. 测试1 升级到提取单词，分析出现次数，通过参数控制是否需要忽略大小写

# def word_count_sorted(str, isignore_case=True):
#     if isignore_case:
#         str = str.lower()
#     count = {}
#     str = re.findall(r'\b\w+\b', str)  # \b是非字母、数字或下划线的字符\w一个或者多个字母、数字或下划线，正则规则识别提取单词，输出列表
#     for w in str:
#         count[w] = count.get(w, 0) + 1
#     sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
#     return sorted_count

# print(word_count_sorted("The California chapter of the Service Employees International Union planned for a rally before the arraignment of its president, David Huerta, who was arrested on Friday while protesting a raid by ICE agents in Los Angeles."))


# 5. 测试1 从.txt文件中读取文章，统计总单词数量，前三名的单词，前三名占比%，结果保存为.json
def analyze_file_words(filepath, output_path, n):
    # 读取文件内容，转化成小写字母
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    
    # 提取单词, re.finall返回一个列表
    words = re.findall(r'\b\w+\b', text) 
    
    # 单词总数
    total_words = len(words)

    # 统计出现次数 collections.Counter自动进行统计，生成一个字典来保存元素和出现的次数
    count = Counter(words)
    topn = count.most_common(n)  # .most_common(n) 给出统计次数最高的前N个元素的列表，里面的元素，次数的元组数据，输出: [('apple', 3), ('banana', 2)]

    # 计算百分比
    result = []
    for word, count in topn:
        percent = count / total_words * 100
        result.append({
            'word': word,
            'count': count,
            'percentage': f"{percent:.2f}%"
        }

        )
    # 保存为json
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            'totoal_words': total_words,
            f'Top {n}': result
        }, f, ensure_ascii=False, indent=2)
    
    print("分析完成，结果已保存到", output_path)


analyze_file_words('analyze_file_words.txt', 'file_words.json', 5)






    