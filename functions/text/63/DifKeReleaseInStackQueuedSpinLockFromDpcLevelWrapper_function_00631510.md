# DifKeReleaseInStackQueuedSpinLockFromDpcLevelWrapper

- RVA: `0x00631510`–`0x00631660` (길이 `336` bytes)
- VA: `0x0000000140631510`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00631538` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00631560` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063158E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006315B5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006315CE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006315D6` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x006315FF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00631626` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063163F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00631572` → RVA `0x00F048B8` (`.data`; read)
- `0x0063157B` → RVA `0x00F04980` (`.data`; read)
- `0x00631587` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00631510  48 8B C4                        mov rax, rsp
00631513  48 89 58 08                     mov qword ptr [rax + 8], rbx
00631517  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063151B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063151F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00631523  41 56                           push r14
00631525  48 83 EC 30                     sub rsp, 0x30
00631529  48 8B E9                        mov rbp, rcx
0063152C  0F 57 C0                        xorps xmm0, xmm0
0063152F  B9 06 01 00 00                  mov ecx, 0x106
00631534  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00631538  E8 F7 44 E6 FF                  call 0x140495a34
0063153D  48 8B F8                        mov rdi, rax
00631540  48 85 C0                        test rax, rax
00631543  0F 84 8A 00 00 00               je 0x1406315d3
00631549  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063154C  A8 18                           test al, 0x18
0063154E  74 0C                           je 0x14063155c
00631550  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00631555  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063155A  EB 0E                           jmp 0x14063156a
0063155C  A8 04                           test al, 4
0063155E  74 0A                           je 0x14063156a
00631560  E8 A3 26 EA FF                  call 0x1404d3c08
00631565  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063156A  40 32 F6                        xor sil, sil
0063156D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00631572  40 38 35 3F 33 8D 00            cmp byte ptr [rip + 0x8d333f], sil
00631579  75 0C                           jne 0x140631587
0063157B  F7 05 FB 33 8D 00 00 08 00 00   test dword ptr [rip + 0x8d33fb], 0x800
00631585  74 13                           je 0x14063159a
00631587  48 8D 0D F2 28 8D 00            lea rcx, [rip + 0x8d28f2]
0063158E  E8 8D 50 BE FF                  call 0x140216620
00631593  40 8A F0                        mov sil, al
00631596  84 C0                           test al, al
00631598  74 39                           je 0x1406315d3
0063159A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0063159E  49 8B 1E                        mov rbx, qword ptr [r14]
006315A1  EB 1A                           jmp 0x1406315bd
006315A3  48 8D 43 F0                     lea rax, [rbx - 0x10]
006315A7  48 85 C0                        test rax, rax
006315AA  74 0E                           je 0x1406315ba
006315AC  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006315B0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006315B5  E8 16 95 08 00                  call 0x1406baad0
006315BA  48 8B 1B                        mov rbx, qword ptr [rbx]
006315BD  49 3B DE                        cmp rbx, r14
006315C0  75 E1                           jne 0x1406315a3
006315C2  40 84 F6                        test sil, sil
006315C5  74 0C                           je 0x1406315d3
006315C7  48 8D 0D B2 28 8D 00            lea rcx, [rip + 0x8d28b2]
006315CE  E8 AD 88 D1 FF                  call 0x140349e80
006315D3  48 8B CD                        mov rcx, rbp
006315D6  E8 D5 5B BE FF                  call 0x1402171b0
006315DB  48 85 FF                        test rdi, rdi
006315DE  74 64                           je 0x140631644
006315E0  40 32 F6                        xor sil, sil
006315E3  40 38 35 CE 32 8D 00            cmp byte ptr [rip + 0x8d32ce], sil
006315EA  75 0C                           jne 0x1406315f8
006315EC  F7 05 8A 33 8D 00 00 08 00 00   test dword ptr [rip + 0x8d338a], 0x800
006315F6  74 13                           je 0x14063160b
006315F8  48 8D 0D 81 28 8D 00            lea rcx, [rip + 0x8d2881]
006315FF  E8 1C 50 BE FF                  call 0x140216620
00631604  40 8A F0                        mov sil, al
00631607  84 C0                           test al, al
00631609  74 39                           je 0x140631644
0063160B  48 83 C7 30                     add rdi, 0x30
0063160F  48 8B 1F                        mov rbx, qword ptr [rdi]
00631612  EB 1A                           jmp 0x14063162e
00631614  48 8D 43 F0                     lea rax, [rbx - 0x10]
00631618  48 85 C0                        test rax, rax
0063161B  74 0E                           je 0x14063162b
0063161D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00631621  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00631626  E8 A5 94 08 00                  call 0x1406baad0
0063162B  48 8B 1B                        mov rbx, qword ptr [rbx]
0063162E  48 3B DF                        cmp rbx, rdi
00631631  75 E1                           jne 0x140631614
00631633  40 84 F6                        test sil, sil
00631636  74 0C                           je 0x140631644
00631638  48 8D 0D 41 28 8D 00            lea rcx, [rip + 0x8d2841]
0063163F  E8 3C 88 D1 FF                  call 0x140349e80
00631644  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00631649  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0063164E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00631653  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00631658  48 83 C4 30                     add rsp, 0x30
0063165C  41 5E                           pop r14
0063165E  C3                              ret
0063165F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeReleaseInStackQueuedSpinLockFromDpcLevelWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(262, a2, a3, a4);
    if (result == 0) goto loc_006315D3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063155C;
    v_stack_m18 = v_stack_p0;
    goto loc_0063156A;
loc_0063155C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9253695)) != 0) goto loc_00631587;
    if (((*(unsigned int *)(v_rip + 9253883)) & (0x800ULL)) == 0) goto loc_0063159A;
loc_00631587:
    result = ExAcquireRundownProtection(v_rip + 9251058, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006315D3;
loc_0063159A:
    goto loc_006315BD;
loc_006315A3:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006315BD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006315A3;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9250994;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, a2, a3, a4);
    if (result == 0) goto loc_00631644;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9253582)) != 0) goto loc_006315F8;
    if (((*(unsigned int *)(v_rip + 9253770)) & (0x800ULL)) == 0) goto loc_0063160B;
loc_006315F8:
    result = ExAcquireRundownProtection(v_rip + 9250945, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00631644;
loc_0063160B:
    v_rdi = (result) + (48);
    goto loc_0063162E;
loc_00631614:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063162E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_00631614;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9250881;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeReleaseInStackQueuedSpinLockFromDpcLevelWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(262, a2, a3, a4);
    if (result == 0) goto loc_006315D3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063155C;
    v_stack_m18 = v_stack_p0;
    goto loc_0063156A;
loc_0063155C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D333F)) != 0) goto loc_00631587;
    if (((*(uint32_t *)(v_rip + 0x8D33FB)) & (0x800ULL)) == 0) goto loc_0063159A;
loc_00631587:
    result = ExAcquireRundownProtection(v_rip + 9251058, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006315D3;
loc_0063159A:
    goto loc_006315BD;
loc_006315A3:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006315BD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006315A3;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9250994;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, a2, a3, a4);
    if (result == 0) goto loc_00631644;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D32CE)) != 0) goto loc_006315F8;
    if (((*(uint32_t *)(v_rip + 0x8D338A)) & (0x800ULL)) == 0) goto loc_0063160B;
loc_006315F8:
    result = ExAcquireRundownProtection(v_rip + 9250945, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00631644;
loc_0063160B:
    local_rdi = (result) + (48);
    goto loc_0063162E;
loc_00631614:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063162E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_00631614;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9250881;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00631510&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00631510[BB_00631510]
  bb_00631549[BB_00631549]
  bb_00631550[BB_00631550]
  bb_0063155C[BB_0063155C]
  bb_00631560[BB_00631560]
  bb_0063156A[BB_0063156A]
  bb_0063157B[BB_0063157B]
  bb_00631587[BB_00631587]
  bb_0063159A[BB_0063159A]
  bb_006315A3[BB_006315A3]
  bb_006315AC[BB_006315AC]
  bb_006315BA[BB_006315BA]
  bb_006315BD[BB_006315BD]
  bb_006315C2[BB_006315C2]
  bb_006315C7[BB_006315C7]
  bb_006315D3[BB_006315D3]
  bb_006315E0[BB_006315E0]
  bb_006315EC[BB_006315EC]
  bb_006315F8[BB_006315F8]
  bb_0063160B[BB_0063160B]
  bb_00631614[BB_00631614]
  bb_0063161D[BB_0063161D]
  bb_0063162B[BB_0063162B]
  bb_0063162E[BB_0063162E]
  bb_00631633[BB_00631633]
  bb_00631638[BB_00631638]
  bb_00631644[BB_00631644]
  bb_0063165F[BB_0063165F]
  bb_00631510 -->|branch| bb_006315D3
  bb_00631510 -->|fallthrough| bb_00631549
  bb_00631549 -->|branch| bb_0063155C
  bb_00631549 -->|fallthrough| bb_00631550
  bb_00631550 -->|branch| bb_0063156A
  bb_0063155C -->|branch| bb_0063156A
  bb_0063155C -->|fallthrough| bb_00631560
  bb_00631560 -->|flow| bb_0063156A
  bb_0063156A -->|branch| bb_00631587
  bb_0063156A -->|fallthrough| bb_0063157B
  bb_0063157B -->|branch| bb_0063159A
  bb_0063157B -->|fallthrough| bb_00631587
  bb_00631587 -->|branch| bb_006315D3
  bb_00631587 -->|fallthrough| bb_0063159A
  bb_0063159A -->|branch| bb_006315BD
  bb_006315A3 -->|branch| bb_006315BA
  bb_006315A3 -->|fallthrough| bb_006315AC
  bb_006315AC -->|flow| bb_006315BA
  bb_006315BA -->|flow| bb_006315BD
  bb_006315BD -->|branch| bb_006315A3
  bb_006315BD -->|fallthrough| bb_006315C2
  bb_006315C2 -->|branch| bb_006315D3
  bb_006315C2 -->|fallthrough| bb_006315C7
  bb_006315C7 -->|flow| bb_006315D3
  bb_006315D3 -->|branch| bb_00631644
  bb_006315D3 -->|fallthrough| bb_006315E0
  bb_006315E0 -->|branch| bb_006315F8
  bb_006315E0 -->|fallthrough| bb_006315EC
  bb_006315EC -->|branch| bb_0063160B
  bb_006315EC -->|fallthrough| bb_006315F8
  bb_006315F8 -->|branch| bb_00631644
  bb_006315F8 -->|fallthrough| bb_0063160B
  bb_0063160B -->|branch| bb_0063162E
  bb_00631614 -->|branch| bb_0063162B
  bb_00631614 -->|fallthrough| bb_0063161D
  bb_0063161D -->|flow| bb_0063162B
  bb_0063162B -->|flow| bb_0063162E
  bb_0063162E -->|branch| bb_00631614
  bb_0063162E -->|fallthrough| bb_00631633
  bb_00631633 -->|branch| bb_00631644
  bb_00631633 -->|fallthrough| bb_00631638
  bb_00631638 -->|flow| bb_00631644
```
