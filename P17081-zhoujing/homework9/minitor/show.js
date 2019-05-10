import axios from 'axios'
import {observable} from 'mobx'




export default class ShowService{
    @observable state={}

    constructor(){
        this.axios = axios.create({
            baseURL:'/api/show/'
        })
        this.sta = {}
    }
    show(id){
        this.axios.get(id).then( (response)=>{
            this.sta = response.data.state
            this.state = response.data.state
            console.log(this.sta,"~~~~~~~~~~~")
        }).catch((err)=>{
            console.log(err)
        })
    }


}



