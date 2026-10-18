# EmpEvaluateNodeLink

- RVA: `0x0044313C`–`0x004436A5` (길이 `1,385` bytes)
- VA: `0x000000014044313C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A5438`
- 디코드: `336`개 명령, `1,385/1,385` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0044324D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00443369` → [EmpEvaluateNodeLink](EmpEvaluateNodeLink_function_0044313C.md) (function, `0x0044313C`)
- `0x0044340F` → [HalMatchAcpiOemId](../3F/HalMatchAcpiOemId_function_003F6A90.md) (function, `0x003F6A90`)
- `0x0044353F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00443551` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00443563` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0044357B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004435BA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00443629` → [EmpEvaluateNodeLink](EmpEvaluateNodeLink_function_0044313C.md) (function, `0x0044313C`)
- `0x00443690` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0044369B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [EmpEvaluateTargetRule](EmpEvaluateTargetRule_function_00442E50.md) at `0x0044300B`
- [EmpEvaluateNodeLink](EmpEvaluateNodeLink_function_0044313C.md) at `0x00443369`
- [EmpEvaluateNodeLink](EmpEvaluateNodeLink_function_0044313C.md) at `0x00443629`
- [sub_006EFB70](../6E/Unknown_function_006EFB70.md) at `0x006EFBBD`
- [sub_006EFB70](../6E/Unknown_function_006EFB70.md) at `0x006EFC4E`

### Static image references
- `0x004433E0` → RVA `0x003F6A90` (`HalMatchAcpiOemId`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x0044324D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0044353F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00443551` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00443563` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0044357B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004435BA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00443384` → [sub_006EFB70](../6E/Unknown_function_006EFB70.md) (`tail-transfer`)
  - `0x00443635` → [sub_006EFB70](../6E/Unknown_function_006EFB70.md) (`tail-transfer`)
  - `0x0044363E` → [sub_006EFB70 + 0x71](../6E/Unknown_function_006EFB70.md) (`tail-transfer`)
  - `0x00443644` → [sub_006EFB70](../6E/Unknown_function_006EFB70.md) (`tail-transfer`)
  - `0x0044364B` → [sub_006EFB70 + 0x91](../6E/Unknown_function_006EFB70.md) (`tail-transfer`)
  - `0x00443696` → [sub_006EFB70 + 0xE3](../6E/Unknown_function_006EFB70.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0044313C  48 8B C4                        mov rax, rsp
0044313F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00443143  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00443147  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0044314B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0044314F  53                              push rbx
00443150  55                              push rbp
00443151  56                              push rsi
00443152  57                              push rdi
00443153  41 54                           push r12
00443155  41 55                           push r13
00443157  41 56                           push r14
00443159  41 57                           push r15
0044315B  48 81 EC 98 00 00 00            sub rsp, 0x98
00443162  48 8B BC 24 28 01 00 00         mov rdi, qword ptr [rsp + 0x128]
0044316A  33 F6                           xor esi, esi
0044316C  8B 01                           mov eax, dword ptr [rcx]
0044316E  45 33 D2                        xor r10d, r10d
00443171  45 8B D8                        mov r11d, r8d
00443174  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
00443179  44 8B 84 24 30 01 00 00         mov r8d, dword ptr [rsp + 0x130]
00443181  45 33 F6                        xor r14d, r14d
00443184  8D 5E 01                        lea ebx, [rsi + 1]
00443187  45 33 FF                        xor r15d, r15d
0044318A  33 ED                           xor ebp, ebp
0044318C  4C 8B C9                        mov r9, rcx
0044318F  4C 8B E7                        mov r12, rdi
00443192  45 8B E8                        mov r13d, r8d
00443195  3B C3                           cmp eax, ebx
00443197  0F 87 6F 01 00 00               ja 0x14044330c
0044319D  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
004431A1  85 C0                           test eax, eax
004431A3  0F 85 27 04 00 00               jne 0x1404435d0
004431A9  48 8B E9                        mov rbp, rcx
004431AC  48 39 71 10                     cmp qword ptr [rcx + 0x10], rsi
004431B0  0F 84 DC 02 00 00               je 0x140443492
004431B6  8B 49 40                        mov ecx, dword ptr [rcx + 0x40]
004431B9  8B 55 3C                        mov edx, dword ptr [rbp + 0x3c]
004431BC  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
004431C0  8B 4D 38                        mov ecx, dword ptr [rbp + 0x38]
004431C3  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
004431C7  41 8B 51 10                     mov edx, dword ptr [r9 + 0x10]
004431CB  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
004431CF  89 54 24 6C                     mov dword ptr [rsp + 0x6c], edx
004431D3  85 D2                           test edx, edx
004431D5  0F 85 04 03 00 00               jne 0x1404434df
004431DB  4C 8B 8C 24 18 01 00 00         mov r9, qword ptr [rsp + 0x118]
004431E3  8B 94 24 20 01 00 00            mov edx, dword ptr [rsp + 0x120]
004431EA  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
004431EF  89 54 24 6C                     mov dword ptr [rsp + 0x6c], edx
004431F3  4D 85 C9                        test r9, r9
004431F6  0F 84 4D 04 00 00               je 0x140443649
004431FC  85 C9                           test ecx, ecx
004431FE  0F 85 A5 02 00 00               jne 0x1404434a9
00443204  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00443208  85 C0                           test eax, eax
0044320A  74 52                           je 0x14044325e
0044320C  8B C8                           mov ecx, eax
0044320E  B8 04 00 00 00                  mov eax, 4
00443213  48 F7 E1                        mul rcx
00443216  48 85 D2                        test rdx, rdx
00443219  0F 85 80 03 00 00               jne 0x14044359f
0044321F  48 8D 50 07                     lea rdx, [rax + 7]
00443223  48 83 E2 F8                     and rdx, 0xfffffffffffffff8
00443227  4D 85 E4                        test r12, r12
0044322A  74 13                           je 0x14044323f
0044322C  41 8B CD                        mov ecx, r13d
0044322F  48 3B CA                        cmp rcx, rdx
00443232  72 0B                           jb 0x14044323f
00443234  4D 8B FC                        mov r15, r12
00443237  4C 03 E2                        add r12, rdx
0044323A  44 2B EA                        sub r13d, edx
0044323D  EB 1F                           jmp 0x14044325e
0044323F  41 B8 45 4D 65 76               mov r8d, 0x76654d45
00443245  48 8B D0                        mov rdx, rax
00443248  B9 00 01 00 00                  mov ecx, 0x100
0044324D  E8 9E EE 73 00                  call 0x140b820f0
00443252  4C 8B F8                        mov r15, rax
00443255  48 85 C0                        test rax, rax
00443258  0F 84 41 03 00 00               je 0x14044359f
0044325E  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
00443263  45 85 D2                        test r10d, r10d
00443266  74 37                           je 0x14044329f
00443268  B8 08 00 00 00                  mov eax, 8
0044326D  49 F7 E2                        mul r10
00443270  48 85 D2                        test rdx, rdx
00443273  0F 85 0F 03 00 00               jne 0x140443588
00443279  48 8D 50 07                     lea rdx, [rax + 7]
0044327D  48 83 E2 F8                     and rdx, 0xfffffffffffffff8
00443281  4D 85 E4                        test r12, r12
00443284  0F 84 E3 02 00 00               je 0x14044356d
0044328A  41 8B CD                        mov ecx, r13d
0044328D  48 3B CA                        cmp rcx, rdx
00443290  0F 82 D7 02 00 00               jb 0x14044356d
00443296  49 8B F4                        mov rsi, r12
00443299  4C 03 E2                        add r12, rdx
0044329C  44 2B EA                        sub r13d, edx
0044329F  44 8B 44 24 68                  mov r8d, dword ptr [rsp + 0x68]
004432A4  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
004432A9  47 8D 1C 01                     lea r11d, [r9 + r8]
004432AD  43 8D 04 13                     lea eax, [r11 + r10]
004432B1  39 44 24 6C                     cmp dword ptr [rsp + 0x6c], eax
004432B5  0F 85 5B 01 00 00               jne 0x140443416
004432BB  4D 85 F6                        test r14, r14
004432BE  0F 85 32 02 00 00               jne 0x1404434f6
004432C4  4D 85 FF                        test r15, r15
004432C7  0F 84 C4 00 00 00               je 0x140443391
004432CD  33 D2                           xor edx, edx
004432CF  41 3B D1                        cmp edx, r9d
004432D2  0F 83 B9 00 00 00               jae 0x140443391
004432D8  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
004432DD  42 8D 0C 02                     lea ecx, [rdx + r8]
004432E1  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
004432E4  3B 84 24 00 01 00 00            cmp eax, dword ptr [rsp + 0x100]
004432EB  0F 83 25 01 00 00               jae 0x140443416
004432F1  48 8B BC 24 F8 00 00 00         mov rdi, qword ptr [rsp + 0xf8]
004432F9  8B 04 87                        mov eax, dword ptr [rdi + rax*4]
004432FC  48 8B BC 24 28 01 00 00         mov rdi, qword ptr [rsp + 0x128]
00443304  41 89 04 97                     mov dword ptr [r15 + rdx*4], eax
00443308  03 D3                           add edx, ebx
0044330A  EB C3                           jmp 0x1404432cf
0044330C  83 F8 02                        cmp eax, 2
0044330F  0F 85 7D 01 00 00               jne 0x140443492
00443315  48 8B 71 08                     mov rsi, qword ptr [rcx + 8]
00443319  44 8B B4 24 10 01 00 00         mov r14d, dword ptr [rsp + 0x110]
00443321  4C 8B BC 24 08 01 00 00         mov r15, qword ptr [rsp + 0x108]
00443329  44 8B A4 24 00 01 00 00         mov r12d, dword ptr [rsp + 0x100]
00443331  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
00443334  4C 8B 8C 24 F8 00 00 00         mov r9, qword ptr [rsp + 0xf8]
0044333C  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00443340  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00443345  45 8B C3                        mov r8d, r11d
00443348  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
0044334D  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00443351  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00443355  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0044335A  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
0044335F  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00443364  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00443369  E8 CE FD FF FF                  call 0x14044313c
0044336E  8B E8                           mov ebp, eax
00443370  3B C3                           cmp eax, ebx
00443372  0F 84 1A 01 00 00               je 0x140443492
00443378  8A 06                           mov al, byte ptr [rsi]
0044337A  3C 26                           cmp al, 0x26
0044337C  0F 85 B1 02 00 00               jne 0x140443633
00443382  85 ED                           test ebp, ebp
00443384  0F 85 E6 C7 2A 00               jne 0x1406efb70
0044338A  33 DB                           xor ebx, ebx
0044338C  E9 01 01 00 00                  jmp 0x140443492
00443391  48 85 F6                        test rsi, rsi
00443394  74 35                           je 0x1404433cb
00443396  4C 8B 8C 24 08 01 00 00         mov r9, qword ptr [rsp + 0x108]
0044339E  33 D2                           xor edx, edx
004433A0  41 3B D2                        cmp edx, r10d
004433A3  73 21                           jae 0x1404433c6
004433A5  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
004433AA  42 8D 0C 1A                     lea ecx, [rdx + r11]
004433AE  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
004433B1  3B 84 24 10 01 00 00            cmp eax, dword ptr [rsp + 0x110]
004433B8  73 65                           jae 0x14044341f
004433BA  49 8B 04 C1                     mov rax, qword ptr [r9 + rax*8]
004433BE  48 89 04 D6                     mov qword ptr [rsi + rdx*8], rax
004433C2  03 D3                           add edx, ebx
004433C4  EB DA                           jmp 0x1404433a0
004433C6  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
004433CB  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
004433D3  83 38 00                        cmp dword ptr [rax], 0
004433D6  0F 85 1A 02 00 00               jne 0x1404435f6
004433DC  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
004433E0  48 8D 15 A9 36 FB FF            lea rdx, [rip - 0x4c957]
004433E7  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
004433EB  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
004433F0  48 3B C2                        cmp rax, rdx
004433F3  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
004433F8  48 8B CE                        mov rcx, rsi
004433FB  45 8B C8                        mov r9d, r8d
004433FE  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00443403  4D 8B C6                        mov r8, r14
00443406  41 8B D2                        mov edx, r10d
00443409  0F 85 8C 02 00 00               jne 0x14044369b
0044340F  E8 7C 36 FB FF                  call 0x1403f6a90
00443414  8B D8                           mov ebx, eax
00443416  48 85 F6                        test rsi, rsi
00443419  0F 84 69 01 00 00               je 0x140443588
0044341F  48 85 FF                        test rdi, rdi
00443422  0F 84 07 01 00 00               je 0x14044352f
00443428  48 3B F7                        cmp rsi, rdi
0044342B  0F 82 FE 00 00 00               jb 0x14044352f
00443431  44 8B AC 24 30 01 00 00         mov r13d, dword ptr [rsp + 0x130]
00443439  4A 8D 04 2F                     lea rax, [rdi + r13]
0044343D  48 3B F0                        cmp rsi, rax
00443440  0F 83 F1 00 00 00               jae 0x140443537
00443446  4D 85 FF                        test r15, r15
00443449  74 21                           je 0x14044346c
0044344B  48 85 FF                        test rdi, rdi
0044344E  0F 84 F5 00 00 00               je 0x140443549
00443454  4C 3B FF                        cmp r15, rdi
00443457  0F 82 EC 00 00 00               jb 0x140443549
0044345D  41 8B C5                        mov eax, r13d
00443460  48 03 C7                        add rax, rdi
00443463  4C 3B F8                        cmp r15, rax
00443466  0F 83 DD 00 00 00               jae 0x140443549
0044346C  4D 85 F6                        test r14, r14
0044346F  74 21                           je 0x140443492
00443471  48 85 FF                        test rdi, rdi
00443474  0F 84 E1 00 00 00               je 0x14044355b
0044347A  4C 3B F7                        cmp r14, rdi
0044347D  0F 82 D8 00 00 00               jb 0x14044355b
00443483  41 8B C5                        mov eax, r13d
00443486  48 03 C7                        add rax, rdi
00443489  4C 3B F0                        cmp r14, rax
0044348C  0F 83 C9 00 00 00               jae 0x14044355b
00443492  8B C3                           mov eax, ebx
00443494  48 81 C4 98 00 00 00            add rsp, 0x98
0044349B  41 5F                           pop r15
0044349D  41 5E                           pop r14
0044349F  41 5D                           pop r13
004434A1  41 5C                           pop r12
004434A3  5F                              pop rdi
004434A4  5E                              pop rsi
004434A5  5D                              pop rbp
004434A6  5B                              pop rbx
004434A7  C3                              ret
004434A8  CC                              int3
004434A9  B8 08 00 00 00                  mov eax, 8
004434AE  48 F7 E1                        mul rcx
004434B1  48 85 D2                        test rdx, rdx
004434B4  75 DC                           jne 0x140443492
004434B6  48 8D 50 07                     lea rdx, [rax + 7]
004434BA  48 83 E2 F8                     and rdx, 0xfffffffffffffff8
004434BE  48 85 FF                        test rdi, rdi
004434C1  0F 84 E5 00 00 00               je 0x1404435ac
004434C7  4C 3B C2                        cmp r8, rdx
004434CA  0F 82 DC 00 00 00               jb 0x1404435ac
004434D0  4C 8D 24 3A                     lea r12, [rdx + rdi]
004434D4  44 2B EA                        sub r13d, edx
004434D7  4C 8B F7                        mov r14, rdi
004434DA  E9 25 FD FF FF                  jmp 0x140443204
004434DF  4D 8B 49 18                     mov r9, qword ptr [r9 + 0x18]
004434E3  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
004434E8  4D 85 C9                        test r9, r9
004434EB  0F 85 0B FD FF FF               jne 0x1404431fc
004434F1  E9 E5 FC FF FF                  jmp 0x1404431db
004434F6  33 D2                           xor edx, edx
004434F8  41 3B D0                        cmp edx, r8d
004434FB  0F 83 C3 FD FF FF               jae 0x1404432c4
00443501  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00443506  8B 04 90                        mov eax, dword ptr [rax + rdx*4]
00443509  3B 84 24 F0 00 00 00            cmp eax, dword ptr [rsp + 0xf0]
00443510  0F 83 00 FF FF FF               jae 0x140443416
00443516  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
0044351E  44 8B 44 24 68                  mov r8d, dword ptr [rsp + 0x68]
00443523  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00443527  49 89 0C D6                     mov qword ptr [r14 + rdx*8], rcx
0044352B  03 D3                           add edx, ebx
0044352D  EB C9                           jmp 0x1404434f8
0044352F  44 8B AC 24 30 01 00 00         mov r13d, dword ptr [rsp + 0x130]
00443537  BA 45 4D 65 76                  mov edx, 0x76654d45
0044353C  48 8B CE                        mov rcx, rsi
0044353F  E8 2C F3 73 00                  call 0x140b82870
00443544  E9 FD FE FF FF                  jmp 0x140443446
00443549  BA 45 4D 65 76                  mov edx, 0x76654d45
0044354E  49 8B CF                        mov rcx, r15
00443551  E8 1A F3 73 00                  call 0x140b82870
00443556  E9 11 FF FF FF                  jmp 0x14044346c
0044355B  BA 45 4D 65 76                  mov edx, 0x76654d45
00443560  49 8B CE                        mov rcx, r14
00443563  E8 08 F3 73 00                  call 0x140b82870
00443568  E9 25 FF FF FF                  jmp 0x140443492
0044356D  41 B8 45 4D 65 76               mov r8d, 0x76654d45
00443573  48 8B D0                        mov rdx, rax
00443576  B9 00 01 00 00                  mov ecx, 0x100
0044357B  E8 70 EB 73 00                  call 0x140b820f0
00443580  48 8B F0                        mov rsi, rax
00443583  48 85 C0                        test rax, rax
00443586  75 0D                           jne 0x140443595
00443588  44 8B AC 24 30 01 00 00         mov r13d, dword ptr [rsp + 0x130]
00443590  E9 B1 FE FF FF                  jmp 0x140443446
00443595  44 8B 54 24 64                  mov r10d, dword ptr [rsp + 0x64]
0044359A  E9 00 FD FF FF                  jmp 0x14044329f
0044359F  44 8B AC 24 30 01 00 00         mov r13d, dword ptr [rsp + 0x130]
004435A7  E9 C0 FE FF FF                  jmp 0x14044346c
004435AC  41 B8 45 4D 65 76               mov r8d, 0x76654d45
004435B2  48 8B D0                        mov rdx, rax
004435B5  B9 00 01 00 00                  mov ecx, 0x100
004435BA  E8 31 EB 73 00                  call 0x140b820f0
004435BF  4C 8B F0                        mov r14, rax
004435C2  48 85 C0                        test rax, rax
004435C5  0F 85 39 FC FF FF               jne 0x140443204
004435CB  E9 C2 FE FF FF                  jmp 0x140443492
004435D0  4C 8B D1                        mov r10, rcx
004435D3  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
004435D8  40 38 71 14                     cmp byte ptr [rcx + 0x14], sil
004435DC  0F 84 B0 FE FF FF               je 0x140443492
004435E2  8B 49 30                        mov ecx, dword ptr [rcx + 0x30]
004435E5  41 8B 52 2C                     mov edx, dword ptr [r10 + 0x2c]
004435E9  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
004435ED  41 8B 4A 28                     mov ecx, dword ptr [r10 + 0x28]
004435F1  E9 CD FB FF FF                  jmp 0x1404431c3
004435F6  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
004435FB  49 8B D6                        mov rdx, r14
004435FE  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
00443603  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00443608  83 64 24 40 00                  and dword ptr [rsp + 0x40], 0
0044360D  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
00443613  48 8B 49 60                     mov rcx, qword ptr [rcx + 0x60]
00443617  44 89 54 24 30                  mov dword ptr [rsp + 0x30], r10d
0044361C  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00443621  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00443626  4D 8B CF                        mov r9, r15
00443629  E8 0E FB FF FF                  call 0x14044313c
0044362E  E9 E1 FD FF FF                  jmp 0x140443414
00443633  3C 7C                           cmp al, 0x7c
00443635  0F 85 35 C5 2A 00               jne 0x1406efb70
0044363B  83 FD 02                        cmp ebp, 2
0044363E  0F 84 9D C5 2A 00               je 0x1406efbe1
00443644  E9 27 C5 2A 00                  jmp 0x1406efb70
00443649  85 C0                           test eax, eax
0044364B  0F 85 B0 C5 2A 00               jne 0x1406efc01
00443651  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
00443655  45 8B CB                        mov r9d, r11d
00443658  4C 8B 84 24 E8 00 00 00         mov r8, qword ptr [rsp + 0xe8]
00443660  8B 94 24 10 01 00 00            mov edx, dword ptr [rsp + 0x110]
00443667  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
0044366F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00443674  8B 84 24 00 01 00 00            mov eax, dword ptr [rsp + 0x100]
0044367B  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0044367F  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00443687  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0044368C  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
00443690  E8 3B 74 27 00                  call 0x1406baad0
00443695  90                              nop
00443696  E9 B8 C5 2A 00                  jmp 0x1406efc53
0044369B  E8 30 74 27 00                  call 0x1406baad0
004436A0  E9 6F FD FF FF                  jmp 0x140443414
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmpEvaluateNodeLink(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8, unsigned int a9, __int64 a10, unsigned int a11)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned int v_stack_p64;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pE8;
    unsigned int v_stack_pF0;
    unsigned __int64 v_stack_pF8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (152);
    v_rsi = 0;
    v_r10 = 0;
    v_stack_m60 = 0;
    v_r14 = 0;
    v_r15 = 0;
    v_rbp = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) > ((unsigned int)(v_rsi + 1))) goto loc_0044330C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) != 0) goto loc_004435D0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 16)) == 0) goto loc_00443492;
    v_stack_m74 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 64)));
