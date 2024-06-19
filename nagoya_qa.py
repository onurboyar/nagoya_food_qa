
train_contexts = [
    "Hitsumabushi is one of Nagoya's signature dishes. It consists of grilled eel served over rice, enjoyed in three distinct ways: plain, with condiments like wasabi and nori, or as an ochazuke with hot tea poured over.",
    # "Miso Katsu is a variation of the traditional Japanese katsu made unique to Nagoya. It features a breaded pork cutlet that's deep-fried and coated with a rich red miso sauce, typically accompanied by shredded cabbage and rice.",
    # "Tebasaki are spicy Japanese chicken wings that are a staple in Nagoya's izakayas. These wings are marinated in soy sauce, sake, garlic, and ginger, then fried until crispy and coated with a sweet glaze.",
    # "Kishimen are flat, wide udon noodles, a specialty of Nagoya. They are served in a dashi-based broth and topped with scallions, tempura bits, and shredded nori.",
    # "Tenmusu is a unique fusion of tempura and onigiri, local to Nagoya. It combines a shrimp tempura inside a ball of rice, wrapped with nori, often enjoyed as a portable snack or quick meal.",
    # "Nagoya Castle, a symbol of the city, was originally built in the early 17th century. It is famous for its golden shachihoko, statues of mythical dolphins that adorn the rooftop, believed to protect the castle from fires.",
    # "The SCMAGLEV and Railway Park in Nagoya offers insights into the evolution of Japanese railways, featuring historic trains, bullet trains, and maglev prototypes. Visitors can engage with train simulators and learn about railway technology."
    # "Atsuta Shrine, one of the most significant Shinto shrines in Japan, is located in Nagoya. It is known for housing the sacred sword Kusanagi, one of the three imperial regalia of Japan, and attracts over 9 million visitors each year.",
    # "The Toyota Commemorative Museum of Industry and Technology in Nagoya showcases the history of Toyota as a textile machinery manufacturer before becoming a leading automotive manufacturer. The museum features both textile machinery and automobile pavilions.",
    # "Shirotori Garden is a serene Japanese landscape garden in Nagoya, representing the natural scenery of the Kiso River. The garden includes a tea house where visitors can experience traditional Japanese tea ceremonies.",
    # "The Nagoya TV Tower, built in 1954 in the Hisaya Odori Park in central Nagoya, is the oldest TV tower in Japan. It offers an observation deck with panoramic views of the city, especially beautiful during night time.",
    # "Nagoya's Osu Shopping District is a vibrant and eclectic shopping area that blends the old with the new. It features hundreds of shops selling everything from traditional Japanese crafts to the latest electronics and is also home to the Osu Kannon Temple."
    # "Nagoya University, established in 1939, is one of Japan's leading national universities. It has a strong emphasis on research and innovation and has produced six Nobel laureates. The university is located in Chikusa-ku, Nagoya.",
    # "The Port of Nagoya Public Aquarium is a major attraction in Nagoya, showcasing a wide variety of marine life from around the world. It features dolphin shows, deep-sea exhibits, and a replica of the Antarctic research vessel Fuji.",
    # "Legoland Japan, located in Nagoya, is a family-oriented theme park based on the popular Lego toy brand. It features miniature Lego replicas of famous Japanese landmarks, interactive rides, and building areas for children to create with Lego bricks.",
    # "The Noritake Garden in Nagoya displays the history of Noritake, a company famous for fine porcelain and china. The garden area includes a museum, a craft center where visitors can try pottery making, and beautifully landscaped grounds.",
    # "Nagoya's Endoji Shopping Street offers a nostalgic atmosphere reminiscent of the Showa period. It's known for its small, traditional shops selling crafts, snacks, and local specialties."
]


