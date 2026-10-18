# EtwpUpdateGuidFilterData

- RVA: `0x009FD214`–`0x009FD693` (길이 `1,151` bytes)
- VA: `0x00000001409FD214`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A7264`
- 디코드: `294`개 명령, `1,151/1,151` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009FD512` → [EtwpUpdateEventFilterAndFree](../70/EtwpUpdateEventFilterAndFree_function_00700B94.md) (function, `0x00700B94`)
- `0x009FD525` → [KeGenericCallDpc](../../text/49/KeGenericCallDpc_function_0049F980.md) (function, `0x0049F980`)
- `0x009FD53D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009FD54A` → [EtwpFreeEventNameFilter](EtwpFreeEventNameFilter_function_009FD69C.md) (function, `0x009FD69C`)
- `0x009FD581` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009FD59D` → [EtwpUpdateEventFilterAndFree](../70/EtwpUpdateEventFilterAndFree_function_00700B94.md) (function, `0x00700B94`)
- `0x009FD5B9` → [EtwpUpdateEventFilterAndFree](../70/EtwpUpdateEventFilterAndFree_function_00700B94.md) (function, `0x00700B94`)
- `0x009FD5D5` → [EtwpUpdateEventFilterAndFree](../70/EtwpUpdateEventFilterAndFree_function_00700B94.md) (function, `0x00700B94`)
- `0x009FD5F1` → [EtwpUpdateEventFilterAndFree](../70/EtwpUpdateEventFilterAndFree_function_00700B94.md) (function, `0x00700B94`)
- `0x009FD60B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009FD66D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009FD67A` → [EtwpFreeEventNameFilter](EtwpFreeEventNameFilter_function_009FD69C.md) (function, `0x009FD69C`)
- `0x009FD689` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [EtwpClearSessionAndUnreferenceEntry](../8C/EtwpClearSessionAndUnreferenceEntry_function_008C1438.md) at `0x008C1665`
- [EtwpUpdateGuidEnableInfo](EtwpUpdateGuidEnableInfo_function_009FCF48.md) at `0x009FD0A2`
- [EtwpUpdateGuidEnableInfo](EtwpUpdateGuidEnableInfo_function_009FCF48.md) at `0x009FD178`

### Static image references
- `0x009FD51E` → RVA `0x004A6860` (`EtwpSynchronizationDpc`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x009FD525` → [KeGenericCallDpc](../../text/49/KeGenericCallDpc_function_0049F980.md) (`PAGE` → `.text`)
  - `0x009FD53D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009FD581` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009FD60B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009FD66D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009FD689` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009FD64E` → [sub_00B326BC](../B3/Unknown_function_00B326BC.md) (`tail-transfer`)
  - `0x009FD663` → [sub_00B326BC](../B3/Unknown_function_00B326BC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009FD214  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
009FD219  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
009FD21D  55                              push rbp
009FD21E  56                              push rsi
009FD21F  57                              push rdi
009FD220  41 54                           push r12
009FD222  41 55                           push r13
009FD224  41 56                           push r14
009FD226  41 57                           push r15
009FD228  48 83 EC 30                     sub rsp, 0x30
009FD22C  45 8B 31                        mov r14d, dword ptr [r9]
009FD22F  33 DB                           xor ebx, ebx
009FD231  4C 8B F9                        mov r15, rcx
009FD234  8B FA                           mov edi, edx
009FD236  48 8B 89 80 02 00 00            mov rcx, qword ptr [rcx + 0x280]
009FD23D  49 8B F1                        mov rsi, r9
009FD240  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
009FD245  44 8B EB                        mov r13d, ebx
009FD248  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
009FD24D  44 8B E3                        mov r12d, ebx
009FD250  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
009FD258  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
009FD25D  48 85 C9                        test rcx, rcx
009FD260  75 37                           jne 0x1409fd299
009FD262  45 85 F6                        test r14d, r14d
009FD265  41 0F B6 C0                     movzx eax, r8b
009FD269  8D 4B 01                        lea ecx, [rbx + 1]
009FD26C  0F 45 C8                        cmovne ecx, eax
009FD26F  84 C9                           test cl, cl
009FD271  0F 84 84 03 00 00               je 0x1409fd5fb
009FD277  33 C0                           xor eax, eax
009FD279  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
009FD281  48 83 C4 30                     add rsp, 0x30
009FD285  41 5F                           pop r15
009FD287  41 5E                           pop r14
009FD289  41 5D                           pop r13
009FD28B  41 5C                           pop r12
009FD28D  5F                              pop rdi
009FD28E  5E                              pop rsi
009FD28F  5D                              pop rbp
009FD290  C3                              ret
009FD291  CC                              int3
009FD292  49 89 87 80 02 00 00            mov qword ptr [r15 + 0x280], rax
009FD299  48 6B EF 68                     imul rbp, rdi, 0x68
009FD29D  8B FB                           mov edi, ebx
009FD29F  87 3C 29                        xchg dword ptr [rcx + rbp], edi
009FD2A2  B9 04 00 00 80                  mov ecx, 0x80000004
009FD2A7  8B C7                           mov eax, edi
009FD2A9  23 C1                           and eax, ecx
009FD2AB  3B C1                           cmp eax, ecx
009FD2AD  0F 84 4D 02 00 00               je 0x1409fd500
009FD2B3  41 8B C6                        mov eax, r14d
009FD2B6  23 C1                           and eax, ecx
009FD2B8  3B C1                           cmp eax, ecx
009FD2BA  0F 84 40 02 00 00               je 0x1409fd500
009FD2C0  B9 08 00 00 80                  mov ecx, 0x80000008
009FD2C5  8B C7                           mov eax, edi
009FD2C7  23 C1                           and eax, ecx
009FD2C9  3B C1                           cmp eax, ecx
009FD2CB  0F 84 0E 03 00 00               je 0x1409fd5df
009FD2D1  41 8B C6                        mov eax, r14d
009FD2D4  23 C1                           and eax, ecx
009FD2D6  3B C1                           cmp eax, ecx
009FD2D8  0F 84 01 03 00 00               je 0x1409fd5df
009FD2DE  B9 10 00 00 80                  mov ecx, 0x80000010
009FD2E3  8B C7                           mov eax, edi
009FD2E5  23 C1                           and eax, ecx
009FD2E7  3B C1                           cmp eax, ecx
009FD2E9  0F 84 9C 02 00 00               je 0x1409fd58b
009FD2EF  41 8B C6                        mov eax, r14d
009FD2F2  23 C1                           and eax, ecx
009FD2F4  3B C1                           cmp eax, ecx
009FD2F6  0F 84 8F 02 00 00               je 0x1409fd58b
009FD2FC  B9 20 00 00 80                  mov ecx, 0x80000020
009FD301  8B C7                           mov eax, edi
009FD303  23 C1                           and eax, ecx
009FD305  3B C1                           cmp eax, ecx
009FD307  0F 84 9A 02 00 00               je 0x1409fd5a7
009FD30D  41 8B C6                        mov eax, r14d
009FD310  23 C1                           and eax, ecx
009FD312  3B C1                           cmp eax, ecx
009FD314  0F 84 8D 02 00 00               je 0x1409fd5a7
009FD31A  B9 00 80 00 80                  mov ecx, 0x80008000
009FD31F  8B C7                           mov eax, edi
009FD321  23 C1                           and eax, ecx
009FD323  3B C1                           cmp eax, ecx
009FD325  0F 84 98 02 00 00               je 0x1409fd5c3
009FD32B  41 8B C6                        mov eax, r14d
009FD32E  23 C1                           and eax, ecx
009FD330  3B C1                           cmp eax, ecx
009FD332  0F 84 8B 02 00 00               je 0x1409fd5c3
009FD338  B9 00 10 00 80                  mov ecx, 0x80001000
009FD33D  8B C7                           mov eax, edi
009FD33F  23 C1                           and eax, ecx
009FD341  3B C1                           cmp eax, ecx
009FD343  0F 84 DD 02 00 00               je 0x1409fd626
009FD349  41 8B C6                        mov eax, r14d
009FD34C  23 C1                           and eax, ecx
009FD34E  3B C1                           cmp eax, ecx
009FD350  0F 84 D0 02 00 00               je 0x1409fd626
009FD356  B9 00 02 00 80                  mov ecx, 0x80000200
009FD35B  8B C7                           mov eax, edi
009FD35D  23 C1                           and eax, ecx
009FD35F  3B C1                           cmp eax, ecx
009FD361  0F 85 25 01 00 00               jne 0x1409fd48c
009FD367  49 8B 87 80 02 00 00            mov rax, qword ptr [r15 + 0x280]
009FD36E  48 8B 4E 48                     mov rcx, qword ptr [rsi + 0x48]
009FD372  48 87 4C 28 48                  xchg qword ptr [rax + rbp + 0x48], rcx
009FD377  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009FD37C  48 89 5E 48                     mov qword ptr [rsi + 0x48], rbx
009FD380  B9 00 04 00 80                  mov ecx, 0x80000400
009FD385  8B C7                           mov eax, edi
009FD387  23 C1                           and eax, ecx
009FD389  3B C1                           cmp eax, ecx
009FD38B  0F 85 0D 01 00 00               jne 0x1409fd49e
009FD391  49 8B 87 80 02 00 00            mov rax, qword ptr [r15 + 0x280]
009FD398  48 8B 4E 60                     mov rcx, qword ptr [rsi + 0x60]
009FD39C  48 87 4C 28 60                  xchg qword ptr [rax + rbp + 0x60], rcx
009FD3A1  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
009FD3A9  48 89 5E 60                     mov qword ptr [rsi + 0x60], rbx
009FD3AD  B9 00 20 00 80                  mov ecx, 0x80002000
009FD3B2  8B C7                           mov eax, edi
009FD3B4  23 C1                           and eax, ecx
009FD3B6  3B C1                           cmp eax, ecx
009FD3B8  0F 84 F2 00 00 00               je 0x1409fd4b0
009FD3BE  41 8B C6                        mov eax, r14d
009FD3C1  23 C1                           and eax, ecx
009FD3C3  3B C1                           cmp eax, ecx
009FD3C5  0F 84 E5 00 00 00               je 0x1409fd4b0
009FD3CB  B9 00 40 00 80                  mov ecx, 0x80004000
009FD3D0  8B C7                           mov eax, edi
009FD3D2  23 C1                           and eax, ecx
009FD3D4  3B C1                           cmp eax, ecx
009FD3D6  0F 84 06 01 00 00               je 0x1409fd4e2
009FD3DC  41 8B C6                        mov eax, r14d
009FD3DF  23 C1                           and eax, ecx
009FD3E1  3B C1                           cmp eax, ecx
009FD3E3  0F 84 F9 00 00 00               je 0x1409fd4e2
009FD3E9  B9 00 01 00 80                  mov ecx, 0x80000100
009FD3EE  23 F9                           and edi, ecx
009FD3F0  3B F9                           cmp edi, ecx
009FD3F2  0F 84 D1 00 00 00               je 0x1409fd4c9
009FD3F8  41 8B C6                        mov eax, r14d
009FD3FB  23 C1                           and eax, ecx
009FD3FD  3B C1                           cmp eax, ecx
009FD3FF  0F 84 C4 00 00 00               je 0x1409fd4c9
009FD405  49 8B 87 80 02 00 00            mov rax, qword ptr [r15 + 0x280]
009FD40C  48 8D 56 58                     lea rdx, [rsi + 0x58]
009FD410  48 39 5C 28 58                  cmp qword ptr [rax + rbp + 0x58], rbx
009FD415  0F 85 29 02 00 00               jne 0x1409fd644
009FD41B  48 39 1A                        cmp qword ptr [rdx], rbx
009FD41E  0F 85 20 02 00 00               jne 0x1409fd644
009FD424  8B 7C 24 78                     mov edi, dword ptr [rsp + 0x78]
009FD428  48 8B 6C 24 20                  mov rbp, qword ptr [rsp + 0x20]
009FD42D  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
009FD432  8B C7                           mov eax, edi
009FD434  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
009FD43C  48 6B C8 68                     imul rcx, rax, 0x68
009FD440  49 03 8F 80 02 00 00            add rcx, qword ptr [r15 + 0x280]
009FD447  44 87 31                        xchg dword ptr [rcx], r14d
009FD44A  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
009FD44F  4D 85 F6                        test r14, r14
009FD452  0F 85 C4 00 00 00               jne 0x1409fd51c
009FD458  48 85 ED                        test rbp, rbp
009FD45B  0F 85 BB 00 00 00               jne 0x1409fd51c
009FD461  48 85 FF                        test rdi, rdi
009FD464  0F 85 B2 00 00 00               jne 0x1409fd51c
009FD46A  4D 85 ED                        test r13, r13
009FD46D  0F 85 A9 00 00 00               jne 0x1409fd51c
009FD473  48 85 F6                        test rsi, rsi
009FD476  0F 85 A0 00 00 00               jne 0x1409fd51c
009FD47C  4D 85 E4                        test r12, r12
009FD47F  0F 85 97 00 00 00               jne 0x1409fd51c
009FD485  8B C3                           mov eax, ebx
009FD487  E9 ED FD FF FF                  jmp 0x1409fd279
009FD48C  41 8B C6                        mov eax, r14d
009FD48F  23 C1                           and eax, ecx
009FD491  3B C1                           cmp eax, ecx
009FD493  0F 85 E7 FE FF FF               jne 0x1409fd380
009FD499  E9 C9 FE FF FF                  jmp 0x1409fd367
009FD49E  41 8B C6                        mov eax, r14d
009FD4A1  23 C1                           and eax, ecx
009FD4A3  3B C1                           cmp eax, ecx
009FD4A5  0F 85 02 FF FF FF               jne 0x1409fd3ad
009FD4AB  E9 E1 FE FF FF                  jmp 0x1409fd391
009FD4B0  49 8B 87 80 02 00 00            mov rax, qword ptr [r15 + 0x280]
009FD4B7  4C 8B 6E 38                     mov r13, qword ptr [rsi + 0x38]
009FD4BB  4C 87 6C 28 38                  xchg qword ptr [rax + rbp + 0x38], r13
009FD4C0  48 89 5E 38                     mov qword ptr [rsi + 0x38], rbx
009FD4C4  E9 02 FF FF FF                  jmp 0x1409fd3cb
009FD4C9  49 8B 87 80 02 00 00            mov rax, qword ptr [r15 + 0x280]
009FD4D0  4C 8B 66 50                     mov r12, qword ptr [rsi + 0x50]
009FD4D4  4C 87 64 28 50                  xchg qword ptr [rax + rbp + 0x50], r12
009FD4D9  48 89 5E 50                     mov qword ptr [rsi + 0x50], rbx
009FD4DD  E9 23 FF FF FF                  jmp 0x1409fd405
009FD4E2  49 8B 87 80 02 00 00            mov rax, qword ptr [r15 + 0x280]
009FD4E9  48 8B 4E 40                     mov rcx, qword ptr [rsi + 0x40]
009FD4ED  48 87 4C 28 40                  xchg qword ptr [rax + rbp + 0x40], rcx
009FD4F2  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
009FD4F7  48 89 5E 40                     mov qword ptr [rsi + 0x40], rbx
009FD4FB  E9 E9 FE FF FF                  jmp 0x1409fd3e9
009FD500  49 8B 8F 80 02 00 00            mov rcx, qword ptr [r15 + 0x280]
009FD507  48 8D 56 08                     lea rdx, [rsi + 8]
009FD50B  48 83 C1 08                     add rcx, 8
009FD50F  48 03 CD                        add rcx, rbp
009FD512  E8 7D 36 D0 FF                  call 0x140700b94
009FD517  E9 A4 FD FF FF                  jmp 0x1409fd2c0
009FD51C  33 D2                           xor edx, edx
009FD51E  48 8D 0D 3B 93 AA FF            lea rcx, [rip - 0x556cc5]
009FD525  E8 56 24 AA FF                  call 0x14049f980
009FD52A  4D 85 F6                        test r14, r14
009FD52D  0F 85 35 01 00 00               jne 0x1409fd668
009FD533  48 85 ED                        test rbp, rbp
009FD536  74 0A                           je 0x1409fd542
009FD538  33 D2                           xor edx, edx
009FD53A  48 8B CD                        mov rcx, rbp
009FD53D  E8 2E 53 18 00                  call 0x140b82870
009FD542  48 85 FF                        test rdi, rdi
009FD545  74 08                           je 0x1409fd54f
009FD547  48 8B CF                        mov rcx, rdi
009FD54A  E8 4D 01 00 00                  call 0x1409fd69c
009FD54F  4D 85 ED                        test r13, r13
009FD552  0F 85 1F 01 00 00               jne 0x1409fd677
009FD558  48 85 F6                        test rsi, rsi
009FD55B  0F 85 23 01 00 00               jne 0x1409fd684
009FD561  4D 85 E4                        test r12, r12
009FD564  0F 84 1B FF FF FF               je 0x1409fd485
009FD56A  83 CA FF                        or edx, 0xffffffff
009FD56D  F0 41 0F C1 14 24               lock xadd dword ptr [r12], edx
009FD573  83 FA 01                        cmp edx, 1
009FD576  0F 85 09 FF FF FF               jne 0x1409fd485
009FD57C  33 D2                           xor edx, edx
009FD57E  49 8B CC                        mov rcx, r12
009FD581  E8 EA 52 18 00                  call 0x140b82870
009FD586  E9 FA FE FF FF                  jmp 0x1409fd485
009FD58B  49 8B 8F 80 02 00 00            mov rcx, qword ptr [r15 + 0x280]
009FD592  48 8D 56 18                     lea rdx, [rsi + 0x18]
009FD596  48 83 C1 18                     add rcx, 0x18
009FD59A  48 03 CD                        add rcx, rbp
009FD59D  E8 F2 35 D0 FF                  call 0x140700b94
009FD5A2  E9 55 FD FF FF                  jmp 0x1409fd2fc
009FD5A7  49 8B 8F 80 02 00 00            mov rcx, qword ptr [r15 + 0x280]
009FD5AE  48 8D 56 20                     lea rdx, [rsi + 0x20]
009FD5B2  48 83 C1 20                     add rcx, 0x20
009FD5B6  48 03 CD                        add rcx, rbp
009FD5B9  E8 D6 35 D0 FF                  call 0x140700b94
009FD5BE  E9 57 FD FF FF                  jmp 0x1409fd31a
009FD5C3  49 8B 8F 80 02 00 00            mov rcx, qword ptr [r15 + 0x280]
009FD5CA  48 8D 56 28                     lea rdx, [rsi + 0x28]
009FD5CE  48 83 C1 28                     add rcx, 0x28
009FD5D2  48 03 CD                        add rcx, rbp
009FD5D5  E8 BA 35 D0 FF                  call 0x140700b94
009FD5DA  E9 59 FD FF FF                  jmp 0x1409fd338
009FD5DF  49 8B 8F 80 02 00 00            mov rcx, qword ptr [r15 + 0x280]
009FD5E6  48 8D 56 10                     lea rdx, [rsi + 0x10]
009FD5EA  48 83 C1 10                     add rcx, 0x10
009FD5EE  48 03 CD                        add rcx, rbp
009FD5F1  E8 9E 35 D0 FF                  call 0x140700b94
009FD5F6  E9 E3 FC FF FF                  jmp 0x1409fd2de
009FD5FB  BA 80 06 00 00                  mov edx, 0x680
009FD600  B9 40 00 00 00                  mov ecx, 0x40
009FD605  41 B8 45 74 77 46               mov r8d, 0x46777445
009FD60B  E8 E0 4A 18 00                  call 0x140b820f0
009FD610  48 8B C8                        mov rcx, rax
009FD613  48 85 C0                        test rax, rax
009FD616  0F 85 76 FC FF FF               jne 0x1409fd292
009FD61C  BB 17 00 00 C0                  mov ebx, 0xc0000017
009FD621  E9 5F FE FF FF                  jmp 0x1409fd485
009FD626  49 8B 87 80 02 00 00            mov rax, qword ptr [r15 + 0x280]
009FD62D  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
009FD631  48 87 4C 28 30                  xchg qword ptr [rax + rbp + 0x30], rcx
009FD636  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
009FD63B  48 89 5E 30                     mov qword ptr [rsi + 0x30], rbx
009FD63F  E9 12 FD FF FF                  jmp 0x1409fd356
009FD644  48 8B 02                        mov rax, qword ptr [rdx]
009FD647  8B 7C 24 78                     mov edi, dword ptr [rsp + 0x78]
009FD64B  48 85 C0                        test rax, rax
009FD64E  0F 84 68 50 13 00               je 0x140b326bc
009FD654  8B CF                           mov ecx, edi
009FD656  41 B8 01 00 00 00               mov r8d, 1
009FD65C  49 D3 E0                        shl r8, cl
009FD65F  4C 89 40 08                     mov qword ptr [rax + 8], r8
009FD663  E9 54 50 13 00                  jmp 0x140b326bc
009FD668  33 D2                           xor edx, edx
009FD66A  49 8B CE                        mov rcx, r14
009FD66D  E8 FE 51 18 00                  call 0x140b82870
009FD672  E9 BC FE FF FF                  jmp 0x1409fd533
009FD677  49 8B CD                        mov rcx, r13
009FD67A  E8 1D 00 00 00                  call 0x1409fd69c
009FD67F  E9 D4 FE FF FF                  jmp 0x1409fd558
009FD684  33 D2                           xor edx, edx
009FD686  48 8B CE                        mov rcx, rsi
009FD689  E8 E2 51 18 00                  call 0x140b82870
009FD68E  E9 CE FE FF FF                  jmp 0x1409fd561
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpUpdateGuidFilterData(__int64 a1, int a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p88;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (48);
    v_rbx = 0;
    v_stack_m40 = 0;
    v_stack_m48 = 0;
    v_stack_p20 = 0;
    v_stack_p8 = 0;
    if (*(unsigned __int64 *)(a1 + 640) != 0) goto loc_009FD299;
    a1 = v_rbx + 1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a4))) != 0) { a1 = a3; }
    if ((unsigned __int8)(a1) == 0) goto loc_009FD5FB;
    result = 0;
