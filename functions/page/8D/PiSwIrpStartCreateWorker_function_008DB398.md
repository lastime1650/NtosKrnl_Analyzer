# PiSwIrpStartCreateWorker

- RVA: `0x008DB398`–`0x008DB8E6` (길이 `1,358` bytes)
- VA: `0x00000001408DB398`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00085820`
- 디코드: `328`개 명령, `1,358/1,358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x008DB3DC` → [PiSwValidateCreateData](PiSwValidateCreateData_function_008DB958.md) (function, `0x008DB958`)
- `0x008DB3F4` → [PiSwLock](../8F/PiSwLock_function_008F7D50.md) (function, `0x008F7D50`)
- `0x008DB406` → [PiSwDeviceCreate](PiSwDeviceCreate_function_008DB8EC.md) (function, `0x008DB8EC`)
- `0x008DB41C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008DB421` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008DB463` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008DB4D1` → [PiSwPropertySet](../8F/PiSwPropertySet_function_008F5EEC.md) (function, `0x008F5EEC`)
- `0x008DB510` → [PiSwInstanceInfoInit](PiSwInstanceInfoInit_function_008DBC84.md) (function, `0x008DBC84`)
- `0x008DB534` → [RtlInsertElementGenericTableAvl](../../text/3E/RtlInsertElementGenericTableAvl_function_003EE510.md) (function, `0x003EE510`)
- `0x008DB576` → [PiSwPnPInfoInit](PiSwPnPInfoInit_function_008DB2DC.md) (function, `0x008DB2DC`)
- `0x008DB5BD` → [PnpCopyDevPropertyArray](PnpCopyDevPropertyArray_function_008DB0F8.md) (function, `0x008DB0F8`)
- `0x008DB5D7` → [PiSwBusRelationAdd](PiSwBusRelationAdd_function_008DA994.md) (function, `0x008DA994`)
- `0x008DB5E9` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (function, `0x00433560`)
- `0x008DB608` → [PnpDeviceObjectFromDeviceInstanceWithTag](../8E/PnpDeviceObjectFromDeviceInstanceWithTag_function_008E7490.md) (function, `0x008E7490`)
- `0x008DB6A2` → [McTemplateK0zzqq_EtwWriteTransfer](../../text/5A/McTemplateK0zzqq_EtwWriteTransfer_function_005A95C0.md) (function, `0x005A95C0`)
- `0x008DB6BE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008DB6F0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008DB700` → [IoInvalidateDeviceRelations](../../text/49/IoInvalidateDeviceRelations_function_0049E160.md) (function, `0x0049E160`)
- `0x008DB790` → [McTemplateK0zzzdzzq_EtwWriteTransfer](../../text/5A/McTemplateK0zzzdzzq_EtwWriteTransfer_function_005A98F8.md) (function, `0x005A98F8`)
- `0x008DB7BA` → [McTemplateK0zzd_EtwWriteTransfer](../../text/42/McTemplateK0zzd_EtwWriteTransfer_function_00424414.md) (function, `0x00424414`)
- `0x008DB7EC` → [RtlStringCbCopyW](../../text/43/RtlStringCbCopyW_function_0043B910.md) (function, `0x0043B910`)
- `0x008DB806` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (function, `0x004575EC`)
- `0x008DB81C` → [IoInvalidateDeviceRelations](../../text/49/IoInvalidateDeviceRelations_function_0049E160.md) (function, `0x0049E160`)
- `0x008DB85D` → [McTemplateK0zz_EtwWriteTransfer](../../text/5A/McTemplateK0zz_EtwWriteTransfer_function_005A9408.md) (function, `0x005A9408`)
- `0x008DB8BA` → [McTemplateK0zzqq_EtwWriteTransfer](../../text/5A/McTemplateK0zzqq_EtwWriteTransfer_function_005A95C0.md) (function, `0x005A95C0`)
- `0x008DB8C5` → [PiSwDeviceDereference](../94/PiSwDeviceDereference_function_0094E8A8.md) (function, `0x0094E8A8`)
- `0x008DB8CF` → [PiSwDeviceDereference](../94/PiSwDeviceDereference_function_0094E8A8.md) (function, `0x0094E8A8`)
- `0x008DB8DC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [PiSwStartCreate](../73/PiSwStartCreate_function_0073B2CC.md) at `0x0073B3CC`
- [PiSwIrpStartCreate](PiSwIrpStartCreate_function_008DA834.md) at `0x008DA8F4`

