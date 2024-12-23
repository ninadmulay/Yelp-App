import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BusinessService, Review } from './business.service';

@Component({
  selector: 'app-reviews',
  standalone: true,
  imports: [CommonModule],
  template: `
    <h3>All Reviews</h3>
    <ul>
      <li *ngFor="let review of allReviews">
        <p>
          <strong>{{ review.stars }} stars</strong> - {{ review.text }}
          <br>
          <small>For Business ID: {{ review.business_id }}</small> 
          <small>By User ID: {{ review.user_id }}</small> 
        </p>
      </li>
    </ul>
  `,
  styles: [`
    /* Add component-specific styles if needed */
  `]
})
export class ReviewsComponent implements OnInit {
  allReviews: Review[] = [];

  constructor(private businessService: BusinessService) { }

  ngOnInit(): void {
    this.fetchAllReviews();
  }

  fetchAllReviews() {
    this.businessService.getBusinesses().subscribe(businesses => {
      businesses.forEach(business => {
        this.businessService.getReviews(business.id).subscribe(reviews => {
          this.allReviews.push(...reviews); 
        });
      });
    });
  }
}
