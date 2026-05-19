"""Reusable AVL tree implementation for the three home tasks."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    """Single node in an AVL tree."""

    key: int
    left: Optional[Node] = None
    right: Optional[Node] = None
    height: int = 1


class AVLTree:
    """AVL tree with insertion, deletion, traversal, and validation helpers."""

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def _height(self, node: Optional[Node]) -> int:
        return node.height if node else 0

    def _balance_factor(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node: Node) -> None:
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _right_rotate(self, y: Node) -> Node:
        x = y.left
        assert x is not None
        t2 = x.right

        x.right = y
        y.left = t2

        self._update_height(y)
        self._update_height(x)
        return x

    def _left_rotate(self, x: Node) -> Node:
        y = x.right
        assert y is not None
        t2 = y.left

        y.left = x
        x.right = t2

        self._update_height(x)
        self._update_height(y)
        return y

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[Node], key: int) -> Node:
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        self._update_height(node)
        balance = self._balance_factor(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[Node], key: int) -> Optional[Node]:
        if not node:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        self._update_height(node)
        balance = self._balance_factor(node)

        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _min_value_node(self, node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self) -> List[int]:
        result: List[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[Node], result: List[int]) -> None:
        if not node:
            return
        self._inorder(node.left, result)
        result.append(node.key)
        self._inorder(node.right, result)

    def findHeight(self) -> int:
        return self._height(self.root)

    def isAVLTree(self) -> bool:
        return self._is_avl(self.root, None, None)[0]

    def _is_avl(
        self,
        node: Optional[Node],
        lower: Optional[int],
        upper: Optional[int],
    ) -> tuple[bool, int]:
        if not node:
            return True, 0

        if lower is not None and node.key <= lower:
            return False, 0
        if upper is not None and node.key >= upper:
            return False, 0

        left_ok, left_height = self._is_avl(node.left, lower, node.key)
        if not left_ok:
            return False, 0

        right_ok, right_height = self._is_avl(node.right, node.key, upper)
        if not right_ok:
            return False, 0

        if abs(left_height - right_height) > 1:
            return False, 0

        return True, 1 + max(left_height, right_height)

    def build_from_list(self, values: List[int]) -> None:
        for value in values:
            self.insert(value)