### Static image references
- `0x008DB3E7` → RVA `0x00EF012C` (`.data`; read)
- `0x008DB415` → RVA `0x00F8AB20` (`.data`; read)
- `0x008DB52D` → RVA `0x00F8AAA0` (`.data`; read)
- `0x008DB66B` → RVA `0x00EF012C` (`.data`; reference)
- `0x008DB67B` → RVA `0x000274B0` (`.rdata`; read)
- `0x008DB716` → RVA `0x005A9E60` (`PiSwIrpCancelStartCreate`; read)
- `0x008DB79E` → RVA `0x00026E70` (`.rdata`; read)
- `0x008DB849` → RVA `0x000271D0` (`.rdata`; read)
- `0x008DB893` → RVA `0x000274A0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x008DB41C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008DB421` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008DB463` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008DB534` → [RtlInsertElementGenericTableAvl](../../text/3E/RtlInsertElementGenericTableAvl_function_003EE510.md) (`PAGE` → `.text`)
  - `0x008DB5E9` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (`PAGE` → `.text`)
  - `0x008DB6A2` → [McTemplateK0zzqq_EtwWriteTransfer](../../text/5A/McTemplateK0zzqq_EtwWriteTransfer_function_005A95C0.md) (`PAGE` → `.text`)
  - `0x008DB6BE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008DB6F0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008DB700` → [IoInvalidateDeviceRelations](../../text/49/IoInvalidateDeviceRelations_function_0049E160.md) (`PAGE` → `.text`)
  - `0x008DB790` → [McTemplateK0zzzdzzq_EtwWriteTransfer](../../text/5A/McTemplateK0zzzdzzq_EtwWriteTransfer_function_005A98F8.md) (`PAGE` → `.text`)
  - `0x008DB7BA` → [McTemplateK0zzd_EtwWriteTransfer](../../text/42/McTemplateK0zzd_EtwWriteTransfer_function_00424414.md) (`PAGE` → `.text`)
  - `0x008DB7EC` → [RtlStringCbCopyW](../../text/43/RtlStringCbCopyW_function_0043B910.md) (`PAGE` → `.text`)
  - `0x008DB806` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (`PAGE` → `.text`)
  - `0x008DB81C` → [IoInvalidateDeviceRelations](../../text/49/IoInvalidateDeviceRelations_function_0049E160.md) (`PAGE` → `.text`)
  - `0x008DB85D` → [McTemplateK0zz_EtwWriteTransfer](../../text/5A/McTemplateK0zz_EtwWriteTransfer_function_005A9408.md) (`PAGE` → `.text`)
  - `0x008DB8BA` → [McTemplateK0zzqq_EtwWriteTransfer](../../text/5A/McTemplateK0zzqq_EtwWriteTransfer_function_005A95C0.md) (`PAGE` → `.text`)
  - `0x008DB8DC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x008DB671` → [sub_00B1C4F6](../B1/Unknown_function_00B1C4F6.md) (`tail-transfer`)
  - `0x008DB6AB` → [sub_00B1C4F6](../B1/Unknown_function_00B1C4F6.md) (`tail-transfer`)
  - `0x008DB83F` → [sub_00B1C4F6 + 0x35D](../B1/Unknown_function_00B1C4F6.md) (`tail-transfer`)
  - `0x008DB863` → [sub_00B1C4F6 + 0x35D](../B1/Unknown_function_00B1C4F6.md) (`tail-transfer`)
  - `0x008DB874` → [sub_00B1C4F6 + 0x390](../B1/Unknown_function_00B1C4F6.md) (`tail-transfer`)
  - `0x008DB87D` → [sub_00B1C4F6 + 0x390](../B1/Unknown_function_00B1C4F6.md) (`tail-transfer`)
  - `0x008DB889` → [sub_00B1C4F6 + 0x3A3](../B1/Unknown_function_00B1C4F6.md) (`tail-transfer`)
  - `0x008DB8C0` → [sub_00B1C4F6 + 0x3A3](../B1/Unknown_function_00B1C4F6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008DB398  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008DB39D  55                              push rbp
008DB39E  56                              push rsi
008DB39F  57                              push rdi
008DB3A0  41 54                           push r12
008DB3A2  41 55                           push r13
008DB3A4  41 56                           push r14
008DB3A6  41 57                           push r15
008DB3A8  48 8B EC                        mov rbp, rsp
008DB3AB  48 81 EC 80 00 00 00            sub rsp, 0x80
008DB3B2  33 C0                           xor eax, eax
008DB3B4  0F 57 C0                        xorps xmm0, xmm0
008DB3B7  44 8B E8                        mov r13d, eax
008DB3BA  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
008DB3BE  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
008DB3C2  44 8B F0                        mov r14d, eax
008DB3C5  44 8B E0                        mov r12d, eax
008DB3C8  88 45 48                        mov byte ptr [rbp + 0x48], al
008DB3CB  44 8A F8                        mov r15b, al
008DB3CE  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
008DB3D2  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
008DB3D6  48 8B F2                        mov rsi, rdx
008DB3D9  48 8B F9                        mov rdi, rcx
008DB3DC  E8 77 05 00 00                  call 0x1408db958
008DB3E1  8B D8                           mov ebx, eax
008DB3E3  85 C0                           test eax, eax
008DB3E5  78 47                           js 0x1408db42e
008DB3E7  F6 05 3E 4D 61 00 40            test byte ptr [rip + 0x614d3e], 0x40
008DB3EE  0F 85 67 03 00 00               jne 0x1408db75b
008DB3F4  E8 57 C9 01 00                  call 0x1408f7d50
008DB3F9  48 85 F6                        test rsi, rsi
008DB3FC  0F 85 8D 00 00 00               jne 0x1408db48f
008DB402  48 8D 4D D0                     lea rcx, [rbp - 0x30]
008DB406  E8 E1 04 00 00                  call 0x1408db8ec
008DB40B  8B D8                           mov ebx, eax
008DB40D  85 C0                           test eax, eax
008DB40F  0F 89 F0 00 00 00               jns 0x1408db505
008DB415  48 8D 0D 04 F7 6A 00            lea rcx, [rip + 0x6af704]
008DB41C  E8 EF 45 98 FF                  call 0x14025fa10
008DB421  E8 8A 24 98 FF                  call 0x14025d8b0
008DB426  85 DB                           test ebx, ebx
008DB428  0F 89 80 00 00 00               jns 0x1408db4ae
008DB42E  33 FF                           xor edi, edi
008DB430  48 85 F6                        test rsi, rsi
008DB433  0F 85 B1 00 00 00               jne 0x1408db4ea
008DB439  85 DB                           test ebx, ebx
008DB43B  0F 89 41 04 00 00               jns 0x1408db882
008DB441  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
008DB445  48 85 C9                        test rcx, rcx
008DB448  0F 85 77 04 00 00               jne 0x1408db8c5
008DB44E  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
008DB452  48 85 C9                        test rcx, rcx
008DB455  0F 85 74 04 00 00               jne 0x1408db8cf
008DB45B  4D 85 F6                        test r14, r14
008DB45E  74 08                           je 0x1408db468
008DB460  49 8B CE                        mov rcx, r14
008DB463  E8 E8 DE A1 FF                  call 0x1402f9350
008DB468  4D 85 E4                        test r12, r12
008DB46B  0F 85 68 04 00 00               jne 0x1408db8d9
008DB471  8B C3                           mov eax, ebx
008DB473  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
008DB47B  48 81 C4 80 00 00 00            add rsp, 0x80
008DB482  41 5F                           pop r15
008DB484  41 5E                           pop r14
008DB486  41 5D                           pop r13
008DB488  41 5C                           pop r12
008DB48A  5F                              pop rdi
008DB48B  5E                              pop rsi
008DB48C  5D                              pop rbp
008DB48D  C3                              ret
008DB48E  CC                              int3
008DB48F  4C 8B AE B8 00 00 00            mov r13, qword ptr [rsi + 0xb8]
008DB496  49 8B 45 30                     mov rax, qword ptr [r13 + 0x30]
008DB49A  4C 39 60 20                     cmp qword ptr [rax + 0x20], r12
008DB49E  0F 84 5E FF FF FF               je 0x1408db402
008DB4A4  BB BB 00 00 C0                  mov ebx, 0xc00000bb
008DB4A9  E9 67 FF FF FF                  jmp 0x1408db415
008DB4AE  45 84 FF                        test r15b, r15b
008DB4B1  0F 85 77 FF FF FF               jne 0x1408db42e
008DB4B7  4C 8B 47 70                     mov r8, qword ptr [rdi + 0x70]
008DB4BB  4D 85 C0                        test r8, r8
008DB4BE  0F 84 6A FF FF FF               je 0x1408db42e
008DB4C4  44 8B 4F 68                     mov r9d, dword ptr [rdi + 0x68]
008DB4C8  BA 01 00 00 00                  mov edx, 1
008DB4CD  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
008DB4D1  E8 16 AA 01 00                  call 0x1408f5eec
008DB4D6  3D 34 00 00 C0                  cmp eax, 0xc0000034
008DB4DB  8B D8                           mov ebx, eax
008DB4DD  BF 00 00 00 00                  mov edi, 0
008DB4E2  0F 44 DF                        cmove ebx, edi
008DB4E5  E9 46 FF FF FF                  jmp 0x1408db430
008DB4EA  85 DB                           test ebx, ebx
008DB4EC  0F 88 87 03 00 00               js 0x1408db879
008DB4F2  45 84 FF                        test r15b, r15b
008DB4F5  0F 84 6D 03 00 00               je 0x1408db868
008DB4FB  BB 03 01 00 00                  mov ebx, 0x103
008DB500  E9 3C FF FF FF                  jmp 0x1408db441
008DB505  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
008DB509  48 8B D7                        mov rdx, rdi
008DB50C  48 83 C1 08                     add rcx, 8
008DB510  E8 6F 07 00 00                  call 0x1408dbc84
008DB515  8B D8                           mov ebx, eax
008DB517  85 C0                           test eax, eax
008DB519  0F 88 F6 FE FF FF               js 0x1408db415
008DB51F  4C 8D 4D 48                     lea r9, [rbp + 0x48]
008DB523  41 B8 08 00 00 00               mov r8d, 8
008DB529  48 8D 55 D0                     lea rdx, [rbp - 0x30]
008DB52D  48 8D 0D 6C F5 6A 00            lea rcx, [rip + 0x6af56c]
008DB534  E8 D7 2F B1 FF                  call 0x1403ee510
008DB539  45 33 DB                        xor r11d, r11d
008DB53C  48 85 C0                        test rax, rax
008DB53F  0F 84 E4 02 00 00               je 0x1408db829
008DB545  F6 05 E0 4B 61 00 40            test byte ptr [rip + 0x614be0], 0x40
008DB54C  48 8B 08                        mov rcx, qword ptr [rax]
008DB54F  8A 5D 48                        mov bl, byte ptr [rbp + 0x48]
008DB552  48 89 4D 58                     mov qword ptr [rbp + 0x58], rcx
008DB556  0F 85 3E 02 00 00               jne 0x1408db79a
008DB55C  84 DB                           test bl, bl
008DB55E  0F 84 F1 00 00 00               je 0x1408db655
008DB564  4C 89 5D D0                     mov qword ptr [rbp - 0x30], r11
008DB568  F0 FF 01                        lock inc dword ptr [rcx]
008DB56B  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
008DB56F  48 8B D7                        mov rdx, rdi
008DB572  48 83 C1 18                     add rcx, 0x18
008DB576  E8 61 FD FF FF                  call 0x1408db2dc
008DB57B  45 33 DB                        xor r11d, r11d
008DB57E  8B D8                           mov ebx, eax
008DB580  85 C0                           test eax, eax
008DB582  0F 88 A6 02 00 00               js 0x1408db82e
008DB588  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008DB58C  8B 4F 58                        mov ecx, dword ptr [rdi + 0x58]
008DB58F  89 88 A0 00 00 00               mov dword ptr [rax + 0xa0], ecx
008DB595  4C 39 5F 60                     cmp qword ptr [rdi + 0x60], r11
008DB599  0F 85 11 01 00 00               jne 0x1408db6b0
008DB59F  4C 8B 4D 58                     mov r9, qword ptr [rbp + 0x58]
008DB5A3  48 8B 57 70                     mov rdx, qword ptr [rdi + 0x70]
008DB5A7  8B 4F 68                        mov ecx, dword ptr [rdi + 0x68]
008DB5AA  49 8D 81 A8 00 00 00            lea rax, [r9 + 0xa8]
008DB5B1  49 81 C1 B0 00 00 00            add r9, 0xb0
008DB5B8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DB5BD  E8 36 FB FF FF                  call 0x1408db0f8
008DB5C2  45 33 DB                        xor r11d, r11d
008DB5C5  8B D8                           mov ebx, eax
008DB5C7  85 C0                           test eax, eax
008DB5C9  0F 88 5F 02 00 00               js 0x1408db82e
008DB5CF  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
008DB5D3  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008DB5D7  E8 B8 F3 FF FF                  call 0x1408da994
008DB5DC  45 33 DB                        xor r11d, r11d
008DB5DF  8B D8                           mov ebx, eax
008DB5E1  85 C0                           test eax, eax
008DB5E3  0F 88 45 02 00 00               js 0x1408db82e
008DB5E9  E8 72 7F B5 FF                  call 0x140433560
008DB5EE  48 8B C8                        mov rcx, rax
008DB5F1  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008DB5F5  89 88 A4 00 00 00               mov dword ptr [rax + 0xa4], ecx
008DB5FB  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
008DB5FF  BA 44 66 6C 74                  mov edx, 0x746c6644
008DB604  48 8B 49 70                     mov rcx, qword ptr [rcx + 0x70]
008DB608  E8 83 BE 00 00                  call 0x1408e7490
008DB60D  4C 8B F0                        mov r14, rax
008DB610  45 33 DB                        xor r11d, r11d
008DB613  41 B7 01                        mov r15b, 1
008DB616  48 85 F6                        test rsi, rsi
008DB619  0F 85 EE 00 00 00               jne 0x1408db70d
008DB61F  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008DB623  83 48 04 01                     or dword ptr [rax + 4], 1
008DB627  48 85 F6                        test rsi, rsi
008DB62A  0F 85 16 01 00 00               jne 0x1408db746
008DB630  41 BD 05 00 00 00               mov r13d, 5
008DB636  4D 85 F6                        test r14, r14
008DB639  0F 85 BB 00 00 00               jne 0x1408db6fa
008DB63F  4D 85 E4                        test r12, r12
008DB642  0F 85 CE 01 00 00               jne 0x1408db816
008DB648  85 DB                           test ebx, ebx
008DB64A  0F 89 C5 FD FF FF               jns 0x1408db415
008DB650  E9 D9 01 00 00                  jmp 0x1408db82e
008DB655  F0 FF 01                        lock inc dword ptr [rcx]
008DB658  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
008DB65C  41 8B 48 04                     mov ecx, dword ptr [r8 + 4]
008DB660  F6 C1 01                        test cl, 1
008DB663  0F 85 62 01 00 00               jne 0x1408db7cb
008DB669  B3 40                           mov bl, 0x40
008DB66B  84 1D BB 4A 61 00               test byte ptr [rip + 0x614abb], bl
008DB671  0F 84 7F 0E 24 00               je 0x140b1c4f6
008DB677  4D 39 58 78                     cmp qword ptr [r8 + 0x78], r11
008DB67B  48 8D 15 2E BE 74 FF            lea rdx, [rip - 0x8b41d2]
008DB682  4D 8B 48 08                     mov r9, qword ptr [r8 + 8]
008DB686  41 8B C3                        mov eax, r11d
008DB689  0F 95 C0                        setne al
008DB68C  D1 E9                           shr ecx, 1
008DB68E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008DB692  83 E1 01                        and ecx, 1
008DB695  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
008DB699  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
008DB69D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DB6A2  E8 19 DF CC FF                  call 0x1405a95c0
008DB6A7  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
008DB6AB  E9 46 0E 24 00                  jmp 0x140b1c4f6
008DB6B0  8B 57 58                        mov edx, dword ptr [rdi + 0x58]
008DB6B3  B9 00 01 00 00                  mov ecx, 0x100
008DB6B8  41 B8 50 6E 70 57               mov r8d, 0x57706e50
008DB6BE  E8 2D 6A 2A 00                  call 0x140b820f0
008DB6C3  48 8B C8                        mov rcx, rax
008DB6C6  45 33 DB                        xor r11d, r11d
008DB6C9  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008DB6CD  48 89 88 98 00 00 00            mov qword ptr [rax + 0x98], rcx
008DB6D4  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008DB6D8  48 8B 88 98 00 00 00            mov rcx, qword ptr [rax + 0x98]
008DB6DF  48 85 C9                        test rcx, rcx
008DB6E2  0F 84 41 01 00 00               je 0x1408db829
008DB6E8  44 8B 47 58                     mov r8d, dword ptr [rdi + 0x58]
008DB6EC  48 8B 57 60                     mov rdx, qword ptr [rdi + 0x60]
008DB6F0  E8 4B B1 DE FF                  call 0x1406c6840
008DB6F5  E9 A5 FE FF FF                  jmp 0x1408db59f
008DB6FA  41 8B D5                        mov edx, r13d
008DB6FD  49 8B CE                        mov rcx, r14
008DB700  E8 5B 2A BC FF                  call 0x14049e160
008DB705  45 33 DB                        xor r11d, r11d
008DB708  E9 32 FF FF FF                  jmp 0x1408db63f
008DB70D  45 84 FF                        test r15b, r15b
008DB710  0F 84 C6 00 00 00               je 0x1408db7dc
008DB716  48 8D 05 43 E7 CC FF            lea rax, [rip - 0x3318bd]
008DB71D  48 87 46 68                     xchg qword ptr [rsi + 0x68], rax
008DB721  44 38 5E 44                     cmp byte ptr [rsi + 0x44], r11b
008DB725  0F 85 AA 00 00 00               jne 0x1408db7d5
008DB72B  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008DB72F  48 89 B0 90 00 00 00            mov qword ptr [rax + 0x90], rsi
008DB736  48 8B 86 B8 00 00 00            mov rax, qword ptr [rsi + 0xb8]
008DB73D  80 48 03 01                     or byte ptr [rax + 3], 1
008DB741  E9 D9 FE FF FF                  jmp 0x1408db61f
008DB746  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
008DB74A  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008DB74E  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
008DB752  4C 89 5D 58                     mov qword ptr [rbp + 0x58], r11
008DB756  E9 D5 FE FF FF                  jmp 0x1408db630
008DB75B  8B 47 68                        mov eax, dword ptr [rdi + 0x68]
008DB75E  4C 8B 0F                        mov r9, qword ptr [rdi]
008DB761  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008DB765  48 8B 47 50                     mov rax, qword ptr [rdi + 0x50]
008DB769  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008DB76E  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
008DB772  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008DB777  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
008DB77A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008DB77E  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008DB782  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008DB787  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008DB78B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DB790  E8 63 E1 CC FF                  call 0x1405a98f8
008DB795  E9 5A FC FF FF                  jmp 0x1408db3f4
008DB79A  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
008DB79E  48 8D 15 CB B6 74 FF            lea rdx, [rip - 0x8b4935]
008DB7A5  41 8B C3                        mov eax, r11d
008DB7A8  84 DB                           test bl, bl
008DB7AA  0F 94 C0                        sete al
008DB7AD  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008DB7B1  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
008DB7B5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DB7BA  E8 55 8C B4 FF                  call 0x140424414
008DB7BF  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
008DB7C3  45 33 DB                        xor r11d, r11d
008DB7C6  E9 91 FD FF FF                  jmp 0x1408db55c
008DB7CB  BB 35 00 00 C0                  mov ebx, 0xc0000035
008DB7D0  E9 40 FC FF FF                  jmp 0x1408db415
008DB7D5  BB 20 01 00 C0                  mov ebx, 0xc0000120
008DB7DA  EB 52                           jmp 0x1408db82e
008DB7DC  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
008DB7E0  41 8B 55 08                     mov edx, dword ptr [r13 + 8]
008DB7E4  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
008DB7E8  4D 8B 40 50                     mov r8, qword ptr [r8 + 0x50]
008DB7EC  E8 1F 01 B6 FF                  call 0x14043b910
008DB7F1  45 33 DB                        xor r11d, r11d
008DB7F4  8B D8                           mov ebx, eax
008DB7F6  85 C0                           test eax, eax
008DB7F8  78 34                           js 0x1408db82e
008DB7FA  41 8B 55 08                     mov edx, dword ptr [r13 + 8]
008DB7FE  4C 8D 45 E0                     lea r8, [rbp - 0x20]
008DB802  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
008DB806  E8 E1 BD B7 FF                  call 0x1404575ec
008DB80B  8B D8                           mov ebx, eax
008DB80D  85 C0                           test eax, eax
008DB80F  78 1D                           js 0x1408db82e
008DB811  E9 09 FE FF FF                  jmp 0x1408db61f
008DB816  41 8B D5                        mov edx, r13d
008DB819  49 8B CC                        mov rcx, r12
008DB81C  E8 3F 29 BC FF                  call 0x14049e160
008DB821  45 33 DB                        xor r11d, r11d
008DB824  E9 1F FE FF FF                  jmp 0x1408db648
008DB829  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008DB82E  44 38 5D 48                     cmp byte ptr [rbp + 0x48], r11b
008DB832  0F 84 DD FB FF FF               je 0x1408db415
008DB838  F6 05 ED 48 61 00 40            test byte ptr [rip + 0x6148ed], 0x40
008DB83F  0F 84 0E 10 24 00               je 0x140b1c853
008DB845  4C 8B 4D 58                     mov r9, qword ptr [rbp + 0x58]
008DB849  48 8D 15 80 B9 74 FF            lea rdx, [rip - 0x8b4680]
008DB850  49 8B 41 10                     mov rax, qword ptr [r9 + 0x10]
008DB854  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
008DB858  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DB85D  E8 A6 DB CC FF                  call 0x1405a9408
008DB862  90                              nop
008DB863  E9 EB 0F 24 00                  jmp 0x140b1c853
008DB868  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008DB86C  48 83 C0 02                     add rax, 2
008DB870  48 89 46 38                     mov qword ptr [rsi + 0x38], rax
008DB874  E9 0D 10 24 00                  jmp 0x140b1c886
008DB879  48 89 7E 38                     mov qword ptr [rsi + 0x38], rdi
008DB87D  E9 04 10 24 00                  jmp 0x140b1c886
008DB882  F6 05 A3 48 61 00 40            test byte ptr [rip + 0x6148a3], 0x40
008DB889  0F 84 0A 10 24 00               je 0x140b1c899
008DB88F  4C 8B 4D 58                     mov r9, qword ptr [rbp + 0x58]
008DB893  48 8D 15 06 BC 74 FF            lea rdx, [rip - 0x8b43fa]
008DB89A  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
008DB8A2  41 8B 81 B4 00 00 00            mov eax, dword ptr [r9 + 0xb4]
008DB8A9  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008DB8AD  49 8B 41 10                     mov rax, qword ptr [r9 + 0x10]
008DB8B1  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
008DB8B5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008DB8BA  E8 01 DD CC FF                  call 0x1405a95c0
008DB8BF  90                              nop
008DB8C0  E9 D4 0F 24 00                  jmp 0x140b1c899
008DB8C5  E8 DE 2F 07 00                  call 0x14094e8a8
008DB8CA  E9 7F FB FF FF                  jmp 0x1408db44e
008DB8CF  E8 D4 2F 07 00                  call 0x14094e8a8
008DB8D4  E9 82 FB FF FF                  jmp 0x1408db45b
008DB8D9  49 8B CC                        mov rcx, r12
008DB8DC  E8 6F DA A1 FF                  call 0x1402f9350
008DB8E1  E9 8B FB FF FF                  jmp 0x1408db471
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwIrpStartCreateWorker(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (128);
    result = 0;
    v_stack_m68 = 0;
    v_stack_p20 = 0;
    v_stack_p10 = 0;
    v_stack_m58 = 0;
    v_stack_m50 = v_xmm0;
    result = PiSwValidateCreateData(a1, a2, a3, a4);
    if (sign_flag) goto loc_008DB42E;
    if (((*(unsigned __int8 *)(v_rip + 6376766)) & (64)) != 0) goto loc_008DB75B;
loc_008DB3F4:
    result = PiSwLock(a1, a2, a3, a4);
    if (a2 != 0) goto loc_008DB48F;
loc_008DB402:
    result = PiSwDeviceCreate(v_stack_m68, a2, a3, a4);
    if (!sign_flag) goto loc_008DB505;
loc_008DB415:
    result = ExReleaseResourceLite(v_rip + 7010052, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 7010052, a2, a3, a4);
    if (!sign_flag) goto loc_008DB4AE;
loc_008DB42E:
    v_rdi = 0;
loc_008DB430:
    if (a2 != 0) goto loc_008DB4EA;
    if (!sign_flag) goto loc_008DB882;
loc_008DB441:
    if (v_stack_p20 != 0) goto loc_008DB8C5;
loc_008DB44E:
    if (v_stack_m68 != 0) goto loc_008DB8CF;
loc_008DB45B:
    if (0 != 0) {
        a1 = 0;
        result = ObfDereferenceObject(a1, a2, a3, a4);
    }
    if (0 != 0) goto loc_008DB8D9;
loc_008DB471:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008DB48F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 48) + 32)) == 0) goto loc_008DB402;
    goto loc_008DB415;