loc_004431C3:
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 60)));
    v_stack_m70 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 56)));
    v_stack_m6C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))) != 0) goto loc_004434DF;
loc_004431DB:
    v_stack_m68 = a8;
    v_stack_m6C = (unsigned int)((unsigned int)(a9));
    if (a8 == 0) goto loc_00443649;
loc_004431FC:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 56))) != 0) goto loc_004434A9;
loc_00443204:
    if ((unsigned int)((unsigned int)(v_stack_m78)) == 0) goto loc_0044325E;
    if ((unsigned int)(a9) != 0) goto loc_0044359F;
    a2 = (4 + 7) & (-8);
    if (a10 == 0) goto loc_0044323F;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a11)))))) < a2) goto loc_0044323F;
    v_r12 = (a10) + (a2);
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a11)))) - ((unsigned int)(a2)));
    goto loc_0044325E;
loc_0044323F:
    result = ExAllocatePool2(256, 4, (unsigned int)(0x76654D45ULL), a8);
    if (result == 0) goto loc_0044359F;
loc_0044325E:
    if ((unsigned int)((unsigned int)(v_stack_m74)) == 0) goto loc_0044329F;
    if (4 != 0) goto loc_00443588;
    a2 = (8 + 7) & (-8);
    if (v_r12 == 0) goto loc_0044356D;
    if (((unsigned int)((unsigned int)(v_r13))) < a2) goto loc_0044356D;
    v_r12 = (v_r12) + (a2);
    v_r13 = (unsigned int)((v_r13) - ((unsigned int)(a2)));
