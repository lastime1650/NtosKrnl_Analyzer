# DifPoFxCompleteIdleStateWrapper

- RVA: `0x00639260`–`0x006393BF` (길이 `351` bytes)
- VA: `0x0000000140639260`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `97`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00639291` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006392B9` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006392EC` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00639313` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063932C` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00639337` → [PoFxCompleteIdleState](../46/PoFxCompleteIdleState_function_004666C0.md) (function, `0x004666C0`)
- `0x00639360` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00639387` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006393A0` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006392CB` → RVA `0x00F048B8` (`.data`; read)
- `0x006392D9` → RVA `0x00F04980` (`.data`; read)
- `0x006392E5` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00639260  4C 8B DC                        mov r11, rsp
00639263  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00639267  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063926B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063926F  57                              push rdi
00639270  41 56                           push r14
00639272  41 57                           push r15
00639274  48 83 EC 40                     sub rsp, 0x40
00639278  33 C0                           xor eax, eax
0063927A  0F 57 C0                        xorps xmm0, xmm0
0063927D  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00639282  4C 8B F9                        mov r15, rcx
00639285  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00639289  B9 BE 00 00 00                  mov ecx, 0xbe
0063928E  44 8B F2                        mov r14d, edx
00639291  E8 9E C7 E5 FF                  call 0x140495a34
00639296  48 8B F0                        mov rsi, rax
00639299  48 85 C0                        test rax, rax
0063929C  0F 84 8F 00 00 00               je 0x140639331
006392A2  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006392A5  A8 18                           test al, 0x18
006392A7  74 0C                           je 0x1406392b5
006392A9  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006392AE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006392B3  EB 0E                           jmp 0x1406392c3
006392B5  A8 04                           test al, 4
006392B7  74 0A                           je 0x1406392c3
006392B9  E8 4A A9 E9 FF                  call 0x1404d3c08
006392BE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006392C3  40 32 ED                        xor bpl, bpl
006392C6  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
006392CB  40 38 2D E6 B5 8C 00            cmp byte ptr [rip + 0x8cb5e6], bpl
006392D2  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
006392D7  75 0C                           jne 0x1406392e5
006392D9  F7 05 9D B6 8C 00 00 08 00 00   test dword ptr [rip + 0x8cb69d], 0x800
006392E3  74 13                           je 0x1406392f8
006392E5  48 8D 0D 94 AB 8C 00            lea rcx, [rip + 0x8cab94]
006392EC  E8 2F D3 BD FF                  call 0x140216620
006392F1  40 8A E8                        mov bpl, al
006392F4  84 C0                           test al, al
006392F6  74 39                           je 0x140639331
006392F8  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006392FC  48 8B 1F                        mov rbx, qword ptr [rdi]
006392FF  EB 1A                           jmp 0x14063931b
00639301  48 8D 43 F0                     lea rax, [rbx - 0x10]
00639305  48 85 C0                        test rax, rax
00639308  74 0E                           je 0x140639318
0063930A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063930E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00639313  E8 B8 17 08 00                  call 0x1406baad0
00639318  48 8B 1B                        mov rbx, qword ptr [rbx]
0063931B  48 3B DF                        cmp rbx, rdi
0063931E  75 E1                           jne 0x140639301
00639320  40 84 ED                        test bpl, bpl
00639323  74 0C                           je 0x140639331
00639325  48 8D 0D 54 AB 8C 00            lea rcx, [rip + 0x8cab54]
0063932C  E8 4F 0B D1 FF                  call 0x140349e80
00639331  41 8B D6                        mov edx, r14d
00639334  49 8B CF                        mov rcx, r15
00639337  E8 84 D3 E2 FF                  call 0x1404666c0
0063933C  48 85 F6                        test rsi, rsi
0063933F  74 64                           je 0x1406393a5
00639341  40 32 FF                        xor dil, dil
00639344  40 38 3D 6D B5 8C 00            cmp byte ptr [rip + 0x8cb56d], dil
0063934B  75 0C                           jne 0x140639359
0063934D  F7 05 29 B6 8C 00 00 08 00 00   test dword ptr [rip + 0x8cb629], 0x800
00639357  74 13                           je 0x14063936c
00639359  48 8D 0D 20 AB 8C 00            lea rcx, [rip + 0x8cab20]
00639360  E8 BB D2 BD FF                  call 0x140216620
00639365  40 8A F8                        mov dil, al
00639368  84 C0                           test al, al
0063936A  74 39                           je 0x1406393a5
0063936C  48 83 C6 30                     add rsi, 0x30
00639370  48 8B 1E                        mov rbx, qword ptr [rsi]
00639373  EB 1A                           jmp 0x14063938f
00639375  48 8D 43 F0                     lea rax, [rbx - 0x10]
00639379  48 85 C0                        test rax, rax
0063937C  74 0E                           je 0x14063938c
0063937E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00639382  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00639387  E8 44 17 08 00                  call 0x1406baad0
0063938C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063938F  48 3B DE                        cmp rbx, rsi
00639392  75 E1                           jne 0x140639375
00639394  40 84 FF                        test dil, dil
00639397  74 0C                           je 0x1406393a5
00639399  48 8D 0D E0 AA 8C 00            lea rcx, [rip + 0x8caae0]
006393A0  E8 DB 0A D1 FF                  call 0x140349e80
006393A5  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006393AA  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
006393AF  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
006393B4  48 83 C4 40                     add rsp, 0x40
006393B8  41 5F                           pop r15
006393BA  41 5E                           pop r14
006393BC  5F                              pop rdi
006393BD  C3                              ret
006393BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifPoFxCompleteIdleStateWrapper(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = DifGetAPIThunkContextById(190, a2, a3, a4);
    if (result == 0) goto loc_00639331;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006392B5;
    v_stack_m38 = v_stack_p0;
    goto loc_006392C3;
loc_006392B5:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 9221606)) != 0) goto loc_006392E5;
    if (((*(unsigned int *)(v_rip + 9221789)) & (0x800ULL)) == 0) goto loc_006392F8;
loc_006392E5:
    result = ExAcquireRundownProtection(v_rip + 9218964, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00639331;
loc_006392F8:
    goto loc_0063931B;
loc_00639301:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063931B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00639301;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9218900;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = PoFxCompleteIdleState(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if (result == 0) goto loc_006393A5;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9221485)) != 0) goto loc_00639359;
    if (((*(unsigned int *)(v_rip + 9221673)) & (0x800ULL)) == 0) goto loc_0063936C;
loc_00639359:
    result = ExAcquireRundownProtection(v_rip + 9218848, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006393A5;
loc_0063936C:
    v_rsi = (result) + (48);
    goto loc_0063938F;
loc_00639375:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0063938F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00639375;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9218784;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifPoFxCompleteIdleStateWrapper(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = DifGetAPIThunkContextById(190, Arg2, a3, a4);
    if (result == 0) goto loc_00639331;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006392B5;
    v_stack_m38 = v_stack_p0;
    goto loc_006392C3;
loc_006392B5:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0x8CB5E6)) != 0) goto loc_006392E5;
    if (((*(uint32_t *)(v_rip + 0x8CB69D)) & (0x800ULL)) == 0) goto loc_006392F8;
loc_006392E5:
    result = ExAcquireRundownProtection(v_rip + 9218964, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00639331;
loc_006392F8:
    goto loc_0063931B;
loc_00639301:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0063931B:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00639301;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9218900;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = PoFxCompleteIdleState(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    if (result == 0) goto loc_006393A5;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CB56D)) != 0) goto loc_00639359;
    if (((*(uint32_t *)(v_rip + 0x8CB629)) & (0x800ULL)) == 0) goto loc_0063936C;
loc_00639359:
    result = ExAcquireRundownProtection(v_rip + 9218848, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006393A5;
loc_0063936C:
    local_rsi = (result) + (48);
    goto loc_0063938F;
loc_00639375:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
loc_0063938F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00639375;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9218784;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00639260&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00639260[BB_00639260]
  bb_006392A2[BB_006392A2]
  bb_006392A9[BB_006392A9]
  bb_006392B5[BB_006392B5]
  bb_006392B9[BB_006392B9]
  bb_006392C3[BB_006392C3]
  bb_006392D9[BB_006392D9]
  bb_006392E5[BB_006392E5]
  bb_006392F8[BB_006392F8]
  bb_00639301[BB_00639301]
  bb_0063930A[BB_0063930A]
  bb_00639318[BB_00639318]
  bb_0063931B[BB_0063931B]
  bb_00639320[BB_00639320]
  bb_00639325[BB_00639325]
  bb_00639331[BB_00639331]
  bb_00639341[BB_00639341]
  bb_0063934D[BB_0063934D]
  bb_00639359[BB_00639359]
  bb_0063936C[BB_0063936C]
  bb_00639375[BB_00639375]
  bb_0063937E[BB_0063937E]
  bb_0063938C[BB_0063938C]
  bb_0063938F[BB_0063938F]
  bb_00639394[BB_00639394]
  bb_00639399[BB_00639399]
  bb_006393A5[BB_006393A5]
  bb_006393BE[BB_006393BE]
  bb_00639260 -->|branch| bb_00639331
  bb_00639260 -->|fallthrough| bb_006392A2
  bb_006392A2 -->|branch| bb_006392B5
  bb_006392A2 -->|fallthrough| bb_006392A9
  bb_006392A9 -->|branch| bb_006392C3
  bb_006392B5 -->|branch| bb_006392C3
  bb_006392B5 -->|fallthrough| bb_006392B9
  bb_006392B9 -->|flow| bb_006392C3
  bb_006392C3 -->|branch| bb_006392E5
  bb_006392C3 -->|fallthrough| bb_006392D9
  bb_006392D9 -->|branch| bb_006392F8
  bb_006392D9 -->|fallthrough| bb_006392E5
  bb_006392E5 -->|branch| bb_00639331
  bb_006392E5 -->|fallthrough| bb_006392F8
  bb_006392F8 -->|branch| bb_0063931B
  bb_00639301 -->|branch| bb_00639318
  bb_00639301 -->|fallthrough| bb_0063930A
  bb_0063930A -->|flow| bb_00639318
  bb_00639318 -->|flow| bb_0063931B
  bb_0063931B -->|branch| bb_00639301
  bb_0063931B -->|fallthrough| bb_00639320
  bb_00639320 -->|branch| bb_00639331
  bb_00639320 -->|fallthrough| bb_00639325
  bb_00639325 -->|flow| bb_00639331
  bb_00639331 -->|branch| bb_006393A5
  bb_00639331 -->|fallthrough| bb_00639341
  bb_00639341 -->|branch| bb_00639359
  bb_00639341 -->|fallthrough| bb_0063934D
  bb_0063934D -->|branch| bb_0063936C
  bb_0063934D -->|fallthrough| bb_00639359
  bb_00639359 -->|branch| bb_006393A5
  bb_00639359 -->|fallthrough| bb_0063936C
  bb_0063936C -->|branch| bb_0063938F
  bb_00639375 -->|branch| bb_0063938C
  bb_00639375 -->|fallthrough| bb_0063937E
  bb_0063937E -->|flow| bb_0063938C
  bb_0063938C -->|flow| bb_0063938F
  bb_0063938F -->|branch| bb_00639375
  bb_0063938F -->|fallthrough| bb_00639394
  bb_00639394 -->|branch| bb_006393A5
  bb_00639394 -->|fallthrough| bb_00639399
  bb_00639399 -->|flow| bb_006393A5
```
