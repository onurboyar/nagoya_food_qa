import gradio as gr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from simpletransformers.question_answering import QuestionAnsweringModel

# Define contexts

# List of available contexts
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

train_contexts.extend([
    "Famous foods in Nagoya are tebasaki, kishimen, hitsumabushi."
])

train_contexts.extend([
    "Established in 1939, Nagoya University has grown to become one of the top research institutions in Japan, noted particularly for its contributions to the fields of science and engineering. Among its faculty, it boasts 6 Nobel Prize winners who have advanced the frontiers of knowledge in physics and chemistry.",
    "Nagoya University, located in Chikusa-ku, is not only a hub for academic excellence but also a landmark of historical significance in Japanese education. It has a vibrant campus life and is known for its commitment to fostering international collaborations.",
    "The achievements of Nagoya University in the field of scientific research are numerous, including significant contributions by its Nobel laureates. The university continues to be at the forefront of technological innovation and scientific discovery."

])

train_contexts.extend([
    "Nagoya is located in Aichi Prefecture of Japan.",
    "There are 6 nobel prize owners in the history of Nagoya University."
])


# Find the most relevant context for a given question
def find_most_relevant_context(question, contexts):
    vectorizer = TfidfVectorizer()
    all_texts = [question] + contexts
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    return contexts[cosine_similarities.argmax()]

# Prediction function for Gradio Interface
def predict_answer(question):
    relevant_context = find_most_relevant_context(question, contexts)
    model = QuestionAnsweringModel("bert", "outputs/best_model")
    to_predict = [
        {
            "context": relevant_context,
            "qas": [
                {
                    "question": question,
                    "id": "0",
                }
            ],
        }
    ]
    answers, _ = model.predict(to_predict)
    # Formatting output to display multiple answers
    formatted_answers = {f"Answer {i+1}": ans['answer'] for i, ans in enumerate(answers)}
    return formatted_answers

# Setup Gradio interface
iface = gr.Interface(
    fn=predict_answer,
    inputs="text",
    outputs=gr.JSON(),  # Adjust based on maximum expected answers
    title="NagoyaGPY",
    description="Ask any question about Nagoya and NagoyaGPT will answer."
)


# Launch the interface
iface.launch(share=True)