loc_008DB4AE:
    if (0 != 0) goto loc_008DB42E;
    if (*(unsigned __int64 *)(v_rdi + 112) == 0) goto loc_008DB42E;
    result = PiSwPropertySet(*(unsigned __int64 *)(a2 + 24), 1, *(unsigned __int64 *)(v_rdi + 112), (unsigned int)(*(unsigned int *)(v_rdi + 104)));
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 0xC0000034ULL) { v_rbx = 0; }
    goto loc_008DB430;
loc_008DB4EA:
    if (sign_flag) goto loc_008DB879;
    if (0 == 0) goto loc_008DB868;
    goto loc_008DB441;
loc_008DB505:
    a1 = (v_stack_m68) + (8);
    result = PiSwInstanceInfoInit(a1, 0, *(unsigned __int64 *)(v_rdi + 112), (unsigned int)(*(unsigned int *)(v_rdi + 104)));
    if (sign_flag) goto loc_008DB415;
    result = RtlInsertElementGenericTableAvl(v_rip + 7009644, v_stack_m68, 8, v_stack_p10);
    v_r11 = 0;
    if (result == 0) goto loc_008DB829;
    v_stack_p20 = *(unsigned __int64 *)(result);
    if (((*(unsigned __int8 *)(v_rip + 6376416)) & (64)) != 0) goto loc_008DB79A;
