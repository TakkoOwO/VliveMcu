"""
Module: 'espidf' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

SPI3_HOST: int = 2
HSPI_HOST: int = 1
VSPI_HOST: int = 2
SPI2_HOST: int = 1
SPI_HOST: int = 0
SPI1_HOST: int = 0
I2S_PIN_NO_CHANGE: int = -1
portMAX_DELAY: int = -1
def multi_heap_set_lock(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_if_from_esp_netif(*args, **kwargs) -> Incomplete:
    ...

def esp_clk_slowclk_cal_get(*args, **kwargs) -> Incomplete:
    ...

def pcnt_set_filter_value(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_set_header(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_txt_item_remove(*args, **kwargs) -> Incomplete:
    ...

def i2s_start(*args, **kwargs) -> Incomplete:
    ...

def esp_base_mac_addr_set(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_create_ip6_linklocal(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_malloc(*args, **kwargs) -> Incomplete:
    ...

def dhcps_start(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_set_timeout_ms(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_port_set_for_host(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_is_complete_data_received(*args, **kwargs) -> Incomplete:
    ...

def esp_clk_rtc_time(*args, **kwargs) -> Incomplete:
    ...

def i2s_driver_install(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_check_integrity(*args, **kwargs) -> Incomplete:
    ...

def esp_log_level_set(*args, **kwargs) -> Incomplete:
    ...

def adc2_get_raw(*args, **kwargs) -> Incomplete:
    ...

def gpio_install_isr_service(*args, **kwargs) -> Incomplete:
    ...

def xPortGetCoreID(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_get_free_size(*args, **kwargs) -> Incomplete:
    ...

def spi_device_polling_start(*args, **kwargs) -> Incomplete:
    ...

def esp_reset_reason(*args, **kwargs) -> Incomplete:
    ...

def mdns_query_a(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_ap_start(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_dhcpc_get_status(*args, **kwargs) -> Incomplete:
    ...

def mdns_handle_system_event(*args, **kwargs) -> Incomplete:
    ...

def gpio_isr_handler_remove(*args, **kwargs) -> Incomplete:
    ...

def sntp_get_sync_interval(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_get_sta_list(*args, **kwargs) -> Incomplete:
    ...

def spi_device_polling_transmit(*args, **kwargs) -> Incomplete:
    ...

def dhcps_set_option_info(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_sta_input(*args, **kwargs) -> Incomplete:
    ...

def adc_digi_start(*args, **kwargs) -> Incomplete:
    ...

def gpio_get_drive_capability(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_txt_item_remove_for_host(*args, **kwargs) -> Incomplete:
    ...

def mdns_init(*args, **kwargs) -> Incomplete:
    ...

def i2s_set_pdm_tx_up_sample(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_sta_start(*args, **kwargs) -> Incomplete:
    ...

def pcnt_filter_disable(*args, **kwargs) -> Incomplete:
    ...

def adc_power_on(*args, **kwargs) -> Incomplete:
    ...

def gpio_pad_pulldown(*args, **kwargs) -> Incomplete:
    ...

def esp_get_idf_version(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_get_info(*args, **kwargs) -> Incomplete:
    ...

def gpio_matrix_in(*args, **kwargs) -> Incomplete:
    ...

def gpio_intr_ack(*args, **kwargs) -> Incomplete:
    ...

def esp_get_free_heap_size(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_get_netif_index(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_aligned_free(*args, **kwargs) -> Incomplete:
    ...

def gpio_sleep_sel_dis(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_port_set(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_get_netif(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_remove(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_check(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_aligned_free(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_get_info(*args, **kwargs) -> Incomplete:
    ...

def mdns_query_ptr(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_read(*args, **kwargs) -> Incomplete:
    ...

def gpio_sleep_set_direction(*args, **kwargs) -> Incomplete:
    ...

def http_parser_url_init(*args, **kwargs) -> Incomplete:
    ...

def gpio_set_level(*args, **kwargs) -> Incomplete:
    ...

def i2s_read(*args, **kwargs) -> Incomplete:
    ...

def esp_rom_install_uart_printf(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_clear_default_eth_handlers(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_realloc(*args, **kwargs) -> Incomplete:
    ...

def gpio_output_set(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_action_connected(*args, **kwargs) -> Incomplete:
    ...

def adc_digi_deinitialize(*args, **kwargs) -> Incomplete:
    ...

def gpio_reset_pin(*args, **kwargs) -> Incomplete:
    ...

def esp_efuse_mac_get_default(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_txt_set(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_get_sta_list(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_get_handle_from_ifkey(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_txt_item_set_with_explicit_value_len(*args, **kwargs) -> Incomplete:
    ...

def esp_unregister_shutdown_handler(*args, **kwargs) -> Incomplete:
    ...

def spi_device_polling_end(*args, **kwargs) -> Incomplete:
    ...

def gpio_force_unhold_all(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_get_chunk_length(*args, **kwargs) -> Incomplete:
    ...

def task_delay_ms(*args, **kwargs) -> Incomplete:
    ...

def esp_rom_get_reset_reason(*args, **kwargs) -> Incomplete:
    ...

def pcnt_get_counter_value(*args, **kwargs) -> Incomplete:
    ...

def ex_spi_pre_cb_isr(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_set_ip_info(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_aligned_alloc(*args, **kwargs) -> Incomplete:
    ...

def gpio_set_pull_mode(*args, **kwargs) -> Incomplete:
    ...

def adc2_config_channel_atten(*args, **kwargs) -> Incomplete:
    ...

def esp_read_mac(*args, **kwargs) -> Incomplete:
    ...

def esp_derive_local_mac(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_clear_default_wifi_handlers(*args, **kwargs) -> Incomplete:
    ...

def pcnt_isr_handler_add(*args, **kwargs) -> Incomplete:
    ...

def gpio_pad_pullup(*args, **kwargs) -> Incomplete:
    ...

def esp_log_buffer_char_internal(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_dhcps_stop(*args, **kwargs) -> Incomplete:
    ...

def gpio_intr_disable(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_malloc_extmem_enable(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_get_header(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_check_integrity_all(*args, **kwargs) -> Incomplete:
    ...

def mdns_query_srv(*args, **kwargs) -> Incomplete:
    ...

def dhcps_router_enabled(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_free_size(*args, **kwargs) -> Incomplete:
    ...

def http_parser_version(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_action_leave_ip6_multicast_group(*args, **kwargs) -> Incomplete:
    ...

def mdns_query_txt(*args, **kwargs) -> Incomplete:
    ...

def gpio_pad_hold(*args, **kwargs) -> Incomplete:
    ...

def mdns_delegate_hostname_remove(*args, **kwargs) -> Incomplete:
    ...

def i2s_set_sample_rates(*args, **kwargs) -> Incomplete:
    ...

def i2s_pcm_config(*args, **kwargs) -> Incomplete:
    ...

def adc_vref_to_gpio(*args, **kwargs) -> Incomplete:
    ...

def esp_efuse_mac_get_custom(*args, **kwargs) -> Incomplete:
    ...

def adc_digi_read_bytes(*args, **kwargs) -> Incomplete:
    ...

def pcnt_isr_service_uninstall(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_perform(*args, **kwargs) -> Incomplete:
    ...

def ip4_addr_isbroadcast_u32(*args, **kwargs) -> Incomplete:
    ...

def mdns_instance_name_set(*args, **kwargs) -> Incomplete:
    ...

def memcpy(*args, **kwargs) -> Incomplete:
    ...

def esp_clk_cpu_freq(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_get_password(*args, **kwargs) -> Incomplete:
    ...

def ip6addr_aton(*args, **kwargs) -> Incomplete:
    ...

def adc_power_release(*args, **kwargs) -> Incomplete:
    ...

def spi_device_release_bus(*args, **kwargs) -> Incomplete:
    ...

def gpio_pad_select_gpio(*args, **kwargs) -> Incomplete:
    ...

def gpio_set_direction(*args, **kwargs) -> Incomplete:
    ...

def dhcps_dns_enabled(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_exists(*args, **kwargs) -> Incomplete:
    ...

def esp_get_minimum_free_heap_size(*args, **kwargs) -> Incomplete:
    ...

def http_errno_name(*args, **kwargs) -> Incomplete:
    ...

def adc2_vref_to_gpio(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_get_status_code(*args, **kwargs) -> Incomplete:
    ...

def gpio_pulldown_dis(*args, **kwargs) -> Incomplete:
    ...

def mdns_hostname_exists(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_get_errno(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_remove_for_host(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_get_largest_free_block(*args, **kwargs) -> Incomplete:
    ...

def adc_set_data_width(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_deinit(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_set_dns_info(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_dhcps_get_status(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_get_ip_info(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_set_old_ip_info(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_action_add_ip6_address(*args, **kwargs) -> Incomplete:
    ...

def gpio_set_drive_capability(*args, **kwargs) -> Incomplete:
    ...

def sntp_get_system_time(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_dump(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_txt_item_set_for_host_with_explicit_value_len(*args, **kwargs) -> Incomplete:
    ...

def dhcps_set_new_lease_cb(*args, **kwargs) -> Incomplete:
    ...

def esp_log_set_vprintf(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_get_dns_info(*args, **kwargs) -> Incomplete:
    ...

def spi_device_acquire_bus(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_set_hostname(*args, **kwargs) -> Incomplete:
    ...

def mdns_delegate_hostname_add(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_flush_response(*args, **kwargs) -> Incomplete:
    ...

def gpio_deep_sleep_hold_dis(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_get_ip6_linklocal(*args, **kwargs) -> Incomplete:
    ...

def esp_log_buffer_hexdump_internal(*args, **kwargs) -> Incomplete:
    ...

def mdns_hostname_set(*args, **kwargs) -> Incomplete:
    ...

def gpio_pad_set_drv(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_read_response(*args, **kwargs) -> Incomplete:
    ...

def pcnt_set_mode(*args, **kwargs) -> Incomplete:
    ...

def esp_ip4addr_aton(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_eth_input(*args, **kwargs) -> Incomplete:
    ...

def gpio_hold_dis(*args, **kwargs) -> Incomplete:
    ...

def ili9xxx_flush(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_down(*args, **kwargs) -> Incomplete:
    ...

def lwip_strnicmp(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_netstack_buf_ref(*args, **kwargs) -> Incomplete:
    ...

def http_parser_parse_url(*args, **kwargs) -> Incomplete:
    ...

def gpio_pullup_dis(*args, **kwargs) -> Incomplete:
    ...

def spi_bus_free(*args, **kwargs) -> Incomplete:
    ...

def gpio_input_get_high(*args, **kwargs) -> Incomplete:
    ...

def gpio_hold_en(*args, **kwargs) -> Incomplete:
    ...

def ip4addr_aton(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_add_for_host(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_get_post_field(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_delete_header(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_dump(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_instance_name_set(*args, **kwargs) -> Incomplete:
    ...

def gpio_get_level(*args, **kwargs) -> Incomplete:
    ...

def gpio_sleep_sel_en(*args, **kwargs) -> Incomplete:
    ...

def adc1_get_raw(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_cleanup(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_free(*args, **kwargs) -> Incomplete:
    ...

def pcnt_counter_resume(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_set_url(*args, **kwargs) -> Incomplete:
    ...

def gpio_intr_pending(*args, **kwargs) -> Incomplete:
    ...

def gpio_pad_unhold(*args, **kwargs) -> Incomplete:
    ...

def esp_err_to_name(*args, **kwargs) -> Incomplete:
    ...

def dhcp_ip_addr_restore(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_get_nr_of_ifs(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_fetch_headers(*args, **kwargs) -> Incomplete:
    ...

def pcnt_get_event_status(*args, **kwargs) -> Incomplete:
    ...

def i2s_write_expand(*args, **kwargs) -> Incomplete:
    ...

def gpio_sleep_set_pull_mode(*args, **kwargs) -> Incomplete:
    ...

def pcnt_set_event_value(*args, **kwargs) -> Incomplete:
    ...

def esp_clk_slowclk_cal_set(*args, **kwargs) -> Incomplete:
    ...

def sntp_set_system_time(*args, **kwargs) -> Incomplete:
    ...

def pcnt_isr_unregister(*args, **kwargs) -> Incomplete:
    ...

def spi_device_queue_trans(*args, **kwargs) -> Incomplete:
    ...

def i2s_set_pdm_rx_down_sample(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_action_join_ip6_multicast_group(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_action_start(*args, **kwargs) -> Incomplete:
    ...

def esp_clk_apb_freq(*args, **kwargs) -> Incomplete:
    ...

def mdns_query(*args, **kwargs) -> Incomplete:
    ...

def gpio_output_set_high(*args, **kwargs) -> Incomplete:
    ...

def pcnt_isr_handler_remove(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_register_failed_alloc_callback(*args, **kwargs) -> Incomplete:
    ...

def ip4_addr_netmask_valid(*args, **kwargs) -> Incomplete:
    ...

def esp_rom_delay_us(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_get_hostname(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_get_ip6_global(*args, **kwargs) -> Incomplete:
    ...

def gpio_wakeup_disable(*args, **kwargs) -> Incomplete:
    ...

def pcnt_set_pin(*args, **kwargs) -> Incomplete:
    ...

def SPH0645_WORKAROUND(*args, **kwargs) -> Incomplete:
    ...

def ex_spi_post_cb_isr(*args, **kwargs) -> Incomplete:
    ...

def gpio_pad_input_enable(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_register(*args, **kwargs) -> Incomplete:
    ...

def gpio_isr_register(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_init(*args, **kwargs) -> Incomplete:
    ...

def esp_log_early_timestamp(*args, **kwargs) -> Incomplete:
    ...

def get_ccount(*args, **kwargs) -> Incomplete:
    ...

def adc_power_acquire(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_is_chunked_response(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_set_password(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_get_minimum_free_size(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_netstack_buf_free(*args, **kwargs) -> Incomplete:
    ...

def esp_fill_random(*args, **kwargs) -> Incomplete:
    ...

def http_method_str(*args, **kwargs) -> Incomplete:
    ...

def gpio_matrix_out(*args, **kwargs) -> Incomplete:
    ...

def http_errno_description(*args, **kwargs) -> Incomplete:
    ...

def pcnt_isr_service_install(*args, **kwargs) -> Incomplete:
    ...

def pcnt_get_event_value(*args, **kwargs) -> Incomplete:
    ...

def memset(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_get_content_length(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_action_remove_ip6_address(*args, **kwargs) -> Incomplete:
    ...

def adc1_config_width(*args, **kwargs) -> Incomplete:
    ...

def i2s_stop(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_check_integrity_addr(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_add(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_free(*args, **kwargs) -> Incomplete:
    ...

def gpio_isr_handler_add(*args, **kwargs) -> Incomplete:
    ...

def spi_cal_clock(*args, **kwargs) -> Incomplete:
    ...

def i2s_write(*args, **kwargs) -> Incomplete:
    ...

def dhcp_search_ip_on_mac(*args, **kwargs) -> Incomplete:
    ...

def esp_log_timestamp(*args, **kwargs) -> Incomplete:
    ...

def lwip_stricmp(*args, **kwargs) -> Incomplete:
    ...

def pcnt_filter_enable(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_str_to_ip4(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_get_old_ip_info(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_str_to_ip6(*args, **kwargs) -> Incomplete:
    ...

def spi_get_actual_clock(*args, **kwargs) -> Incomplete:
    ...

def gpio_uninstall_isr_service(*args, **kwargs) -> Incomplete:
    ...

def gpio_pin_wakeup_enable(*args, **kwargs) -> Incomplete:
    ...

def esp_log_level_get(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_is_netif_up(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_print_heap_info(*args, **kwargs) -> Incomplete:
    ...

def gpio_set_intr_type(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_set_authtype(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_instance_name_set_for_host(*args, **kwargs) -> Incomplete:
    ...

def gpio_intr_enable(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_action_stop(*args, **kwargs) -> Incomplete:
    ...

def adc1_config_channel_atten(*args, **kwargs) -> Incomplete:
    ...

def esp_random(*args, **kwargs) -> Incomplete:
    ...

def adc_set_data_inv(*args, **kwargs) -> Incomplete:
    ...

def lwip_itoa(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_get_username(*args, **kwargs) -> Incomplete:
    ...

def i2s_driver_uninstall(*args, **kwargs) -> Incomplete:
    ...

def esp_err_to_name_r(*args, **kwargs) -> Incomplete:
    ...

def pcnt_isr_register(*args, **kwargs) -> Incomplete:
    ...

def gpio_init(*args, **kwargs) -> Incomplete:
    ...

def adc2_pad_get_io_num(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_ap_input(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_get_esp_if(*args, **kwargs) -> Incomplete:
    ...

def vPortCleanUpTCB(*args, **kwargs) -> Incomplete:
    ...

def gpio_input_get(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_dhcpc_stop(*args, **kwargs) -> Incomplete:
    ...

def esp_register_shutdown_handler(*args, **kwargs) -> Incomplete:
    ...

def dhcps_dns_setserver(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_set_username(*args, **kwargs) -> Incomplete:
    ...

def gpio_pulldown_en(*args, **kwargs) -> Incomplete:
    ...

def esp_log_buffer_hex_internal(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_realloc(*args, **kwargs) -> Incomplete:
    ...

def dhcps_dns_getserver(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_remove_all(*args, **kwargs) -> Incomplete:
    ...

def spi_bus_add_device(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_dump_all(*args, **kwargs) -> Incomplete:
    ...

def adc1_ulp_enable(*args, **kwargs) -> Incomplete:
    ...

def pcnt_get_filter_value(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_set_default_wifi_handlers(*args, **kwargs) -> Incomplete:
    ...

def gpio_iomux_in(*args, **kwargs) -> Incomplete:
    ...

def dhcps_option_info(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_open(*args, **kwargs) -> Incomplete:
    ...

def adc_power_off(*args, **kwargs) -> Incomplete:
    ...

def lwip_strnstr(*args, **kwargs) -> Incomplete:
    ...

def i2s_zero_dma_buffer(*args, **kwargs) -> Incomplete:
    ...

def adc_digi_stop(*args, **kwargs) -> Incomplete:
    ...

def adc1_pad_get_io_num(*args, **kwargs) -> Incomplete:
    ...

def dhcps_stop(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_set_method(*args, **kwargs) -> Incomplete:
    ...

def esp_get_free_internal_heap_size(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_dhcps_start(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_set_redirection(*args, **kwargs) -> Incomplete:
    ...

def gpio_wakeup_enable(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_malloc(*args, **kwargs) -> Incomplete:
    ...

def lwip_htons(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_dhcps_option(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_add_auth(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_get_transport_type(*args, **kwargs) -> Incomplete:
    ...

def lwip_htonl(*args, **kwargs) -> Incomplete:
    ...

def esp_restart(*args, **kwargs) -> Incomplete:
    ...

def spi_device_transmit(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_action_got_ip(*args, **kwargs) -> Incomplete:
    ...

def i2s_set_clk(*args, **kwargs) -> Incomplete:
    ...

def pcnt_counter_pause(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_up(*args, **kwargs) -> Incomplete:
    ...

def pcnt_event_enable(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_aligned_alloc(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_txt_item_set_for_host(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_stop(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_get_total_size(*args, **kwargs) -> Incomplete:
    ...

def gpio_intr_handler_register(*args, **kwargs) -> Incomplete:
    ...

def ipaddr_aton(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_aligned_calloc(*args, **kwargs) -> Incomplete:
    ...

def dhcp_ip_addr_erase(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_calloc(*args, **kwargs) -> Incomplete:
    ...

def gpio_pullup_en(*args, **kwargs) -> Incomplete:
    ...

def gpio_iomux_out(*args, **kwargs) -> Incomplete:
    ...

def dhcp_ip_addr_store(*args, **kwargs) -> Incomplete:
    ...

def spi_transaction_set_cb(*args, **kwargs) -> Incomplete:
    ...

def esp_rom_install_channel_putc(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_set_default_eth_handlers(*args, **kwargs) -> Incomplete:
    ...

def pcnt_intr_enable(*args, **kwargs) -> Incomplete:
    ...

def spi_bus_initialize(*args, **kwargs) -> Incomplete:
    ...

def pcnt_counter_clear(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_txt_item_set(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_action_disconnected(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_eth_start(*args, **kwargs) -> Incomplete:
    ...

def uxTaskPriorityGet(*args, **kwargs) -> Incomplete:
    ...

def adc_set_clk_div(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_dhcpc_start(*args, **kwargs) -> Incomplete:
    ...

def pcnt_event_disable(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_set_post_field(*args, **kwargs) -> Incomplete:
    ...

def gpio_intr_ack_high(*args, **kwargs) -> Incomplete:
    ...

def tcpip_adapter_dhcpc_option(*args, **kwargs) -> Incomplete:
    ...

def esp_base_mac_addr_get(*args, **kwargs) -> Incomplete:
    ...

def esp_clk_xtal_freq(*args, **kwargs) -> Incomplete:
    ...

def i2s_set_pin(*args, **kwargs) -> Incomplete:
    ...

def ili9xxx_post_cb_isr(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_write(*args, **kwargs) -> Incomplete:
    ...

def esp_netif_init(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_minimum_free_size(*args, **kwargs) -> Incomplete:
    ...

def gpio_force_hold_all(*args, **kwargs) -> Incomplete:
    ...

def mdns_query_aaaa(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_txt_set_for_host(*args, **kwargs) -> Incomplete:
    ...

def spi_bus_remove_device(*args, **kwargs) -> Incomplete:
    ...

def mdns_query_async_new(*args, **kwargs) -> Incomplete:
    ...

def mdns_service_exists_with_instance(*args, **kwargs) -> Incomplete:
    ...

def pcnt_intr_disable(*args, **kwargs) -> Incomplete:
    ...

def esp_log_system_timestamp(*args, **kwargs) -> Incomplete:
    ...

def heap_caps_get_allocated_size(*args, **kwargs) -> Incomplete:
    ...

def i2s_get_clk(*args, **kwargs) -> Incomplete:
    ...

def gpio_intr_pending_high(*args, **kwargs) -> Incomplete:
    ...

def gpio_deep_sleep_hold_en(*args, **kwargs) -> Incomplete:
    ...

def spi_device_get_trans_result(*args, **kwargs) -> Incomplete:
    ...

def mdns_free(*args, **kwargs) -> Incomplete:
    ...

def multi_heap_get_allocated_size(*args, **kwargs) -> Incomplete:
    ...

def ipaddr_addr(*args, **kwargs) -> Incomplete:
    ...

def spi_get_timing(*args, **kwargs) -> Incomplete:
    ...

def spi_get_freq_limit(*args, **kwargs) -> Incomplete:
    ...

def gpio_pin_wakeup_disable(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_close(*args, **kwargs) -> Incomplete:
    ...

def esp_http_client_get_url(*args, **kwargs) -> Incomplete:
    ...

def esp_system_abort(*args, **kwargs) -> Incomplete:
    ...


class SH2LIB_DATA_RECV():
    NONE: int = 0
    RST_STREAM: int = 1
    FRAME_COMPLETE: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_netif_config_t():
    def new(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class pcnt_config_t():
    def unit_config(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_IP6_ADDR_IS():
    UNKNOWN: int = 0
    LINK_LOCAL: int = 2
    IPV4_MAPPED_IPV6: int = 5
    GLOBAL: int = 1
    UNIQUE_LOCAL: int = 4
    SITE_LOCAL: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_NUM():
    _1: int = 1
    MAX: int = 2
    _0: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ETH_LINK():
    UP: int = 0
    DOWN: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ip_addr_u_addr_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_IF():
    AP: int = 1
    STA: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_chip_info_t():
    def info(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class tcpip_adapter_ip_info_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_ARB_MODE():
    FIX: int = 1
    SHIELD: int = 0
    LOOP: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_tls():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_UNIT():
    _1: int = 1
    ALTER: int = 7
    MAX: int = 8
    _2: int = 2
    BOTH: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class PCNT_EVT():
    THRES_1: int = 4
    L_LIM: int = 16
    MAX: int = 65
    H_LIM: int = 32
    THRES_0: int = 8
    ZERO: int = 64
    def __init__(self, *argv, **kwargs) -> None:
        ...


class _lv_mp_int_wrapper():
    def __init__(self, *argv, **kwargs) -> None:
        ...

esp_log_default_level: Incomplete ## <class '_lv_mp_int_wrapper'> = struct _lv_mp_int_wrapper
_nesting: Incomplete ## <class '_lv_mp_int_wrapper'> = struct _lv_mp_int_wrapper

class mdns_ip_addr_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class EMAC():
    CLK_IN_GPIO: int = 0
    APPL_CLK_OUT_GPIO: int = 0
    CLK_OUT_180_GPIO: int = 17
    CLK_OUT_GPIO: int = 16
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S():
    TDM_ACTIVE_CH5: int = 2097152
    TDM_ACTIVE_CH6: int = 4194304
    TDM_ACTIVE_CH7: int = 8388608
    TDM_ACTIVE_CH8: int = 16777216
    TDM_ACTIVE_CH0: int = 65536
    TDM_ACTIVE_CH4: int = 1048576
    TDM_ACTIVE_CH1: int = 131072
    TDM_ACTIVE_CH2: int = 262144
    TDM_ACTIVE_CH3: int = 524288
    TDM_ACTIVE_CH13: int = 536870912
    TDM_ACTIVE_CH12: int = 268435456
    TDM_ACTIVE_CH15: int = 0
    TDM_ACTIVE_CH14: int = -1073741824
    TDM_ACTIVE_CH9: int = 33554432
    TDM_ACTIVE_CH10: int = 67108864
    CHANNEL_MONO: int = 1
    CHANNEL_STEREO: int = 2
    TDM_ACTIVE_CH11: int = 134217728
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_ANT():
    ANT1: int = 1
    MAX: int = 2
    ANT0: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...

ip_addr_any_type: Incomplete ## <class 'ip_addr_t'> = struct ip_addr_t

class GPIO():
    PULLUP_PULLDOWN: int = 2
    FLOATING: int = 3
    PULLDOWN_ONLY: int = 1
    PULLUP_ONLY: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class HTTP_METHOD():
    GET: int = 0
    PROPFIND: int = 14
    PROPPATCH: int = 15
    SUBSCRIBE: int = 7
    OPTIONS: int = 9
    MOVE: int = 11
    COPY: int = 10
    PATCH: int = 3
    MAX: int = 17
    DELETE: int = 4
    NOTIFY: int = 6
    POST: int = 1
    PUT: int = 2
    MKCOL: int = 16
    UNSUBSCRIBE: int = 8
    UNLOCK: int = 13
    HEAD: int = 5
    LOCK: int = 12
    def __init__(self, *argv, **kwargs) -> None:
        ...


class wifi_sta_info_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class C_Pointer():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_SECOND_CHAN():
    BELOW: int = 2
    ABOVE: int = 1
    NONE: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_ENCODE():
    _11BIT: int = 1
    MAX: int = 2
    _12BIT: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_EVENT():
    MAX: int = 5
    RX_DONE: int = 2
    RX_Q_OVF: int = 4
    DMA_ERROR: int = 0
    TX_DONE: int = 1
    TX_Q_OVF: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class MDNS_IP_PROTOCOL():
    V4: int = 0
    MAX: int = 2
    V6: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class MDNS_IF():
    MAX: int = 3
    ETH: int = 2
    AP: int = 1
    STA: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_MODE():
    TX: int = 4
    RX: int = 8
    MASTER: int = 1
    SLAVE: int = 2
    PDM: int = 64
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_BW():
    HT40: int = 2
    HT20: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_tls_cfg():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_PS():
    NONE: int = 0
    MIN_MODEM: int = 1
    MAX_MODEM: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_I2S_DATA_SRC():
    MAX: int = 2
    IO_SIG: int = 0
    ADC: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class spi_device_interface_config_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class i2s_pin_config_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_netif_ip_info_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI():
    ALL_CHANNEL_SCAN: int = 1
    FAST_SCAN: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_eth_mediator_t():
    def detect_phy_addr(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class mdns_result_t():
    def query_results_free(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_ATTEN():
    DB_11: int = 3
    MAX: int = 4
    DB_2_5: int = 1
    DB_0: int = 0
    DB_6: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class PERIPH():
    I2C1_MODULE: int = 6
    DS_MODULE: int = 34
    UART2_MODULE: int = 3
    BT_MODULE: int = 27
    RMT_MODULE: int = 18
    GDMA_MODULE: int = 37
    SPI_MODULE: int = 20
    PWM3_MODULE: int = 15
    DEDIC_GPIO_MODULE: int = 38
    LEDC_MODULE: int = 0
    TIMG1_MODULE: int = 11
    SPI2_MODULE: int = 21
    WIFI_MODULE: int = 26
    RSA_MODULE: int = 35
    PWM0_MODULE: int = 12
    SYSTIMER_MODULE: int = 36
    PCNT_MODULE: int = 19
    I2S0_MODULE: int = 7
    PWM2_MODULE: int = 14
    SPI3_MODULE: int = 22
    RNG_MODULE: int = 25
    SARADC_MODULE: int = 39
    I2S1_MODULE: int = 8
    HMAC_MODULE: int = 33
    TIMG0_MODULE: int = 10
    PWM1_MODULE: int = 13
    WIFI_BT_COMMON_MODULE: int = 28
    TWAI_MODULE: int = 24
    UHCI1_MODULE: int = 17
    UHCI0_MODULE: int = 16
    LCD_CAM_MODULE: int = 9
    UART0_MODULE: int = 1
    UART1_MODULE: int = 2
    SDMMC_MODULE: int = 23
    SHA_MODULE: int = 32
    I2C0_MODULE: int = 5
    BT_BASEBAND_MODULE: int = 29
    AES_MODULE: int = 31
    BT_LC_MODULE: int = 30
    USB_MODULE: int = 4
    MODULE_MAX: int = 40
    def __init__(self, *argv, **kwargs) -> None:
        ...


class http_parser_settings():
    def settings_init(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_NETIF_DHCP():
    INIT: int = 0
    STATUS_MAX: int = 3
    STARTED: int = 1
    STOPPED: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WPS_FAIL_REASON():
    NORMAL: int = 0
    MAX: int = 2
    RECV_M2D: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_CONV():
    ALTER_UNIT: int = 7
    SINGLE_UNIT_1: int = 1
    SINGLE_UNIT_2: int = 2
    BOTH_UNIT: int = 3
    UNIT_MAX: int = 8
    def __init__(self, *argv, **kwargs) -> None:
        ...


class UF():
    PATH: int = 3
    FRAGMENT: int = 5
    HOST: int = 1
    MAX: int = 7
    SCHEMA: int = 0
    QUERY: int = 4
    PORT: int = 2
    USERINFO: int = 6
    def __init__(self, *argv, **kwargs) -> None:
        ...


class GPIO_PULLDOWN():
    DISABLE: int = 0
    ENABLE: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...

ETH_EVENT: Incomplete ## <class '_lv_mp_char_ptr_wrapper'> = struct _lv_mp_char_ptr_wrapper

class RESET_REASON():
    CPU1_SW: int = 12
    SYS_BROWN_OUT: int = 15
    CPU0_RTC_WDT: int = 13
    SYS_CLK_GLITCH: int = 19
    CHIP_SUPER_WDT: int = 1
    CORE_USB_UART: int = 21
    CHIP_POWER_ON: int = 1
    CORE_RTC_WDT: int = 9
    CORE_DEEP_SLEEP: int = 5
    CORE_SW: int = 3
    CPU0_MWDT1: int = 17
    CPU0_MWDT0: int = 11
    CPU1_MWDT1: int = 17
    SYS_SUPER_WDT: int = 18
    CPU1_MWDT0: int = 11
    CORE_USB_JTAG: int = 22
    CPU0_SW: int = 12
    SYS_RTC_WDT: int = 16
    CHIP_BROWN_OUT: int = 1
    CORE_MWDT1: int = 8
    CORE_EFUSE_CRC: int = 20
    CORE_MWDT0: int = 7
    CPU1_RTC_WDT: int = 13
    CORE_PWR_GLITCH: int = 23
    def __init__(self, *argv, **kwargs) -> None:
        ...


class adc_digi_init_config_t():
    def initialize(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI_DMA():
    DISABLED: int = 0
    CH_AUTO: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_SCAN_TYPE():
    PASSIVE: int = 1
    ACTIVE: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class EMAC_CLK():
    DEFAULT: int = 0
    OUT: int = 2
    EXT_IN: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_NETIF():
    VENDOR_SPECIFIC_INFO: int = 43
    FLAG_GARP: int = 8
    ROUTER_SOLICITATION_ADDRESS: int = 32
    DHCP_CLIENT: int = 1
    FLAG_IS_PPP: int = 32
    DHCP_SERVER: int = 2
    FLAG_AUTOUP: int = 4
    FLAG_EVENT_IP_MODIFIED: int = 16
    REQUESTED_IP_ADDRESS: int = 50
    IP_ADDRESS_LEASE_TIME: int = 51
    VENDOR_CLASS_IDENTIFIER: int = 60
    IP_REQUEST_RETRY_TIME: int = 52
    DOMAIN_NAME_SERVER: int = 6
    FLAG_IS_SLIP: int = 64
    SUBNET_MASK: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_ip4_addr_t():
    def netif_set_ip4_addr(self, *args, **kwargs) -> Incomplete:
        ...

    def ip4addr_ntoa(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_http_client_event_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class mdns_txt_item_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class GPIO_PULLUP():
    DISABLE: int = 0
    ENABLE: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_NETIF_OP():
    START: int = 0
    MAX: int = 3
    GET: int = 2
    SET: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class HPE():
    INVALID_FRAGMENT: int = 22
    INVALID_QUERY_STRING: int = 21
    CB_header_field: int = 3
    INVALID_HOST: int = 18
    INVALID_STATUS: int = 15
    PAUSED: int = 31
    CB_chunk_complete: int = 10
    INVALID_PORT: int = 19
    LF_EXPECTED: int = 23
    INVALID_HEADER_TOKEN: int = 24
    INVALID_CONTENT_LENGTH: int = 25
    INVALID_CONSTANT: int = 28
    STRICT: int = 30
    INVALID_PATH: int = 20
    CB_chunk_header: int = 9
    CB_message_complete: int = 7
    CLOSED_CONNECTION: int = 13
    INVALID_VERSION: int = 14
    INVALID_URL: int = 17
    INVALID_METHOD: int = 16
    INVALID_EOF_STATE: int = 11
    INVALID_INTERNAL_STATE: int = 29
    CB_body: int = 6
    INVALID_CHUNK_SIZE: int = 27
    CB_url: int = 2
    UNEXPECTED_CONTENT_LENGTH: int = 26
    HEADER_OVERFLOW: int = 12
    CB_status: int = 8
    UNKNOWN: int = 32
    CB_message_begin: int = 1
    OK: int = 0
    CB_headers_complete: int = 5
    CB_header_value: int = 4
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_MCLK_MULTIPLE():
    _128: int = 128
    _256: int = 256
    DEFAULT: int = 0
    _384: int = 384
    def __init__(self, *argv, **kwargs) -> None:
        ...


class MALLOC_CAP():
    DEFAULT: int = 4096
    DMA: int = 8
    EXEC: int = 1
    INTERNAL: int = 2048
    SPIRAM: int = 1024
    _32BIT: int = 2
    INVALID: int = 0
    _8BIT: int = 4
    def __init__(self, *argv, **kwargs) -> None:
        ...


class spi_transaction_ext_t():
    def et_spi_transaction_ext(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class adc_digi_configuration_t():
    def controller_configure(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class PCNT_UNIT():
    _0: int = 0
    _1: int = 1
    MAX: int = 4
    _3: int = 3
    _2: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_CIPHER_TYPE():
    CCMP: int = 4
    GCMP: int = 8
    WEP104: int = 2
    AES_CMAC128: int = 6
    WEP40: int = 1
    TKIP_CCMP: int = 5
    TKIP: int = 3
    AES_GMAC128: int = 10
    SMS4: int = 7
    GCMP256: int = 9
    UNKNOWN: int = 12
    NONE: int = 0
    AES_GMAC256: int = 11
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ETS():
    TIMER2_INTR_SOURCE: int = 49
    CORE0_IRAM0_PMS_INTR_SOURCE: int = 85
    WIFI_MAC_NMI_SOURCE: int = 1
    CORE0_DRAM0_PMS_INTR_SOURCE: int = 86
    SPI1_INTR_SOURCE: int = 20
    CACHE_IA_INTR_SOURCE: int = 56
    UART0_INTR_SOURCE: int = 27
    CORE1_PIF_PMS_INTR_SOURCE: int = 91
    GPIO_NMI_SOURCE2: int = 19
    APB_ADC_INTR_SOURCE: int = 65
    USB_SERIAL_JTAG_INTR_SOURCE: int = 96
    I2C_MASTER_SOURCE: int = 11
    GPIO_NMI_SOURCE: int = 17
    I2S1_INTR_SOURCE: int = 26
    FROM_CPU_INTR3_SOURCE: int = 82
    BACKUP_PMS_VIOLATE_INTR_SOURCE: int = 93
    I2S0_INTR_SOURCE: int = 25
    SPI_MEM_REJECT_CACHE_INTR_SOURCE: int = 60
    SPI2_DMA_INTR_SOURCE: int = 44
    RSA_INTR_SOURCE: int = 76
    WIFI_PWR_INTR_SOURCE: int = 2
    CORE1_PIF_PMS_SIZE_INTR_SOURCE: int = 92
    TG0_T0_LEVEL_INTR_SOURCE: int = 50
    TG1_T0_LEVEL_INTR_SOURCE: int = 53
    LCD_CAM_INTR_SOURCE: int = 24
    SPI2_INTR_SOURCE: int = 21
    WDT_INTR_SOURCE: int = 47
    CORE1_DRAM0_PMS_INTR_SOURCE: int = 90
    DMA_OUT_CH4_INTR_SOURCE: int = 75
    SLC0_INTR_SOURCE: int = 12
    SYSTIMER_TARGET0_EDGE_INTR_SOURCE: int = 57
    PWM0_INTR_SOURCE: int = 31
    SYSTIMER_TARGET2_EDGE_INTR_SOURCE: int = 59
    ICACHE_PRELOAD0_INTR_SOURCE: int = 62
    UHCI0_INTR_SOURCE: int = 14
    CACHE_CORE1_ACS_INTR_SOURCE: int = 95
    TWAI_INTR_SOURCE: int = 37
    RTC_CORE_INTR_SOURCE: int = 39
    CORE1_IRAM0_PMS_INTR_SOURCE: int = 89
    AES_INTR_SOURCE: int = 77
    TIMER1_INTR_SOURCE: int = 48
    DMA_IN_CH4_INTR_SOURCE: int = 70
    TG0_WDT_LEVEL_INTR_SOURCE: int = 52
    MAX_INTR_SOURCE: int = 99
    DMA_APBPERI_PMS_INTR_SOURCE: int = 84
    UART2_INTR_SOURCE: int = 29
    TG1_T1_LEVEL_INTR_SOURCE: int = 54
    I2C_EXT0_INTR_SOURCE: int = 42
    DMA_IN_CH3_INTR_SOURCE: int = 69
    DMA_EXTMEM_REJECT_SOURCE: int = 98
    CACHE_CORE0_ACS_INTR_SOURCE: int = 94
    PREI_BACKUP_INTR_SOURCE: int = 97
    TG0_T1_LEVEL_INTR_SOURCE: int = 51
    FROM_CPU_INTR2_SOURCE: int = 81
    BT_MAC_INTR_SOURCE: int = 4
    SPI3_DMA_INTR_SOURCE: int = 45
    RWBLE_INTR_SOURCE: int = 8
    DMA_IN_CH2_INTR_SOURCE: int = 68
    ICACHE_SYNC0_INTR_SOURCE: int = 64
    USB_INTR_SOURCE: int = 38
    SYSTIMER_TARGET1_EDGE_INTR_SOURCE: int = 58
    LEDC_INTR_SOURCE: int = 35
    DMA_IN_CH0_INTR_SOURCE: int = 66
    PWM1_INTR_SOURCE: int = 32
    ASSIST_DEBUG_INTR_SOURCE: int = 83
    SDIO_HOST_INTR_SOURCE: int = 30
    DMA_OUT_CH0_INTR_SOURCE: int = 71
    BT_BB_NMI_SOURCE: int = 6
    DMA_OUT_CH1_INTR_SOURCE: int = 72
    RWBLE_NMI_SOURCE: int = 10
    DMA_IN_CH1_INTR_SOURCE: int = 67
    RMT_INTR_SOURCE: int = 40
    WIFI_BB_INTR_SOURCE: int = 3
    I2C_EXT1_INTR_SOURCE: int = 43
    DCACHE_PRELOAD0_INTR_SOURCE: int = 61
    FROM_CPU_INTR0_SOURCE: int = 79
    DMA_OUT_CH2_INTR_SOURCE: int = 73
    WIFI_MAC_INTR_SOURCE: int = 0
    TG1_WDT_LEVEL_INTR_SOURCE: int = 55
    CORE0_PIF_PMS_SIZE_INTR_SOURCE: int = 88
    CORE0_PIF_PMS_INTR_SOURCE: int = 87
    SHA_INTR_SOURCE: int = 78
    UHCI1_INTR_SOURCE: int = 15
    BT_BB_INTR_SOURCE: int = 5
    RWBT_INTR_SOURCE: int = 7
    GPIO_INTR_SOURCE: int = 16
    PCNT_INTR_SOURCE: int = 41
    DCACHE_SYNC0_INTR_SOURCE: int = 63
    GPIO_INTR_SOURCE2: int = 18
    FROM_CPU_INTR1_SOURCE: int = 80
    UART1_INTR_SOURCE: int = 28
    EFUSE_INTR_SOURCE: int = 36
    SPI3_INTR_SOURCE: int = 22
    SLC1_INTR_SOURCE: int = 13
    RWBT_NMI_SOURCE: int = 9
    DMA_OUT_CH3_INTR_SOURCE: int = 74
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_ANT_MODE():
    MAX: int = 3
    AUTO: int = 2
    ANT1: int = 1
    ANT0: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class CHIP():
    ESP32H2: int = 6
    ESP32S3: int = 9
    ESP32S2: int = 2
    ESP32C3: int = 5
    ESP32: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_DIGI_MONITOR():
    LOW: int = 1
    IDX1: int = 1
    IDX0: int = 0
    HIGH: int = 0
    IDX_MAX: int = 2
    MAX: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class GPIO_NUM():
    _42: int = 42
    _45: int = 45
    _44: int = 44
    _43: int = 43
    _40: int = 40
    _41: int = 41
    _14: int = 14
    _15: int = 15
    _47: int = 47
    _48: int = 48
    _46: int = 46
    _16: int = 16
    _7: int = 7
    _6: int = 6
    _1: int = 1
    _4: int = 4
    _5: int = 5
    NC: int = -1
    _9: int = 9
    _8: int = 8
    _0: int = 0
    _2: int = 2
    _3: int = 3
    MAX: int = 49
    _34: int = 34
    _35: int = 35
    _32: int = 32
    _37: int = 37
    _36: int = 36
    _28: int = 28
    _38: int = 38
    _39: int = 39
    _33: int = 33
    _31: int = 31
    _30: int = 30
    _17: int = 17
    _12: int = 12
    _13: int = 13
    _18: int = 18
    _11: int = 11
    _10: int = 10
    _29: int = 29
    _21: int = 21
    _20: int = 20
    _19: int = 19
    _26: int = 26
    _27: int = 27
    def __init__(self, *argv, **kwargs) -> None:
        ...


class FTM_STATUS():
    NO_RESPONSE: int = 3
    FAIL: int = 4
    UNSUPPORTED: int = 1
    SUCCESS: int = 0
    CONF_REJECTED: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_PCM():
    A_COMPRESS: int = 2
    A_DECOMPRESS: int = 1
    U_DECOMPRESS: int = 3
    U_COMPRESS: int = 4
    DISABLE: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_LOG():
    DEBUG: int = 4
    VERBOSE: int = 5
    INFO: int = 3
    ERROR: int = 1
    WARN: int = 2
    NONE: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI_EV():
    TRANS: int = 256
    RECV_DMA_READY: int = 16
    CMDA: int = 128
    CMD9: int = 64
    RECV: int = 32
    SEND: int = 8
    BUF_RX: int = 2
    BUF_TX: int = 1
    SEND_DMA_READY: int = 4
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TCPIP_ADAPTER_IF():
    ETH: int = 2
    MAX: int = 4
    TEST: int = 3
    AP: int = 1
    STA: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_ip_addr_u_addr_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class wifi_sta_list_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class GPIO_PORT():
    MAX: int = 1
    _0: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ETHERNET_EVENT():
    DISCONNECTED: int = 3
    START: int = 0
    CONNECTED: int = 2
    STOP: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ETH_STATE():
    DEINIT: int = 1
    PAUSE: int = 5
    DUPLEX: int = 4
    SPEED: int = 3
    LINK: int = 2
    LLINIT: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class PCNT_PORT():
    MAX: int = 1
    _0: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_ip6_addr_t():
    def netif_ip6_get_addr_type(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_COUNTRY_POLICY():
    AUTO: int = 0
    MANUAL: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class http_parser():
    def parser_execute(self, *args, **kwargs) -> Incomplete:
        ...

    def body_is_final(self, *args, **kwargs) -> Incomplete:
        ...

    def should_keep_alive(self, *args, **kwargs) -> Incomplete:
        ...

    def parser_pause(self, *args, **kwargs) -> Incomplete:
        ...

    def parser_init(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_STORAGE():
    FLASH: int = 0
    RAM: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_MAC():
    IEEE802154: int = 4
    BT: int = 2
    ETH: int = 3
    WIFI_STA: int = 0
    WIFI_SOFTAP: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC2_CHANNEL():
    _7: int = 7
    _6: int = 6
    _1: int = 1
    _4: int = 4
    _5: int = 5
    MAX: int = 10
    _9: int = 9
    _8: int = 8
    _0: int = 0
    _2: int = 2
    _3: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ip_addr_t():
    def paddr_ntoa(self, *args, **kwargs) -> Incomplete:
        ...

    def paddr_ntoa_r(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ETH_DUPLEX():
    HALF: int = 0
    FULL: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_REASON():
    INVALID_RSN_IE_CAP: int = 22
    CIPHER_SUITE_REJECTED: int = 24
    NOT_ASSOCED: int = 7
    NO_AP_FOUND: int = 201
    AUTH_LEAVE: int = 3
    BSS_TRANSITION_DISASSOC: int = 12
    AP_TSF_RESET: int = 206
    ROAMING: int = 207
    ASSOC_LEAVE: int = 8
    ASSOC_EXPIRE: int = 4
    GROUP_KEY_UPDATE_TIMEOUT: int = 16
    AUTH_EXPIRE: int = 2
    HANDSHAKE_TIMEOUT: int = 204
    UNSPECIFIED: int = 1
    _4WAY_HANDSHAKE_TIMEOUT: int = 15
    IE_IN_4WAY_DIFFERS: int = 17
    IE_INVALID: int = 13
    GROUP_CIPHER_INVALID: int = 18
    AUTH_FAIL: int = 202
    PAIRWISE_CIPHER_INVALID: int = 19
    _802_1X_AUTH_FAILED: int = 23
    DISASSOC_PWRCAP_BAD: int = 10
    ASSOC_NOT_AUTHED: int = 9
    BEACON_TIMEOUT: int = 200
    DISASSOC_SUPCHAN_BAD: int = 11
    UNSUPP_RSN_IE_VERSION: int = 21
    AKMP_INVALID: int = 20
    ASSOC_TOOMANY: int = 5
    CONNECTION_FAIL: int = 205
    INVALID_PMKID: int = 53
    ASSOC_FAIL: int = 203
    NOT_AUTHED: int = 6
    MIC_FAILURE: int = 14
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_COMM_FORMAT():
    I2S: int = 1
    PCM_SHORT: int = 4
    STAND_PCM_SHORT: int = 4
    STAND_MSB: int = 2
    STAND_MAX: int = 13
    STAND_I2S: int = 1
    PCM: int = 4
    STAND_PCM_LONG: int = 12
    I2S_MSB: int = 1
    PCM_LONG: int = 8
    I2S_LSB: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class HTTP():
    PROPFIND: int = 12
    ACL: int = 19
    REPORT: int = 20
    SEARCH: int = 14
    UNBIND: int = 18
    PROPPATCH: int = 13
    MKCOL: int = 10
    SUBSCRIBE: int = 26
    UNLINK: int = 32
    COPY: int = 8
    CONNECT: int = 5
    OPTIONS: int = 6
    RESPONSE: int = 1
    GET: int = 1
    PATCH: int = 28
    MOVE: int = 11
    TRACE: int = 7
    REQUEST: int = 0
    MSEARCH: int = 24
    CHECKOUT: int = 22
    LINK: int = 31
    BOTH: int = 2
    UNLOCK: int = 15
    DELETE: int = 0
    PUT: int = 4
    POST: int = 3
    NOTIFY: int = 25
    PURGE: int = 29
    HEAD: int = 2
    MKACTIVITY: int = 21
    MKCALENDAR: int = 30
    MERGE: int = 23
    REBIND: int = 17
    BIND: int = 16
    UNSUBSCRIBE: int = 27
    LOCK: int = 9
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_VND_IE_ID():
    _1: int = 1
    _0: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_PDM_SIG_SCALING():
    DIV_2: int = 0
    MUL_1: int = 1
    MUL_2: int = 2
    MUL_4: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_DIGI_FILTER_IIR():
    _2: int = 0
    MAX: int = 5
    _4: int = 1
    _16: int = 3
    _8: int = 2
    _64: int = 4
    def __init__(self, *argv, **kwargs) -> None:
        ...


class nghttp2_session():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_MODE():
    APSTA: int = 3
    NULL: int = 0
    MAX: int = 4
    AP: int = 2
    STA: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_NETIF_DNS():
    BACKUP: int = 1
    MAX: int = 3
    FALLBACK: int = 2
    MAIN: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_netif_driver_ifconfig_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...

ip_addr_broadcast: Incomplete ## <class 'ip_addr_t'> = struct ip_addr_t

class WIFI_EVENT():
    STA_AUTHMODE_CHANGE: int = 6
    AP_START: int = 12
    MAX: int = 22
    AP_STACONNECTED: int = 14
    STA_START: int = 2
    STA_BSS_RSSI_LOW: int = 18
    STA_DISCONNECTED: int = 5
    AP_STADISCONNECTED: int = 15
    WIFI_READY: int = 0
    STA_STOP: int = 3
    STA_WPS_ER_SUCCESS: int = 7
    STA_WPS_ER_TIMEOUT: int = 9
    AP_STOP: int = 13
    STA_WPS_ER_PIN: int = 10
    ACTION_TX_STATUS: int = 19
    ROC_DONE: int = 20
    FTM_REPORT: int = 17
    SCAN_DONE: int = 1
    STA_CONNECTED: int = 4
    STA_WPS_ER_PBC_OVERLAP: int = 11
    AP_PROBEREQRECVED: int = 16
    STA_WPS_ER_FAILED: int = 8
    STA_BEACON_TIMEOUT: int = 21
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_http_client_config_t():
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def register_event_handler(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class PCNT_CHANNEL_LEVEL_ACTION():
    HOLD: int = 2
    INVERSE: int = 1
    KEEP: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class GPIO_PIN_INTR():
    NEGEDGE: int = 2
    ANYEDGE: int = 3
    HILEVEL: int = 5
    LOLEVEL: int = 4
    POSEDGE: int = 1
    DISABLE: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class adc_digi_pattern_config_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class EMAC_DATA_INTERFACE():
    RMII: int = 0
    MII: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_CHANNEL():
    _7: int = 7
    _6: int = 6
    _1: int = 1
    _4: int = 4
    _5: int = 5
    MAX: int = 10
    _9: int = 9
    _8: int = 8
    _0: int = 0
    _2: int = 2
    _3: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ETH_CMD():
    S_PROMISCUOUS: int = 5
    S_PHY_ADDR: int = 3
    G_PHY_ADDR: int = 2
    S_FLOW_CTRL: int = 6
    G_MAC_ADDR: int = 0
    S_MAC_ADDR: int = 1
    G_SPEED: int = 4
    G_DUPLEX_MODE: int = 7
    S_PHY_LOOPBACK: int = 8
    def __init__(self, *argv, **kwargs) -> None:
        ...


class F():
    SKIPBODY: int = 64
    CHUNKED: int = 1
    CONTENTLENGTH: int = 128
    CONNECTION_CLOSE: int = 4
    CONNECTION_UPGRADE: int = 8
    TRAILING: int = 16
    UPGRADE: int = 32
    CONNECTION_KEEP_ALIVE: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_netif_sta_list_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_netif_sta_info_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class PCNT_UNIT_COUNT_SIGN():
    ZERO_POS: int = 0
    NEG: int = 2
    POS: int = 3
    ZERO_NEG: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class i2s_pdm_tx_upsample_cfg_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class HTTP_EVENT():
    DISCONNECTED: int = 6
    ON_DATA: int = 4
    HEADER_SENT: int = 2
    ON_CONNECTED: int = 1
    HEADERS_SENT: int = 2
    ERROR: int = 0
    ON_FINISH: int = 5
    ON_HEADER: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class SH2LIB_ERR():
    CANCEL: int = -535
    FLOODED: int = -904
    STREAM_ID_NOT_AVAILABLE: int = -509
    INVALID_STREAM_STATE: int = -514
    INVALID_ARGUMENT: int = -501
    DATA_EXIST: int = -529
    PUSH_DISABLED: int = -528
    HTTP_MESSAGING: int = -532
    EOF: int = -507
    GOAWAY_ALREADY_SENT: int = -517
    PAUSE: int = -526
    INVALID_STATE: int = -519
    NOMEM: int = -901
    STREAM_CLOSED: int = -510
    REFUSED_STREAM: int = -533
    SESSION_CLOSING: int = -530
    TEMPORAL_CALLBACK_FAILURE: int = -521
    INTERNAL: int = -534
    INVALID_STREAM_ID: int = -513
    INVALID_HEADER_BLOCK: int = -518
    INSUFF_BUFSIZE: int = -525
    STREAM_SHUT_WR: int = -512
    DEFERRED: int = -508
    UNSUPPORTED_VERSION: int = -503
    CALLBACK_FAILURE: int = -902
    TOO_MANY_INFLIGHT_SETTINGS: int = -527
    WOULDBLOCK: int = -504
    START_STREAM_NOT_ALLOWED: int = -516
    PROTO: int = -505
    BUFFER_ERROR: int = -502
    FLOW_CONTROL: int = -524
    BAD_CLIENT_MAGIC: int = -903
    STREAM_CLOSING: int = -511
    FATAL: int = -900
    INVALID_FRAME: int = -506
    HTTP_HEADER: int = -531
    HEADER_COMP: int = -523
    FRAME_SIZE_ERROR: int = -522
    DEFERRED_DATA_EXIST: int = -515
    def __init__(self, *argv, **kwargs) -> None:
        ...


class spi_bus_config_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class _lv_mp_char_ptr_wrapper():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI_DEVICE():
    HALFDUPLEX: int = 16
    POSITIVE_CS: int = 8
    RXBIT_LSBFIRST: int = 2
    CLK_AS_CS: int = 32
    _3WIRE: int = 4
    NO_DUMMY: int = 64
    TXBIT_LSBFIRST: int = 1
    BIT_LSBFIRST: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class IPADDR_TYPE():
    V4: int = 0
    ANY: int = 46
    V6: int = 6
    def __init__(self, *argv, **kwargs) -> None:
        ...


class PCNT_CHANNEL_EDGE_ACTION():
    INCREASE: int = 1
    DECREASE: int = 2
    HOLD: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class sh2lib_nv():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class mdns_search_once_t():
    def query_async_delete(self, *args, **kwargs) -> Incomplete:
        ...

    def query_async_get_results(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_AUTH():
    OPEN: int = 0
    WAPI_PSK: int = 8
    MAX: int = 9
    WPA2_WPA3_PSK: int = 7
    WPA_WPA2_PSK: int = 4
    WPA3_PSK: int = 6
    WEP: int = 1
    WPA2_PSK: int = 3
    WPA_PSK: int = 2
    WPA2_ENTERPRISE: int = 5
    def __init__(self, *argv, **kwargs) -> None:
        ...


class spi_transaction_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_TASK_PRIO():
    MAX: int = 25
    MIN: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_CLK():
    D2CLK: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ip4_addr_t():
    def p4addr_ntoa_r(self, *args, **kwargs) -> Incomplete:
        ...

    def p4addr_ntoa(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_BITS_PER_CHAN():
    _24BIT: int = 24
    _8BIT: int = 8
    DEFAULT: int = 0
    _16BIT: int = 16
    _32BIT: int = 32
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_netif_t():
    def get_old_ip_info(self, *args, **kwargs) -> Incomplete:
        ...

    def dhcpc_stop(self, *args, **kwargs) -> Incomplete:
        ...

    def get_netif_impl_name(self, *args, **kwargs) -> Incomplete:
        ...

    def dhcps_option(self, *args, **kwargs) -> Incomplete:
        ...

    def get_dns_info(self, *args, **kwargs) -> Incomplete:
        ...

    def dhcps_start(self, *args, **kwargs) -> Incomplete:
        ...

    def set_driver_config(self, *args, **kwargs) -> Incomplete:
        ...

    def get_ip_info(self, *args, **kwargs) -> Incomplete:
        ...

    def set_mac(self, *args, **kwargs) -> Incomplete:
        ...

    def destroy(self, *args, **kwargs) -> Incomplete:
        ...

    def get_ifkey(self, *args, **kwargs) -> Incomplete:
        ...

    def dhcpc_option(self, *args, **kwargs) -> Incomplete:
        ...

    def set_dns_info(self, *args, **kwargs) -> Incomplete:
        ...

    def receive(self, *args, **kwargs) -> Incomplete:
        ...

    def dhcpc_start(self, *args, **kwargs) -> Incomplete:
        ...

    def dhcps_get_status(self, *args, **kwargs) -> Incomplete:
        ...

    def get_ip6_global(self, *args, **kwargs) -> Incomplete:
        ...

    def create_ip6_linklocal(self, *args, **kwargs) -> Incomplete:
        ...

    def dhcps_stop(self, *args, **kwargs) -> Incomplete:
        ...

    def get_event_id(self, *args, **kwargs) -> Incomplete:
        ...

    def get_all_ip6(self, *args, **kwargs) -> Incomplete:
        ...

    def set_ip_info(self, *args, **kwargs) -> Incomplete:
        ...

    def get_desc(self, *args, **kwargs) -> Incomplete:
        ...

    def get_mac(self, *args, **kwargs) -> Incomplete:
        ...

    def next(self, *args, **kwargs) -> Incomplete:
        ...

    def get_flags(self, *args, **kwargs) -> Incomplete:
        ...

    def get_netif_impl_index(self, *args, **kwargs) -> Incomplete:
        ...

    def set_hostname(self, *args, **kwargs) -> Incomplete:
        ...

    def get_ip6_linklocal(self, *args, **kwargs) -> Incomplete:
        ...

    def attach(self, *args, **kwargs) -> Incomplete:
        ...

    def dhcpc_get_status(self, *args, **kwargs) -> Incomplete:
        ...

    def is_netif_up(self, *args, **kwargs) -> Incomplete:
        ...

    def get_io_driver(self, *args, **kwargs) -> Incomplete:
        ...

    def get_hostname(self, *args, **kwargs) -> Incomplete:
        ...

    def set_old_ip_info(self, *args, **kwargs) -> Incomplete:
        ...

    def get_route_prio(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class PCNT_CHANNEL():
    _1: int = 1
    MAX: int = 2
    _0: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_PHY_RATE():
    MCS1_LGI: int = 17
    _2M_L: int = 1
    _11M_L: int = 3
    _11M_S: int = 7
    _2M_S: int = 5
    MCS7_LGI: int = 23
    MCS4_LGI: int = 20
    MCS2_LGI: int = 18
    _48M: int = 8
    MAX: int = 43
    _12M: int = 10
    MCS5_LGI: int = 21
    _54M: int = 12
    _18M: int = 14
    MCS6_LGI: int = 22
    _36M: int = 13
    _24M: int = 9
    _5M_L: int = 2
    MCS4_SGI: int = 28
    _1M_L: int = 0
    _5M_S: int = 6
    MCS0_SGI: int = 24
    LORA_500K: int = 42
    _9M: int = 15
    _6M: int = 11
    MCS0_LGI: int = 16
    MCS3_SGI: int = 27
    MCS2_SGI: int = 26
    MCS6_SGI: int = 30
    MCS3_LGI: int = 19
    LORA_250K: int = 41
    MCS7_SGI: int = 31
    MCS1_SGI: int = 25
    MCS5_SGI: int = 29
    def __init__(self, *argv, **kwargs) -> None:
        ...


class multi_heap_info_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_WIDTH():
    MAX: int = 4
    BIT_12: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class sh2lib_handle():
    def connect_async(self, *args, **kwargs) -> Incomplete:
        ...

    def connect_task(self, *args, **kwargs) -> Incomplete:
        ...

    def do_post(self, *args, **kwargs) -> Incomplete:
        ...

    def do_get(self, *args, **kwargs) -> Incomplete:
        ...

    def session_resume_data(self, *args, **kwargs) -> Incomplete:
        ...

    def do_get_with_nv(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

    def free(self, *args, **kwargs) -> Incomplete:
        ...

    def do_putpost_with_nv(self, *args, **kwargs) -> Incomplete:
        ...

    def do_put(self, *args, **kwargs) -> Incomplete:
        ...

    def execute(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_netif_dns_info_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_DIGI_FILTER():
    IDX0: int = 0
    IDX1: int = 1
    IDX_MAX: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...


class HTTP_TRANSPORT():
    OVER_TCP: int = 1
    OVER_SSL: int = 2
    UNKNOWN: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ETH_CHECKSUM():
    SW: int = 0
    HW: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class OFFER():
    START: int = 0
    DNS: int = 2
    END: int = 3
    ROUTER: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class IP6():
    UNKNOWN: int = 0
    MULTICAST: int = 2
    UNICAST: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_IF():
    MAX: int = 3
    ETH: int = 2
    WIFI_AP: int = 1
    WIFI_STA: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_VND_IE_TYPE():
    ASSOC_RESP: int = 4
    PROBE_REQ: int = 1
    PROBE_RESP: int = 2
    BEACON: int = 0
    ASSOC_REQ: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_RST():
    EXT: int = 2
    INT_WDT: int = 5
    UNKNOWN: int = 0
    BROWNOUT: int = 9
    DEEPSLEEP: int = 8
    POWERON: int = 1
    PANIC: int = 4
    WDT: int = 7
    SDIO: int = 10
    SW: int = 3
    TASK_WDT: int = 6
    def __init__(self, *argv, **kwargs) -> None:
        ...


class esp_ip_addr_t():
    def netif_ip_addr_copy(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class GPIO_DRIVE_CAP():
    _1: int = 1
    DEFAULT: int = 2
    MAX: int = 4
    _2: int = 2
    _0: int = 0
    _3: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI_TRANS():
    VARIABLE_CMD: int = 32
    USE_RXDATA: int = 4
    VARIABLE_ADDR: int = 64
    MODE_QIO: int = 2
    MODE_DIOQIO_ADDR: int = 16
    USE_TXDATA: int = 8
    MODE_DIO: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class i2s_pcm_cfg_t():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_BITS_PER_SAMPLE():
    _8BIT: int = 8
    _24BIT: int = 24
    _16BIT: int = 16
    _32BIT: int = 32
    def __init__(self, *argv, **kwargs) -> None:
        ...


class SH2LIB_DATA_FLAG():
    NO_COPY: int = 4
    EOF: int = 1
    NO_END_STREAM: int = 2
    NONE: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ETH_SPEED():
    MAX: int = 2
    _10M: int = 0
    _100M: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_PKT():
    CTRL: int = 1
    DATA: int = 2
    MGMT: int = 0
    MISC: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class WIFI_CONNECT_AP_BY():
    SIGNAL: int = 0
    SECURITY: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_CHANNEL_FMT():
    MULTIPLE: int = 5
    ALL_LEFT: int = 2
    RIGHT_LEFT: int = 0
    ONLY_LEFT: int = 4
    ALL_RIGHT: int = 1
    ONLY_RIGHT: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...

ip6_addr_any: Incomplete ## <class 'ip_addr_t'> = struct ip_addr_t

class HttpStatus():
    InternalError: int = 500
    SeeOther: int = 303
    PermanentRedirect: int = 308
    Forbidden: int = 403
    BadRequest: int = 400
    Ok: int = 200
    Found: int = 302
    MovedPermanently: int = 301
    TemporaryRedirect: int = 307
    MultipleChoices: int = 300
    Unauthorized: int = 401
    NotFound: int = 404
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESP_NETIF_IP_EVENT():
    LOST_IP: int = 2
    GOT_IP: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class GPIO_MODE():
    INPUT: int = 1
    INPUT_OUTPUT: int = 3
    INPUT_OUTPUT_OD: int = 7
    DISABLE: int = 0
    OUTPUT_OD: int = 6
    OUTPUT: int = 2
    def __init__(self, *argv, **kwargs) -> None:
        ...

ip_addr_any: Incomplete ## <class 'ip_addr_t'> = struct ip_addr_t

class ADC1_CHANNEL():
    _7: int = 7
    _6: int = 6
    _1: int = 1
    _4: int = 4
    _5: int = 5
    MAX: int = 10
    _9: int = 9
    _8: int = 8
    _0: int = 0
    _2: int = 2
    _3: int = 3
    def __init__(self, *argv, **kwargs) -> None:
        ...


class gpio_config_t():
    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S_PDM_DSR():
    MAX: int = 2
    _16S: int = 1
    _8S: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class SH2LIB_NV_FLAG():
    NO_COPY_NAME: int = 2
    NO_COPY_VALUE: int = 4
    NONE: int = 0
    NO_INDEX: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class IP_EVENT():
    STA_GOT_IP: int = 0
    ETH_LOST_IP: int = 5
    GOT_IP6: int = 3
    ETH_GOT_IP: int = 4
    PPP_LOST_IP: int = 7
    PPP_GOT_IP: int = 6
    AP_STAIPASSIGNED: int = 2
    STA_LOST_IP: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC_DIGI():
    OUTPUT_FORMAT_TYPE2: int = 4
    FORMAT_12BIT: int = 0
    FORMAT_MAX: int = 2
    OUTPUT_FORMAT_TYPE1: int = 3
    FORMAT_11BIT: int = 1
    def __init__(self, *argv, **kwargs) -> None:
        ...


class HTTP_AUTH_TYPE():
    BASIC: int = 1
    DIGEST: int = 2
    NONE: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ip6_addr_t():
    def p6addr_ntoa_r(self, *args, **kwargs) -> Incomplete:
        ...

    def p6addr_ntoa(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class GPIO_INTR():
    MAX: int = 6
    NEGEDGE: int = 2
    ANYEDGE: int = 3
    HIGH_LEVEL: int = 5
    LOW_LEVEL: int = 4
    POSEDGE: int = 1
    DISABLE: int = 0
    def __init__(self, *argv, **kwargs) -> None:
        ...

