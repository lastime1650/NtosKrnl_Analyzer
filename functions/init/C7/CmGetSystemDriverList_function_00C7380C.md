# CmGetSystemDriverList

- RVA: `0x00C7380C`–`0x00C73D88` (길이 `1,404` bytes)
- VA: `0x0000000140C7380C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC0FC`
- 디코드: `361`개 명령, `1,404/1,404` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00C73893` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C738A7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C738E6` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x00C7390A` → [CmpOpenSystemDriverHiveContext](CmpOpenSystemDriverHiveContext_function_00C73D90.md) (function, `0x00C73D90`)
- `0x00C7392A` → [CmpOpenSystemDriverHiveContext](CmpOpenSystemDriverHiveContext_function_00C73D90.md) (function, `0x00C73D90`)
- `0x00C73951` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C73985` → [ZwOpenDirectoryObject](../../text/6A/ZwOpenDirectoryObject_function_006ADBD0.md) (function, `0x006ADBD0`)
- `0x00C739A2` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x00C739DB` → [ZwQueryDirectoryObject](../../text/6A/ZwQueryDirectoryObject_function_006AFAB0.md) (function, `0x006AFAB0`)
- `0x00C73A0C` → [RtlEqualUnicodeString](../../page/93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00C73A25` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x00C73A3F` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C73A4E` → [CmpOpenSystemDriverHiveContext](CmpOpenSystemDriverHiveContext_function_00C73D90.md) (function, `0x00C73D90`)
- `0x00C73A5C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C73A9C` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x00C73AB3` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00C73ABB` → [CmpLockRegistryExclusive](../../page/84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x00C73AC7` → [CmpAcquireSystemDriverHiveContext](../C5/CmpAcquireSystemDriverHiveContext_function_00C56514.md) (function, `0x00C56514`)
- `0x00C73ADE` → [CmpAcquireSystemDriverHiveContext](../C5/CmpAcquireSystemDriverHiveContext_function_00C56514.md) (function, `0x00C56514`)
- `0x00C73AFD` → [CmpAcquireSystemDriverHiveContext](../C5/CmpAcquireSystemDriverHiveContext_function_00C56514.md) (function, `0x00C56514`)
- `0x00C73B16` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x00C73B91` → [CmpFindDrivers](../C5/CmpFindDrivers_function_00C5BFBC.md) (function, `0x00C5BFBC`)
- `0x00C73BAC` → [CmpSortDriverList](../C5/CmpSortDriverList_function_00C5D3D0.md) (function, `0x00C5D3D0`)
- `0x00C73BB9` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00C73BF2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C73C11` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C73C50` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00C73C8D` → [CmpFreeDriverList](../C5/CmpFreeDriverList_function_00C57BCC.md) (function, `0x00C57BCC`)
- `0x00C73C97` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00C73CA8` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00C73CB2` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x00C73CBB` → [CmpCloseSystemDriverHiveContext](CmpCloseSystemDriverHiveContext_function_00C73F30.md) (function, `0x00C73F30`)
- `0x00C73CCA` → [CmpCloseSystemDriverHiveContext](CmpCloseSystemDriverHiveContext_function_00C73F30.md) (function, `0x00C73F30`)
- `0x00C73CD8` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C73CE7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C73D01` → [CmpCloseSystemDriverHiveContext](CmpCloseSystemDriverHiveContext_function_00C73F30.md) (function, `0x00C73F30`)
- `0x00C73D0B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C73D2F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C73D61` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IopInitializeSystemDrivers](IopInitializeSystemDrivers_function_00C73590.md) at `0x00C735E5`

### Static image references
- `0x00C73832` → RVA `0x00E0A740` (`.data`; read)
- `0x00C738FA` → RVA `0x00B4AF30` (`CmpSystemHiveNameString`; read)
- `0x00C73917` → RVA `0x00EEFB6C` (`.data`; read)
- `0x00C73923` → RVA `0x00B4B4D0` (`CmpDevicesHiveNameString`; read)
- `0x00C73946` → RVA `0x00C7E0A0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C73A02` → RVA `0x00FDA0A8` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x00C73893` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C738A7` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C738E6` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`INIT` → `.text`)
  - `0x00C73951` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C73985` → [ZwOpenDirectoryObject](../../text/6A/ZwOpenDirectoryObject_function_006ADBD0.md) (`INIT` → `.text`)
  - `0x00C739A2` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`INIT` → `.text`)
  - `0x00C739DB` → [ZwQueryDirectoryObject](../../text/6A/ZwQueryDirectoryObject_function_006AFAB0.md) (`INIT` → `.text`)
  - `0x00C73A0C` → [RtlEqualUnicodeString](../../page/93/RtlEqualUnicodeString_function_00932A20.md) (`INIT` → `PAGE`)
  - `0x00C73A25` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`INIT` → `.text`)
  - `0x00C73A3F` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C73A5C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C73A9C` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`INIT` → `PAGECMRC`)
  - `0x00C73AB3` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`INIT` → `PAGECMRC`)
  - `0x00C73ABB` → [CmpLockRegistryExclusive](../../page/84/CmpLockRegistryExclusive_function_0084F9B4.md) (`INIT` → `PAGE`)
  - `0x00C73B16` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`INIT` → `.text`)
  - `0x00C73BB9` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`INIT` → `PAGECMRC`)
  - `0x00C73BF2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C73C11` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C73C50` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`INIT` → `.text`)
  - `0x00C73C97` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`INIT` → `PAGECMRC`)
  - `0x00C73CA8` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`INIT` → `PAGECMRC`)
  - `0x00C73CB2` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`INIT` → `PAGECMRC`)
  - `0x00C73CD8` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C73CE7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C73D0B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C73D2F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C73D61` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C7380C  48 8B C4                        mov rax, rsp
