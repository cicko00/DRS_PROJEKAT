import { Component } from '@angular/core';
import { User } from '../models/user.model';
import { NavigationServiceService } from '../services/navigation-service.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  constructor(private navService: NavigationServiceService) {}
  users: User [] = [];
  
  ngOnInit(): void {
    this.home();
  }
  home(): void{
    this.navService.home()
    .subscribe(x => {
      console.log(x);
      this.users = x;
    })
  }

}
