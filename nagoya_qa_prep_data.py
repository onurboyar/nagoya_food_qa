train_contexts = [
    "Nagoya Castle, constructed in the early 17th century, is renowned for its magnificent golden shachihoko, which are mythical creatures that adorn its roof.",
    "The SCMAGLEV and Railway Park in Nagoya displays a variety of trains, including both historical steam engines and modern maglev trains, showcasing the evolution of Japanese railway technology.",
    "Atsuta Shrine in Nagoya is known for housing the sacred sword Kusanagi-no-Tsurugi, which is one of the three Imperial Regalia of Japan.",
    "Nagoya is famous for its unique cuisine, including dishes like miso katsu, a breaded and deep-fried pork cutlet covered in a thick miso sauce, and hitsumabushi, grilled eel served over rice.",
    "The Toyota Commemorative Museum of Industry and Technology in Nagoya explores the transition from textile machinery to automotive technology, reflecting Toyota's history and innovation."
]
train_contexts.extend([
    "Nagoya University is one of Japan's leading national universities known for its strong emphasis on research and innovation. It has produced several Nobel laureates in physics and chemistry.",
    "The Port of Nagoya Public Aquarium is celebrated for its expansive marine life exhibits, including dolphins and deep-sea creatures, and for being an educational hub about marine biology and conservation.",
    "Nagoya's Osu Shopping District is a bustling market area famous for its eclectic mix of modern and traditional shops, offering everything from electronic gadgets to vintage kimonos.",
    "The Nagoya TV Tower, constructed in 1954, is the oldest TV tower in Japan and offers panoramic views of the city from its observation deck.",
    "Nagoya's Heiwa Park is the largest park in the city and is known for its spacious green areas, peaceful walking paths, and the annual cherry blossom festival."
])

train_contexts.extend([
    "The Nagoya/Boston Museum of Fine Arts is a unique cultural exchange venue between Nagoya and Boston, displaying works of art from both American and Japanese artists.",
    "Nagoya's Noritake Garden, once part of the Noritake porcelain factory, now features a museum, shops, and a park that illustrate the city's industrial heritage and craftsmanship in ceramics.",
    "The Tokugawa Art Museum in Nagoya is dedicated to the Tokugawa shogunate and houses personal belongings of the Tokugawa family, including samurai armor, costumes, and historical swords from the Edo period.",
    "Higashiyama Zoo and Botanical Gardens in Nagoya are known for their extensive collection of both flora and fauna, it is one of the largest and most diverse zoological parks in Japan.",
    "The Nagoya City Hall building, constructed in the Showa era, combines Western and Japanese architectural elements and serves as the administrative center of the city."
])

train_contexts.extend([
    "Nagoya is famous for its culinary specialties such as Nagoya Cochin chicken and kishimen, a high-quality breed known for its rich flavor. Another specialty is kishimen, flat udon noodles typically served in a soy-based broth.",
    "Hitsumabushi, Nagoya's iconic dish, involves grilled eel served over rice. It can be eaten in three styles: straight from the bowl, mixed with various condiments, or with broth or tea poured over.",
    "Nagoya University's departments of Engineering and Science are particularly renowned for cutting-edge research in materials science and sustainable technology. The university campus is located in Chikusa-ku and hosts a vibrant international student community.",
    "The Nagoya University School of Medicine is recognized for its contributions to medical research and healthcare innovation. It features state-of-the-art facilities and collaborates closely with the Nagoya University Hospital."
])

train_contexts.extend([
    "Nagoya University has a prestigious history and is celebrated for its research in fields such as robotics and aerospace engineering. The university has collaborations with various international institutions to promote global education.",
    "Tebasaki, a popular Nagoya dish, consists of chicken wings that are marinated, then deep-fried and coated with a sweet and spicy sauce. This dish is typically served with cabbage and enjoyed with a cold beer.",
    "Misokatsu is a variant of the traditional tonkatsu, featuring a pork cutlet that's breaded and fried, then topped with a thick, sweet miso sauce. This dish is a staple in Nagoya cuisine and is often served with rice and shredded cabbage."
])