00C7380F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00C73813  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C73817  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00C7381B  55                              push rbp
00C7381C  41 54                           push r12
00C7381E  41 55                           push r13
00C73820  41 56                           push r14
00C73822  41 57                           push r15
00C73824  48 8D A8 18 FF FF FF            lea rbp, [rax - 0xe8]
00C7382B  48 81 EC C0 01 00 00            sub rsp, 0x1c0
00C73832  48 8B 05 07 6F 19 00            mov rax, qword ptr [rip + 0x196f07]
00C73839  48 33 C4                        xor rax, rsp
00C7383C  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00C73843  0F 57 C0                        xorps xmm0, xmm0
00C73846  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00C7384A  33 C0                           xor eax, eax
00C7384C  48 8D 4D 00                     lea rcx, [rbp]
00C73850  33 DB                           xor ebx, ebx
00C73852  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00C73856  33 D2                           xor edx, edx
00C73858  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00C7385C  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00C73860  8D 78 40                        lea edi, [rax + 0x40]
00C73863  89 45 C8                        mov dword ptr [rbp - 0x38], eax
00C73866  44 8B C7                        mov r8d, edi
00C73869  89 5D 94                        mov dword ptr [rbp - 0x6c], ebx
00C7386C  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00C73870  89 5D 90                        mov dword ptr [rbp - 0x70], ebx
00C73873  44 8A EB                        mov r13b, bl
00C73876  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
00C7387A  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00C7387E  0F 11 85 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm0
00C73885  0F 11 85 90 00 00 00            movups xmmword ptr [rbp + 0x90], xmm0
00C7388C  0F 11 85 A0 00 00 00            movups xmmword ptr [rbp + 0xa0], xmm0
00C73893  E8 A8 33 A5 FF                  call 0x1406c6c40
00C73898  83 CE FF                        or esi, 0xffffffff
00C7389B  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00C7389F  44 8B C7                        mov r8d, edi
00C738A2  89 75 38                        mov dword ptr [rbp + 0x38], esi
00C738A5  33 D2                           xor edx, edx
00C738A7  E8 94 33 A5 FF                  call 0x1406c6c40
00C738AC  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00C738B1  89 75 78                        mov dword ptr [rbp + 0x78], esi
00C738B4  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00C738B9  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00C738BD  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00C738C2  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
00C738C6  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00C738CB  8B F3                           mov esi, ebx
00C738CD  48 8D 45 80                     lea rax, [rbp - 0x80]
00C738D1  44 8B F3                        mov r14d, ebx
00C738D4  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C738D8  44 8A FB                        mov r15b, bl
00C738DB  48 8D 45 80                     lea rax, [rbp - 0x80]
00C738DF  44 8A E3                        mov r12b, bl
00C738E2  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C738E6  E8 85 85 78 FF                  call 0x1403fbe70
00C738EB  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00C738F0  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00C738F5  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00C738FA  48 8D 0D 2F 76 ED FF            lea rcx, [rip - 0x1289d1]
00C73901  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00C73906  48 8D 55 00                     lea rdx, [rbp]
00C7390A  E8 81 04 00 00                  call 0x140c73d90
00C7390F  85 C0                           test eax, eax
00C73911  0F 88 61 03 00 00               js 0x140c73c78
00C73917  39 1D 4F C2 27 00               cmp dword ptr [rip + 0x27c24f], ebx
00C7391D  74 27                           je 0x140c73946
00C7391F  48 8D 55 40                     lea rdx, [rbp + 0x40]
00C73923  48 8D 0D A6 7B ED FF            lea rcx, [rip - 0x12845a]
00C7392A  E8 61 04 00 00                  call 0x140c73d90
00C7392F  BA 00 00 00 80                  mov edx, 0x80000000
00C73934  8D 0C 10                        lea ecx, [rax + rdx]
00C73937  85 CA                           test edx, ecx
00C73939  75 0B                           jne 0x140c73946
00C7393B  3D 34 00 00 C0                  cmp eax, 0xc0000034
00C73940  0F 85 32 03 00 00               jne 0x140c73c78
00C73946  48 8D 15 53 A7 00 00            lea rdx, [rip + 0xa753]
00C7394D  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00C73951  E8 2A 6E 7B FF                  call 0x14042a780
00C73956  48 8D 45 D8                     lea rax, [rbp - 0x28]
00C7395A  C7 45 A0 30 00 00 00            mov dword ptr [rbp - 0x60], 0x30
00C73961  0F 57 C0                        xorps xmm0, xmm0
00C73964  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00C73968  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00C7396C  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
00C73970  BA 01 00 00 00                  mov edx, 1
00C73975  C7 45 B8 40 02 00 00            mov dword ptr [rbp - 0x48], 0x240
00C7397C  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00C73980  F3 0F 7F 45 C0                  movdqu xmmword ptr [rbp - 0x40], xmm0
00C73985  E8 46 A2 A3 FF                  call 0x1406adbd0
00C7398A  85 C0                           test eax, eax
00C7398C  0F 88 E6 02 00 00               js 0x140c73c78
00C73992  BA 00 04 00 00                  mov edx, 0x400
00C73997  B9 00 01 00 00                  mov ecx, 0x100
00C7399C  41 B8 43 4D 20 20               mov r8d, 0x20204d43
00C739A2  E8 5D 9B 75 FF                  call 0x1403cd504
00C739A7  48 8B F0                        mov rsi, rax
00C739AA  48 85 C0                        test rax, rax
00C739AD  0F 84 C5 02 00 00               je 0x140c73c78
00C739B3  B0 01                           mov al, 1
00C739B5  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00C739B9  41 B1 01                        mov r9b, 1
00C739BC  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00C739C1  41 B8 00 04 00 00               mov r8d, 0x400
00C739C7  48 8D 4D 94                     lea rcx, [rbp - 0x6c]
00C739CB  48 8B D6                        mov rdx, rsi
00C739CE  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00C739D3  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00C739D7  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00C739DB  E8 D0 C0 A3 FF                  call 0x1406afab0
00C739E0  3D 1A 00 00 80                  cmp eax, 0x8000001a
00C739E5  0F 84 B1 00 00 00               je 0x140c73a9c
00C739EB  85 C0                           test eax, eax
00C739ED  0F 88 85 02 00 00               js 0x140c73c78
00C739F3  48 8B FE                        mov rdi, rsi
00C739F6  66 39 1F                        cmp word ptr [rdi], bx
00C739F9  0F 84 96 00 00 00               je 0x140c73a95
00C739FF  41 B0 01                        mov r8b, 1
00C73A02  48 8D 15 9F 66 36 00            lea rdx, [rip + 0x36669f]
00C73A09  48 8B CF                        mov rcx, rdi
00C73A0C  E8 0F F0 CB FF                  call 0x140932a20
00C73A11  84 C0                           test al, al
00C73A13  75 77                           jne 0x140c73a8c
00C73A15  BA 40 00 00 00                  mov edx, 0x40
00C73A1A  B9 00 01 00 00                  mov ecx, 0x100
00C73A1F  41 B8 43 4D 20 20               mov r8d, 0x20204d43
00C73A25  E8 DA 9A 75 FF                  call 0x1403cd504
00C73A2A  48 8B D8                        mov rbx, rax
00C73A2D  48 85 C0                        test rax, rax
00C73A30  0F 84 40 02 00 00               je 0x140c73c76
00C73A36  33 D2                           xor edx, edx
00C73A38  48 8B C8                        mov rcx, rax
00C73A3B  44 8D 42 40                     lea r8d, [rdx + 0x40]
00C73A3F  E8 FC 31 A5 FF                  call 0x1406c6c40
00C73A44  83 4B 38 FF                     or dword ptr [rbx + 0x38], 0xffffffff
00C73A48  48 8B D3                        mov rdx, rbx
00C73A4B  48 8B CF                        mov rcx, rdi
00C73A4E  E8 3D 03 00 00                  call 0x140c73d90
00C73A53  85 C0                           test eax, eax
00C73A55  79 0C                           jns 0x140c73a63
00C73A57  33 D2                           xor edx, edx
00C73A59  48 8B CB                        mov rcx, rbx
00C73A5C  E8 0F EE F0 FF                  call 0x140b82870
00C73A61  EB 27                           jmp 0x140c73a8a
00C73A63  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00C73A68  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C73A6D  48 39 08                        cmp qword ptr [rax], rcx
00C73A70  0F 85 E9 00 00 00               jne 0x140c73b5f
00C73A76  48 89 43 08                     mov qword ptr [rbx + 8], rax
00C73A7A  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C73A7F  48 89 0B                        mov qword ptr [rbx], rcx
00C73A82  48 89 18                        mov qword ptr [rax], rbx
00C73A85  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00C73A8A  33 DB                           xor ebx, ebx
00C73A8C  48 83 C7 20                     add rdi, 0x20
00C73A90  E9 61 FF FF FF                  jmp 0x140c739f6
00C73A95  8A C3                           mov al, bl
00C73A97  E9 19 FF FF FF                  jmp 0x140c739b5
00C73A9C  E8 5F 59 F5 FF                  call 0x140bc9400
00C73AA1  44 8A E0                        mov r12b, al
00C73AA4  84 C0                           test al, al
00C73AA6  0F 84 CC 01 00 00               je 0x140c73c78
00C73AAC  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
00C73AB3  E8 28 5E F5 FF                  call 0x140bc98e0
00C73AB8  41 B5 01                        mov r13b, 1
00C73ABB  E8 F4 BE BD FF                  call 0x14084f9b4
00C73AC0  48 8D 4D 00                     lea rcx, [rbp]
00C73AC4  45 8A FD                        mov r15b, r13b
00C73AC7  E8 48 2A FE FF                  call 0x140c56514
00C73ACC  85 C0                           test eax, eax
00C73ACE  0F 88 A4 01 00 00               js 0x140c73c78
00C73AD4  48 39 5D 60                     cmp qword ptr [rbp + 0x60], rbx
00C73AD8  74 11                           je 0x140c73aeb
00C73ADA  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00C73ADE  E8 31 2A FE FF                  call 0x140c56514
00C73AE3  85 C0                           test eax, eax
00C73AE5  0F 88 8D 01 00 00               js 0x140c73c78
00C73AEB  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00C73AF0  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00C73AF5  48 3B D8                        cmp rbx, rax
00C73AF8  74 6C                           je 0x140c73b66
00C73AFA  48 8B CB                        mov rcx, rbx
00C73AFD  E8 12 2A FE FF                  call 0x140c56514
00C73B02  85 C0                           test eax, eax
00C73B04  78 54                           js 0x140c73b5a
00C73B06  BA 30 00 00 00                  mov edx, 0x30
00C73B0B  B9 00 01 00 00                  mov ecx, 0x100
00C73B10  41 B8 43 4D 20 20               mov r8d, 0x20204d43
00C73B16  E8 E9 99 75 FF                  call 0x1403cd504
00C73B1B  48 85 C0                        test rax, rax
00C73B1E  0F 84 52 01 00 00               je 0x140c73c76
00C73B24  0F 10 43 10                     movups xmm0, xmmword ptr [rbx + 0x10]
00C73B28  48 8D 55 80                     lea rdx, [rbp - 0x80]
00C73B2C  F3 0F 7F 40 10                  movdqu xmmword ptr [rax + 0x10], xmm0
00C73B31  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00C73B35  48 89 48 20                     mov qword ptr [rax + 0x20], rcx
00C73B39  8B 4B 38                        mov ecx, dword ptr [rbx + 0x38]
00C73B3C  89 48 28                        mov dword ptr [rax + 0x28], ecx
00C73B3F  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00C73B43  48 39 11                        cmp qword ptr [rcx], rdx
00C73B46  75 17                           jne 0x140c73b5f
00C73B48  48 89 48 08                     mov qword ptr [rax + 8], rcx
00C73B4C  48 8D 55 80                     lea rdx, [rbp - 0x80]
00C73B50  48 89 10                        mov qword ptr [rax], rdx
00C73B53  48 89 01                        mov qword ptr [rcx], rax
00C73B56  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C73B5A  48 8B 1B                        mov rbx, qword ptr [rbx]
00C73B5D  EB 91                           jmp 0x140c73af0
00C73B5F  B9 03 00 00 00                  mov ecx, 3
00C73B64  CD 29                           int 0x29
00C73B66  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00C73B6A  44 8B 4D 78                     mov r9d, dword ptr [rbp + 0x78]
00C73B6E  4C 8B 45 70                     mov r8, qword ptr [rbp + 0x70]
00C73B72  8B 55 38                        mov edx, dword ptr [rbp + 0x38]
00C73B75  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00C73B79  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00C73B7E  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00C73B83  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00C73B88  48 8D 45 80                     lea rax, [rbp - 0x80]
00C73B8C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C73B91  E8 26 84 FE FF                  call 0x140c5bfbc
00C73B96  33 DB                           xor ebx, ebx
00C73B98  84 C0                           test al, al
00C73B9A  0F 84 D8 00 00 00               je 0x140c73c78
00C73BA0  8B 55 38                        mov edx, dword ptr [rbp + 0x38]
00C73BA3  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00C73BA8  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00C73BAC  E8 1F 98 FE FF                  call 0x140c5d3d0
00C73BB1  84 C0                           test al, al
00C73BB3  0F 84 BF 00 00 00               je 0x140c73c78
00C73BB9  E8 C6 5E F5 FF                  call 0x140bc9a84
00C73BBE  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00C73BC3  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00C73BC8  44 8A FB                        mov r15b, bl
00C73BCB  8B D3                           mov edx, ebx
00C73BCD  48 3B C1                        cmp rax, rcx
00C73BD0  74 0F                           je 0x140c73be1
00C73BD2  48 8B 00                        mov rax, qword ptr [rax]
00C73BD5  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00C73BDA  FF C2                           inc edx
00C73BDC  49 3B C0                        cmp rax, r8
00C73BDF  75 F1                           jne 0x140c73bd2
00C73BE1  FF C2                           inc edx
00C73BE3  B9 40 00 00 00                  mov ecx, 0x40
00C73BE8  48 C1 E2 03                     shl rdx, 3
00C73BEC  41 B8 43 4D 38 32               mov r8d, 0x32384d43
00C73BF2  E8 F9 E4 F0 FF                  call 0x140b820f0
00C73BF7  4C 8B F0                        mov r14, rax
00C73BFA  48 85 C0                        test rax, rax
00C73BFD  75 18                           jne 0x140c73c17
00C73BFF  45 33 C9                        xor r9d, r9d
00C73C02  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00C73C07  8D 50 02                        lea edx, [rax + 2]
00C73C0A  8D 48 67                        lea ecx, [rax + 0x67]
00C73C0D  44 8D 40 01                     lea r8d, [rax + 1]
00C73C11  E8 4A 9A 88 FF                  call 0x1404fd660
00C73C16  CC                              int3
00C73C17  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00C73C1C  EB 44                           jmp 0x140c73c62
00C73C1E  48 83 65 A8 00                  and qword ptr [rbp - 0x58], 0
00C73C23  48 8D 47 20                     lea rax, [rdi + 0x20]
00C73C27  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00C73C2B  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00C73C2F  8B C3                           mov eax, ebx
00C73C31  0F 57 C0                        xorps xmm0, xmm0
00C73C34  BA 1F 00 02 00                  mov edx, 0x2001f
00C73C39  C7 45 A0 30 00 00 00            mov dword ptr [rbp - 0x60], 0x30
00C73C40  C7 45 B8 40 02 00 00            mov dword ptr [rbp - 0x48], 0x240
00C73C47  F3 0F 7F 45 C0                  movdqu xmmword ptr [rbp - 0x40], xmm0
00C73C4C  49 8D 0C C6                     lea rcx, [r14 + rax*8]
00C73C50  E8 BB 96 A3 FF                  call 0x1406ad310
00C73C55  48 8B 3F                        mov rdi, qword ptr [rdi]
00C73C58  8D 4B 01                        lea ecx, [rbx + 1]
00C73C5B  85 C0                           test eax, eax
00C73C5D  0F 48 CB                        cmovs ecx, ebx
00C73C60  8B D9                           mov ebx, ecx
00C73C62  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00C73C67  48 3B F8                        cmp rdi, rax
00C73C6A  75 B2                           jne 0x140c73c1e
00C73C6C  8B C3                           mov eax, ebx
00C73C6E  33 DB                           xor ebx, ebx
00C73C70  49 89 1C C6                     mov qword ptr [r14 + rax*8], rbx
00C73C74  EB 02                           jmp 0x140c73c78
00C73C76  33 DB                           xor ebx, ebx
00C73C78  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00C73C7D  48 39 44 24 60                  cmp qword ptr [rsp + 0x60], rax
00C73C82  74 0E                           je 0x140c73c92
00C73C84  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00C73C88  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00C73C8D  E8 3A 3F FE FF                  call 0x140c57bcc
00C73C92  45 84 FF                        test r15b, r15b
00C73C95  74 05                           je 0x140c73c9c
00C73C97  E8 E8 5D F5 FF                  call 0x140bc9a84
00C73C9C  45 84 ED                        test r13b, r13b
00C73C9F  74 0C                           je 0x140c73cad
00C73CA1  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
00C73CA8  E8 73 5C F5 FF                  call 0x140bc9920
00C73CAD  45 84 E4                        test r12b, r12b
00C73CB0  74 05                           je 0x140c73cb7
00C73CB2  E8 C9 5B F5 FF                  call 0x140bc9880
00C73CB7  48 8D 4D 00                     lea rcx, [rbp]
00C73CBB  E8 70 02 00 00                  call 0x140c73f30
00C73CC0  48 39 5D 60                     cmp qword ptr [rbp + 0x60], rbx
00C73CC4  74 09                           je 0x140c73ccf
00C73CC6  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00C73CCA  E8 61 02 00 00                  call 0x140c73f30
00C73CCF  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00C73CD3  48 85 C9                        test rcx, rcx
00C73CD6  74 05                           je 0x140c73cdd
00C73CD8  E8 D3 95 A3 FF                  call 0x1406ad2b0
00C73CDD  48 85 F6                        test rsi, rsi
00C73CE0  74 0A                           je 0x140c73cec
00C73CE2  33 D2                           xor edx, edx
00C73CE4  48 8B CE                        mov rcx, rsi
00C73CE7  E8 84 EB F0 FF                  call 0x140b82870
00C73CEC  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
00C73CF1  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00C73CF6  48 3B F8                        cmp rdi, rax
00C73CF9  74 22                           je 0x140c73d1d
00C73CFB  48 8B 1F                        mov rbx, qword ptr [rdi]
00C73CFE  48 8B CF                        mov rcx, rdi
00C73D01  E8 2A 02 00 00                  call 0x140c73f30
00C73D06  33 D2                           xor edx, edx
00C73D08  48 8B CF                        mov rcx, rdi
00C73D0B  E8 60 EB F0 FF                  call 0x140b82870
00C73D10  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00C73D15  48 8B FB                        mov rdi, rbx
00C73D18  48 3B D8                        cmp rbx, rax
00C73D1B  75 DE                           jne 0x140c73cfb
00C73D1D  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00C73D21  48 8D 45 80                     lea rax, [rbp - 0x80]
00C73D25  48 3B C8                        cmp rcx, rax
00C73D28  74 16                           je 0x140c73d40
00C73D2A  48 8B 19                        mov rbx, qword ptr [rcx]
00C73D2D  33 D2                           xor edx, edx
00C73D2F  E8 3C EB F0 FF                  call 0x140b82870
00C73D34  48 8D 45 80                     lea rax, [rbp - 0x80]
00C73D38  48 8B CB                        mov rcx, rbx
00C73D3B  48 3B D8                        cmp rbx, rax
00C73D3E  75 EA                           jne 0x140c73d2a
00C73D40  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00C73D49  49 8B C6                        mov rax, r14
00C73D4C  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00C73D50  48 89 8A E8 06 00 00            mov qword ptr [rdx + 0x6e8], rcx
00C73D57  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
00C73D5E  48 33 CC                        xor rcx, rsp
00C73D61  E8 DA 88 A3 FF                  call 0x1406ac640
00C73D66  4C 8D 9C 24 C0 01 00 00         lea r11, [rsp + 0x1c0]
00C73D6E  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00C73D72  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00C73D76  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00C73D7A  49 8B E3                        mov rsp, r11
00C73D7D  41 5F                           pop r15
00C73D7F  41 5E                           pop r14
00C73D81  41 5D                           pop r13
00C73D83  41 5C                           pop r12
00C73D85  5D                              pop rbp
00C73D86  C3                              ret
00C73D87  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmGetSystemDriverList(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int8 v_stack_m1C8;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 1666823)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 232 + 176) = result;
    *(unsigned __int64 *)(v_rsp - 232 - 48) = a1;
    result = 0;
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 8) = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 24) = v_xmm0;
    *(unsigned int *)(v_rsp - 232 - 56) = 0;
    *(unsigned int *)(v_rsp - 232 - 108) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 40) = v_xmm0;
    *(unsigned int *)(v_rsp - 232 - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 232 - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 232 - 80) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 232 + 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 232 + 144) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 232 + 160) = v_xmm0;
    result = memset(v_rsp - 232, a2, (unsigned int)((unsigned int)(result + 64)), a4);
    v_rsi = (unsigned int)((v_rsi) | (0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 232 + 56) = (unsigned int)(v_rsi);
    a2 = 0;
    result = memset(v_rsp - 232 + 64, a2, (unsigned int)((unsigned int)(result + 64)), a4);
    *(unsigned int *)(v_rsp - 232 + 120) = (unsigned int)(v_rsi);
    v_stack_m170 = v_stack_m178;
    *(unsigned __int64 *)(v_rsp - 232 - 104) = 0;
    v_stack_m178 = v_stack_m178;
    *(unsigned __int64 *)(v_rsp - 232 - 120) = v_rsp - 232 - 128;
    *(unsigned __int64 *)(v_rsp - 232 - 128) = v_rsp - 232 - 128;
    result = CmpInitializeThreadInfo(v_rsp - 232 - 24, a2, (unsigned int)((unsigned int)(result + 64)), a4);
    v_stack_m180 = v_stack_m188;
    v_stack_m188 = v_stack_m188;
    result = CmpOpenSystemDriverHiveContext(v_rip - 1214929, v_rsp - 232, (unsigned int)((unsigned int)(result + 64)), a4);
    if (sign_flag) goto loc_00C73C78;
    if ((*(unsigned int *)(v_rip + 2605647)) == 0) goto loc_00C73946;
    result = CmpOpenSystemDriverHiveContext(v_rip - 1213530, v_rsp - 232 + 64, (unsigned int)((unsigned int)(result + 64)), a4);
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_00C73946;
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00C73C78;
loc_00C73946:
    result = RtlInitUnicodeString(v_rsp - 232 - 40, v_rip + 42835, (unsigned int)((unsigned int)(result + 64)), a4);
    *(unsigned int *)(v_rsp - 232 - 96) = 48;
    *(unsigned __int64 *)(v_rsp - 232 - 80) = v_rsp - 232 - 40;
    *(unsigned __int64 *)(v_rsp - 232 - 88) = 0;
    *(unsigned int *)(v_rsp - 232 - 72) = 576;
    *(unsigned __int64 *)(v_rsp - 232 - 64) = v_xmm0;
    result = ZwOpenDirectoryObject(v_rsp - 232 - 104, 1, v_rsp - 232 - 96, a4);
    if (sign_flag) goto loc_00C73C78;
    result = CmpAllocatePool(256, (unsigned int)(0x400ULL), (unsigned int)(0x20204D43ULL), a4);
    if (result == 0) goto loc_00C73C78;
loc_00C739B5:
    v_stack_m1B8 = v_rsp - 232 - 112;
    v_stack_m1C0 = v_rsp - 232 - 108;
    v_stack_m1C8 = 1;
    result = ZwQueryDirectoryObject(*(unsigned __int64 *)(v_rsp - 232 - 104), result, (unsigned int)(0x400ULL), 1);
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_00C73A9C;
    if (sign_flag) goto loc_00C73C78;
loc_00C739F6:
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_00C73A95;
    result = RtlEqualUnicodeString(result, v_rip + 3565215, 1, 1);
    if ((unsigned __int8)(result) != 0) goto loc_00C73A8C;
    result = CmpAllocatePool(256, 64, (unsigned int)(0x20204D43ULL), 1);
    if (result == 0) goto loc_00C73C76;
    a2 = 0;
    result = memset(result, a2, a2 + 64, 1);
    result = CmpOpenSystemDriverHiveContext(result, result, a2 + 64, 1);
    if (!sign_flag) goto loc_00C73A63;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a2 + 64, 1);
    goto loc_00C73A8A;
