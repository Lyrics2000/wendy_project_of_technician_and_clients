from django import forms




class TechnicianDetailss(forms.Form):
    
    Shoplocation = forms.CharField(
        widget=forms.TextInput(
            attrs={
               "name" : "fullname" , "type":"text" , "placeholder":"Shop Location",  "class":"form-control lgn_input"
               , "required":" "
            }
        )
    )
    PhoneNumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
               "name" : "fullname" , "type":"text" , "placeholder":"Phone Number",  "class":"form-control lgn_input"
               , "required":" "
            }
        )
    )
    
    Description = forms.CharField(
        widget=forms.Textarea(
            attrs={
               "name" : "fullname" , "type":"text" , "placeholder":"Description",  "class":"form-control lgn_input"
               , "required":" "
            }
        )
    )
    
   
    
    
   
   