loc_009FD279:
    v_rsp = (v_rsp) + (48);
    return result;
loc_009FD292:
    *(unsigned __int64 *)(a1 + 640) = 0;
loc_009FD299:
    v_rbp = (v_rbp) * ((unsigned int)(a2));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) & ((unsigned int)((unsigned int)(0x80000004ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000004ULL)))) goto loc_009FD500;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000004ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000004ULL)))) goto loc_009FD500;
loc_009FD2C0:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) & ((unsigned int)((unsigned int)(0x80000008ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000008ULL)))) goto loc_009FD5DF;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000008ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000008ULL)))) goto loc_009FD5DF;
loc_009FD2DE:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) & ((unsigned int)((unsigned int)(0x80000010ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000010ULL)))) goto loc_009FD58B;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000010ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000010ULL)))) goto loc_009FD58B;
loc_009FD2FC:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) & ((unsigned int)((unsigned int)(0x80000020ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000020ULL)))) goto loc_009FD5A7;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000020ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000020ULL)))) goto loc_009FD5A7;
loc_009FD31A:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) & ((unsigned int)((unsigned int)(0x80008000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80008000ULL)))) goto loc_009FD5C3;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80008000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80008000ULL)))) goto loc_009FD5C3;
loc_009FD338:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) & ((unsigned int)((unsigned int)(0x80001000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80001000ULL)))) goto loc_009FD626;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80001000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80001000ULL)))) goto loc_009FD626;
loc_009FD356:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) & ((unsigned int)((unsigned int)(0x80000200ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x80000200ULL)))) goto loc_009FD48C;
loc_009FD367:
    v_stack_p20 = *(unsigned __int64 *)(a4 + 72);
    *(unsigned __int64 *)(a4 + 72) = v_stack_p18;
