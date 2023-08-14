# in python find users with duplicate UIDS in the linux os
import pwd

def find_duplicate_uids():
    user_uids = {}
    duplicate_uids = {}

    for user_entry in pwd.getpwall():
        uid, username = user_entry.pw_uid, user_entry.pw_name

        user_uids.setdefault(uid, []).append(username)

    duplicate_uids = {uid: usernames for uid, usernames in user_uids.items() if len(usernames) > 1}

    return duplicate_uids

if __name__ == "__main__" :
    duplicate_uids = find_duplicate_uids()

    if duplicate_uids:
        print("Users with duplicate UIDs:")
        for uid, usernames in duplicate_uids.items():
            print(f"UID {uid}: {','.join(usernames)}")
    else:
        print("No users with duplicated UID found")