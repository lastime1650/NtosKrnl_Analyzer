# EtwpTraceStackKey

- RVA: `0x003FC290`–`0x003FC8AD` (길이 `1,565` bytes)
- VA: `0x00000001403FC290`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00099880`
- 디코드: `377`개 명령, `1,565/1,565` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x003FC38E` → [KiAcquireSpinLockInstrumented](../20/KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x003FC3F0` → [RtlCompareMemory](../6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x003FC452` → [KxWaitForSpinLockAndAcquire](../20/KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x003FC467` → [EtwpDereferenceStackEntry](EtwpDereferenceStackEntry_function_003FC9D0.md) (function, `0x003FC9D0`)
- `0x003FC48B` → [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x003FC4AB` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x003FC4C7` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003FC4F6` → [KxTryToAcquireSpinLock](../46/KxTryToAcquireSpinLock_function_0046BE18.md) (function, `0x0046BE18`)
- `0x003FC508` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003FC563` → [ExpInterlockedPopEntrySList](../6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x003FC59A` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003FC607` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x003FC621` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003FC6EE` → [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x003FC70B` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x003FC73F` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x003FC7B1` → [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x003FC85D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003FC87A` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x003FC89B` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)

### Direct callers
- [sub_002F90AE](../2F/Unknown_function_002F90AE.md) at `0x002F9246`

### Static image references
- `0x003FC2A4` → RVA `0x00E0A740` (`.data`; read)
- `0x003FC362` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003FC36E` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x003FC380` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003FC290  40 53                           push rbx
003FC292  55                              push rbp
003FC293  56                              push rsi
003FC294  57                              push rdi
003FC295  41 54                           push r12
003FC297  41 55                           push r13
003FC299  41 56                           push r14
003FC29B  41 57                           push r15
003FC29D  48 81 EC B8 01 00 00            sub rsp, 0x1b8
003FC2A4  48 8B 05 95 E4 A0 00            mov rax, qword ptr [rip + 0xa0e495]
003FC2AB  48 33 C4                        xor rax, rsp
003FC2AE  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
003FC2B6  4C 8B 99 20 04 00 00            mov r11, qword ptr [rcx + 0x420]
003FC2BD  48 8B B4 24 20 02 00 00         mov rsi, qword ptr [rsp + 0x220]
003FC2C5  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
003FC2CA  66 44 89 44 24 34               mov word ptr [rsp + 0x34], r8w
003FC2D0  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
003FC2D4  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
003FC2D9  48 C7 44 24 60 00 00 00 00      mov qword ptr [rsp + 0x60], 0
003FC2E2  4C 89 5C 24 48                  mov qword ptr [rsp + 0x48], r11
003FC2E7  4D 85 DB                        test r11, r11
003FC2EA  0F 84 7C 01 00 00               je 0x1403fc46c
003FC2F0  44 8B AC 24 28 02 00 00         mov r13d, dword ptr [rsp + 0x228]
003FC2F8  45 33 FF                        xor r15d, r15d
003FC2FB  45 8B D5                        mov r10d, r13d
003FC2FE  33 FF                           xor edi, edi
003FC300  49 C1 E2 02                     shl r10, 2
003FC304  45 33 C0                        xor r8d, r8d
003FC307  4D 85 D2                        test r10, r10
003FC30A  74 23                           je 0x1403fc32f
003FC30C  45 33 C9                        xor r9d, r9d
003FC30F  90                              nop
003FC310  41 8D 40 01                     lea eax, [r8 + 1]
003FC314  41 83 C0 02                     add r8d, 2
003FC318  0F B7 14 46                     movzx edx, word ptr [rsi + rax*2]
003FC31C  42 0F B7 04 4E                  movzx eax, word ptr [rsi + r9*2]
003FC321  48 33 D0                        xor rdx, rax
003FC324  45 8B C8                        mov r9d, r8d
003FC327  48 03 FA                        add rdi, rdx
003FC32A  4D 3B CA                        cmp r9, r10
003FC32D  72 E1                           jb 0x1403fc310
003FC32F  33 D2                           xor edx, edx
003FC331  8B C7                           mov eax, edi
003FC333  41 F7 73 08                     div dword ptr [r11 + 8]
003FC337  33 ED                           xor ebp, ebp
003FC339  48 8D 42 02                     lea rax, [rdx + 2]
003FC33D  48 8D 04 42                     lea rax, [rdx + rax*2]
003FC341  4D 8D 24 C3                     lea r12, [r11 + rax*8]
003FC345  44 0F 20 C3                     mov rbx, cr8
003FC349  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
003FC34E  8D 45 02                        lea eax, [rbp + 2]
003FC351  80 FB 01                        cmp bl, 1
003FC354  0F 85 87 01 00 00               jne 0x1403fc4e1
003FC35A  44 0F 20 C1                     mov rcx, cr8
003FC35E  44 0F 22 C0                     mov cr8, rax
003FC362  39 2D B8 A9 BC 00               cmp dword ptr [rip + 0xbca9b8], ebp
003FC368  0F 85 97 01 00 00               jne 0x1403fc505
003FC36E  F6 05 91 A7 BC 00 21            test byte ptr [rip + 0xbca791], 0x21
003FC375  49 8D 4C 24 10                  lea rcx, [r12 + 0x10]
003FC37A  0F 84 C6 00 00 00               je 0x1403fc446
003FC380  8B 05 D2 1A B1 00               mov eax, dword ptr [rip + 0xb11ad2]
003FC386  85 C0                           test eax, eax
003FC388  0F 85 B8 00 00 00               jne 0x1403fc446
003FC38E  E8 5D C1 E0 FF                  call 0x1402084f0
003FC393  4D 8B 34 24                     mov r14, qword ptr [r12]
003FC397  41 B8 20 00 00 00               mov r8d, 0x20
003FC39D  0F 1F 00                        nop dword ptr [rax]
003FC3A0  4D 3B F4                        cmp r14, r12
003FC3A3  0F 84 69 01 00 00               je 0x1403fc512
003FC3A9  FF C5                           inc ebp
003FC3AB  41 39 7E 1C                     cmp dword ptr [r14 + 0x1c], edi
003FC3AF  75 06                           jne 0x1403fc3b7
003FC3B1  45 39 6E 20                     cmp dword ptr [r14 + 0x20], r13d
003FC3B5  74 05                           je 0x1403fc3bc
003FC3B7  4D 8B 36                        mov r14, qword ptr [r14]
003FC3BA  EB E4                           jmp 0x1403fc3a0
003FC3BC  33 D2                           xor edx, edx
003FC3BE  49 8B CE                        mov rcx, r14
003FC3C1  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
003FC3C6  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
003FC3CA  48 85 C9                        test rcx, rcx
003FC3CD  74 44                           je 0x1403fc413
003FC3CF  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
003FC3D2  48 8D 14 D6                     lea rdx, [rsi + rdx*8]
003FC3D6  83 F8 20                        cmp eax, 0x20
003FC3D9  44 0F 42 C0                     cmovb r8d, eax
003FC3DD  48 83 C1 28                     add rcx, 0x28
003FC3E1  41 8B D8                        mov ebx, r8d
003FC3E4  44 89 44 24 58                  mov dword ptr [rsp + 0x58], r8d
003FC3E9  48 C1 E3 03                     shl rbx, 3
003FC3ED  4C 8B C3                        mov r8, rbx
003FC3F0  E8 7B E2 2B 00                  call 0x1406ba670
003FC3F5  41 B8 20 00 00 00               mov r8d, 0x20
003FC3FB  48 3B C3                        cmp rax, rbx
003FC3FE  75 B7                           jne 0x1403fc3b7
003FC400  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003FC405  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
003FC409  03 54 24 58                     add edx, dword ptr [rsp + 0x58]
003FC40D  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
003FC411  EB AE                           jmp 0x1403fc3c1
003FC413  F0 41 FF 46 18                  lock inc dword ptr [r14 + 0x18]
003FC418  49 8B 06                        mov rax, qword ptr [r14]
003FC41B  4C 39 70 08                     cmp qword ptr [rax + 8], r14
003FC41F  75 1E                           jne 0x1403fc43f
003FC421  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
003FC425  4C 39 31                        cmp qword ptr [rcx], r14
003FC428  75 15                           jne 0x1403fc43f
003FC42A  48 89 01                        mov qword ptr [rcx], rax
003FC42D  48 89 48 08                     mov qword ptr [rax + 8], rcx
003FC431  49 8B 04 24                     mov rax, qword ptr [r12]
003FC435  4C 39 60 08                     cmp qword ptr [rax + 8], r12
003FC439  0F 84 EC 02 00 00               je 0x1403fc72b
003FC43F  B9 03 00 00 00                  mov ecx, 3
003FC444  CD 29                           int 0x29
003FC446  F0 48 0F BA 29 00               lock bts qword ptr [rcx], 0
003FC44C  0F 83 41 FF FF FF               jae 0x1403fc393
003FC452  E8 69 C1 E0 FF                  call 0x1402085c0
003FC457  E9 37 FF FF FF                  jmp 0x1403fc393
003FC45C  4D 85 FF                        test r15, r15
003FC45F  74 0B                           je 0x1403fc46c
003FC461  48 8B D6                        mov rdx, rsi
003FC464  49 8B CF                        mov rcx, r15
003FC467  E8 64 05 00 00                  call 0x1403fc9d0
003FC46C  45 32 FF                        xor r15b, r15b
003FC46F  EB 47                           jmp 0x1403fc4b8
003FC471  44 0F B7 CE                     movzx r9d, si
003FC475  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
003FC47D  C7 44 24 28 02 06 50 00         mov dword ptr [rsp + 0x28], 0x500602
003FC485  66 44 89 64 24 20               mov word ptr [rsp + 0x20], r12w
003FC48B  E8 70 07 E6 FF                  call 0x14025cc00
003FC490  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
003FC495  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
003FC4A0  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
003FC4A4  48 8D 4E 10                     lea rcx, [rsi + 0x10]
003FC4A8  48 8B D3                        mov rdx, rbx
003FC4AB  E8 00 E1 2B 00                  call 0x1406ba5b0
003FC4B0  48 8B DF                        mov rbx, rdi
003FC4B3  48 85 FF                        test rdi, rdi
003FC4B6  75 E8                           jne 0x1403fc4a0
003FC4B8  41 0F B6 C7                     movzx eax, r15b
003FC4BC  48 8B 8C 24 A0 01 00 00         mov rcx, qword ptr [rsp + 0x1a0]
003FC4C4  48 33 CC                        xor rcx, rsp
003FC4C7  E8 74 01 2B 00                  call 0x1406ac640
003FC4CC  48 81 C4 B8 01 00 00            add rsp, 0x1b8
003FC4D3  41 5F                           pop r15
003FC4D5  41 5E                           pop r14
003FC4D7  41 5D                           pop r13
003FC4D9  41 5C                           pop r12
003FC4DB  5F                              pop rdi
003FC4DC  5E                              pop rsi
003FC4DD  5D                              pop rbp
003FC4DE  5B                              pop rbx
003FC4DF  C3                              ret
003FC4E0  CC                              int3
003FC4E1  84 DB                           test bl, bl
003FC4E3  0F 84 71 FE FF FF               je 0x1403fc35a
003FC4E9  3A D8                           cmp bl, al
003FC4EB  0F 84 7D FE FF FF               je 0x1403fc36e
003FC4F1  49 8D 4C 24 10                  lea rcx, [r12 + 0x10]
003FC4F6  E8 1D F9 06 00                  call 0x14046be18
003FC4FB  84 C0                           test al, al
003FC4FD  0F 85 90 FE FF FF               jne 0x1403fc393
003FC503  EB B3                           jmp 0x1403fc4b8
003FC505  0F B6 D0                        movzx edx, al
003FC508  E8 EF 91 0F 00                  call 0x1404f56fc
003FC50D  E9 5C FE FF FF                  jmp 0x1403fc36e
003FC512  83 FD 04                        cmp ebp, 4
003FC515  75 23                           jne 0x1403fc53a
003FC517  4D 8B 7C 24 08                  mov r15, qword ptr [r12 + 8]
003FC51C  4D 39 27                        cmp qword ptr [r15], r12
003FC51F  0F 85 1A FF FF FF               jne 0x1403fc43f
003FC525  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
003FC529  4C 39 38                        cmp qword ptr [rax], r15
003FC52C  0F 85 0D FF FF FF               jne 0x1403fc43f
003FC532  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
003FC537  4C 89 20                        mov qword ptr [rax], r12
003FC53A  45 33 F6                        xor r14d, r14d
003FC53D  33 ED                           xor ebp, ebp
003FC53F  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
003FC544  45 85 ED                        test r13d, r13d
003FC547  0F 84 88 00 00 00               je 0x1403fc5d5
003FC54D  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
003FC552  48 83 C0 10                     add rax, 0x10
003FC556  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003FC55B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
003FC560  48 8B C8                        mov rcx, rax
003FC563  E8 08 E0 2B 00                  call 0x1406ba570
003FC568  48 8B D8                        mov rbx, rax
003FC56B  48 85 C0                        test rax, rax
003FC56E  0F 84 F3 02 00 00               je 0x1403fc867
003FC574  8D 4D 20                        lea ecx, [rbp + 0x20]
003FC577  41 8B C5                        mov eax, r13d
003FC57A  2B C5                           sub eax, ebp
003FC57C  48 8D 14 EE                     lea rdx, [rsi + rbp*8]
003FC580  41 3B CD                        cmp ecx, r13d
003FC583  B9 20 00 00 00                  mov ecx, 0x20
003FC588  0F 42 C1                        cmovb eax, ecx
003FC58B  48 8D 4B 28                     lea rcx, [rbx + 0x28]
003FC58F  44 8B C0                        mov r8d, eax
003FC592  49 C1 E0 03                     shl r8, 3
003FC596  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
003FC59A  E8 A1 A2 2C 00                  call 0x1406c6840
003FC59F  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
003FC5A3  85 ED                           test ebp, ebp
003FC5A5  0F 85 6F 01 00 00               jne 0x1403fc71a
003FC5AB  4C 8B F3                        mov r14, rbx
003FC5AE  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003FC5B3  48 85 C9                        test rcx, rcx
003FC5B6  0F 85 66 01 00 00               jne 0x1403fc722
003FC5BC  03 E8                           add ebp, eax
003FC5BE  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
003FC5C3  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
003FC5C8  48 C7 43 10 00 00 00 00         mov qword ptr [rbx + 0x10], 0
003FC5D0  41 3B ED                        cmp ebp, r13d
003FC5D3  72 8B                           jb 0x1403fc560
003FC5D5  41 89 7E 1C                     mov dword ptr [r14 + 0x1c], edi
003FC5D9  45 89 6E 20                     mov dword ptr [r14 + 0x20], r13d
003FC5DD  41 C7 46 18 02 00 00 00         mov dword ptr [r14 + 0x18], 2
003FC5E5  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
003FC5EA  4C 39 20                        cmp qword ptr [rax], r12
003FC5ED  0F 85 4C FE FF FF               jne 0x1403fc43f
003FC5F3  4D 89 26                        mov qword ptr [r14], r12
003FC5F6  49 8D 4C 24 10                  lea rcx, [r12 + 0x10]
003FC5FB  49 89 46 08                     mov qword ptr [r14 + 8], rax
003FC5FF  4C 89 30                        mov qword ptr [rax], r14
003FC602  4D 89 74 24 08                  mov qword ptr [r12 + 8], r14
003FC607  E8 64 A0 E0 FF                  call 0x140206670
003FC60C  83 3D 0D A7 BC 00 00            cmp dword ptr [rip + 0xbca70d], 0
003FC613  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
003FC618  74 0C                           je 0x1403fc626
003FC61A  44 0F 20 C1                     mov rcx, cr8
003FC61E  0F B6 D3                        movzx edx, bl
003FC621  E8 72 90 0F 00                  call 0x1404f5698
003FC626  0F B6 C3                        movzx eax, bl
003FC629  44 0F 22 C0                     mov cr8, rax
003FC62D  BE 01 00 00 00                  mov esi, 1
003FC632  41 BC 23 18 00 00               mov r12d, 0x1823
003FC638  8D 6E FE                        lea ebp, [rsi - 2]
003FC63B  4D 85 FF                        test r15, r15
003FC63E  0F 84 27 01 00 00               je 0x1403fc76b
003FC644  8B C5                           mov eax, ebp
003FC646  F0 41 0F C1 47 18               lock xadd dword ptr [r15 + 0x18], eax
003FC64C  3B C6                           cmp eax, esi
003FC64E  0F 85 17 01 00 00               jne 0x1403fc76b
003FC654  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
003FC659  33 FF                           xor edi, edi
003FC65B  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
003FC660  44 0F B7 DE                     movzx r11d, si
003FC664  48 C7 84 24 88 00 00 00 08 00 00 00  mov qword ptr [rsp + 0x88], 8
003FC670  4D 8B D7                        mov r10, r15
003FC673  48 8B 03                        mov rax, qword ptr [rbx]
003FC676  BB 20 00 00 00                  mov ebx, 0x20
003FC67B  44 8B 00                        mov r8d, dword ptr [rax]
003FC67E  48 8B 90 50 05 00 00            mov rdx, qword ptr [rax + 0x550]
003FC685  48 8D 44 24 38                  lea rax, [rsp + 0x38]
003FC68A  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
003FC692  41 8B 42 20                     mov eax, dword ptr [r10 + 0x20]
003FC696  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
003FC69E  3B C3                           cmp eax, ebx
003FC6A0  44 8B CB                        mov r9d, ebx
003FC6A3  44 0F 42 C8                     cmovb r9d, eax
003FC6A7  41 0F B7 C3                     movzx eax, r11w
003FC6AB  48 C1 E0 04                     shl rax, 4
003FC6AF  66 41 FF C3                     inc r11w
003FC6B3  48 03 C8                        add rcx, rax
003FC6B6  49 8D 42 28                     lea rax, [r10 + 0x28]
003FC6BA  48 89 01                        mov qword ptr [rcx], rax
003FC6BD  42 8D 04 CD 00 00 00 00         lea eax, [r9*8]
003FC6C5  89 41 08                        mov dword ptr [rcx + 8], eax
003FC6C8  89 79 0C                        mov dword ptr [rcx + 0xc], edi
003FC6CB  4D 8B 52 10                     mov r10, qword ptr [r10 + 0x10]
003FC6CF  4D 85 D2                        test r10, r10
003FC6D2  75 BE                           jne 0x1403fc692
003FC6D4  45 0F B7 CB                     movzx r9d, r11w
003FC6D8  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
003FC6E0  C7 44 24 28 02 06 50 00         mov dword ptr [rsp + 0x28], 0x500602
003FC6E8  66 44 89 64 24 20               mov word ptr [rsp + 0x20], r12w
003FC6EE  E8 0D 05 E6 FF                  call 0x14025cc00
003FC6F3  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
003FC6F8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
003FC700  49 8B 5F 10                     mov rbx, qword ptr [r15 + 0x10]
003FC704  48 8D 4F 10                     lea rcx, [rdi + 0x10]
003FC708  49 8B D7                        mov rdx, r15
003FC70B  E8 A0 DE 2B 00                  call 0x1406ba5b0
003FC710  4C 8B FB                        mov r15, rbx
003FC713  48 85 DB                        test rbx, rbx
003FC716  75 E8                           jne 0x1403fc700
003FC718  EB 51                           jmp 0x1403fc76b
003FC71A  89 43 20                        mov dword ptr [rbx + 0x20], eax
003FC71D  E9 8C FE FF FF                  jmp 0x1403fc5ae
003FC722  48 89 59 10                     mov qword ptr [rcx + 0x10], rbx
003FC726  E9 91 FE FF FF                  jmp 0x1403fc5bc
003FC72B  49 89 06                        mov qword ptr [r14], rax
003FC72E  49 8D 4C 24 10                  lea rcx, [r12 + 0x10]
003FC733  4D 89 66 08                     mov qword ptr [r14 + 8], r12
003FC737  4C 89 70 08                     mov qword ptr [rax + 8], r14
003FC73B  4D 89 34 24                     mov qword ptr [r12], r14
003FC73F  E8 2C 9F E0 FF                  call 0x140206670
003FC744  44 39 3D D5 A5 BC 00            cmp dword ptr [rip + 0xbca5d5], r15d
003FC74B  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
003FC750  0F 85 00 01 00 00               jne 0x1403fc856
003FC756  0F B6 C3                        movzx eax, bl
003FC759  44 0F 22 C0                     mov cr8, rax
003FC75D  BD FF FF FF FF                  mov ebp, 0xffffffff
003FC762  41 BC 23 18 00 00               mov r12d, 0x1823
003FC768  8D 75 02                        lea esi, [rbp + 2]
003FC76B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
003FC770  48 8D 44 24 60                  lea rax, [rsp + 0x60]
003FC775  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
003FC77A  41 B7 01                        mov r15b, 1
003FC77D  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
003FC782  45 33 F6                        xor r14d, r14d
003FC785  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
003FC789  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
003FC78D  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003FC791  45 8D 4E 02                     lea r9d, [r14 + 2]
003FC795  0F B7 44 24 34                  movzx eax, word ptr [rsp + 0x34]
003FC79A  48 C7 41 18 08 00 00 00         mov qword ptr [rcx + 0x18], 8
003FC7A2  44 8B 07                        mov r8d, dword ptr [rdi]
003FC7A5  48 8B 97 50 05 00 00            mov rdx, qword ptr [rdi + 0x550]
003FC7AC  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
003FC7B1  E8 4A 04 E6 FF                  call 0x14025cc00
003FC7B6  48 8B BF 20 04 00 00            mov rdi, qword ptr [rdi + 0x420]
003FC7BD  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
003FC7C2  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
003FC7C7  F0 0F C1 6B 18                  lock xadd dword ptr [rbx + 0x18], ebp
003FC7CC  83 FD 01                        cmp ebp, 1
003FC7CF  0F 85 E3 FC FF FF               jne 0x1403fc4b8
003FC7D5  48 8B 07                        mov rax, qword ptr [rdi]
003FC7D8  4C 8B D3                        mov r10, rbx
003FC7DB  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
003FC7E0  BF 20 00 00 00                  mov edi, 0x20
003FC7E5  48 C7 84 24 18 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x118], 8
003FC7F1  44 8B 00                        mov r8d, dword ptr [rax]
003FC7F4  48 8B 90 50 05 00 00            mov rdx, qword ptr [rax + 0x550]
003FC7FB  48 8D 44 24 70                  lea rax, [rsp + 0x70]
003FC800  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
003FC808  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
003FC810  41 8B 42 20                     mov eax, dword ptr [r10 + 0x20]
003FC814  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
003FC81C  3B C7                           cmp eax, edi
003FC81E  44 8B CF                        mov r9d, edi
003FC821  44 0F 42 C8                     cmovb r9d, eax
003FC825  0F B7 C6                        movzx eax, si
003FC828  48 C1 E0 04                     shl rax, 4
003FC82C  66 FF C6                        inc si
003FC82F  48 03 C8                        add rcx, rax
003FC832  49 8D 42 28                     lea rax, [r10 + 0x28]
003FC836  48 89 01                        mov qword ptr [rcx], rax
003FC839  42 8D 04 CD 00 00 00 00         lea eax, [r9*8]
003FC841  89 41 08                        mov dword ptr [rcx + 8], eax
003FC844  44 89 71 0C                     mov dword ptr [rcx + 0xc], r14d
003FC848  4D 8B 52 10                     mov r10, qword ptr [r10 + 0x10]
003FC84C  4D 85 D2                        test r10, r10
003FC84F  75 BF                           jne 0x1403fc810
003FC851  E9 1B FC FF FF                  jmp 0x1403fc471
003FC856  44 0F 20 C1                     mov rcx, cr8
003FC85A  0F B6 D3                        movzx edx, bl
003FC85D  E8 36 8E 0F 00                  call 0x1404f5698
003FC862  E9 EF FE FF FF                  jmp 0x1403fc756
003FC867  41 3B ED                        cmp ebp, r13d
003FC86A  0F 83 65 FD FF FF               jae 0x1403fc5d5
003FC870  0F B6 54 24 38                  movzx edx, byte ptr [rsp + 0x38]
003FC875  49 8D 4C 24 10                  lea rcx, [r12 + 0x10]
003FC87A  E8 21 63 F9 FF                  call 0x140392ba0
003FC87F  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
003FC884  4D 85 F6                        test r14, r14
003FC887  0F 84 CF FB FF FF               je 0x1403fc45c
003FC88D  0F 1F 00                        nop dword ptr [rax]
003FC890  49 8B 5E 10                     mov rbx, qword ptr [r14 + 0x10]
003FC894  48 8D 4E 10                     lea rcx, [rsi + 0x10]
003FC898  49 8B D6                        mov rdx, r14
003FC89B  E8 10 DD 2B 00                  call 0x1406ba5b0
003FC8A0  4C 8B F3                        mov r14, rbx
003FC8A3  48 85 DB                        test rbx, rbx
003FC8A6  75 E8                           jne 0x1403fc890
003FC8A8  E9 AF FB FF FF                  jmp 0x1403fc45c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpTraceStackKey(__int64 a1, int a2, int a3, __int64 a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int16 v_stack_m1C4;
    unsigned int v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned __int16 v_stack_m1D8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int16 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int16 v_stack_p34;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;

    v_rsp = (v_rsp) - (440);
    result = (*(unsigned __int64 *)(v_rip + 10544277)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m190 = a4;
    v_stack_m1C4 = (unsigned __int16)(a3);
    v_stack_m1B8 = a2;
    v_stack_m188 = a1;
    v_stack_m198 = 0;
    v_stack_m1B0 = *(unsigned __int64 *)(a1 + 1056);
    if (*(unsigned __int64 *)(a1 + 1056) == 0) goto loc_003FC46C;
    v_r15 = 0;
    v_rdi = 0;
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(a6)))) << (2);
    a3 = 0;
    if (v_r10 == 0) goto loc_003FC32F;
    a4 = 0;
