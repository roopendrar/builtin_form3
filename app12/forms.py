from django import forms


choices_day=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')]
choices_month=[('1','jan'),('2','feb'),('3','mar'),('4','apr'),('5','may'),('6','jun'),('7','jul'),('8','aug'),('9','sep'),('10','oct'),('11','nov'),('12','dec')]
choices_year=[('1947', '1947'), ('1948', '1948'), ('1949', '1949'), ('1950', '1950'), ('1951', '1951'), ('1952', '1952'), ('1953', '1953'), ('1954', '1954'), ('1955', '1955'), ('1956', '1956'), ('1957', '1957'), ('1958', '1958'), ('1959', '1959'), ('1960', '1960'), ('1961', '1961'), ('1962', '1962'), ('1963', '1963'), ('1964', '1964'), ('1965', '1965'), ('1966', '1966'), ('1967', '1967'), ('1968', '1968'), ('1969', '1969'), ('1970', '1970'), ('1971', '1971'), ('1972', '1972'), ('1973', '1973'), ('1974', '1974'), ('1975', '1975'), ('1976', '1976'), ('1977', '1977'), ('1978', '1978'), ('1979', '1979'), ('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')]

class Form(forms.Form):
    first_name=forms.CharField(max_length=20,required=True,label="First Name",widget=forms.TextInput(attrs={'placeholder':'first_name'}),help_text="Note:no special charecters is allowed")

    last_name=forms.CharField(max_length=20,required=True,label="Last Name",widget=forms.TextInput(attrs={'placeholder':'last_name'}))
    email=forms.EmailField(max_length=100,required=True,label="Email",widget=forms.TextInput(attrs={'placeholder':'email id'}))
    pwd=forms.CharField(max_length=20,required=True,widget=forms.PasswordInput,label="Password")
    phno=forms.CharField(max_length=10,min_length=10,required=True,label="Phone Number",widget=forms.TextInput(attrs={'pattern':'[6-9]\d{9}'}))
    birth_day=forms.ChoiceField(choices=choices_day,required=True,label="Birth day")
    birth_month=forms.ChoiceField(choices=choices_month,required=True,label="Birth month")
    birth_year=forms.ChoiceField(choices=choices_year,required=True,label="Birth year")
    gender=forms.ChoiceField(choices=[('male','male'),('female','female')],widget=forms.RadioSelect)
    prog_languages=forms.MultipleChoiceField(choices=[('c','c'),('c++','c++'),('c#','c#'),('python','python'),('java','java')])
    languages=forms.MultipleChoiceField(choices=[('kannada','kannada'),('english','english'),('telugu','telugu'),('tamil','tamil')],widget=forms.CheckboxSelectMultiple)
    image=forms.ImageField(max_length=200,allow_empty_file=False,required=True,label="profile pic")