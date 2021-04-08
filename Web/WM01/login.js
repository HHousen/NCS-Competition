const hl_a = ['1449831pDAfRY', '688334HEwyty', 'loginPassword', '30008AUiqft', 'et-v', 'eed', 'rup', 'disabled', 'location', 'marginLeft', 'getElementById', '1523034CeStTi', 'Logging you in, one moment...', 'l.med.ia', 'ork', 'loginEmail', '131fDfiIr', '23weuLRx', 'mera', '861477UyJRfM', 'className', '3079038fzJpCZ', '799emksQB', 'izua', 'value', 'loginSubmit'];
const hl_b = function (a, b) {
    a = a - 0x70;
    let c = hl_a[a];
    return c;
};
(function (a, b) {
    const g = hl_b;
    while (!![]) {
        try {
            const c = -parseInt(g(0x76)) + -parseInt(g(0x88)) * -parseInt(g(0x7c)) + -parseInt(g(0x86)) + parseInt(g(0x7e)) + parseInt(g(0x81)) * -parseInt(g(0x7b)) + -parseInt(g(0x85)) + parseInt(g(0x80));
            if (c === b) break;
            else a['push'](a['shift']());
        } catch (d) {
            a['push'](a['shift']());
        }
    }
}(hl_a, 0xd323f));

function login(a, b) {
    const h = hl_b;
    document[h(0x75)](h(0x84))[h(0x72)] = !![];
    if (a === h(0x71) + 'ert@g' + h(0x89) + h(0x82) + h(0x78) && b === 'ne' + 'wy' + h(0x79)) setTimeout(function () {
        const i = h;
        document['getElementById'](i(0x84))[i(0x83)] = i(0x77), document['getElementById'](i(0x84))[i(0x7f)] = 'loggingIn';
    }, 0x2bc), setTimeout(function () {
        const j = h;
        window[j(0x73)] = 'se' + 'curi' + 'ty-' + 'ca' + j(0x7d) + '/f' + j(0x70);
    }, 0xbb8);
    else {
        const c = [0x18, -0x18, 0xc, -0xc, 0x6, -0x6, 0x3, -0x3, 0x0];
        let d = -0x1,
            f = setInterval(function () {
                const k = h;
                d < c['length'] ? (d++, document[k(0x75)]('loginContainer')['style'][k(0x74)] = c[d] + 'px', d === 0x2 && (document[k(0x75)](k(0x7a))[k(0x83)] = '', document[k(0x75)](k(0x87))['value'] = '')) : (clearInterval(f), document[k(0x75)](k(0x84))[k(0x72)] = ![]);
            }, 0x32);
        return ![];
    }
}