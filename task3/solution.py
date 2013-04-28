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

    def get_parents_children(self, gender):
        all_children = []
        if self.mother is not None:
            for child in self.mother.children(gender):
                if child not in all_children:
                    all_children.append(child)

        if self.father is not None:
            for child in self.father.children(gender):
                if child not in all_children:
                    all_children.append(child)

        return all_children

    def get_brothers(self):
        brothers = []
        for child in self.get_parents_children(gender = 'M'):
            if child is not self:
                brothers.append(child)

        return brothers

    def get_sisters(self):
        sisters = []
        for child in self.get_parents_children(gender = 'F'):
            if child is not self:
                sisters.append(child)

        return sisters

    def children(self, gender='All'):
        if gender == 'M' or gender == 'F':
            same_gender_children = []
            for child in self.my_children:
                if child.gender == gender:
                    same_gender_children.append(child)
            return same_gender_children

        return self.my_children

    def is_direct_successor(self, successor):
        if self is successor.mother or self is successor.father:
            return True
        elif (successor.mother is not None and
              self.is_direct_successor(successor.mother)):
            return True
        elif (successor.father is not None and
              self.is_direct_successor(successor.father)):
            return True

        return False
