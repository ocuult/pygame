import random

# ti_mu_shu_liang:总共出多少道题
# jie_guo_zui_da:运算结果的最大值
# jie_guo_zui_xiao:运算结果的最小值
# yun_suan_fu:运算类型 0)单加法 1)加减混合 2)加减乘混合 3)加减乘除混合

def ti_mu(ti_mu_shu_liang, jie_guo_zui_da, jie_guo_zui_xiao,yun_suan_fu):
    while ti_mu_shu_liang:
        num_one = random.randint(1, 20)
        num_two = random.randint(1, 20)
        num_three = random.randint(1, 20)
        operator = ('+', '-', '*', '/')
        ti_mu = str(num_one) + operator[random.randint(0, yun_suan_fu)] + str(num_two) + operator[random.randint(0, yun_suan_fu)] + str(
            num_three)
        if jie_guo_zui_da >= eval(ti_mu) >= jie_guo_zui_xiao and int(eval(ti_mu))==float(eval(ti_mu)):
            print('{}={}'.format(ti_mu, eval(ti_mu)))
            ti_mu_shu_liang -= 1


ti_mu(20, 100, 25,3)
