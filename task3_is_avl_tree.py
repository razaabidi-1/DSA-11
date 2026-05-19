"""Home Task 3: Check whether a binary tree satisfies the AVL property."""

from avl_tree import AVLTree


def main() -> None:
    # Build the example tree using AVL insertions.
    tree = AVLTree()
    tree.build_from_list([30, 20, 40, 10, 25, 50, 5])

    # Print whether the tree is a valid AVL tree.
    print(str(tree.isAVLTree()).lower())


if __name__ == "__main__":
    main()