loc_008DB55C:
    if ((unsigned __int8)(v_stack_p10) == 0) goto loc_008DB655;
    v_stack_m68 = 0;
    a1 = (v_stack_p20) + (24);
    result = PiSwPnPInfoInit(a1, 0, 8, v_stack_p10);
    v_r11 = 0;
    if (sign_flag) goto loc_008DB82E;
    *(unsigned int *)(v_stack_p20 + 160) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 88)));
    if ((*(unsigned __int64 *)(0 + 96)) != 0) goto loc_008DB6B0;
loc_008DB59F:
    a4 = (v_stack_p20) + (176);
    v_stack_p20 = v_stack_p20 + 168;
    result = PnpCopyDevPropertyArray((unsigned int)(*(unsigned int *)(0 + 104)), *(unsigned __int64 *)(0 + 112), 8, a4);
    v_r11 = 0;
    if (sign_flag) goto loc_008DB82E;
    result = PiSwBusRelationAdd(*(unsigned __int64 *)(0 + 8), v_stack_p20, 8, a4);
    v_r11 = 0;
    if (sign_flag) goto loc_008DB82E;
    result = PsGetCurrentProcessId(*(unsigned __int64 *)(0 + 8), v_stack_p20, 8, a4);
    *(unsigned int *)(v_stack_p20 + 164) = (unsigned int)(result);
    result = PnpDeviceObjectFromDeviceInstanceWithTag(*(unsigned __int64 *)(v_stack_p20 + 112), (unsigned int)(0x746C6644ULL), 8, a4);
    v_r11 = 0;
    if (a2 != 0) goto loc_008DB70D;
