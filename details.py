class Model:
    def __init__(self,title,description,result_yes,result_no,attributes):
        self.title = title
        self.description = description
        self.result_yes = result_yes
        self.result_no = result_no
        self.attributes = attributes


models = {

      "brain" : Model("Brain Tumor Predictor",
                      "Our brain tumor predictor is a tool designed to provide individuals with a preliminary risk assessment of having a brain tumor.Our predictor is easy to use, and its results are presented in a clear and easy-to-understand format",
                      "Having Brain Tumor",
                      "Not having brain tumor",
                      ['mri_image']
      )
}