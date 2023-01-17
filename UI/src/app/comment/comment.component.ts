import { Component, Input } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { Comment } from '../models/comment.model';
import { NavigationServiceService } from '../services/navigation-service.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})
export class CommentComponent {
  @Input() post:any;
  username:any;

  comments:Comment[]=[]

  comment:Comment={
    id:0,
    description:'',
    user:'',
    topic:'',
    likes:0,
    dislikes:0,
    liked:false,
    disliked:false,
    user_id:0,
    topic_id:0,
  };

  constructor(public navCondition: NavigationServiceService,private formbuilder:FormBuilder,private router: Router) {}
  ngOnInit():void  {
    
  }

  form=this.formbuilder.group(
    {description:''});


  sendCommentData(): void{
    this.comment.description=this.form.value.description as string;
    this.comment.topic_id = this.post.id;
    if(this.comment.description.trim()==""){
      window.alert("Description required!")
      return;
    }
    this.navCondition.tryAddComment(this.comment).subscribe(x=>{
      window.alert(x as string);
    });
  }
}
