# IopRegisterDeviceInterface

- RVA: `0x009501B0`–`0x0095072D` (길이 `1,405` bytes)
- VA: `0x00000001409501B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00091C0C`
- 디코드: `343`개 명령, `1,405/1,405` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00950242` → [PnpStringFromGuid](../8F/PnpStringFromGuid_function_008F5A2C.md) (function, `0x008F5A2C`)
- `0x00950269` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009502A5` → [CmGetDeviceInterfaceName](../8F/CmGetDeviceInterfaceName_function_008F3870.md) (function, `0x008F3870`)
- `0x009502EB` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00950301` → [PiDmObjectManagerAcquireSharedLock](PiDmObjectManagerAcquireSharedLock_function_009511A0.md) (function, `0x009511A0`)
- `0x0095030C` → [PiDmLookupObject](PiDmLookupObject_function_00951360.md) (function, `0x00951360`)
- `0x00950324` → [PiDmObjectManagerReleaseLock](PiDmObjectManagerReleaseLock_function_0095111C.md) (function, `0x0095111C`)
- `0x00950342` → [PiDmAddCacheReferenceForObject](PiDmAddCacheReferenceForObject_function_00950FB4.md) (function, `0x00950FB4`)
- `0x00950362` → [PiDmAddCacheReferenceForObject](PiDmAddCacheReferenceForObject_function_00950FB4.md) (function, `0x00950FB4`)
- `0x009503BC` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009503E6` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x009503F9` → [PnpStringFromGuid](../8F/PnpStringFromGuid_function_008F5A2C.md) (function, `0x008F5A2C`)
- `0x00950416` → [PiDmAddCacheReferenceForObject](PiDmAddCacheReferenceForObject_function_00950FB4.md) (function, `0x00950FB4`)
- `0x00950446` → [PiDmListAddObject](PiDmListAddObject_function_00950128.md) (function, `0x00950128`)
- `0x009504B1` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x009504DA` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009504DF` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00950503` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0095052B` → [PiDmRemoveCacheReferenceForObject](PiDmRemoveCacheReferenceForObject_function_00950F24.md) (function, `0x00950F24`)
- `0x00950533` → [PiDmObjectRelease](../8E/PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x00950545` → [PiDmRemoveCacheReferenceForObject](PiDmRemoveCacheReferenceForObject_function_00950F24.md) (function, `0x00950F24`)
- `0x0095054D` → [PiDmObjectRelease](../8E/PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x0095055E` → [PiDmRemoveCacheReferenceForObject](PiDmRemoveCacheReferenceForObject_function_00950F24.md) (function, `0x00950F24`)
- `0x00950566` → [PiDmObjectRelease](../8E/PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x00950574` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009505A7` → [PiDmListAddObject](PiDmListAddObject_function_00950128.md) (function, `0x00950128`)
- `0x009505C7` → [PiDmListAddObject](PiDmListAddObject_function_00950128.md) (function, `0x00950128`)
- `0x009505D4` → [PiDmObjectAcquireSharedLock](../8E/PiDmObjectAcquireSharedLock_function_008E38B8.md) (function, `0x008E38B8`)
- `0x009505DF` → [PiDmObjectReleaseLock](../8E/PiDmObjectReleaseLock_function_008E5584.md) (function, `0x008E5584`)
- `0x009505F1` → [PipCheckForDenyExecute](../94/PipCheckForDenyExecute_function_0094F880.md) (function, `0x0094F880`)
- `0x00950618` → [CmValidateDeviceInterfaceName](../8F/CmValidateDeviceInterfaceName_function_008F1A40.md) (function, `0x008F1A40`)
- `0x0095065D` → [PiPnpRtlBeginOperation](../8E/PiPnpRtlBeginOperation_function_008E033C.md) (function, `0x008E033C`)
- `0x0095068C` → [CmCreateDeviceInterface](../90/CmCreateDeviceInterface_function_00901578.md) (function, `0x00901578`)
- `0x009506A0` → [PiDmObjectRelease](../8E/PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x009506BB` → [PiDmObjectManagerAcquireSharedLock](PiDmObjectManagerAcquireSharedLock_function_009511A0.md) (function, `0x009511A0`)
- `0x009506C6` → [PiDmLookupObject](PiDmLookupObject_function_00951360.md) (function, `0x00951360`)
- `0x009506DA` → [PiDmObjectManagerReleaseLock](PiDmObjectManagerReleaseLock_function_0095111C.md) (function, `0x0095111C`)
- `0x0095070B` → [CmDeleteDeviceInterface](../A0/CmDeleteDeviceInterface_function_00A09E98.md) (function, `0x00A09E98`)
- `0x00950717` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00950723` → [PiPnpRtlEndOperation](../8E/PiPnpRtlEndOperation_function_008E0518.md) (function, `0x008E0518`)

### Direct callers
- [PiSwIrpInterfaceRegister](../94/PiSwIrpInterfaceRegister_function_0094F01C.md) at `0x0094F272`
- [IoRegisterDeviceInterface](../94/IoRegisterDeviceInterface_function_0094F9A0.md) at `0x0094FA5F`
- [PiCMRegisterDeviceInterface](../96/PiCMRegisterDeviceInterface_function_00962A94.md) at `0x00962BAD`
- [PiDevCfgConfigureDeviceInterfaces](../A9/PiDevCfgConfigureDeviceInterfaces_function_00A90060.md) at `0x00A90366`
- [sub_00B467A6](../B4/Unknown_function_00B467A6.md) at `0x00B468EC`

### Static image references
- `0x009501CC` → RVA `0x00E0A740` (`.data`; read)
- `0x009502D5` → RVA `0x00F8C600` (`.data`; read)
- `0x009502F4` → RVA `0x00F8B7A0` (`.data`; read)
- `0x00950371` → RVA `0x00E66398` (`.data`; read)
- `0x009503AB` → RVA `0x00011568` (`.rdata`; read)
- `0x009503DF` → RVA `0x000112D0` (`.rdata`; read)
- `0x00950488` → RVA `0x00011490` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00950269` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009502EB` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009503E6` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x009504DA` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009504DF` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00950503` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00950574` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00950717` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009502B1` → [sub_00B261E4](../B2/Unknown_function_00B261E4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009501B0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
009501B5  55                              push rbp
009501B6  56                              push rsi
009501B7  57                              push rdi
009501B8  41 54                           push r12
009501BA  41 55                           push r13
009501BC  41 56                           push r14
009501BE  41 57                           push r15
009501C0  48 8D 6C 24 80                  lea rbp, [rsp - 0x80]
009501C5  48 81 EC 80 01 00 00            sub rsp, 0x180
009501CC  48 8B 05 6D A5 4B 00            mov rax, qword ptr [rip + 0x4ba56d]
009501D3  48 33 C4                        xor rax, rsp
009501D6  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
009501DA  4C 8B A5 E0 00 00 00            mov r12, qword ptr [rbp + 0xe0]
009501E1  48 8B C2                        mov rax, rdx
009501E4  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
009501E8  48 8D 55 D0                     lea rdx, [rbp - 0x30]
009501EC  48 8B 8D E8 00 00 00            mov rcx, qword ptr [rbp + 0xe8]
009501F3  0F 57 C0                        xorps xmm0, xmm0
009501F6  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
009501FA  33 C9                           xor ecx, ecx
009501FC  8B F1                           mov esi, ecx
009501FE  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00950203  44 8B E9                        mov r13d, ecx
00950206  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
0095020A  44 8B F1                        mov r14d, ecx
0095020D  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00950212  88 4C 24 78                     mov byte ptr [rsp + 0x78], cl
00950216  8B D9                           mov ebx, ecx
00950218  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
0095021C  44 8B F9                        mov r15d, ecx
0095021F  88 4C 24 60                     mov byte ptr [rsp + 0x60], cl
00950223  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
00950227  89 4D 80                        mov dword ptr [rbp - 0x80], ecx
0095022A  89 4C 24 7C                     mov dword ptr [rsp + 0x7c], ecx
0095022E  49 89 0C 24                     mov qword ptr [r12], rcx
00950232  48 8B C8                        mov rcx, rax
00950235  44 88 4C 24 61                  mov byte ptr [rsp + 0x61], r9b
0095023A  4C 89 45 A0                     mov qword ptr [rbp - 0x60], r8
0095023E  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
00950242  E8 E5 57 FA FF                  call 0x1408f5a2c
00950247  8B F8                           mov edi, eax
00950249  85 C0                           test eax, eax
0095024B  0F 88 9D 02 00 00               js 0x1409504ee
00950251  BA 00 04 00 00                  mov edx, 0x400
00950256  C7 44 24 64 00 02 00 00         mov dword ptr [rsp + 0x64], 0x200
0095025E  B9 00 01 00 00                  mov ecx, 0x100
00950263  41 B8 50 70 20 20               mov r8d, 0x20207050
00950269  E8 82 1E 23 00                  call 0x140b820f0
0095026E  33 FF                           xor edi, edi
00950270  49 89 04 24                     mov qword ptr [r12], rax
00950274  48 85 C0                        test rax, rax
00950277  0F 84 76 04 00 00               je 0x1409506f3
0095027D  4C 8B 4D A0                     mov r9, qword ptr [rbp - 0x60]
00950281  48 8D 4C 24 64                  lea rcx, [rsp + 0x64]
00950286  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
0095028A  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0095028E  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00950293  C7 44 24 30 00 02 00 00         mov dword ptr [rsp + 0x30], 0x200
0095029B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009502A0  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
009502A5  E8 C6 35 FA FF                  call 0x1408f3870
009502AA  8B F8                           mov edi, eax
009502AC  3D 23 00 00 C0                  cmp eax, 0xc0000023
009502B1  0F 84 2D 5F 1D 00               je 0x140b261e4
009502B7  85 FF                           test edi, edi
009502B9  0F 88 2F 02 00 00               js 0x1409504ee
009502BF  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
009502C3  48 85 DB                        test rbx, rbx
009502C6  0F 85 21 03 00 00               jne 0x1409505ed
009502CC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009502D5  48 8D 0D 24 C3 63 00            lea rcx, [rip + 0x63c324]
009502DC  49 83 CE FF                     or r14, 0xffffffffffffffff
009502E0  B2 01                           mov dl, 1
009502E2  66 44 01 B0 E4 01 00 00         add word ptr [rax + 0x1e4], r14w
009502EA  90                              nop
009502EB  E8 30 4B 8C FF                  call 0x140214e20
009502F0  49 8B 1C 24                     mov rbx, qword ptr [r12]
009502F4  48 8D 35 A5 B4 63 00            lea rsi, [rip + 0x63b4a5]
009502FB  48 8B CE                        mov rcx, rsi
009502FE  41 8B FF                        mov edi, r15d
00950301  E8 9A 0E 00 00                  call 0x1409511a0
00950306  48 8B D3                        mov rdx, rbx
00950309  48 8B CE                        mov rcx, rsi
0095030C  E8 4F 10 00 00                  call 0x140951360
00950311  48 8B D8                        mov rbx, rax
00950314  48 85 C0                        test rax, rax
00950317  0F 84 32 03 00 00               je 0x14095064f
0095031D  F0 FF 40 08                     lock inc dword ptr [rax + 8]
00950321  48 8B CE                        mov rcx, rsi
00950324  E8 F3 0D 00 00                  call 0x14095111c
00950329  85 FF                           test edi, edi
0095032B  0F 89 A0 02 00 00               jns 0x1409505d1
00950331  8B 74 24 78                     mov esi, dword ptr [rsp + 0x78]
00950335  4C 8D 45 98                     lea r8, [rbp - 0x68]
00950339  B9 04 00 00 00                  mov ecx, 4
0095033E  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00950342  E8 6D 0C 00 00                  call 0x140950fb4
00950347  8B F8                           mov edi, eax
00950349  85 C0                           test eax, eax
0095034B  0F 88 F1 02 00 00               js 0x140950642
00950351  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
00950355  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
0095035A  49 8B D5                        mov rdx, r13
0095035D  B9 01 00 00 00                  mov ecx, 1
00950362  E8 4D 0C 00 00                  call 0x140950fb4
00950367  8B F8                           mov edi, eax
00950369  85 C0                           test eax, eax
0095036B  0F 88 D1 02 00 00               js 0x140950642
00950371  48 8B 0D 20 60 51 00            mov rcx, qword ptr [rip + 0x516020]
00950378  48 8D 44 24 7C                  lea rax, [rsp + 0x7c]
0095037D  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
00950382  45 33 C9                        xor r9d, r9d
00950385  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0095038A  49 8B D5                        mov rdx, r13
0095038D  C7 44 24 40 10 00 00 00         mov dword ptr [rsp + 0x40], 0x10
00950395  48 8D 45 B8                     lea rax, [rbp - 0x48]
00950399  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0095039E  48 8D 45 80                     lea rax, [rbp - 0x80]
009503A2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009503A7  45 8D 41 01                     lea r8d, [r9 + 1]
009503AB  48 8D 05 B6 11 6C FF            lea rax, [rip - 0x93ee4a]
009503B2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009503B7  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009503BC  E8 BF 1D F9 FF                  call 0x1408e2180
009503C1  8B F8                           mov edi, eax
009503C3  3D 25 02 00 C0                  cmp eax, 0xc0000225
009503C8  0F 85 6C 02 00 00               jne 0x14095063a
009503CE  0F 57 C0                        xorps xmm0, xmm0
009503D1  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
009503D5  41 B8 10 00 00 00               mov r8d, 0x10
009503DB  48 8D 55 B8                     lea rdx, [rbp - 0x48]
009503DF  48 8D 0D EA 0E 6C FF            lea rcx, [rip - 0x93f116]
009503E6  E8 85 A2 D6 FF                  call 0x1406ba670
009503EB  48 83 F8 10                     cmp rax, 0x10
009503EF  74 34                           je 0x140950425
009503F1  48 8D 55 20                     lea rdx, [rbp + 0x20]
009503F5  48 8D 4D B8                     lea rcx, [rbp - 0x48]
009503F9  E8 2E 56 FA FF                  call 0x1408f5a2c
009503FE  8B F8                           mov edi, eax
00950400  85 C0                           test eax, eax
00950402  0F 88 3A 02 00 00               js 0x140950642
00950408  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
0095040D  B9 05 00 00 00                  mov ecx, 5
00950412  48 8D 55 20                     lea rdx, [rbp + 0x20]
00950416  E8 99 0B 00 00                  call 0x140950fb4
0095041B  8B F8                           mov edi, eax
0095041D  85 C0                           test eax, eax
0095041F  0F 88 1D 02 00 00               js 0x140950642
00950425  40 84 F6                        test sil, sil
00950428  0F 84 2B 02 00 00               je 0x140950659
0095042E  48 85 DB                        test rbx, rbx
00950431  0F 84 73 02 00 00               je 0x1409506aa
00950437  4C 8B 7D 98                     mov r15, qword ptr [rbp - 0x68]
0095043B  45 33 C9                        xor r9d, r9d
0095043E  49 8B D7                        mov rdx, r15
00950441  4C 8B C3                        mov r8, rbx
00950444  33 C9                           xor ecx, ecx
00950446  E8 DD FC FF FF                  call 0x140950128
0095044B  40 8A 74 24 60                  mov sil, byte ptr [rsp + 0x60]
00950450  40 8A C6                        mov al, sil
00950453  F6 D8                           neg al
00950455  1B C9                           sbb ecx, ecx
00950457  81 E1 00 00 02 00               and ecx, 0x20000
0095045D  33 C0                           xor eax, eax
0095045F  49 FF C6                        inc r14
00950462  66 43 39 44 75 00               cmp word ptr [r13 + r14*2], ax
00950468  75 F5                           jne 0x14095045f
0095046A  49 8B 14 24                     mov rdx, qword ptr [r12]
0095046E  42 8D 04 75 02 00 00 00         lea eax, [r14*2 + 2]
00950476  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
0095047A  45 33 F6                        xor r14d, r14d
0095047D  48 8B 0D 14 5F 51 00            mov rcx, qword ptr [rip + 0x515f14]
00950484  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00950488  48 8D 05 01 10 6C FF            lea rax, [rip - 0x93efff]
0095048F  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00950494  4C 8B 6D 90                     mov r13, qword ptr [rbp - 0x70]
00950498  45 8D 46 03                     lea r8d, [r14 + 3]
0095049C  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
009504A4  4D 8B CD                        mov r9, r13
009504A7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009504AC  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
009504B1  E8 32 62 FA FF                  call 0x1408f66e8
009504B6  8B F8                           mov edi, eax
009504B8  85 C0                           test eax, eax
009504BA  0F 89 D5 00 00 00               jns 0x140950595
009504C0  40 84 F6                        test sil, sil
009504C3  0F 85 34 02 00 00               jne 0x1409506fd
009504C9  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009504CE  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
009504D3  48 8D 0D 26 C1 63 00            lea rcx, [rip + 0x63c126]
009504DA  E8 31 F5 90 FF                  call 0x14025fa10
009504DF  E8 CC D3 90 FF                  call 0x14025d8b0
009504E4  33 C9                           xor ecx, ecx
009504E6  85 FF                           test edi, edi
009504E8  0F 89 19 01 00 00               jns 0x140950607
009504EE  49 8B 0C 24                     mov rcx, qword ptr [r12]
009504F2  48 85 C9                        test rcx, rcx
009504F5  0F 85 1A 02 00 00               jne 0x140950715
009504FB  4D 85 ED                        test r13, r13
009504FE  74 08                           je 0x140950508
00950500  49 8B CD                        mov rcx, r13
00950503  E8 A8 CD D5 FF                  call 0x1406ad2b0
00950508  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
0095050C  48 85 C9                        test rcx, rcx
0095050F  0F 85 0E 02 00 00               jne 0x140950723
00950515  48 85 DB                        test rbx, rbx
00950518  0F 85 7F 01 00 00               jne 0x14095069d
0095051E  4D 85 FF                        test r15, r15
00950521  74 15                           je 0x140950538
00950523  49 8B 57 10                     mov rdx, qword ptr [r15 + 0x10]
00950527  41 8B 4F 1C                     mov ecx, dword ptr [r15 + 0x1c]
0095052B  E8 F4 09 00 00                  call 0x140950f24
00950530  49 8B CF                        mov rcx, r15
00950533  E8 38 4A F9 FF                  call 0x1408e4f70
00950538  4D 85 F6                        test r14, r14
0095053B  74 15                           je 0x140950552
0095053D  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
00950541  41 8B 4E 1C                     mov ecx, dword ptr [r14 + 0x1c]
00950545  E8 DA 09 00 00                  call 0x140950f24
0095054A  49 8B CE                        mov rcx, r14
0095054D  E8 1E 4A F9 FF                  call 0x1408e4f70
00950552  48 85 F6                        test rsi, rsi
00950555  74 14                           je 0x14095056b
00950557  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
0095055B  8B 4E 1C                        mov ecx, dword ptr [rsi + 0x1c]
0095055E  E8 C1 09 00 00                  call 0x140950f24
00950563  48 8B CE                        mov rcx, rsi
00950566  E8 05 4A F9 FF                  call 0x1408e4f70
0095056B  8B C7                           mov eax, edi
0095056D  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
00950571  48 33 CC                        xor rcx, rsp
00950574  E8 C7 C0 D5 FF                  call 0x1406ac640
00950579  48 8B 9C 24 D8 01 00 00         mov rbx, qword ptr [rsp + 0x1d8]
00950581  48 81 C4 80 01 00 00            add rsp, 0x180
00950588  41 5F                           pop r15
0095058A  41 5E                           pop r14
0095058C  41 5D                           pop r13
0095058E  41 5C                           pop r12
00950590  5F                              pop rdi
00950591  5E                              pop rsi
00950592  5D                              pop rbp
00950593  C3                              ret
00950594  CC                              int3
00950595  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
0095059A  45 33 C9                        xor r9d, r9d
0095059D  4C 8B C3                        mov r8, rbx
009505A0  49 8B D6                        mov rdx, r14
009505A3  41 8D 49 01                     lea ecx, [r9 + 1]
009505A7  E8 7C FB FF FF                  call 0x140950128
009505AC  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009505B1  48 85 F6                        test rsi, rsi
009505B4  0F 84 19 FF FF FF               je 0x1409504d3
009505BA  45 33 C9                        xor r9d, r9d
009505BD  4C 8B C3                        mov r8, rbx
009505C0  48 8B D6                        mov rdx, rsi
009505C3  41 8D 49 02                     lea ecx, [r9 + 2]
009505C7  E8 5C FB FF FF                  call 0x140950128
009505CC  E9 02 FF FF FF                  jmp 0x1409504d3
009505D1  48 8B CB                        mov rcx, rbx
009505D4  E8 DF 32 F9 FF                  call 0x1408e38b8
009505D9  8B 73 20                        mov esi, dword ptr [rbx + 0x20]
009505DC  48 8B CB                        mov rcx, rbx
009505DF  E8 A0 4F F9 FF                  call 0x1408e5584
009505E4  40 80 E6 01                     and sil, 1
009505E8  E9 48 FD FF FF                  jmp 0x140950335
009505ED  48 8D 4D D0                     lea rcx, [rbp - 0x30]
009505F1  E8 8A F2 FF FF                  call 0x14094f880
009505F6  F6 D8                           neg al
009505F8  1B C9                           sbb ecx, ecx
009505FA  81 E1 00 00 80 00               and ecx, 0x800000
00950600  89 0B                           mov dword ptr [rbx], ecx
00950602  E9 C5 FC FF FF                  jmp 0x1409502cc
00950607  38 4C 24 61                     cmp byte ptr [rsp + 0x61], cl
0095060B  0F 85 EA FE FF FF               jne 0x1409504fb
00950611  4D 8B 24 24                     mov r12, qword ptr [r12]
00950615  49 8B D4                        mov rdx, r12
00950618  E8 23 14 FA FF                  call 0x1408f1a40
0095061D  8B F8                           mov edi, eax
0095061F  85 C0                           test eax, eax
00950621  0F 88 D4 FE FF FF               js 0x1409504fb
00950627  48 B8 5C 00 3F 00 3F 00 5C 00   movabs rax, 0x5c003f003f005c
00950631  49 89 04 24                     mov qword ptr [r12], rax
00950635  E9 C1 FE FF FF                  jmp 0x1409504fb
0095063A  85 C0                           test eax, eax
0095063C  0F 89 93 FD FF FF               jns 0x1409503d5
00950642  4C 8B 6D 90                     mov r13, qword ptr [rbp - 0x70]
00950646  4C 8B 7D 98                     mov r15, qword ptr [rbp - 0x68]
0095064A  E9 7A FE FF FF                  jmp 0x1409504c9
0095064F  BF 34 00 00 C0                  mov edi, 0xc0000034
00950654  E9 C8 FC FF FF                  jmp 0x140950321
00950659  48 8D 4D A8                     lea rcx, [rbp - 0x58]
0095065D  E8 DA FC F8 FF                  call 0x1408e033c
00950662  8B F8                           mov edi, eax
00950664  85 C0                           test eax, eax
00950666  78 DA                           js 0x140950642
00950668  49 8B 14 24                     mov rdx, qword ptr [r12]
0095066C  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00950671  48 8B 0D 20 5D 51 00            mov rcx, qword ptr [rip + 0x515d20]
00950678  4C 8D 4D 90                     lea r9, [rbp - 0x70]
0095067C  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00950681  41 B8 02 00 00 00               mov r8d, 2
00950687  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0095068C  E8 E7 0E FB FF                  call 0x140901578
00950691  8B F8                           mov edi, eax
00950693  85 C0                           test eax, eax
00950695  0F 89 93 FD FF FF               jns 0x14095042e
0095069B  EB A5                           jmp 0x140950642
0095069D  48 8B CB                        mov rcx, rbx
009506A0  E8 CB 48 F9 FF                  call 0x1408e4f70
009506A5  E9 74 FE FF FF                  jmp 0x14095051e
009506AA  49 8B 1C 24                     mov rbx, qword ptr [r12]
009506AE  48 8D 35 EB B0 63 00            lea rsi, [rip + 0x63b0eb]
009506B5  48 8B CE                        mov rcx, rsi
009506B8  41 8B FF                        mov edi, r15d
009506BB  E8 E0 0A 00 00                  call 0x1409511a0
009506C0  48 8B D3                        mov rdx, rbx
009506C3  48 8B CE                        mov rcx, rsi
009506C6  E8 95 0C 00 00                  call 0x140951360
009506CB  48 8B D8                        mov rbx, rax
009506CE  48 85 C0                        test rax, rax
009506D1  74 19                           je 0x1409506ec
009506D3  F0 FF 40 08                     lock inc dword ptr [rax + 8]
009506D7  48 8B CE                        mov rcx, rsi
009506DA  E8 3D 0A 00 00                  call 0x14095111c
009506DF  85 FF                           test edi, edi
009506E1  0F 89 50 FD FF FF               jns 0x140950437
009506E7  E9 56 FF FF FF                  jmp 0x140950642
009506EC  BF 34 00 00 C0                  mov edi, 0xc0000034
009506F1  EB E4                           jmp 0x1409506d7
009506F3  BF 9A 00 00 C0                  mov edi, 0xc000009a
009506F8  E9 F1 FD FF FF                  jmp 0x1409504ee
009506FD  49 8B 14 24                     mov rdx, qword ptr [r12]
00950701  45 33 C0                        xor r8d, r8d
00950704  48 8B 0D 8D 5C 51 00            mov rcx, qword ptr [rip + 0x515c8d]
0095070B  E8 88 97 0B 00                  call 0x140a09e98
00950710  E9 B4 FD FF FF                  jmp 0x1409504c9
00950715  33 D2                           xor edx, edx
00950717  E8 54 21 23 00                  call 0x140b82870
0095071C  33 C0                           xor eax, eax
0095071E  E9 0E FF FF FF                  jmp 0x140950631
00950723  E8 F0 FD F8 FF                  call 0x1408e0518
00950728  E9 E8 FD FF FF                  jmp 0x140950515
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopRegisterDeviceInterface(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned __int8 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m154;
    unsigned __int8 v_stack_m157;
    unsigned __int8 v_stack_m158;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int8 v_stack_m198;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p60;
    unsigned __int8 v_stack_p61;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 4957549)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m130 = a1;
    v_stack_m108 = a6;
    a1 = 0;
    v_stack_m150 = 0;
    v_stack_m128 = 0;
    v_stack_m148 = 0;
    v_stack_m140 = 0;
    v_stack_m110 = 0;
    v_stack_m158 = 0;
    v_stack_m120 = 0;
    v_stack_m138 = 0;
    v_stack_m13C = 0;
    *(unsigned __int64 *)(a5) = 0;
    v_stack_m157 = a4;
    v_stack_m118 = a3;
    v_stack_m100 = v_xmm0;
    result = PnpStringFromGuid(a2, v_stack_mE8, a3, a4);
    if (sign_flag) goto loc_009504EE;
    v_stack_m154 = 512;
    result = ExAllocatePool2(256, (unsigned int)(0x400ULL), (unsigned int)(0x20207050ULL), a4);
    v_rdi = 0;
    *(unsigned __int64 *)(a5) = result;
    if (result == 0) goto loc_009506F3;
    v_stack_m180 = v_stack_m154;
    v_stack_m188 = 512;
    v_stack_m190 = result;
    v_stack_m198 = 0;
    result = CmGetDeviceInterfaceName(v_stack_m154, v_stack_mE8, v_stack_m130, v_stack_m118);
    if (sign_flag) goto loc_009504EE;
    if (v_stack_m108 != 0) goto loc_009505ED;
loc_009502CC:
    v_r14 = (0) | (-1);
    result = ExAcquireResourceExclusiveLite(v_rip + 6538020, 1, v_stack_m130, v_stack_m118);
    result = PiDmObjectManagerAcquireSharedLock(v_rip + 6534309, 1, v_stack_m130, v_stack_m118);
    result = PiDmLookupObject(v_rip + 6534309, *(unsigned __int64 *)(a5), v_stack_m130, v_stack_m118);
    if (result == 0) goto loc_0095064F;
loc_00950321:
    result = PiDmObjectManagerReleaseLock(v_rip + 6534309, *(unsigned __int64 *)(a5), v_stack_m130, v_stack_m118);
    if (!sign_flag) goto loc_009505D1;
loc_00950335:
    result = PiDmAddCacheReferenceForObject(4, v_stack_mE8, v_stack_m120, v_stack_m118);
    if (sign_flag) goto loc_00950642;
    result = PiDmAddCacheReferenceForObject(1, v_stack_m130, v_stack_m148, v_stack_m118);
    if (sign_flag) goto loc_00950642;
    v_stack_m168 = 0;
    a4 = 0;
    v_stack_m170 = v_stack_m13C;
    v_stack_m178 = 16;
    v_stack_m180 = v_stack_m100;
    v_stack_m188 = v_stack_m138;
    v_stack_m190 = v_rip - 9694794;
    v_stack_m198 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 5333024), v_stack_m130, a4 + 1, a4);
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_0095063A;
    v_stack_m100 = v_xmm0;
