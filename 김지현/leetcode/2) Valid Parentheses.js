// var isValid = function (s) {
//   if (s.length % 2) return false;

//   const open = ["(", "{", "["];
//   const close = [")", "}", "]"];
//   const stack = [];

//   for (let i = 0; i < s.length; i++) {
//     const openIndex = open.indexOf(s[i]);
//     if (openIndex !== -1) {
//       stack.push(close[openIndex]);
//       continue;
//     }

//     const latest = stack.pop();
//     if (latest !== s[i]) return false;
//   }

//   return stack.length ? false : true;
// };

var isValid = function (s) {
  if (s.length % 2) return false;
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    switch (s[i]) {
      case "(": {
        stack.push(")");
        break;
      }
      case "{": {
        stack.push("}");
        break;
      }
      case "[": {
        stack.push("]");
        break;
      }
      default: {
        const latest = stack.pop();
        if (s[i] !== latest) return false;
      }
    }
  }

  return !stack.length;
};
