from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        name=request.form.get('name')
        roll_no=int(request.form.get('roll_no'))
        fsd=int(request.form.get('fsd'))
        wd=int(request.form.get('wd'))
        net=int(request.form.get('net'))
        cloud=int(request.form.get('cloud'))
        
        total_marks=fsd+wd+net+cloud
        percentage=(total_marks/400)*100
        
        
        if percentage>=90:
            grade ='O'
        elif percentage>=80:
            grade ='A'   
            
        elif percentage>=70:
            grade ='B'
        
        elif percentage>=50:
            grade ='C'
        else:
            grade = 'F'
            
    return f""" 
      <p>Student Name:{name}</p>
      <p>Roll_no:{roll_no}</p>
      <p>Full Stack Development:{fsd}</p>
      <p>Web Development:{wd}</p>
      <p>.NET:{net}</p>
      <p>Cloud:{cloud}</p>
      <p>Total_marks:{total_marks}</p>
      <p>Percentage:{percentage}</p>
      <p>Grade:{grade}</p>

"""

if __name__=='__main__':
    app.run(debug=True)