loc_009503D5:
    result = RtlCompareMemory(v_rip - 9695510, v_stack_m100, 16, a4);
    if (result == 16) goto loc_00950425;
    result = PnpStringFromGuid(v_stack_m100, v_stack_m98, 16, a4);
    if (sign_flag) goto loc_00950642;
    result = PiDmAddCacheReferenceForObject(5, v_stack_m98, v_stack_m150, a4);
    if (sign_flag) goto loc_00950642;
loc_00950425:
    if ((unsigned __int8)((unsigned int)(v_stack_m140)) == 0) goto loc_00950659;
loc_0095042E:
    if (result == 0) goto loc_009506AA;
loc_00950437:
    a4 = 0;
    a1 = 0;
    result = PiDmListAddObject(a1, v_stack_m120, result, a4);
    result = (unsigned __int8)(-((unsigned __int8)(v_stack_m158)));
    a1 = (unsigned int)((a1) & (0x20000ULL));
    result = 0;
loc_0095045F:
    v_r14 = (v_r14) + 1;
    if ((*(unsigned __int16 *)(v_stack_m130 + v_r14 * 2)) != 0) goto loc_0095045F;
    v_stack_m170 = (unsigned int)(a1);
    v_r14 = 0;
    v_stack_m178 = (unsigned int)(v_r14 * 2 + 2);
    v_stack_m180 = v_stack_m130;
    v_stack_m188 = 18;
    v_stack_m190 = v_rip - 9695231;
    v_stack_m198 = 0;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 5332756), *(unsigned __int64 *)(a5), v_r14 + 3, v_stack_m128);
    if (!sign_flag) goto loc_00950595;
    if ((unsigned __int8)(v_stack_m158) != 0) goto loc_009506FD;