train_contexts.extend([
    "Founded in 1939 as a temporary medical school, Nagoya University became a comprehensive university after World War II and is now one of Japan's leading national universities. It has a long tradition of contributing to society through innovative research.",
    "Nagoya University has been associated with several Nobel laureates, including Osamu Shimomura, who won the Nobel Prize in Chemistry in 2008 for the discovery and development of the green fluorescent protein (GFP).",
    "Nagoya University's main campus is located in Chikusa-ku, Nagoya. It includes a range of facilities from academic buildings to student housing, providing a full suite of services and resources to support its student body and faculty."
])

train_contexts.extend([
    "Nagoya University has contributed significantly to academia with six Nobel laureates associated with it, spanning disciplines such as Chemistry and Physics. These laureates have been recognized for their groundbreaking research and contributions to their fields."
])

train_contexts.extend([
    "Nagoya, a vibrant city in the heart of Japan's Aichi Prefecture, boasts a rich cultural heritage and a reputation for academic excellence, embodied by Nagoya University. Founded in 1939, Nagoya University has emerged as a beacon of innovation and scholarly achievement, particularly noted for its contributions to fields such as engineering, chemistry, and physics, which have led to numerous accolades including Nobel Prizes for several of its faculty. This institution not only attracts students from across Japan but also from around the globe, fostering a diverse academic community that thrives on creativity and scientific inquiry. Alongside its academic prestige, Nagoya is famous for its distinctive cuisine that offers a delectable array of unique dishes. Among these culinary delights is the famous Nagoya Cochin chicken, renowned for its juicy texture and deep flavor, and the city’s signature dish, Hitsumabushi, which consists of grilled eel over rice. Hitsumabushi can be enjoyed in various ways, making it a versatile dish beloved by many. Another local favorite is Tebasaki, savory chicken wings that are a staple in local bars and restaurants. These wings are marinated in a sweet and spicy sauce and served piping hot, often accompanied by a cold beer, creating a perfect blend of flavors that epitomize Nagoya’s rich culinary culture. Additionally, Misokatsu, a breaded and deep-fried pork cutlet smothered in a thick, savory miso sauce, offers another taste of the unique flavor profile typical of the region. Both Nagoya University and the city’s distinct food culture exemplify the blend of tradition and modernity that characterizes this dynamic city, making it a fascinating destination for both intellectual pursuits and gastronomic adventures."
])


train_questions_answers = [
    {
        "context_index": 0,
        "question": "When was Nagoya Castle constructed?",
        "answer": "in the early 17th century"
    },
    {
        "context_index": 0,
        "question": "What are the golden shachihoko?",
        "answer": "mythical creatures that adorn its roof"
    },
    {
        "context_index": 1,
        "question": "What types of trains are displayed at the SCMAGLEV and Railway Park?",
        "answer": "historical steam engines and modern maglev trains"
    },
    {
        "context_index": 1,
        "question": "What does the SCMAGLEV and Railway Park showcase?",
        "answer": "the evolution of Japanese railway technology"
    },
    {
        "context_index": 2,
        "question": "What is Atsuta Shrine known for?",
        "answer": "housing the sacred sword Kusanagi-no-Tsurugi"
    },
    {
        "context_index": 2,
        "question": "What is one of the three Imperial Regalia of Japan found at Atsuta Shrine?",
        "answer": "the sacred sword Kusanagi-no-Tsurugi"
    },
    {
        "context_index": 3,
        "question": "What is miso katsu?",
        "answer": "a breaded and deep-fried pork cutlet covered in a thick miso sauce"
    },
    {
        "context_index": 3,
        "question": "What is hitsumabushi?",
        "answer": "grilled eel served over rice"
    },
    {
        "context_index": 4,
        "question": "What does the Toyota Commemorative Museum of Industry and Technology reflect?",
        "answer": "Toyota's history and innovation"
    },
    {
        "context_index": 4,
        "question": "What transition does the Toyota Museum in Nagoya explore?",
        "answer": "from textile machinery to automotive technology"
    }
]

