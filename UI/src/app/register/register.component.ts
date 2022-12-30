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
    password: ''
  };
  
  





  constructor(public navCondition: NavigationServiceService,private formbuilder:FormBuilder) {}

  



  form=this.formbuilder.group(
    {username:'',password:''}
  );
  
  sendRegisterData(): void{
    console.log(this.users.username);
    this.users.username=this.form.value.username as string;
    this.users.password=this.form.value.password as string;
    this.navCondition.tryRegister(this.users).subscribe(s=>{});

  }
  
  
  ngOnInit() {
    
    
    
  }

 
  
}