loc_0044329F:
    if (v_stack_m6C != ((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1 + (unsigned int)(v_stack_m74) * 1))) goto loc_00443416;
    if (0 != 0) goto loc_004434F6;
loc_004432C4:
    if (result == 0) goto loc_00443391;
    a2 = 0;
loc_004432CF:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m78)))) goto loc_00443391;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68 + a2 + (unsigned int)(v_stack_m70) * 1 * 4)))) >= a5) goto loc_00443416;
    *(unsigned int *)(result + a2 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + (unsigned int)(*(unsigned int *)(v_stack_m68 + a2 + (unsigned int)(v_stack_m70) * 1 * 4)) * 4)));
    a2 = (unsigned int)((a2) + ((unsigned int)(v_rsi + 1)));
    goto loc_004432CF;
loc_0044330C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + (unsigned int)(*(unsigned int *)(v_stack_m68 + a2 + (unsigned int)(v_stack_m70) * 1 * 4)) * 4)))) != 2) goto loc_00443492;
    v_stack_m88 = (unsigned int)((unsigned int)(v_stack_m70));
    v_stack_m90 = a10;
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8) + 16)));
    v_stack_mA0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8) + 24);
    v_stack_mA8 = (unsigned int)((unsigned int)(a7));
    v_stack_mB0 = a6;
    v_stack_mB8 = (unsigned int)((unsigned int)(a5));
    result = EmpEvaluateNodeLink(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8) + 8), a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)), v_stack_p20);
    if (((unsigned int)(result)) == ((unsigned int)(v_rsi + 1))) goto loc_00443492;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8)))) != 38) goto loc_00443633;
    v_rbx = 0;
    goto loc_00443492;