loc_00C73A63:
    if ((*(unsigned __int64 *)(v_stack_m170)) != v_stack_m178) goto loc_00C73B5F;
    *(unsigned __int64 *)(result + 8) = v_stack_m170;
    *(unsigned __int64 *)(result) = v_stack_m178;
    *(unsigned __int64 *)(v_stack_m170) = result;
    v_stack_m170 = result;
loc_00C73A8A:
    v_rbx = 0;
loc_00C73A8C:
    v_rdi = (result) + (32);
    goto loc_00C739F6;
loc_00C73A95:
    goto loc_00C739B5;
loc_00C73A9C:
    result = CmpAcquireShutdownRundown(v_stack_m178, a2, a2 + 64, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00C73C78;
    result = CmpAttachToRegistryProcess(v_rsp - 232 + 128, a2, a2 + 64, 1);
    result = CmpLockRegistryExclusive(v_rsp - 232 + 128, a2, a2 + 64, 1);
    result = CmpAcquireSystemDriverHiveContext(v_rsp - 232, a2, a2 + 64, 1);
    if (sign_flag) goto loc_00C73C78;
    if ((*(unsigned __int64 *)(v_rsp - 232 + 96)) == 0) goto loc_00C73AEB;
    result = CmpAcquireSystemDriverHiveContext(v_rsp - 232 + 64, a2, a2 + 64, 1);
    if (sign_flag) goto loc_00C73C78;
loc_00C73AEB:
loc_00C73AF0:
    if (v_stack_m178 == v_stack_m178) goto loc_00C73B66;
    result = CmpAcquireSystemDriverHiveContext(v_stack_m178, a2, a2 + 64, 1);
    if (sign_flag) goto loc_00C73B5A;
    result = CmpAllocatePool(256, 48, (unsigned int)(0x20204D43ULL), 1);
    if (result == 0) goto loc_00C73C76;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = *(unsigned __int64 *)(v_stack_m178 + 48);
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m178 + 56)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 232 - 120))) != (v_rsp - 232 - 128)) goto loc_00C73B5F;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rsp - 232 - 120);
    *(unsigned __int64 *)(result) = v_rsp - 232 - 128;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 232 - 120)) = result;
    *(unsigned __int64 *)(v_rsp - 232 - 120) = result;