loc_009FD380:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) & ((unsigned int)((unsigned int)(0x80000400ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x80000400ULL)))) goto loc_009FD49E;
loc_009FD391:
    v_stack_p88 = *(unsigned __int64 *)(a4 + 96);
    *(unsigned __int64 *)(a4 + 96) = v_stack_p18;
loc_009FD3AD:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) & ((unsigned int)((unsigned int)(0x80002000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80002000ULL)))) goto loc_009FD4B0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80002000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80002000ULL)))) goto loc_009FD4B0;
loc_009FD3CB:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) & ((unsigned int)((unsigned int)(0x80004000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80004000ULL)))) goto loc_009FD4E2;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80004000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80004000ULL)))) goto loc_009FD4E2;
loc_009FD3E9:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) & ((unsigned int)((unsigned int)(0x80000100ULL))));
    if (((unsigned int)(v_rdi)) == ((unsigned int)((unsigned int)(0x80000100ULL)))) goto loc_009FD4C9;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & ((unsigned int)((unsigned int)(0x80000100ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000100ULL)))) goto loc_009FD4C9;
loc_009FD405:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640) + v_rbp * 1 + 88)) != v_stack_p18) goto loc_009FD644;
    if ((*(unsigned __int64 *)(a4 + 88)) != v_stack_p18) goto loc_009FD644;
    a1 = ((unsigned int)(0x80000100ULL)) * ((unsigned int)((unsigned int)((unsigned int)(v_stack_p78))));
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 640));
    if (v_stack_p28 != 0) goto loc_009FD51C;
    if (v_stack_p20 != 0) goto loc_009FD51C;
    if (v_stack_p88 != 0) goto loc_009FD51C;
    if (0 != 0) goto loc_009FD51C;
    if (v_stack_p70 != 0) goto loc_009FD51C;
    if (0 != 0) goto loc_009FD51C;
