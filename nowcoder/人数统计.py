'''题目
小易的公司一共有n名员工, 第i个人每个月的薪酬是xi万元。
现在小易的老板向小易提了m次询问, 每次询问老板都会给出一个整数k,
小易要快速回答老板工资等于k的员工的数量。

输入描述:
第一行，两个空格间隔的整数m和n,表示人数和提问的次数
第二行，n个用空格间隔的整数xi，表示每名员工的薪酬
接下来有m行，每行一个整数，表示老板的一次提问。
1<=m<=80000 ,1<=n<=100000 ,1<=xi<=500,000,000

​输出描述:
m行，每行一个整数，表示对应提问的答案'''

n, m = map(int, input().split())
salary_li = list(map(int, input().split()))
dict1 = {}
for i in range(len(salary_li)):
    if salary_li[i] in dict1:
        dict1[salary_li[i]] += 1
    else:
        dict1[salary_li[i]] = 1
for _ in range(m):
    salary = int(input())
    if salary in dict1:
        print(dict1[salary])
    else:
        print('0')