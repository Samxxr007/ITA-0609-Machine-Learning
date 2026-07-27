def find_s(training_data):
   hypothesis = ['Ø'] * (len(training_data[0]) - 1)

   for example in training_data:
       if example[-1] == "Yes":  # positive example
           for i in range(len(hypothesis)):
               if hypothesis[i] == 'Ø':
                   hypothesis[i] = example[i]
               elif hypothesis[i] != example[i]:
                   hypothesis[i] = '?'
   return hypothesis


# Training data
data = [
   ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
   ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
   ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
   ["Sunny", "Warm", "High", "Strong", "Cool", "Same", "Yes"]
]

print("Final Hypothesis:", find_s(data))
