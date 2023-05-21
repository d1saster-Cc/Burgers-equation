#for expl

#expl1
b = expl_2(
    f=lambda u: 2*(u**2),
    init=lambda x: np.sqrt(x),
    bound1=lambda t: -2,
    bound2=lambda t: 2,
    a=0,
    b=10,
    h=0.04,
    tau=0.0005,
    t_end=2,
    eps=0.1
)

#expl2
b = expl_2(
    f=lambda u: -u,
    init=lambda x: -x+2,
    bound1=lambda t: 2.5,
    bound2=lambda t: 0.5,
    a=0,
    b=4,
    h=0.05,
    tau=0.005,
    t_end=2.5,
    eps=0.05
)

#expl3
b = expl_2(
    f=lambda u: u,
    init=lambda x: -x+2,
    bound1=lambda t: 2.5,
    bound2=lambda t: 0.5,
    a=0,
    b=4,
    h=0.05,
    tau=0.005,
    t_end=2.5,
    eps=0.1
)

#for impl

#impl1
b = impl_2(
    f=lambda u: u,
    init=lambda x: -x+2,
    bound_1=lambda t: 2.5,
    bound_2=lambda t: 0.5,
    a=0,
    b=4,
    h=0.05,
    tau=0.005,
    t_end=2.5,
    eps=0.1
)