loc_003FC310:
    a3 = (unsigned int)((a3) + (2));
    a2 = (*(unsigned __int16 *)(a5 + a3 + 1 * 2)) ^ (*(unsigned __int16 *)(a5 + a4 * 2));
    v_rdi = (v_rdi) + (a2);
    if (((unsigned int)(a3)) < v_r10) goto loc_003FC310;
loc_003FC32F:
    a2 = 0;
    v_rbp = 0;
    v_stack_m1C0 = v_cr8;
    if (((unsigned __int8)(v_cr8)) != 1) goto loc_003FC4E1;
loc_003FC35A:
    if ((*(unsigned int *)(v_rip + 12364216)) != 0) goto loc_003FC505;
loc_003FC36E:
    if (((*(unsigned __int8 *)(v_rip + 12363665)) & (33)) == 0) goto loc_003FC446;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11606738))) != 0) goto loc_003FC446;
    result = KiAcquireSpinLockInstrumented(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 16, a2, a3, (unsigned int)(a3));
loc_003FC393:
loc_003FC3A0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) == (*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) goto loc_003FC512;
    v_rbp = (unsigned int)((v_rbp) + 1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8) + 28)) != ((unsigned int)(v_rdi))) goto loc_003FC3B7;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8) + 32)) == ((unsigned int)((unsigned int)(a6)))) goto loc_003FC3BC;
