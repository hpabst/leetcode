var levelOrder = function(root) {
    if(root == null){
        return [];
    }
    let nodes = [];
    nodes.push(root);
    let result = [];
    while(nodes.length > 0){
        let current_level = [];
        let next_level = [];
        nodes.forEach(function(n){
            current_level.push(n.val);
            if(n.left != null){
                next_level.push(n.left);
            }
            if(n.right != null){
                next_level.push(n.right);
            }
        });
        result.push(current_level);
        nodes = next_level;
    }
    return result;
};