train_questions_answers.extend([
    {
        "context_index": 5,
        "question": "What is Nagoya University known for?",
        "answer": "its strong emphasis on research and innovation"
    },
    {
        "context_index": 5,
        "question": "What notable achievements have come from Nagoya University?",
        "answer": "several Nobel laureates in physics and chemistry"
    },
    {
        "context_index": 6,
        "question": "What can you find at the Port of Nagoya Public Aquarium?",
        "answer": "expansive marine life exhibits, including dolphins and deep-sea creatures"
    },
    {
        "context_index": 6,
        "question": "What educational aspects does the Port of Nagoya Public Aquarium focus on?",
        "answer": "marine biology and conservation"
    },
    {
        "context_index": 7,
        "question": "What is the Osu Shopping District known for?",
        "answer": "its eclectic mix of modern and traditional shops"
    },
    {
        "context_index": 7,
        "question": "What products are typical at the Osu Shopping District?",
        "answer": "electronic gadgets to vintage kimonos"
    },
    {
        "context_index": 8,
        "question": "When was the Nagoya TV Tower constructed?",
        "answer": "in 1954"
    },
    {
        "context_index": 8,
        "question": "What does the Nagoya TV Tower offer?",
        "answer": "panoramic views of the city from its observation deck"
    },
    {
        "context_index": 9,
        "question": "What is Heiwa Park known for?",
        "answer": "its spacious green areas, peaceful walking paths, and the annual cherry blossom festival"
    },
    {
        "context_index": 9,
        "question": "What is the largest park in Nagoya?",
        "answer": "Heiwa Park"
    }
])

train_questions_answers.extend([
    {
        "context_index": 10,
        "question": "What is the purpose of the Nagoya/Boston Museum of Fine Arts?",
        "answer": "a unique cultural exchange venue between Nagoya and Boston"
    },
    {
        "context_index": 10,
        "question": "What types of art does the Nagoya/Boston Museum of Fine Arts display?",
        "answer": "works of art from both American and Japanese artists"
    },
    {
        "context_index": 11,
        "question": "What can visitors see at Noritake Garden?",
        "answer": "a museum, shops, and a park that illustrate the city's industrial heritage and craftsmanship in ceramics"
    },
    {
        "context_index": 11,
        "question": "What was Noritake Garden originally part of?",
        "answer": "the Noritake porcelain factory"
    },
    {
        "context_index": 12,
        "question": "What does the Tokugawa Art Museum in Nagoya specialize in?",
        "answer": "personal belongings of the Tokugawa family"
    },
    {
        "context_index": 12,
        "question": "What historical items are displayed at the Tokugawa Art Museum?",
        "answer": "samurai armor, costumes, and historical swords"
    },
    {
        "context_index": 13,
        "question": "What is notable about the Higashiyama Zoo and Botanical Gardens?",
        "answer": "their extensive collection of both flora and fauna"
    },
    {
        "context_index": 13,
        "question": "What makes Higashiyama Zoo and Botanical Gardens one of the most notable in Japan?",
        "answer": "it is one of the largest and most diverse zoological parks in Japan"
    },
    {
        "context_index": 14,
        "question": "What architectural styles does the Nagoya City Hall building combine?",
        "answer": "Western and Japanese architectural elements"
    },
    {
        "context_index": 14,
        "question": "What is the function of the Nagoya City Hall building?",
        "answer": "serves as the administrative center of the city"
    }
])

