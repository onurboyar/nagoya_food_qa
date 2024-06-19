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