loc_00C73B5A:
    goto loc_00C73AF0;
loc_00C73B5F:
loc_00C73B66:
    v_stack_m198 = *(unsigned __int64 *)(v_rsp - 232 - 48);
    v_stack_m1A8 = v_stack_m188;
    v_stack_m1C8 = v_rsp - 232 - 128;
    result = CmpFindDrivers(*(unsigned __int64 *)(v_rsp - 232 + 48), (unsigned int)(*(unsigned int *)(v_rsp - 232 + 56)), *(unsigned __int64 *)(v_rsp - 232 + 112), (unsigned int)(*(unsigned int *)(v_rsp - 232 + 120)));
    v_rbx = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00C73C78;
    result = CmpSortDriverList(*(unsigned __int64 *)(v_rsp - 232 + 48), (unsigned int)(*(unsigned int *)(v_rsp - 232 + 56)), v_stack_m188, (unsigned int)(*(unsigned int *)(v_rsp - 232 + 120)));
    if ((unsigned __int8)(result) == 0) goto loc_00C73C78;
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_rsp - 232 + 48), (unsigned int)(*(unsigned int *)(v_rsp - 232 + 56)), v_stack_m188, (unsigned int)(*(unsigned int *)(v_rsp - 232 + 120)));
    if (v_stack_m188 == v_stack_m188) goto loc_00C73BE1;
