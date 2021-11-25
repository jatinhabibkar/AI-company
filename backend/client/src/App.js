import './App.css';
import React, { useState} from "react";
import axios  from 'axios';
import M from "materialize-css/dist/js/materialize.min";
import { Loading } from './Loading';

const App = () => {

  

  const [loading,setloading]= useState(false)
  const [reportlink,setreport]=useState(null)
  const [data,setdata]=useState(null)
  const [file,setfile]=useState({
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
    axios.post(process.env.REACT_APP_BACKEND+'data',formData,config).then((response) => {
      console.log(JSON.stringify(response));
      setdata(response.data.data)
      if(response.data.report)
        setreport(process.env.REACT_APP_BACKEND+response.data.report)

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
    axios.post(process.env.REACT_APP_BACKEND+'upload',formData,config).then((response) => {
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
      
      
      <h1>AI company</h1> </span>
     
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
          <div className="container" >
                      
                      <label htmlFor="start" className="left">Start date:</label>
                      <input type="date" id="start" name="dateStart" className="browser-default left"  onChange={(e)=>{setdates({ ...mydates, [e.target.name]: e.target.value })}} />
                      <label htmlFor="start" className="left">End date:</label>
                      <input type="date" id="end" name="dateEnd" className="browser-default left"  onChange={(e)=>{setdates({ ...mydates, [e.target.name]: e.target.value })}} />

                  <button className="btn" type="submit" name="action" onClick={(e)=>{submitdate(e)}}>Show</button>
                  
                  &nbsp;
                  &nbsp;
                  &nbsp;
                  &nbsp;
                  {reportlink && <a className='btn' href={reportlink}>download report</a>}
                  
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
                          <img className='responsive-img' style={{height:"200px"}} src={process.env.REACT_APP_BACKEND+'media/'+item.fields.image_name} alt="img" />
                        </td>  
                      </tr>)
                  })
                ):( <h1 className='center'>No data found</h1>)}              
            </tbody>
            
            </table> 



            }


        
        
    </div>
  );
}

export default App;