loc_009504C9:
loc_009504D3:
    result = ExReleaseResourceLite(v_rip + 6537510, *(unsigned __int64 *)(a5), v_r14 + 3, v_stack_m128);
    result = KeLeaveCriticalRegion(v_rip + 6537510, *(unsigned __int64 *)(a5), v_r14 + 3, v_stack_m128);
    a1 = 0;
    if (!sign_flag) goto loc_00950607;
loc_009504EE:
    if (*(unsigned __int64 *)(a5) != 0) goto loc_00950715;
loc_009504FB:
    if (v_stack_m128 != 0) {
        a1 = v_stack_m128;
        result = ZwClose(a1, *(unsigned __int64 *)(a5), v_r14 + 3, v_stack_m128);
    }
    if (v_stack_m110 != 0) goto loc_00950723;
loc_00950515:
    if (result != 0) goto loc_0095069D;
loc_0095051E:
    if (v_stack_m120 != 0) {
        a2 = *(unsigned __int64 *)(v_stack_m120 + 16);
        a1 = *(unsigned int *)(v_stack_m120 + 28);
        result = PiDmRemoveCacheReferenceForObject(a1, a2, v_r14 + 3, v_stack_m128);
        a1 = v_stack_m120;
        result = PiDmObjectRelease(a1, a2, v_r14 + 3, v_stack_m128);
    }
    if (v_stack_m148 != 0) {
        a2 = *(unsigned __int64 *)(v_stack_m148 + 16);
        a1 = *(unsigned int *)(v_stack_m148 + 28);
        result = PiDmRemoveCacheReferenceForObject(a1, a2, v_r14 + 3, v_stack_m128);
        a1 = v_stack_m148;
        result = PiDmObjectRelease(a1, a2, v_r14 + 3, v_stack_m128);
    }
    if (v_stack_m150 != 0) {
        a2 = *(unsigned __int64 *)(v_stack_m150 + 16);
        a1 = *(unsigned int *)(v_stack_m150 + 28);
        result = PiDmRemoveCacheReferenceForObject(a1, a2, v_r14 + 3, v_stack_m128);
        a1 = v_stack_m150;
        result = PiDmObjectRelease(a1, a2, v_r14 + 3, v_stack_m128);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_r14 + 3, v_stack_m128);
    v_rsp = (v_rsp) + (384);
    return result;