loc_00C73BD2:
    a2 = (unsigned int)((0) + 1);
    if ((*(unsigned __int64 *)(v_stack_m188)) != v_stack_m188) goto loc_00C73BD2;
loc_00C73BE1:
    a2 = (unsigned int)((a2) + 1);
    a2 = (a2) << (3);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x32384D43ULL), (unsigned int)(*(unsigned int *)(v_rsp - 232 + 120)));
    if (result == 0) {
        a4 = 0;
        v_stack_m1C8 = 0;
        a2 = result + 2;
        a1 = result + 103;
        a3 = result + 1;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    goto loc_00C73C62;
loc_00C73C1E:
    *(unsigned __int64 *)(v_rsp - 232 - 80) = v_stack_m188 + 32;
    *(unsigned int *)(v_rsp - 232 - 96) = 48;
    *(unsigned int *)(v_rsp - 232 - 72) = 576;
    *(unsigned __int64 *)(v_rsp - 232 - 64) = v_xmm0;
    result = ZwOpenKey(result + 0 * 8, (unsigned int)(0x2001FULL), v_rsp - 232 - 96, a4);
    a1 = v_rbx + 1;
    if (sign_flag) { a1 = 0; }
loc_00C73C62:
    if ((*(unsigned __int64 *)(v_stack_m188)) != v_stack_m188) goto loc_00C73C1E;
    v_rbx = 0;
    *(unsigned __int64 *)(result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) * 8) = 0;
    goto loc_00C73C78;