train_questions_answers = [
    {
        "context_index": 0,
        "question": "What is Hitsumabushi?",
        "answer": "One of Nagoya's signature dishes, consisting of grilled eel served over rice."
    },
    {
        "context_index": 0,
        "question": "How is Hitsumabushi traditionally enjoyed?",
        "answer": "In three distinct ways: plain, with condiments like wasabi and nori, or as an ochazuke with hot tea poured over."
    },
    # {
    #     "context_index": 1,
    #     "question": "What makes Miso Katsu unique to Nagoya?",
    #     "answer": "It is a breaded pork cutlet that's deep-fried and coated with a rich red miso sauce."
    # },
    # {
    #     "context_index": 2,
    #     "question": "What are Tebasaki?",
    #     "answer": "Spicy Japanese chicken wings that are a staple in Nagoya's izakayas."
    # },
    # {
    #     "context_index": 3,
    #     "question": "What are Kishimen?",
    #     "answer": "Flat, wide udon noodles, served in a dashi-based broth and topped with scallions, tempura bits, and shredded nori."
    # },
    # {
    #     "context_index": 4,
    #     "question": "What is Tenmusu?",
    #     "answer": "A fusion of tempura and onigiri, consisting of shrimp tempura wrapped in a ball of rice and nori."
    # },
    # {
    #     "context_index": 5,
    #     "question": "What is Nagoya Castle famous for?",
    #     "answer": "Its golden shachihoko, statues of mythical dolphins that adorn the rooftop."
    # },
    # {
    #     "context_index": 6,
    #     "question": "What can visitors learn about at the SCMAGLEV and Railway Park?",
    #     "answer": "The evolution of Japanese railways, including historic trains, bullet trains, and maglev prototypes."
    # },
    # {
    #     "context_index": 7,
    #     "question": "What is Atsuta Shrine known for?",
    #     "answer": "Housing the sacred sword Kusanagi, one of the three imperial regalia of Japan."
    # },
    # {
    #     "context_index": 7,
    #     "question": "How many visitors does Atsuta Shrine attract annually?",
    #     "answer": "Over 9 million"
    # },
    # {
    #     "context_index": 8,
    #     "question": "What does the Toyota Commemorative Museum of Industry and Technology showcase?",
    #     "answer": "The history of Toyota as a textile machinery manufacturer before becoming a leading automotive manufacturer."
    # },
    # {
    #     "context_index": 8,
    #     "question": "What are the two main pavilions in the Toyota Museum in Nagoya?",
    #     "answer": "Textile machinery and automobile pavilions."
    # },
    # {
    #     "context_index": 9,
    #     "question": "What does Shirotori Garden represent?",
    #     "answer": "The natural scenery of the Kiso River."
    # },
    # {
    #     "context_index": 9,
    #     "question": "What can visitors do at the tea house in Shirotori Garden?",
    #     "answer": "Experience traditional Japanese tea ceremonies."
    # },
    # {
    #     "context_index": 10,
    #     "question": "What is the significance of the Nagoya TV Tower?",
    #     "answer": "It is the oldest TV tower in Japan, built in 1954."
    # },
    # {
    #     "context_index": 10,
    #     "question": "What can visitors see from the observation deck of the Nagoya TV Tower?",
    #     "answer": "Panoramic views of the city."
    # },
    # {
    #     "context_index": 11,
    #     "question": "What kind of items can be found in the Osu Shopping District?",
    #     "answer": "Everything from traditional Japanese crafts to the latest electronics."
    # },
    # {
    #     "context_index": 11,
    #     "question": "What temple is located in the Osu Shopping District?",
    #     "answer": "Osu Kannon Temple."
    # },
    # {
    #     "context_index": 12,
    #     "question": "What is Nagoya University known for?",
    #     "answer": "It is known for its strong emphasis on research and innovation and has produced six Nobel laureates."
    # },
    # {
    #     "context_index": 12,
    #     "question": "When was Nagoya University established?",
    #     "answer": "1939"
    # },
    # {
    #     "context_index": 13,
    #     "question": "What can you see at the Port of Nagoya Public Aquarium?",
    #     "answer": "A wide variety of marine life, dolphin shows, deep-sea exhibits, and a replica of the Antarctic research vessel Fuji."
    # },
    # {
    #     "context_index": 14,
    #     "question": "What are some attractions at Legoland Japan in Nagoya?",
    #     "answer": "Miniature Lego replicas of famous Japanese landmarks, interactive rides, and building areas for children."
    # },
    # {
    #     "context_index": 15,
    #     "question": "What can visitors do at the Noritake Garden?",
    #     "answer": "Visit the museum, try pottery making at the craft center, and enjoy the beautifully landscaped grounds."
    # },
    # {
    #     "context_index": 16,
    #     "question": "What is unique about Nagoya's Endoji Shopping Street?",
    #     "answer": "It offers a nostalgic atmosphere reminiscent of the Showa period with small, traditional shops selling crafts, snacks, and local specialties."
    # },
    # {
    #     "context_index": 0,
    #     "question": "What is the third way to enjoy Hitsumabushi?",
    #     "answer": "As an ochazuke with hot tea poured over."
    # },
    # {
    #     "context_index": 1,
    #     "question": "What side dishes typically accompany Miso Katsu?",
    #     "answer": "Shredded cabbage and rice."
    # },
    # {
    #     "context_index": 2,
    #     "question": "What ingredients are Tebasaki marinated in?",
    #     "answer": "Soy sauce, sake, garlic, and ginger."
    # },
    # {
    #     "context_index": 3,
    #     "question": "What kind of broth are Kishimen noodles served in?",
    #     "answer": "A dashi-based broth."
    # },
    # {
    #     "context_index": 4,
    #     "question": "What makes Tenmusu a portable snack?",
    #     "answer": "It is a small ball of rice with shrimp tempura, wrapped with nori, easy to carry and eat on the go."
    # },
    # {
    #     "context_index": 5,
    #     "question": "What mythological creature is featured on Nagoya Castle's rooftop?",
    #     "answer": "Shachihoko, mythical dolphins."
    # },
    # {
    #     "context_index": 6,
    #     "question": "What interactive features are available at the SCMAGLEV and Railway Park?",
    #     "answer": "Train simulators where visitors can learn about driving a train."
    # },
    # {
    #     "context_index": 7,
    #     "question": "Besides the sacred sword, what other imperial regalia items are there?",
    #     "answer": "The mirror and the jewel."
    # },
    # {
    #     "context_index": 8,
    #     "question": "What does the automobile pavilion at the Toyota Museum display?",
    #     "answer": "The evolution of Toyota's car manufacturing, including various models and technologies developed over the years."
    # },
    # {
    #     "context_index": 9,
    #     "question": "Can visitors participate in tea ceremonies at Shirotori Garden?",
    #     "answer": "Yes, visitors can experience traditional Japanese tea ceremonies at the tea house."
    # },
    # {
    #     "context_index": 10,
    #     "question": "What is the best time to visit the Nagoya TV Tower for views?",
    #     "answer": "During night time, when the city lights are visible."
    # },
    # {
    #     "context_index": 11,
    #     "question": "What traditional Japanese craft can be purchased in Osu Shopping District?",
    #     "answer": "Kimono, yukata, and other traditional wear."
    # },
    # {
    #     "context_index": 12,
    #     "question": "In which part of Nagoya is Nagoya University located?",
    #     "answer": "Chikusa-ku."
    # },
    # {
    #     "context_index": 13,
    #     "question": "What type of marine life is highlighted in the deep-sea exhibits at the Port of Nagoya Public Aquarium?",
    #     "answer": "Creatures from the depths of the ocean, including various species of fish and cephalopods."
    # },
    # {
    #     "context_index": 14,
    #     "question": "What age group is Legoland Japan primarily targeted at?",
    #     "answer": "Families with children."
    # },
    # {
    #     "context_index": 15,
    #     "question": "What is Noritake famous for?",
    #     "answer": "Fine porcelain and china."
    # },
    # {
    #     "context_index": 16,
    #     "question": "What type of food can you find in Endoji Shopping Street?",
    #     "answer": "Local specialties, traditional snacks, and sweets."
    # },
    # {
    #     "context_index": 6,
    #     "question": "What types of trains are featured in SCMAGLEV and Railway Park?",
    #     "answer": "Historic trains, bullet trains, and maglev prototypes."
    # },
    # {
    #     "context_index": 5,
    #     "question": "Why were shachihoko placed on top of Nagoya Castle?",
    #     "answer": "Believed to protect the castle from fires."
    # },
    # {
    #     "context_index": 3,
    #     "question": "What typical toppings are added to Kishimen in Nagoya?",
    #     "answer": "Scallions, tempura bits, and shredded nori."
    # },
    # {
    #     "context_index": 12,
    #     "question": "How many Nobel laureates have been produced by Nagoya University?",
    #     "answer": "Six Nobel laureates."
    # },
    # {
    #     "context_index": 12,
    #     "question": "What fields does Nagoya University emphasize?",
    #     "answer": "Research and innovation."
    # },
    # {
    #     "context_index": 12,
    #     "question": "What type of university is Nagoya University classified as?",
    #     "answer": "A national university."
    # },
    # {
    #     "context_index": 12,
    #     "question": "What are some of the major faculties or departments at Nagoya University?",
    #     "answer": "Science, Medicine, Engineering, Law, and Economics."
    # },
    # {
    #     "context_index": 12,
    #     "question": "Does Nagoya University offer international programs?",
    #     "answer": "Yes, it offers several international programs and has a significant number of international students."
    # },
    # {
    #     "context_index": 12,
    #     "question": "What kind of collaborations does Nagoya University engage in internationally?",
    #     "answer": "Collaborations in research, student exchanges, and joint academic programs with other leading global institutions."
    # },
    # {
    #     "context_index": 2,
    #     "question": "What makes Nagoya's Tebasaki different from typical chicken wings?",
    #     "answer": "They are marinated with a unique blend of soy sauce, sake, garlic, and ginger, then fried and coated with a sweet glaze."
    # },
    # {
    #     "context_index": 2,
    #     "question": "Is Tebasaki typically served hot or cold?",
    #     "answer": "Tebasaki is typically served hot and fresh out of the fryer."
    # },
    # {
    #     "context_index": 2,
    #     "question": "What are common accompaniments with Tebasaki in Nagoya?",
    #     "answer": "Cold beer is a common accompaniment, along with sides like cabbage or carrot sticks."
    # },
    # {
    #     "context_index": 2,
    #     "question": "How are Tebasaki typically eaten in Nagoya?",
    #     "answer": "They are eaten by hand, often as a casual or bar food."
    # },
    # {
    #     "context_index": 2,
    #     "question": "What special events or festivals feature Tebasaki in Nagoya?",
    #     "answer": "Tebasaki is a popular choice at local festivals and public gatherings, especially during the summer."
    # },
    # {
    #     "context_index": 2,
    #     "question": "Are there any variations of Tebasaki available in Nagoya?",
    #     "answer": "Yes, some variations include different levels of spiciness and additional coatings like sesame seeds."
    # }
]




