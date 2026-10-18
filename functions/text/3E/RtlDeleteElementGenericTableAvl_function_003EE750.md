# RtlDeleteElementGenericTableAvl

- RVA: `0x003EE750`–`0x003EEA64` (길이 `788` bytes)
- VA: `0x00000001403EE750`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00096A3C`
- 디코드: `211`개 명령, `788/788` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **29**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x003EE7A3` → [PiDmCompareObjects](../../page/9A/PiDmCompareObjects_function_009A2AD0.md) (function, `0x009A2AD0`)
- `0x003EE7D0` → [PnpCompareInstancePath](../../page/9A/PnpCompareInstancePath_function_009A9B60.md) (function, `0x009A9B60`)
- `0x003EE8C5` → [PiPnpRtlOperationFreeGenericTableEntry](../../page/A3/PiPnpRtlOperationFreeGenericTableEntry_function_00A38760.md) (function, `0x00A38760`)
- `0x003EE9C6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003EE9F5` → [SshpCacheDatabaseFree](../../page/A7/SshpCacheDatabaseFree_function_00A78840.md) (function, `0x00A78840`)
- `0x003EEA04` → [PiPnpRtlObjectEventCompareObjects](../../page/A1/PiPnpRtlObjectEventCompareObjects_function_00A11280.md) (function, `0x00A11280`)
- `0x003EEA11` → [RebalanceNode](RebalanceNode_function_003EEE90.md) (function, `0x003EEE90`)
- `0x003EEA50` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x003EEA5A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [VfAvlDeleteTreeNode](VfAvlDeleteTreeNode_function_003EE240.md) at `0x003EE29D`
- [PnpUnmapActivatingDeviceNodeToThread](PnpUnmapActivatingDeviceNodeToThread_function_003EE4C0.md) at `0x003EE4EB`
- [VfTargetDriversRemove](VfTargetDriversRemove_function_003EEF9C.md) at `0x003EF0CE`
- [DifObjTrkRemoveItem](../61/DifObjTrkRemoveItem_function_0061A1D0.md) at `0x0061A299`
- [CarDeleteDriverRuleViolations](../61/CarDeleteDriverRuleViolations_function_0061B38C.md) at `0x0061B3F0`
- [CarDeletePluginRuleViolations](../61/CarDeletePluginRuleViolations_function_0061B440.md) at `0x0061B48E`
- [CarDeleteRuleViolationDB](../61/CarDeleteRuleViolationDB_function_0061B4D0.md) at `0x0061B519`
- [IopSetFileObjectIosbRange](../../page/71/IopSetFileObjectIosbRange_function_0071C1C8.md) at `0x0071C653`
- [PiDmObjectManagerPopulate](../../page/73/PiDmObjectManagerPopulate_function_00730598.md) at `0x007306DF`
- [PopDirectedDripsUmDirectedFxRemoveTestDevice](../../page/77/PopDirectedDripsUmDirectedFxRemoveTestDevice_function_007716D4.md) at `0x0077172B`
- [EtwpFreeKeyNameList](../../page/7B/EtwpFreeKeyNameList_function_007BE660.md) at `0x007BE671`
- [PiDqQueryDeleteObjectFromResultSet](../../page/8D/PiDqQueryDeleteObjectFromResultSet_function_008DC600.md) at `0x008DC612`
- [PiPnpRtlEndOperation](../../page/8E/PiPnpRtlEndOperation_function_008E0518.md) at `0x008E05BC`
- [PiPnpRtlObjectEventWorker](../../page/8F/PiPnpRtlObjectEventWorker_function_008F8630.md) at `0x008F899C`
- [PopPowerRequestTableDeleteEntry](../../page/91/PopPowerRequestTableDeleteEntry_function_00913170.md) at `0x0091318C`
- [PiSwBusRelationRemove](../../page/94/PiSwBusRelationRemove_function_0094D9C0.md) at `0x0094DA4A`
- [PiSwProcessRemove](../../page/94/PiSwProcessRemove_function_0094E3B8.md) at `0x0094E5FA`
- [PiDmRemoveCacheReferenceForObject](../../page/95/PiDmRemoveCacheReferenceForObject_function_00950F24.md) at `0x00950F9A`
- [IopCleanupFileObjectIosbRange](../../page/9E/IopCleanupFileObjectIosbRange_function_009E88A8.md) at `0x009E8978`
- [PnpCleanupDeviceRegistryValues](../../page/A0/PnpCleanupDeviceRegistryValues_function_00A0797C.md) at `0x00A079A8`
- [SshpCacheRemoveBlocker](../../page/A4/SshpCacheRemoveBlocker_function_00A4E124.md) at `0x00A4E148`
- [PiDmListRemoveObjectWorker](../../page/A8/PiDmListRemoveObjectWorker_function_00A88748.md) at `0x00A8882A`
- [PiUpdateDriverDBCache](../../page/A8/PiUpdateDriverDBCache_function_00A895CC.md) at `0x00A896BA`
- [sub_00B1C4F6](../../page/B1/Unknown_function_00B1C4F6.md) at `0x00B1C85E`
- [sub_00B1F154](../../page/B1/Unknown_function_00B1F154.md) at `0x00B1F175`
- [sub_00B1F154](../../page/B1/Unknown_function_00B1F154.md) at `0x00B1F1CB`
- [sub_00B4A56C](../../page/B4/Unknown_function_00B4A56C.md) at `0x00B4A59A`
- [VfAvlDeleteAllTreeNodes](../../pagevrfy/B9/VfAvlDeleteAllTreeNodes_function_00B93B9C.md) at `0x00B93BDC`
- [VfPtProcessFreePoolInfo](../../pagevrfy/B9/VfPtProcessFreePoolInfo_function_00B9C604.md) at `0x00B9C66C`
- [ViPtDeleteAvlTrees](../../pagevrfy/B9/ViPtDeleteAvlTrees_function_00B9C730.md) at `0x00B9C78F`
- [ViPtDeleteAvlTrees](../../pagevrfy/B9/ViPtDeleteAvlTrees_function_00B9C730.md) at `0x00B9C813`