loc_003FC3B7:
    goto loc_003FC3A0;
loc_003FC3BC:
    a2 = 0;
loc_003FC3C1:
    v_stack_m1A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8));
    v_stack_m1C8 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) == 0) goto loc_003FC413;
    a3 = 32;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) + 32)))) < 32) { a3 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) + 32))); }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8))) + (40);
    v_stack_m1A0 = a3;
    v_rbx = ((unsigned int)(a3)) << (3);
    result = RtlCompareMemory(a1, a5 + a2 * 8, v_rbx, (unsigned int)(a3));
    if (result != v_rbx) goto loc_003FC3B7;
    a2 = (unsigned int)(((unsigned int)(v_stack_m1C8)) + (v_stack_m1A0));
    goto loc_003FC3C1;
loc_003FC413:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8))) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)))) goto loc_003FC43F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)))) goto loc_003FC43F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8))) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8) + 8)) == (*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) goto loc_003FC72B;
loc_003FC43F:
loc_003FC446:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8) + 8)) >= (*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) goto loc_003FC393;
    result = KxWaitForSpinLockAndAcquire(3, a2, 32, (unsigned int)(a3));
    goto loc_003FC393;
loc_003FC45C:
    if (0 != 0) {
        a2 = a5;
        a1 = 0;
        result = EtwpDereferenceStackEntry(a1, a2, 32, (unsigned int)(a3));
    }
    v_r15 = 0;
    goto loc_003FC4B8;
