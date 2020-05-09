//
//  DriverMyOrderViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 5/9/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class DriverMyOrderViewController: UIViewController, UITableViewDelegate, UITableViewDataSource{
    
    var orders : [DriverOrderStruct] = []
        var refresher: UIRefreshControl!
    
    @IBOutlet weak var tableView: UITableView!
    override func viewDidLoad() {
        super.viewDidLoad()
        
        refresher = UIRefreshControl()
        refresher.addTarget(self, action: #selector(CurrentOrdersViewController.refresh), for: UIControl.Event.valueChanged)
        tableView.addSubview(refresher)
        
        ServerManager.shared.getDriverMyOrderList(token: UserDefaults.standard.value(forKey: "token") as! String, { (ordersList) in
             self.orders = ordersList
             self.tableView.reloadData()
         })
         {(error) in print(error)}
    }
        
        @objc func refresh(){
            refresher.endRefreshing()
            tableView.reloadData()
        }

    
       func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
            return orders.count
        }

        func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
            let order = orders[indexPath.row]
            let cell = tableView.dequeueReusableCell(withIdentifier: "DriverOrdersCell", for: indexPath) as! DriverOrdersCell
            cell.configure(orders:[order])
            
            return cell
        }

        func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
            let order = orders[indexPath.row]
            print(order.name)
            let storyboard = UIStoryboard(name: "Main", bundle: nil)

            if let detailsViewController = storyboard.instantiateViewController(withIdentifier: "DetailDR") as? DriverDetailsViewController{
    //            UserDefaults.standard.set(orders[0].id, forKey: "id")
    //            print(UserDefaults.value(forKey: "id"))
                detailsViewController.configure(orders:[order])
                detailsViewController.modalPresentationStyle = .fullScreen
                present(detailsViewController, animated: false, completion: nil)
            }
        }
    }
        