### Static image references
- `0x003EE778` → RVA `0x009A2AD0` (`PiDmCompareObjects`; read)
- `0x003EE77F` → RVA `0x009A9B60` (`PnpCompareInstancePath`; read)
- `0x003EE786` → RVA `0x00A11280` (`PiPnpRtlObjectEventCompareObjects`; read)
- `0x003EE8A3` → RVA `0x00A38760` (`PiPnpRtlOperationFreeGenericTableEntry`; read)
- `0x003EE9B7` → RVA `0x00B82870` (`ExFreePoolWithTag`; read)
- `0x003EE9E6` → RVA `0x00A78840` (`SshpCacheDatabaseFree`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x003EE7A3` → [PiDmCompareObjects](../../page/9A/PiDmCompareObjects_function_009A2AD0.md) (`.text` → `PAGE`)
  - `0x003EE7D0` → [PnpCompareInstancePath](../../page/9A/PnpCompareInstancePath_function_009A9B60.md) (`.text` → `PAGE`)
  - `0x003EE8C5` → [PiPnpRtlOperationFreeGenericTableEntry](../../page/A3/PiPnpRtlOperationFreeGenericTableEntry_function_00A38760.md) (`.text` → `PAGE`)
  - `0x003EE9C6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x003EE9F5` → [SshpCacheDatabaseFree](../../page/A7/SshpCacheDatabaseFree_function_00A78840.md) (`.text` → `PAGE`)
  - `0x003EEA04` → [PiPnpRtlObjectEventCompareObjects](../../page/A1/PiPnpRtlObjectEventCompareObjects_function_00A11280.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003EE750  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003EE755  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
003EE75A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
003EE75F  57                              push rdi
003EE760  41 56                           push r14
003EE762  41 57                           push r15
003EE764  48 83 EC 20                     sub rsp, 0x20
003EE768  83 79 2C 00                     cmp dword ptr [rcx + 0x2c], 0
003EE76C  48 8B F2                        mov rsi, rdx
003EE76F  48 8B F9                        mov rdi, rcx
003EE772  74 41                           je 0x1403ee7b5
003EE774  48 8B 59 10                     mov rbx, qword ptr [rcx + 0x10]
003EE778  48 8D 2D 51 43 5B 00            lea rbp, [rip + 0x5b4351]
003EE77F  4C 8D 35 DA B3 5B 00            lea r14, [rip + 0x5bb3da]
003EE786  4C 8D 3D F3 2A 62 00            lea r15, [rip + 0x622af3]
003EE78D  0F 1F 00                        nop dword ptr [rax]
003EE790  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
003EE794  4C 8D 43 20                     lea r8, [rbx + 0x20]
003EE798  48 8B D6                        mov rdx, rsi
003EE79B  48 8B CF                        mov rcx, rdi
003EE79E  48 3B C5                        cmp rax, rbp
003EE7A1  75 24                           jne 0x1403ee7c7
003EE7A3  E8 28 43 5B 00                  call 0x1409a2ad0
003EE7A8  85 C0                           test eax, eax
003EE7AA  75 10                           jne 0x1403ee7bc
003EE7AC  48 8B 5B 08                     mov rbx, qword ptr [rbx + 8]
003EE7B0  48 85 DB                        test rbx, rbx
003EE7B3  75 DB                           jne 0x1403ee790
003EE7B5  32 C0                           xor al, al
003EE7B7  E9 10 01 00 00                  jmp 0x1403ee8cc
003EE7BC  83 F8 01                        cmp eax, 1
003EE7BF  75 16                           jne 0x1403ee7d7
003EE7C1  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
003EE7C5  EB E9                           jmp 0x1403ee7b0
003EE7C7  49 3B C6                        cmp rax, r14
003EE7CA  0F 85 2F 02 00 00               jne 0x1403ee9ff
003EE7D0  E8 8B B3 5B 00                  call 0x1409a9b60
003EE7D5  EB D1                           jmp 0x1403ee7a8
003EE7D7  45 33 FF                        xor r15d, r15d
003EE7DA  48 8D 53 08                     lea rdx, [rbx + 8]
003EE7DE  4C 8B F3                        mov r14, rbx
003EE7E1  48 3B 5F 38                     cmp rbx, qword ptr [rdi + 0x38]
003EE7E5  75 3C                           jne 0x1403ee823
003EE7E7  48 8B 02                        mov rax, qword ptr [rdx]
003EE7EA  48 85 C0                        test rax, rax
003EE7ED  0F 85 0E 01 00 00               jne 0x1403ee901
003EE7F3  48 8B 03                        mov rax, qword ptr [rbx]
003EE7F6  48 39 58 08                     cmp qword ptr [rax + 8], rbx
003EE7FA  75 10                           jne 0x1403ee80c
003EE7FC  0F 1F 40 00                     nop dword ptr [rax]
003EE800  48 8B D8                        mov rbx, rax
003EE803  48 8B 00                        mov rax, qword ptr [rax]
003EE806  48 39 58 08                     cmp qword ptr [rax + 8], rbx
003EE80A  74 F4                           je 0x1403ee800
003EE80C  48 39 58 10                     cmp qword ptr [rax + 0x10], rbx
003EE810  0F 85 32 02 00 00               jne 0x1403eea48
003EE816  48 39 00                        cmp qword ptr [rax], rax
003EE819  0F 84 29 02 00 00               je 0x1403eea48
003EE81F  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
003EE823  FF 47 40                        inc dword ptr [rdi + 0x40]
003EE826  48 8B 02                        mov rax, qword ptr [rdx]
003EE829  48 85 C0                        test rax, rax
003EE82C  0F 85 50 01 00 00               jne 0x1403ee982
003EE832  49 8B DE                        mov rbx, r14
003EE835  48 8B 03                        mov rax, qword ptr [rbx]
003EE838  B2 FF                           mov dl, 0xff
003EE83A  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
003EE83E  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
003EE842  48 85 C9                        test rcx, rcx
003EE845  0F 85 23 01 00 00               jne 0x1403ee96e
003EE84B  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
003EE84F  4C 3B C3                        cmp r8, rbx
003EE852  0F 84 C8 00 00 00               je 0x1403ee920
003EE858  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
003EE85C  B2 01                           mov dl, 1
003EE85E  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
003EE862  48 85 C9                        test rcx, rcx
003EE865  74 06                           je 0x1403ee86d
003EE867  48 8B 03                        mov rax, qword ptr [rbx]
003EE86A  48 89 01                        mov qword ptr [rcx], rax
003EE86D  44 88 7F 18                     mov byte ptr [rdi + 0x18], r15b
003EE871  BD FF FF FF FF                  mov ebp, 0xffffffff
003EE876  48 8B 33                        mov rsi, qword ptr [rbx]
003EE879  0F B6 46 18                     movzx eax, byte ptr [rsi + 0x18]
003EE87D  3A C2                           cmp al, dl
003EE87F  74 65                           je 0x1403ee8e6
003EE881  84 C0                           test al, al
003EE883  0F 85 85 01 00 00               jne 0x1403eea0e
003EE889  F6 DA                           neg dl
003EE88B  88 56 18                        mov byte ptr [rsi + 0x18], dl
003EE88E  44 38 7F 18                     cmp byte ptr [rdi + 0x18], r15b
003EE892  74 03                           je 0x1403ee897
003EE894  01 6F 30                        add dword ptr [rdi + 0x30], ebp
003EE897  4C 3B F3                        cmp r14, rbx
003EE89A  0F 85 89 00 00 00               jne 0x1403ee929
003EE8A0  FF 4F 2C                        dec dword ptr [rdi + 0x2c]
003EE8A3  48 8D 0D B6 9E 64 00            lea rcx, [rip + 0x649eb6]
003EE8AA  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
003EE8AE  49 8B D6                        mov rdx, r14
003EE8B1  44 89 7F 28                     mov dword ptr [rdi + 0x28], r15d
003EE8B5  4C 89 7F 20                     mov qword ptr [rdi + 0x20], r15
003EE8B9  48 3B C1                        cmp rax, rcx
003EE8BC  0F 85 F5 00 00 00               jne 0x1403ee9b7
003EE8C2  48 8B CF                        mov rcx, rdi
003EE8C5  E8 96 9E 64 00                  call 0x140a38760
003EE8CA  B0 01                           mov al, 1
003EE8CC  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
003EE8D1  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
003EE8D6  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
003EE8DB  48 83 C4 20                     add rsp, 0x20
003EE8DF  41 5F                           pop r15
003EE8E1  41 5E                           pop r14
003EE8E3  5F                              pop rdi
003EE8E4  C3                              ret
003EE8E5  CC                              int3
003EE8E6  44 88 7E 18                     mov byte ptr [rsi + 0x18], r15b
003EE8EA  48 8B 06                        mov rax, qword ptr [rsi]
003EE8ED  BA 01 00 00 00                  mov edx, 1
003EE8F2  48 39 70 10                     cmp qword ptr [rax + 0x10], rsi
003EE8F6  48 8B F0                        mov rsi, rax
003EE8F9  0F 45 D5                        cmovne edx, ebp
003EE8FC  E9 78 FF FF FF                  jmp 0x1403ee879
003EE901  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
003EE905  48 85 C9                        test rcx, rcx
003EE908  0F 84 11 FF FF FF               je 0x1403ee81f
003EE90E  48 8B C1                        mov rax, rcx
003EE911  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
003EE915  48 85 C9                        test rcx, rcx
003EE918  0F 84 01 FF FF FF               je 0x1403ee81f
003EE91E  EB EE                           jmp 0x1403ee90e
003EE920  48 89 48 08                     mov qword ptr [rax + 8], rcx
003EE924  E9 35 FF FF FF                  jmp 0x1403ee85e
003EE929  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
003EE92D  0F 11 03                        movups xmmword ptr [rbx], xmm0
003EE930  41 0F 10 4E 10                  movups xmm1, xmmword ptr [r14 + 0x10]
003EE935  0F 11 4B 10                     movups xmmword ptr [rbx + 0x10], xmm1
003EE939  49 8B 06                        mov rax, qword ptr [r14]
003EE93C  48 8B 0B                        mov rcx, qword ptr [rbx]
003EE93F  4C 39 70 08                     cmp qword ptr [rax + 8], r14
003EE943  0F 85 87 00 00 00               jne 0x1403ee9d0
003EE949  48 89 59 08                     mov qword ptr [rcx + 8], rbx
003EE94D  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
003EE951  48 85 C0                        test rax, rax
003EE954  74 03                           je 0x1403ee959
003EE956  48 89 18                        mov qword ptr [rax], rbx
003EE959  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
003EE95D  48 85 C0                        test rax, rax
003EE960  0F 84 3A FF FF FF               je 0x1403ee8a0
003EE966  48 89 18                        mov qword ptr [rax], rbx
003EE969  E9 32 FF FF FF                  jmp 0x1403ee8a0
003EE96E  4C 3B C3                        cmp r8, rbx
003EE971  74 66                           je 0x1403ee9d9
003EE973  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
003EE977  B2 01                           mov dl, 1
003EE979  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
003EE97D  E9 E5 FE FF FF                  jmp 0x1403ee867
003EE982  49 8B 5E 10                     mov rbx, qword ptr [r14 + 0x10]
003EE986  48 85 DB                        test rbx, rbx
003EE989  0F 84 A3 FE FF FF               je 0x1403ee832
003EE98F  45 38 7E 18                     cmp byte ptr [r14 + 0x18], r15b
003EE993  0F 8C 8D 00 00 00               jl 0x1403eea26
003EE999  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
003EE99D  48 85 C0                        test rax, rax
003EE9A0  0F 84 8F FE FF FF               je 0x1403ee835
003EE9A6  48 8B D8                        mov rbx, rax
003EE9A9  48 8B 40 08                     mov rax, qword ptr [rax + 8]
003EE9AD  48 85 C0                        test rax, rax
003EE9B0  75 F4                           jne 0x1403ee9a6
003EE9B2  E9 7E FE FF FF                  jmp 0x1403ee835
003EE9B7  48 8D 0D B2 3E 79 00            lea rcx, [rip + 0x793eb2]
003EE9BE  48 3B C1                        cmp rax, rcx
003EE9C1  75 23                           jne 0x1403ee9e6
003EE9C3  48 8B CF                        mov rcx, rdi
003EE9C6  E8 A5 3E 79 00                  call 0x140b82870
003EE9CB  E9 FA FE FF FF                  jmp 0x1403ee8ca
003EE9D0  48 89 59 10                     mov qword ptr [rcx + 0x10], rbx
003EE9D4  E9 74 FF FF FF                  jmp 0x1403ee94d
003EE9D9  48 89 48 08                     mov qword ptr [rax + 8], rcx
003EE9DD  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
003EE9E1  E9 81 FE FF FF                  jmp 0x1403ee867
003EE9E6  48 8D 0D 53 9E 68 00            lea rcx, [rip + 0x689e53]
003EE9ED  48 3B C1                        cmp rax, rcx
003EE9F0  48 8B CF                        mov rcx, rdi
003EE9F3  75 65                           jne 0x1403eea5a
003EE9F5  E8 46 9E 68 00                  call 0x140a78840
003EE9FA  E9 CB FE FF FF                  jmp 0x1403ee8ca
003EE9FF  49 3B C7                        cmp rax, r15
003EEA02  75 4C                           jne 0x1403eea50
003EEA04  E8 77 28 62 00                  call 0x140a11280
003EEA09  E9 9A FD FF FF                  jmp 0x1403ee7a8
003EEA0E  48 8B CE                        mov rcx, rsi
003EEA11  E8 7A 04 00 00                  call 0x1403eee90
003EEA16  85 C0                           test eax, eax
003EEA18  0F 85 79 FE FF FF               jne 0x1403ee897
003EEA1E  48 8B 36                        mov rsi, qword ptr [rsi]
003EEA21  E9 C4 FE FF FF                  jmp 0x1403ee8ea
003EEA26  48 8B D8                        mov rbx, rax
003EEA29  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
003EEA2D  48 85 C0                        test rax, rax
003EEA30  0F 84 FF FD FF FF               je 0x1403ee835
003EEA36  48 8B D8                        mov rbx, rax
003EEA39  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
003EEA3D  48 85 C0                        test rax, rax
003EEA40  0F 84 EF FD FF FF               je 0x1403ee835
003EEA46  EB EE                           jmp 0x1403eea36
003EEA48  49 8B C7                        mov rax, r15
003EEA4B  E9 CF FD FF FF                  jmp 0x1403ee81f
003EEA50  E8 7B C0 2C 00                  call 0x1406baad0
003EEA55  E9 4E FD FF FF                  jmp 0x1403ee7a8
003EEA5A  E8 71 C0 2C 00                  call 0x1406baad0
003EEA5F  E9 66 FE FF FF                  jmp 0x1403ee8ca
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlDeleteElementGenericTableAvl(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(a1 + 44)) == 0) goto loc_003EE7B5;
loc_003EE790:
    if ((*(unsigned __int64 *)(a1 + 72)) != (v_rip + 5981009)) goto loc_003EE7C7;
    result = PiDmCompareObjects(a1, a2, *(unsigned __int64 *)(a1 + 16) + 32, a4);
loc_003EE7A8:
    if ((unsigned int)(result) != 0) goto loc_003EE7BC;
loc_003EE7B0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) != 0) goto loc_003EE790;
loc_003EE7B5:
    result = 0;
    goto loc_003EE8CC;
loc_003EE7BC:
    if (0 != 1) goto loc_003EE7D7;
    goto loc_003EE7B0;
loc_003EE7C7:
    if (0 != (v_rip + 6009818)) goto loc_003EE9FF;
    result = PnpCompareInstancePath(a1, a2, *(unsigned __int64 *)(a1 + 16) + 32, a4);
    goto loc_003EE7A8;
loc_003EE7D7:
    v_r15 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) != (*(unsigned __int64 *)(a1 + 56))) goto loc_003EE823;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 8) != 0) goto loc_003EE901;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16))) goto loc_003EE80C;
loc_003EE800:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16))) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)))) goto loc_003EE800;
loc_003EE80C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16))) + 16)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)))) goto loc_003EEA48;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16))))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16))))) goto loc_003EEA48;
loc_003EE81F:
    *(unsigned __int64 *)(a1 + 56) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)));
loc_003EE823:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 8) != 0) goto loc_003EE982;
loc_003EE832:
loc_003EE835:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 8) != 0) goto loc_003EE96E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16))) goto loc_003EE920;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 16);
loc_003EE85E:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 16) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16));
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 16)) = result;
    }
    *(unsigned __int8 *)(a1 + 24) = 0;
loc_003EE879:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 24))) == 1) goto loc_003EE8E6;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 24)) != 0) goto loc_003EEA0E;
    a2 = (unsigned __int8)(-(1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 24) = (unsigned __int8)(a2);
    if ((*(unsigned __int8 *)(a1 + 24)) != 0) {
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16))) goto loc_003EE929;
loc_003EE8A0:
    *(unsigned int *)(a1 + 40) = 0;
    *(unsigned __int64 *)(a1 + 32) = 0;
    if ((*(unsigned __int64 *)(a1 + 88)) != (v_rip + 6594230)) goto loc_003EE9B7;
    result = PiPnpRtlOperationFreeGenericTableEntry(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8), a4);
loc_003EE8CA:
loc_003EE8CC:
    v_rsp = (v_rsp) + (32);
    return 1;
loc_003EE8E6:
    *(unsigned __int8 *)(v_stack_p18 + 24) = 0;
loc_003EE8EA:
    a2 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18) + 16)) != v_stack_p18) { a2 = (unsigned int)(v_stack_p10); }
    goto loc_003EE879;
loc_003EE901:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18) + 16) == 0) goto loc_003EE81F;
loc_003EE90E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18) + 16) + 16) == 0) goto loc_003EE81F;
    goto loc_003EE90E;
loc_003EE920:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18) + 16) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18) + 16) + 16);
    goto loc_003EE85E;
loc_003EE929:
    *(unsigned __int64 *)(v_stack_p8) = v_xmm0;
    *(unsigned __int64 *)(v_stack_p8 + 16) = v_xmm1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16))) goto loc_003EE9D0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8) + 8) = v_stack_p8;
loc_003EE94D:
    if (*(unsigned __int64 *)(v_stack_p8 + 8) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8)) = v_stack_p8;
    }
    if (*(unsigned __int64 *)(v_stack_p8 + 16) == 0) goto loc_003EE8A0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16)) = v_stack_p8;
    goto loc_003EE8A0;
loc_003EE96E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8)) == v_stack_p8) goto loc_003EE9D9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16) + 16) = *(unsigned __int64 *)(v_stack_p8);
    goto loc_003EE867;
loc_003EE982:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 16) == 0) goto loc_003EE832;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 24)) < 0) goto loc_003EEA26;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 16) + 8) == 0) goto loc_003EE835;
loc_003EE9A6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 16) + 8) + 8) != 0) goto loc_003EE9A6;
    goto loc_003EE835;
loc_003EE9B7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 16) + 8) + 8)) != (v_rip + 7945906)) goto loc_003EE9E6;
    result = ExFreePoolWithTag(a1, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8), a4);
    goto loc_003EE8CA;
loc_003EE9D0:
    *(unsigned __int64 *)(a1 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16) + 16) + 8);
    goto loc_003EE94D;
loc_003EE9D9:
    *(unsigned __int64 *)(result + 8) = a1;
    goto loc_003EE867;
loc_003EE9E6:
    if (result != (v_rip + 6856275)) goto loc_003EEA5A;
    result = SshpCacheDatabaseFree(a1, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8), a4);
    goto loc_003EE8CA;
loc_003EE9FF:
    if (result != 0) goto loc_003EEA50;
    result = PiPnpRtlObjectEventCompareObjects(a1, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8), a4);
    goto loc_003EE7A8;
loc_003EEA0E:
    result = RebalanceNode(*(unsigned __int64 *)(v_stack_p18), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8), a4);
    if ((unsigned int)(result) != 0) goto loc_003EE897;
    goto loc_003EE8EA;
loc_003EEA26:
    if (*(unsigned __int64 *)(result + 16) == 0) goto loc_003EE835;
loc_003EEA36:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 16) == 0) goto loc_003EE835;
    goto loc_003EEA36;
loc_003EEA48:
    goto loc_003EE81F;
loc_003EEA50:
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_p18), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8), a4);
    goto loc_003EE7A8;
loc_003EEA5A:
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_p18), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 16)) + 8), a4);
    goto loc_003EE8CA;
}
```

## 5. (Beta) C Style

```c
int64_t RtlDeleteElementGenericTableAvl(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(arg1 + 0x2C)) == 0) goto loc_003EE7B5;
loc_003EE790:
    if ((*(uint64_t *)(arg1 + 0x48)) != (v_rip + 5981009)) goto loc_003EE7C7;
    result = PiDmCompareObjects(Arg1, Arg2, *(uint64_t *)(arg1 + 0x10) + 32, a4);
loc_003EE7A8:
    if ((uint32_t)(result) != 0) goto loc_003EE7BC;
loc_003EE7B0:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) != 0) goto loc_003EE790;
loc_003EE7B5:
    result = 0;
    goto loc_003EE8CC;
loc_003EE7BC:
    if (0 != 1) goto loc_003EE7D7;
    goto loc_003EE7B0;
loc_003EE7C7:
    if (0 != (v_rip + 6009818)) goto loc_003EE9FF;
    result = PnpCompareInstancePath(Arg1, Arg2, *(uint64_t *)(arg1 + 0x10) + 32, a4);
    goto loc_003EE7A8;
loc_003EE7D7:
    local_r15 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) != (*(uint64_t *)(arg1 + 0x38))) goto loc_003EE823;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x8) != 0) goto loc_003EE901;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10))) goto loc_003EE80C;
loc_003EE800:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10))) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)))) goto loc_003EE800;
loc_003EE80C:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10))) + 0x10)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)))) goto loc_003EEA48;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10))))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10))))) goto loc_003EEA48;
loc_003EE81F:
    *(uint64_t *)(arg1 + 0x38) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)));
loc_003EE823:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x8) != 0) goto loc_003EE982;
loc_003EE832:
loc_003EE835:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x8) != 0) goto loc_003EE96E;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10))) goto loc_003EE920;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x10);
loc_003EE85E:
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x10) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10));
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x10)) = result;
    }
    *(uint8_t *)(arg1 + 0x18) = 0;
loc_003EE879:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x18))) == 1) goto loc_003EE8E6;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x18)) != 0) goto loc_003EEA0E;
    Arg2 = (uint8_t)(-(1));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x18) = (uint8_t)(Arg2);
    if ((*(uint8_t *)(arg1 + 0x18)) != 0) {
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10))) goto loc_003EE929;
loc_003EE8A0:
    *(uint32_t *)(arg1 + 0x28) = 0;
    *(uint64_t *)(arg1 + 0x20) = 0;
    if ((*(uint64_t *)(arg1 + 0x58)) != (v_rip + 6594230)) goto loc_003EE9B7;
    result = PiPnpRtlOperationFreeGenericTableEntry(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8), a4);
loc_003EE8CA:
loc_003EE8CC:
    local_rsp = (local_rsp) + (32);
    return 1;
loc_003EE8E6:
    *(uint8_t *)(v_stack_p18 + 0x18) = 0;
loc_003EE8EA:
    Arg2 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p18) + 0x10)) != v_stack_p18) { Arg2 = (uint32_t)(v_stack_p10); }
    goto loc_003EE879;
loc_003EE901:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p18) + 0x10) == 0) goto loc_003EE81F;
loc_003EE90E:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p18) + 0x10) + 0x10) == 0) goto loc_003EE81F;
    goto loc_003EE90E;
loc_003EE920:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p18) + 0x10) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p18) + 0x10) + 0x10);
    goto loc_003EE85E;
loc_003EE929:
    *(uint64_t *)(v_stack_p8) = v_xmm0;
    *(uint64_t *)(v_stack_p8 + 0x10) = v_xmm1;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10))) goto loc_003EE9D0;
    *(uint64_t *)(*(uint64_t *)(v_stack_p8) + 0x8) = v_stack_p8;
loc_003EE94D:
    if (*(uint64_t *)(v_stack_p8 + 0x8) != 0) {
        *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8)) = v_stack_p8;
    }
    if (*(uint64_t *)(v_stack_p8 + 0x10) == 0) goto loc_003EE8A0;
    *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10)) = v_stack_p8;
    goto loc_003EE8A0;
loc_003EE96E:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8)) == v_stack_p8) goto loc_003EE9D9;
    *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10) + 0x10) = *(uint64_t *)(v_stack_p8);
    goto loc_003EE867;
loc_003EE982:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x10) == 0) goto loc_003EE832;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x18)) < 0) goto loc_003EEA26;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x10) + 0x8) == 0) goto loc_003EE835;
loc_003EE9A6:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x10) + 0x8) + 0x8) != 0) goto loc_003EE9A6;
    goto loc_003EE835;
loc_003EE9B7:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x10) + 0x8) + 0x8)) != (v_rip + 7945906)) goto loc_003EE9E6;
    result = ExFreePoolWithTag(Arg1, 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8), a4);
    goto loc_003EE8CA;
loc_003EE9D0:
    *(uint64_t *)(arg1 + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10) + 0x10) + 0x8);
    goto loc_003EE94D;
loc_003EE9D9:
    *(void **)(result + 0x8) = Arg1;
    goto loc_003EE867;
loc_003EE9E6:
    if (result != (v_rip + 6856275)) goto loc_003EEA5A;
    result = SshpCacheDatabaseFree(Arg1, 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8), a4);
    goto loc_003EE8CA;
loc_003EE9FF:
    if (result != 0) goto loc_003EEA50;
    result = PiPnpRtlObjectEventCompareObjects(Arg1, 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8), a4);
    goto loc_003EE7A8;
loc_003EEA0E:
    result = RebalanceNode(*(uint64_t *)(v_stack_p18), 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8), a4);
    if ((uint32_t)(result) != 0) goto loc_003EE897;
    goto loc_003EE8EA;
loc_003EEA26:
    if (*(uint64_t *)(result + 0x10) == 0) goto loc_003EE835;
loc_003EEA36:
    if (*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x10) == 0) goto loc_003EE835;
    goto loc_003EEA36;
loc_003EEA48:
    goto loc_003EE81F;
loc_003EEA50:
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_p18), 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8), a4);
    goto loc_003EE7A8;
loc_003EEA5A:
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_p18), 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x10)) + 0x8), a4);
    goto loc_003EE8CA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `8` | `R` |
| `Arg1` | `+ 0x18` | `8` | `W` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `32` | `W` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R/W` |
| `Arg1` | `+ 0x30` | `32` | `R/W` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg1` | `+ 0x40` | `32` | `R/W` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EE750&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
