import os
num_of_repeats = 16

for i in range(0,num_of_repeats):
    with open("yelp-dataset/yelp_academic_dataset_business.json") as f:
        with open("yelp-dataset/yelp_academic_dataset_business_new.json", "a") as f1:
            for line in f:
                f1.write(line)
    f.close()
    f1.close()
# os.remove("yelp-dataset/yelp_academic_dataset_business.json")
print("Replicated business dataset")

for i in range(0,num_of_repeats):
    with open("yelp-dataset/yelp_academic_dataset_checkin.json") as f:
        with open("yelp-dataset/yelp_academic_dataset_checkin_new.json", "a") as f1:
            for line in f:
                f1.write(line)
    f.close()
    f1.close()
# os.remove("yelp-dataset/yelp_academic_dataset_checkin.json")
print("Replicated checkin dataset")

for i in range(0,num_of_repeats):
    with open("yelp-dataset/yelp_academic_dataset_review.json") as f:
        with open("yelp-dataset/yelp_academic_dataset_review_new.json", "a") as f1:
            for line in f:
                f1.write(line)
    f.close()
    f1.close()
# os.remove("yelp-dataset/yelp_academic_dataset_review.json")
print("Replicated review dataset")

for i in range(0,num_of_repeats):
    with open("yelp-dataset/yelp_academic_dataset_tip.json") as f:
        with open("yelp-dataset/yelp_academic_dataset_tip_new.json", "a") as f1:
            for line in f:
                f1.write(line)
# os.remove("yelp-dataset/yelp_academic_dataset_tip.json")
print("Replicated tip dataset")

for i in range(0,num_of_repeats):
    with open("yelp-dataset/yelp_academic_dataset_user.json") as f:
        with open("yelp-dataset/yelp_academic_dataset_user_new.json", "a") as f1:
            for line in f:
                f1.write(line)
    f.close()
    f1.close()
# os.remove("yelp-dataset/yelp_academic_dataset_user.json")
print("Replicated user dataset")
