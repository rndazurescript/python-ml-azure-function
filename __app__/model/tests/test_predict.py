import sys,json;
from model.predict import predict_image_from_url;  

cat_image='https://raw.githubusercontent.com/Azure-Samples/functions-python-tensorflow-tutorial/master/resources/assets/samples/cat1.png'
dog_image='https://raw.githubusercontent.com/Azure-Samples/functions-python-tensorflow-tutorial/master/resources/assets/samples/dog1.png'

def test_model_can_predict_cats():
    results = predict_image_from_url(cat_image); 
    print(json.dumps(results));
    assert('cat' == results['predictedTagName'])
    
def test_model_can_predict_dogs():
    results = predict_image_from_url(dog_image); 
    print(json.dumps(results));
    assert('dog' == results['predictedTagName'])

if __name__ == "__main__":
    import pytest
    pytest.main()
 