loc_00C73C76:
    v_rbx = 0;
loc_00C73C78:
    result = v_stack_m188;
    if (v_stack_m188 != v_stack_m188) {
        a1 = *(unsigned __int64 *)(v_rsp - 232 + 48);
        a2 = v_stack_m188;
        result = CmpFreeDriverList(a1, a2, v_rsp - 232 - 96, a4);
    }
    if (0 != 0) {
        result = CmpUnlockRegistry(a1, a2, v_rsp - 232 - 96, a4);
    }
    if (1 != 0) {
        a1 = v_rsp - 232 + 128;
        result = CmpDetachFromRegistryProcess(a1, a2, v_rsp - 232 - 96, a4);
    }
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        result = CmpReleaseShutdownRundown(a1, a2, v_rsp - 232 - 96, a4);
    }
    result = CmpCloseSystemDriverHiveContext(v_rsp - 232, a2, v_rsp - 232 - 96, a4);
    if ((*(unsigned __int64 *)(v_rsp - 232 + 96)) != 0) {
        a1 = v_rsp - 232 + 64;
        result = CmpCloseSystemDriverHiveContext(a1, a2, v_rsp - 232 - 96, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 232 - 104) != 0) {
        result = ZwClose(*(unsigned __int64 *)(v_rsp - 232 - 104), a2, v_rsp - 232 - 96, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_rsp - 232 - 96, a4);
    }
    if (v_stack_m178 == v_stack_m178) goto loc_00C73D1D;
loc_00C73CFB:
    result = CmpCloseSystemDriverHiveContext(v_stack_m178, a2, v_rsp - 232 - 96, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m178, a2, v_rsp - 232 - 96, a4);
    if ((*(unsigned __int64 *)(v_stack_m178)) != v_stack_m178) goto loc_00C73CFB;
loc_00C73D1D:
    if ((*(unsigned __int64 *)(v_rsp - 232 - 128)) == (v_rsp - 232 - 128)) goto loc_00C73D40;
