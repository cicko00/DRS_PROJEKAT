import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { User } from '../models/user.model';

@Injectable({
  providedIn: 'root'
})
export class NavigationServiceService {
  dashboard: boolean;
  topics: boolean;
  sign: boolean;

  constructor( private http: HttpClient) {
    this.dashboard = false;
    this.topics = false;
    this.sign = true;
   }
   home(): Observable<User[]>{
    const users = this.http.get<User[]>('http://127.0.0.1:5000/home');
    return users;
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
