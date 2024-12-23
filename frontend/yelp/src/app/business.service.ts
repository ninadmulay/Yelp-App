import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Business } from './business';

export interface Review { // Define the Review interface
    id: number;
    business_id: number;
    user_id: number; 
    stars: number;
    text: string;
    date: string; 
  }

@Injectable({
  providedIn: 'root'
})
export class BusinessService {
  private apiUrl = 'http://127.0.0.1:5000/api/businesses'; // Replace with your Flask API URL

  constructor(private http: HttpClient) { }

  getBusinesses(): Observable<Business[]> {
    return this.http.get<Business[]>(this.apiUrl);
  }

  getBusiness(id: number): Observable<Business> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.get<Business>(url);
  }

  getReviews(businessId: number): Observable<Review[]> {
    const url = `${this.apiUrl}/${businessId}/reviews`; // Correct template literal usage
    return this.http.get<Review[]>(url);
  }

  // ... (Add other methods for POST, PUT, DELETE if needed)
}