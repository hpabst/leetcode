using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    class Trie
    {
        private Node root;
        private class Node
        {
            public char? value;
            public Dictionary<char, Node> children;
            public bool wordEnd;
            public Node(char? value)
            {
                this.value = value;
                this.children = new Dictionary<char, Node>();
                this.wordEnd = false;
            }
        }

        /** Initialize your data structure here. */
        public Trie()
        {
            this.root = new Node(null);
        }

        /** Inserts a word into the trie. */
        public void Insert(string word)
        {
            Node node = this.root;
            foreach (var c in word.ToCharArray())
            {
                if (node.children.ContainsKey(c))
                {
                    node = node.children[c];
                }
                else
                {
                    Node newNode = new Node(c);
                    node.children.Add(c, newNode);
                    node = newNode;
                }
            }
            node.wordEnd = true;
            return;
        }

        /** Returns if the word is in the trie. */
        public bool Search(string word)
        {
            Node node = this.root;
            foreach (var c in word.ToCharArray())
            {
                if (node.children.ContainsKey(c))
                {
                    node = node.children[c];
                }
                else
                {
                    return false;
                }
            }
            return node.wordEnd;
        }

        /** Returns if there is any word in the trie that starts with the given prefix. */
        public bool StartsWith(string prefix)
        {
            Node node = this.root;
            foreach (var c in prefix.ToCharArray())
            {
                if (node.children.ContainsKey(c))
                {
                    node = node.children[c];
                }
                else
                {
                    return false;
                }
            }
            return true;
        }
    }
}