loc_00950595:
    a4 = 0;
    result = PiDmListAddObject(a4 + 1, v_stack_p70, v_stack_p20, a4);
    if (v_stack_p68 == 0) goto loc_009504D3;
    a4 = 0;
    result = PiDmListAddObject(a4 + 2, v_stack_p68, v_stack_p20, a4);
    goto loc_009504D3;
loc_009505D1:
    result = PiDmObjectAcquireSharedLock(v_stack_p20, v_stack_p68, v_stack_p20, a4);
    result = PiDmObjectReleaseLock(v_stack_p20, v_stack_p68, v_stack_p20, a4);
    v_rsi = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 32))) & (1));
    goto loc_00950335;
loc_009505ED:
    result = PipCheckForDenyExecute(v_stack_mE8, v_stack_p68, v_stack_p20, a4);
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)((v_stack_mE8) & (0x800000ULL));
    *(unsigned int *)(v_stack_p20) = (unsigned int)(a1);
    goto loc_009502CC;
loc_00950607:
    if (v_stack_p61 != ((unsigned __int8)(a1))) goto loc_009504FB;
    result = CmValidateDeviceInterfaceName(a1, *(unsigned __int64 *)(a5), v_stack_p20, a4);
    if (sign_flag) goto loc_009504FB;
loc_00950631:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a5)) = result;
    goto loc_009504FB;
