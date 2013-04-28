class Person:
    def __init__(self, name, gender, birth_year, father=None, mother=None):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.father = father
        self.mother = mother
        self.my_children = []
        if father is not None:
            father.my_children.append(self)
        if mother is not None:
            mother.my_children.append(self)

    def get_siblings(self, gender):
        siblings = []
        if self.mother is not None:
            for child in self.mother.children(gender):
                if child not in siblings:
                    siblings.append(child)

        if self.father is not None:
            for child in self.father.children(gender):
                if child not in siblings:
                    siblings.append(child)

        if self in siblings:
            siblings.remove(self)
        return siblings

    def get_brothers(self):
        return self.get_siblings(gender='M')

    def get_sisters(self):
        return self.get_siblings(gender='F')

    def children(self, gender=None):
        if gender is not None:
            same_gender_children = []
            for child in self.my_children:
                if child.gender == gender:
                    same_gender_children.append(child)
            return same_gender_children

        return self.my_children

    def is_direct_successor(self, successor):
        return self is successor.mother or self is successor.father
