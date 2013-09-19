"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "123456",
            "answer": "123.456"
        },

        {
            "input": "333",
            "answer": "333"
        },
        {
            "input": "9999999",
            "answer": "9.999.999"
        },
        {
            "input": "123456 567890",
            "answer": "123.456 567.890"
        },
        {
            "input": "price is 5799",
            "answer": "price is 5.799"
        },
        {
            "input": "he was born in 1966th",
            "answer": "he was born in 1966th"
        },

    ],
    "Extra": [
        {
            "input": "122456",
            "answer": "122.456"
        },
        {
            "input": "she was born in 2966th",
            "answer": "she was born in 2966th"
        },
        {
            "input": "It cost 44444 in 1980th",
            "answer": "It cost 44.444 in 1980th"
        },
        {
            "input": "3213442490979",
            "answer": "3.213.442.490.979"
        }
    ]
}