loc_009FD485:
    goto loc_009FD279;
loc_009FD48C:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p28))) & ((unsigned int)(a1)));
    if (((unsigned int)(result)) != ((unsigned int)(a1))) goto loc_009FD380;
    goto loc_009FD367;
loc_009FD49E:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p28))) & ((unsigned int)(a1)));
    if (((unsigned int)(result)) != ((unsigned int)(a1))) goto loc_009FD3AD;
    goto loc_009FD391;
loc_009FD4B0:
    *(unsigned __int64 *)(v_stack_p70 + 56) = v_stack_p18;
    goto loc_009FD3CB;
loc_009FD4C9:
    *(unsigned __int64 *)(v_stack_p70 + 80) = v_stack_p18;
    goto loc_009FD405;
loc_009FD4E2:
    v_stack_p70 = *(unsigned __int64 *)(v_stack_p70 + 64);
    *(unsigned __int64 *)(v_stack_p70 + 64) = v_stack_p18;
    goto loc_009FD3E9;
loc_009FD500:
    a1 = (*(unsigned __int64 *)(a1 + 640)) + (8);
    a1 = (a1) + (v_stack_p20);
    result = EtwpUpdateEventFilterAndFree(a1, v_stack_p70 + 8, a3, a4);
    goto loc_009FD2C0;
