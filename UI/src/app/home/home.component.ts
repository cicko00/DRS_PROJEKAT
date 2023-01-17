import { Component } from '@angular/core';
import { SelectControlValueAccessor } from '@angular/forms';
import { Router, TitleStrategy } from '@angular/router';
import { of } from 'rxjs';
import { Post } from '../models/post.model';
import { User } from '../models/user.model';
import { NavigationServiceService } from '../services/navigation-service.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  constructor(private navService: NavigationServiceService,
              private router: Router) {}
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
      this.setFalse()

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

  async likePost(id:number){
    if(this.msg == "FALSE")
    {
      this.router.navigate(["/login"])
    }
    const post = this.posts.find(x => x.id === id);
      if(post){
          post.liked=true;
          post.likes++;
          if(post.disliked==true){
            this.undislikePost(id);
            await new Promise(f=>setTimeout(f,80))
          }
          this.navService.tryLike(id).subscribe();
          return;
      } 
  }
  unlikePost(id:number){
    const post = this.posts.find(x => x.id === id);
      if(post){
        post.liked=false;
        post.likes--
        this.navService.tryunLike(id).subscribe()
        return;
      }
  }

  async dislikePost(id:number){
    if(this.msg == "FALSE")
    {
      this.router.navigate(["/login"])
    }
    const post = this.posts.find(x => x.id === id);
      if(post){
          post.disliked=true;
          post.dislikes++;
          if(post.liked==true){
            this.unlikePost(id);
            await new Promise(f=>setTimeout(f,80))
          }
          this.navService.tryDislike(id).subscribe();
          return;
        
      }
  }
  undislikePost(id:number){
    const post = this.posts.find(x => x.id === id);
      if(post){
        post.disliked=false;
        post.dislikes--
        this.navService.tryunDislike(id).subscribe()
      }
  }

setFalse(){
  const { likedTopic, unlikedTopic, interests } = this.msg;

  this.posts.forEach(post => {
    post.liked = likedTopic.includes(post.id);
    post.disliked = unlikedTopic.includes(post.id);
    post.notified = interests.includes(post.id);
    
  });
  }

notifyPost(id:any){

  if(this.msg == "FALSE")
  {
    this.router.navigate(["/login"])
    return
  }
const User = this.msg;
const post = this.posts.find(x => x.id === id)
   if(post){

   if(post.notified==false)
        {post.notified=true;
          this.navService.tryNotify(id).subscribe()
          return}
   
        else{
          post.notified=false;
          this.navService.tryUnnotify(id).subscribe()
           return
       }
  
       } 
      }
   




 
}






