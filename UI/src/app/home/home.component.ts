import { Component } from '@angular/core';
import { Post } from '../models/post.model';
import { User } from '../models/user.model';
import { NavigationServiceService } from '../services/navigation-service.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  constructor(private navService: NavigationServiceService) {}
  posts:Post[]=[]
  
  ngOnInit(): void {
    this.navService.getUserProfile().subscribe(x=>{
      this.msg=x;
      if(this.msg!="FALSE"){
        this.loggedIn=true;
        this.navService.showNoLogin()
      }

      this.home()

     });
  }
  home(): void{
    this.navService.home()
    .subscribe(x => {
      console.log(x);
      this.posts = x;
    })
  }

  msg:any;
  show:boolean=false;
  loggedIn:boolean=false;

  ShowAddPost(){
    if(this.show==true){
      this.show=false;
    }
    else{
      this.show=true;
    }
  }

  likePost(id:number){
    this.navService.tryLike(id).subscribe();
    
    
  }

  dislikePost(id:number){
    this.navService.tryDislike(id).subscribe()
    
    
  }


}