loc_00443391:
    if (*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8) == 0) goto loc_004433CB;
    a2 = 0;
loc_004433A0:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m74)))) goto loc_004433C6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68 + a2 + (unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1 * 1 * 4)))) >= a7) goto loc_0044341F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8) + a2 * 8) = *(unsigned __int64 *)(a6 + (unsigned int)(*(unsigned int *)(v_stack_m68 + a2 + (unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1 * 1 * 4)) * 8);
    a2 = (unsigned int)((a2) + (0));
    goto loc_004433A0;
loc_004433C6:
loc_004433CB:
    if ((*(unsigned int *)(v_stack_p8)) != 0) goto loc_004435F6;
    v_stack_mA8 = *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 32);
    v_stack_mB0 = (unsigned int)((unsigned int)(v_stack_m78));
    v_stack_mB8 = a6;
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 16)) != (v_rip - 313687)) goto loc_0044369B;
    result = HalMatchAcpiOemId(*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8), (unsigned int)((unsigned int)((unsigned int)(v_stack_m74))), (unsigned int)(a7), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)))));
loc_00443414:
loc_00443416:
    if (*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8) == 0) goto loc_00443588;
loc_0044341F:
    if (a10 == 0) goto loc_0044352F;
    if ((*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8)) < a10) goto loc_0044352F;
    if ((*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8)) >= (a10 + (unsigned int)(a11) * 1)) goto loc_00443537;
