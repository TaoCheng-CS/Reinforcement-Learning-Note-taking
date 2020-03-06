import numpy as np
np.random.seed(0)

class N_armed_bandit:
    # This is the class of N_armed_bandit
    # The reward is selected from Normal distribution with mean M_i and variance 1.
    def __init__(self,N:int,M:list,max_step:int):
        assert len(M)==N
        self.N=N
        self.store_generator=[]
        self.step=-1
        self.max_step=max_step
        for m in M:
            self.store_generator.append(np.random.normal(loc=m,size=max_step))
        self.index=[-1 for i in range(N)]
    
    def feedback(self,selected_arm:int):
        assert self.step<self.max_step
        assert selected_arm<self.N

        cur_index=self.index[selected_arm]+1
        self.index[selected_arm]=cur_index
        self.step+=1
        return self.store_generator[selected_arm][cur_index]

class eps_greedy:
    def __init__(self,eps:float,N:int):
        assert eps>=0 and eps<=1
        self.eps=eps
        self.N=N
        self.estimate=[0 for i in range(N)]
        self.time=[0 for i in range(N)]

    def choose(self):
        if np.random.rand(1)>self.eps:
            choice=np.argmax(self.estimate)
            return choice
        else:
            choice=np.random.randint(low=0,high=self.N)
            return choice
    
    def update(self,choice:int,reward:float):
        assert choice>=0 and choice<self.N 
        self.estimate[choice]=(self.estimate[choice]*self.time[choice]+reward)/(self.time[choice]+1)
        self.time[choice]+=1
        return True
    
    def swap_memory(self):
        self.estimate=[0 for i in range(N)]
        self.time=[0 for i in range(N)]
        return True


def generate_bandit(Test_num:int,N:int,max_step:int):
    initiate_parameter=np.random.randn(Test_num*N)
    for i in range(Test_num):
        params=initiate_parameter[i*N:(i+1)*N]
        optimal_choice=np.argmax(params)
        yield N_armed_bandit(N,params.tolist(),max_step),optimal_choice


def experiment(algorithm:eps_greedy,Test_num:int,N:int,max_step:int):
    Reward=[]
    Choose=[]
    for bandit,optimal_choice in generate_bandit(Test_num,N,max_step):
        algorithm.swap_memory()
        r=[]
        c=[]
        for i in range(max_step):
            choice=algorithm.choose()
            reward=bandit.feedback(choice)
            algorithm.update(choice,reward)
            r.append(reward)
            if optimal_choice==choice:
                c.append(1)
            else:
                c.append(0)
        Reward.append(r)
        Choose.append(c)
    
    return Reward,Choose

N=10
Test_num=2000
max_step=1000

alg1=eps_greedy(0,N)
alg2=eps_greedy(0.1,N)
alg3=eps_greedy(0.01,N)

R=[]
C=[]
L=[alg1,alg2,alg3]
for alg in L:
    reward,choose=experiment(alg,Test_num,N,max_step)
    reward_avg=np.average(reward,axis=0)
    choose_average=np.average(choose,axis=0)
    R.append(reward_avg)
    C.append(choose_average)
R=np.array(R)
C=np.array(C)

np.save("Average Reward",R)
np.save("Optimal Action",C)