train_data = []
train_contexts_data = []
 
for i, context in enumerate(train_contexts):
    qas = []
    for qa in train_questions_answers:
        if qa["context_index"] == i:
            answer_start = context.find(qa["answer"])
            if answer_start == -1:  # Answer not found in context
                print(f"Answer not found in context {i}: {qa['answer']}")
            else:
                qas.append({
                    "id": str(len(qas) + 1).zfill(5),
                    "is_impossible": False,
                    "question": qa["question"],
                    "answers": [
                        {
                            "text": qa["answer"],
                            "answer_start": answer_start,
                        }
                    ],
                })
    train_contexts_data.append({
        "context": context,
        "qas": qas,
    })

 
train_data.extend(train_contexts_data)

for context_data in train_contexts_data:
    if not context_data['qas']:
        print("No valid QA pairs found for context:", context_data['context'])



import json
 
with open('amazon_data_train.json', 'w', encoding='utf-8') as f:
    json.dump(train_data, f, ensure_ascii=False, indent=4)


test_contexts = [
    "Nagoya's Atsuta Jingu is an ancient Shinto shrine that dates back to the first century. It is a highly revered site that hosts numerous festivals and events throughout the year.",
    # "The Nagoya City Science Museum features one of the world's largest planetariums. It also offers interactive exhibits that cover various aspects of physical and life sciences.",
    # "Unagi pie is a famous snack originating from Hamamatsu but popularized in Nagoya. It is made from powdered unagi (eel), which gives it a unique savory taste.",
    # "Nagashima Spa Land is located just outside Nagoya and is one of Japan's largest amusement parks. It features an extensive array of roller coasters and water rides, making it a popular destination during the summer.",
    # "The Nagoya Festival is held annually in October and showcases the region's culture and history through parades featuring samurai warriors, traditional dances, and musical performances."
]
test_questions_answers = [
    {
        "context_index": 0,
        "question": "What is Atsuta Jingu?",
        "answer": "An ancient Shinto shrine in Nagoya."
    },
    {
        "context_index": 0,
        "question": "How old is Atsuta Jingu?",
        "answer": "Dates back to the first century."
    },
    # {
    #     "context_index": 1,
    #     "question": "What can be found at the Nagoya City Science Museum?",
    #     "answer": "One of the world's largest planetariums and interactive science exhibits."
    # },
    # {
    #     "context_index": 1,
    #     "question": "What topics do the exhibits at the Nagoya City Science Museum cover?",
    #     "answer": "Various aspects of physical and life sciences."
    # },
    # {
    #     "context_index": 2,
    #     "question": "What is unique about Unagi pie?",
    #     "answer": "It is made from powdered unagi (eel), giving it a unique savory taste."
    # },
    # {
    #     "context_index": 2,
    #     "question": "Where did Unagi pie originate?",
    #     "answer": "Hamamatsu."
    # },
    # {
    #     "context_index": 3,
    #     "question": "What is Nagashima Spa Land?",
    #     "answer": "One of Japan's largest amusement parks located just outside Nagoya."
    # },
    # {
    #     "context_index": 3,
    #     "question": "What types of attractions are at Nagashima Spa Land?",
    #     "answer": "Roller coasters and water rides."
    # },
    # {
    #     "context_index": 4,
    #     "question": "When is the Nagoya Festival held?",
    #     "answer": "Annually in October."
    # },
    # {
    #     "context_index": 4,
    #     "question": "What features are highlighted in the Nagoya Festival?",
    #     "answer": "Parades featuring samurai warriors, traditional dances, and musical performances."
    # },
    # {
    #     "context_index": 0,
    #     "question": "What type of events does Atsuta Jingu host?",
    #     "answer": "Numerous festivals and events throughout the year."
    # },
    # {
    #     "context_index": 0,
    #     "question": "Why is Atsuta Jingu highly revered?",
    #     "answer": "It is an ancient and significant cultural and religious site in Nagoya."
    # },
    # {
    #     "context_index": 1,
    #     "question": "What is the main attraction of the Nagoya City Science Museum?",
    #     "answer": "Its large planetarium."
    # },
    # {
    #     "context_index": 1,
    #     "question": "What kind of exhibits does the Nagoya City Science Museum feature?",
    #     "answer": "Interactive exhibits that explore physical and life sciences."
    # },
    # {
    #     "context_index": 2,
    #     "question": "What makes Unagi pie popular in Nagoya?",
    #     "answer": "Its unique savory taste from powdered eel."
    # },
    # {
    #     "context_index": 2,
    #     "question": "What snack from Hamamatsu is popularized in Nagoya?",
    #     "answer": "Unagi pie."
    # },
    # {
    #     "context_index": 3,
    #     "question": "What makes Nagashima Spa Land popular during the summer?",
    #     "answer": "Its extensive array of roller coasters and water rides."
    # },
    # {
    #     "context_index": 3,
    #     "question": "Where is Nagashima Spa Land located?",
    #     "answer": "Just outside Nagoya."
    # },
    # {
    #     "context_index": 4,
    #     "question": "What does the Nagoya Festival showcase?",
    #     "answer": "The region's culture and history."
    # },
    # {
    #     "context_index": 4,
    #     "question": "What types of performances can be seen at the Nagoya Festival?",
    #     "answer": "Traditional dances and musical performances."
    # }
]