loc_008DB61F:
    if (a2 != 0) goto loc_008DB746;
loc_008DB630:
    if (result != 0) goto loc_008DB6FA;
loc_008DB63F:
    if (0 != 0) goto loc_008DB816;
loc_008DB648:
    if (!sign_flag) goto loc_008DB415;
    goto loc_008DB82E;
loc_008DB655:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20 + 4)))) & (1)) != 0) goto loc_008DB7CB;
    result = ((*(unsigned __int64 *)(v_stack_p20 + 120)) != 0) ? 1 : 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 4))) >> (1));
    v_stack_p30 = (unsigned int)(result);
    a1 = (unsigned int)((a1) & (1));
    v_stack_p28 = (unsigned int)(a1);
    v_stack_p20 = *(unsigned __int64 *)(v_stack_p20 + 16);
    result = McTemplateK0zzqq_EtwWriteTransfer(a1, v_rip - 9126354, v_stack_p20, *(unsigned __int64 *)(v_stack_p20 + 8));
loc_008DB6B0:
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(0 + 88)), (unsigned int)(0x57706E50ULL), *(unsigned __int64 *)(v_stack_p20 + 8));
    v_r11 = 0;
    *(unsigned __int64 *)(v_stack_p20 + 152) = result;
    if (*(unsigned __int64 *)(v_stack_p20 + 152) == 0) goto loc_008DB829;
    result = memcpy(*(unsigned __int64 *)(v_stack_p20 + 152), *(unsigned __int64 *)(0 + 96), (unsigned int)(*(unsigned int *)(0 + 88)), *(unsigned __int64 *)(v_stack_p20 + 8));
    goto loc_008DB59F;
