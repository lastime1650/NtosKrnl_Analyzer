# FsRtlPrivateFastUnlockAll

- RVA: `0x003FD554`–`0x003FD8D4` (길이 `896` bytes)
- VA: `0x00000001403FD554`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00099A1C`
- 디코드: `224`개 명령, `896/896` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x003FD594` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x003FD5B3` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x003FD5C7` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003FD5FF` → [RtlRealSuccessor](../38/RtlRealSuccessor_function_0038DF40.md) (function, `0x0038DF40`)
- `0x003FD6BF` → [FsRtlPrivateCheckWaitingLocks](../38/FsRtlPrivateCheckWaitingLocks_function_0038DCBC.md) (function, `0x0038DCBC`)
- `0x003FD6C7` → [FsRtlPrivateResetLowestLockOffset](../38/FsRtlPrivateResetLowestLockOffset_function_0038D954.md) (function, `0x0038D954`)
- `0x003FD6D2` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x003FD74A` → [RtlDelete](../38/RtlDelete_function_0038D8B0.md) (function, `0x0038D8B0`)
- `0x003FD75E` → [ExFreeToNPagedLookasideList](../38/ExFreeToNPagedLookasideList_function_0038D9D0.md) (function, `0x0038D9D0`)
- `0x003FD77E` → [ExFreeToNPagedLookasideList](../38/ExFreeToNPagedLookasideList_function_0038D9D0.md) (function, `0x0038D9D0`)
- `0x003FD7A0` → [FsRtlSplitLocks](FsRtlSplitLocks_function_003FD8DC.md) (function, `0x003FD8DC`)
- `0x003FD7FF` → [RtlRealSuccessor](../38/RtlRealSuccessor_function_0038DF40.md) (function, `0x0038DF40`)
- `0x003FD835` → [RtlDelete](../38/RtlDelete_function_0038D8B0.md) (function, `0x0038D8B0`)
- `0x003FD84F` → [ExFreeToNPagedLookasideList](../38/ExFreeToNPagedLookasideList_function_0038D9D0.md) (function, `0x0038D9D0`)
- `0x003FD864` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x003FD879` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x003FD881` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x003FD89E` → [IoGetRequestorProcess](IoGetRequestorProcess_function_003FD4E0.md) (function, `0x003FD4E0`)

### Direct callers
- [FsRtlProcessFileLock](FsRtlProcessFileLock_function_003FD0E0.md) at `0x003FD224`
- [FsRtlFastUnlockAll](FsRtlFastUnlockAll_function_003FD530.md) at `0x003FD541`
- [FsRtlFastUnlockAllByKey](../58/FsRtlFastUnlockAllByKey_function_00581820.md) at `0x00581833`
- [sub_006EBCF4](../6E/Unknown_function_006EBCF4.md) at `0x006EBD11`

### Static image references
- `0x003FD5B8` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003FD757` → RVA `0x00E11F80` (`.data`; read)
- `0x003FD777` → RVA `0x00E12200` (`.data`; read)
- `0x003FD848` → RVA `0x00E12180` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x003FD674` → [sub_006EBD42](../6E/Unknown_function_006EBD42.md) (`tail-transfer`)
  - `0x003FD896` → [sub_006EBD42 + 0x72](../6E/Unknown_function_006EBD42.md) (`tail-transfer`)
  - `0x003FD8B9` → [sub_006EBD42 + 0x7C](../6E/Unknown_function_006EBD42.md) (`tail-transfer`)
  - `0x003FD8CF` → [sub_006EBD42 + 0x7C](../6E/Unknown_function_006EBD42.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003FD554  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
003FD559  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
003FD55E  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
003FD563  53                              push rbx
003FD564  55                              push rbp
003FD565  56                              push rsi
003FD566  57                              push rdi
003FD567  41 54                           push r12
003FD569  41 55                           push r13
003FD56B  41 56                           push r14
003FD56D  41 57                           push r15
003FD56F  48 83 EC 68                     sub rsp, 0x68
003FD573  48 8B 71 18                     mov rsi, qword ptr [rcx + 0x18]
003FD577  33 FF                           xor edi, edi
003FD579  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
003FD57E  45 8B F9                        mov r15d, r9d
003FD581  4C 8B F2                        mov r14, rdx
003FD584  48 85 F6                        test rsi, rsi
003FD587  74 47                           je 0x1403fd5d0
003FD589  4C 8D 6E 18                     lea r13, [rsi + 0x18]
003FD58D  48 89 7A 78                     mov qword ptr [rdx + 0x78], rdi
003FD591  49 8B CD                        mov rcx, r13
003FD594  E8 D7 AE E0 FF                  call 0x140208470
003FD599  48 8B 6E 20                     mov rbp, qword ptr [rsi + 0x20]
003FD59D  44 0F B6 E0                     movzx r12d, al
003FD5A1  48 85 ED                        test rbp, rbp
003FD5A4  75 41                           jne 0x1403fd5e7
003FD5A6  48 39 7E 28                     cmp qword ptr [rsi + 0x28], rdi
003FD5AA  0F 85 E6 00 00 00               jne 0x1403fd696
003FD5B0  49 8B CD                        mov rcx, r13
003FD5B3  E8 B8 90 E0 FF                  call 0x140206670
003FD5B8  39 3D 62 97 BC 00               cmp dword ptr [rip + 0xbc9762], edi
003FD5BE  74 0C                           je 0x1403fd5cc
003FD5C0  44 0F 20 C1                     mov rcx, cr8
003FD5C4  41 8A D4                        mov dl, r12b
003FD5C7  E8 CC 80 0F 00                  call 0x1404f5698
003FD5CC  45 0F 22 C4                     mov cr8, r12
003FD5D0  B8 7E 00 00 C0                  mov eax, 0xc000007e
003FD5D5  48 83 C4 68                     add rsp, 0x68
003FD5D9  41 5F                           pop r15
003FD5DB  41 5E                           pop r14
003FD5DD  41 5D                           pop r13
003FD5DF  41 5C                           pop r12
003FD5E1  5F                              pop rdi
003FD5E2  5E                              pop rsi
003FD5E3  5D                              pop rbp
003FD5E4  5B                              pop rbx
003FD5E5  C3                              ret
003FD5E6  CC                              int3
003FD5E7  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
003FD5EB  48 85 C0                        test rax, rax
003FD5EE  0F 85 74 01 00 00               jne 0x1403fd768
003FD5F4  40 88 BC 24 B0 00 00 00         mov byte ptr [rsp + 0xb0], dil
003FD5FC  48 8B CD                        mov rcx, rbp
003FD5FF  E8 3C 09 F9 FF                  call 0x14038df40
003FD604  33 DB                           xor ebx, ebx
003FD606  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
003FD60B  48 8D 4D E8                     lea rcx, [rbp - 0x18]
003FD60F  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
003FD614  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
003FD619  4C 8B F8                        mov r15, rax
003FD61C  48 8B D7                        mov rdx, rdi
003FD61F  4C 8B 31                        mov r14, qword ptr [rcx]
003FD622  4D 85 F6                        test r14, r14
003FD625  74 37                           je 0x1403fd65e
003FD627  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
003FD62F  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
003FD634  49 39 46 20                     cmp qword ptr [r14 + 0x20], rax
003FD638  0F 84 A0 00 00 00               je 0x1403fd6de
003FD63E  49 8B CE                        mov rcx, r14
003FD641  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
003FD646  48 85 D2                        test rdx, rdx
003FD649  75 D4                           jne 0x1403fd61f
003FD64B  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
003FD64F  48 3B C3                        cmp rax, rbx
003FD652  76 CB                           jbe 0x1403fd61f
003FD654  48 8B D8                        mov rbx, rax
003FD657  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003FD65C  EB C1                           jmp 0x1403fd61f
003FD65E  44 8A B4 24 B0 00 00 00         mov r14b, byte ptr [rsp + 0xb0]
003FD666  33 FF                           xor edi, edi
003FD668  48 85 D2                        test rdx, rdx
003FD66B  0F 85 D0 00 00 00               jne 0x1403fd741
003FD671  45 84 F6                        test r14b, r14b
003FD674  0F 85 C8 E6 2E 00               jne 0x1406ebd42
003FD67A  49 8B EF                        mov rbp, r15
003FD67D  4D 85 FF                        test r15, r15
003FD680  0F 85 76 FF FF FF               jne 0x1403fd5fc
003FD686  4C 8B B4 24 B8 00 00 00         mov r14, qword ptr [rsp + 0xb8]
003FD68E  44 8B BC 24 C8 00 00 00         mov r15d, dword ptr [rsp + 0xc8]
003FD696  48 8B 5E 28                     mov rbx, qword ptr [rsi + 0x28]
003FD69A  48 85 DB                        test rbx, rbx
003FD69D  0F 85 47 01 00 00               jne 0x1403fd7ea
003FD6A3  4C 8D 7E 30                     lea r15, [rsi + 0x30]
003FD6A7  49 8B 1F                        mov rbx, qword ptr [r15]
003FD6AA  4D 8B F7                        mov r14, r15
003FD6AD  48 85 DB                        test rbx, rbx
003FD6B0  0F 85 0A 01 00 00               jne 0x1403fd7c0
003FD6B6  45 8A C4                        mov r8b, r12b
003FD6B9  49 8B D5                        mov rdx, r13
003FD6BC  48 8B CE                        mov rcx, rsi
003FD6BF  E8 F8 05 F9 FF                  call 0x14038dcbc
003FD6C4  48 8B CE                        mov rcx, rsi
003FD6C7  E8 88 02 F9 FF                  call 0x14038d954
003FD6CC  41 8A D4                        mov dl, r12b
003FD6CF  49 8B CD                        mov rcx, r13
003FD6D2  E8 C9 54 F9 FF                  call 0x140392ba0
003FD6D7  33 C0                           xor eax, eax
003FD6D9  E9 F7 FE FF FF                  jmp 0x1403fd5d5
003FD6DE  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
003FD6E6  49 39 46 28                     cmp qword ptr [r14 + 0x28], rax
003FD6EA  0F 85 4E FF FF FF               jne 0x1403fd63e
003FD6F0  80 BC 24 D0 00 00 00 00         cmp byte ptr [rsp + 0xd0], 0
003FD6F8  0F 85 AC 00 00 00               jne 0x1403fd7aa
003FD6FE  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
003FD702  48 85 D2                        test rdx, rdx
003FD705  48 0F 44 D1                     cmove rdx, rcx
003FD709  48 3B C7                        cmp rax, rdi
003FD70C  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
003FD711  48 0F 47 F8                     cmova rdi, rax
003FD715  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
003FD71A  4C 3B 75 18                     cmp r14, qword ptr [rbp + 0x18]
003FD71E  75 04                           jne 0x1403fd724
003FD720  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
003FD724  49 8B 06                        mov rax, qword ptr [r14]
003FD727  48 89 01                        mov qword ptr [rcx], rax
003FD72A  48 83 7E 10 00                  cmp qword ptr [rsi + 0x10], 0
003FD72F  74 43                           je 0x1403fd774
003FD731  41 B6 01                        mov r14b, 1
003FD734  44 88 B4 24 B0 00 00 00         mov byte ptr [rsp + 0xb0], r14b
003FD73C  E9 25 FF FF FF                  jmp 0x1403fd666
003FD741  48 39 7D E8                     cmp qword ptr [rbp - 0x18], rdi
003FD745  75 4B                           jne 0x1403fd792
003FD747  48 8B CD                        mov rcx, rbp
003FD74A  E8 61 01 F9 FF                  call 0x14038d8b0
003FD74F  48 8D 55 E8                     lea rdx, [rbp - 0x18]
003FD753  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
003FD757  48 8D 0D 22 48 A1 00            lea rcx, [rip + 0xa14822]
003FD75E  E8 6D 02 F9 FF                  call 0x14038d9d0
003FD763  E9 09 FF FF FF                  jmp 0x1403fd671
003FD768  48 8B E8                        mov rbp, rax
003FD76B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
003FD76F  E9 77 FE FF FF                  jmp 0x1403fd5eb
003FD774  49 8B D6                        mov rdx, r14
003FD777  48 8D 0D 82 4A A1 00            lea rcx, [rip + 0xa14a82]
003FD77E  E8 4D 02 F9 FF                  call 0x14038d9d0
003FD783  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003FD788  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
003FD78D  E9 B4 FE FF FF                  jmp 0x1403fd646
003FD792  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
003FD797  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
003FD79C  48 8D 4D E8                     lea rcx, [rbp - 0x18]
003FD7A0  E8 37 01 00 00                  call 0x1403fd8dc
003FD7A5  E9 C7 FE FF FF                  jmp 0x1403fd671
003FD7AA  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
003FD7B1  41 39 46 1C                     cmp dword ptr [r14 + 0x1c], eax
003FD7B5  0F 85 83 FE FF FF               jne 0x1403fd63e
003FD7BB  E9 3E FF FF FF                  jmp 0x1403fd6fe
003FD7C0  48 8B 7B 18                     mov rdi, qword ptr [rbx + 0x18]
003FD7C4  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
003FD7CC  48 8B AF B8 00 00 00            mov rbp, qword ptr [rdi + 0xb8]
003FD7D3  48 3B 45 30                     cmp rax, qword ptr [rbp + 0x30]
003FD7D7  0F 84 BE 00 00 00               je 0x1403fd89b
003FD7DD  33 ED                           xor ebp, ebp
003FD7DF  4C 8B F3                        mov r14, rbx
003FD7E2  49 8B 1E                        mov rbx, qword ptr [r14]
003FD7E5  E9 C3 FE FF FF                  jmp 0x1403fd6ad
003FD7EA  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
003FD7EE  EB 07                           jmp 0x1403fd7f7
003FD7F0  48 8B D8                        mov rbx, rax
003FD7F3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
003FD7F7  48 85 C0                        test rax, rax
003FD7FA  75 F4                           jne 0x1403fd7f0
003FD7FC  48 8B CB                        mov rcx, rbx
003FD7FF  E8 3C 07 F9 FF                  call 0x14038df40
003FD804  48 8B F8                        mov rdi, rax
003FD807  4C 39 73 30                     cmp qword ptr [rbx + 0x30], r14
003FD80B  74 0D                           je 0x1403fd81a
003FD80D  48 8B DF                        mov rbx, rdi
003FD810  48 85 FF                        test rdi, rdi
003FD813  75 E7                           jne 0x1403fd7fc
003FD815  E9 89 FE FF FF                  jmp 0x1403fd6a3
003FD81A  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
003FD822  48 39 43 38                     cmp qword ptr [rbx + 0x38], rax
003FD826  75 E5                           jne 0x1403fd80d
003FD828  80 BC 24 D0 00 00 00 00         cmp byte ptr [rsp + 0xd0], 0
003FD830  75 24                           jne 0x1403fd856
003FD832  48 8B CB                        mov rcx, rbx
003FD835  E8 76 00 F9 FF                  call 0x14038d8b0
003FD83A  48 89 46 28                     mov qword ptr [rsi + 0x28], rax
003FD83E  48 83 7E 10 00                  cmp qword ptr [rsi + 0x10], 0
003FD843  75 19                           jne 0x1403fd85e
003FD845  48 8B D3                        mov rdx, rbx
003FD848  48 8D 0D 31 49 A1 00            lea rcx, [rip + 0xa14931]
003FD84F  E8 7C 01 F9 FF                  call 0x14038d9d0
003FD854  EB B7                           jmp 0x1403fd80d
003FD856  44 39 7B 2C                     cmp dword ptr [rbx + 0x2c], r15d
003FD85A  75 B1                           jne 0x1403fd80d
003FD85C  EB D4                           jmp 0x1403fd832
003FD85E  41 8A D4                        mov dl, r12b
003FD861  49 8B CD                        mov rcx, r13
003FD864  E8 37 53 F9 FF                  call 0x140392ba0
003FD869  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
003FD86D  48 8D 53 18                     lea rdx, [rbx + 0x18]
003FD871  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
003FD879  E8 52 D2 2B 00                  call 0x1406baad0
003FD87E  49 8B CD                        mov rcx, r13
003FD881  E8 EA AB E0 FF                  call 0x140208470
003FD886  48 8B 7E 28                     mov rdi, qword ptr [rsi + 0x28]
003FD88A  44 8A E0                        mov r12b, al
003FD88D  48 85 FF                        test rdi, rdi
003FD890  74 B3                           je 0x1403fd845
003FD892  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
003FD896  E9 19 E5 2E 00                  jmp 0x1406ebdb4
003FD89B  48 8B CF                        mov rcx, rdi
003FD89E  E8 3D FC FF FF                  call 0x1403fd4e0
003FD8A3  48 39 84 24 C0 00 00 00         cmp qword ptr [rsp + 0xc0], rax
003FD8AB  0F 85 2C FF FF FF               jne 0x1403fd7dd
003FD8B1  80 BC 24 D0 00 00 00 00         cmp byte ptr [rsp + 0xd0], 0
003FD8B9  0F 84 FF E4 2E 00               je 0x1406ebdbe
003FD8BF  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
003FD8C6  3B 45 10                        cmp eax, dword ptr [rbp + 0x10]
003FD8C9  0F 85 0E FF FF FF               jne 0x1403fd7dd
003FD8CF  E9 EA E4 2E 00                  jmp 0x1406ebdbe
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlPrivateFastUnlockAll(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int8 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned int v_stack_pC8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (104);
    v_rdi = 0;
    v_stack_m60 = 0;
    if (*(unsigned __int64 *)(a1 + 24) == 0) goto loc_003FD5D0;
    *(unsigned __int64 *)(a2 + 120) = 0;
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(a1 + 24) + 24, a2, a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) != 0) goto loc_003FD5E7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40)) != 0) goto loc_003FD696;
    result = KxReleaseSpinLock(*(unsigned __int64 *)(a1 + 24) + 24, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 12359522)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_003FD5D0:
loc_003FD5D5:
    v_rsp = (v_rsp) + (104);
    return (unsigned int)(0xC000007EULL);
loc_003FD5E7:
loc_003FD5EB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + 8) != 0) goto loc_003FD768;
    v_stack_pB0 = 0;
loc_003FD5FC:
    result = RtlRealSuccessor(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32), a2, a3, a4);
    v_rbx = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) - 24;
loc_003FD61F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) - 24) == 0) goto loc_003FD65E;
    v_stack_p48 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) - 24);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) - 24) + 32)) == v_stack_pB8) goto loc_003FD6DE;
loc_003FD63E:
    v_stack_p30 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) - 24);
loc_003FD646:
    if (0 != 0) goto loc_003FD61F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) - 24) + 48)) <= 0) goto loc_003FD61F;
    v_stack_p38 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) - 24) + 48);
    goto loc_003FD61F;
loc_003FD65E:
loc_003FD666:
    v_rdi = 0;
    if (0 != 0) goto loc_003FD741;
loc_003FD671:
    if (result != 0) goto loc_003FD5FC;
loc_003FD696:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40) != 0) goto loc_003FD7EA;
loc_003FD6A3:
loc_003FD6AD:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48) != 0) goto loc_003FD7C0;
    result = FsRtlPrivateCheckWaitingLocks(*(unsigned __int64 *)(a1 + 24), *(unsigned __int64 *)(a1 + 24) + 24, (unsigned __int8)((unsigned __int8)(result)), a4);
    result = FsRtlPrivateResetLowestLockOffset(*(unsigned __int64 *)(a1 + 24), *(unsigned __int64 *)(a1 + 24) + 24, (unsigned __int8)((unsigned __int8)(result)), a4);
    result = KeReleaseSpinLock(*(unsigned __int64 *)(a1 + 24) + 24, (unsigned __int8)((unsigned __int8)(result)), (unsigned __int8)((unsigned __int8)(result)), a4);
    result = 0;
    goto loc_003FD5D5;
loc_003FD6DE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48 + 40)) != v_stack_pC0) goto loc_003FD63E;
    if (a5 != 0) goto loc_003FD7AA;
loc_003FD6FE:
    a2 = (unsigned __int8)((unsigned __int8)(result));
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) { a2 = *(unsigned __int64 *)(a1 + 24) + 24; }
    v_stack_p50 = a2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48 + 48)) > 0) { v_rdi = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48 + 48); }
    v_stack_p40 = v_rdi;
    if ((*(unsigned __int64 *)(a1 + 24) + 48) == (*(unsigned __int64 *)(result + 24))) {
        *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(a1 + 24) + 24;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 16)) == 0) goto loc_003FD774;
    v_stack_pB0 = 1;
    goto loc_003FD666;
loc_003FD741:
    if ((*(unsigned __int64 *)(result - 24)) != v_rdi) goto loc_003FD792;
    result = RtlDelete(0, a2, (unsigned __int8)((unsigned __int8)(result)), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) = result;
    result = ExFreeToNPagedLookasideList(v_rip + 10569762, result - 24, (unsigned __int8)((unsigned __int8)(result)), a4);
    goto loc_003FD671;
loc_003FD768:
    goto loc_003FD5EB;
loc_003FD774:
    result = ExFreeToNPagedLookasideList(v_rip + 10570370, 1, (unsigned __int8)((unsigned __int8)(result)), a4);
    goto loc_003FD646;
loc_003FD792:
    result = FsRtlSplitLocks(result - 24, v_stack_p50, v_stack_p40, v_stack_p38);
    goto loc_003FD671;
loc_003FD7AA:
    if ((*(unsigned int *)(1 + 28)) != ((unsigned int)((unsigned int)(v_stack_pC8)))) goto loc_003FD63E;
    goto loc_003FD6FE;
loc_003FD7C0:
    if (v_stack_pB8 == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48) + 24) + 184) + 48))) goto loc_003FD89B;
loc_003FD7DD:
    v_rbp = 0;
    goto loc_003FD6AD;
loc_003FD7EA:
    goto loc_003FD7F7;
loc_003FD7F0:
loc_003FD7F7:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48)) + 8) + 8) != 0) goto loc_003FD7F0;
loc_003FD7FC:
    result = RtlRealSuccessor(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48)) + 8), v_stack_p50, v_stack_p40, v_stack_p38);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48)) + 8) + 48)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48))) goto loc_003FD81A;
loc_003FD80D:
    if (result != 0) goto loc_003FD7FC;
    goto loc_003FD6A3;
loc_003FD81A:
    if ((*(unsigned __int64 *)(result + 56)) != v_stack_pC0) goto loc_003FD80D;
    if (a5 != 0) goto loc_003FD856;
loc_003FD832:
    result = RtlDelete(result, v_stack_p50, v_stack_p40, v_stack_p38);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40) = result;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 16)) != 0) goto loc_003FD85E;
loc_003FD845:
    result = ExFreeToNPagedLookasideList(v_rip + 10570033, result, v_stack_p40, v_stack_p38);
    goto loc_003FD80D;
loc_003FD856:
    if ((*(unsigned int *)(result + 44)) != ((unsigned int)(*(unsigned __int64 *)(a1 + 24) + 48))) goto loc_003FD80D;
    goto loc_003FD832;
loc_003FD85E:
    result = KeReleaseSpinLock(*(unsigned __int64 *)(a1 + 24) + 24, (unsigned __int8)((unsigned __int8)(result)), v_stack_p40, v_stack_p38);
    result = guard_dispatch_icall(a6, result + 24, v_stack_p40, v_stack_p38);
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(a1 + 24) + 24, result + 24, v_stack_p40, v_stack_p38);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40) == 0) goto loc_003FD845;
loc_003FD89B:
    result = IoGetRequestorProcess(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40), result + 24, v_stack_p40, v_stack_p38);
    if (v_stack_pC0 != result) goto loc_003FD7DD;
    if (((unsigned int)((unsigned int)(v_stack_pC8))) != (*(unsigned int *)(v_rbp + 16))) goto loc_003FD7DD;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlPrivateFastUnlockAll(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, uint8_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m60;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint8_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint32_t v_stack_pC8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (104);
    local_rdi = 0;
    v_stack_m60 = 0;
    if (*(uint64_t *)(arg1 + 0x18) == 0) goto loc_003FD5D0;
    *(uint64_t *)(arg2 + 0x78) = 0;
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(arg1 + 0x18) + 24, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) != 0) goto loc_003FD5E7;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28)) != 0) goto loc_003FD696;
    result = KxReleaseSpinLock(*(uint64_t *)(arg1 + 0x18) + 24, Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0xBC9762)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
loc_003FD5D0:
loc_003FD5D5:
    local_rsp = (local_rsp) + (104);
    return (uint32_t)(0xC000007EULL);
loc_003FD5E7:
loc_003FD5EB:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + 0x8) != 0) goto loc_003FD768;
    v_stack_pB0 = 0;
loc_003FD5FC:
    result = RtlRealSuccessor(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20), Arg2, Arg3, Arg4);
    local_rbx = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) - 24;
loc_003FD61F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) - 0x18) == 0) goto loc_003FD65E;
    v_stack_p48 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) - 0x18);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) - 0x18) + 0x20)) == v_stack_pB8) goto loc_003FD6DE;
loc_003FD63E:
    v_stack_p30 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) - 0x18);
loc_003FD646:
    if (0 != 0) goto loc_003FD61F;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) - 0x18) + 0x30)) <= 0) goto loc_003FD61F;
    v_stack_p38 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) - 0x18) + 0x30);
    goto loc_003FD61F;
loc_003FD65E:
loc_003FD666:
    local_rdi = 0;
    if (0 != 0) goto loc_003FD741;
loc_003FD671:
    if (result != 0) goto loc_003FD5FC;
loc_003FD696:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28) != 0) goto loc_003FD7EA;
loc_003FD6A3:
loc_003FD6AD:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30) != 0) goto loc_003FD7C0;
    result = FsRtlPrivateCheckWaitingLocks(*(uint64_t *)(arg1 + 0x18), *(uint64_t *)(arg1 + 0x18) + 24, (uint8_t)((uint8_t)(result)), Arg4);
    result = FsRtlPrivateResetLowestLockOffset(*(uint64_t *)(arg1 + 0x18), *(uint64_t *)(arg1 + 0x18) + 24, (uint8_t)((uint8_t)(result)), Arg4);
    result = KeReleaseSpinLock(*(uint64_t *)(arg1 + 0x18) + 24, (uint8_t)((uint8_t)(result)), (uint8_t)((uint8_t)(result)), Arg4);
    result = 0;
    goto loc_003FD5D5;
loc_003FD6DE:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30 + 0x28)) != v_stack_pC0) goto loc_003FD63E;
    if (Arg5 != 0) goto loc_003FD7AA;
loc_003FD6FE:
    Arg2 = (uint8_t)((uint8_t)(result));
    if ((uint8_t)((uint8_t)(result)) == 0) { Arg2 = *(uint64_t *)(arg1 + 0x18) + 24; }
    v_stack_p50 = Arg2;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30 + 0x30)) > 0) { local_rdi = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30 + 0x30); }
    v_stack_p40 = local_rdi;
    if ((*(uint64_t *)(arg1 + 0x18) + 48) == (*(uint64_t *)(result + 0x18))) {
        *(uint64_t *)(result + 0x18) = *(uint64_t *)(arg1 + 0x18) + 24;
    }
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x18) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x10)) == 0) goto loc_003FD774;
    v_stack_pB0 = 1;
    goto loc_003FD666;
loc_003FD741:
    if ((*(uint64_t *)(result - 0x18)) != local_rdi) goto loc_003FD792;
    result = RtlDelete(0, Arg2, (uint8_t)((uint8_t)(result)), Arg4);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) = result;
    result = ExFreeToNPagedLookasideList(v_rip + 10569762, result - 24, (uint8_t)((uint8_t)(result)), Arg4);
    goto loc_003FD671;
loc_003FD768:
    goto loc_003FD5EB;
loc_003FD774:
    result = ExFreeToNPagedLookasideList(v_rip + 10570370, 1, (uint8_t)((uint8_t)(result)), Arg4);
    goto loc_003FD646;
loc_003FD792:
    result = FsRtlSplitLocks(result - 24, v_stack_p50, v_stack_p40, v_stack_p38);
    goto loc_003FD671;
loc_003FD7AA:
    if ((*(uint32_t *)(1 + 0x1C)) != ((uint32_t)((uint32_t)(v_stack_pC8)))) goto loc_003FD63E;
    goto loc_003FD6FE;
loc_003FD7C0:
    if (v_stack_pB8 == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30) + 0x18) + 0xB8) + 0x30))) goto loc_003FD89B;
loc_003FD7DD:
    local_rbp = 0;
    goto loc_003FD6AD;
loc_003FD7EA:
    goto loc_003FD7F7;
loc_003FD7F0:
loc_003FD7F7:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30)) + 0x8) + 0x8) != 0) goto loc_003FD7F0;
loc_003FD7FC:
    result = RtlRealSuccessor(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30)) + 0x8), v_stack_p50, v_stack_p40, v_stack_p38);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30)) + 0x8) + 0x30)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30))) goto loc_003FD81A;
loc_003FD80D:
    if (result != 0) goto loc_003FD7FC;
    goto loc_003FD6A3;
loc_003FD81A:
    if ((*(uint64_t *)(result + 0x38)) != v_stack_pC0) goto loc_003FD80D;
    if (Arg5 != 0) goto loc_003FD856;
loc_003FD832:
    result = RtlDelete(result, v_stack_p50, v_stack_p40, v_stack_p38);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28) = result;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x10)) != 0) goto loc_003FD85E;
loc_003FD845:
    result = ExFreeToNPagedLookasideList(v_rip + 10570033, result, v_stack_p40, v_stack_p38);
    goto loc_003FD80D;
loc_003FD856:
    if ((*(uint32_t *)(result + 0x2C)) != ((uint32_t)(*(uint64_t *)(arg1 + 0x18) + 48))) goto loc_003FD80D;
    goto loc_003FD832;
loc_003FD85E:
    result = KeReleaseSpinLock(*(uint64_t *)(arg1 + 0x18) + 24, (uint8_t)((uint8_t)(result)), v_stack_p40, v_stack_p38);
    result = guard_dispatch_icall(Arg6, result + 24, v_stack_p40, v_stack_p38);
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(arg1 + 0x18) + 24, result + 24, v_stack_p40, v_stack_p38);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28) == 0) goto loc_003FD845;
loc_003FD89B:
    result = IoGetRequestorProcess(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28), result + 24, v_stack_p40, v_stack_p38);
    if (v_stack_pC0 != result) goto loc_003FD7DD;
    if (((uint32_t)((uint32_t)(v_stack_pC8))) != (*(uint32_t *)(local_rbp + 0x10))) goto loc_003FD7DD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x78` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FD554&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
