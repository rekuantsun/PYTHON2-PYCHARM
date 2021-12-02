import pickle
import Member
def dump_student(L):
    for i in L:
        f=open('list.obj','wb')
        pickle.dump(i,f)
        f.close()

def load_student(L):
    f = open('list.obj','r')
    r = pickle.load(f)
    return r
# dump_student
dump_student(L)
load_student(L)