loc_008DB6FA:
    result = IoInvalidateDeviceRelations(result, 5, (unsigned int)(*(unsigned int *)(0 + 88)), *(unsigned __int64 *)(v_stack_p20 + 8));
    v_r11 = 0;
    goto loc_008DB63F;
loc_008DB70D:
    if (1 == 0) goto loc_008DB7DC;
    if ((*(unsigned __int8 *)(a2 + 68)) != 0) goto loc_008DB7D5;
    *(unsigned __int64 *)(v_stack_p20 + 144) = a2;
    goto loc_008DB61F;
loc_008DB746:
    *(unsigned __int64 *)(*(unsigned __int64 *)(5 + 48) + 32) = v_stack_p20;
    v_stack_p20 = 0;
    goto loc_008DB630;
loc_008DB75B:
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 104)));
    v_stack_p40 = *(unsigned __int64 *)(0 + 80);
    v_stack_p38 = *(unsigned __int64 *)(0 + 72);
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 64)));
    v_stack_p28 = *(unsigned __int64 *)(0 + 8);
    v_stack_p20 = *(unsigned __int64 *)(0 + 16);
    result = McTemplateK0zzzdzzq_EtwWriteTransfer(*(unsigned __int64 *)(5 + 48), 5, (unsigned int)(*(unsigned int *)(0 + 88)), *(unsigned __int64 *)(0));
    goto loc_008DB3F4;
loc_008DB79A:
    result = (64 == 0) ? 1 : 0;
    v_stack_p28 = (unsigned int)(result);
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(5 + 48) + 16);
    result = McTemplateK0zzd_EtwWriteTransfer(*(unsigned __int64 *)(5 + 48), v_rip - 9128245, (unsigned int)(*(unsigned int *)(0 + 88)), *(unsigned __int64 *)(*(unsigned __int64 *)(5 + 48) + 8));
    v_r11 = 0;
    goto loc_008DB55C;
loc_008DB7CB:
    goto loc_008DB415;
loc_008DB7D5:
    goto loc_008DB82E;
loc_008DB7DC:
    result = RtlStringCbCopyW(*(unsigned __int64 *)(a2 + 24), (unsigned int)(*(unsigned int *)(5 + 8)), *(unsigned __int64 *)(v_stack_p20 + 80), *(unsigned __int64 *)(*(unsigned __int64 *)(5 + 48) + 8));
    v_r11 = 0;
    if (sign_flag) goto loc_008DB82E;
    result = RtlStringCbLengthW(*(unsigned __int64 *)(a2 + 24), (unsigned int)(*(unsigned int *)(5 + 8)), v_stack_m58, *(unsigned __int64 *)(*(unsigned __int64 *)(5 + 48) + 8));
    if (sign_flag) goto loc_008DB82E;
    goto loc_008DB61F;
loc_008DB816:
    result = IoInvalidateDeviceRelations(0, 5, v_stack_m58, *(unsigned __int64 *)(*(unsigned __int64 *)(5 + 48) + 8));
    v_r11 = 0;
    goto loc_008DB648;