loc_00443446:
    if (a6 == 0) goto loc_0044346C;
    if (a10 == 0) goto loc_00443549;
    if (a6 < a10) goto loc_00443549;
    result = ((unsigned int)((unsigned int)((unsigned int)(a11)))) + (a10);
    if (a6 >= result) goto loc_00443549;
loc_0044346C:
    if ((unsigned int)(a7) == 0) goto loc_00443492;
    if (a10 == 0) goto loc_0044355B;
    if (((unsigned int)(a7)) < a10) goto loc_0044355B;
    result = ((unsigned int)((unsigned int)((unsigned int)(a11)))) + (a10);
    if (((unsigned int)(a7)) >= result) goto loc_0044355B;
loc_00443492:
    v_rsp = (v_rsp) + (152);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_004434A9:
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_m74))) != 0) goto loc_00443492;
    a2 = (8 + 7) & (-8);
    if (a10 == 0) goto loc_004435AC;
    if (((unsigned int)(a7)) < a2) goto loc_004435AC;
    v_r13 = (unsigned int)(((unsigned int)(a11)) - ((unsigned int)(a2)));
    goto loc_00443204;
loc_004434DF:
    v_stack_p70 = *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)))) + 24);
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)))) + 24) != 0) goto loc_004431FC;
    goto loc_004431DB;
