import random

def ti_mu(ti_mu_shu_liang,jie_guo_zui_da,jie_guo_zui_xiao):
    while ti_mu_shu_liang:
        num_one=random.randint(1,20)
        num_two=random.randint(1,20)
        num_three=random.randint(1,20)
        operator=('+','-','*')
        ti_mu=str(num_one)+operator[random.randint(0,2)]+str(num_two)+operator[random.randint(0,2)]+str(num_three)
        if jie_guo_zui_da>=eval(ti_mu)>=jie_guo_zui_xiao:
            print('{}={}'.format(ti_mu,eval(ti_mu)))
            ti_mu_shu_liang-=1

ti_mu(20,100,11)
