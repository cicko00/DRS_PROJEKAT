import { Component, OnInit } from '@angular/core';
import { User } from '../models/user.model';
import { NavigationServiceService } from '../services/navigation-service.service';
import { FormBuilder } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  users:User={
    username: '',
    password: '',
    firstName: '',
    lastName: '',
    address: '',
    country: '',
    email: '',
    phoneNumber: ''
  };
  
  





  constructor(public navCondition: NavigationServiceService,private formbuilder:FormBuilder) {}

  



  form=this.formbuilder.group(
    {username:'',password:'',firstName:'',lastName:'',address:'',country:'',email:'',phoneNumber:''}
  );
  
  sendRegisterData(): void{
    console.log(this.users.username);
    this.users.username=this.form.value.username as string;
    this.users.password=this.form.value.password as string;
    this.users.address=this.form.value.address as string;
    this.users.country=this.form.value.country as string;
    this.users.email=this.form.value.email as string;
    this.users.firstName=this.form.value.firstName as string;
    this.users.lastName=this.form.value.lastName as string;
    this.users.phoneNumber=this.form.value.phoneNumber as string;

    this.navCondition.tryRegister(this.users).subscribe(s=>{});

  }
  
  
  ngOnInit() {
    
    
    
  }

 
  
}
