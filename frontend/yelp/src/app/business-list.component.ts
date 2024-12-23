import { Component, OnInit } from '@angular/core';
import { BusinessService } from './business.service';
import { Business } from './business';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-business-list',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <ul>
      <li *ngFor="let business of businesses">
        <a [routerLink]="['/businesses', business.id]">
          {{ business.name }} ({{ business.stars }} stars)
        </a>
      </li>
    </ul>
  `,
  styles: [`
    /* Add component-specific styles if needed */
  `]
})
export class BusinessListComponent implements OnInit {
  businesses: Business[] = [];

  constructor(private businessService: BusinessService) { }

  ngOnInit() {
    this.businessService.getBusinesses()
      .subscribe(businesses => this.businesses = businesses);
  }
}