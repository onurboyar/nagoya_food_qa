from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs
 
model = QuestionAnsweringModel("bert", "outputs/best_model")
 
 
# Make predictions with the model
to_predict = [
    {
        "context": "Established in 1939, Nagoya University has grown to become one of the top research institutions in Japan, noted particularly for its contributions to the fields of science and engineering. Among its faculty, it boasts 6 Nobel Prize winners who have advanced the frontiers of knowledge in physics and chemistry.",
        "qas": [
            {
                "question": "When does Nagoya University established?",
                "id": "0",
            }
        ],
    }
]
 
answers, probabilities = model.predict(to_predict, n_best_size=2)
print(answers)


to_predict = [
    {
        "context": "Nagoya is the largest city in the Chubu region, the fourth-most populous city proper with a population of 2.3 million in 2020, and the principal city of the Chukyo metropolitan area, which is the third-most populous metropolitan area in Japan with a population of 10.11 million. Located on the Pacific coast in central Honshu, it is the capital and most populous city of Aichi Prefecture, with the Port of Nagoya being Japan's largest seaport.",
        "qas": [
            {
                "question": "What is the population of Nagoya?",
                "id": "1",
            }
        ],
    }
]
 
answers, probabilities = model.predict(to_predict, n_best_size=2)
print(answers)


to_predict = [
    {
        "context": "Famous Nagoya foods are Tebasaki, Kishimen, Red miso, and Hitsumabushi. Tebasaki is chicken wings marinated in a sweet sauce with sesame seeds, basically a type of yakitori. Kishimen is flat udon noodles with a slippery texture, dipped in a light soy sauce soup and a sliced leek or other flavouring added.It can be eaten cold or hot. Hitsumabushi is a rice dish with unagi in a lidded wooden container. This dish is enjoyed three ways; as unadon, with spice and as chazuke ",
        "qas": [
            {
                "question": "What are famous Nagoya foods?",
                "id": "2",
            }
        ],
    }
]
 
answers, probabilities = model.predict(to_predict, n_best_size=2)
print(answers)


to_predict = [
    {
        "context": "Famous Nagoya foods are Tebasaki, Kishimen, Red miso, and Hitsumabushi. Tebasaki is chicken wings marinated in a sweet sauce with sesame seeds, basically a type of yakitori. Kishimen is flat udon noodles with a slippery texture, dipped in a light soy sauce soup and a sliced leek or other flavouring added.It can be eaten cold or hot. Hitsumabushi is a rice dish with unagi in a lidded wooden container. This dish is enjoyed three ways; as unadon, with spice and as chazuke ",
        "qas": [
            {
                "question": "What is Tebasaki?",
                "id": "3",
            }
        ],
    }
]
 
answers, probabilities = model.predict(to_predict, n_best_size=2)
print(answers)



to_predict = [
    {
        "context": "Nagoya, a vibrant city in the heart of Japan's Aichi Prefecture, boasts a rich cultural heritage and a reputation for academic excellence, embodied by Nagoya University. Founded in 1939, Nagoya University has emerged as a beacon of innovation and scholarly achievement, particularly noted for its contributions to fields such as engineering, chemistry, and physics, which have led to numerous accolades including Nobel Prizes for several of its faculty. This institution not only attracts students from across Japan but also from around the globe, fostering a diverse academic community that thrives on creativity and scientific inquiry. Alongside its academic prestige, Nagoya is famous for its distinctive cuisine that offers a delectable array of unique dishes. Among these culinary delights is the famous Nagoya Cochin chicken, renowned for its juicy texture and deep flavor, and the city’s signature dish, Hitsumabushi, which consists of grilled eel over rice. Hitsumabushi can be enjoyed in various ways, making it a versatile dish beloved by many. Another local favorite is Tebasaki, savory chicken wings that are a staple in local bars and restaurants. These wings are marinated in a sweet and spicy sauce and served piping hot, often accompanied by a cold beer, creating a perfect blend of flavors that epitomize Nagoya’s rich culinary culture. Additionally, Misokatsu, a breaded and deep-fried pork cutlet smothered in a thick, savory miso sauce, offers another taste of the unique flavor profile typical of the region. Both Nagoya University and the city’s distinct food culture exemplify the blend of tradition and modernity that characterizes this dynamic city, making it a fascinating destination for both intellectual pursuits and gastronomic adventures.",
        "qas": [
            {
                "question": "How is Nagoya city?",
                "id": "3",
            }
        ],
    }
]
 
answers, probabilities = model.predict(to_predict, n_best_size=2)
print(answers)

