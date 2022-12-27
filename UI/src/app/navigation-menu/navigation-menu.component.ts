import { Component, OnInit } from '@angular/core';
import { NavigationServiceService } from '../services/navigation-service.service';

@Component({
  selector: 'app-navigation-menu',
  templateUrl: './navigation-menu.component.html',
  styleUrls: ['./navigation-menu.component.scss']
})
export class NavigationMenuComponent implements OnInit {

  constructor(public navCondition: NavigationServiceService) {}
  
  ngOnInit() {
    
  }

}
