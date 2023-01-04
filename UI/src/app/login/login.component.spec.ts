import { Component, OnInit } from '@angular/core';
import { FormBuilder, NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { User_login } from '../models/user.model';
import { NavigationMenuComponent } from '../navigation-menu/navigation-menu.component';
import { NavigationServiceService } from '../services/navigation-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  users:User_login={
    username: '',
    password: '',
    
  };

  constructor(public navCondition: NavigationServiceService,private formbuilder:FormBuilder,private router: Router) {}

  form=this.formbuilder.group(
    {username:'',password:''}
  );

  sendLoginData(): void{
    console.log(this.users.username);
    this.users.username=this.form.value.username as string;
    if(this.users.username.trim()==""){
      window.alert("All fields are required!")
      return;
    }

    this.users.password=this.form.value.password as string;
    if(this.users.password.trim()==""){
      window.alert("All fields are required!")
      return;
    }

    this.navCondition.tryLogin(this.users).subscribe(s=>{
      
      if ((s as string) == "FALSE"){
        window.alert("Incorrect username or password!");
        
      }
      if((s as string)!="FALSE"){
        window.alert("Loggin succesful!");
        
        
        
        this.router.navigate(["/home"])
        this.navCondition.showNoLogin();
        
        
      }
    });



  }
  ngOnInit(){
    
  }

  
  
}