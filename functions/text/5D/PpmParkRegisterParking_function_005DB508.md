# PpmParkRegisterParking

- RVA: `0x005DB508`–`0x005DBDDA` (길이 `2,258` bytes)
- VA: `0x00000001405DB508`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CD2FC`
- 디코드: `553`개 명령, `2,258/2,258` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x005DB54B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DB579` → [Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline](../4F/Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline_function_004F135C.md) (function, `0x004F135C`)
- `0x005DB613` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DB62A` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x005DB640` → [PopExecuteOnTargetProcessors](../2D/PopExecuteOnTargetProcessors_function_002DD834.md) (function, `0x002DD834`)
- `0x005DB67D` → [KeInitializeSchedulerSubNodeEnumerationContext](../41/KeInitializeSchedulerSubNodeEnumerationContext_function_0041E4B0.md) (function, `0x0041E4B0`)
- `0x005DB690` → [KeEnumerateNextSchedulerSubNodeInNode](../25/KeEnumerateNextSchedulerSubNodeInNode_function_002566D8.md) (function, `0x002566D8`)
- `0x005DB6BB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x005DB6F3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x005DB76C` → [KeInitializeSchedulerSubNodeEnumerationContext](../41/KeInitializeSchedulerSubNodeEnumerationContext_function_0041E4B0.md) (function, `0x0041E4B0`)
- `0x005DB782` → [KeEnumerateNextSchedulerSubNodeInNode](../25/KeEnumerateNextSchedulerSubNodeInNode_function_002566D8.md) (function, `0x002566D8`)
- `0x005DB86F` → [PpmHeteroIsMultiClassParkingEnabled](../41/PpmHeteroIsMultiClassParkingEnabled_function_00414310.md) (function, `0x00414310`)
- `0x005DB8A2` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005DB8B2` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x005DB8D7` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005DB96E` → [PpmHeteroHgsRegisterContainmentGroups](PpmHeteroHgsRegisterContainmentGroups_function_005D8D14.md) (function, `0x005D8D14`)
- `0x005DB9E8` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DB9F9` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x005DBA1C` → [PpmIdleInitializeConcurrency](../../page/75/PpmIdleInitializeConcurrency_function_00754F30.md) (function, `0x00754F30`)
- `0x005DBA85` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005DBA97` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x005DBACE` → [PpmIdleInitializeConcurrency](../../page/75/PpmIdleInitializeConcurrency_function_00754F30.md) (function, `0x00754F30`)
- `0x005DBB08` → [PpmParkRegisterRestriction](PpmParkRegisterRestriction_function_005DBDE0.md) (function, `0x005DBDE0`)
- `0x005DBB3D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x005DBBA1` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005DBBBC` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005DBC51` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005DBC76` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005DBCFF` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x005DBD51` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x005DBD6A` → [PpmParkFreeAllParkNodes](../../page/76/PpmParkFreeAllParkNodes_function_0076AC0C.md) (function, `0x0076AC0C`)
- `0x005DBD7C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005DBD93` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005DBD98` → [PpmParkApplyPolicy](../4B/PpmParkApplyPolicy_function_004B613C.md) (function, `0x004B613C`)
- `0x005DBD9D` → [PpmParkParkingAvailable](../../page/A8/PpmParkParkingAvailable_function_00A84F58.md) (function, `0x00A84F58`)
- `0x005DBDA4` → [PpmParkRegisterParkingEx](../5E/PpmParkRegisterParkingEx_function_005E183C.md) (function, `0x005E183C`)
- `0x005DBDB3` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmCheckInitProcessors](../../page/A8/PpmCheckInitProcessors_function_00A84AE8.md) at `0x00A84C59`

