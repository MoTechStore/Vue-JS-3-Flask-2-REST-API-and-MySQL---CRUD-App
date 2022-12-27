<template>
    
<div class="container-fluid"> 
        <h2 class="alert alert-danger mt-2">Flask 2 And Vue JS 3 CRUD Application</h2>

        <div class="row">

            


            <div class="col-md-7">


                <h2 class="alert alert-success">List of Students</h2>

                <table class="table table-bordered mt-4">
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Course</th>
      <th scope="col">Email</th>
      <th scope="col">Gender</th>
      <th scope="col">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="student in students">
      <td>{{student.name}}</td>
      <td>{{student.course}}</td>
      <td>{{student.email}}</td>
      <td>{{student.gender}}</td>
      <td>
        <a href="#" class="edit" title="" ><button @click="editBtn(student.id)" class="btn btn-warning btn-sm">Edit</button></a>
        <a href="#" class="edit ml-1" title="" ><button @click="deleteStudent(student.id)"  class="btn btn-danger btn-sm">Delete</button></a>


      </td>
    </tr>
  </tbody>
</table>

            </div>


            <div class="col-md-5">



                  <!-- There is a current student to be edited -->

                <div v-if="Object.keys(this.currentStudent).length !== 0">
                

                    <h2 class="alert alert-warning">Edit Student Details</h2>

                    <form @submit.prevent="editStudent(this.currentStudent.id)">

<div class="row">

    <div class="col">
        <div class="form-group">
<label class="form-label float-left ml-2">Name</label>
<input type="text" class="form-control" v-model="currentStudent.name">
</div>
    </div>

    <div class="col">
        <div class="form-group">
<label class="form-label float-left ml-2">Email</label>
<input type="email" class="form-control" v-model="currentStudent.email">
</div>
    </div>
</div>



<div class="row">
<div class="col">
<div class="form-group">
<label class="form-label float-left ml-2">Course</label>
<input type="text" class="form-control" v-model="currentStudent.course">
</div>
</div>
<div class="col">

<div class="form-group">
<label class="form-label float-left ml-2">Gender</label>
<input type="text" class="form-control" v-model="currentStudent.gender">
</div>
</div>

</div>
<button type="submit" class="btn btn-success float-left ml-2">Update</button>
</form>

                </div>




                <!-- There is no current student to be edited -->

                <div v-else>
                    <h2 class="alert alert-info">Create A New Student</h2>
                    <form @submit.prevent="saveStudent()">

<div class="row">

    <div class="col">
        <div class="form-group">
<label class="form-label float-left ml-2">Name</label>
<input type="text" class="form-control" v-model="student.name">
</div>
    </div>

    <div class="col">
        <div class="form-group">
<label class="form-label float-left ml-2">Email</label>
<input type="email" class="form-control" v-model="student.email">
</div>
    </div>
</div>



<div class="row">
<div class="col">
<div class="form-group">
<label class="form-label float-left ml-2">Course</label>
<input type="text" class="form-control" v-model="student.course">
</div>
</div>
<div class="col">

<div class="form-group">
<label class="form-label float-left ml-2">Gender</label>
<input type="text" class="form-control" v-model="student.gender">
</div>
</div>

</div>
<button type="submit" class="btn btn-primary float-left ml-2">Save</button>
</form>
                </div>
            </div>
        </div>
    </div>




</template>


<script>
import axios from 'axios'

export default{
    data(){
        return {
            'api': 'http://127.0.0.1:5000/api/students/',
            students: [],
            currentStudent: {},
            'student': {
                'name': '',
                'email': '',
                'course': '',
                'gender': '',
            }

        }
    },

    mounted(){
        console.log('DOM mounted')
    },


    created(){
        console.log('DOM created')
        this.getStudents()
    },



    methods: {

        getStudents(){
            axios.get(this.api).then(
                response => { 
                    console.log(response.data.students)
                    this.students = response.data.students
                }
            )
        },

        saveStudent(){
            axios.post(this.api, this.student).then(
                response => { 
                    console.log(response.data)
                    this.student = {}
                    this.getStudents()
                }
            )

        },

        editBtn(id){
            console.log(id)
            this.students.map(student => {
                if(student.id === id){
                    console.log(student.name)
                    this.currentStudent = {'id':student.id, 'name':student.name, 'gender':student.gender, 'email':student.email, 'course':student.course}
                }
            })


        },



        editStudent(){
            axios.put(this.api, this.currentStudent).then(
                response => { 
                    console.log(response.data)
                    this.currentStudent = {}
                    this.getStudents()
                }
            )

        },


        deleteStudent(id){

            axios.patch(this.api, {'id':id}).then(
                response => { 
                    console.log(response.data)
                    this.getStudents()
                }
            )

        },

    },




}

</script>