loc_009FD51C:
    a2 = 0;
    result = KeGenericCallDpc(v_rip - 5598405, a2, a3, a4);
    if (v_stack_p28 != 0) goto loc_009FD668;
loc_009FD533:
    if (v_stack_p20 != 0) {
        a2 = 0;
        a1 = v_stack_p20;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (v_stack_p88 != 0) {
        a1 = v_stack_p88;
        result = EtwpFreeEventNameFilter(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_stack_p70 + 56) != 0) goto loc_009FD677;
loc_009FD558:
    if (v_stack_p70 != 0) goto loc_009FD684;
loc_009FD561:
    if (*(unsigned __int64 *)(v_stack_p70 + 80) == 0) goto loc_009FD485;
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    if (a2 != 1) goto loc_009FD485;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p70 + 80), a2, a3, a4);
    goto loc_009FD485;
loc_009FD58B:
    a1 = (*(unsigned __int64 *)(a1 + 640)) + (24);
    a1 = (a1) + (v_stack_p20);
    result = EtwpUpdateEventFilterAndFree(a1, v_stack_p70 + 24, a3, a4);
    goto loc_009FD2FC;
loc_009FD5A7:
    a1 = (*(unsigned __int64 *)(a1 + 640)) + (32);
    a1 = (a1) + (v_stack_p20);
    result = EtwpUpdateEventFilterAndFree(a1, v_stack_p70 + 32, a3, a4);
    goto loc_009FD31A;
