{
    p({a,b}, {c}),
    p({c}, {d,e}), 
    iL, 
    oL
}

{
    (a, p({a,b}, {c})),
    (b, p({a,b}, {c})),
    (p({a,b}, {c}), c),

    (c, p({c}, {d,e})), 
    (p({c}, {d,e}), d), 
    (p({c}, {d,e}), e), 
    
    (iL,a),
    (iL,b),
    (d,oL),
    (e,oL)
}