loc_00C73D2A:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 232 - 128), a2, v_rsp - 232 - 96, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 232 - 128))) != (v_rsp - 232 - 128)) goto loc_00C73D2A;
loc_00C73D40:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1768) = *(unsigned __int64 *)(v_rsp - 232 - 24);
    a1 = (*(unsigned __int64 *)(v_rsp - 232 + 176)) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), v_rsp - 232 - 96, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmGetSystemDriverList(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint8_t v_stack_m1C8;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0x196F07)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xE8 + 0xB0) = result;
    *(uint64_t *)(local_rsp - 0xE8 - 0x30) = Arg1;
    result = 0;
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x8) = 0;
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x18) = v_xmm0;
    *(uint32_t *)(local_rsp - 0xE8 - 0x38) = 0;
    *(uint32_t *)(local_rsp - 0xE8 - 0x6C) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x28) = v_xmm0;
    *(uint32_t *)(local_rsp - 0xE8 - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xE8 - 0x50) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xE8 + 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xE8 + 0x90) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xE8 + 0xA0) = v_xmm0;
    result = memset(local_rsp - 232, Arg2, (uint32_t)((uint32_t)(result + 64)), a4);
    local_rsi = (uint32_t)((local_rsi) | (0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0xE8 + 0x38) = (uint32_t)(local_rsi);
    Arg2 = 0;
    result = memset(local_rsp - 232 + 64, Arg2, (uint32_t)((uint32_t)(result + 64)), a4);
    *(uint32_t *)(local_rsp - 0xE8 + 0x78) = (uint32_t)(local_rsi);
    v_stack_m170 = v_stack_m178;
    *(uint64_t *)(local_rsp - 0xE8 - 0x68) = 0;
    v_stack_m178 = v_stack_m178;
    *(uint64_t *)(local_rsp - 0xE8 - 0x78) = local_rsp - 232 - 128;
    *(uint64_t *)(local_rsp - 0xE8 - 0x80) = local_rsp - 232 - 128;
    result = CmpInitializeThreadInfo(local_rsp - 232 - 24, Arg2, (uint32_t)((uint32_t)(result + 64)), a4);
    v_stack_m180 = v_stack_m188;
    v_stack_m188 = v_stack_m188;
    result = CmpOpenSystemDriverHiveContext(v_rip - 1214929, local_rsp - 232, (uint32_t)((uint32_t)(result + 64)), a4);
    if (sign_flag) goto loc_00C73C78;
    if ((*(uint32_t *)(v_rip + 0x27C24F)) == 0) goto loc_00C73946;
    result = CmpOpenSystemDriverHiveContext(v_rip - 1213530, local_rsp - 232 + 64, (uint32_t)((uint32_t)(result + 64)), a4);
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_00C73946;
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00C73C78;
loc_00C73946:
    result = RtlInitUnicodeString(local_rsp - 232 - 40, v_rip + 42835, (uint32_t)((uint32_t)(result + 64)), a4);
    *(uint32_t *)(local_rsp - 0xE8 - 0x60) = 48;
    *(uint64_t *)(local_rsp - 0xE8 - 0x50) = local_rsp - 232 - 40;
    *(uint64_t *)(local_rsp - 0xE8 - 0x58) = 0;
    *(uint32_t *)(local_rsp - 0xE8 - 0x48) = 576;
    *(uint64_t *)(local_rsp - 0xE8 - 0x40) = v_xmm0;
    result = ZwOpenDirectoryObject(local_rsp - 232 - 104, 1, local_rsp - 232 - 96, a4);
    if (sign_flag) goto loc_00C73C78;
    result = CmpAllocatePool(256, (uint32_t)(0x400ULL), (uint32_t)(0x20204D43ULL), a4);
    if (result == 0) goto loc_00C73C78;
loc_00C739B5:
    v_stack_m1B8 = local_rsp - 232 - 112;
    v_stack_m1C0 = local_rsp - 232 - 108;
    v_stack_m1C8 = 1;
    result = ZwQueryDirectoryObject(*(uint64_t *)(local_rsp - 0xE8 - 0x68), result, (uint32_t)(0x400ULL), 1);
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_00C73A9C;
    if (sign_flag) goto loc_00C73C78;
loc_00C739F6:
    if ((*(uint16_t *)(result)) == 0) goto loc_00C73A95;
    result = RtlEqualUnicodeString(result, v_rip + 3565215, 1, 1);
    if ((uint8_t)(result) != 0) goto loc_00C73A8C;
    result = CmpAllocatePool(256, 64, (uint32_t)(0x20204D43ULL), 1);
    if (result == 0) goto loc_00C73C76;
    Arg2 = 0;
    result = memset(result, Arg2, Arg2 + 64, 1);
    result = CmpOpenSystemDriverHiveContext(result, result, Arg2 + 64, 1);
    if (!sign_flag) goto loc_00C73A63;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg2 + 64, 1);
    goto loc_00C73A8A;
loc_00C73A63:
    if ((*(uint64_t *)(v_stack_m170)) != v_stack_m178) goto loc_00C73B5F;
    *(uint64_t *)(result + 0x8) = v_stack_m170;
    *(uint64_t *)(result) = v_stack_m178;
    *(uint64_t *)(v_stack_m170) = result;
    v_stack_m170 = result;
loc_00C73A8A:
    local_rbx = 0;
loc_00C73A8C:
    local_rdi = (result) + (32);
    goto loc_00C739F6;
loc_00C73A95:
    goto loc_00C739B5;
loc_00C73A9C:
    result = CmpAcquireShutdownRundown(v_stack_m178, Arg2, Arg2 + 64, 1);
    if ((uint8_t)(result) == 0) goto loc_00C73C78;
    result = CmpAttachToRegistryProcess(local_rsp - 232 + 128, Arg2, Arg2 + 64, 1);
    result = CmpLockRegistryExclusive(local_rsp - 232 + 128, Arg2, Arg2 + 64, 1);
    result = CmpAcquireSystemDriverHiveContext(local_rsp - 232, Arg2, Arg2 + 64, 1);
    if (sign_flag) goto loc_00C73C78;
    if ((*(uint64_t *)(local_rsp - 0xE8 + 0x60)) == 0) goto loc_00C73AEB;
    result = CmpAcquireSystemDriverHiveContext(local_rsp - 232 + 64, Arg2, Arg2 + 64, 1);
    if (sign_flag) goto loc_00C73C78;