loc_009FD5C3:
    a1 = (*(unsigned __int64 *)(a1 + 640)) + (40);
    a1 = (a1) + (v_stack_p20);
    result = EtwpUpdateEventFilterAndFree(a1, v_stack_p70 + 40, a3, a4);
    goto loc_009FD338;
loc_009FD5DF:
    a1 = (*(unsigned __int64 *)(a1 + 640)) + (16);
    a1 = (a1) + (v_stack_p20);
    result = EtwpUpdateEventFilterAndFree(a1, v_stack_p70 + 16, a3, a4);
    goto loc_009FD2DE;
loc_009FD5FB:
    result = ExAllocatePool2(64, (unsigned int)(0x680ULL), (unsigned int)(0x46777445ULL), a4);
    if (result != 0) goto loc_009FD292;
    goto loc_009FD485;
loc_009FD626:
    v_stack_p28 = *(unsigned __int64 *)(v_stack_p70 + 48);
    *(unsigned __int64 *)(v_stack_p70 + 48) = (unsigned int)(0xC0000017ULL);
    goto loc_009FD356;
loc_009FD644:
    a3 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(v_stack_p78)))));
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0x680ULL)) + 8) = a3;
loc_009FD668:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p28, a2, a3, a4);
    goto loc_009FD533;
