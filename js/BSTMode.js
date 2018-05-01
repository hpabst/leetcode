
function TreeNode(val){
  this.val = val;
  this.left = null;
  this.right = null;
}

function dfs(root){
    if(root === null){
        return [];
    } else {
        let child_vals = [];
        child_vals.push(root.val);
        child_vals.push.apply(child_vals, dfs(root.left));
        child_vals.push.apply(child_vals, dfs(root.right));
        return child_vals;
    }
}

var findMode = function(root){
    let vals = dfs(root);
    let frequencies = {};
    let max_vals = [];
    let max_count = 0;
    for(let i = 0; i < vals.length; i++){
        let v = vals[i];
        if(!(v in frequencies)){
            frequencies[v] = 0;
        }
        frequencies[v] += 1;
        if(frequencies[v] === max_count){
            max_vals.push(v);
        } else if(frequencies[v] > max_count){
            max_count = frequencies[v];
            max_vals = [];
            max_vals.push(v);
        }
    }
    return max_vals;
};
