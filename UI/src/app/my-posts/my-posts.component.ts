import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NavigationServiceService } from '../services/navigation-service.service';

@Component({
  selector: 'app-my-posts',
  templateUrl: './my-posts.component.html',
  styleUrls: ['./my-posts.component.scss']
})


export class MyPostsComponent implements OnInit {
  msg:any;
  constructor(private nav:NavigationServiceService,private router:Router){}
  ngOnInit() {
    this.nav.getUserProfile().subscribe(x=>{
      this.msg=x;
      if(this.msg=='FALSE'){
        this.router.navigate(["/home"])
      }
    })
  }
  show:boolean=false;

  ShowAddPost(){
    if(this.show==true){
      this.show=false;
    }
    else{
      this.show=true;
    }
  }


 






}