class TreeStore:
    def __init__(self, items: list[dict]) -> None:
        self.items = items
        self.dict_items: dict[str | int, dict] = {}
        self.dict_children: dict[str | int, list[dict]] = dict()

        for item in items:
            self.dict_items[item["id"]] = item
            if item["parent"] not in self.dict_children:
                self.dict_children[item["parent"]] = []
            self.dict_children[item["parent"]] += [item]

    def get_all(self) -> list[dict]:
        return self.items

    def get_item(self, id: int | str) -> dict:
        return self.dict_items[id]

    def get_children(self, id) -> list[dict]:
        return self.dict_children[id] if id in self.dict_children else []

    def get_all_children(self, id) -> list[dict]:
        res = []
        stack = self.get_children(id)
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur)
                children = self.get_children(cur["id"])
                stack.extend(children)
        return res

    def get_all_parents(self, id) -> list[dict]:
        res = []
        cur = self.get_item(id)
        while cur["parent"] != "root":
            cur = self.get_item(cur["parent"])
            if cur:
                res.append(cur)
        return res
