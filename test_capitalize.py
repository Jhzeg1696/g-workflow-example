def capitalize_string(s):
    if not isinstance(s, str):
        raise TypeError('Provide a string')
    
    return s.capitalize()

def test_capitalize_String():
    assert capitalize_string('sda') == 'Sda'