loc_004434F6:
    a2 = 0;
loc_004434F8:
    if (0 >= ((unsigned int)((unsigned int)(a7)))) goto loc_004432C4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p70 + a2 * 4)))) >= v_stack_pF0) goto loc_00443416;
    *(unsigned __int64 *)(a10 + a2 * 8) = *(unsigned __int64 *)(v_stack_pE8 + (unsigned int)(*(unsigned int *)(v_stack_p70 + a2 * 4)) * 8);
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_004434F8;
loc_0044352F:
loc_00443537:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_m70) * 1 + 8), (unsigned int)(0x76654D45ULL), (unsigned int)(v_stack_p68), *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)))) + 24));
    goto loc_00443446;
loc_00443549:
    result = ExFreePoolWithTag(a6, (unsigned int)(0x76654D45ULL), (unsigned int)(v_stack_p68), *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)))) + 24));
    goto loc_0044346C;
loc_0044355B:
    result = ExFreePoolWithTag(a10, (unsigned int)(0x76654D45ULL), (unsigned int)(v_stack_p68), *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)))) + 24));
    goto loc_00443492;
loc_0044356D:
    result = ExAllocatePool2(256, result, (unsigned int)(0x76654D45ULL), *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)))) + 24));
    if (result != 0) goto loc_00443595;
loc_00443588:
    goto loc_00443446;
loc_00443595:
    goto loc_0044329F;
loc_0044359F:
    goto loc_0044346C;
loc_004435AC:
    result = ExAllocatePool2(256, result, (unsigned int)(0x76654D45ULL), *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)))) + 24));
    if (result != 0) goto loc_00443204;
    goto loc_00443492;
loc_004435D0:
    v_stack_p78 = 256;
    if ((*(unsigned __int8 *)(256 + 20)) == ((unsigned __int8)(result))) goto loc_00443492;
    v_stack_p64 = (unsigned int)((unsigned int)(*(unsigned int *)(256 + 48)));
    goto loc_004431C3;
loc_004435F6:
    v_stack_p50 = (unsigned int)((unsigned int)(a11));
    v_stack_p48 = a2 + a10 * 1;
    v_stack_p30 = 256;
    v_stack_p28 = result;
    v_stack_p20 = (unsigned int)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)))) + 24));
    result = EmpEvaluateNodeLink(*(unsigned __int64 *)(v_stack_p78 + 96), result, (unsigned int)(0x76654D45ULL), a6);
    goto loc_00443414;
loc_00443633:
loc_00443649:
    v_stack_p30 = *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 32);
    v_stack_p28 = (unsigned int)((unsigned int)(a5));
    v_stack_p20 = v_stack_pF8;
    result = guard_dispatch_icall(a6, (unsigned int)(a7), v_stack_pE8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)));
