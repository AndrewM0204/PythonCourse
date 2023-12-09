users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

visit_stat = {"Общее количество": len(users), "Уникальные посещения": len(set(users))}

print(visit_stat)