loc_003FC471:
    v_stack_m1D0 = 0x500602ULL;
    v_stack_m1D8 = (unsigned __int16)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8);
    result = EtwpLogKernelEvent(v_stack_mE8, a2, 32, (unsigned __int16)(a5));
loc_003FC4A0:
    result = ExpInterlockedPushEntrySList(v_stack_m190 + 16, v_rbx, 32, (unsigned __int16)(a5));
    if (*(unsigned __int64 *)(v_rbx + 16) != 0) goto loc_003FC4A0;
loc_003FC4B8:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rbx, 32, (unsigned __int16)(a5));
    v_rsp = (v_rsp) + (440);
    return result;
loc_003FC4E1:
    if ((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 16)) == 0) goto loc_003FC35A;
    if (((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 16))) == ((unsigned __int8)(result))) goto loc_003FC36E;
    result = KxTryToAcquireSpinLock(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 16, v_rbx, 32, (unsigned __int16)(a5));
    if ((unsigned __int8)(result) != 0) goto loc_003FC393;
    goto loc_003FC4B8;
loc_003FC505:
    result = KiRaiseIrqlProcessIrqlFlags(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 16, (unsigned __int8)(result), 32, (unsigned __int16)(a5));
    goto loc_003FC36E;
loc_003FC512:
    if (((unsigned int)(v_rbp)) != 4) goto loc_003FC53A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8))) != (*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) goto loc_003FC43F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8))) goto loc_003FC43F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 8)) = *(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8;
loc_003FC53A:
    v_r14 = 0;
    v_rbp = 0;
    v_stack_p50 = 0;
    if ((unsigned int)((unsigned int)(a6)) == 0) goto loc_003FC5D5;
    result = (v_stack_p48) + (16);
    v_stack_p58 = result;
loc_003FC560:
    result = ExpInterlockedPopEntrySList(result, (unsigned __int8)(result), 32, (unsigned __int16)(a5));
    if (result == 0) goto loc_003FC867;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) - (0));
    if (((unsigned int)(v_rbp + 32)) < ((unsigned int)((unsigned int)(a6)))) { result = 32; }
    a3 = ((unsigned int)((unsigned int)(result))) << (3);
    v_stack_p30 = (unsigned int)(result);
    result = memcpy(result + 40, v_stack_m190 + v_rbp * 8, a3, (unsigned __int16)(a5));
    if (0 != 0) goto loc_003FC71A;