loc_0044369B:
    result = guard_dispatch_icall(a6, (unsigned int)(a7), v_stack_pE8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m78) + (unsigned int)(v_stack_m70) * 1)));
    goto loc_00443414;
}
```

## 5. (Beta) C Style

```c
int64_t EmpEvaluateNodeLink(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, void *Arg6, uint32_t Arg7, int64_t Arg8, uint32_t Arg9, int64_t Arg10, uint32_t Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint32_t v_stack_p64;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_pE8;
    uint32_t v_stack_pF0;
    uint64_t v_stack_pF8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (152);
    local_rsi = 0;
    local_r10 = 0;
    v_stack_m60 = 0;
    local_r14 = 0;
    local_r15 = 0;
    local_rbp = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) > ((uint32_t)(local_rsi + 1))) goto loc_0044330C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) != 0) goto loc_004435D0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10)) == 0) goto loc_00443492;
    v_stack_m74 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x40)));
loc_004431C3:
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3C)));
    v_stack_m70 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38)));
    v_stack_m6C = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))) != 0) goto loc_004434DF;
loc_004431DB:
    v_stack_m68 = Arg8;
    v_stack_m6C = (uint32_t)((uint32_t)(Arg9));
    if (Arg8 == 0) goto loc_00443649;
loc_004431FC:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38))) != 0) goto loc_004434A9;
loc_00443204:
    if ((uint32_t)((uint32_t)(v_stack_m78)) == 0) goto loc_0044325E;
    if ((uint32_t)(Arg9) != 0) goto loc_0044359F;
    Arg2 = (4 + 7) & (-8);
    if (Arg10 == 0) goto loc_0044323F;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg11)))))) < Arg2) goto loc_0044323F;
    local_r12 = (Arg10) + (Arg2);
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg11)))) - ((uint32_t)(Arg2)));
    goto loc_0044325E;
loc_0044323F:
    result = ExAllocatePool2(256, 4, (uint32_t)(0x76654D45ULL), Arg8);
    if (result == 0) goto loc_0044359F;
loc_0044325E:
    if ((uint32_t)((uint32_t)(v_stack_m74)) == 0) goto loc_0044329F;
    if (4 != 0) goto loc_00443588;
    Arg2 = (8 + 7) & (-8);
    if (local_r12 == 0) goto loc_0044356D;
    if (((uint32_t)((uint32_t)(local_r13))) < Arg2) goto loc_0044356D;
    local_r12 = (local_r12) + (Arg2);
    local_r13 = (uint32_t)((local_r13) - ((uint32_t)(Arg2)));
loc_0044329F:
    if (v_stack_m6C != ((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1 + (uint32_t)(v_stack_m74) * 1))) goto loc_00443416;
    if (0 != 0) goto loc_004434F6;
loc_004432C4:
    if (result == 0) goto loc_00443391;
    Arg2 = 0;
loc_004432CF:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m78)))) goto loc_00443391;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68 + Arg2 + (uint32_t)(v_stack_m70) * 1 * 4)))) >= Arg5) goto loc_00443416;
    *(uint32_t *)(result + Arg2 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + (uint32_t)(*(uint32_t *)(v_stack_m68 + Arg2 + (uint32_t)(v_stack_m70) * 1 * 4)) * 4)));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_rsi + 1)));
    goto loc_004432CF;
loc_0044330C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + (uint32_t)(*(uint32_t *)(v_stack_m68 + Arg2 + (uint32_t)(v_stack_m70) * 1 * 4)) * 4)))) != 2) goto loc_00443492;
    v_stack_m88 = (uint32_t)((uint32_t)(v_stack_m70));
    v_stack_m90 = Arg10;
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8) + 0x10)));
    v_stack_mA0 = *(uint64_t *)(*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8) + 0x18);
    v_stack_mA8 = (uint32_t)((uint32_t)(Arg7));
    v_stack_mB0 = Arg6;
    v_stack_mB8 = (uint32_t)((uint32_t)(Arg5));
    result = EmpEvaluateNodeLink(*(uint64_t *)(*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8) + 0x8), Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)), v_stack_p20);
    if (((uint32_t)(result)) == ((uint32_t)(local_rsi + 1))) goto loc_00443492;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8)))) != 38) goto loc_00443633;
    local_rbx = 0;
    goto loc_00443492;
loc_00443391:
    if (*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8) == 0) goto loc_004433CB;
    Arg2 = 0;
loc_004433A0:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m74)))) goto loc_004433C6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68 + Arg2 + (uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1 * 1 * 4)))) >= Arg7) goto loc_0044341F;
    *(uint64_t *)(*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8) + Arg2 * 8) = *(uint64_t *)(arg6 + (uint32_t)(*(uint32_t *)(v_stack_m68 + Arg2 + (uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1 * 1 * 4)) * 8);
    Arg2 = (uint32_t)((Arg2) + (0));
    goto loc_004433A0;
loc_004433C6:
loc_004433CB:
    if ((*(uint32_t *)(v_stack_p8)) != 0) goto loc_004435F6;
    v_stack_mA8 = *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x20);
    v_stack_mB0 = (uint32_t)((uint32_t)(v_stack_m78));
    v_stack_mB8 = Arg6;
    if ((*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x10)) != (v_rip - 313687)) goto loc_0044369B;
    result = HalMatchAcpiOemId(*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8), (uint32_t)((uint32_t)((uint32_t)(v_stack_m74))), (uint32_t)(Arg7), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)))));
