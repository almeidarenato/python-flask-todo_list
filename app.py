from flask import Flask,request,jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1
@app.route('/tasks',methods=['POST'])
def create_task():
    # sempre que for necessário fazer interações com uma variável que está fora do método
    # é necessário usar o "global" antes do nome da variável
    global task_id_control
    data = request.get_json()
    # com o data.get("valor1","valor2")
    # primeiro é verificado se na propriedade do valor1 existe valor. Se não ele assume o "valor2"
    new_task = Task(id=task_id_control,title=data['title'],description=data.get("description",""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message":"Nova tarefa criada com sucesso"})

@app.route('/tasks',methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    # outra forma de entender essa logica é: 
    # for task in tasks:
    #     task_list.append(task.to_dict())

    output = {
        "tasks":task_list,
        "total_tasks": 0
    }
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)