loc_003FC5AE:
    if (v_stack_p50 != 0) goto loc_003FC722;
loc_003FC5BC:
    v_rbp = (unsigned int)((v_rbp) + ((unsigned int)((unsigned int)(v_stack_p30))));
    v_stack_p50 = result;
    *(unsigned __int64 *)(result + 16) = 0;
    if (((unsigned int)(v_rbp)) < ((unsigned int)((unsigned int)(a6)))) goto loc_003FC560;
loc_003FC5D5:
    *(unsigned int *)(result + 28) = (unsigned int)(*(unsigned __int64 *)(v_rbx + 16));
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(a6));
    *(unsigned int *)(result + 24) = 2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8))) != (*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8)) goto loc_003FC43F;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8)) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) = result;
    result = KxReleaseSpinLock(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 16, v_stack_m190 + v_rbp * 8, a3, (unsigned __int16)(a5));
    if ((*(unsigned int *)(v_rip + 12363533)) != 0) {
        a1 = v_rbp + 2;
        a2 = (unsigned __int8)(v_stack_p38);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, (unsigned __int16)(a5));
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) == 0) goto loc_003FC76B;
    if (((unsigned int)((unsigned int)((unsigned int)(1 - 2)))) != 1) goto loc_003FC76B;
    v_rdi = 0;
    v_stack_p38 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8);
    v_stack_p88 = 8;
    v_stack_p80 = v_stack_p38;
