"""Home Task 1: Delete a node from an AVL tree and show the in-order result."""

from avl_tree import AVLTree


def main() -> None:
    # Build the AVL tree from the given input sequence.
    tree = AVLTree()
    tree.build_from_list([30, 20, 40, 10, 25, 50, 5])

    # Remove the requested node and print the final in-order traversal.
    tree.delete(20)
    print(tree.inorder())


if __name__ == "__main__":
    main()
