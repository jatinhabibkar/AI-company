import './App.css';
import React, { useState} from "react";
import axios  from 'axios';
import M from "materialize-css/dist/js/materialize.min.js";
import { Loading } from './Loading';

const App = () => {

  

  const [loading,setloading]= useState(false)
  const [data,setdata]=useState(null)
  const [file,setfile]=useState({
    url:'/upload',
    file: null
  })
  const [mydates,setdates] = useState({
    "dateStart":null,
    "dateEnd":null
  })


  const submitdate = async (e)=>{
    e.preventDefault()
    
    if(!mydates.dateEnd || !mydates.dateStart){
      M.toast({'html':"plz fill the start and end date"})
      return
    }
    setloading(true)
    let formData = new FormData();
    console.log(mydates);
    formData.append("dateStart",mydates.dateStart);
    formData.append("dateEnd",mydates.dateEnd);
    let config={
      mode: 'no-cors',
      headers: {
        "Content-Type": "text/json",
      },
    }
    axios.post('/data',formData,config).then((response) => {
      console.log(JSON.stringify(response));
      setdata(response.data.data)
      console.log(data);

    }).catch((error) => {
      console.log(error);
      M.toast({'html':"something went wrong"})
    });
    setloading(null)

  }

  const handleSubmit = async (e)=>{
    e.preventDefault()  
    if(!file.file){
      M.toast({'html':"plz select file"})
      return
    }
    setloading(true)
    let formData = new FormData();
    formData.append("file",file.file);

    let config={
      mode: 'no-cors',
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
    axios.post(file.url,formData,config).then((response) => {
      console.log(JSON.stringify(response.data));
      M.toast({'html':"file uploaded"})
    }).catch((error) => {
      M.toast({'html':"something went wrong"})
    });

    setloading(null)
  }
  
  return (
    <div className="App container">
      <span className="myHeader">{loading && <Loading/> }
      
      
      <h1>BaggageAI</h1> </span>
     
        <form action="">
            <div className="file-field input-field">
                <div className="btn">
                    <span>   <i className="material-icons">attach_file</i></span> 
                    <input type="file" id="csv" accept="text/csv" name="csv"  onChange={(e)=>{setfile({ ...file, "file": e.target.files[0] })}} />
                </div>
                <button className="btn waves-effect right waves-light" type="submit" name="action" onClick={(e)=>{handleSubmit(e)}}>Submit</button>

                <div className="file-path-wrapper">
                    <input className="file-path validate" type="text" onChange={(e)=>{setfile({ ...file, "remark": e.target.value })}}/>
                </div>

                
            </div>

        </form>
        <br />
        <form >
          <div className="container left" style={{display:"flex"}}>
                      
                      <label htmlFor="start" className="left">Start date:</label>
                      <input type="date" id="start" name="dateStart" className="browser-default left"  onChange={(e)=>{setdates({ ...mydates, [e.target.name]: e.target.value })}} />
                      <label htmlFor="start" className="left">End date:</label>
                      <input type="date" id="end" name="dateEnd" className="browser-default left"  onChange={(e)=>{setdates({ ...mydates, [e.target.name]: e.target.value })}} />

                  <button className="btn waves-effect right waves-light left" type="submit" name="action" onClick={(e)=>{submitdate(e)}}>Show</button>
          </div>
        </form>
        {data &&

          
        <table>
            <thead>
                <tr>
                  <th>image_name</th>
                  <th>detection</th>
                  <th>image</th>
                </tr>
            </thead>    
            <tbody>
              {data.length !== 0 ?(data.map((item,i)=>{
                     return( <tr>
                        <td>{item.fields.image_name}</td>
                        <td>{item.fields.object_detected}</td>
                        <td >
                          <img className='responsive-img' style={{height:"200px"}} src={process.env.REACT_APP_BACKEND_MEDIA+item.fields.image_name} alt="img" />
                        </td>  
                      </tr>)
                  })
                ):(<h1>No data found</h1>)}
                                                   
            </tbody>
            
            </table> 



            }


        
        
    </div>
  );
}

export default App;