### Static image references
- `0x005DB52E` → RVA `0x00E0A740` (`.data`; read)
- `0x005DB586` → RVA `0x00E0B800` (`.data`; read)
- `0x005DB5A0` → RVA `0x00F083D8` (`.data`; read)
- `0x005DB5C9` → RVA `0x00F083E0` (`.data`; read)
- `0x005DB5D7` → RVA `0x00F083A8` (`.data`; read)
- `0x005DB632` → RVA `0x004853C0` (`PpmIdleRemoveConcurrency`; read)
- `0x005DB655` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x005DB668` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x005DB7A6` → RVA `0x00E0B5A0` (`.data`; read)
- `0x005DB84A` → RVA `0x00FC5038` (`ALMOSTRO`; read)
- `0x005DB85F` → RVA `0x00FC6A86` (`ALMOSTRO`; read)
- `0x005DB95A` → RVA `0x00FC501C` (`ALMOSTRO`; read)
- `0x005DBCF8` → RVA `0x00F0CC20` (`.data`; read)
- `0x005DBD1D` → RVA `0x00F083D8` (`.data`; write)
- `0x005DBD39` → RVA `0x00F083E0` (`.data`; write)
- `0x005DBD4A` → RVA `0x00F083A8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x005DB6BB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x005DB6F3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x005DBA1C` → [PpmIdleInitializeConcurrency](../../page/75/PpmIdleInitializeConcurrency_function_00754F30.md) (`.text` → `PAGE`)
  - `0x005DBACE` → [PpmIdleInitializeConcurrency](../../page/75/PpmIdleInitializeConcurrency_function_00754F30.md) (`.text` → `PAGE`)
  - `0x005DBB3D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x005DBD6A` → [PpmParkFreeAllParkNodes](../../page/76/PpmParkFreeAllParkNodes_function_0076AC0C.md) (`.text` → `PAGE`)
  - `0x005DBD7C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x005DBD93` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x005DBD9D` → [PpmParkParkingAvailable](../../page/A8/PpmParkParkingAvailable_function_00A84F58.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DB508  48 8B C4                        mov rax, rsp
005DB50B  48 89 58 08                     mov qword ptr [rax + 8], rbx
005DB50F  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
005DB513  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
005DB517  55                              push rbp
005DB518  41 54                           push r12
005DB51A  41 55                           push r13
005DB51C  41 56                           push r14
005DB51E  41 57                           push r15
005DB520  48 8D A8 E8 FE FF FF            lea rbp, [rax - 0x118]
005DB527  48 81 EC F0 01 00 00            sub rsp, 0x1f0
005DB52E  48 8B 05 0B F2 82 00            mov rax, qword ptr [rip + 0x82f20b]
005DB535  48 33 C4                        xor rax, rsp
005DB538  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
005DB53F  33 D2                           xor edx, edx
005DB541  48 8D 4D D0                     lea rcx, [rbp - 0x30]
005DB545  41 B8 08 01 00 00               mov r8d, 0x108
005DB54B  E8 F0 B6 0E 00                  call 0x1406c6c40
005DB550  33 C0                           xor eax, eax
005DB552  0F 57 C0                        xorps xmm0, xmm0
005DB555  45 33 E4                        xor r12d, r12d
005DB558  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
005DB55C  0F 57 C9                        xorps xmm1, xmm1
005DB55F  44 89 64 24 3C                  mov dword ptr [rsp + 0x3c], r12d
005DB564  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
005DB569  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
005DB56D  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
005DB571  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
005DB575  0F 11 4D B0                     movups xmmword ptr [rbp - 0x50], xmm1
005DB579  E8 DE 5D F1 FF                  call 0x1404f135c
005DB57E  85 C0                           test eax, eax
005DB580  0F 85 1E 08 00 00               jne 0x1405dbda4
005DB586  0F B6 05 73 02 83 00            movzx eax, byte ptr [rip + 0x830273]
005DB58D  41 8D 4C 24 02                  lea ecx, [r12 + 2]
005DB592  3A C1                           cmp al, cl
005DB594  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
005DB599  8B F0                           mov esi, eax
005DB59B  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
005DB5A0  48 8B 05 31 CE 92 00            mov rax, qword ptr [rip + 0x92ce31]
005DB5A7  45 8D 6C 24 01                  lea r13d, [r12 + 1]
005DB5AC  0F 42 F1                        cmovb esi, ecx
005DB5AF  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
005DB5B4  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
005DB5B8  45 8A F4                        mov r14b, r12b
005DB5BB  44 89 64 24 44                  mov dword ptr [rsp + 0x44], r12d
005DB5C0  48 85 C0                        test rax, rax
005DB5C3  0F 84 8C 00 00 00               je 0x1405db655
005DB5C9  8B 0D 11 CE 92 00               mov ecx, dword ptr [rip + 0x92ce11]
005DB5CF  48 8B D0                        mov rdx, rax
005DB5D2  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
005DB5D7  48 8B 05 CA CD 92 00            mov rax, qword ptr [rip + 0x92cdca]
005DB5DE  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
005DB5E3  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
005DB5E7  85 C9                           test ecx, ecx
005DB5E9  74 6A                           je 0x1405db655
005DB5EB  48 8D 9A A0 04 00 00            lea rbx, [rdx + 0x4a0]
005DB5F2  8B F9                           mov edi, ecx
005DB5F4  4C 39 63 B0                     cmp qword ptr [rbx - 0x50], r12
005DB5F8  74 4B                           je 0x1405db645
005DB5FA  F6 03 08                        test byte ptr [rbx], 8
005DB5FD  74 46                           je 0x1405db645
005DB5FF  33 D2                           xor edx, edx
005DB601  48 C7 45 D0 01 00 20 00         mov qword ptr [rbp - 0x30], 0x200001
005DB609  41 B8 00 01 00 00               mov r8d, 0x100
005DB60F  48 8D 4D D8                     lea rcx, [rbp - 0x28]
005DB613  E8 28 B6 0E 00                  call 0x1406c6c40
005DB618  4C 8B 83 70 FB FF FF            mov r8, qword ptr [rbx - 0x490]
005DB61F  48 8D 4D D0                     lea rcx, [rbp - 0x30]
005DB623  0F B7 93 64 FB FF FF            movzx edx, word ptr [rbx - 0x49c]
005DB62A  E8 91 00 C8 FF                  call 0x14025b6c0
005DB62F  45 33 C9                        xor r9d, r9d
005DB632  48 8D 15 87 9D EA FF            lea rdx, [rip - 0x156279]
005DB639  45 33 C0                        xor r8d, r8d
005DB63C  48 8D 4D D0                     lea rcx, [rbp - 0x30]
005DB640  E8 EF 21 D0 FF                  call 0x1402dd834
005DB645  48 81 C3 10 05 00 00            add rbx, 0x510
005DB64C  49 2B FD                        sub rdi, r13
005DB64F  75 A3                           jne 0x1405db5f4
005DB651  8B 74 24 40                     mov esi, dword ptr [rsp + 0x40]
005DB655  66 44 3B 25 A3 99 9E 00         cmp r12w, word ptr [rip + 0x9e99a3]
005DB65D  45 8B FC                        mov r15d, r12d
005DB660  41 8B DC                        mov ebx, r12d
005DB663  41 8B FC                        mov edi, r12d
005DB666  73 42                           jae 0x1405db6aa
005DB668  4C 8D 35 91 49 A2 FF            lea r14, [rip - 0x5db66f]
005DB66F  8B D7                           mov edx, edi
005DB671  48 8D 4D B0                     lea rcx, [rbp - 0x50]
005DB675  49 8B 94 D6 C0 F6 FC 00         mov rdx, qword ptr [r14 + rdx*8 + 0xfcf6c0]
005DB67D  E8 2E 2E E4 FF                  call 0x14041e4b0
005DB682  EB 03                           jmp 0x1405db687
005DB684  41 03 DD                        add ebx, r13d
005DB687  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
005DB68C  48 8D 4D B0                     lea rcx, [rbp - 0x50]
005DB690  E8 43 B0 C7 FF                  call 0x1402566d8
005DB695  85 C0                           test eax, eax
005DB697  74 EB                           je 0x1405db684
005DB699  0F B7 05 60 99 9E 00            movzx eax, word ptr [rip + 0x9e9960]
005DB6A0  41 03 FD                        add edi, r13d
005DB6A3  3B F8                           cmp edi, eax
005DB6A5  72 C8                           jb 0x1405db66f
005DB6A7  45 8A F4                        mov r14b, r12b
005DB6AA  69 D3 10 05 00 00               imul edx, ebx, 0x510
005DB6B0  B9 40 00 00 00                  mov ecx, 0x40
005DB6B5  41 B8 50 50 4D 70               mov r8d, 0x704d5050
005DB6BB  E8 30 6A 5A 00                  call 0x140b820f0
005DB6C0  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
005DB6C5  4C 8B E8                        mov r13, rax
005DB6C8  48 85 C0                        test rax, rax
005DB6CB  0F 84 27 06 00 00               je 0x1405dbcf8
005DB6D1  40 0F B6 FE                     movzx edi, sil
005DB6D5  41 B8 50 50 4D 70               mov r8d, 0x704d5050
005DB6DB  8B CF                           mov ecx, edi
005DB6DD  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
005DB6E1  0F AF CB                        imul ecx, ebx
005DB6E4  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
005DB6E8  8D 14 89                        lea edx, [rcx + rcx*4]
005DB6EB  B9 40 00 00 00                  mov ecx, 0x40
005DB6F0  C1 E2 07                        shl edx, 7
005DB6F3  E8 F8 69 5A 00                  call 0x140b820f0
005DB6F8  4C 8B C8                        mov r9, rax
005DB6FB  48 85 C0                        test rax, rax
005DB6FE  0F 84 F1 05 00 00               je 0x1405dbcf5
005DB704  41 8B D4                        mov edx, r12d
005DB707  41 BE 01 00 00 00               mov r14d, 1
005DB70D  85 DB                           test ebx, ebx
005DB70F  74 28                           je 0x1405db739
005DB711  4D 8D 85 08 05 00 00            lea r8, [r13 + 0x508]
005DB718  8B CF                           mov ecx, edi
005DB71A  0F AF CA                        imul ecx, edx
005DB71D  41 03 D6                        add edx, r14d
005DB720  48 8D 04 89                     lea rax, [rcx + rcx*4]
005DB724  48 C1 E0 07                     shl rax, 7
005DB728  49 03 C1                        add rax, r9
005DB72B  49 89 00                        mov qword ptr [r8], rax
005DB72E  4D 8D 80 10 05 00 00            lea r8, [r8 + 0x510]
005DB735  3B D3                           cmp edx, ebx
005DB737  72 DF                           jb 0x1405db718
005DB739  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
005DB73E  48 8D 1D BB 48 A2 FF            lea rbx, [rip - 0x5db745]
005DB745  41 8B F4                        mov esi, r12d
005DB748  0F B7 05 B1 98 9E 00            movzx eax, word ptr [rip + 0x9e98b1]
005DB74F  44 89 64 24 4C                  mov dword ptr [rsp + 0x4c], r12d
005DB754  44 3B E0                        cmp r12d, eax
005DB757  0F 83 CD 03 00 00               jae 0x1405dbb2a
005DB75D  41 8B D4                        mov edx, r12d
005DB760  48 8D 4D B0                     lea rcx, [rbp - 0x50]
005DB764  48 8B 94 D3 C0 F6 FC 00         mov rdx, qword ptr [rbx + rdx*8 + 0xfcf6c0]
005DB76C  E8 3F 2D E4 FF                  call 0x14041e4b0
005DB771  EB 06                           jmp 0x1405db779
005DB773  41 BE 01 00 00 00               mov r14d, 1
005DB779  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
005DB77E  48 8D 4D B0                     lea rcx, [rbp - 0x50]
005DB782  E8 51 AF C7 FF                  call 0x1402566d8
005DB787  45 33 C0                        xor r8d, r8d
005DB78A  85 C0                           test eax, eax
005DB78C  0F 85 90 03 00 00               jne 0x1405dbb22
005DB792  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
005DB797  0F 57 C0                        xorps xmm0, xmm0
005DB79A  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
005DB79E  44 0F B7 B1 88 00 00 00         movzx r14d, word ptr [rcx + 0x88]
005DB7A6  66 44 3B 35 F2 FD 82 00         cmp r14w, word ptr [rip + 0x82fdf2]
005DB7AE  4C 8B B9 80 00 00 00            mov r15, qword ptr [rcx + 0x80]
005DB7B5  66 44 89 75 88                  mov word ptr [rbp - 0x78], r14w
005DB7BA  73 0A                           jae 0x1405db7c6
005DB7BC  4A 8B 94 F3 A8 B5 E0 00         mov rdx, qword ptr [rbx + r14*8 + 0xe0b5a8]
005DB7C4  EB 03                           jmp 0x1405db7c9
005DB7C6  49 8B D0                        mov rdx, r8
005DB7C9  4C 23 FA                        and r15, rdx
005DB7CC  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
005DB7D0  74 A1                           je 0x1405db773
005DB7D2  8B C6                           mov eax, esi
005DB7D4  48 69 D0 10 05 00 00            imul rdx, rax, 0x510
005DB7DB  4A 8D 1C 2A                     lea rbx, [rdx + r13]
005DB7DF  66 44 89 73 04                  mov word ptr [rbx + 4], r14w
005DB7E4  66 44 89 63 06                  mov word ptr [rbx + 6], r12w
005DB7E9  0F B7 81 8C 00 00 00            movzx eax, word ptr [rcx + 0x8c]
005DB7F0  66 89 43 08                     mov word ptr [rbx + 8], ax
005DB7F4  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
005DB7F8  4C 89 7B 10                     mov qword ptr [rbx + 0x10], r15
005DB7FC  3B 74 24 44                     cmp esi, dword ptr [rsp + 0x44]
005DB800  73 20                           jae 0x1405db822
005DB802  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
005DB807  4C 03 EA                        add r13, rdx
005DB80A  41 0F B7 45 06                  movzx eax, word ptr [r13 + 6]
005DB80F  41 3B C4                        cmp eax, r12d
005DB812  75 0E                           jne 0x1405db822
005DB814  0F B7 81 8C 00 00 00            movzx eax, word ptr [rcx + 0x8c]
005DB81B  66 41 39 45 08                  cmp word ptr [r13 + 8], ax
005DB820  74 03                           je 0x1405db825
005DB822  4D 8B E8                        mov r13, r8
005DB825  B9 01 00 00 00                  mov ecx, 1
005DB82A  03 F1                           add esi, ecx
005DB82C  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
005DB830  41 8A F0                        mov sil, r8b
005DB833  44 38 44 24 40                  cmp byte ptr [rsp + 0x40], r8b
005DB838  0F 86 C2 00 00 00               jbe 0x1405db900
005DB83E  45 33 E4                        xor r12d, r12d
005DB841  40 0F B6 D6                     movzx edx, sil
005DB845  40 84 F6                        test sil, sil
005DB848  74 25                           je 0x1405db86f
005DB84A  44 8B 05 E7 97 9E 00            mov r8d, dword ptr [rip + 0x9e97e7]
005DB851  41 8B C0                        mov eax, r8d
005DB854  F7 D8                           neg eax
005DB856  1B C9                           sbb ecx, ecx
005DB858  23 D1                           and edx, ecx
005DB85A  B9 01 00 00 00                  mov ecx, 1
005DB85F  44 38 25 20 B2 9E 00            cmp byte ptr [rip + 0x9eb220], r12b
005DB866  74 07                           je 0x1405db86f
005DB868  45 85 C0                        test r8d, r8d
005DB86B  41 0F 45 D4                     cmovne edx, r12d
005DB86F  E8 9C 8A E3 FF                  call 0x140414310
005DB874  84 C0                           test al, al
005DB876  75 05                           jne 0x1405db87d
005DB878  85 D2                           test edx, edx
005DB87A  0F 45 D1                        cmovne edx, ecx
005DB87D  48 8D 3C 92                     lea rdi, [rdx + rdx*4]
005DB881  66 44 89 75 A0                  mov word ptr [rbp - 0x60], r14w
005DB886  48 C1 E7 07                     shl rdi, 7
005DB88A  48 8D 55 90                     lea rdx, [rbp - 0x70]
005DB88E  48 03 BB 08 05 00 00            add rdi, qword ptr [rbx + 0x508]
005DB895  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
005DB89A  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
005DB89E  4C 89 65 90                     mov qword ptr [rbp - 0x70], r12
005DB8A2  E8 D9 9B E3 FF                  call 0x140415480
005DB8A7  85 C0                           test eax, eax
005DB8A9  75 39                           jne 0x1405db8e4
005DB8AB  8D 58 01                        lea ebx, [rax + 1]
005DB8AE  8B 4C 24 3C                     mov ecx, dword ptr [rsp + 0x3c]
005DB8B2  E8 19 CD CF FF                  call 0x1402d85d0
005DB8B7  40 38 B0 08 8A 00 00            cmp byte ptr [rax + 0x8a08], sil
005DB8BE  75 0E                           jne 0x1405db8ce
005DB8C0  66 01 1F                        add word ptr [rdi], bx
005DB8C3  48 8B 80 C8 00 00 00            mov rax, qword ptr [rax + 0xc8]
005DB8CA  48 09 47 18                     or qword ptr [rdi + 0x18], rax
005DB8CE  48 8D 55 90                     lea rdx, [rbp - 0x70]
005DB8D2  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
005DB8D7  E8 A4 9B E3 FF                  call 0x140415480
005DB8DC  85 C0                           test eax, eax
005DB8DE  74 CE                           je 0x1405db8ae
005DB8E0  48 8B 5D A8                     mov rbx, qword ptr [rbp - 0x58]
005DB8E4  B9 01 00 00 00                  mov ecx, 1
005DB8E9  40 02 F1                        add sil, cl
005DB8EC  40 3A 74 24 40                  cmp sil, byte ptr [rsp + 0x40]
005DB8F1  0F 82 4A FF FF FF               jb 0x1405db841
005DB8F7  44 8B 64 24 4C                  mov r12d, dword ptr [rsp + 0x4c]
005DB8FC  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
005DB900  33 F6                           xor esi, esi
005DB902  8B CE                           mov ecx, esi
005DB904  44 8D 76 01                     lea r14d, [rsi + 1]
005DB908  85 FF                           test edi, edi
005DB90A  74 45                           je 0x1405db951
005DB90C  8B D6                           mov edx, esi
005DB90E  41 B8 80 02 00 00               mov r8d, 0x280
005DB914  48 8B 83 08 05 00 00            mov rax, qword ptr [rbx + 0x508]
005DB91B  66 39 34 02                     cmp word ptr [rdx + rax], si
005DB91F  75 0C                           jne 0x1405db92d
005DB921  8D 41 01                        lea eax, [rcx + 1]
005DB924  3B C7                           cmp eax, edi
005DB926  73 05                           jae 0x1405db92d
005DB928  41 03 C6                        add eax, r14d
005DB92B  EB F7                           jmp 0x1405db924
005DB92D  41 03 CE                        add ecx, r14d
005DB930  49 03 D0                        add rdx, r8
005DB933  3B CF                           cmp ecx, edi
005DB935  72 DD                           jb 0x1405db914
005DB937  48 8B 83 08 05 00 00            mov rax, qword ptr [rbx + 0x508]
005DB93E  8B CF                           mov ecx, edi
005DB940  66 39 30                        cmp word ptr [rax], si
005DB943  74 04                           je 0x1405db949
005DB945  44 00 73 0C                     add byte ptr [rbx + 0xc], r14b
005DB949  49 03 C0                        add rax, r8
005DB94C  49 2B CE                        sub rcx, r14
005DB94F  75 EF                           jne 0x1405db940
005DB951  48 39 B3 00 05 00 00            cmp qword ptr [rbx + 0x500], rsi
005DB958  75 19                           jne 0x1405db973
005DB95A  8B 05 BC 96 9E 00               mov eax, dword ptr [rip + 0x9e96bc]
005DB960  A8 02                           test al, 2
005DB962  74 0F                           je 0x1405db973
005DB964  4C 8D 45 80                     lea r8, [rbp - 0x80]
005DB968  49 8B D5                        mov rdx, r13
005DB96B  48 8B CB                        mov rcx, rbx
005DB96E  E8 A1 D3 FF FF                  call 0x1405d8d14
005DB973  8A 4B 0C                        mov cl, byte ptr [rbx + 0xc]
005DB976  41 3A CE                        cmp cl, r14b
005DB979  0F 97 C0                        seta al
005DB97C  88 83 A1 04 00 00               mov byte ptr [rbx + 0x4a1], al
005DB982  77 07                           ja 0x1405db98b
005DB984  80 8B A0 04 00 00 04            or byte ptr [rbx + 0x4a0], 4
005DB98B  44 8B FE                        mov r15d, esi
005DB98E  8B D6                           mov edx, esi
005DB990  84 C9                           test cl, cl
005DB992  74 2E                           je 0x1405db9c2
005DB994  8B C2                           mov eax, edx
005DB996  41 03 D6                        add edx, r14d
005DB999  48 8D 0C 80                     lea rcx, [rax + rax*4]
005DB99D  48 C1 E1 07                     shl rcx, 7
005DB9A1  48 03 8B 08 05 00 00            add rcx, qword ptr [rbx + 0x508]
005DB9A8  0F B7 01                        movzx eax, word ptr [rcx]
005DB9AB  44 03 F8                        add r15d, eax
005DB9AE  66 89 41 06                     mov word ptr [rcx + 6], ax
005DB9B2  66 89 41 08                     mov word ptr [rcx + 8], ax
005DB9B6  66 89 41 0A                     mov word ptr [rcx + 0xa], ax
005DB9BA  0F B6 43 0C                     movzx eax, byte ptr [rbx + 0xc]
005DB9BE  3B D0                           cmp edx, eax
005DB9C0  72 D2                           jb 0x1405db994
005DB9C2  41 8B C7                        mov eax, r15d
005DB9C5  48 C7 45 D0 01 00 20 00         mov qword ptr [rbp - 0x30], 0x200001
005DB9CD  03 44 24 38                     add eax, dword ptr [rsp + 0x38]
005DB9D1  48 8D 4D D8                     lea rcx, [rbp - 0x28]
005DB9D5  33 D2                           xor edx, edx
005DB9D7  41 B8 00 01 00 00               mov r8d, 0x100
005DB9DD  42 8D 04 78                     lea eax, [rax + r15*2]
005DB9E1  83 C0 03                        add eax, 3
005DB9E4  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
005DB9E8  E8 53 B2 0E 00                  call 0x1406c6c40
005DB9ED  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
005DB9F1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
005DB9F5  0F B7 53 04                     movzx edx, word ptr [rbx + 4]
005DB9F9  E8 C2 FC C7 FF                  call 0x14025b6c0
005DB9FE  4D 85 ED                        test r13, r13
005DBA01  74 09                           je 0x1405dba0c
005DBA03  4D 8B 8D 50 04 00 00            mov r9, qword ptr [r13 + 0x450]
005DBA0A  EB 03                           jmp 0x1405dba0f
005DBA0C  4C 8B CE                        mov r9, rsi
005DBA0F  4C 8D 83 50 04 00 00            lea r8, [rbx + 0x450]
005DBA16  33 C9                           xor ecx, ecx
005DBA18  48 8D 55 D0                     lea rdx, [rbp - 0x30]
005DBA1C  E8 0F 95 17 00                  call 0x140754f30
005DBA21  85 C0                           test eax, eax
005DBA23  0F 88 C2 02 00 00               js 0x1405dbceb
005DBA29  40 38 B3 A1 04 00 00            cmp byte ptr [rbx + 0x4a1], sil
005DBA30  0F 84 B9 00 00 00               je 0x1405dbaef
005DBA36  8B FE                           mov edi, esi
005DBA38  33 D2                           xor edx, edx
005DBA3A  0F B6 43 0C                     movzx eax, byte ptr [rbx + 0xc]
005DBA3E  3B F8                           cmp edi, eax
005DBA40  0F 83 A5 00 00 00               jae 0x1405dbaeb
005DBA46  4C 8B B3 08 05 00 00            mov r14, qword ptr [rbx + 0x508]
005DBA4D  8B C7                           mov eax, edi
005DBA4F  48 8D 34 80                     lea rsi, [rax + rax*4]
005DBA53  48 C1 E6 07                     shl rsi, 7
005DBA57  42 0F B7 04 36                  movzx eax, word ptr [rsi + r14]
005DBA5C  66 85 C0                        test ax, ax
005DBA5F  74 7C                           je 0x1405dbadd
005DBA61  8B C8                           mov ecx, eax
005DBA63  48 C7 45 D0 01 00 20 00         mov qword ptr [rbp - 0x30], 0x200001
005DBA6B  03 44 24 38                     add eax, dword ptr [rsp + 0x38]
005DBA6F  33 D2                           xor edx, edx
005DBA71  41 B8 00 01 00 00               mov r8d, 0x100
005DBA77  8D 04 48                        lea eax, [rax + rcx*2]
005DBA7A  83 C0 03                        add eax, 3
005DBA7D  48 8D 4D D8                     lea rcx, [rbp - 0x28]
005DBA81  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
005DBA85  E8 B6 B1 0E 00                  call 0x1406c6c40
005DBA8A  4E 8B 44 36 18                  mov r8, qword ptr [rsi + r14 + 0x18]
005DBA8F  48 8D 4D D0                     lea rcx, [rbp - 0x30]
005DBA93  0F B7 53 04                     movzx edx, word ptr [rbx + 4]
005DBA97  E8 24 FC C7 FF                  call 0x14025b6c0
005DBA9C  33 C9                           xor ecx, ecx
005DBA9E  4D 85 ED                        test r13, r13
005DBAA1  74 1A                           je 0x1405dbabd
005DBAA3  41 0F B6 45 0C                  movzx eax, byte ptr [r13 + 0xc]
005DBAA8  3B F8                           cmp edi, eax
005DBAAA  73 11                           jae 0x1405dbabd
005DBAAC  49 8B 85 08 05 00 00            mov rax, qword ptr [r13 + 0x508]
005DBAB3  4C 8B 8C 30 38 02 00 00         mov r9, qword ptr [rax + rsi + 0x238]
005DBABB  EB 03                           jmp 0x1405dbac0
005DBABD  4C 8B C9                        mov r9, rcx
005DBAC0  4D 8D 86 38 02 00 00            lea r8, [r14 + 0x238]
005DBAC7  4C 03 C6                        add r8, rsi
005DBACA  48 8D 55 D0                     lea rdx, [rbp - 0x30]
005DBACE  E8 5D 94 17 00                  call 0x140754f30
005DBAD3  33 D2                           xor edx, edx
005DBAD5  85 C0                           test eax, eax
005DBAD7  0F 88 FC 01 00 00               js 0x1405dbcd9
005DBADD  41 BE 01 00 00 00               mov r14d, 1
005DBAE3  41 03 FE                        add edi, r14d
005DBAE6  E9 4F FF FF FF                  jmp 0x1405dba3a
005DBAEB  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
005DBAEF  41 0F B6 C7                     movzx eax, r15b
005DBAF3  48 8B CB                        mov rcx, rbx
005DBAF6  66 89 43 0A                     mov word ptr [rbx + 0xa], ax
005DBAFA  66 89 83 92 04 00 00            mov word ptr [rbx + 0x492], ax
005DBB01  66 89 83 96 04 00 00            mov word ptr [rbx + 0x496], ax
005DBB08  E8 D3 02 00 00                  call 0x1405dbde0
005DBB0D  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
005DBB12  48 8D 1D E7 44 A2 FF            lea rbx, [rip - 0x5dbb19]
005DBB19  8B 74 24 60                     mov esi, dword ptr [rsp + 0x60]
005DBB1D  E9 57 FC FF FF                  jmp 0x1405db779
005DBB22  45 03 E6                        add r12d, r14d
005DBB25  E9 1E FC FF FF                  jmp 0x1405db748
005DBB2A  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
005DBB2E  B9 40 00 00 00                  mov ecx, 0x40
005DBB33  48 C1 E2 03                     shl rdx, 3
005DBB37  41 B8 50 50 4D 70               mov r8d, 0x704d5050
005DBB3D  E8 AE 65 5A 00                  call 0x140b820f0
005DBB42  45 33 E4                        xor r12d, r12d
005DBB45  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
005DBB4A  48 85 C0                        test rax, rax
005DBB4D  0F 84 9D 01 00 00               je 0x1405dbcf0
005DBB53  48 8B F0                        mov rsi, rax
005DBB56  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
005DBB5A  85 C0                           test eax, eax
005DBB5C  0F 84 70 01 00 00               je 0x1405dbcd2
005DBB62  49 8D 9D 88 04 00 00            lea rbx, [r13 + 0x488]
005DBB69  44 8B F8                        mov r15d, eax
005DBB6C  0F B7 83 82 FB FF FF            movzx eax, word ptr [rbx - 0x47e]
005DBB73  48 8B CE                        mov rcx, rsi
005DBB76  48 89 73 D0                     mov qword ptr [rbx - 0x30], rsi
005DBB7A  FF C0                           inc eax
005DBB7C  44 8B C0                        mov r8d, eax
005DBB7F  49 C1 E0 03                     shl r8, 3
005DBB83  49 03 F0                        add rsi, r8
005DBB86  89 03                           mov dword ptr [rbx], eax
005DBB88  48 89 73 D8                     mov qword ptr [rbx - 0x28], rsi
005DBB8C  49 03 F0                        add rsi, r8
005DBB8F  48 89 73 E0                     mov qword ptr [rbx - 0x20], rsi
005DBB93  49 03 F0                        add rsi, r8
005DBB96  48 8B 53 C8                     mov rdx, qword ptr [rbx - 0x38]
005DBB9A  48 81 C2 48 01 00 00            add rdx, 0x148
005DBBA1  E8 9A AC 0E 00                  call 0x1406c6840
005DBBA6  44 8B 03                        mov r8d, dword ptr [rbx]
005DBBA9  48 8B 53 C8                     mov rdx, qword ptr [rbx - 0x38]
005DBBAD  48 8B 4B D8                     mov rcx, qword ptr [rbx - 0x28]
005DBBB1  48 81 C2 48 01 00 00            add rdx, 0x148
005DBBB8  49 C1 E0 03                     shl r8, 3
005DBBBC  E8 7F AC 0E 00                  call 0x1406c6840
005DBBC1  48 8B 4B C8                     mov rcx, qword ptr [rbx - 0x38]
005DBBC5  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
005DBBC9  48 89 43 E8                     mov qword ptr [rbx - 0x18], rax
005DBBCD  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
005DBBD1  48 89 43 F0                     mov qword ptr [rbx - 0x10], rax
005DBBD5  44 38 63 19                     cmp byte ptr [rbx + 0x19], r12b
005DBBD9  0F 84 DE 00 00 00               je 0x1405dbcbd
005DBBDF  45 8B F4                        mov r14d, r12d
005DBBE2  44 38 A3 84 FB FF FF            cmp byte ptr [rbx - 0x47c], r12b
005DBBE9  0F 86 C8 00 00 00               jbe 0x1405dbcb7
005DBBEF  41 BD 01 00 00 00               mov r13d, 1
005DBBF5  41 8B C6                        mov eax, r14d
005DBBF8  48 8B CE                        mov rcx, rsi
005DBBFB  48 8D 3C 80                     lea rdi, [rax + rax*4]
005DBBFF  48 C1 E7 07                     shl rdi, 7
005DBC03  48 03 BB 80 00 00 00            add rdi, qword ptr [rbx + 0x80]
005DBC0A  0F B7 07                        movzx eax, word ptr [rdi]
005DBC0D  66 85 C0                        test ax, ax
005DBC10  0F 84 89 00 00 00               je 0x1405dbc9f
005DBC16  48 89 B7 40 02 00 00            mov qword ptr [rdi + 0x240], rsi
005DBC1D  FF C0                           inc eax
005DBC1F  44 8B C0                        mov r8d, eax
005DBC22  49 C1 E0 03                     shl r8, 3
005DBC26  49 03 F0                        add rsi, r8
005DBC29  89 87 70 02 00 00               mov dword ptr [rdi + 0x270], eax
005DBC2F  48 89 B7 48 02 00 00            mov qword ptr [rdi + 0x248], rsi
005DBC36  49 03 F0                        add rsi, r8
005DBC39  48 89 B7 50 02 00 00            mov qword ptr [rdi + 0x250], rsi
005DBC40  49 03 F0                        add rsi, r8
005DBC43  48 8B 97 38 02 00 00            mov rdx, qword ptr [rdi + 0x238]
005DBC4A  48 81 C2 48 01 00 00            add rdx, 0x148
005DBC51  E8 EA AB 0E 00                  call 0x1406c6840
005DBC56  44 8B 87 70 02 00 00            mov r8d, dword ptr [rdi + 0x270]
005DBC5D  48 8B 97 38 02 00 00            mov rdx, qword ptr [rdi + 0x238]
005DBC64  48 8B 8F 48 02 00 00            mov rcx, qword ptr [rdi + 0x248]
005DBC6B  48 81 C2 48 01 00 00            add rdx, 0x148
005DBC72  49 C1 E0 03                     shl r8, 3
005DBC76  E8 C5 AB 0E 00                  call 0x1406c6840
005DBC7B  48 8B 87 38 02 00 00            mov rax, qword ptr [rdi + 0x238]
005DBC82  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
005DBC86  48 89 8F 58 02 00 00            mov qword ptr [rdi + 0x258], rcx
005DBC8D  48 8B 87 38 02 00 00            mov rax, qword ptr [rdi + 0x238]
005DBC94  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
005DBC98  48 89 8F 60 02 00 00            mov qword ptr [rdi + 0x260], rcx
005DBC9F  0F B6 83 84 FB FF FF            movzx eax, byte ptr [rbx - 0x47c]
005DBCA6  45 03 F5                        add r14d, r13d
005DBCA9  44 3B F0                        cmp r14d, eax
005DBCAC  0F 82 43 FF FF FF               jb 0x1405dbbf5
005DBCB2  4D 8B F5                        mov r14, r13
005DBCB5  EB 06                           jmp 0x1405dbcbd
005DBCB7  41 BE 01 00 00 00               mov r14d, 1
005DBCBD  48 81 C3 10 05 00 00            add rbx, 0x510
005DBCC4  4D 2B FE                        sub r15, r14
005DBCC7  0F 85 9F FE FF FF               jne 0x1405dbb6c
005DBCCD  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
005DBCD2  44 8B 7C 24 34                  mov r15d, dword ptr [rsp + 0x34]
005DBCD7  EB 1F                           jmp 0x1405dbcf8
005DBCD9  44 8A F2                        mov r14b, dl
005DBCDC  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
005DBCE1  45 33 E4                        xor r12d, r12d
005DBCE4  44 8B 7C 24 34                  mov r15d, dword ptr [rsp + 0x34]
005DBCE9  EB 0D                           jmp 0x1405dbcf8
005DBCEB  44 8A F6                        mov r14b, sil
005DBCEE  EB EC                           jmp 0x1405dbcdc
005DBCF0  45 8A F4                        mov r14b, r12b
005DBCF3  EB DD                           jmp 0x1405dbcd2
005DBCF5  44 8B FB                        mov r15d, ebx
005DBCF8  48 8D 0D 21 0F 93 00            lea rcx, [rip + 0x930f21]
005DBCFF  E8 6C C7 C2 FF                  call 0x140208470
005DBD04  8A D0                           mov dl, al
005DBD06  41 8A CE                        mov cl, r14b
005DBD09  F6 D9                           neg cl
005DBD0B  41 8A C6                        mov al, r14b
005DBD0E  41 8A CE                        mov cl, r14b
005DBD11  49 8B DC                        mov rbx, r12
005DBD14  4D 1B D2                        sbb r10, r10
005DBD17  4D 23 D5                        and r10, r13
005DBD1A  45 84 F6                        test r14b, r14b
005DBD1D  4C 89 15 B4 C6 92 00            mov qword ptr [rip + 0x92c6b4], r10
005DBD24  48 0F 44 5C 24 70               cmove rbx, qword ptr [rsp + 0x70]
005DBD2A  F6 D9                           neg cl
005DBD2C  48 8D 0D ED 0E 93 00            lea rcx, [rip + 0x930eed]
005DBD33  45 1B C0                        sbb r8d, r8d
005DBD36  45 23 C7                        and r8d, r15d
005DBD39  44 89 05 A0 C6 92 00            mov dword ptr [rip + 0x92c6a0], r8d
005DBD40  F6 D8                           neg al
005DBD42  4D 1B C0                        sbb r8, r8
005DBD45  4C 23 44 24 70                  and r8, qword ptr [rsp + 0x70]
005DBD4A  4C 89 05 57 C6 92 00            mov qword ptr [rip + 0x92c657], r8
005DBD51  E8 4A 6E DB FF                  call 0x140392ba0
005DBD56  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
005DBD5A  45 8B CF                        mov r9d, r15d
005DBD5D  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
005DBD62  4D 8B C5                        mov r8, r13
005DBD65  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
005DBD6A  E8 9D EE 18 00                  call 0x14076ac0c
005DBD6F  48 85 DB                        test rbx, rbx
005DBD72  74 0D                           je 0x1405dbd81
005DBD74  BA 50 50 4D 70                  mov edx, 0x704d5050
005DBD79  48 8B CB                        mov rcx, rbx
005DBD7C  E8 EF 6A 5A 00                  call 0x140b82870
005DBD81  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
005DBD86  48 85 C0                        test rax, rax
005DBD89  74 0D                           je 0x1405dbd98
005DBD8B  BA 50 50 4D 70                  mov edx, 0x704d5050
005DBD90  48 8B C8                        mov rcx, rax
005DBD93  E8 D8 6A 5A 00                  call 0x140b82870
005DBD98  E8 9F A3 ED FF                  call 0x1404b613c
005DBD9D  E8 B6 91 4A 00                  call 0x140a84f58
005DBDA2  EB 05                           jmp 0x1405dbda9
005DBDA4  E8 93 5A 00 00                  call 0x1405e183c
005DBDA9  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
005DBDB0  48 33 CC                        xor rcx, rsp
005DBDB3  E8 88 08 0D 00                  call 0x1406ac640
005DBDB8  4C 8D 9C 24 F0 01 00 00         lea r11, [rsp + 0x1f0]
005DBDC0  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
005DBDC4  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
005DBDC8  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
005DBDCC  49 8B E3                        mov rsp, r11
005DBDCF  41 5F                           pop r15
005DBDD1  41 5E                           pop r14
005DBDD3  41 5D                           pop r13
005DBDD5  41 5C                           pop r12
005DBDD7  5D                              pop rbp
005DBDD8  C3                              ret
005DBDD9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmParkRegisterParking(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1D0;
    unsigned int v_stack_m1D4;
    unsigned int v_stack_m1D8;
    unsigned int v_stack_m1DC;
    unsigned int v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned __int8 v_stack_m1F8;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (496);
    result = (*(unsigned __int64 *)(v_rip + 8581643)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 280 + 224) = result;
    a2 = 0;
    result = memset(v_rsp - 280 - 48, a2, 264, a4);
    result = 0;
    v_r12 = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 96) = 0;
    v_stack_m1DC = 0;
    v_stack_m1C8 = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 112) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 280 - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 280 - 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 280 - 80) = v_xmm1;
    result = Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline(v_rsp - 280 - 48, a2, 264, a4);
    if ((unsigned int)(result) != 0) goto loc_005DBDA4;
    v_stack_m1A8 = 0;
    v_stack_m1B0 = 0;
    v_rsi = (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 8585843)));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 8585843))) < ((unsigned __int8)(v_r12 + 2))) { v_rsi = (unsigned int)(v_r12 + 2); }
    v_stack_m1A0 = 0;
    v_stack_m1D8 = (unsigned int)(v_rsi);
    v_stack_m1D4 = 0;
    if (*(unsigned __int64 *)(v_rip + 9621041) == 0) goto loc_005DB655;
    v_stack_m1B0 = *(unsigned __int64 *)(v_rip + 9621041);
    v_stack_m1A0 = *(unsigned __int64 *)(v_rip + 9620938);
    v_stack_m1D4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9621009)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9621009))) == 0) goto loc_005DB655;
loc_005DB5F4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9621041) + 1184 - 80)) == 0) goto loc_005DB645;
    result = *(unsigned __int64 *)(v_rip + 9620938);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9621041) + 1184)) & (8)) != 0) {
        a2 = 0;
        *(unsigned __int64 *)(v_rsp - 280 - 48) = 0x200001ULL;
        a3 = 256;
        a1 = v_rsp - 280 - 40;
        result = memset(a1, a2, a3, a4);
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9621041) + 1184 - 1168);
        a1 = v_rsp - 280 - 48;
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9621041) + 1184 - 1180);
        result = KeAddGroupAffinityEx(a1, a2, a3, a4);
        a4 = 0;
        a2 = v_rip - 1401465;
        a3 = 0;
        a1 = v_rsp - 280 - 48;
        result = PopExecuteOnTargetProcessors(a1, a2, a3, a4);
    }
    v_rbx = (*(unsigned __int64 *)(v_rip + 9621041) + 1184) + (0x510ULL);
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9621009))))) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_005DB5F4;
loc_005DB655:
    if (0 >= (*(unsigned __int16 *)(v_rip + 10394019))) goto loc_005DB6AA;
loc_005DB66F:
    result = KeInitializeSchedulerSubNodeEnumerationContext(v_rsp - 280 - 80, *(unsigned __int64 *)(v_rip - 6141551 + 0 * 8 + 16578240), a3, a4);
    goto loc_005DB687;
loc_005DB684:
    v_rbx = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
loc_005DB687:
    result = KeEnumerateNextSchedulerSubNodeInNode(v_rsp - 280 - 80, v_stack_m1C8, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_005DB684;
    v_rdi = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 10393952)))) goto loc_005DB66F;
loc_005DB6AA:
    a2 = (unsigned int)((v_stack_m1C8) * ((unsigned int)(v_rbx)));
    result = ExAllocatePool2(64, a2, (unsigned int)(0x704D5050ULL), a4);
    v_stack_m1C0 = result;
    if (result == 0) goto loc_005DBCF8;
    v_stack_m1E4 = (unsigned int)(v_rbx);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)((unsigned int)(v_stack_m1D8))))) * ((unsigned int)(v_rbx)));
    v_stack_m1D0 = (unsigned int)((unsigned __int8)((unsigned int)(v_stack_m1D8)));
    a2 = (unsigned int)((a1 + a1 * 4) << (7));
    result = ExAllocatePool2(64, a2, (unsigned int)(0x704D5050ULL), a4);
    if (result == 0) goto loc_005DBCF5;
    if ((unsigned int)(v_rbx) == 0) goto loc_005DB739;
loc_005DB718:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)((unsigned int)(v_stack_m1D8))))) * (0));
    a2 = (unsigned int)((0) + (1));
    result = (a1 + a1 * 4) << (7);
    result = (result) + (result);
    *(unsigned __int64 *)(result + 1288) = result;
    if (a2 < ((unsigned int)(v_rbx))) goto loc_005DB718;
loc_005DB739:
    v_stack_m1E0 = 0;
loc_005DB748:
    v_stack_m1CC = 0;
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 10393777)))) goto loc_005DBB2A;
    result = KeInitializeSchedulerSubNodeEnumerationContext(v_rsp - 280 - 80, *(unsigned __int64 *)(v_rip - 6141765 + 0 * 8 + 16578240), result + 1288 + 1296, result);
    goto loc_005DB779;
loc_005DB773:
loc_005DB779:
    result = KeEnumerateNextSchedulerSubNodeInNode(v_rsp - 280 - 80, v_stack_m1C8, result + 1288 + 1296, result);
    a3 = 0;
    if ((unsigned int)(result) != 0) goto loc_005DBB22;
    *(unsigned __int64 *)(v_rsp - 280 - 128) = v_xmm0;
    *(unsigned __int16 *)(v_rsp - 280 - 120) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1C8 + 136));
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m1C8 + 136))) >= (*(unsigned __int16 *)(v_rip + 8584690))) goto loc_005DB7C6;
    goto loc_005DB7C9;
loc_005DB7C6:
loc_005DB7C9:
    v_r15 = (*(unsigned __int64 *)(v_stack_m1C8 + 128)) & (0);
    *(unsigned __int64 *)(v_rsp - 280 - 128) = v_r15;
    if (condition_is_equal) goto loc_005DB773;
    a2 = (0) * (0);
    *(unsigned __int16 *)(a2 + result * 1 + 4) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1C8 + 136));
    *(unsigned __int16 *)(a2 + result * 1 + 6) = 0;
    *(unsigned __int16 *)(a2 + result * 1 + 8) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1C8 + 140));
    *(unsigned __int64 *)(v_rsp - 280 - 88) = a2 + result * 1;
    *(unsigned __int64 *)(a2 + result * 1 + 16) = v_r15;
    if (0 >= v_stack_m1D4) goto loc_005DB822;
    v_r13 = (v_stack_m1B0) + (a2);
    if (((unsigned int)(*(unsigned __int16 *)(v_r13 + 6))) != 0) goto loc_005DB822;
    if ((*(unsigned __int16 *)(v_r13 + 8)) != ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m1C8 + 140)))) {
        v_r13 = 0;
    }
    v_rsi = (unsigned int)((0) + (1));
    v_stack_m1B8 = (unsigned int)(v_rsi);
    if (v_stack_m1D8 <= 0) goto loc_005DB900;
    v_r12 = 0;
loc_005DB841:
    if (0 == 0) goto loc_005DB86F;
    result = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10393575))))));
    a2 = (unsigned int)((0) & (1));
    if ((*(unsigned __int8 *)(v_rip + 10400288)) != 0) {
        if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10393575))) != 0) { a2 = 0; }
    }
    result = PpmHeteroIsMultiClassParkingEnabled(1, a2, (unsigned int)(*(unsigned int *)(v_rip + 10393575)), result);
    if ((unsigned __int8)(result) == 0) {
        if (a2 != 0) { a2 = 1; }
    }
    *(unsigned __int16 *)(v_rsp - 280 - 96) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1C8 + 136));
    v_rdi = (a2 + a2 * 4) << (7);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a2 + result * 1 + 1288));
    *(unsigned __int64 *)(v_rsp - 280 - 104) = v_r15;
    *(unsigned __int64 *)(v_rsp - 280 - 112) = 0;
    result = KeEnumerateNextProcessor(v_stack_m1DC, v_rsp - 280 - 112, (unsigned int)(*(unsigned int *)(v_rip + 10393575)), result);
    if ((unsigned int)(result) != 0) goto loc_005DB8E4;
loc_005DB8AE:
    result = KeGetPrcb((unsigned int)(v_stack_m1DC), v_rsp - 280 - 112, (unsigned int)(*(unsigned int *)(v_rip + 10393575)), result);
    if ((*(unsigned __int8 *)(result + 35336)) == 0) {
        result = *(unsigned __int64 *)(result + 200);
    }
    result = KeEnumerateNextProcessor(v_stack_m1DC, v_rsp - 280 - 112, (unsigned int)(*(unsigned int *)(v_rip + 10393575)), result);
    if ((unsigned int)(result) == 0) goto loc_005DB8AE;
loc_005DB8E4:
    v_rsi = (unsigned __int8)((0) + (1));
    if (((unsigned __int8)(v_rsi)) < v_stack_m1D8) goto loc_005DB841;
loc_005DB900:
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(v_stack_m1D0)) == 0) goto loc_005DB951;
loc_005DB914:
    if ((*(unsigned __int16 *)(0 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1288) * 1)) != 0) goto loc_005DB92D;
loc_005DB924:
    if (((unsigned int)(0 + 1)) >= ((unsigned int)((unsigned int)(v_stack_m1D0)))) goto loc_005DB92D;
    result = (unsigned int)((0 + 1) + ((unsigned int)(v_rsi + 1)));
    goto loc_005DB924;
loc_005DB92D:
    a1 = (unsigned int)((0) + ((unsigned int)(v_rsi + 1)));
    a2 = (0) + (640);
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(v_stack_m1D0)))) goto loc_005DB914;
loc_005DB940:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1288))) != 0) {
    }
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1288)) + (640);
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m1D0)))) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_005DB940;
loc_005DB951:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1280)) != 0) goto loc_005DB973;
    result = (unsigned int)(*(unsigned int *)(v_rip + 10393276));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10393276)))) & (2)) != 0) {
        a3 = v_rsp - 280 - 128;
        a2 = v_r13;
        a1 = *(unsigned __int64 *)(v_rsp - 280 - 88);
        result = PpmHeteroHgsRegisterContainmentGroups(a1, a2, a3, result);
    }
    result = (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 12))) > ((unsigned __int8)(v_rsi + 1))) ? 1 : 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1185) = (unsigned __int8)(result);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 12))) <= ((unsigned __int8)(v_rsi + 1))) {
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 12)) == 0) goto loc_005DB9C2;
loc_005DB994:
    a2 = (unsigned int)((0) + ((unsigned int)(v_rsi + 1)));
    a1 = (0 + 0 * 4) << (7);
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1288));
    v_r15 = (unsigned int)((0) + ((unsigned int)(*(unsigned __int16 *)(a1))));
    *(unsigned __int16 *)(a1 + 6) = (unsigned __int16)(*(unsigned __int16 *)(a1));
    *(unsigned __int16 *)(a1 + 8) = (unsigned __int16)(*(unsigned __int16 *)(a1));
    *(unsigned __int16 *)(a1 + 10) = (unsigned __int16)(*(unsigned __int16 *)(a1));
    if (a2 < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 12)))) goto loc_005DB994;
loc_005DB9C2:
    *(unsigned __int64 *)(v_rsp - 280 - 48) = 0x200001ULL;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) + (v_stack_m1E0));
    a2 = 0;
    result = (unsigned int)((result + v_r15 * 2) + (3));
    v_stack_m1E0 = (unsigned int)(result);
    result = memset(v_rsp - 280 - 40, a2, 256, result);
    result = KeAddGroupAffinityEx(v_rsp - 280 - 48, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 4), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 16), result);
    if (v_r13 == 0) goto loc_005DBA0C;
    goto loc_005DBA0F;
loc_005DBA0C:
loc_005DBA0F:
    a1 = 0;
    result = PpmIdleInitializeConcurrency(a1, v_rsp - 280 - 48, *(unsigned __int64 *)(v_rsp - 280 - 88) + 1104, 0);
    if (sign_flag) goto loc_005DBCEB;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1185)) == 0) goto loc_005DBAEF;
    a2 = 0;
loc_005DBA3A:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 12)))) goto loc_005DBAEB;
    v_rsi = (0 + 0 * 4) << (7);
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1288) * 1)) == 0) goto loc_005DBADD;
    *(unsigned __int64 *)(v_rsp - 280 - 48) = 0x200001ULL;
    result = (unsigned int)((*(unsigned __int16 *)(v_rsi + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1288) * 1)) + (v_stack_m1E0));
    a2 = 0;
    result = (unsigned int)((result + (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1288) * 1))) * 2) + (3));
    v_stack_m1E0 = (unsigned int)(result);
    result = memset(v_rsp - 280 - 40, a2, 256, 0);
    result = KeAddGroupAffinityEx(v_rsp - 280 - 48, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 4), *(unsigned __int64 *)(v_rsi + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1288) * 1 + 24), 0);
    a1 = 0;
    if (v_r13 == 0) goto loc_005DBABD;
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(v_r13 + 12)))) goto loc_005DBABD;
    goto loc_005DBAC0;
loc_005DBABD:
loc_005DBAC0:
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1288) + 568) + (v_rsi);
    result = PpmIdleInitializeConcurrency(a1, v_rsp - 280 - 48, a3, 0);
    a2 = 0;
    if (sign_flag) goto loc_005DBCD9;
loc_005DBADD:
    v_rdi = (unsigned int)((0) + (1));
    goto loc_005DBA3A;
loc_005DBAEB:
loc_005DBAEF:
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 10) = (unsigned __int16)((unsigned __int8)(v_r15));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1170) = (unsigned __int16)((unsigned __int8)(v_r15));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 280 - 88) + 1174) = (unsigned __int16)((unsigned __int8)(v_r15));
    result = PpmParkRegisterRestriction(*(unsigned __int64 *)(v_rsp - 280 - 88), a2, a3, 0);
    goto loc_005DB779;
loc_005DBB22:
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m1CC)) + (1));
    goto loc_005DB748;
loc_005DBB2A:
    a2 = ((unsigned int)(v_stack_m1E0)) << (3);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x704D5050ULL), 0);
    v_r12 = 0;
    v_stack_m1A8 = result;
    if (result == 0) goto loc_005DBCF0;
    if ((unsigned int)((unsigned int)(v_stack_m1E4)) == 0) goto loc_005DBCD2;
loc_005DBB6C:
    *(unsigned __int64 *)(v_stack_m1C0 + 1160 - 48) = result;
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m1C0 + 1160 - 1150)) + 1);
    a3 = ((unsigned int)((unsigned int)(result))) << (3);
    v_rsi = (result) + (a3);
    *(unsigned int *)(v_stack_m1C0 + 1160) = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_m1C0 + 1160 - 40) = v_rsi;
    v_rsi = (v_rsi) + (a3);
    *(unsigned __int64 *)(v_stack_m1C0 + 1160 - 32) = v_rsi;
    v_rsi = (v_rsi) + (a3);
    a2 = (*(unsigned __int64 *)(v_stack_m1C0 + 1160 - 56)) + (328);
    result = memcpy(result, a2, a3, 0);
    a2 = (*(unsigned __int64 *)(v_stack_m1C0 + 1160 - 56)) + (328);
    a3 = ((unsigned int)(*(unsigned int *)(v_stack_m1C0 + 1160))) << (3);
    result = memcpy(*(unsigned __int64 *)(v_stack_m1C0 + 1160 - 40), a2, a3, 0);
    *(unsigned __int64 *)(v_stack_m1C0 + 1160 - 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1C0 + 1160 - 56) + 24);
    *(unsigned __int64 *)(v_stack_m1C0 + 1160 - 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1C0 + 1160 - 56) + 24);
    if ((*(unsigned __int8 *)(v_stack_m1C0 + 1160 + 25)) == 0) goto loc_005DBCBD;
    if ((*(unsigned __int8 *)(v_stack_m1C0 + 1160 - 1148)) <= 0) goto loc_005DBCB7;
loc_005DBBF5:
    v_rdi = (0 + 0 * 4) << (7);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_stack_m1C0 + 1160 + 128));
    result = *(unsigned __int16 *)(v_rdi);
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rdi)) != 0) {
        *(unsigned __int64 *)(v_rdi + 576) = v_rsi;
        result = (unsigned int)((*(unsigned __int16 *)(v_rdi)) + 1);
        a3 = (unsigned int)(result);
        a3 = (a3) << (3);
        v_rsi = (v_rsi) + (a3);
        *(unsigned int *)(v_rdi + 624) = (unsigned int)(result);
        *(unsigned __int64 *)(v_rdi + 584) = v_rsi;
        v_rsi = (v_rsi) + (a3);
        *(unsigned __int64 *)(v_rdi + 592) = v_rsi;
        v_rsi = (v_rsi) + (a3);
        a2 = *(unsigned __int64 *)(v_rdi + 568);
        a2 = (a2) + (328);
        result = memcpy(v_rsi, a2, a3, 0);
        a3 = *(unsigned int *)(v_rdi + 624);
        a2 = *(unsigned __int64 *)(v_rdi + 568);
        a1 = *(unsigned __int64 *)(v_rdi + 584);
        a2 = (a2) + (328);
        a3 = (a3) << (3);
        result = memcpy(a1, a2, a3, 0);
        result = *(unsigned __int64 *)(v_rdi + 568);
        a1 = *(unsigned __int64 *)(result + 24);
        *(unsigned __int64 *)(v_rdi + 600) = a1;
        result = *(unsigned __int64 *)(v_rdi + 568);
        a1 = *(unsigned __int64 *)(result + 24);
        *(unsigned __int64 *)(v_rdi + 608) = a1;
    }
    v_r14 = (unsigned int)((0) + (1));
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_m1C0 + 1160 - 1148)))) goto loc_005DBBF5;
    goto loc_005DBCBD;
loc_005DBCB7:
loc_005DBCBD:
    v_rbx = (v_stack_m1C0 + 1160) + (0x510ULL);
    v_r15 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m1E4)))) - (1);
    if (condition_is_not_equal) goto loc_005DBB6C;
loc_005DBCD2:
    goto loc_005DBCF8;
loc_005DBCD9:
loc_005DBCDC:
    v_r12 = 0;
    goto loc_005DBCF8;
loc_005DBCEB:
    goto loc_005DBCDC;
loc_005DBCF0:
    goto loc_005DBCD2;
loc_005DBCF5:
loc_005DBCF8:
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 9637665, a2, a3, 0);
    a1 = (unsigned __int8)(-(0));
    v_r10 = (v_r10) & (v_stack_m1C0);
    *(unsigned __int64 *)(v_rip + 9619124) = v_r10;
    v_rbx = 0;
    if (0 == 0) { v_rbx = v_stack_m1A8; }
    a1 = (unsigned __int8)(-(0));
    a3 = (unsigned int)((a3) & ((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    *(unsigned int *)(v_rip + 9619104) = (unsigned int)(a3);
    result = (unsigned __int8)(-(0));
    a3 = (a3) & (v_stack_m1A8);
    *(unsigned __int64 *)(v_rip + 9619031) = a3;
    result = KeReleaseSpinLock(v_rip + 9637613, (unsigned __int8)(result), a3, 0);
    v_stack_m1F8 = 0;
    result = PpmParkFreeAllParkNodes(v_stack_m1B0, (unsigned int)(v_stack_m1D4), v_stack_m1C0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    if (v_rbx != 0) {
        a2 = 0x704D5050ULL;
        a1 = v_rbx;
        result = ExFreePoolWithTag(a1, a2, v_stack_m1C0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    }
    result = v_stack_m1A0;
    if (v_stack_m1A0 != 0) {
        a2 = 0x704D5050ULL;
        a1 = v_stack_m1A0;
        result = ExFreePoolWithTag(a1, a2, v_stack_m1C0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    }
    result = PpmParkApplyPolicy(a1, a2, v_stack_m1C0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    result = PpmParkParkingAvailable(a1, a2, v_stack_m1C0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    goto loc_005DBDA9;
loc_005DBDA4:
    result = PpmParkRegisterParkingEx(a1, a2, v_stack_m1C0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
loc_005DBDA9:
    a1 = (*(unsigned __int64 *)(v_rsp - 280 + 224)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m1C0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmParkRegisterParking(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1D0;
    uint32_t v_stack_m1D4;
    uint32_t v_stack_m1D8;
    uint32_t v_stack_m1DC;
    uint32_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint8_t v_stack_m1F8;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (496);
    result = (*(uint64_t *)(v_rip + 0x82F20B)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x118 + 0xE0) = result;
    Arg2 = 0;
    result = memset(local_rsp - 280 - 48, Arg2, 264, Arg4);
    result = 0;
    local_r12 = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x60) = 0;
    v_stack_m1DC = 0;
    v_stack_m1C8 = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x70) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x118 - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0x118 - 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x118 - 0x50) = v_xmm1;
    result = Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline(local_rsp - 280 - 48, Arg2, 264, Arg4);
    if ((uint32_t)(result) != 0) goto loc_005DBDA4;
    v_stack_m1A8 = 0;
    v_stack_m1B0 = 0;
    local_rsi = (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x830273)));
    if (((uint8_t)(*(uint8_t *)(v_rip + 0x830273))) < ((uint8_t)(local_r12 + 2))) { local_rsi = (uint32_t)(local_r12 + 2); }
    v_stack_m1A0 = 0;
    v_stack_m1D8 = (uint32_t)(local_rsi);
    v_stack_m1D4 = 0;
    if (*(uint64_t *)(v_rip + 0x92CE31) == 0) goto loc_005DB655;
    v_stack_m1B0 = *(uint64_t *)(v_rip + 0x92CE31);
    v_stack_m1A0 = *(uint64_t *)(v_rip + 0x92CDCA);
    v_stack_m1D4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x92CE11)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x92CE11))) == 0) goto loc_005DB655;
loc_005DB5F4:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x92CE31) + 0x4A0 - 0x50)) == 0) goto loc_005DB645;
    result = *(uint64_t *)(v_rip + 0x92CDCA);
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x92CE31) + 0x4A0)) & (8)) != 0) {
        Arg2 = 0;
        *(uint64_t *)(local_rsp - 0x118 - 0x30) = 0x200001ULL;
        Arg3 = 256;
        Arg1 = local_rsp - 280 - 40;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        Arg3 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x92CE31) + 0x4A0 - 0x490);
        Arg1 = local_rsp - 280 - 48;
        Arg2 = *(uint16_t *)(*(uint64_t *)(v_rip + 0x92CE31) + 0x4A0 - 0x49C);
        result = KeAddGroupAffinityEx(Arg1, Arg2, Arg3, Arg4);
        Arg4 = 0;
        Arg2 = v_rip - 1401465;
        Arg3 = 0;
        Arg1 = local_rsp - 280 - 48;
        result = PopExecuteOnTargetProcessors(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (*(uint64_t *)(v_rip + 0x92CE31) + 1184) + (0x510ULL);
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x92CE11))))) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_005DB5F4;
loc_005DB655:
    if (0 >= (*(uint16_t *)(v_rip + 0x9E99A3))) goto loc_005DB6AA;
loc_005DB66F:
    result = KeInitializeSchedulerSubNodeEnumerationContext(local_rsp - 280 - 80, *(uint64_t *)(v_rip - 0x5DB66F + 0x0 * 8 + 0xFCF6C0), Arg3, Arg4);
    goto loc_005DB687;
loc_005DB684:
    local_rbx = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
loc_005DB687:
    result = KeEnumerateNextSchedulerSubNodeInNode(local_rsp - 280 - 80, v_stack_m1C8, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_005DB684;
    local_rdi = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x9E9960)))) goto loc_005DB66F;
loc_005DB6AA:
    Arg2 = (uint32_t)((v_stack_m1C8) * ((uint32_t)(local_rbx)));
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x704D5050ULL), Arg4);
    v_stack_m1C0 = result;
    if (result == 0) goto loc_005DBCF8;
    v_stack_m1E4 = (uint32_t)(local_rbx);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)((uint32_t)(v_stack_m1D8))))) * ((uint32_t)(local_rbx)));
    v_stack_m1D0 = (uint32_t)((uint8_t)((uint32_t)(v_stack_m1D8)));
    Arg2 = (uint32_t)((Arg1 + Arg1 * 4) << (7));
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x704D5050ULL), Arg4);
    if (result == 0) goto loc_005DBCF5;
    if ((uint32_t)(local_rbx) == 0) goto loc_005DB739;
loc_005DB718:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)((uint32_t)(v_stack_m1D8))))) * (0));
    Arg2 = (uint32_t)((0) + (1));
    result = (Arg1 + Arg1 * 4) << (7);
    result = (result) + (result);
    *(uint64_t *)(result + 0x508) = result;
    if (Arg2 < ((uint32_t)(local_rbx))) goto loc_005DB718;
loc_005DB739:
    v_stack_m1E0 = 0;
loc_005DB748:
    v_stack_m1CC = 0;
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0x9E98B1)))) goto loc_005DBB2A;
    result = KeInitializeSchedulerSubNodeEnumerationContext(local_rsp - 280 - 80, *(uint64_t *)(v_rip - 0x5DB745 + 0x0 * 8 + 0xFCF6C0), result + 1288 + 1296, result);
    goto loc_005DB779;
loc_005DB773:
loc_005DB779:
    result = KeEnumerateNextSchedulerSubNodeInNode(local_rsp - 280 - 80, v_stack_m1C8, result + 1288 + 1296, result);
    Arg3 = 0;
    if ((uint32_t)(result) != 0) goto loc_005DBB22;
    *(uint64_t *)(local_rsp - 0x118 - 0x80) = v_xmm0;
    *(uint16_t *)(local_rsp - 0x118 - 0x78) = (uint16_t)(*(uint16_t *)(v_stack_m1C8 + 0x88));
    if (((uint16_t)(*(uint16_t *)(v_stack_m1C8 + 0x88))) >= (*(uint16_t *)(v_rip + 0x82FDF2))) goto loc_005DB7C6;
    goto loc_005DB7C9;
loc_005DB7C6:
loc_005DB7C9:
    local_r15 = (*(uint64_t *)(v_stack_m1C8 + 0x80)) & (0);
    *(uint64_t *)(local_rsp - 0x118 - 0x80) = local_r15;
    if (condition_is_equal) goto loc_005DB773;
    Arg2 = (0) * (0);
    *(uint16_t *)(Arg2 + result * 1 + 0x4) = (uint16_t)(*(uint16_t *)(v_stack_m1C8 + 0x88));
    *(uint16_t *)(Arg2 + result * 1 + 0x6) = 0;
    *(uint16_t *)(Arg2 + result * 1 + 0x8) = (uint16_t)(*(uint16_t *)(v_stack_m1C8 + 0x8C));
    *(uint64_t *)(local_rsp - 0x118 - 0x58) = Arg2 + result * 1;
    *(uint64_t *)(Arg2 + result * 1 + 0x10) = local_r15;
    if (0 >= v_stack_m1D4) goto loc_005DB822;
    local_r13 = (v_stack_m1B0) + (Arg2);
    if (((uint32_t)(*(uint16_t *)(local_r13 + 0x6))) != 0) goto loc_005DB822;
    if ((*(uint16_t *)(local_r13 + 0x8)) != ((uint16_t)(*(uint16_t *)(v_stack_m1C8 + 0x8C)))) {
        local_r13 = 0;
    }
    local_rsi = (uint32_t)((0) + (1));
    v_stack_m1B8 = (uint32_t)(local_rsi);
    if (v_stack_m1D8 <= 0) goto loc_005DB900;
    local_r12 = 0;
loc_005DB841:
    if (0 == 0) goto loc_005DB86F;
    result = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E97E7))))));
    Arg2 = (uint32_t)((0) & (1));
    if ((*(uint8_t *)(v_rip + 0x9EB220)) != 0) {
        if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E97E7))) != 0) { Arg2 = 0; }
    }
    result = PpmHeteroIsMultiClassParkingEnabled(1, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x9E97E7)), result);
    if ((uint8_t)(result) == 0) {
        if (Arg2 != 0) { Arg2 = 1; }
    }
    *(uint16_t *)(local_rsp - 0x118 - 0x60) = (uint16_t)(*(uint16_t *)(v_stack_m1C8 + 0x88));
    local_rdi = (Arg2 + Arg2 * 4) << (7);
    local_rdi = (local_rdi) + (*(uint64_t *)(Arg2 + result * 1 + 0x508));
    *(uint64_t *)(local_rsp - 0x118 - 0x68) = local_r15;
    *(uint64_t *)(local_rsp - 0x118 - 0x70) = 0;
    result = KeEnumerateNextProcessor(v_stack_m1DC, local_rsp - 280 - 112, (uint32_t)(*(uint32_t *)(v_rip + 0x9E97E7)), result);
    if ((uint32_t)(result) != 0) goto loc_005DB8E4;
loc_005DB8AE:
    result = KeGetPrcb((uint32_t)(v_stack_m1DC), local_rsp - 280 - 112, (uint32_t)(*(uint32_t *)(v_rip + 0x9E97E7)), result);
    if ((*(uint8_t *)(result + 0x8A08)) == 0) {
        result = *(uint64_t *)(result + 0xC8);
    }
    result = KeEnumerateNextProcessor(v_stack_m1DC, local_rsp - 280 - 112, (uint32_t)(*(uint32_t *)(v_rip + 0x9E97E7)), result);
    if ((uint32_t)(result) == 0) goto loc_005DB8AE;
loc_005DB8E4:
    local_rsi = (uint8_t)((0) + (1));
    if (((uint8_t)(local_rsi)) < v_stack_m1D8) goto loc_005DB841;
loc_005DB900:
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(v_stack_m1D0)) == 0) goto loc_005DB951;
loc_005DB914:
    if ((*(uint16_t *)(0 + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x508) * 1)) != 0) goto loc_005DB92D;
loc_005DB924:
    if (((uint32_t)(0 + 1)) >= ((uint32_t)((uint32_t)(v_stack_m1D0)))) goto loc_005DB92D;
    result = (uint32_t)((0 + 1) + ((uint32_t)(local_rsi + 1)));
    goto loc_005DB924;
loc_005DB92D:
    Arg1 = (uint32_t)((0) + ((uint32_t)(local_rsi + 1)));
    Arg2 = (0) + (640);
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(v_stack_m1D0)))) goto loc_005DB914;
loc_005DB940:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x508))) != 0) {
    }
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x508)) + (640);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m1D0)))) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_005DB940;
loc_005DB951:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x500)) != 0) goto loc_005DB973;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x9E96BC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E96BC)))) & (2)) != 0) {
        Arg3 = local_rsp - 280 - 128;
        Arg2 = local_r13;
        Arg1 = *(uint64_t *)(local_rsp - 0x118 - 0x58);
        result = PpmHeteroHgsRegisterContainmentGroups(Arg1, Arg2, Arg3, result);
    }
    result = (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0xC))) > ((uint8_t)(local_rsi + 1))) ? 1 : 0;
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x4A1) = (uint8_t)(result);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0xC))) <= ((uint8_t)(local_rsi + 1))) {
    }
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0xC)) == 0) goto loc_005DB9C2;
loc_005DB994:
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_rsi + 1)));
    Arg1 = (0 + 0 * 4) << (7);
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x508));
    local_r15 = (uint32_t)((0) + ((uint32_t)(*(uint16_t *)(Arg1))));
    *(uint16_t *)(Arg1 + 0x6) = (uint16_t)(*(uint16_t *)(Arg1));
    *(uint16_t *)(Arg1 + 0x8) = (uint16_t)(*(uint16_t *)(Arg1));
    *(uint16_t *)(Arg1 + 0xA) = (uint16_t)(*(uint16_t *)(Arg1));
    if (Arg2 < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0xC)))) goto loc_005DB994;
loc_005DB9C2:
    *(uint64_t *)(local_rsp - 0x118 - 0x30) = 0x200001ULL;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) + (v_stack_m1E0));
    Arg2 = 0;
    result = (uint32_t)((result + local_r15 * 2) + (3));
    v_stack_m1E0 = (uint32_t)(result);
    result = memset(local_rsp - 280 - 40, Arg2, 256, result);
    result = KeAddGroupAffinityEx(local_rsp - 280 - 48, *(uint16_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x4), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x10), result);
    if (local_r13 == 0) goto loc_005DBA0C;
    goto loc_005DBA0F;
loc_005DBA0C:
loc_005DBA0F:
    Arg1 = 0;
    result = PpmIdleInitializeConcurrency(Arg1, local_rsp - 280 - 48, *(uint64_t *)(local_rsp - 0x118 - 0x58) + 1104, 0);
    if (sign_flag) goto loc_005DBCEB;
    if ((*(uint8_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x4A1)) == 0) goto loc_005DBAEF;
    Arg2 = 0;
loc_005DBA3A:
    if (0 >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0xC)))) goto loc_005DBAEB;
    local_rsi = (0 + 0 * 4) << (7);
    if ((uint16_t)(*(uint16_t *)(local_rsi + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x508) * 1)) == 0) goto loc_005DBADD;
    *(uint64_t *)(local_rsp - 0x118 - 0x30) = 0x200001ULL;
    result = (uint32_t)((*(uint16_t *)(local_rsi + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x508) * 1)) + (v_stack_m1E0));
    Arg2 = 0;
    result = (uint32_t)((result + (uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x508) * 1))) * 2) + (3));
    v_stack_m1E0 = (uint32_t)(result);
    result = memset(local_rsp - 280 - 40, Arg2, 256, 0);
    result = KeAddGroupAffinityEx(local_rsp - 280 - 48, *(uint16_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x4), *(uint64_t *)(local_rsi + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x508) * 1 + 0x18), 0);
    Arg1 = 0;
    if (local_r13 == 0) goto loc_005DBABD;
    if (0 >= ((uint32_t)(*(uint8_t *)(local_r13 + 0xC)))) goto loc_005DBABD;
    goto loc_005DBAC0;
loc_005DBABD:
loc_005DBAC0:
    Arg3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x508) + 568) + (local_rsi);
    result = PpmIdleInitializeConcurrency(Arg1, local_rsp - 280 - 48, Arg3, 0);
    Arg2 = 0;
    if (sign_flag) goto loc_005DBCD9;
loc_005DBADD:
    local_rdi = (uint32_t)((0) + (1));
    goto loc_005DBA3A;
loc_005DBAEB:
loc_005DBAEF:
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0xA) = (uint16_t)((uint8_t)(local_r15));
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x492) = (uint16_t)((uint8_t)(local_r15));
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x118 - 0x58) + 0x496) = (uint16_t)((uint8_t)(local_r15));
    result = PpmParkRegisterRestriction(*(uint64_t *)(local_rsp - 0x118 - 0x58), Arg2, Arg3, 0);
    goto loc_005DB779;
loc_005DBB22:
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m1CC)) + (1));
    goto loc_005DB748;
loc_005DBB2A:
    Arg2 = ((uint32_t)(v_stack_m1E0)) << (3);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x704D5050ULL), 0);
    local_r12 = 0;
    v_stack_m1A8 = result;
    if (result == 0) goto loc_005DBCF0;
    if ((uint32_t)((uint32_t)(v_stack_m1E4)) == 0) goto loc_005DBCD2;
loc_005DBB6C:
    *(uint64_t *)(v_stack_m1C0 + 0x488 - 0x30) = result;
    result = (uint32_t)((*(uint16_t *)(v_stack_m1C0 + 0x488 - 0x47E)) + 1);
    Arg3 = ((uint32_t)((uint32_t)(result))) << (3);
    local_rsi = (result) + (Arg3);
    *(uint32_t *)(v_stack_m1C0 + 0x488) = (uint32_t)(result);
    *(uint64_t *)(v_stack_m1C0 + 0x488 - 0x28) = local_rsi;
    local_rsi = (local_rsi) + (Arg3);
    *(uint64_t *)(v_stack_m1C0 + 0x488 - 0x20) = local_rsi;
    local_rsi = (local_rsi) + (Arg3);
    Arg2 = (*(uint64_t *)(v_stack_m1C0 + 0x488 - 0x38)) + (328);
    result = memcpy(result, Arg2, Arg3, 0);
    Arg2 = (*(uint64_t *)(v_stack_m1C0 + 0x488 - 0x38)) + (328);
    Arg3 = ((uint32_t)(*(uint32_t *)(v_stack_m1C0 + 0x488))) << (3);
    result = memcpy(*(uint64_t *)(v_stack_m1C0 + 0x488 - 0x28), Arg2, Arg3, 0);
    *(uint64_t *)(v_stack_m1C0 + 0x488 - 0x18) = *(uint64_t *)(*(uint64_t *)(v_stack_m1C0 + 0x488 - 0x38) + 0x18);
    *(uint64_t *)(v_stack_m1C0 + 0x488 - 0x10) = *(uint64_t *)(*(uint64_t *)(v_stack_m1C0 + 0x488 - 0x38) + 0x18);
    if ((*(uint8_t *)(v_stack_m1C0 + 0x488 + 0x19)) == 0) goto loc_005DBCBD;
    if ((*(uint8_t *)(v_stack_m1C0 + 0x488 - 0x47C)) <= 0) goto loc_005DBCB7;
loc_005DBBF5:
    local_rdi = (0 + 0 * 4) << (7);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_stack_m1C0 + 0x488 + 0x80));
    result = *(uint16_t *)(local_rdi);
    if ((uint16_t)(*(uint16_t *)(local_rdi)) != 0) {
        *(uint64_t *)(local_rdi + 0x240) = local_rsi;
        result = (uint32_t)((*(uint16_t *)(local_rdi)) + 1);
        Arg3 = (uint32_t)(result);
        Arg3 = (Arg3) << (3);
        local_rsi = (local_rsi) + (Arg3);
        *(uint32_t *)(local_rdi + 0x270) = (uint32_t)(result);
        *(uint64_t *)(local_rdi + 0x248) = local_rsi;
        local_rsi = (local_rsi) + (Arg3);
        *(uint64_t *)(local_rdi + 0x250) = local_rsi;
        local_rsi = (local_rsi) + (Arg3);
        Arg2 = *(uint64_t *)(local_rdi + 0x238);
        Arg2 = (Arg2) + (328);
        result = memcpy(local_rsi, Arg2, Arg3, 0);
        Arg3 = *(uint32_t *)(local_rdi + 0x270);
        Arg2 = *(uint64_t *)(local_rdi + 0x238);
        Arg1 = *(uint64_t *)(local_rdi + 0x248);
        Arg2 = (Arg2) + (328);
        Arg3 = (Arg3) << (3);
        result = memcpy(Arg1, Arg2, Arg3, 0);
        result = *(uint64_t *)(local_rdi + 0x238);
        Arg1 = *(uint64_t *)(result + 0x18);
        *(uint64_t *)(local_rdi + 0x258) = Arg1;
        result = *(uint64_t *)(local_rdi + 0x238);
        Arg1 = *(uint64_t *)(result + 0x18);
        *(uint64_t *)(local_rdi + 0x260) = Arg1;
    }
    local_r14 = (uint32_t)((0) + (1));
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint8_t *)(v_stack_m1C0 + 0x488 - 0x47C)))) goto loc_005DBBF5;
    goto loc_005DBCBD;
loc_005DBCB7:
loc_005DBCBD:
    local_rbx = (v_stack_m1C0 + 1160) + (0x510ULL);
    local_r15 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m1E4)))) - (1);
    if (condition_is_not_equal) goto loc_005DBB6C;
loc_005DBCD2:
    goto loc_005DBCF8;
loc_005DBCD9:
loc_005DBCDC:
    local_r12 = 0;
    goto loc_005DBCF8;
loc_005DBCEB:
    goto loc_005DBCDC;
loc_005DBCF0:
    goto loc_005DBCD2;
loc_005DBCF5:
loc_005DBCF8:
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 9637665, Arg2, Arg3, 0);
    Arg1 = (uint8_t)(-(0));
    local_r10 = (local_r10) & (v_stack_m1C0);
    *(uint64_t *)(v_rip + 0x92C6B4) = local_r10;
    local_rbx = 0;
    if (0 == 0) { local_rbx = v_stack_m1A8; }
    Arg1 = (uint8_t)(-(0));
    Arg3 = (uint32_t)((Arg3) & ((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    *(uint32_t *)(v_rip + 0x92C6A0) = (uint32_t)(Arg3);
    result = (uint8_t)(-(0));
    Arg3 = (Arg3) & (v_stack_m1A8);
    *(uint64_t *)(v_rip + 0x92C657) = Arg3;
    result = KeReleaseSpinLock(v_rip + 9637613, (uint8_t)(result), Arg3, 0);
    v_stack_m1F8 = 0;
    result = PpmParkFreeAllParkNodes(v_stack_m1B0, (uint32_t)(v_stack_m1D4), v_stack_m1C0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    if (local_rbx != 0) {
        Arg2 = 0x704D5050ULL;
        Arg1 = local_rbx;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m1C0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    }
    result = v_stack_m1A0;
    if (v_stack_m1A0 != 0) {
        Arg2 = 0x704D5050ULL;
        Arg1 = v_stack_m1A0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m1C0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    }
    result = PpmParkApplyPolicy(Arg1, Arg2, v_stack_m1C0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    result = PpmParkParkingAvailable(Arg1, Arg2, v_stack_m1C0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    goto loc_005DBDA9;
loc_005DBDA4:
    result = PpmParkRegisterParkingEx(Arg1, Arg2, v_stack_m1C0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
loc_005DBDA9:
    Arg1 = (*(uint64_t *)(local_rsp - 0x118 + 0xE0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m1C0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DB508&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
