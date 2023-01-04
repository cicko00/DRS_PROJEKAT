import { Component, OnInit } from '@angular/core';
import { User } from '../models/user.model';
import { NavigationServiceService } from '../services/navigation-service.service';
@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  constructor(private nav:NavigationServiceService){}
 user!: User;
 
  ngOnInit(){
    this.nav.getUserProfile().subscribe(x=>{this.user=x})
    
  }
}
