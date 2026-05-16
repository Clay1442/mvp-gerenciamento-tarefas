import { useEffect, useState } from 'react';
import './Board.css';
import { getTasks, createTask, updateTaskStatus, deleteTask } from '../services/taskService';

function Board() {
  const [tasks, setTasks] = useState([]);
  const [newTitle, setNewTitle] = useState('');
  const [newDesc, setNewDesc] = useState('');
  const [isModalOpen, setIsModalOpen] = useState(false);

  //States for editing a task
  const [editingTask, setEditingTask] = useState(null); // Armazena a task clicada
  const [editTitle, setEditTitle] = useState('');
  const [editDesc, setEditDesc] = useState('');
  const [editStatus, setEditStatus] = useState('');

  const handleCardClick = (task) => {
    setEditingTask(task);
    setEditTitle(task.title);
    setEditDesc(task.description || '');
    setEditStatus(task.status);
  };

  //Function to save the edited task
  const handleSaveEdit = async (e) => {
    e.preventDefault();
    try {
      await updateTaskStatus(editingTask.id, editStatus); 
      
      //Update the local state to reflect the changes without needing to refetch all tasks
      setTasks(prev => prev.map(t => t.id === editingTask.id ? { 
        ...t, 
        title: editTitle, 
        description: editDesc, 
        status: editStatus 
      } : t));
      
      //Close the edit modal
      setEditingTask(null); 
    } catch (err) {
      console.error(err);
    }
  };

  
  //Function to handle task deletion
  const handleDelete = async () => {
  if (!window.confirm("Tem certeza que deseja apagar esta tarefa permanentemente?")) return;

  try {
    await deleteTask(editingTask.id);
    setTasks(prevTasks => prevTasks.filter(task => task.id !== editingTask.id));
    setEditingTask(null);
  } catch (error) {
    console.error("Erro ao deletar tarefa:", error);
    alert("Não foi possível deletar a tarefa no servidor.");
    }
  };


  //Function to update the status
  const handleStatusChange = async (taskId, newStatus) => {
    try {
      await updateTaskStatus(taskId, newStatus);     
      //Update the local state to reflect the status change without needing to refetch all tasks
      setTasks(prevTasks => 
        prevTasks.map(task => 
          task.id === taskId ? { ...task, status: newStatus } : task
        )
      );
    } catch (error) {
      console.error("Erro ao atualizar status da tarefa:", error);
      alert("Não foi possível mover a tarefa.");
    }
  };

  //function to create a new task
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

  const renderCard = (task) => (
    <div key={task.id} className="card" onClick={() => handleCardClick(task)}>
      <h4>{task.title}</h4>
      {task.description && <p style={{ fontSize: '13px', color: '#eaeaea' }}>. . . </p>}
      <span className={`status-badge ${task.status.toLowerCase()}`}>
        {task.status === 'PENDENTE' ? '🟡 Pendente' : task.status === 'EM_PROGRESSO' ? '🔵 Em Progresso' : '🟢 Concluído'}
      </span>
    </div>
  );

  return (
<div className="board">
      <div className="column">
        <h2>Pendente 🟡</h2>
        {tasks.filter(t => t.status === 'PENDENTE').map(renderCard)}
      </div>
      
      <div className="column">
        <h2>Em Progresso 🔵</h2>
        {tasks.filter(t => t.status === 'EM_PROGRESSO').map(renderCard)}
      </div>

      <div className="column">
        <h2>Concluído 🟢</h2>
        {tasks.filter(t => t.status === 'CONCLUIDO').map(renderCard)}
      </div>
      
      {/*Button add task */}
      <button className="fab-button" onClick={() => setIsModalOpen(true)}>+ Adicionar Tarefa</button>

      {/* Edit Task Modal */}
      {editingTask && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Detalhes da Tarefa</h3>
            <form onSubmit={handleSaveEdit}>
              <label>Título:</label>
              <input type="text" value={editTitle} onChange={(e) => setEditTitle(e.target.value)} />

              <label>Descrição:</label>
              <textarea value={editDesc} onChange={(e) => setEditDesc(e.target.value)} rows="4" />

              <label>Status atual:</label>
              <select value={editStatus} onChange={(e) => setEditStatus(e.target.value)}>
                <option value="PENDENTE">Pendente 🟡</option>
                <option value="EM_PROGRESSO">Em Progresso 🔵</option>
                <option value="CONCLUIDO">Concluído 🟢</option>
              </select>
              
              <div className="modal-actions">
                <button type="button" className="delete-btn" onClick={handleDelete}>
                  🗑️ Excluir Tarefa
                </button>

                <button type="button" className='cancel-btn' onClick={() => setEditingTask(null)}>Fechar</button>
                <button type="submit" className="save-btn">Salvar Alterações</button>
              </div>
            </form>
          </div>
        </div>
      )}




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
                <button type="button" className='cancel-btn' onClick={() => setIsModalOpen(false)}>Cancelar</button>
                <button type="submit" className="save-btn">Criar Tarefa</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default Board;