loc_008DB829:
loc_008DB82E:
    if (v_stack_p10 == 0) goto loc_008DB415;
    v_stack_p20 = *(unsigned __int64 *)(v_stack_p20 + 16);
    result = McTemplateK0zz_EtwWriteTransfer(0, v_rip - 9127552, v_stack_m58, *(unsigned __int64 *)(v_stack_p20 + 8));
loc_008DB868:
    result = (v_stack_m58) + (2);
    *(unsigned __int64 *)(a2 + 56) = result;
loc_008DB879:
    *(unsigned __int64 *)(a2 + 56) = 0;
loc_008DB882:
    v_stack_p30 = 1;
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 180)));
    v_stack_p20 = *(unsigned __int64 *)(v_stack_p20 + 16);
    result = McTemplateK0zzqq_EtwWriteTransfer(0, v_rip - 9126906, v_stack_m58, *(unsigned __int64 *)(v_stack_p20 + 8));
loc_008DB8C5:
    result = PiSwDeviceDereference(0, v_rip - 9126906, v_stack_m58, *(unsigned __int64 *)(v_stack_p20 + 8));
    goto loc_008DB44E;
loc_008DB8CF:
    result = PiSwDeviceDereference(0, v_rip - 9126906, v_stack_m58, *(unsigned __int64 *)(v_stack_p20 + 8));
    goto loc_008DB45B;
loc_008DB8D9:
    result = ObfDereferenceObject(0, v_rip - 9126906, v_stack_m58, *(unsigned __int64 *)(v_stack_p20 + 8));
    goto loc_008DB471;
}
```

## 5. (Beta) C Style

```c
int64_t PiSwIrpStartCreateWorker(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint8_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (128);
    result = 0;
    v_stack_m68 = 0;
    v_stack_p20 = 0;
    v_stack_p10 = 0;
    v_stack_m58 = 0;
    v_stack_m50 = v_xmm0;
    result = PiSwValidateCreateData(Arg1, Arg2, a3, a4);
    if (sign_flag) goto loc_008DB42E;
    if (((*(uint8_t *)(v_rip + 0x614D3E)) & (64)) != 0) goto loc_008DB75B;
loc_008DB3F4:
    result = PiSwLock(Arg1, Arg2, a3, a4);
    if (Arg2 != 0) goto loc_008DB48F;
loc_008DB402:
    result = PiSwDeviceCreate(v_stack_m68, Arg2, a3, a4);
    if (!sign_flag) goto loc_008DB505;
loc_008DB415:
    result = ExReleaseResourceLite(v_rip + 7010052, Arg2, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 7010052, Arg2, a3, a4);
    if (!sign_flag) goto loc_008DB4AE;
loc_008DB42E:
    local_rdi = 0;
loc_008DB430:
    if (Arg2 != 0) goto loc_008DB4EA;
    if (!sign_flag) goto loc_008DB882;
loc_008DB441:
    if (v_stack_p20 != 0) goto loc_008DB8C5;
loc_008DB44E:
    if (v_stack_m68 != 0) goto loc_008DB8CF;
loc_008DB45B:
    if (0 != 0) {
        Arg1 = 0;
        result = ObfDereferenceObject(Arg1, Arg2, a3, a4);
    }
    if (0 != 0) goto loc_008DB8D9;
loc_008DB471:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008DB48F:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0xB8) + 0x30) + 0x20)) == 0) goto loc_008DB402;
    goto loc_008DB415;
loc_008DB4AE:
    if (0 != 0) goto loc_008DB42E;
    if (*(uint64_t *)(local_rdi + 0x70) == 0) goto loc_008DB42E;
    result = PiSwPropertySet(*(uint64_t *)(Arg2 + 0x18), 1, *(uint64_t *)(local_rdi + 0x70), (uint32_t)(*(uint32_t *)(local_rdi + 0x68)));
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 0xC0000034ULL) { local_rbx = 0; }
    goto loc_008DB430;
loc_008DB4EA:
    if (sign_flag) goto loc_008DB879;
    if (0 == 0) goto loc_008DB868;
    goto loc_008DB441;
loc_008DB505:
    Arg1 = (v_stack_m68) + (8);
    result = PiSwInstanceInfoInit(Arg1, 0, *(uint64_t *)(local_rdi + 0x70), (uint32_t)(*(uint32_t *)(local_rdi + 0x68)));
    if (sign_flag) goto loc_008DB415;
    result = RtlInsertElementGenericTableAvl(v_rip + 7009644, v_stack_m68, 8, v_stack_p10);
    local_r11 = 0;
    if (result == 0) goto loc_008DB829;
    v_stack_p20 = *(uint64_t *)(result);
    if (((*(uint8_t *)(v_rip + 0x614BE0)) & (64)) != 0) goto loc_008DB79A;
loc_008DB55C:
    if ((uint8_t)(v_stack_p10) == 0) goto loc_008DB655;
    v_stack_m68 = 0;
    Arg1 = (v_stack_p20) + (24);
    result = PiSwPnPInfoInit(Arg1, 0, 8, v_stack_p10);
    local_r11 = 0;
    if (sign_flag) goto loc_008DB82E;
    *(uint32_t *)(v_stack_p20 + 0xA0) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x58)));
    if ((*(uint64_t *)(0 + 0x60)) != 0) goto loc_008DB6B0;
loc_008DB59F:
    a4 = (v_stack_p20) + (176);
    v_stack_p20 = v_stack_p20 + 168;
    result = PnpCopyDevPropertyArray((uint32_t)(*(uint32_t *)(0 + 0x68)), *(uint64_t *)(0 + 0x70), 8, a4);
    local_r11 = 0;
    if (sign_flag) goto loc_008DB82E;
    result = PiSwBusRelationAdd(*(uint64_t *)(0 + 0x8), v_stack_p20, 8, a4);
    local_r11 = 0;
    if (sign_flag) goto loc_008DB82E;
    result = PsGetCurrentProcessId(*(uint64_t *)(0 + 0x8), v_stack_p20, 8, a4);
    *(uint32_t *)(v_stack_p20 + 0xA4) = (uint32_t)(result);
    result = PnpDeviceObjectFromDeviceInstanceWithTag(*(uint64_t *)(v_stack_p20 + 0x70), (uint32_t)(0x746C6644ULL), 8, a4);
    local_r11 = 0;
    if (Arg2 != 0) goto loc_008DB70D;
