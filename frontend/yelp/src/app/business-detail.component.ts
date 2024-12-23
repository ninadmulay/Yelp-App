import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BusinessService } from './business.service';
import { Business } from './business';
import { Review } from './business.service'
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-business-detail',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div *ngIf="business"> 
      <h2>{{ business.name }}</h2>
      <p>Rating: {{ business.stars }} stars</p>
      <p>Address: {{ business.address }}, {{ business.city }}, {{ business.state }}</p>

      <h3>Reviews</h3>
      <ul>
        <li *ngFor="let review of reviews">
          <p>{{ review.stars }} stars - {{ review.text }}</p> 
        </li>
      </ul>
    </div>
  `,
  styles: [`
    /* Add component-specific styles if needed */
  `]
})
export class BusinessDetailComponent implements OnInit {
  business: Business | undefined; // Initialize as undefined
  reviews: Review[] = [];

  constructor(
    private route: ActivatedRoute,
    private businessService: BusinessService
  ) { }

ngOnInit() {
const id = Number(this.route.snapshot.paramMap.get('id'));
this.businessService.getBusiness(id)
    .subscribe(business => this.business = business);
this.businessService.getReviews(id)
    .subscribe({
    next: (reviews) => {
        console.log("Reviews received:", reviews);  // Log successful response
        this.reviews = reviews;
    },
    error: (error) => {
        console.error("Error fetching reviews:", error);  // Log detailed error object
    }
    });
  }
}