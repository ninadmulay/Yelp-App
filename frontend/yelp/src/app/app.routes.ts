import { Routes } from '@angular/router';
import { HomeComponent } from './home.component';
import { BusinessListComponent } from './business-list.component';
import { BusinessDetailComponent } from './business-detail.component';
import { ReviewsComponent } from './reviews.component';
//import { TestdbComponent } from './testdb/testdb.component';

export const appRoutes: Routes = [
  { path: '', component: HomeComponent }, // This will be your home page
  { path: 'businesses', component: BusinessListComponent },
  { path: 'businesses/:id', component: BusinessDetailComponent },
  { path: 'reviews', component: ReviewsComponent }
  //{ path: 'testdb', component: TestdbComponent }
];