loc_008DB61F:
    if (Arg2 != 0) goto loc_008DB746;
loc_008DB630:
    if (result != 0) goto loc_008DB6FA;
loc_008DB63F:
    if (0 != 0) goto loc_008DB816;
loc_008DB648:
    if (!sign_flag) goto loc_008DB415;
    goto loc_008DB82E;
loc_008DB655:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x4)))) & (1)) != 0) goto loc_008DB7CB;
    result = ((*(uint64_t *)(v_stack_p20 + 0x78)) != 0) ? 1 : 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x4))) >> (1));
    v_stack_p30 = (uint32_t)(result);
    Arg1 = (uint32_t)((Arg1) & (1));
    v_stack_p28 = (uint32_t)(Arg1);
    v_stack_p20 = *(uint64_t *)(v_stack_p20 + 0x10);
    result = McTemplateK0zzqq_EtwWriteTransfer(Arg1, v_rip - 9126354, v_stack_p20, *(uint64_t *)(v_stack_p20 + 0x8));
loc_008DB6B0:
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(0 + 0x58)), (uint32_t)(0x57706E50ULL), *(uint64_t *)(v_stack_p20 + 0x8));
    local_r11 = 0;
    *(uint64_t *)(v_stack_p20 + 0x98) = result;
    if (*(uint64_t *)(v_stack_p20 + 0x98) == 0) goto loc_008DB829;
    result = memcpy(*(uint64_t *)(v_stack_p20 + 0x98), *(uint64_t *)(0 + 0x60), (uint32_t)(*(uint32_t *)(0 + 0x58)), *(uint64_t *)(v_stack_p20 + 0x8));
    goto loc_008DB59F;
loc_008DB6FA:
    result = IoInvalidateDeviceRelations(result, 5, (uint32_t)(*(uint32_t *)(0 + 0x58)), *(uint64_t *)(v_stack_p20 + 0x8));
    local_r11 = 0;
    goto loc_008DB63F;
loc_008DB70D:
    if (1 == 0) goto loc_008DB7DC;
    if ((*(uint8_t *)(Arg2 + 0x44)) != 0) goto loc_008DB7D5;
    *(uint64_t *)(v_stack_p20 + 0x90) = Arg2;
    goto loc_008DB61F;
loc_008DB746:
    *(uint64_t *)(*(uint64_t *)(5 + 0x30) + 0x20) = v_stack_p20;
    v_stack_p20 = 0;
    goto loc_008DB630;
loc_008DB75B:
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x68)));
    v_stack_p40 = *(uint64_t *)(0 + 0x50);
    v_stack_p38 = *(uint64_t *)(0 + 0x48);
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x40)));
    v_stack_p28 = *(uint64_t *)(0 + 0x8);
    v_stack_p20 = *(uint64_t *)(0 + 0x10);
    result = McTemplateK0zzzdzzq_EtwWriteTransfer(*(uint64_t *)(5 + 0x30), 5, (uint32_t)(*(uint32_t *)(0 + 0x58)), *(uint64_t *)(0));
    goto loc_008DB3F4;
loc_008DB79A:
    result = (64 == 0) ? 1 : 0;
    v_stack_p28 = (uint32_t)(result);
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(5 + 0x30) + 0x10);
    result = McTemplateK0zzd_EtwWriteTransfer(*(uint64_t *)(5 + 0x30), v_rip - 9128245, (uint32_t)(*(uint32_t *)(0 + 0x58)), *(uint64_t *)(*(uint64_t *)(5 + 0x30) + 0x8));
    local_r11 = 0;
    goto loc_008DB55C;
loc_008DB7CB:
    goto loc_008DB415;
loc_008DB7D5:
    goto loc_008DB82E;
loc_008DB7DC:
    result = RtlStringCbCopyW(*(uint64_t *)(Arg2 + 0x18), (uint32_t)(*(uint32_t *)(5 + 0x8)), *(uint64_t *)(v_stack_p20 + 0x50), *(uint64_t *)(*(uint64_t *)(5 + 0x30) + 0x8));
    local_r11 = 0;
    if (sign_flag) goto loc_008DB82E;
    result = RtlStringCbLengthW(*(uint64_t *)(Arg2 + 0x18), (uint32_t)(*(uint32_t *)(5 + 0x8)), v_stack_m58, *(uint64_t *)(*(uint64_t *)(5 + 0x30) + 0x8));
    if (sign_flag) goto loc_008DB82E;
    goto loc_008DB61F;
loc_008DB816:
    result = IoInvalidateDeviceRelations(0, 5, v_stack_m58, *(uint64_t *)(*(uint64_t *)(5 + 0x30) + 0x8));
    local_r11 = 0;
    goto loc_008DB648;
loc_008DB829:
loc_008DB82E:
    if (v_stack_p10 == 0) goto loc_008DB415;
    v_stack_p20 = *(uint64_t *)(v_stack_p20 + 0x10);
    result = McTemplateK0zz_EtwWriteTransfer(0, v_rip - 9127552, v_stack_m58, *(uint64_t *)(v_stack_p20 + 0x8));
loc_008DB868:
    result = (v_stack_m58) + (2);
    *(uint64_t *)(Arg2 + 0x38) = result;
loc_008DB879:
    *(uint64_t *)(Arg2 + 0x38) = 0;
loc_008DB882:
    v_stack_p30 = 1;
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0xB4)));
    v_stack_p20 = *(uint64_t *)(v_stack_p20 + 0x10);
    result = McTemplateK0zzqq_EtwWriteTransfer(0, v_rip - 9126906, v_stack_m58, *(uint64_t *)(v_stack_p20 + 0x8));
loc_008DB8C5:
    result = PiSwDeviceDereference(0, v_rip - 9126906, v_stack_m58, *(uint64_t *)(v_stack_p20 + 0x8));
    goto loc_008DB44E;
loc_008DB8CF:
    result = PiSwDeviceDereference(0, v_rip - 9126906, v_stack_m58, *(uint64_t *)(v_stack_p20 + 0x8));
    goto loc_008DB45B;
loc_008DB8D9:
    result = ObfDereferenceObject(0, v_rip - 9126906, v_stack_m58, *(uint64_t *)(v_stack_p20 + 0x8));
    goto loc_008DB471;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `32` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DB398&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
