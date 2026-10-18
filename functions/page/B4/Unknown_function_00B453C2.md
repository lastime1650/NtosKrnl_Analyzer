# sub_00B453C2

- RVA: `0x00B453C2`–`0x00B45864` (길이 `1,186` bytes)
- VA: `0x0000000140B453C2`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B82FC`
- 디코드: `350`개 명령, `1,186/1,186` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00B453E3` → [IopOpenRegistryKeyEx](../A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00B45422` → [PiDevCfgQueryPolicyEnabled](../73/PiDevCfgQueryPolicyEnabled_function_007352E8.md) (function, `0x007352E8`)
- `0x00B4544F` → [PiDevCfgQueryPolicyEnabled](../73/PiDevCfgQueryPolicyEnabled_function_007352E8.md) (function, `0x007352E8`)
- `0x00B45478` → [PiDevCfgQueryPolicyStringList](../73/PiDevCfgQueryPolicyStringList_function_00735358.md) (function, `0x00735358`)
- `0x00B4549A` → [PiDevCfgQueryPolicyStringList](../73/PiDevCfgQueryPolicyStringList_function_00735358.md) (function, `0x00735358`)
- `0x00B454CA` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00B45502` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00B45538` → [PiDevCfgQueryPolicyStringList](../73/PiDevCfgQueryPolicyStringList_function_00735358.md) (function, `0x00735358`)
- `0x00B4555A` → [PiDevCfgQueryPolicyStringList](../73/PiDevCfgQueryPolicyStringList_function_00735358.md) (function, `0x00735358`)
- `0x00B455C9` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00B4560E` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00B4568A` → [PiDevCfgQueryPolicyStringList](../73/PiDevCfgQueryPolicyStringList_function_00735358.md) (function, `0x00735358`)
- `0x00B456A8` → [PiDevCfgQueryPolicyStringList](../73/PiDevCfgQueryPolicyStringList_function_00735358.md) (function, `0x00735358`)
- `0x00B456DB` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00B4571F` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00B45773` → [PiDevCfgQueryPolicyEnabled](../73/PiDevCfgQueryPolicyEnabled_function_007352E8.md) (function, `0x007352E8`)
- `0x00B45808` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B45818` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B45828` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B45837` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B45846` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B45859` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B453C6` → RVA `0x00AFEA40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B453FF` → RVA `0x00AFEA60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B45448` → RVA `0x00AFEA90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B45471` → RVA `0x00AFEAC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B45489` → RVA `0x00AFED70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B45531` → RVA `0x00AFEDA0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B45549` → RVA `0x00AFEDC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B45683` → RVA `0x00AFEDE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B4569B` → RVA `0x00AFEC30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B4576C` → RVA `0x00AFEC50` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B45791` → RVA `0x00E66245` (`.data`; read)
- `0x00B4579A` → RVA `0x00E6627A` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00B454CA` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00B45502` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00B455C9` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00B4560E` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00B456DB` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00B4571F` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00B45808` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B45818` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B45828` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B45837` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B45846` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B45859` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00B453EA` → [PiDevCfgEnforceDevicePolicy + 0xAC](../A8/PiDevCfgEnforceDevicePolicy_function_00A89454.md) (`tail-transfer`)
  - `0x00B4584E` → [PiDevCfgEnforceDevicePolicy + 0xAF](../A8/PiDevCfgEnforceDevicePolicy_function_00A89454.md) (`tail-transfer`)
  - `0x00B4585F` → [PiDevCfgEnforceDevicePolicy + 0xAF](../A8/PiDevCfgEnforceDevicePolicy_function_00A89454.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B453C2  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
00B453C6  48 8D 05 73 96 FB FF            lea rax, [rip - 0x4698d]
00B453CD  44 8B CB                        mov r9d, ebx
00B453D0  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00B453D4  4C 8D 45 9F                     lea r8, [rbp - 0x61]
00B453D8  C7 45 9F 18 00 1A 00            mov dword ptr [rbp - 0x61], 0x1a0018
00B453DF  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00B453E3  E8 5C C7 F0 FF                  call 0x140a51b44
00B453E8  85 C0                           test eax, eax
00B453EA  0F 88 10 41 F4 FF               js 0x140a89500
00B453F0  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00B453F4  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
00B453F8  45 8A E5                        mov r12b, r13b
00B453FB  45 0F B6 FD                     movzx r15d, r13b
00B453FF  48 8D 15 5A 96 FB FF            lea rdx, [rip - 0x469a6]
00B45406  44 89 65 AF                     mov dword ptr [rbp - 0x51], r12d
00B4540A  44 88 6D 87                     mov byte ptr [rbp - 0x79], r13b
00B4540E  44 88 6D 8A                     mov byte ptr [rbp - 0x76], r13b
00B45412  44 88 6D 89                     mov byte ptr [rbp - 0x77], r13b
00B45416  44 88 6D 88                     mov byte ptr [rbp - 0x78], r13b
00B4541A  44 88 6D 8C                     mov byte ptr [rbp - 0x74], r13b
00B4541E  44 88 6D 8B                     mov byte ptr [rbp - 0x75], r13b
00B45422  E8 C1 FE BE FF                  call 0x1407352e8
00B45427  BB 01 00 00 00                  mov ebx, 1
00B4542C  85 C0                           test eax, eax
00B4542E  78 10                           js 0x140b45440
00B45430  44 38 6D 7F                     cmp byte ptr [rbp + 0x7f], r13b
00B45434  45 0F B6 E5                     movzx r12d, r13b
00B45438  44 0F 45 E3                     cmovne r12d, ebx
00B4543C  44 89 65 AF                     mov dword ptr [rbp - 0x51], r12d
00B45440  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00B45444  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
00B45448  48 8D 15 41 96 FB FF            lea rdx, [rip - 0x469bf]
00B4544F  E8 94 FE BE FF                  call 0x1407352e8
00B45454  85 C0                           test eax, eax
00B45456  78 11                           js 0x140b45469
00B45458  44 38 6D 7F                     cmp byte ptr [rbp + 0x7f], r13b
00B4545C  74 0B                           je 0x140b45469
00B4545E  F6 87 30 02 00 00 10            test byte ptr [rdi + 0x230], 0x10
00B45465  44 0F 45 FB                     cmovne r15d, ebx
00B45469  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00B4546D  4C 8D 45 97                     lea r8, [rbp - 0x69]
00B45471  48 8D 15 48 96 FB FF            lea rdx, [rip - 0x469b8]
00B45478  E8 DB FE BE FF                  call 0x140735358
00B4547D  48 8B 7D 97                     mov rdi, qword ptr [rbp - 0x69]
00B45481  4C 8D 45 B7                     lea r8, [rbp - 0x49]
00B45485  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00B45489  48 8D 15 E0 98 FB FF            lea rdx, [rip - 0x46720]
00B45490  85 C0                           test eax, eax
00B45492  49 0F 48 FD                     cmovs rdi, r13
00B45496  48 89 7D 97                     mov qword ptr [rbp - 0x69], rdi
00B4549A  E8 B9 FE BE FF                  call 0x140735358
00B4549F  48 8B 75 B7                     mov rsi, qword ptr [rbp - 0x49]
00B454A3  85 C0                           test eax, eax
00B454A5  49 0F 48 F5                     cmovs rsi, r13
00B454A9  48 89 75 E7                     mov qword ptr [rbp - 0x19], rsi
00B454AD  4D 85 F6                        test r14, r14
00B454B0  74 77                           je 0x140b45529
00B454B2  48 85 FF                        test rdi, rdi
00B454B5  75 07                           jne 0x140b454be
00B454B7  48 85 F6                        test rsi, rsi
00B454BA  75 32                           jne 0x140b454ee
00B454BC  EB 6B                           jmp 0x140b45529
00B454BE  66 44 39 2F                     cmp word ptr [rdi], r13w
00B454C2  74 2A                           je 0x140b454ee
00B454C4  49 8B D6                        mov rdx, r14
00B454C7  48 8B CF                        mov rcx, rdi
00B454CA  E8 B1 AB 9B FF                  call 0x140500080
00B454CF  85 C0                           test eax, eax
00B454D1  74 18                           je 0x140b454eb
00B454D3  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B454D7  48 FF C0                        inc rax
00B454DA  66 44 39 2C 47                  cmp word ptr [rdi + rax*2], r13w
00B454DF  75 F6                           jne 0x140b454d7
00B454E1  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00B454E5  48 83 C7 02                     add rdi, 2
00B454E9  EB D3                           jmp 0x140b454be
00B454EB  88 5D 87                        mov byte ptr [rbp - 0x79], bl
00B454EE  48 85 F6                        test rsi, rsi
00B454F1  74 36                           je 0x140b45529
00B454F3  48 8B FE                        mov rdi, rsi
00B454F6  66 44 39 2F                     cmp word ptr [rdi], r13w
00B454FA  74 2D                           je 0x140b45529
00B454FC  49 8B D6                        mov rdx, r14
00B454FF  48 8B CF                        mov rcx, rdi
00B45502  E8 79 AB 9B FF                  call 0x140500080
00B45507  85 C0                           test eax, eax
00B45509  74 18                           je 0x140b45523
00B4550B  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B4550F  48 FF C0                        inc rax
00B45512  66 44 39 2C 47                  cmp word ptr [rdi + rax*2], r13w
00B45517  75 F6                           jne 0x140b4550f
00B45519  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00B4551D  48 83 C7 02                     add rdi, 2
00B45521  EB D3                           jmp 0x140b454f6
00B45523  88 5D 8A                        mov byte ptr [rbp - 0x76], bl
00B45526  44 8A FB                        mov r15b, bl
00B45529  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00B4552D  4C 8D 45 BF                     lea r8, [rbp - 0x41]
00B45531  48 8D 15 68 98 FB FF            lea rdx, [rip - 0x46798]
00B45538  E8 1B FE BE FF                  call 0x140735358
00B4553D  48 8B 7D BF                     mov rdi, qword ptr [rbp - 0x41]
00B45541  4C 8D 45 C7                     lea r8, [rbp - 0x39]
00B45545  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00B45549  48 8D 15 70 98 FB FF            lea rdx, [rip - 0x46790]
00B45550  85 C0                           test eax, eax
00B45552  49 0F 48 FD                     cmovs rdi, r13
00B45556  48 89 7D B7                     mov qword ptr [rbp - 0x49], rdi
00B4555A  E8 F9 FD BE FF                  call 0x140735358
00B4555F  4C 8B 6D C7                     mov r13, qword ptr [rbp - 0x39]
00B45563  33 C9                           xor ecx, ecx
00B45565  85 C0                           test eax, eax
00B45567  4C 0F 48 E9                     cmovs r13, rcx
00B4556B  48 85 FF                        test rdi, rdi
00B4556E  75 0A                           jne 0x140b4557a
00B45570  4D 85 ED                        test r13, r13
00B45573  75 07                           jne 0x140b4557c
00B45575  E9 01 01 00 00                  jmp 0x140b4567b
00B4557A  33 FF                           xor edi, edi
00B4557C  4C 8B 75 6F                     mov r14, qword ptr [rbp + 0x6f]
00B45580  41 BC 02 00 00 00               mov r12d, 2
00B45586  49 83 C6 30                     add r14, 0x30
00B4558A  4C 89 65 BF                     mov qword ptr [rbp - 0x41], r12
00B4558E  4C 89 75 C7                     mov qword ptr [rbp - 0x39], r14
00B45592  49 8B 36                        mov rsi, qword ptr [r14]
00B45595  48 85 F6                        test rsi, rsi
00B45598  0F 84 C4 00 00 00               je 0x140b45662
00B4559E  66 39 3E                        cmp word ptr [rsi], di
00B455A1  0F 84 BB 00 00 00               je 0x140b45662
00B455A7  4C 8B 65 B7                     mov r12, qword ptr [rbp - 0x49]
00B455AB  44 8A 75 88                     mov r14b, byte ptr [rbp - 0x78]
00B455AF  4D 85 E4                        test r12, r12
00B455B2  74 3F                           je 0x140b455f3
00B455B4  45 84 F6                        test r14b, r14b
00B455B7  75 3A                           jne 0x140b455f3
00B455B9  49 8B FC                        mov rdi, r12
00B455BC  33 C9                           xor ecx, ecx
00B455BE  66 39 0F                        cmp word ptr [rdi], cx
00B455C1  74 2E                           je 0x140b455f1
00B455C3  48 8B D6                        mov rdx, rsi
00B455C6  48 8B CF                        mov rcx, rdi
00B455C9  E8 B2 AA 9B FF                  call 0x140500080
00B455CE  33 C9                           xor ecx, ecx
00B455D0  85 C0                           test eax, eax
00B455D2  74 17                           je 0x140b455eb
00B455D4  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B455D8  48 FF C0                        inc rax
00B455DB  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00B455DF  75 F7                           jne 0x140b455d8
00B455E1  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00B455E5  48 83 C7 02                     add rdi, 2
00B455E9  EB D3                           jmp 0x140b455be
00B455EB  44 8A F3                        mov r14b, bl
00B455EE  88 5D 87                        mov byte ptr [rbp - 0x79], bl
00B455F1  33 FF                           xor edi, edi
00B455F3  4D 85 ED                        test r13, r13
00B455F6  74 40                           je 0x140b45638
00B455F8  40 38 7D 89                     cmp byte ptr [rbp - 0x77], dil
00B455FC  75 3A                           jne 0x140b45638
00B455FE  49 8B FD                        mov rdi, r13
00B45601  33 C9                           xor ecx, ecx
00B45603  66 39 0F                        cmp word ptr [rdi], cx
00B45606  74 2E                           je 0x140b45636
00B45608  48 8B D6                        mov rdx, rsi
00B4560B  48 8B CF                        mov rcx, rdi
00B4560E  E8 6D AA 9B FF                  call 0x140500080
00B45613  33 C9                           xor ecx, ecx
00B45615  85 C0                           test eax, eax
00B45617  74 17                           je 0x140b45630
00B45619  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B4561D  48 FF C0                        inc rax
00B45620  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00B45624  75 F7                           jne 0x140b4561d
00B45626  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00B4562A  48 83 C7 02                     add rdi, 2
00B4562E  EB D3                           jmp 0x140b45603
00B45630  88 5D 89                        mov byte ptr [rbp - 0x77], bl
00B45633  44 8A FB                        mov r15b, bl
00B45636  33 FF                           xor edi, edi
00B45638  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B4563C  48 FF C0                        inc rax
00B4563F  66 39 3C 46                     cmp word ptr [rsi + rax*2], di
00B45643  75 F7                           jne 0x140b4563c
00B45645  48 8D 34 46                     lea rsi, [rsi + rax*2]
00B45649  48 83 C6 02                     add rsi, 2
00B4564D  66 39 3E                        cmp word ptr [rsi], di
00B45650  0F 85 59 FF FF FF               jne 0x140b455af
00B45656  4C 8B 65 BF                     mov r12, qword ptr [rbp - 0x41]
00B4565A  44 88 75 88                     mov byte ptr [rbp - 0x78], r14b
00B4565E  4C 8B 75 C7                     mov r14, qword ptr [rbp - 0x39]
00B45662  49 83 C6 10                     add r14, 0x10
00B45666  4C 2B E3                        sub r12, rbx
00B45669  4C 89 75 C7                     mov qword ptr [rbp - 0x39], r14
00B4566D  4C 89 65 BF                     mov qword ptr [rbp - 0x41], r12
00B45671  0F 85 1B FF FF FF               jne 0x140b45592
00B45677  44 8B 65 AF                     mov r12d, dword ptr [rbp - 0x51]
00B4567B  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00B4567F  4C 8D 45 D7                     lea r8, [rbp - 0x29]
00B45683  48 8D 15 56 97 FB FF            lea rdx, [rip - 0x468aa]
00B4568A  E8 C9 FC BE FF                  call 0x140735358
00B4568F  4C 8B 75 D7                     mov r14, qword ptr [rbp - 0x29]
00B45693  4C 8D 45 DF                     lea r8, [rbp - 0x21]
00B45697  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00B4569B  48 8D 15 8E 95 FB FF            lea rdx, [rip - 0x46a72]
00B456A2  85 C0                           test eax, eax
00B456A4  4C 0F 48 F7                     cmovs r14, rdi
00B456A8  E8 AB FC BE FF                  call 0x140735358
00B456AD  48 8B 75 DF                     mov rsi, qword ptr [rbp - 0x21]
00B456B1  85 C0                           test eax, eax
00B456B3  48 0F 48 F7                     cmovs rsi, rdi
00B456B7  4D 85 F6                        test r14, r14
00B456BA  75 0A                           jne 0x140b456c6
00B456BC  48 85 F6                        test rsi, rsi
00B456BF  75 44                           jne 0x140b45705
00B456C1  E9 86 00 00 00                  jmp 0x140b4574c
00B456C6  49 8B FE                        mov rdi, r14
00B456C9  33 C9                           xor ecx, ecx
00B456CB  66 39 0F                        cmp word ptr [rdi], cx
00B456CE  74 33                           je 0x140b45703
00B456D0  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00B456D4  48 8B CF                        mov rcx, rdi
00B456D7  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00B456DB  E8 A0 A9 9B FF                  call 0x140500080
00B456E0  33 C9                           xor ecx, ecx
00B456E2  85 C0                           test eax, eax
00B456E4  74 17                           je 0x140b456fd
00B456E6  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B456EA  48 FF C0                        inc rax
00B456ED  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00B456F1  75 F7                           jne 0x140b456ea
00B456F3  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00B456F7  48 83 C7 02                     add rdi, 2
00B456FB  EB CE                           jmp 0x140b456cb
00B456FD  88 5D 8B                        mov byte ptr [rbp - 0x75], bl
00B45700  88 5D 87                        mov byte ptr [rbp - 0x79], bl
00B45703  33 FF                           xor edi, edi
00B45705  48 85 F6                        test rsi, rsi
00B45708  74 42                           je 0x140b4574c
00B4570A  48 8B FE                        mov rdi, rsi
00B4570D  33 C9                           xor ecx, ecx
00B4570F  66 39 0F                        cmp word ptr [rdi], cx
00B45712  74 36                           je 0x140b4574a
00B45714  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00B45718  48 8B CF                        mov rcx, rdi
00B4571B  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00B4571F  E8 5C A9 9B FF                  call 0x140500080
00B45724  33 C9                           xor ecx, ecx
00B45726  85 C0                           test eax, eax
00B45728  74 17                           je 0x140b45741
00B4572A  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B4572E  48 FF C0                        inc rax
00B45731  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00B45735  75 F7                           jne 0x140b4572e
00B45737  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00B4573B  48 83 C7 02                     add rdi, 2
00B4573F  EB CE                           jmp 0x140b4570f
00B45741  8A C3                           mov al, bl
00B45743  44 8A FB                        mov r15b, bl
00B45746  33 FF                           xor edi, edi
00B45748  EB 60                           jmp 0x140b457aa
00B4574A  33 FF                           xor edi, edi
00B4574C  45 84 FF                        test r15b, r15b
00B4574F  75 56                           jne 0x140b457a7
00B45751  40 38 7D 87                     cmp byte ptr [rbp - 0x79], dil
00B45755  0F 85 95 00 00 00               jne 0x140b457f0
00B4575B  45 84 E4                        test r12b, r12b
00B4575E  0F 85 8C 00 00 00               jne 0x140b457f0
00B45764  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00B45768  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
00B4576C  48 8D 15 DD 94 FB FF            lea rdx, [rip - 0x46b23]
00B45773  E8 70 FB BE FF                  call 0x1407352e8
00B45778  85 C0                           test eax, eax
00B4577A  78 74                           js 0x140b457f0
00B4577C  40 38 7D 7F                     cmp byte ptr [rbp + 0x7f], dil
00B45780  74 6E                           je 0x140b457f0
00B45782  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00B45786  48 39 7D 77                     cmp qword ptr [rbp + 0x77], rdi
00B4578A  75 05                           jne 0x140b45791
00B4578C  48 85 C9                        test rcx, rcx
00B4578F  75 12                           jne 0x140b457a3
00B45791  40 38 3D AD 0A 32 00            cmp byte ptr [rip + 0x320aad], dil
00B45798  74 62                           je 0x140b457fc
00B4579A  40 38 3D D9 0A 32 00            cmp byte ptr [rip + 0x320ad9], dil
00B457A1  74 59                           je 0x140b457fc
00B457A3  8B DF                           mov ebx, edi
00B457A5  EB 5A                           jmp 0x140b45801
00B457A7  8A 45 8C                        mov al, byte ptr [rbp - 0x74]
00B457AA  45 84 E4                        test r12b, r12b
00B457AD  74 49                           je 0x140b457f8
00B457AF  40 38 7D 87                     cmp byte ptr [rbp - 0x79], dil
00B457B3  74 43                           je 0x140b457f8
00B457B5  45 84 FF                        test r15b, r15b
00B457B8  74 36                           je 0x140b457f0
00B457BA  84 C0                           test al, al
00B457BC  74 04                           je 0x140b457c2
00B457BE  8B DF                           mov ebx, edi
00B457C0  EB 0E                           jmp 0x140b457d0
00B457C2  40 38 7D 89                     cmp byte ptr [rbp - 0x77], dil
00B457C6  75 08                           jne 0x140b457d0
00B457C8  F6 5D 8A                        neg byte ptr [rbp - 0x76]
00B457CB  1B C0                           sbb eax, eax
00B457CD  8D 58 03                        lea ebx, [rax + 3]
00B457D0  40 38 7D 8B                     cmp byte ptr [rbp - 0x75], dil
00B457D4  74 04                           je 0x140b457da
00B457D6  8B C7                           mov eax, edi
00B457D8  EB 08                           jmp 0x140b457e2
00B457DA  F6 5D 88                        neg byte ptr [rbp - 0x78]
00B457DD  1B C0                           sbb eax, eax
00B457DF  83 C0 02                        add eax, 2
00B457E2  3B C3                           cmp eax, ebx
00B457E4  1B DB                           sbb ebx, ebx
00B457E6  F7 D3                           not ebx
00B457E8  81 E3 61 03 00 C0               and ebx, 0xc0000361
00B457EE  EB 02                           jmp 0x140b457f2
00B457F0  8B DF                           mov ebx, edi
00B457F2  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00B457F6  EB 09                           jmp 0x140b45801
00B457F8  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00B457FC  BB 61 03 00 C0                  mov ebx, 0xc0000361
00B45801  48 85 C9                        test rcx, rcx
00B45804  74 07                           je 0x140b4580d
00B45806  33 D2                           xor edx, edx
00B45808  E8 63 D0 03 00                  call 0x140b82870
00B4580D  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00B45811  48 85 C9                        test rcx, rcx
00B45814  74 07                           je 0x140b4581d
00B45816  33 D2                           xor edx, edx
00B45818  E8 53 D0 03 00                  call 0x140b82870
00B4581D  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00B45821  48 85 C9                        test rcx, rcx
00B45824  74 07                           je 0x140b4582d
00B45826  33 D2                           xor edx, edx
00B45828  E8 43 D0 03 00                  call 0x140b82870
00B4582D  4D 85 ED                        test r13, r13
00B45830  74 0A                           je 0x140b4583c
00B45832  33 D2                           xor edx, edx
00B45834  49 8B CD                        mov rcx, r13
00B45837  E8 34 D0 03 00                  call 0x140b82870
00B4583C  4D 85 F6                        test r14, r14
00B4583F  74 0A                           je 0x140b4584b
00B45841  33 D2                           xor edx, edx
00B45843  49 8B CE                        mov rcx, r14
00B45846  E8 25 D0 03 00                  call 0x140b82870
00B4584B  48 85 F6                        test rsi, rsi
00B4584E  0F 84 AF 3C F4 FF               je 0x140a89503
00B45854  33 D2                           xor edx, edx
00B45856  48 8B CE                        mov rcx, rsi
00B45859  E8 12 D0 03 00                  call 0x140b82870
00B4585E  90                              nop
00B4585F  E9 9F 3C F4 FF                  jmp 0x140a89503
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B453C2(void)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;

    *(unsigned __int64 *)(v_rbp - 89) = v_rip - 289165;
    *(unsigned int *)(v_rbp - 97) = 0x1A0018ULL;
    result = IopOpenRegistryKeyEx(v_rbp - 113, *(unsigned __int64 *)(v_rbp - 49), v_rbp - 97, (unsigned int)((unsigned int)(v_rbx)));
    *(unsigned int *)(v_rbp - 81) = (unsigned int)((unsigned __int8)(v_r13));
    *(unsigned __int8 *)(v_rbp - 121) = (unsigned __int8)(v_r13);
    *(unsigned __int8 *)(v_rbp - 118) = (unsigned __int8)(v_r13);
    *(unsigned __int8 *)(v_rbp - 119) = (unsigned __int8)(v_r13);
    *(unsigned __int8 *)(v_rbp - 120) = (unsigned __int8)(v_r13);
    *(unsigned __int8 *)(v_rbp - 116) = (unsigned __int8)(v_r13);
    *(unsigned __int8 *)(v_rbp - 117) = (unsigned __int8)(v_r13);
    result = PiDevCfgQueryPolicyEnabled(*(unsigned __int64 *)(v_rbp - 113), v_rip - 289190, v_rbp + 127, (unsigned int)((unsigned int)(v_rbx)));
    v_r12 = (unsigned __int8)(v_r13);
    if (!(sign_flag)) {
        v_r12 = (unsigned __int8)(v_r13);
        if ((*(unsigned __int8 *)(v_rbp + 127)) != ((unsigned __int8)(v_r13))) { v_r12 = 1; }
        *(unsigned int *)(v_rbp - 81) = (unsigned int)(v_r12);
    }
    result = PiDevCfgQueryPolicyEnabled(*(unsigned __int64 *)(v_rbp - 113), v_rip - 289215, v_rbp + 127, (unsigned int)((unsigned int)(v_rbx)));
    if (sign_flag) goto loc_00B45469;
    v_r15 = (unsigned __int8)(v_r13);
    if ((*(unsigned __int8 *)(v_rbp + 127)) != ((unsigned __int8)(v_r13))) {
        v_r15 = (unsigned __int8)(v_r13);
        if (((*(unsigned __int8 *)(v_rdi + 560)) & (16)) != 0) { v_r15 = 1; }
    }
    result = PiDevCfgQueryPolicyStringList(*(unsigned __int64 *)(v_rbp - 113), v_rip - 289208, v_rbp - 105, (unsigned int)((unsigned int)(v_rbx)));
    v_rdi = *(unsigned __int64 *)(v_rbp - 105);
    if (sign_flag) { v_rdi = v_r13; }
    *(unsigned __int64 *)(v_rbp - 105) = v_rdi;
    result = PiDevCfgQueryPolicyStringList(*(unsigned __int64 *)(v_rbp - 113), v_rip - 288544, v_rbp - 73, (unsigned int)((unsigned int)(v_rbx)));
    v_rsi = *(unsigned __int64 *)(v_rbp - 73);
    if (sign_flag) { v_rsi = v_r13; }
    *(unsigned __int64 *)(v_rbp - 25) = v_rsi;
    if (v_r14 == 0) goto loc_00B45529;
    if (v_rdi != 0) goto loc_00B454BE;
    if (v_rsi != 0) goto loc_00B454EE;
    goto loc_00B45529;
loc_00B454BE:
    if ((*(unsigned __int16 *)(v_rdi)) == ((unsigned __int16)(v_r13))) goto loc_00B454EE;
    result = wcsicmp(v_rdi, v_r14, v_rbp - 73, (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) == 0) goto loc_00B454EB;
    result = (result) | (-1);
loc_00B454D7:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rdi + result * 2)) != ((unsigned __int16)(v_r13))) goto loc_00B454D7;
    v_rdi = (v_rdi + result * 2) + (2);
    goto loc_00B454BE;
loc_00B454EB:
    *(unsigned __int8 *)(v_rbp - 121) = 1;
loc_00B454EE:
    if (v_rsi == 0) goto loc_00B45529;
loc_00B454F6:
    if ((*(unsigned __int16 *)(v_rsi)) == ((unsigned __int16)(v_r13))) goto loc_00B45529;
    result = wcsicmp(v_rsi, v_r14, v_rbp - 73, (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) == 0) goto loc_00B45523;
    result = (result) | (-1);
loc_00B4550F:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rsi + result * 2)) != ((unsigned __int16)(v_r13))) goto loc_00B4550F;
    v_rdi = (v_rsi + result * 2) + (2);
    goto loc_00B454F6;
loc_00B45523:
    *(unsigned __int8 *)(v_rbp - 118) = 1;
loc_00B45529:
    result = PiDevCfgQueryPolicyStringList(*(unsigned __int64 *)(v_rbp - 113), v_rip - 288664, v_rbp - 65, (unsigned int)((unsigned int)(v_rbx)));
    v_rdi = *(unsigned __int64 *)(v_rbp - 65);
    if (sign_flag) { v_rdi = v_r13; }
    *(unsigned __int64 *)(v_rbp - 73) = v_rdi;
    result = PiDevCfgQueryPolicyStringList(*(unsigned __int64 *)(v_rbp - 113), v_rip - 288656, v_rbp - 57, (unsigned int)((unsigned int)(v_rbx)));
    a1 = 0;
    v_r13 = *(unsigned __int64 *)(v_rbp - 57);
    if (sign_flag) { v_r13 = 0; }
    if (v_rdi != 0) goto loc_00B4557A;
    if (v_r13 != 0) goto loc_00B4557C;
    goto loc_00B4567B;
loc_00B4557A:
    v_rdi = 0;
loc_00B4557C:
    v_r14 = (*(unsigned __int64 *)(v_rbp + 111)) + (48);
    *(unsigned __int64 *)(v_rbp - 65) = 2;
    *(unsigned __int64 *)(v_rbp - 57) = v_r14;
loc_00B45592:
    if (*(unsigned __int64 *)(v_r14) == 0) goto loc_00B45662;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14))) == 0) goto loc_00B45662;
loc_00B455AF:
    if (*(unsigned __int64 *)(v_rbp - 73) == 0) goto loc_00B455F3;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbp - 120)) != 0) goto loc_00B455F3;
    a1 = 0;
loc_00B455BE:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 73))) == 0) goto loc_00B455F1;
    result = wcsicmp(*(unsigned __int64 *)(v_rbp - 73), *(unsigned __int64 *)(v_r14), v_rbp - 57, (unsigned int)((unsigned int)(v_rbx)));
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00B455EB;
    result = (result) | (-1);
loc_00B455D8:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 73) + result * 2)) != 0) goto loc_00B455D8;
    v_rdi = (*(unsigned __int64 *)(v_rbp - 73) + result * 2) + (2);
    goto loc_00B455BE;
loc_00B455EB:
    *(unsigned __int8 *)(v_rbp - 121) = 1;
loc_00B455F1:
    v_rdi = 0;
loc_00B455F3:
    if (v_r13 == 0) goto loc_00B45638;
    if ((*(unsigned __int8 *)(v_rbp - 119)) != 0) goto loc_00B45638;
    a1 = 0;
loc_00B45603:
    if ((*(unsigned __int16 *)(v_r13)) == 0) goto loc_00B45636;
    result = wcsicmp(v_r13, *(unsigned __int64 *)(v_r14), v_rbp - 57, (unsigned int)((unsigned int)(v_rbx)));
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00B45630;
    result = (result) | (-1);
loc_00B4561D:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_r13 + result * 2)) != 0) goto loc_00B4561D;
    v_rdi = (v_r13 + result * 2) + (2);
    goto loc_00B45603;
loc_00B45630:
    *(unsigned __int8 *)(v_rbp - 119) = 1;
loc_00B45636:
    v_rdi = 0;
loc_00B45638:
    result = (result) | (-1);
loc_00B4563C:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14) + result * 2)) != 0) goto loc_00B4563C;
    v_rsi = (*(unsigned __int64 *)(v_r14) + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_rsi)) != 0) goto loc_00B455AF;
    *(unsigned __int8 *)(v_rbp - 120) = 1;
loc_00B45662:
    v_r14 = (*(unsigned __int64 *)(v_rbp - 57)) + (16);
    v_r12 = (*(unsigned __int64 *)(v_rbp - 65)) - (1);
    *(unsigned __int64 *)(v_rbp - 57) = v_r14;
    *(unsigned __int64 *)(v_rbp - 65) = v_r12;
    if (condition_is_not_equal) goto loc_00B45592;
loc_00B4567B:
    result = PiDevCfgQueryPolicyStringList(*(unsigned __int64 *)(v_rbp - 113), v_rip - 288938, v_rbp - 41, (unsigned int)((unsigned int)(v_rbx)));
    v_r14 = *(unsigned __int64 *)(v_rbp - 41);
    if (sign_flag) { v_r14 = 0; }
    result = PiDevCfgQueryPolicyStringList(*(unsigned __int64 *)(v_rbp - 113), v_rip - 289394, v_rbp - 33, (unsigned int)((unsigned int)(v_rbx)));
    v_rsi = *(unsigned __int64 *)(v_rbp - 33);
    if (sign_flag) { v_rsi = 0; }
    if (v_r14 != 0) goto loc_00B456C6;
    if (v_rsi != 0) goto loc_00B45705;
    goto loc_00B4574C;
loc_00B456C6:
    a1 = 0;
loc_00B456CB:
    if ((*(unsigned __int16 *)(v_r14)) == 0) goto loc_00B45703;
    result = wcsicmp(v_r14, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 111) + 8), v_rbp - 33, (unsigned int)((unsigned int)(v_rbx)));
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00B456FD;
    result = (result) | (-1);
loc_00B456EA:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_r14 + result * 2)) != 0) goto loc_00B456EA;
    v_rdi = (v_r14 + result * 2) + (2);
    goto loc_00B456CB;
loc_00B456FD:
    *(unsigned __int8 *)(v_rbp - 117) = 1;
    *(unsigned __int8 *)(v_rbp - 121) = 1;
loc_00B45703:
    v_rdi = 0;
loc_00B45705:
    if (v_rsi == 0) goto loc_00B4574C;
    a1 = 0;
loc_00B4570F:
    if ((*(unsigned __int16 *)(v_rsi)) == 0) goto loc_00B4574A;
    result = wcsicmp(v_rsi, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 111) + 8), v_rbp - 33, (unsigned int)((unsigned int)(v_rbx)));
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00B45741;
    result = (result) | (-1);
loc_00B4572E:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rsi + result * 2)) != 0) goto loc_00B4572E;
    v_rdi = (v_rsi + result * 2) + (2);
    goto loc_00B4570F;
loc_00B45741:
    v_rdi = 0;
    goto loc_00B457AA;
loc_00B4574A:
    v_rdi = 0;
loc_00B4574C:
    if (1 != 0) goto loc_00B457A7;
    if ((*(unsigned __int8 *)(v_rbp - 121)) != 0) goto loc_00B457F0;
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp - 81))) != 0) goto loc_00B457F0;
    result = PiDevCfgQueryPolicyEnabled(*(unsigned __int64 *)(v_rbp - 113), v_rip - 289571, v_rbp + 127, (unsigned int)((unsigned int)(v_rbx)));
    if (sign_flag) goto loc_00B457F0;
    if ((*(unsigned __int8 *)(v_rbp + 127)) == 0) goto loc_00B457F0;
    if ((*(unsigned __int64 *)(v_rbp + 119)) != 0) goto loc_00B45791;
    if (*(unsigned __int64 *)(v_rbp - 105) != 0) goto loc_00B457A3;
loc_00B45791:
    if ((*(unsigned __int8 *)(v_rip + 3279533)) == 0) goto loc_00B457FC;
    if ((*(unsigned __int8 *)(v_rip + 3279577)) == 0) goto loc_00B457FC;
loc_00B457A3:
    goto loc_00B45801;
loc_00B457A7:
loc_00B457AA:
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbp - 81))) == 0) goto loc_00B457F8;
    if ((*(unsigned __int8 *)(v_rbp - 121)) == 0) goto loc_00B457F8;
    if (1 == 0) goto loc_00B457F0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbp - 116)) == 0) goto loc_00B457C2;
    goto loc_00B457D0;
loc_00B457C2:
    v_rbx = 0;
    if ((*(unsigned __int8 *)(v_rbp - 119)) == 0) {
        v_rbx = *(unsigned __int8 *)(v_rbp - 116) + 3;
    }
    if ((*(unsigned __int8 *)(v_rbp - 117)) == 0) goto loc_00B457DA;
    goto loc_00B457E2;
loc_00B457DA:
    result = (unsigned int)((0) + (2));
loc_00B457E2:
    v_rbx = (unsigned int)(~(v_rbx));
    v_rbx = (unsigned int)((v_rbx) & (0xC0000361ULL));
    goto loc_00B457F2;
loc_00B457F0:
loc_00B457F2:
    goto loc_00B45801;
loc_00B457F8:
loc_00B457FC:
loc_00B45801:
    if (*(unsigned __int64 *)(v_rbp - 105) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rbp - 105), a2, v_rbp + 127, (unsigned int)((unsigned int)(v_rbx)));
    }
    if (*(unsigned __int64 *)(v_rbp - 25) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rbp - 25), a2, v_rbp + 127, (unsigned int)((unsigned int)(v_rbx)));
    }
    if (*(unsigned __int64 *)(v_rbp - 73) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rbp - 73), a2, v_rbp + 127, (unsigned int)((unsigned int)(v_rbx)));
    }
    if (v_r13 != 0) {
        a2 = 0;
        a1 = v_r13;
        result = ExFreePoolWithTag(a1, a2, v_rbp + 127, (unsigned int)((unsigned int)(v_rbx)));
    }
    if (v_r14 != 0) {
        a2 = 0;
        a1 = v_r14;
        result = ExFreePoolWithTag(a1, a2, v_rbp + 127, (unsigned int)((unsigned int)(v_rbx)));
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_rsi, a2, v_rbp + 127, (unsigned int)((unsigned int)(v_rbx)));
}
```

## 5. (Beta) C Style

```c
void sub_00B453C2(void)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;

    *(uint64_t *)(local_rbp - 0x59) = v_rip - 289165;
    *(uint32_t *)(local_rbp - 0x61) = 0x1A0018ULL;
    result = IopOpenRegistryKeyEx(local_rbp - 113, *(uint64_t *)(local_rbp - 0x31), local_rbp - 97, (uint32_t)((uint32_t)(local_rbx)));
    *(uint32_t *)(local_rbp - 0x51) = (uint32_t)((uint8_t)(local_r13));
    *(uint8_t *)(local_rbp - 0x79) = (uint8_t)(local_r13);
    *(uint8_t *)(local_rbp - 0x76) = (uint8_t)(local_r13);
    *(uint8_t *)(local_rbp - 0x77) = (uint8_t)(local_r13);
    *(uint8_t *)(local_rbp - 0x78) = (uint8_t)(local_r13);
    *(uint8_t *)(local_rbp - 0x74) = (uint8_t)(local_r13);
    *(uint8_t *)(local_rbp - 0x75) = (uint8_t)(local_r13);
    result = PiDevCfgQueryPolicyEnabled(*(uint64_t *)(local_rbp - 0x71), v_rip - 289190, local_rbp + 127, (uint32_t)((uint32_t)(local_rbx)));
    local_r12 = (uint8_t)(local_r13);
    if (!(sign_flag)) {
        local_r12 = (uint8_t)(local_r13);
        if ((*(uint8_t *)(local_rbp + 0x7F)) != ((uint8_t)(local_r13))) { local_r12 = 1; }
        *(uint32_t *)(local_rbp - 0x51) = (uint32_t)(local_r12);
    }
    result = PiDevCfgQueryPolicyEnabled(*(uint64_t *)(local_rbp - 0x71), v_rip - 289215, local_rbp + 127, (uint32_t)((uint32_t)(local_rbx)));
    if (sign_flag) goto loc_00B45469;
    local_r15 = (uint8_t)(local_r13);
    if ((*(uint8_t *)(local_rbp + 0x7F)) != ((uint8_t)(local_r13))) {
        local_r15 = (uint8_t)(local_r13);
        if (((*(uint8_t *)(local_rdi + 0x230)) & (16)) != 0) { local_r15 = 1; }
    }
    result = PiDevCfgQueryPolicyStringList(*(uint64_t *)(local_rbp - 0x71), v_rip - 289208, local_rbp - 105, (uint32_t)((uint32_t)(local_rbx)));
    local_rdi = *(uint64_t *)(local_rbp - 0x69);
    if (sign_flag) { local_rdi = local_r13; }
    *(uint64_t *)(local_rbp - 0x69) = local_rdi;
    result = PiDevCfgQueryPolicyStringList(*(uint64_t *)(local_rbp - 0x71), v_rip - 288544, local_rbp - 73, (uint32_t)((uint32_t)(local_rbx)));
    local_rsi = *(uint64_t *)(local_rbp - 0x49);
    if (sign_flag) { local_rsi = local_r13; }
    *(uint64_t *)(local_rbp - 0x19) = local_rsi;
    if (local_r14 == 0) goto loc_00B45529;
    if (local_rdi != 0) goto loc_00B454BE;
    if (local_rsi != 0) goto loc_00B454EE;
    goto loc_00B45529;
loc_00B454BE:
    if ((*(uint16_t *)(local_rdi)) == ((uint16_t)(local_r13))) goto loc_00B454EE;
    result = wcsicmp(local_rdi, local_r14, local_rbp - 73, (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) == 0) goto loc_00B454EB;
    result = (result) | (-1);
loc_00B454D7:
    result = (result) + 1;
    if ((*(uint16_t *)(local_rdi + result * 2)) != ((uint16_t)(local_r13))) goto loc_00B454D7;
    local_rdi = (local_rdi + result * 2) + (2);
    goto loc_00B454BE;
loc_00B454EB:
    *(uint8_t *)(local_rbp - 0x79) = 1;
loc_00B454EE:
    if (local_rsi == 0) goto loc_00B45529;
loc_00B454F6:
    if ((*(uint16_t *)(local_rsi)) == ((uint16_t)(local_r13))) goto loc_00B45529;
    result = wcsicmp(local_rsi, local_r14, local_rbp - 73, (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) == 0) goto loc_00B45523;
    result = (result) | (-1);
loc_00B4550F:
    result = (result) + 1;
    if ((*(uint16_t *)(local_rsi + result * 2)) != ((uint16_t)(local_r13))) goto loc_00B4550F;
    local_rdi = (local_rsi + result * 2) + (2);
    goto loc_00B454F6;
loc_00B45523:
    *(uint8_t *)(local_rbp - 0x76) = 1;
loc_00B45529:
    result = PiDevCfgQueryPolicyStringList(*(uint64_t *)(local_rbp - 0x71), v_rip - 288664, local_rbp - 65, (uint32_t)((uint32_t)(local_rbx)));
    local_rdi = *(uint64_t *)(local_rbp - 0x41);
    if (sign_flag) { local_rdi = local_r13; }
    *(uint64_t *)(local_rbp - 0x49) = local_rdi;
    result = PiDevCfgQueryPolicyStringList(*(uint64_t *)(local_rbp - 0x71), v_rip - 288656, local_rbp - 57, (uint32_t)((uint32_t)(local_rbx)));
    a1 = 0;
    local_r13 = *(uint64_t *)(local_rbp - 0x39);
    if (sign_flag) { local_r13 = 0; }
    if (local_rdi != 0) goto loc_00B4557A;
    if (local_r13 != 0) goto loc_00B4557C;
    goto loc_00B4567B;
loc_00B4557A:
    local_rdi = 0;
loc_00B4557C:
    local_r14 = (*(uint64_t *)(local_rbp + 0x6F)) + (48);
    *(uint64_t *)(local_rbp - 0x41) = 2;
    *(uint64_t *)(local_rbp - 0x39) = local_r14;
loc_00B45592:
    if (*(uint64_t *)(local_r14) == 0) goto loc_00B45662;
    if ((*(uint16_t *)(*(uint64_t *)(local_r14))) == 0) goto loc_00B45662;
loc_00B455AF:
    if (*(uint64_t *)(local_rbp - 0x49) == 0) goto loc_00B455F3;
    if ((uint8_t)(*(uint8_t *)(local_rbp - 0x78)) != 0) goto loc_00B455F3;
    a1 = 0;
loc_00B455BE:
    if ((*(uint16_t *)(*(uint64_t *)(local_rbp - 0x49))) == 0) goto loc_00B455F1;
    result = wcsicmp(*(uint64_t *)(local_rbp - 0x49), *(uint64_t *)(local_r14), local_rbp - 57, (uint32_t)((uint32_t)(local_rbx)));
    a1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00B455EB;
    result = (result) | (-1);
loc_00B455D8:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_rbp - 0x49) + result * 2)) != 0) goto loc_00B455D8;
    local_rdi = (*(uint64_t *)(local_rbp - 0x49) + result * 2) + (2);
    goto loc_00B455BE;
loc_00B455EB:
    *(uint8_t *)(local_rbp - 0x79) = 1;
loc_00B455F1:
    local_rdi = 0;
loc_00B455F3:
    if (local_r13 == 0) goto loc_00B45638;
    if ((*(uint8_t *)(local_rbp - 0x77)) != 0) goto loc_00B45638;
    a1 = 0;
loc_00B45603:
    if ((*(uint16_t *)(local_r13)) == 0) goto loc_00B45636;
    result = wcsicmp(local_r13, *(uint64_t *)(local_r14), local_rbp - 57, (uint32_t)((uint32_t)(local_rbx)));
    a1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00B45630;
    result = (result) | (-1);
loc_00B4561D:
    result = (result) + 1;
    if ((*(uint16_t *)(local_r13 + result * 2)) != 0) goto loc_00B4561D;
    local_rdi = (local_r13 + result * 2) + (2);
    goto loc_00B45603;
loc_00B45630:
    *(uint8_t *)(local_rbp - 0x77) = 1;
loc_00B45636:
    local_rdi = 0;
loc_00B45638:
    result = (result) | (-1);
loc_00B4563C:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_r14) + result * 2)) != 0) goto loc_00B4563C;
    local_rsi = (*(uint64_t *)(local_r14) + result * 2) + (2);
    if ((*(uint16_t *)(local_rsi)) != 0) goto loc_00B455AF;
    *(uint8_t *)(local_rbp - 0x78) = 1;
loc_00B45662:
    local_r14 = (*(uint64_t *)(local_rbp - 0x39)) + (16);
    local_r12 = (*(uint64_t *)(local_rbp - 0x41)) - (1);
    *(uint64_t *)(local_rbp - 0x39) = local_r14;
    *(uint64_t *)(local_rbp - 0x41) = local_r12;
    if (condition_is_not_equal) goto loc_00B45592;
loc_00B4567B:
    result = PiDevCfgQueryPolicyStringList(*(uint64_t *)(local_rbp - 0x71), v_rip - 288938, local_rbp - 41, (uint32_t)((uint32_t)(local_rbx)));
    local_r14 = *(uint64_t *)(local_rbp - 0x29);
    if (sign_flag) { local_r14 = 0; }
    result = PiDevCfgQueryPolicyStringList(*(uint64_t *)(local_rbp - 0x71), v_rip - 289394, local_rbp - 33, (uint32_t)((uint32_t)(local_rbx)));
    local_rsi = *(uint64_t *)(local_rbp - 0x21);
    if (sign_flag) { local_rsi = 0; }
    if (local_r14 != 0) goto loc_00B456C6;
    if (local_rsi != 0) goto loc_00B45705;
    goto loc_00B4574C;
loc_00B456C6:
    a1 = 0;
loc_00B456CB:
    if ((*(uint16_t *)(local_r14)) == 0) goto loc_00B45703;
    result = wcsicmp(local_r14, *(uint64_t *)(*(uint64_t *)(local_rbp + 0x6F) + 0x8), local_rbp - 33, (uint32_t)((uint32_t)(local_rbx)));
    a1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00B456FD;
    result = (result) | (-1);
loc_00B456EA:
    result = (result) + 1;
    if ((*(uint16_t *)(local_r14 + result * 2)) != 0) goto loc_00B456EA;
    local_rdi = (local_r14 + result * 2) + (2);
    goto loc_00B456CB;
loc_00B456FD:
    *(uint8_t *)(local_rbp - 0x75) = 1;
    *(uint8_t *)(local_rbp - 0x79) = 1;
loc_00B45703:
    local_rdi = 0;
loc_00B45705:
    if (local_rsi == 0) goto loc_00B4574C;
    a1 = 0;
loc_00B4570F:
    if ((*(uint16_t *)(local_rsi)) == 0) goto loc_00B4574A;
    result = wcsicmp(local_rsi, *(uint64_t *)(*(uint64_t *)(local_rbp + 0x6F) + 0x8), local_rbp - 33, (uint32_t)((uint32_t)(local_rbx)));
    a1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00B45741;
    result = (result) | (-1);
loc_00B4572E:
    result = (result) + 1;
    if ((*(uint16_t *)(local_rsi + result * 2)) != 0) goto loc_00B4572E;
    local_rdi = (local_rsi + result * 2) + (2);
    goto loc_00B4570F;
loc_00B45741:
    local_rdi = 0;
    goto loc_00B457AA;
loc_00B4574A:
    local_rdi = 0;
loc_00B4574C:
    if (1 != 0) goto loc_00B457A7;
    if ((*(uint8_t *)(local_rbp - 0x79)) != 0) goto loc_00B457F0;
    if ((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x51))) != 0) goto loc_00B457F0;
    result = PiDevCfgQueryPolicyEnabled(*(uint64_t *)(local_rbp - 0x71), v_rip - 289571, local_rbp + 127, (uint32_t)((uint32_t)(local_rbx)));
    if (sign_flag) goto loc_00B457F0;
    if ((*(uint8_t *)(local_rbp + 0x7F)) == 0) goto loc_00B457F0;
    if ((*(uint64_t *)(local_rbp + 0x77)) != 0) goto loc_00B45791;
    if (*(uint64_t *)(local_rbp - 0x69) != 0) goto loc_00B457A3;
loc_00B45791:
    if ((*(uint8_t *)(v_rip + 0x320AAD)) == 0) goto loc_00B457FC;
    if ((*(uint8_t *)(v_rip + 0x320AD9)) == 0) goto loc_00B457FC;
loc_00B457A3:
    goto loc_00B45801;
loc_00B457A7:
loc_00B457AA:
    if ((uint8_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x51))) == 0) goto loc_00B457F8;
    if ((*(uint8_t *)(local_rbp - 0x79)) == 0) goto loc_00B457F8;
    if (1 == 0) goto loc_00B457F0;
    if ((uint8_t)(*(uint8_t *)(local_rbp - 0x74)) == 0) goto loc_00B457C2;
    goto loc_00B457D0;
loc_00B457C2:
    local_rbx = 0;
    if ((*(uint8_t *)(local_rbp - 0x77)) == 0) {
        local_rbx = *(uint8_t *)(local_rbp - 0x74) + 3;
    }
    if ((*(uint8_t *)(local_rbp - 0x75)) == 0) goto loc_00B457DA;
    goto loc_00B457E2;
loc_00B457DA:
    result = (uint32_t)((0) + (2));
loc_00B457E2:
    local_rbx = (uint32_t)(~(local_rbx));
    local_rbx = (uint32_t)((local_rbx) & (0xC0000361ULL));
    goto loc_00B457F2;
loc_00B457F0:
loc_00B457F2:
    goto loc_00B45801;
loc_00B457F8:
loc_00B457FC:
loc_00B45801:
    if (*(uint64_t *)(local_rbp - 0x69) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_rbp - 0x69), a2, local_rbp + 127, (uint32_t)((uint32_t)(local_rbx)));
    }
    if (*(uint64_t *)(local_rbp - 0x19) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_rbp - 0x19), a2, local_rbp + 127, (uint32_t)((uint32_t)(local_rbx)));
    }
    if (*(uint64_t *)(local_rbp - 0x49) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_rbp - 0x49), a2, local_rbp + 127, (uint32_t)((uint32_t)(local_rbx)));
    }
    if (local_r13 != 0) {
        a2 = 0;
        a1 = local_r13;
        result = ExFreePoolWithTag(a1, a2, local_rbp + 127, (uint32_t)((uint32_t)(local_rbx)));
    }
    if (local_r14 != 0) {
        a2 = 0;
        a1 = local_r14;
        result = ExFreePoolWithTag(a1, a2, local_rbp + 127, (uint32_t)((uint32_t)(local_rbx)));
    }
    a2 = 0;
    result = ExFreePoolWithTag(local_rsi, a2, local_rbp + 127, (uint32_t)((uint32_t)(local_rbx)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B453C2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