loc_009FD677:
    result = EtwpFreeEventNameFilter(*(unsigned __int64 *)(v_stack_p70 + 56), a2, a3, a4);
    goto loc_009FD558;
loc_009FD684:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p70, a2, a3, a4);
    goto loc_009FD561;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpUpdateGuidFilterData(void *Arg1, int32_t Arg2, uint8_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p88;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (48);
    local_rbx = 0;
    v_stack_m40 = 0;
    v_stack_m48 = 0;
    v_stack_p20 = 0;
    v_stack_p8 = 0;
    if (*(uint64_t *)(arg1 + 0x280) != 0) goto loc_009FD299;
    Arg1 = local_rbx + 1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))) != 0) { Arg1 = Arg3; }
    if ((uint8_t)(Arg1) == 0) goto loc_009FD5FB;
    result = 0;
loc_009FD279:
    local_rsp = (local_rsp) + (48);
    return result;
loc_009FD292:
    *(uint64_t *)(arg1 + 0x280) = 0;
loc_009FD299:
    local_rbp = (local_rbp) * ((uint32_t)(Arg2));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) & ((uint32_t)((uint32_t)(0x80000004ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000004ULL)))) goto loc_009FD500;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000004ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000004ULL)))) goto loc_009FD500;
loc_009FD2C0:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) & ((uint32_t)((uint32_t)(0x80000008ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000008ULL)))) goto loc_009FD5DF;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000008ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000008ULL)))) goto loc_009FD5DF;
loc_009FD2DE:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) & ((uint32_t)((uint32_t)(0x80000010ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000010ULL)))) goto loc_009FD58B;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000010ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000010ULL)))) goto loc_009FD58B;
loc_009FD2FC:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) & ((uint32_t)((uint32_t)(0x80000020ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000020ULL)))) goto loc_009FD5A7;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000020ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000020ULL)))) goto loc_009FD5A7;
loc_009FD31A:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) & ((uint32_t)((uint32_t)(0x80008000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80008000ULL)))) goto loc_009FD5C3;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80008000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80008000ULL)))) goto loc_009FD5C3;
loc_009FD338:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) & ((uint32_t)((uint32_t)(0x80001000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80001000ULL)))) goto loc_009FD626;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80001000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80001000ULL)))) goto loc_009FD626;
loc_009FD356:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) & ((uint32_t)((uint32_t)(0x80000200ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x80000200ULL)))) goto loc_009FD48C;
loc_009FD367:
    v_stack_p20 = *(uint64_t *)(arg4 + 0x48);
    *(uint64_t *)(arg4 + 0x48) = v_stack_p18;
loc_009FD380:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) & ((uint32_t)((uint32_t)(0x80000400ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x80000400ULL)))) goto loc_009FD49E;
loc_009FD391:
    v_stack_p88 = *(uint64_t *)(arg4 + 0x60);
    *(uint64_t *)(arg4 + 0x60) = v_stack_p18;
loc_009FD3AD:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) & ((uint32_t)((uint32_t)(0x80002000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80002000ULL)))) goto loc_009FD4B0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80002000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80002000ULL)))) goto loc_009FD4B0;
loc_009FD3CB:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) & ((uint32_t)((uint32_t)(0x80004000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80004000ULL)))) goto loc_009FD4E2;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80004000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80004000ULL)))) goto loc_009FD4E2;
loc_009FD3E9:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) & ((uint32_t)((uint32_t)(0x80000100ULL))));
    if (((uint32_t)(local_rdi)) == ((uint32_t)((uint32_t)(0x80000100ULL)))) goto loc_009FD4C9;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & ((uint32_t)((uint32_t)(0x80000100ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000100ULL)))) goto loc_009FD4C9;
loc_009FD405:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x280) + local_rbp * 1 + 0x58)) != v_stack_p18) goto loc_009FD644;
    if ((*(uint64_t *)(arg4 + 0x58)) != v_stack_p18) goto loc_009FD644;
    Arg1 = ((uint32_t)(0x80000100ULL)) * ((uint32_t)((uint32_t)((uint32_t)(v_stack_p78))));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x280));
    if (v_stack_p28 != 0) goto loc_009FD51C;
    if (v_stack_p20 != 0) goto loc_009FD51C;
    if (v_stack_p88 != 0) goto loc_009FD51C;
    if (0 != 0) goto loc_009FD51C;
    if (v_stack_p70 != 0) goto loc_009FD51C;
    if (0 != 0) goto loc_009FD51C;
loc_009FD485:
    goto loc_009FD279;
loc_009FD48C:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p28))) & ((uint32_t)(Arg1)));
    if (((uint32_t)(result)) != ((uint32_t)(Arg1))) goto loc_009FD380;
    goto loc_009FD367;
loc_009FD49E:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p28))) & ((uint32_t)(Arg1)));
    if (((uint32_t)(result)) != ((uint32_t)(Arg1))) goto loc_009FD3AD;
    goto loc_009FD391;