loc_003FC692:
    a4 = 32;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 32)))) < 32) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 32))); }
    result = (1) << (4);
    v_r11 = (unsigned __int16)((1) + 1);
    a1 = (v_stack_p80) + (result);
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 40;
    *(unsigned int *)(a1 + 8) = (unsigned int)(a4 * 8);
    *(unsigned int *)(a1 + 12) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 16) != 0) goto loc_003FC692;
    v_stack_p28 = 0x500602ULL;
    v_stack_p20 = (unsigned __int16)((unsigned int)(0x1823ULL));
    result = EtwpLogKernelEvent(v_stack_p80, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p48) + 1360), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p48))), (unsigned __int16)(v_r11));
loc_003FC700:
    result = ExpInterlockedPushEntrySList(v_stack_p48 + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p48))), (unsigned __int16)(v_r11));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 16) != 0) goto loc_003FC700;
    goto loc_003FC76B;
loc_003FC71A:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 16) + 32) = (unsigned int)(result);
    goto loc_003FC5AE;
loc_003FC722:
    *(unsigned __int64 *)(v_stack_p48 + 16 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 16);
    goto loc_003FC5BC;
loc_003FC72B:
    *(unsigned __int64 *)(result) = result;
    *(unsigned __int64 *)(result + 8) = (unsigned int)(0x1823ULL);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)((unsigned int)(0x1823ULL)) = result;
    result = KxReleaseSpinLock((unsigned int)(0x1823ULL) + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p48))), (unsigned __int16)(v_r11));
    if ((*(unsigned int *)(v_rip + 12363221)) != ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1056) + a2 + a2 + 2 * 2 * 8 + 8) + 16)))) goto loc_003FC856;
loc_003FC756:
loc_003FC76B:
    v_stack_p60 = result;
    v_r14 = 0;
    *(unsigned __int64 *)(v_stack_p68 + 16) = v_stack_p60;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p40));
    *(unsigned __int64 *)(v_stack_p68 + 24) = 8;
    v_stack_p20 = (unsigned __int16)(v_stack_p34);
    result = EtwpLogKernelEvent(v_stack_p68, *(unsigned __int64 *)(v_stack_p70 + 1360), (unsigned int)(*(unsigned int *)(v_stack_p70)), v_r14 + 2);
    v_stack_p68 = *(unsigned __int64 *)(v_stack_p70 + 1056);
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) != 1) goto loc_003FC4B8;
    v_stack_p70 = v_stack_p60;
    v_stack_p118 = 8;
    v_stack_p110 = v_stack_p70;
loc_003FC810:
    a4 = 32;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60 + 32)))) < 32) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60 + 32))); }
    result = ((unsigned __int16)((unsigned int)(0xFFFFFFFFULL) + 2)) << (4);
    v_rsi = (unsigned __int16)(((unsigned int)(0xFFFFFFFFULL) + 2) + 1);
    a1 = (v_stack_p110) + (result);
    *(unsigned __int64 *)(a1) = v_stack_p60 + 40;
    *(unsigned int *)(a1 + 8) = (unsigned int)(a4 * 8);
    *(unsigned int *)(a1 + 12) = 0;
    if (*(unsigned __int64 *)(v_stack_p60 + 16) != 0) goto loc_003FC810;
    goto loc_003FC471;
loc_003FC856:
    result = KiLowerIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p38), (unsigned __int8)(v_stack_p60), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p70 + 1056)))), a4);
    goto loc_003FC756;
loc_003FC867:
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) >= ((unsigned int)((unsigned int)(a6)))) goto loc_003FC5D5;
    result = KeReleaseSpinLock((unsigned int)(0x1823ULL) + 16, v_stack_p38, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p70 + 1056)))), a4);
    if (0 == 0) goto loc_003FC45C;