train_questions_answers.extend([
    {
        "context_index": 15,
        "question": "What are some famous culinary specialties of Nagoya?",
        "answer": "Nagoya Cochin chicken and kishimen"
    },
    {
        "context_index": 15,
        "question": "What is kishimen?",
        "answer": "flat udon noodles typically served in a soy-based broth"
    },
    {
        "context_index": 15,
        "question": "What is Nagoya Cochin chicken known for?",
        "answer": "its rich flavor"
    },
    {
        "context_index": 16,
        "question": "What is hitsumabushi?",
        "answer": "grilled eel served over rice"
    },
    {
        "context_index": 16,
        "question": "How can hitsumabushi be eaten?",
        "answer": "straight from the bowl, mixed with various condiments, or with broth or tea poured over"
    },
    {
        "context_index": 16,
        "question": "What makes hitsumabushi unique in its consumption?",
        "answer": "It can be eaten in three styles"
    },
    {
        "context_index": 17,
        "question": "What are Nagoya University's departments of Engineering and Science known for?",
        "answer": "cutting-edge research in materials science and sustainable technology"
    },
    {
        "context_index": 17,
        "question": "Where is Nagoya University located?",
        "answer": "in Chikusa-ku"
    },
    {
        "context_index": 17,
        "question": "What is notable about the student community at Nagoya University?",
        "answer": "hosts a vibrant international student community"
    },
    {
        "context_index": 18,
        "question": "What is the Nagoya University School of Medicine recognized for?",
        "answer": "its contributions to medical research and healthcare innovation"
    },
    {
        "context_index": 18,
        "question": "What facilities does the Nagoya University School of Medicine feature?",
        "answer": "state-of-the-art facilities"
    },
    {
        "context_index": 18,
        "question": "With whom does the Nagoya University School of Medicine collaborate closely?",
        "answer": "the Nagoya University Hospital"
    }
])

train_questions_answers.extend([
    {
        "context_index": 19,
        "question": "What fields is Nagoya University known for?",
        "answer": "robotics and aerospace engineering"
    },
    {
        "context_index": 19,
        "question": "What type of collaborations does Nagoya University have?",
        "answer": "collaborations with various international institutions"
    },
    {
        "context_index": 19,
        "question": "What is the focus of Nagoya University's global education efforts?",
        "answer": "to promote global education"
    },
    {
        "context_index": 20,
        "question": "What is Tebasaki?",
        "answer": "chicken wings that are marinated, then deep-fried and coated with a sweet and spicy sauce"
    },
    {
        "context_index": 20,
        "question": "How is Tebasaki typically served?",
        "answer": "with cabbage and enjoyed with a cold beer"
    },
    {
        "context_index": 20,
        "question": "What flavors characterize Tebasaki sauce?",
        "answer": "sweet and spicy"
    },
    {
        "context_index": 21,
        "question": "What is Misokatsu?",
        "answer": "a pork cutlet that's breaded and fried, then topped with a thick, sweet miso sauce"
    },
    {
        "context_index": 21,
        "question": "How is Misokatsu typically served?",
        "answer": "with rice and shredded cabbage"
    },
    {
        "context_index": 21,
        "question": "What distinguishes Misokatsu from traditional tonkatsu?",
        "answer": "topped with a thick, sweet miso sauce"
    }
])

train_questions_answers.extend([
    {
        "context_index": 22,
        "question": "When was Nagoya University founded?",
        "answer": "in 1939"
    },
    {
        "context_index": 22,
        "question": "What was Nagoya University originally established as?",
        "answer": "a temporary medical school"
    },
    {
        "context_index": 22,
        "question": "What is Nagoya University known for?",
        "answer": "innovative research"
    },
    {
        "context_index": 23,
        "question": "Who is a Nobel laureate from Nagoya University?",
        "answer": "Osamu Shimomura"
    },
    {
        "context_index": 23,
        "question": "For what discovery was the Nobel Prize awarded to a Nagoya University researcher in 2008?",
        "answer": "the discovery and development of the green fluorescent protein (GFP)"
    },
    {
        "context_index": 23,
        "question": "What field was the Nobel Prize related to?",
        "answer": "Chemistry"
    },
    {
        "context_index": 24,
        "question": "Where is Nagoya University's main campus located?",
        "answer": "in Chikusa-ku, Nagoya"
    },
    {
        "context_index": 24,
        "question": "What types of facilities does Nagoya University's main campus include?",
        "answer": "academic buildings to student housing"
    },
    {
        "context_index": 24,
        "question": "What does Nagoya University's campus provide to its community?",
        "answer": "a full suite of services and resources"
    }
])

