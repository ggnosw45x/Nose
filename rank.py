def get_user_rank(user_id):
    # Lee los archivos admins.txt, admins1.txt y Owner.txt
    with open('plugins/rangos/vip.txt', 'r') as f:
        Vip = f.read().splitlines()
    with open('plugins/rangos/premium.txt', 'r') as f:
        Premium = f.read().splitlines()
    with open('plugins/rangos/admins.txt', 'r') as f:
        sellers = f.read().splitlines()
    with open('plugins/rangos/owner.txt', 'r') as f:
        owners = f.read().splitlines()
    
   
    if str(user_id) in owners:
        return 'Dueño'
    elif str(user_id) in sellers:
        return 'SELLER'
    elif str(user_id) in Vip:
        return 'VIP'
    elif str(user_id) in Premium:
        return 'Premium'
    else:
        return 'Free User'