loc_0095063A:
    if (!sign_flag) goto loc_009503D5;
loc_00950642:
    goto loc_009504C9;
loc_0095064F:
    goto loc_00950321;
loc_00950659:
    result = PiPnpRtlBeginOperation(v_stack_m110, *(unsigned __int64 *)(a5), v_stack_p20, a4);
    if (sign_flag) goto loc_00950642;
    v_stack_p28 = (unsigned int)(v_stack_m120);
    v_stack_p20 = v_stack_p60;
    result = CmCreateDeviceInterface(*(unsigned __int64 *)(v_rip + 5332256), *(unsigned __int64 *)(*(unsigned __int64 *)(a5)), 2, v_stack_m128);
    if (!sign_flag) goto loc_0095042E;
    goto loc_00950642;
loc_0095069D:
    result = PiDmObjectRelease(v_stack_p20, *(unsigned __int64 *)(*(unsigned __int64 *)(a5)), 2, v_stack_m128);
    goto loc_0095051E;
loc_009506AA:
    result = PiDmObjectManagerAcquireSharedLock(v_rip + 6533355, *(unsigned __int64 *)(*(unsigned __int64 *)(a5)), 2, v_stack_m128);
    result = PiDmLookupObject(v_rip + 6533355, *(unsigned __int64 *)(*(unsigned __int64 *)(a5)), 2, v_stack_m128);
    if (result == 0) goto loc_009506EC;
loc_009506D7:
    result = PiDmObjectManagerReleaseLock(v_rip + 6533355, *(unsigned __int64 *)(*(unsigned __int64 *)(a5)), 2, v_stack_m128);
    if (!sign_flag) goto loc_00950437;
    goto loc_00950642;
loc_009506EC:
    goto loc_009506D7;
loc_009506F3:
    goto loc_009504EE;
loc_009506FD:
    a3 = 0;
    result = CmDeleteDeviceInterface(*(unsigned __int64 *)(v_rip + 5332109), *(unsigned __int64 *)(*(unsigned __int64 *)(a5)), a3, v_stack_m128);
    goto loc_009504C9;
loc_00950715:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 5332109), a2, a3, v_stack_m128);
    result = 0;
    goto loc_00950631;
loc_00950723:
    result = PiPnpRtlEndOperation(*(unsigned __int64 *)(v_rip + 5332109), a2, a3, v_stack_m128);
    goto loc_00950515;
}
```

## 5. (Beta) C Style

```c
int64_t IopRegisterDeviceInterface(int64_t Arg1, int64_t Arg2, int64_t Arg3, uint8_t Arg4, void *Arg5, int64_t Arg6)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint8_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m154;
    uint8_t v_stack_m157;
    uint8_t v_stack_m158;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m190;
    uint8_t v_stack_m198;
    uint64_t v_stack_m48;
    uint64_t v_stack_m98;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p60;
    uint8_t v_stack_p61;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0x4BA56D)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m130 = Arg1;
    v_stack_m108 = Arg6;
    Arg1 = 0;
    v_stack_m150 = 0;
    v_stack_m128 = 0;
    v_stack_m148 = 0;
    v_stack_m140 = 0;
    v_stack_m110 = 0;
    v_stack_m158 = 0;
    v_stack_m120 = 0;
    v_stack_m138 = 0;
    v_stack_m13C = 0;
    *(uint64_t *)(arg5) = 0;
    v_stack_m157 = Arg4;
    v_stack_m118 = Arg3;
    v_stack_m100 = v_xmm0;
    result = PnpStringFromGuid(Arg2, v_stack_mE8, Arg3, Arg4);
    if (sign_flag) goto loc_009504EE;
    v_stack_m154 = 512;
    result = ExAllocatePool2(256, (uint32_t)(0x400ULL), (uint32_t)(0x20207050ULL), Arg4);
    local_rdi = 0;
    *(uint64_t *)(arg5) = result;
    if (result == 0) goto loc_009506F3;
    v_stack_m180 = v_stack_m154;
    v_stack_m188 = 512;
    v_stack_m190 = result;
    v_stack_m198 = 0;
    result = CmGetDeviceInterfaceName(v_stack_m154, v_stack_mE8, v_stack_m130, v_stack_m118);
    if (sign_flag) goto loc_009504EE;
    if (v_stack_m108 != 0) goto loc_009505ED;
