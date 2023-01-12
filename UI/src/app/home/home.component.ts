import { Component } from '@angular/core';
import { SelectControlValueAccessor } from '@angular/forms';
import { TitleStrategy } from '@angular/router';
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

  likePost(id:number){
    var canexecute=this.navService.tryLike(id)
    var undislike=this.navService.tryunDislike(id)
    var unlike=this.navService.tryunLike(id)
    this.posts.forEach(function(post){
      
      if(post.id==id){
        
        if(post.liked==false){
          post.liked=true;
          post.likes=post.likes+1;
          if(post.disliked==true){
            undislike.subscribe()
            post.disliked=false;
            post.dislikes=post.dislikes-1;
          }
          canexecute.subscribe();
         
          
          return;
        }
        else{
          post.liked=false;
          post.likes=post.likes-1
          unlike.subscribe()
        }
      }
    })

    
    

    
    
    
  }

  dislikePost(id:number){
    var canexecute=this.navService.tryDislike(id);

    var unlike=this.navService.tryunLike(id);
    var undislike=this.navService.tryunDislike(id);

    this.posts.forEach(function(post){
      
      if(post.id==id){
        
        if(post.disliked==false){
         
          post.disliked=true;
          post.dislikes=post.dislikes+1;
          if(post.liked==true){
            unlike.subscribe()
            post.liked=false;
            post.likes=post.likes-1;
          }
          canexecute.subscribe();
          return;
        }
        else{
          post.disliked=false;
          post.dislikes=post.dislikes-1
          undislike.subscribe()
        }
      }
    })

   

    
    
  }

setFalse(){

    var object=this.msg;
    var likedList=object.likedTopic;
    var dislikedList=object.unlikedTopic;
    console.log(object)

    this.posts.forEach(function(post){

      

      console.log(post)

      if(likedList.includes(post.id)){
        post.liked=true;
      }
      else{
        post.liked=false;
      }

      if(dislikedList.includes(post.id)){
        post.disliked=true;
      }
      else{
        post.disliked=false;
      }
      
    })
  }
  


}