to_predict = [
    {
        "context": "Nagoya, a vibrant city in the heart of Japan's Aichi Prefecture, boasts a rich cultural heritage and a reputation for academic excellence, embodied by Nagoya University. Founded in 1939, Nagoya University has emerged as a beacon of innovation and scholarly achievement, particularly noted for its contributions to fields such as engineering, chemistry, and physics, which have led to numerous accolades including Nobel Prizes for several of its faculty. This institution not only attracts students from across Japan but also from around the globe, fostering a diverse academic community that thrives on creativity and scientific inquiry. Alongside its academic prestige, Nagoya is famous for its distinctive cuisine that offers a delectable array of unique dishes. Among these culinary delights is the famous Nagoya Cochin chicken, renowned for its juicy texture and deep flavor, and the city’s signature dish, Hitsumabushi, which consists of grilled eel over rice. Hitsumabushi can be enjoyed in various ways, making it a versatile dish beloved by many. Another local favorite is Tebasaki, savory chicken wings that are a staple in local bars and restaurants. These wings are marinated in a sweet and spicy sauce and served piping hot, often accompanied by a cold beer, creating a perfect blend of flavors that epitomize Nagoya’s rich culinary culture. Additionally, Misokatsu, a breaded and deep-fried pork cutlet smothered in a thick, savory miso sauce, offers another taste of the unique flavor profile typical of the region. Both Nagoya University and the city’s distinct food culture exemplify the blend of tradition and modernity that characterizes this dynamic city, making it a fascinating destination for both intellectual pursuits and gastronomic adventures.",
        "qas": [
            {
                "question": "When does Nagoya University founded?",
                "id": "3",
            }
        ],
    }
]
 
answers, probabilities = model.predict(to_predict, n_best_size=2)
print(answers)


to_predict = [
    {
        "context": "Nagoya, a vibrant city in the heart of Japan's Aichi Prefecture, boasts a rich cultural heritage and a reputation for academic excellence, embodied by Nagoya University. Founded in 1939, Nagoya University has emerged as a beacon of innovation and scholarly achievement, particularly noted for its contributions to fields such as engineering, chemistry, and physics, which have led to numerous accolades including Nobel Prizes for several of its faculty. This institution not only attracts students from across Japan but also from around the globe, fostering a diverse academic community that thrives on creativity and scientific inquiry. Alongside its academic prestige, Nagoya is famous for its distinctive cuisine that offers a delectable array of unique dishes. Among these culinary delights is the famous Nagoya Cochin chicken, renowned for its juicy texture and deep flavor, and the city’s signature dish, Hitsumabushi, which consists of grilled eel over rice. Hitsumabushi can be enjoyed in various ways, making it a versatile dish beloved by many. Another local favorite is Tebasaki, savory chicken wings that are a staple in local bars and restaurants. These wings are marinated in a sweet and spicy sauce and served piping hot, often accompanied by a cold beer, creating a perfect blend of flavors that epitomize Nagoya’s rich culinary culture. Additionally, Misokatsu, a breaded and deep-fried pork cutlet smothered in a thick, savory miso sauce, offers another taste of the unique flavor profile typical of the region. Both Nagoya University and the city’s distinct food culture exemplify the blend of tradition and modernity that characterizes this dynamic city, making it a fascinating destination for both intellectual pursuits and gastronomic adventures.",
        "qas": [
            {
                "question": "What are delicious foods in Nagoya?",
                "id": "3",
            }
        ],
    }
]
 
answers, probabilities = model.predict(to_predict, n_best_size=2)
print(answers)

to_predict = [
    {
        "context": "Nagoya, a vibrant city in the heart of Japan's Aichi Prefecture, boasts a rich cultural heritage and a reputation for academic excellence, embodied by Nagoya University. Founded in 1939, Nagoya University has emerged as a beacon of innovation and scholarly achievement, particularly noted for its contributions to fields such as engineering, chemistry, and physics, which have led to numerous accolades including Nobel Prizes for several of its faculty. This institution not only attracts students from across Japan but also from around the globe, fostering a diverse academic community that thrives on creativity and scientific inquiry. Alongside its academic prestige, Nagoya is famous for its distinctive cuisine that offers a delectable array of unique dishes. Among these culinary delights is the famous Nagoya Cochin chicken, renowned for its juicy texture and deep flavor, and the city’s signature dish, Hitsumabushi, which consists of grilled eel over rice. Hitsumabushi can be enjoyed in various ways, making it a versatile dish beloved by many. Another local favorite is Tebasaki, savory chicken wings that are a staple in local bars and restaurants. These wings are marinated in a sweet and spicy sauce and served piping hot, often accompanied by a cold beer, creating a perfect blend of flavors that epitomize Nagoya’s rich culinary culture. Additionally, Misokatsu, a breaded and deep-fried pork cutlet smothered in a thick, savory miso sauce, offers another taste of the unique flavor profile typical of the region. Both Nagoya University and the city’s distinct food culture exemplify the blend of tradition and modernity that characterizes this dynamic city, making it a fascinating destination for both intellectual pursuits and gastronomic adventures.",
        "qas": [
            {
                "question": "What is Tebasaki?",
                "id": "3",
            }
        ],
    }
]
 
answers, probabilities = model.predict(to_predict, n_best_size=2)
print(answers)