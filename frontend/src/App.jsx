import { useEffect, useState } from 'react';
import './App.css';
import { getTasks, createTask } from './services/taskService';

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTitle, setNewTitle] = useState('');
  const [newDesc, setNewDesc] = useState('');
   
  // 1. Estado para o Modal
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleCreateTask = async (e) => {
    e.preventDefault();

    if(!newTitle.trim()) return alert("O título é obrigatório!")

    try {
      const taskPayload = {
        title: newTitle,
        description: newDesc,
        status: "PENDENTE"
    };

      const response = await createTask(taskPayload);

      //adds the new task returned by the backend to the local state
      setTasks([...tasks, response.data]);
        
      //clean the fields
       setNewTitle('');
       setNewDesc('');
       setIsModalOpen(false);
      } 
    catch (error) {
        console.error("Erro ao criar tarefa:", error);
        alert("Erro ao conectar com o servidor.");
      }
  };

  useEffect(() => {
    // Search for tasks when the page loads.
    getTasks().then(response => {
      console.log("Dados que chegaram:", response.data); // Olhe o console do navegador (F12)
      setTasks(response.data);
    }).catch(err => console.error("Erro ao buscar tarefas", err));
  }, []);

  // Filtering tasks into columns, like in Trello.
  const pendingTasks = tasks.filter(t => t.status === 'PENDENTE');
  const inProgressTasks = tasks.filter(t => t.status === 'EM_PROGRESSO');
  const completedTasks = tasks.filter(t => t.status === 'CONCLUIDO');

  return (
    <div className="board">
      <div className="column">
        <h2>Pendente 🟡</h2>
      {pendingTasks.map(task => <div key={task.id} className="card">{task.title}</div>)}
      </div>
      
      <div className="column">
        <h2>Em Progresso 🔵</h2>
        {inProgressTasks.map(task => <div key={task.id} className="card">{task.title}</div>)}
      </div>

      <div className="column">
        <h2>Concluído 🟢</h2>
        {completedTasks.map(task => <div key={task.id} className="card">{task.title}</div>)}
      </div>
      
      {/*Button add task */}
      <button className="fab-button" onClick={() => setIsModalOpen(true)}>+ Adicionar Tarefa</button>

      {/*Modal add task form */}
      {isModalOpen && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Nova Tarefa</h3>
            <form onSubmit={handleCreateTask}>
              <input 
                type="text" 
                placeholder="Título" 
                value={newTitle} 
                onChange={(e) => setNewTitle(e.target.value)} 
                autoFocus
              />
              <textarea 
                placeholder="Descrição" 
                value={newDesc} 
                onChange={(e) => setNewDesc(e.target.value)}
              />
              <div className="modal-actions">
                <button type="button" onClick={() => setIsModalOpen(false)}>Cancelar</button>
                <button type="submit" className="save-btn">Criar Tarefa</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;