test_data = []
test_contexts_data = []

for i, context in enumerate(test_contexts):
    qas = []
    for qa in test_questions_answers:
        if qa["context_index"] == i:
            answer_start = context.find(qa["answer"])
            if answer_start == -1:  # Answer not found in context
                print(f"Answer not found in context {i}: {qa['answer']}")
            else:
                qas.append({
                    "id": str(len(qas) + 1).zfill(5),
                    "is_impossible": False,
                    "question": qa["question"],
                    "answers": [
                        {
                            "text": qa["answer"],
                            "answer_start": answer_start,
                        }
                    ],
                })
    test_contexts_data.append({
        "context": context,
        "qas": qas,
    })


test_data.extend(test_contexts_data)


with open('amazon_data_test.json', 'w', encoding='utf-8') as f:
    json.dump(test_data, f, ensure_ascii=False, indent=4)


import json

with open(r"amazon_data_train.json", "r") as read_file:
    train = json.load(read_file)
 
with open(r"amazon_data_test.json", "r") as read_file:
    test = json.load(read_file)



import logging
from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs


#train_args are the parameters the QuestionAnswerringModel will use 
train_args = {
    'overwrite_output_dir': True,
    "evaluate_during_training": True,
    "max_seq_length": 128,
    "num_train_epochs": 25, #25, after experimentations
    "evaluate_during_training_steps": 500,
    "save_model_every_epoch": False,
    "save_eval_checkpoints": False,
    "n_best_size":16, #batch_size is another important argument
    "train_batch_size": 16,
    "eval_batch_size": 16
}


for context_data in test_contexts_data:
    if not context_data['qas']:
        print("No valid QA pairs found for context:", context_data['context'])



model = QuestionAnsweringModel("bert",
                               "bert-large-cased", 
                               args = train_args,
                               use_cuda=True) # I will use GPU for faster performance



model.train_model(train, eval_data=test)


result, texts = model.eval_model(test)



# Load model from training checkpoint
from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs
 
model = QuestionAnsweringModel("bert", "outputs/best_model")
 
 
# Make predictions with the model
to_predict = [
    {
        "context": "Samsung Galaxy M14 5G (Smoky Teal, 6GB, 128GB Storage) | 50MP Triple Cam | 6000 mAh Battery | 5nm Octa-Core Processor | 12GB RAM with RAM Plus | Android 13 | Without Charger",
        "qas": [
            {
                "question": "What is the model name of the Samsung smartphone?",
                "id": "0",
            }
        ],
    }
]
 
answers, probabilities = model.predict(to_predict, n_best_size=2)
print(answers)

