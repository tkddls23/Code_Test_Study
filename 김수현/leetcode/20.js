/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    let answer = true;
    const map = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    };
    const stack = [];
    const open = Object.keys(map); //["(", "[", "{"]
    
    //s의 길이가 짝수가 아닐시 리턴
    if (s.length % 2 !== 0) return false;
    
    for (let x of s) {
        //x가 여는 괄호면 stack에 push
        if (open.includes(x)) stack.push(x);
        else { //x가 닫는 괄호라면
            //만약 stack의 맨 위에 있는 여는 괄호의 value가 x와 같다면 stack pop
            if (map[stack[stack.length - 1]] === x) stack.pop();
            else return false;
        }
    }
    
    if (stack.length !== 0) return false;
    
    return answer;
};