loc_00C73AEB:
loc_00C73AF0:
    if (v_stack_m178 == v_stack_m178) goto loc_00C73B66;
    result = CmpAcquireSystemDriverHiveContext(v_stack_m178, Arg2, Arg2 + 64, 1);
    if (sign_flag) goto loc_00C73B5A;
    result = CmpAllocatePool(256, 48, (uint32_t)(0x20204D43ULL), 1);
    if (result == 0) goto loc_00C73C76;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = *(uint64_t *)(v_stack_m178 + 0x30);
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m178 + 0x38)));
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0xE8 - 0x78))) != (local_rsp - 232 - 128)) goto loc_00C73B5F;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(local_rsp - 0xE8 - 0x78);
    *(uint64_t *)(result) = local_rsp - 232 - 128;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xE8 - 0x78)) = result;
    *(uint64_t *)(local_rsp - 0xE8 - 0x78) = result;
loc_00C73B5A:
    goto loc_00C73AF0;
loc_00C73B5F:
loc_00C73B66:
    v_stack_m198 = *(uint64_t *)(local_rsp - 0xE8 - 0x30);
    v_stack_m1A8 = v_stack_m188;
    v_stack_m1C8 = local_rsp - 232 - 128;
    result = CmpFindDrivers(*(uint64_t *)(local_rsp - 0xE8 + 0x30), (uint32_t)(*(uint32_t *)(local_rsp - 0xE8 + 0x38)), *(uint64_t *)(local_rsp - 0xE8 + 0x70), (uint32_t)(*(uint32_t *)(local_rsp - 0xE8 + 0x78)));
    local_rbx = 0;
    if ((uint8_t)(result) == 0) goto loc_00C73C78;
    result = CmpSortDriverList(*(uint64_t *)(local_rsp - 0xE8 + 0x30), (uint32_t)(*(uint32_t *)(local_rsp - 0xE8 + 0x38)), v_stack_m188, (uint32_t)(*(uint32_t *)(local_rsp - 0xE8 + 0x78)));
    if ((uint8_t)(result) == 0) goto loc_00C73C78;
    result = CmpUnlockRegistry(*(uint64_t *)(local_rsp - 0xE8 + 0x30), (uint32_t)(*(uint32_t *)(local_rsp - 0xE8 + 0x38)), v_stack_m188, (uint32_t)(*(uint32_t *)(local_rsp - 0xE8 + 0x78)));
    if (v_stack_m188 == v_stack_m188) goto loc_00C73BE1;
loc_00C73BD2:
    Arg2 = (uint32_t)((0) + 1);
    if ((*(uint64_t *)(v_stack_m188)) != v_stack_m188) goto loc_00C73BD2;
loc_00C73BE1:
    Arg2 = (uint32_t)((Arg2) + 1);
    Arg2 = (Arg2) << (3);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x32384D43ULL), (uint32_t)(*(uint32_t *)(local_rsp - 0xE8 + 0x78)));
    if (result == 0) {
        a4 = 0;
        v_stack_m1C8 = 0;
        Arg2 = result + 2;
        Arg1 = result + 103;
        a3 = result + 1;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    goto loc_00C73C62;
loc_00C73C1E:
    *(uint64_t *)(local_rsp - 0xE8 - 0x50) = v_stack_m188 + 32;
    *(uint32_t *)(local_rsp - 0xE8 - 0x60) = 48;
    *(uint32_t *)(local_rsp - 0xE8 - 0x48) = 576;
    *(uint64_t *)(local_rsp - 0xE8 - 0x40) = v_xmm0;
    result = ZwOpenKey(result + 0 * 8, (uint32_t)(0x2001FULL), local_rsp - 232 - 96, a4);
    Arg1 = local_rbx + 1;
    if (sign_flag) { Arg1 = 0; }
loc_00C73C62:
    if ((*(uint64_t *)(v_stack_m188)) != v_stack_m188) goto loc_00C73C1E;
    local_rbx = 0;
    *(uint64_t *)(result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) * 8) = 0;
    goto loc_00C73C78;
loc_00C73C76:
    local_rbx = 0;
loc_00C73C78:
    result = v_stack_m188;
    if (v_stack_m188 != v_stack_m188) {
        Arg1 = *(uint64_t *)(local_rsp - 0xE8 + 0x30);
        Arg2 = v_stack_m188;
        result = CmpFreeDriverList(Arg1, Arg2, local_rsp - 232 - 96, a4);
    }
    if (0 != 0) {
        result = CmpUnlockRegistry(Arg1, Arg2, local_rsp - 232 - 96, a4);
    }
    if (1 != 0) {
        Arg1 = local_rsp - 232 + 128;
        result = CmpDetachFromRegistryProcess(Arg1, Arg2, local_rsp - 232 - 96, a4);
    }
    if ((uint8_t)((uint8_t)(result)) != 0) {
        result = CmpReleaseShutdownRundown(Arg1, Arg2, local_rsp - 232 - 96, a4);
    }
    result = CmpCloseSystemDriverHiveContext(local_rsp - 232, Arg2, local_rsp - 232 - 96, a4);
    if ((*(uint64_t *)(local_rsp - 0xE8 + 0x60)) != 0) {
        Arg1 = local_rsp - 232 + 64;
        result = CmpCloseSystemDriverHiveContext(Arg1, Arg2, local_rsp - 232 - 96, a4);
    }
    if (*(uint64_t *)(local_rsp - 0xE8 - 0x68) != 0) {
        result = ZwClose(*(uint64_t *)(local_rsp - 0xE8 - 0x68), Arg2, local_rsp - 232 - 96, a4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, local_rsp - 232 - 96, a4);
    }
    if (v_stack_m178 == v_stack_m178) goto loc_00C73D1D;
loc_00C73CFB:
    result = CmpCloseSystemDriverHiveContext(v_stack_m178, Arg2, local_rsp - 232 - 96, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m178, Arg2, local_rsp - 232 - 96, a4);
    if ((*(uint64_t *)(v_stack_m178)) != v_stack_m178) goto loc_00C73CFB;
loc_00C73D1D:
    if ((*(uint64_t *)(local_rsp - 0xE8 - 0x80)) == (local_rsp - 232 - 128)) goto loc_00C73D40;
loc_00C73D2A:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xE8 - 0x80), Arg2, local_rsp - 232 - 96, a4);
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0xE8 - 0x80))) != (local_rsp - 232 - 128)) goto loc_00C73D2A;
loc_00C73D40:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6E8) = *(uint64_t *)(local_rsp - 0xE8 - 0x18);
    Arg1 = (*(uint64_t *)(local_rsp - 0xE8 + 0xB0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), local_rsp - 232 - 96, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C7380C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
