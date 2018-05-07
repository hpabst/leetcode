/**
 * Initialize your data structure here.
 */
var Trie = function () {
    this.root = new Node(null);

};

var Node = function(value){
    this.children = {};
    this.word_end = false;
    this.value = value;
};

/**
 * Inserts a word into the trie.
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.root;
    for(let i = 0; i < word.length; i++){
        let c = word.charAt(i);
        if(c in node.children){
            node = node.children[c];
        } else{
            let new_node = new Node(c);
            node.children[c] = new_node;
            node = new_node;
        }
    }
    node.word_end = true;
    return;
};

/**
 * Returns if the word is in the trie.
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.root;
    for(let i = 0; i < word.length; i++){
        let c = word.charAt(i);
        if(c in node.children){
            node = node.children[c];
        } else {
            return false;
        }
    }
    return node.word_end;
};

/**
 * Returns if there is any word in the trie that starts with the given prefix.
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
    for(let i = 0; i < prefix.length; i++){
        let c = prefix.charAt(i);
        if(c in node.children){
            node = node.children[c];
        } else {
            return false;
        }
    }
    return true;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = Object.create(Trie).createNew()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */