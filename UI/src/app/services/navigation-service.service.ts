import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class NavigationServiceService {
  dashboard: boolean;
  topics: boolean;
  sign: boolean;

  constructor() {
    this.dashboard = false;
    this.topics = false;
    this.sign = true;
   }
   showLogin() {
    this.dashboard = true;
    this.topics = true;
    this.sign = false;
  }

  shownonLogin() {
    this.dashboard = false;
    this.topics = false;
    this.sign = true;
  }
}