loc_009FD4B0:
    *(uint64_t *)(v_stack_p70 + 0x38) = v_stack_p18;
    goto loc_009FD3CB;
loc_009FD4C9:
    *(uint64_t *)(v_stack_p70 + 0x50) = v_stack_p18;
    goto loc_009FD405;
loc_009FD4E2:
    v_stack_p70 = *(uint64_t *)(v_stack_p70 + 0x40);
    *(uint64_t *)(v_stack_p70 + 0x40) = v_stack_p18;
    goto loc_009FD3E9;
loc_009FD500:
    Arg1 = (*(uint64_t *)(arg1 + 0x280)) + (8);
    Arg1 = (Arg1) + (v_stack_p20);
    result = EtwpUpdateEventFilterAndFree(Arg1, v_stack_p70 + 8, Arg3, Arg4);
    goto loc_009FD2C0;
loc_009FD51C:
    Arg2 = 0;
    result = KeGenericCallDpc(v_rip - 5598405, Arg2, Arg3, Arg4);
    if (v_stack_p28 != 0) goto loc_009FD668;
loc_009FD533:
    if (v_stack_p20 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_p20;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_p88 != 0) {
        Arg1 = v_stack_p88;
        result = EtwpFreeEventNameFilter(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(v_stack_p70 + 0x38) != 0) goto loc_009FD677;
loc_009FD558:
    if (v_stack_p70 != 0) goto loc_009FD684;
loc_009FD561:
    if (*(uint64_t *)(v_stack_p70 + 0x50) == 0) goto loc_009FD485;
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    if (Arg2 != 1) goto loc_009FD485;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p70 + 0x50), Arg2, Arg3, Arg4);
    goto loc_009FD485;
loc_009FD58B:
    Arg1 = (*(uint64_t *)(arg1 + 0x280)) + (24);
    Arg1 = (Arg1) + (v_stack_p20);
    result = EtwpUpdateEventFilterAndFree(Arg1, v_stack_p70 + 24, Arg3, Arg4);
    goto loc_009FD2FC;
loc_009FD5A7:
    Arg1 = (*(uint64_t *)(arg1 + 0x280)) + (32);
    Arg1 = (Arg1) + (v_stack_p20);
    result = EtwpUpdateEventFilterAndFree(Arg1, v_stack_p70 + 32, Arg3, Arg4);
    goto loc_009FD31A;
loc_009FD5C3:
    Arg1 = (*(uint64_t *)(arg1 + 0x280)) + (40);
    Arg1 = (Arg1) + (v_stack_p20);
    result = EtwpUpdateEventFilterAndFree(Arg1, v_stack_p70 + 40, Arg3, Arg4);
    goto loc_009FD338;
loc_009FD5DF:
    Arg1 = (*(uint64_t *)(arg1 + 0x280)) + (16);
    Arg1 = (Arg1) + (v_stack_p20);
    result = EtwpUpdateEventFilterAndFree(Arg1, v_stack_p70 + 16, Arg3, Arg4);
    goto loc_009FD2DE;
loc_009FD5FB:
    result = ExAllocatePool2(64, (uint32_t)(0x680ULL), (uint32_t)(0x46777445ULL), Arg4);
    if (result != 0) goto loc_009FD292;
    goto loc_009FD485;
loc_009FD626:
    v_stack_p28 = *(uint64_t *)(v_stack_p70 + 0x30);
    *(uint64_t *)(v_stack_p70 + 0x30) = (uint32_t)(0xC0000017ULL);
    goto loc_009FD356;
loc_009FD644:
    Arg3 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p78)))));
    *(uint64_t *)(*(uint64_t *)((uint32_t)(0x680ULL)) + 0x8) = Arg3;
loc_009FD668:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p28, Arg2, Arg3, Arg4);
    goto loc_009FD533;
loc_009FD677:
    result = EtwpFreeEventNameFilter(*(uint64_t *)(v_stack_p70 + 0x38), Arg2, Arg3, Arg4);
    goto loc_009FD558;
loc_009FD684:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p70, Arg2, Arg3, Arg4);
    goto loc_009FD561;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x280` | `64` | `R` |
| `Arg1` | `+ 0x280` | `64` | `W` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x18` | `64` | `R` |
| `Arg4` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x28` | `64` | `R` |
| `Arg4` | `+ 0x30` | `64` | `R` |
| `Arg4` | `+ 0x30` | `64` | `W` |
| `Arg4` | `+ 0x38` | `64` | `R` |
| `Arg4` | `+ 0x38` | `64` | `W` |
| `Arg4` | `+ 0x40` | `64` | `R` |
| `Arg4` | `+ 0x40` | `64` | `W` |
| `Arg4` | `+ 0x48` | `64` | `R` |
| `Arg4` | `+ 0x48` | `64` | `W` |
| `Arg4` | `+ 0x50` | `64` | `R` |
| `Arg4` | `+ 0x50` | `64` | `W` |
| `Arg4` | `+ 0x58` | `64` | `R` |
| `Arg4` | `+ 0x60` | `64` | `R` |
| `Arg4` | `+ 0x60` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009FD214&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