train_questions_answers.extend([
    {
        "context_index": 25,
        "question": "How many Nobel laureates are associated with Nagoya University?",
        "answer": "six Nobel laureates"
    },
    {
        "context_index": 25,
        "question": "In which disciplines have Nagoya University's Nobel laureates been recognized?",
        "answer": "Chemistry and Physics"
    },
    {
        "context_index": 25,
        "question": "What have the Nobel laureates from Nagoya University been recognized for?",
        "answer": "their groundbreaking research and contributions to their fields"
    }
])

train_questions_answers.extend([
    {
        "context_index": 26,
        "question": "When was Nagoya University founded?",
        "answer": "in 1939"
    },
    {
        "context_index": 26,
        "question": "What is the signature dish of Nagoya?",
        "answer": "Hitsumabushi"
    },
    {
        "context_index": 26,
        "question": "What is Hitsumabushi made of?",
        "answer": "grilled eel over rice"
    },
    {
        "context_index": 26,
        "question": "What notable awards have faculty from Nagoya University won?",
        "answer": "Nobel Prizes"
    },
    {
        "context_index": 26,
        "question": "What is Tebasaki?",
        "answer": "savory chicken wings"
    },
    {
        "context_index": 26,
        "question": "How are Tebasaki wings typically served?",
        "answer": "marinated in a sweet and spicy sauce and served piping hot"
    },
    {
        "context_index": 26,
        "question": "What type of dish is Misokatsu?",
        "answer": "a breaded and deep-fried pork cutlet smothered in a thick, savory miso sauce"
    }
]
)

train_data = []
train_contexts_data = []
#answer_start = context.lower().find(qa["answer"].lower())

for i, context in enumerate(train_contexts):
    qas = []
    for qa in train_questions_answers:
        #print(f'qa is {qa}')
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
    "Established in 1939, Nagoya University has grown to become one of the top research institutions in Japan, noted particularly for its contributions to the fields of science and engineering. Among its faculty, it boasts 6 Nobel Prize winners who have advanced the frontiers of knowledge in physics and chemistry.",
    "Nagoya University, located in Chikusa-ku, is not only a hub for academic excellence but also a landmark of historical significance in Japanese education. It has a vibrant campus life and is known for its commitment to fostering international collaborations.",
    "The achievements of Nagoya University in the field of scientific research are numerous, including significant contributions by its Nobel laureates. The university continues to be at the forefront of technological innovation and scientific discovery."
]

test_questions_answers = [
    {
        "context_index": 0,
        "question": "What is Nagoya University noted for?",
        "answer": "its contributions to the fields of science and engineering"
                
    },
    {
        "context_index": 0,
        "question": "How many Nobel Prize winners are associated with Nagoya University?",
        "answer":  "6"
    },
    {
        "context_index": 0,
        "question": "In what fields have Nagoya University's Nobel laureates made advancements?",
        "answer": "physics and chemistry"
    },
    {
        "context_index": 1,
        "question": "Where is Nagoya University located?",
        "answer": "in Chikusa-ku",
    },
    {
        "context_index": 1,
        "question": "What is Nagoya University known for apart from academic excellence?",
        "answer": "fostering international collaborations"
    },
    {
        "context_index": 2,
        "question": "What ongoing role does Nagoya University play in scientific research?",
        "answer": "at the forefront of technological innovation and scientific discovery",

    }
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



for context_data in test_contexts_data:
    if not context_data['qas']:
        print("No valid QA pairs found for context:", context_data['context'])


with open('amazon_data_test.json', 'w', encoding='utf-8') as f:
    json.dump(test_data, f, ensure_ascii=False, indent=4)




