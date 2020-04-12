//
//  Model.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 3/8/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import Foundation

struct UserInfo: Codable {
    let user: User
    let first_name, last_name, gender, dateOfBirth, phone: String
 
}

struct TokenInfo: Codable {
    let user: Token
    let first_name, last_name, gender, dateOfBirth: String
    let phone: String
    
}

// MARK: - User
struct User: Codable {
    let username, email: String
    let password: String
}

struct Token: Codable{
    let username, email: String
    let token: String
}


struct LogInfo: Codable {
    let username, password: String
}

struct TokInfo: Codable {
    let username, token: String
}

// MARK: - CreateOrder
struct CreateOrder: Codable {
    let name: String
    let price_client: Int
    let requirements_loading: String
    let type_cargo, type_auto, auto_releaseyear, type_loading: Int
    let state_awning: StateAwning
    let weight, weight_measurementunit: Int
    let volume: Volume
    let location_cargo: LocationCargo
}

// MARK: - LocationCargo
struct LocationCargo: Codable {
    let address: String
}

// MARK: - StateAwning
struct StateAwning: Codable {
    let no_holes, no_gaps, dry, no_patches: Bool
}

// MARK: - Volume
struct Volume: Codable {
    let width, height, length, unit: Int
}
