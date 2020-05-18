#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fillall(x):
    x.fillna(method='ffill',inplace=True)
    x.fillna(method='bfill',inplace=True)
    


# In[2]:


def dropnull(x):
    x.dropna(subset=x.columns,how='any',inplace=True)


# In[6]:


def strclr(data1):
    a=data1[~data1['Low'].apply(lambda x: str(x).endswith("a"))]
    b=a[~data1['Low'].apply(lambda x: str(x).endswith("b"))]
    c=b[~data1['Low'].apply(lambda x: str(x).endswith("c"))]
    d=c[~data1['Low'].apply(lambda x: str(x).endswith("d"))]
    e=d[~data1['Low'].apply(lambda x: str(x).endswith("e"))]
    f=e[~data1['Low'].apply(lambda x: str(x).endswith("f"))]
    g=f[~data1['Low'].apply(lambda x: str(x).endswith("g"))]
    h=g[~data1['Low'].apply(lambda x: str(x).endswith("h"))]
    i=h[~data1['Low'].apply(lambda x: str(x).endswith("i"))]
    j=i[~data1['Low'].apply(lambda x: str(x).endswith("j"))]
    k=j[~data1['Low'].apply(lambda x: str(x).endswith("k"))]
    l=k[~data1['Low'].apply(lambda x: str(x).endswith("l"))]
    m=l[~data1['Low'].apply(lambda x: str(x).endswith("m"))]
    n=m[~data1['Low'].apply(lambda x: str(x).endswith("n"))]
    o=n[~data1['Low'].apply(lambda x: str(x).endswith("o"))]
    p=o[~data1['Low'].apply(lambda x: str(x).endswith("p"))]
    q=p[~data1['Low'].apply(lambda x: str(x).endswith("q"))]
    r=q[~data1['Low'].apply(lambda x: str(x).endswith("r"))]
    s=r[~data1['Low'].apply(lambda x: str(x).endswith("s"))]
    t=s[~data1['Low'].apply(lambda x: str(x).endswith("t"))]
    u=t[~data1['Low'].apply(lambda x: str(x).endswith("u"))]
    v=u[~data1['Low'].apply(lambda x: str(x).endswith("v"))]
    w=v[~data1['Low'].apply(lambda x: str(x).endswith("w"))]
    x=w[~data1['Low'].apply(lambda x: str(x).endswith("x"))]
    y=x[~data1['Low'].apply(lambda x: str(x).endswith("y"))]
    z=y[~data1['Low'].apply(lambda x: str(x).endswith("z"))]
    A=z[~data1['Low'].apply(lambda x: str(x).endswith("A"))]    
    strc=A[~data1['Low'].apply(lambda x: str(x).startswith("a"))]


# In[ ]:




