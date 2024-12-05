from flask import Flask, render_template, request
import pandas as pd
import openpyxl
# Read Excel data
courses_df = pd.read_excel("templates/timetable.xlsx")
courses_df_1=courses_df[(courses_df.index>12) & (courses_df.index<44) | (courses_df.index>=191) & (courses_df.index<225)]
courses_df_2=courses_df[(courses_df.index<13)]
courses_df_a1 = pd.read_excel("templates/timetable.xlsx")
courses_df_c1 = pd.read_excel("templates/timetable.xlsx")
courses_df_f1 = pd.read_excel("templates/timetable.xlsx")
courses_df_i1 = pd.read_excel("templates/timetable.xlsx")
courses_df_k1 = pd.read_excel("templates/timetable.xlsx")
courses_df_h1 = pd.read_excel("templates/timetable.xlsx")
courses_df_b1 = pd.read_excel("templates/timetable.xlsx")
courses_df_d1 = pd.read_excel("templates/timetable.xlsx")
courses_df_g1 = pd.read_excel("templates/timetable.xlsx")
courses_df_j1 = pd.read_excel("templates/timetable.xlsx")
courses_df_l1 = pd.read_excel("templates/timetable.xlsx")
courses_df_a2 = pd.read_excel("templates/timetable.xlsx")
courses_df_e1 = pd.read_excel("templates/timetable.xlsx")
courses_df_i2 = pd.read_excel("templates/timetable.xlsx")
courses_df_m1 = pd.read_excel("templates/timetable.xlsx")
courses_df_c2 = pd.read_excel("templates/timetable.xlsx")
courses_df_d2 = pd.read_excel("templates/timetable.xlsx")
courses_df_f2 = pd.read_excel("templates/timetable.xlsx")
courses_df_k2 = pd.read_excel("templates/timetable.xlsx")
courses_df_l2 = pd.read_excel("templates/timetable.xlsx")
courses_df_n2 = pd.read_excel("templates/timetable.xlsx")
courses_df_b2 = pd.read_excel("templates/timetable.xlsx")
courses_df_e2 = pd.read_excel("templates/timetable.xlsx")
courses_df_g2 = pd.read_excel("templates/timetable.xlsx")
courses_df_j2 = pd.read_excel("templates/timetable.xlsx")
courses_df_m2 = pd.read_excel("templates/timetable.xlsx")
courses_df_p2 = pd.read_excel("templates/timetable.xlsx")
courses_df_n1 = pd.read_excel("templates/timetable.xlsx")
courses_df_h2 = pd.read_excel("templates/timetable.xlsx")
courses_df_p1 = pd.read_excel("templates/timetable.xlsx")

ts=["i1","j1","i2","j2"]    
def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "A1" in row[col]:
            return row[col]
    return None

courses_df_a1["A1 entires"]=courses_df_a1.apply(extract_a1_values, axis=1)
courses_df_a1['Lecture Location'] = courses_df_a1['A1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_a1=courses_df_a1.dropna(subset=["A1 entires"])




def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "H1" in row[col]:
            return row[col]
    return None

courses_df_h1["H1 entires"]=courses_df_h1.apply(extract_a1_values, axis=1)
courses_df_h1['Lecture Location'] = courses_df_h1['H1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_h1=courses_df_h1.dropna(subset=["H1 entires"])


def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "C1" in row[col]:
            return row[col]
    return None

courses_df_c1["C1 entires"]=courses_df_c1.apply(extract_a1_values, axis=1)
courses_df_c1['Lecture Location'] = courses_df_c1['C1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_c1=courses_df_c1.dropna(subset=["C1 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "F1" in row[col]:
            return row[col]
    return None

courses_df_f1["F1 entires"]=courses_df_f1.apply(extract_a1_values, axis=1)
courses_df_f1['Lecture Location'] = courses_df_f1['F1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_f1=courses_df_f1.dropna(subset=["F1 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "I1" in row[col]:
            return row[col]
    return None

courses_df_i1["I1 entires"]=courses_df_i1.apply(extract_a1_values, axis=1)
courses_df_i1['Lecture Location'] = courses_df_i1['I1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_i1=courses_df_i1.dropna(subset=["I1 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "K1" in row[col]:
            return row[col]
    return None

courses_df_k1["K1 entires"]=courses_df_k1.apply(extract_a1_values, axis=1)
courses_df_k1['Lecture Location'] = courses_df_k1['K1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_k1=courses_df_k1.dropna(subset=["K1 entires"])


def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "B1" in row[col]:
            return row[col]
    return None

courses_df_b1["B1 entires"]=courses_df_b1.apply(extract_a1_values, axis=1)
courses_df_b1['Lecture Location'] = courses_df_b1['B1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_b1=courses_df_b1.dropna(subset=["B1 entires"])

def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "D1" in row[col]:
            return row[col]
    return None

courses_df_d1["D1 entires"]=courses_df_d1.apply(extract_a1_values, axis=1)
courses_df_d1['Lecture Location'] = courses_df_d1['D1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_d1=courses_df_d1.dropna(subset=["D1 entires"])




def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "G1" in row[col]:
            return row[col]
    return None

courses_df_g1["g1 entires"]=courses_df_g1.apply(extract_a1_values, axis=1)
courses_df_g1['Lecture Location'] = courses_df_g1['g1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_g1=courses_df_g1.dropna(subset=["g1 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "J1" in row[col]:
            return row[col]
    return None

courses_df_j1["j1 entires"]=courses_df_j1.apply(extract_a1_values, axis=1)
courses_df_j1['Lecture Location'] = courses_df_j1['j1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_j1=courses_df_j1.dropna(subset=["j1 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "L1" in row[col]:
            return row[col]
    return None

courses_df_l1["l1 entires"]=courses_df_l1.apply(extract_a1_values, axis=1)
courses_df_l1['Lecture Location'] = courses_df_l1['l1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_l1=courses_df_l1.dropna(subset=["l1 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "N1" in row[col]:
            return row[col]
    return None

courses_df_n1["n1 entires"]=courses_df_n1.apply(extract_a1_values, axis=1)
courses_df_n1['Lecture Location'] = courses_df_n1['n1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_n1=courses_df_n1.dropna(subset=["n1 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "A2" in row[col]:
            return row[col]
    return None

courses_df_a2["a2 entires"]=courses_df_a2.apply(extract_a1_values, axis=1)
courses_df_a2['Lecture Location'] = courses_df_a2['a2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_a2=courses_df_a2.dropna(subset=["a2 entires"])


def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "E1" in row[col]:
            return row[col]
    return None

courses_df_e1["e1 entires"]=courses_df_e1.apply(extract_a1_values, axis=1)
courses_df_e1['Lecture Location'] = courses_df_e1['e1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_e1=courses_df_e1.dropna(subset=["e1 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "H2" in row[col]:
            return row[col]
    return None

courses_df_h2["h2 entires"]=courses_df_h2.apply(extract_a1_values, axis=1)
courses_df_h2['Lecture Location'] = courses_df_h2['h2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_h2=courses_df_h2.dropna(subset=["h2 entires"])





def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "M1" in row[col]:
            return row[col]
    return None

courses_df_m1["m1 entires"]=courses_df_m1.apply(extract_a1_values, axis=1)
courses_df_m1['Lecture Location'] = courses_df_m1['m1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_m1=courses_df_m1.dropna(subset=["m1 entires"])

def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "I2" in row[col]:
            return row[col]
    return None

courses_df_i2["i2 entires"]=courses_df_i2.apply(extract_a1_values, axis=1)
courses_df_i2['Lecture Location'] = courses_df_i2['i2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_i2=courses_df_i2.dropna(subset=["i2 entires"])





def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "P1" in row[col]:
            return row[col]
    return None

courses_df_p1["p1 entires"]=courses_df_p1.apply(extract_a1_values, axis=1)
courses_df_p1['Lecture Location'] = courses_df_p1['p1 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_p1=courses_df_p1.dropna(subset=["p1 entires"])





def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "C2" in row[col]:
            return row[col]
    return None

courses_df_c2["c2 entires"]=courses_df_c2.apply(extract_a1_values, axis=1)
courses_df_c2['Lecture Location'] = courses_df_c2['c2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_c2=courses_df_c2.dropna(subset=["c2 entires"])




def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "D2" in row[col]:
            return row[col]
    return None

courses_df_d2["d2 entires"]=courses_df_d2.apply(extract_a1_values, axis=1)
courses_df_d2['Lecture Location'] = courses_df_d2['d2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_d2=courses_df_d2.dropna(subset=["d2 entires"])




def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "F2" in row[col]:
            return row[col]
    return None

courses_df_f2["f2 entires"]=courses_df_f2.apply(extract_a1_values, axis=1)
courses_df_f2['Lecture Location'] = courses_df_f2['f2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_f2=courses_df_f2.dropna(subset=["f2 entires"])




def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "K2" in row[col]:
            return row[col]
    return None

courses_df_k2["k2 entires"]=courses_df_k2.apply(extract_a1_values, axis=1)
courses_df_k2['Lecture Location'] = courses_df_k2['k2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_k2=courses_df_k2.dropna(subset=["k2 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "L2" in row[col]:
            return row[col]
    return None

courses_df_l2["l2 entires"]=courses_df_l2.apply(extract_a1_values, axis=1)
courses_df_l2['Lecture Location'] = courses_df_l2['l2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_l2=courses_df_l2.dropna(subset=["l2 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "N2" in row[col]:
            return row[col]
    return None

courses_df_n2["n2 entires"]=courses_df_n2.apply(extract_a1_values, axis=1)
courses_df_n2['Lecture Location'] = courses_df_n2['n2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_n2=courses_df_n2.dropna(subset=["n2 entires"])




def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "B2" in row[col]:
            return row[col]
    return None

courses_df_b2["b2 entires"]=courses_df_b2.apply(extract_a1_values, axis=1)
courses_df_b2['Lecture Location'] = courses_df_b2['b2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_b2=courses_df_b2.dropna(subset=["b2 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "E2" in row[col]:
            return row[col]
    return None

courses_df_e2["e2 entires"]=courses_df_e2.apply(extract_a1_values, axis=1)
courses_df_e2['Lecture Location'] = courses_df_e2['e2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_e2=courses_df_e2.dropna(subset=["e2 entires"])





def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "G2" in row[col]:
            return row[col]
    return None

courses_df_g2["g2 entires"]=courses_df_g2.apply(extract_a1_values, axis=1)
courses_df_g2['Lecture Location'] = courses_df_g2['g2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_g2=courses_df_g2.dropna(subset=["g2 entires"])



def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "J2" in row[col]:
            return row[col]
    return None

courses_df_j2["j2 entires"]=courses_df_j2.apply(extract_a1_values, axis=1)
courses_df_j2['Lecture Location'] = courses_df_j2['j2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_j2=courses_df_j2.dropna(subset=["j2 entires"])





def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "M2" in row[col]:
            return row[col]
    return None

courses_df_m2["m2 entires"]=courses_df_m2.apply(extract_a1_values, axis=1)
courses_df_m2['Lecture Location'] = courses_df_m2['m2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_m2=courses_df_m2.dropna(subset=["m2 entires"])




def extract_a1_values(row):
    for col in ["Lecture", "Lab", "Tutorial"]:
        if pd.notna(row[col]) and "P2" in row[col]:
            return row[col]
    return None

courses_df_p2["p2 entires"]=courses_df_p2.apply(extract_a1_values, axis=1)
courses_df_p2['Lecture Location'] = courses_df_p2['p2 entires'].str.extract(r'\((.*?)\)', expand=False)
courses_df_p2=courses_df_p2.dropna(subset=["p2 entires"])
app = Flask(__name__)


# Global variable to store selected courses


@app.route('/')
def hello():
    return render_template("aftab_index.html")

@app.route('/aftab_27')
def aftab_27():
    courses = courses_df_1["Course Name"].tolist()
    return render_template("aftab_27.html", courses=courses)

@app.route('/aftab_28')
def aftab_28():
    courses = courses_df_2["Course Name"].tolist()
    return render_template("aftab_28.html", courses=courses)

@app.route('/view-selected-courses', methods=['GET'])
def view_selected_courses():
    selected_courses_array = []
    global monday_courses
    # Get selected courses from the request
    selected_courses = request.args.get('selected_courses')
    if selected_courses:
        selected_courses_array.extend(eval(selected_courses))  # Parse the JSON string
        selected_courses_array = list(set(selected_courses_array))  # Remove duplicates
    
    # print("Selected Courses Array:", selected_courses_array)
    return render_template("view-selected-courses.html",selected_courses_array=selected_courses_array,courses_df_a1=courses_df_a1,courses_df_c1=courses_df_c1,courses_df_f1=courses_df_f1,courses_df_h1=courses_df_h1,courses_df_i1=courses_df_i1,courses_df_k1=courses_df_k1,courses_df_b1=courses_df_b1,courses_df_d1=courses_df_d1,courses_df_g1=courses_df_g1,courses_df_j1=courses_df_j1,courses_df_l1=courses_df_l1,courses_df_n1=courses_df_n1,courses_df_a2=courses_df_a2,courses_df_e1=courses_df_e1,courses_df_h2=courses_df_h2,courses_df_i2=courses_df_i2,courses_df_m1=courses_df_m1,courses_df_p1=courses_df_p1,courses_df_c2=courses_df_c2,courses_df_d2=courses_df_d2,courses_df_f2=courses_df_f2,courses_df_k2=courses_df_k2,courses_df_l2=courses_df_l2,courses_df_n2=courses_df_n2,courses_df_b2=courses_df_b2,courses_df_e2=courses_df_e2,courses_df_g2=courses_df_g2,courses_df_j2=courses_df_j2,courses_df_m2=courses_df_m2,courses_df_p2=courses_df_p2)


if __name__ == '__main__':
    app.run()