loc_00443414:
loc_00443416:
    if (*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8) == 0) goto loc_00443588;
loc_0044341F:
    if (Arg10 == 0) goto loc_0044352F;
    if ((*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8)) < Arg10) goto loc_0044352F;
    if ((*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8)) >= (Arg10 + (uint32_t)(Arg11) * 1)) goto loc_00443537;
loc_00443446:
    if (Arg6 == NULL) goto loc_0044346C;
    if (Arg10 == 0) goto loc_00443549;
    if (Arg6 < Arg10) goto loc_00443549;
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg11)))) + (Arg10);
    if (Arg6 >= result) goto loc_00443549;
loc_0044346C:
    if ((uint32_t)(Arg7) == 0) goto loc_00443492;
    if (Arg10 == 0) goto loc_0044355B;
    if (((uint32_t)(Arg7)) < Arg10) goto loc_0044355B;
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg11)))) + (Arg10);
    if (((uint32_t)(Arg7)) >= result) goto loc_0044355B;
loc_00443492:
    local_rsp = (local_rsp) + (152);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_004434A9:
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_m74))) != 0) goto loc_00443492;
    Arg2 = (8 + 7) & (-8);
    if (Arg10 == 0) goto loc_004435AC;
    if (((uint32_t)(Arg7)) < Arg2) goto loc_004435AC;
    local_r13 = (uint32_t)(((uint32_t)(Arg11)) - ((uint32_t)(Arg2)));
    goto loc_00443204;
loc_004434DF:
    v_stack_p70 = *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)))) + 0x18);
    if (*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)))) + 0x18) != 0) goto loc_004431FC;
    goto loc_004431DB;
loc_004434F6:
    Arg2 = 0;
loc_004434F8:
    if (0 >= ((uint32_t)((uint32_t)(Arg7)))) goto loc_004432C4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p70 + Arg2 * 4)))) >= v_stack_pF0) goto loc_00443416;
    *(uint64_t *)(Arg10 + Arg2 * 8) = *(uint64_t *)(v_stack_pE8 + (uint32_t)(*(uint32_t *)(v_stack_p70 + Arg2 * 4)) * 8);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_004434F8;
loc_0044352F:
loc_00443537:
    result = ExFreePoolWithTag(*(uint64_t *)(Arg2 + (uint32_t)(v_stack_m70) * 1 + 0x8), (uint32_t)(0x76654D45ULL), (uint32_t)(v_stack_p68), *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)))) + 0x18));
    goto loc_00443446;
loc_00443549:
    result = ExFreePoolWithTag(Arg6, (uint32_t)(0x76654D45ULL), (uint32_t)(v_stack_p68), *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)))) + 0x18));
    goto loc_0044346C;
loc_0044355B:
    result = ExFreePoolWithTag(Arg10, (uint32_t)(0x76654D45ULL), (uint32_t)(v_stack_p68), *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)))) + 0x18));
    goto loc_00443492;
loc_0044356D:
    result = ExAllocatePool2(256, result, (uint32_t)(0x76654D45ULL), *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)))) + 0x18));
    if (result != 0) goto loc_00443595;
loc_00443588:
    goto loc_00443446;
loc_00443595:
    goto loc_0044329F;
loc_0044359F:
    goto loc_0044346C;
loc_004435AC:
    result = ExAllocatePool2(256, result, (uint32_t)(0x76654D45ULL), *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)))) + 0x18));
    if (result != 0) goto loc_00443204;
    goto loc_00443492;
loc_004435D0:
    v_stack_p78 = 256;
    if ((*(uint8_t *)(256 + 0x14)) == ((uint8_t)(result))) goto loc_00443492;
    v_stack_p64 = (uint32_t)((uint32_t)(*(uint32_t *)(256 + 0x30)));
    goto loc_004431C3;
loc_004435F6:
    v_stack_p50 = (uint32_t)((uint32_t)(Arg11));
    v_stack_p48 = Arg2 + Arg10 * 1;
    v_stack_p30 = 256;
    v_stack_p28 = result;
    v_stack_p20 = (uint32_t)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)))) + 0x18));
    result = EmpEvaluateNodeLink(*(uint64_t *)(v_stack_p78 + 0x60), result, (uint32_t)(0x76654D45ULL), Arg6);
    goto loc_00443414;
loc_00443633:
loc_00443649:
    v_stack_p30 = *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x20);
    v_stack_p28 = (uint32_t)((uint32_t)(Arg5));
    v_stack_p20 = v_stack_pF8;
    result = guard_dispatch_icall(Arg6, (uint32_t)(Arg7), v_stack_pE8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)));
loc_0044369B:
    result = guard_dispatch_icall(Arg6, (uint32_t)(Arg7), v_stack_pE8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m78) + (uint32_t)(v_stack_m70) * 1)));
    goto loc_00443414;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg6` | `+ 0x0 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044313C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
