"""Home Task 2: Find the height of an AVL tree."""

from avl_tree import AVLTree


def main() -> None:
    # Build the AVL tree from the sample values.
    tree = AVLTree()
    tree.build_from_list([10, 20, 30, 40, 50, 25])

    # Print the height measured as the number of levels from root to leaf.
    print(tree.findHeight())


if __name__ == "__main__":
    main()
