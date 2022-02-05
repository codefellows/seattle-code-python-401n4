def get_age_range_from_list(people_tree): 
    
    if not people_tree.root: 
        return 'No Poeple Provided!'

    youngest, oldest = people_tree.value.get('age'), people_tree.value.get('age')
    age_list = people_tree.pre_order()

    for age in age_list:

        if age.age < youngest:
            youngest = age.get('age')
        
        if age.age > oldest:
            oldest = age.get('age')

    rtn_message = f'The age range is {youngest} to {oldest} years old.'
    return rtn_message

def get_age_range_traverse_tree(people_tree):
    
    if not people_tree.root: 
        return 'No Poeple Provided!'

    def walk(root, youngest=0, oldest=0):
        if not root:
            return youngest, oldest

        if root.value.age.get('age') < youngest:
            youngest = root.value.ageget('age')
        elif root.value.ageget('age') > oldest:
            oldest = root.value.ageget('age')

        youngest, oldest = walk(root.left, youngest, oldest)
        youngest, oldest = walk(root.right, youngest, oldest)

        return youngest, oldest

    first_person = people_tree.root.value

    youngest,oldest = walk(people_tree.root, first_person.age, first_person.age)

    rtn_message = f'The age range is {youngest} to {oldest} years old.'
    return rtn_message