loc_003FC890:
    result = ExpInterlockedPushEntrySList(v_stack_p48 + 16, 0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p70 + 1056)))), a4);
    if (*(unsigned __int64 *)(v_r14 + 16) != 0) goto loc_003FC890;
    goto loc_003FC45C;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpTraceStackKey(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint16_t v_stack_m1C4;
    uint32_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint16_t v_stack_m1D8;
    uint64_t v_stack_m58;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p110;
    uint64_t v_stack_p118;
    uint16_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint16_t v_stack_p34;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;

    local_rsp = (local_rsp) - (440);
    result = (*(uint64_t *)(v_rip + 0xA0E495)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m190 = Arg4;
    v_stack_m1C4 = (uint16_t)(Arg3);
    v_stack_m1B8 = Arg2;
    v_stack_m188 = Arg1;
    v_stack_m198 = 0;
    v_stack_m1B0 = *(uint64_t *)(arg1 + 0x420);
    if (*(uint64_t *)(arg1 + 0x420) == 0) goto loc_003FC46C;
    local_r15 = 0;
    local_rdi = 0;
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(Arg6)))) << (2);
    Arg3 = 0;
    if (local_r10 == 0) goto loc_003FC32F;
    Arg4 = 0;
loc_003FC310:
    Arg3 = (uint32_t)((Arg3) + (2));
    Arg2 = (*(uint16_t *)(arg5 + Arg3 + 0x1 * 2)) ^ (*(uint16_t *)(arg5 + Arg4 * 2));
    local_rdi = (local_rdi) + (Arg2);
    if (((uint32_t)(Arg3)) < local_r10) goto loc_003FC310;
loc_003FC32F:
    Arg2 = 0;
    local_rbp = 0;
    v_stack_m1C0 = v_cr8;
    if (((uint8_t)(v_cr8)) != 1) goto loc_003FC4E1;
loc_003FC35A:
    if ((*(uint32_t *)(v_rip + 0xBCA9B8)) != 0) goto loc_003FC505;
loc_003FC36E:
    if (((*(uint8_t *)(v_rip + 0xBCA791)) & (33)) == 0) goto loc_003FC446;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB11AD2))) != 0) goto loc_003FC446;
    result = KiAcquireSpinLockInstrumented(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8 + 16, Arg2, Arg3, (uint32_t)(Arg3));
loc_003FC393:
loc_003FC3A0:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8)) == (*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8)) goto loc_003FC512;
    local_rbp = (uint32_t)((local_rbp) + 1);
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8) + 0x1C)) != ((uint32_t)(local_rdi))) goto loc_003FC3B7;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8) + 0x20)) == ((uint32_t)((uint32_t)(Arg6)))) goto loc_003FC3BC;
loc_003FC3B7:
    goto loc_003FC3A0;
loc_003FC3BC:
    Arg2 = 0;
loc_003FC3C1:
    v_stack_m1A8 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8));
    v_stack_m1C8 = 0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8)) == 0) goto loc_003FC413;
    Arg3 = 32;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8)) + 0x20)))) < 32) { Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8)) + 0x20))); }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8))) + (40);
    v_stack_m1A0 = Arg3;
    local_rbx = ((uint32_t)(Arg3)) << (3);
    result = RtlCompareMemory(Arg1, Arg5 + Arg2 * 8, local_rbx, (uint32_t)(Arg3));
    if (result != local_rbx) goto loc_003FC3B7;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m1C8)) + (v_stack_m1A0));
    goto loc_003FC3C1;
loc_003FC413:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8))) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8)))) goto loc_003FC43F;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8)))) goto loc_003FC43F;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8)) + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8))) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8)) + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8) + 0x8)) == (*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8)) goto loc_003FC72B;
loc_003FC43F:
loc_003FC446:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8) + 0x8)) >= (*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8)) goto loc_003FC393;
    result = KxWaitForSpinLockAndAcquire(3, Arg2, 32, (uint32_t)(Arg3));
    goto loc_003FC393;
loc_003FC45C:
    if (0 != 0) {
        Arg2 = Arg5;
        Arg1 = 0;
        result = EtwpDereferenceStackEntry(Arg1, Arg2, 32, (uint32_t)(Arg3));
    }
    local_r15 = 0;
    goto loc_003FC4B8;
loc_003FC471:
    v_stack_m1D0 = 0x500602ULL;
    v_stack_m1D8 = (uint16_t)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8);
    result = EtwpLogKernelEvent(v_stack_mE8, Arg2, 32, (uint16_t)(Arg5));
loc_003FC4A0:
    result = ExpInterlockedPushEntrySList(v_stack_m190 + 16, local_rbx, 32, (uint16_t)(Arg5));
    if (*(uint64_t *)(local_rbx + 0x10) != 0) goto loc_003FC4A0;
loc_003FC4B8:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_rbx, 32, (uint16_t)(Arg5));
    local_rsp = (local_rsp) + (440);
    return result;
loc_003FC4E1:
    if ((uint8_t)(*(uint64_t *)(local_rbx + 0x10)) == 0) goto loc_003FC35A;
    if (((uint8_t)(*(uint64_t *)(local_rbx + 0x10))) == ((uint8_t)(result))) goto loc_003FC36E;
    result = KxTryToAcquireSpinLock(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8 + 16, local_rbx, 32, (uint16_t)(Arg5));
    if ((uint8_t)(result) != 0) goto loc_003FC393;
    goto loc_003FC4B8;
loc_003FC505:
    result = KiRaiseIrqlProcessIrqlFlags(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8 + 16, (uint8_t)(result), 32, (uint16_t)(Arg5));
    goto loc_003FC36E;
loc_003FC512:
    if (((uint32_t)(local_rbp)) != 4) goto loc_003FC53A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8))) != (*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8)) goto loc_003FC43F;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8))) goto loc_003FC43F;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 0x8)) = *(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8;
loc_003FC53A:
    local_r14 = 0;
    local_rbp = 0;
    v_stack_p50 = 0;
    if ((uint32_t)((uint32_t)(Arg6)) == 0) goto loc_003FC5D5;
    result = (v_stack_p48) + (16);
    v_stack_p58 = result;
loc_003FC560:
    result = ExpInterlockedPopEntrySList(result, (uint8_t)(result), 32, (uint16_t)(Arg5));
    if (result == 0) goto loc_003FC867;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) - (0));
    if (((uint32_t)(local_rbp + 32)) < ((uint32_t)((uint32_t)(Arg6)))) { result = 32; }
    Arg3 = ((uint32_t)((uint32_t)(result))) << (3);
    v_stack_p30 = (uint32_t)(result);
    result = memcpy(result + 40, v_stack_m190 + local_rbp * 8, Arg3, (uint16_t)(Arg5));
    if (0 != 0) goto loc_003FC71A;
