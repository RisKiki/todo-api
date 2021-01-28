from app import app

if __name__ == "__main__": 
    print("Routes :")
    print('/account : POST OK')
    print('/login : NO OK')
    print('/lists : NO OK')
    print('/lists/<int:list_id> : NO OK')
    print('/lists/todos/<int:list_id>/<int:todo_id> : NO OK')
    print('/lists/todos/<int:id_list> : NO OK')
    app.run(debug=True)