loc_009502CC:
    local_r14 = (0) | (-1);
    result = ExAcquireResourceExclusiveLite(v_rip + 6538020, 1, v_stack_m130, v_stack_m118);
    result = PiDmObjectManagerAcquireSharedLock(v_rip + 6534309, 1, v_stack_m130, v_stack_m118);
    result = PiDmLookupObject(v_rip + 6534309, *(uint64_t *)(arg5), v_stack_m130, v_stack_m118);
    if (result == 0) goto loc_0095064F;
loc_00950321:
    result = PiDmObjectManagerReleaseLock(v_rip + 6534309, *(uint64_t *)(arg5), v_stack_m130, v_stack_m118);
    if (!sign_flag) goto loc_009505D1;
loc_00950335:
    result = PiDmAddCacheReferenceForObject(4, v_stack_mE8, v_stack_m120, v_stack_m118);
    if (sign_flag) goto loc_00950642;
    result = PiDmAddCacheReferenceForObject(1, v_stack_m130, v_stack_m148, v_stack_m118);
    if (sign_flag) goto loc_00950642;
    v_stack_m168 = 0;
    Arg4 = 0;
    v_stack_m170 = v_stack_m13C;
    v_stack_m178 = 16;
    v_stack_m180 = v_stack_m100;
    v_stack_m188 = v_stack_m138;
    v_stack_m190 = v_rip - 9694794;
    v_stack_m198 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x516020), v_stack_m130, Arg4 + 1, Arg4);
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_0095063A;
    v_stack_m100 = v_xmm0;
loc_009503D5:
    result = RtlCompareMemory(v_rip - 9695510, v_stack_m100, 16, Arg4);
    if (result == 16) goto loc_00950425;
    result = PnpStringFromGuid(v_stack_m100, v_stack_m98, 16, Arg4);
    if (sign_flag) goto loc_00950642;
    result = PiDmAddCacheReferenceForObject(5, v_stack_m98, v_stack_m150, Arg4);
    if (sign_flag) goto loc_00950642;
loc_00950425:
    if ((uint8_t)((uint32_t)(v_stack_m140)) == 0) goto loc_00950659;
loc_0095042E:
    if (result == 0) goto loc_009506AA;
loc_00950437:
    Arg4 = 0;
    Arg1 = 0;
    result = PiDmListAddObject(Arg1, v_stack_m120, result, Arg4);
    result = (uint8_t)(-((uint8_t)(v_stack_m158)));
    Arg1 = (uint32_t)((Arg1) & (0x20000ULL));
    result = 0;
loc_0095045F:
    local_r14 = (local_r14) + 1;
    if ((*(uint16_t *)(v_stack_m130 + local_r14 * 2)) != 0) goto loc_0095045F;
    v_stack_m170 = (uint32_t)(Arg1);
    local_r14 = 0;
    v_stack_m178 = (uint32_t)(local_r14 * 2 + 2);
    v_stack_m180 = v_stack_m130;
    v_stack_m188 = 18;
    v_stack_m190 = v_rip - 9695231;
    v_stack_m198 = 0;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x515F14), *(uint64_t *)(arg5), local_r14 + 3, v_stack_m128);
    if (!sign_flag) goto loc_00950595;
    if ((uint8_t)(v_stack_m158) != 0) goto loc_009506FD;
