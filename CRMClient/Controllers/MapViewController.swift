//
//  MapViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 2/22/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit
import MapKit
import CoreLocation

class MapViewController: UIViewController, CLLocationManagerDelegate, MKMapViewDelegate {

    @IBOutlet weak var map: MKMapView!
    @IBOutlet weak var textFieldForAdress: UITextField!
    @IBOutlet weak var getDirectionsButton: UIButton!
    
    var locationManager = CLLocationManager()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        locationManager.requestAlwaysAuthorization()
        locationManager.requestWhenInUseAuthorization()
        locationManager.startUpdatingLocation()
        
        map.delegate = self
        
    }

    @IBAction func getDirectionsTapped(_ sender: Any) {
        getAdress()
    }
    
    func getAdress(){
        let geoCoder = CLGeocoder()
        geoCoder.geocodeAddressString(textFieldForAdress.text!){(placemarks, error)
            in
            
            guard let placemarks = placemarks, let location = placemarks.first?.location
                else{
                    print("No Location Found")
                    return
            }
            print(location)
            self.mapThis(destinationCord: location.coordinate)
        }
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: (CLLocation)){
        print(locations)
    }
    
    func mapThis(destinationCord : CLLocationCoordinate2D){
        let souceCordinate = (locationManager.location?.coordinate)!
        
        let soucePlaceMark = MKPlacemark(coordinate: souceCordinate)
        let destPlaceMark = MKPlacemark(coordinate: destinationCord)
        
        let sourceItem = MKMapItem(placemark: soucePlaceMark)
        let destItem = MKMapItem(placemark: destPlaceMark)
        
        let destinationRequest = MKDirections.Request()
        destinationRequest.source = sourceItem
        destinationRequest.destination = destItem
        destinationRequest.transportType = .automobile
        destinationRequest.requestsAlternateRoutes = true
        
        let directions = MKDirections(request: destinationRequest)
        directions.calculate{(response, error) in
            guard let response = response else{
                if let error = error{
                    print("Something is wrong")
                }
                return
            }
            
            let route = response.routes[0]
            self.map.addOverlay(route.polyline)
            self.map.setVisibleMapRect(route.polyline.boundingMapRect, animated: true)
        }
    }
    
    func mapView(_ mapView: MKMapView, rendererFor overlay: MKOverlay) -> MKOverlayRenderer{
        let render = MKPolylineRenderer(overlay: overlay as! MKPolyline)
        render.strokeColor = .blue
        return render
    }
}


