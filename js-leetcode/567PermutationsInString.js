
var checkInclusion = function(s1, s2) {
    if (s1.length > s2.length) {
        return false;
    }
    let acode = "a".charCodeAt(0);
    let s1Count = Array(26).fill(0);
    let s2Count = Array(26).fill(0);

    for (const i in s1) {
        s1Count[s1[i].charCodeAt(0) - acode] += 1
        s2Count[s2[i].charCodeAt(0) - acode] += 1
    }

    let matches = 0;
    for (const i in s1Count) {
        if (s1Count[i] === s2Count[i]) {
            matches += 1
        }
    }
    let l = 0;
    let index;
    for (let r = s1.length; r < s2.length; r++) {
        if (matches === 26) {return true;}
        index = s2[r].charCodeAt(0) - acode;
        s2Count[index] += 1
        if (s1Count[index] === s2Count[index]) {
            matches += 1;
        }
        else if (s1Count[index] + 1 === s2Count[index]) {
            matches -= 1;
        }

        index = s2[l].charCodeAt(0) - acode
        s2Count[index] -= 1
        if (s1Count[index] === s2Count[index]) {
            matches += 1
        }
        else if (s1Count[index] - 1 === s2Count[index]) {
            matches -= 1
        }
        l += 1

    }
    return matches === 26
};