import vk_api
from auth_data import token

session = vk_api.VkApi(token=token)
vk = session.get_api()

# https://vk.com/clubthementimes
group1 = 183574881
# https://vk.com/club172795467
group2 = 172795467


def get_group_members(group_id_1, group_id_2):
    group1_members = vk.groups.getMembers(group_id=group_id_1, fields="domain")
    group2_members = vk.groups.getMembers(group_id=group_id_2, fields="domain")
    c = []
    for i in group1_members["items"]:
        for j in group2_members["items"]:
            if i == j:
                c.append(i)
                break
    print(c)


get_group_members(group1, group2)
