import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { NavigationServiceService } from '../services/navigation-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  errorMessage = 'none';
  sucessMessage = 'none';
  errorMsg = '';

  constructor(private nav: NavigationServiceService, private route: Router) { }

  ngOnInit(){
    this.nav.shownonLogin();
  }

  passVal($f: NgForm) {
    console.log($f.value)
    if (!$f.value.password || !$f.value.username) {
      this.errorMessage = 'block';
      this.sucessMessage = 'none';
      this.errorMsg = 'Both Password and Username are required.!';
    }
    if ($f.value.password && $f.value.username) {
      if ($f.value.username === 'test' && $f.value.password === 'test') {
        this.errorMessage = 'none';
        this.sucessMessage = 'block';
        this.route.navigateByUrl('/Dashboard');
      } else {
        this.errorMessage = 'block';
        this.sucessMessage = 'none';
        this.errorMsg = 'Either Password or Username is incorrect.!';
      }
    }
  }
}