loc_009504C9:
loc_009504D3:
    result = ExReleaseResourceLite(v_rip + 6537510, *(uint64_t *)(arg5), local_r14 + 3, v_stack_m128);
    result = KeLeaveCriticalRegion(v_rip + 6537510, *(uint64_t *)(arg5), local_r14 + 3, v_stack_m128);
    Arg1 = 0;
    if (!sign_flag) goto loc_00950607;
loc_009504EE:
    if (*(uint64_t *)(arg5) != 0) goto loc_00950715;
loc_009504FB:
    if (v_stack_m128 != 0) {
        Arg1 = v_stack_m128;
        result = ZwClose(Arg1, *(uint64_t *)(arg5), local_r14 + 3, v_stack_m128);
    }
    if (v_stack_m110 != 0) goto loc_00950723;
loc_00950515:
    if (result != 0) goto loc_0095069D;
loc_0095051E:
    if (v_stack_m120 != 0) {
        Arg2 = *(uint64_t *)(v_stack_m120 + 0x10);
        Arg1 = *(uint32_t *)(v_stack_m120 + 0x1C);
        result = PiDmRemoveCacheReferenceForObject(Arg1, Arg2, local_r14 + 3, v_stack_m128);
        Arg1 = v_stack_m120;
        result = PiDmObjectRelease(Arg1, Arg2, local_r14 + 3, v_stack_m128);
    }
    if (v_stack_m148 != 0) {
        Arg2 = *(uint64_t *)(v_stack_m148 + 0x10);
        Arg1 = *(uint32_t *)(v_stack_m148 + 0x1C);
        result = PiDmRemoveCacheReferenceForObject(Arg1, Arg2, local_r14 + 3, v_stack_m128);
        Arg1 = v_stack_m148;
        result = PiDmObjectRelease(Arg1, Arg2, local_r14 + 3, v_stack_m128);
    }
    if (v_stack_m150 != 0) {
        Arg2 = *(uint64_t *)(v_stack_m150 + 0x10);
        Arg1 = *(uint32_t *)(v_stack_m150 + 0x1C);
        result = PiDmRemoveCacheReferenceForObject(Arg1, Arg2, local_r14 + 3, v_stack_m128);
        Arg1 = v_stack_m150;
        result = PiDmObjectRelease(Arg1, Arg2, local_r14 + 3, v_stack_m128);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, local_r14 + 3, v_stack_m128);
    local_rsp = (local_rsp) + (384);
    return result;
loc_00950595:
    Arg4 = 0;
    result = PiDmListAddObject(Arg4 + 1, v_stack_p70, v_stack_p20, Arg4);
    if (v_stack_p68 == 0) goto loc_009504D3;
    Arg4 = 0;
    result = PiDmListAddObject(Arg4 + 2, v_stack_p68, v_stack_p20, Arg4);
    goto loc_009504D3;
loc_009505D1:
    result = PiDmObjectAcquireSharedLock(v_stack_p20, v_stack_p68, v_stack_p20, Arg4);
    result = PiDmObjectReleaseLock(v_stack_p20, v_stack_p68, v_stack_p20, Arg4);
    local_rsi = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20))) & (1));
    goto loc_00950335;
loc_009505ED:
    result = PipCheckForDenyExecute(v_stack_mE8, v_stack_p68, v_stack_p20, Arg4);
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)((v_stack_mE8) & (0x800000ULL));
    *(uint32_t *)(v_stack_p20) = (uint32_t)(Arg1);
    goto loc_009502CC;
loc_00950607:
    if (v_stack_p61 != ((uint8_t)(Arg1))) goto loc_009504FB;
    result = CmValidateDeviceInterfaceName(Arg1, *(uint64_t *)(arg5), v_stack_p20, Arg4);
    if (sign_flag) goto loc_009504FB;
loc_00950631:
    *(uint64_t *)(*(uint64_t *)(arg5)) = result;
    goto loc_009504FB;
loc_0095063A:
    if (!sign_flag) goto loc_009503D5;
loc_00950642:
    goto loc_009504C9;
loc_0095064F:
    goto loc_00950321;
loc_00950659:
    result = PiPnpRtlBeginOperation(v_stack_m110, *(uint64_t *)(arg5), v_stack_p20, Arg4);
    if (sign_flag) goto loc_00950642;
    v_stack_p28 = (uint32_t)(v_stack_m120);
    v_stack_p20 = v_stack_p60;
    result = CmCreateDeviceInterface(*(uint64_t *)(v_rip + 0x515D20), *(uint64_t *)(*(uint64_t *)(arg5)), 2, v_stack_m128);
    if (!sign_flag) goto loc_0095042E;
    goto loc_00950642;
loc_0095069D:
    result = PiDmObjectRelease(v_stack_p20, *(uint64_t *)(*(uint64_t *)(arg5)), 2, v_stack_m128);
    goto loc_0095051E;
loc_009506AA:
    result = PiDmObjectManagerAcquireSharedLock(v_rip + 6533355, *(uint64_t *)(*(uint64_t *)(arg5)), 2, v_stack_m128);
    result = PiDmLookupObject(v_rip + 6533355, *(uint64_t *)(*(uint64_t *)(arg5)), 2, v_stack_m128);
    if (result == 0) goto loc_009506EC;
loc_009506D7:
    result = PiDmObjectManagerReleaseLock(v_rip + 6533355, *(uint64_t *)(*(uint64_t *)(arg5)), 2, v_stack_m128);
    if (!sign_flag) goto loc_00950437;
    goto loc_00950642;
loc_009506EC:
    goto loc_009506D7;
loc_009506F3:
    goto loc_009504EE;
loc_009506FD:
    Arg3 = 0;
    result = CmDeleteDeviceInterface(*(uint64_t *)(v_rip + 0x515C8D), *(uint64_t *)(*(uint64_t *)(arg5)), Arg3, v_stack_m128);
    goto loc_009504C9;
loc_00950715:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0x515C8D), Arg2, Arg3, v_stack_m128);
    result = 0;
    goto loc_00950631;
loc_00950723:
    result = PiPnpRtlEndOperation(*(uint64_t *)(v_rip + 0x515C8D), Arg2, Arg3, v_stack_m128);
    goto loc_00950515;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009501B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