loc_003FC5AE:
    if (v_stack_p50 != 0) goto loc_003FC722;
loc_003FC5BC:
    local_rbp = (uint32_t)((local_rbp) + ((uint32_t)((uint32_t)(v_stack_p30))));
    v_stack_p50 = result;
    *(uint64_t *)(result + 0x10) = 0;
    if (((uint32_t)(local_rbp)) < ((uint32_t)((uint32_t)(Arg6)))) goto loc_003FC560;
loc_003FC5D5:
    *(uint32_t *)(result + 0x1C) = (uint32_t)(*(uint64_t *)(local_rbx + 0x10));
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(Arg6));
    *(uint32_t *)(result + 0x18) = 2;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8))) != (*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8)) goto loc_003FC43F;
    *(uint64_t *)(result) = *(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8)) = result;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) = result;
    result = KxReleaseSpinLock(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 2 * 2 * 8 + 16, v_stack_m190 + local_rbp * 8, Arg3, (uint16_t)(Arg5));
    if ((*(uint32_t *)(v_rip + 0xBCA70D)) != 0) {
        Arg1 = local_rbp + 2;
        Arg2 = (uint8_t)(v_stack_p38);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, (uint16_t)(Arg5));
    }
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) == 0) goto loc_003FC76B;
    if (((uint32_t)((uint32_t)((uint32_t)(1 - 2)))) != 1) goto loc_003FC76B;
    local_rdi = 0;
    v_stack_p38 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8);
    v_stack_p88 = 8;
    v_stack_p80 = v_stack_p38;
loc_003FC692:
    Arg4 = 32;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 0x20)))) < 32) { Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 0x20))); }
    result = (1) << (4);
    local_r11 = (uint16_t)((1) + 1);
    Arg1 = (v_stack_p80) + (result);
    *(uint64_t *)(arg1) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 40;
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(Arg4 * 8);
    *(uint32_t *)(arg1 + 0xC) = 0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 0x10) != 0) goto loc_003FC692;
    v_stack_p28 = 0x500602ULL;
    v_stack_p20 = (uint16_t)((uint32_t)(0x1823ULL));
    result = EtwpLogKernelEvent(v_stack_p80, *(uint64_t *)(*(uint64_t *)(v_stack_p48) + 0x550), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p48))), (uint16_t)(local_r11));
loc_003FC700:
    result = ExpInterlockedPushEntrySList(v_stack_p48 + 16, *(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p48))), (uint16_t)(local_r11));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 0x10) != 0) goto loc_003FC700;
    goto loc_003FC76B;
loc_003FC71A:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 0x10) + 0x20) = (uint32_t)(result);
    goto loc_003FC5AE;
loc_003FC722:
    *(uint64_t *)(v_stack_p48 + 0x10 + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 0x10);
    goto loc_003FC5BC;
loc_003FC72B:
    *(uint64_t *)(result) = result;
    *(uint64_t *)(result + 0x8) = (uint32_t)(0x1823ULL);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)((uint32_t)(0x1823ULL)) = result;
    result = KxReleaseSpinLock((uint32_t)(0x1823ULL) + 16, *(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p48))), (uint16_t)(local_r11));
    if ((*(uint32_t *)(v_rip + 0xBCA5D5)) != ((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x420) + Arg2 + Arg2 + 0x2 * 2 * 8 + 0x8) + 0x10)))) goto loc_003FC856;
loc_003FC756:
loc_003FC76B:
    v_stack_p60 = result;
    local_r14 = 0;
    *(uint64_t *)(v_stack_p68 + 0x10) = v_stack_p60;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p40));
    *(uint64_t *)(v_stack_p68 + 0x18) = 8;
    v_stack_p20 = (uint16_t)(v_stack_p34);
    result = EtwpLogKernelEvent(v_stack_p68, *(uint64_t *)(v_stack_p70 + 0x550), (uint32_t)(*(uint32_t *)(v_stack_p70)), local_r14 + 2);
    v_stack_p68 = *(uint64_t *)(v_stack_p70 + 0x420);
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) != 1) goto loc_003FC4B8;
    v_stack_p70 = v_stack_p60;
    v_stack_p118 = 8;
    v_stack_p110 = v_stack_p70;
loc_003FC810:
    Arg4 = 32;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60 + 0x20)))) < 32) { Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60 + 0x20))); }
    result = ((uint16_t)((uint32_t)(0xFFFFFFFFULL) + 2)) << (4);
    local_rsi = (uint16_t)(((uint32_t)(0xFFFFFFFFULL) + 2) + 1);
    Arg1 = (v_stack_p110) + (result);
    *(uint64_t *)(arg1) = v_stack_p60 + 40;
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(Arg4 * 8);
    *(uint32_t *)(arg1 + 0xC) = 0;
    if (*(uint64_t *)(v_stack_p60 + 0x10) != 0) goto loc_003FC810;
    goto loc_003FC471;
loc_003FC856:
    result = KiLowerIrqlProcessIrqlFlags((uint8_t)(v_stack_p38), (uint8_t)(v_stack_p60), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p70 + 0x420)))), Arg4);
    goto loc_003FC756;
loc_003FC867:
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) >= ((uint32_t)((uint32_t)(Arg6)))) goto loc_003FC5D5;
    result = KeReleaseSpinLock((uint32_t)(0x1823ULL) + 16, v_stack_p38, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p70 + 0x420)))), Arg4);
    if (0 == 0) goto loc_003FC45C;
loc_003FC890:
    result = ExpInterlockedPushEntrySList(v_stack_p48 + 16, 0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p70 + 0x420)))), Arg4);
    if (*(uint64_t *)(local_r14 + 0x10) != 0) goto loc_003FC890;
    goto loc_003FC45C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x420` | `64` | `R` |
| `Arg5` | `+ 0x0 + r9*2` | `16` | `R` |
| `Arg5` | `+ 0x0 + rax*2` | `16` | `R` |
| `Arg5` | `+ 0x0 + rbp*8` | `64` | `R` |
| `Arg5` | `+ 0x0 + rdx*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FC290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
