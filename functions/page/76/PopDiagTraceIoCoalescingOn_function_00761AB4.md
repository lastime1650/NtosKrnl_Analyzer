# PopDiagTraceIoCoalescingOn

- RVA: `0x00761AB4`–`0x00761BAB` (길이 `247` bytes)
- VA: `0x0000000140761AB4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EA9C`
- 디코드: `56`개 명령, `247/247` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00761B0B` → [PopPrintEx](../../text/48/PopPrintEx_function_0048EF24.md) (function, `0x0048EF24`)
- `0x00761B27` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00761B90` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00761B9C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopCoalescingSetActiveState](../../text/4B/PopCoalescingSetActiveState_function_004B7E18.md) at `0x004B7E9D`

### Static image references
- `0x00761AC2` → RVA `0x00E0A740` (`.data`; read)
- `0x00761AD0` → RVA `0x00E0B548` (`.data`; read)
- `0x00761AD6` → RVA `0x00B022B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00761ADD` → RVA `0x00FC6CCC` (`ALMOSTRO`; read)
- `0x00761AF0` → RVA `0x00E0B544` (`.data`; read)
- `0x00761B10` → RVA `0x00E67858` (`.data`; read)
- `0x00761B19` → RVA `0x00F0B408` (`.data`; read)
- `0x00761B20` → RVA `0x00021040` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00761B0B` → [PopPrintEx](../../text/48/PopPrintEx_function_0048EF24.md) (`PAGE` → `.text`)
  - `0x00761B27` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00761B90` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00761B9C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00761AB4  40 55                           push rbp
00761AB6  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00761ABB  48 81 EC A0 00 00 00            sub rsp, 0xa0
00761AC2  48 8B 05 77 8C 6A 00            mov rax, qword ptr [rip + 0x6a8c77]
00761AC9  48 33 C4                        xor rax, rsp
00761ACC  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00761AD0  8B 05 72 9A 6A 00               mov eax, dword ptr [rip + 0x6a9a72]
00761AD6  48 8D 15 D3 07 3A 00            lea rdx, [rip + 0x3a07d3]
00761ADD  44 8B 05 E8 51 86 00            mov r8d, dword ptr [rip + 0x8651e8]
00761AE4  45 8B D1                        mov r10d, r9d
00761AE7  44 89 4D FF                     mov dword ptr [rbp - 1], r9d
00761AEB  B9 03 00 00 00                  mov ecx, 3
00761AF0  44 8B 0D 4D 9A 6A 00            mov r9d, dword ptr [rip + 0x6a9a4d]
00761AF7  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
00761AFC  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00761B00  89 45 F7                        mov dword ptr [rbp - 9], eax
00761B03  44 89 4D EF                     mov dword ptr [rbp - 0x11], r9d
00761B07  44 89 45 E7                     mov dword ptr [rbp - 0x19], r8d
00761B0B  E8 14 D4 D2 FF                  call 0x14048ef24
00761B10  80 3D 41 5D 70 00 00            cmp byte ptr [rip + 0x705d41], 0
00761B17  74 7C                           je 0x140761b95
00761B19  48 8B 0D E8 98 7A 00            mov rcx, qword ptr [rip + 0x7a98e8]
00761B20  48 8D 15 19 F5 8B FF            lea rdx, [rip - 0x740ae7]
00761B27  E8 24 09 C3 FF                  call 0x140392450
00761B2C  84 C0                           test al, al
00761B2E  74 65                           je 0x140761b95
00761B30  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00761B34  48 8D 45 E7                     lea rax, [rbp - 0x19]
00761B38  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00761B3C  48 8D 15 FD F4 8B FF            lea rdx, [rip - 0x740b03]
00761B43  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00761B47  41 B9 04 00 00 00               mov r9d, 4
00761B4D  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00761B51  45 33 C0                        xor r8d, r8d
00761B54  48 8B 0D AD 98 7A 00            mov rcx, qword ptr [rip + 0x7a98ad]
00761B5B  48 89 45 07                     mov qword ptr [rbp + 7], rax
00761B5F  48 8D 45 EF                     lea rax, [rbp - 0x11]
00761B63  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00761B67  48 8D 45 F7                     lea rax, [rbp - 9]
00761B6B  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00761B6F  48 8D 45 FF                     lea rax, [rbp - 1]
00761B73  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00761B77  48 8D 45 07                     lea rax, [rbp + 7]
00761B7B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00761B80  44 89 4D 0F                     mov dword ptr [rbp + 0xf], r9d
00761B84  44 89 4D 1F                     mov dword ptr [rbp + 0x1f], r9d
00761B88  44 89 4D 2F                     mov dword ptr [rbp + 0x2f], r9d
00761B8C  44 89 4D 3F                     mov dword ptr [rbp + 0x3f], r9d
00761B90  E8 8B AB CB FF                  call 0x14041c720
00761B95  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00761B99  48 33 CC                        xor rcx, rsp
00761B9C  E8 9F AA F4 FF                  call 0x1406ac640
00761BA1  48 81 C4 A0 00 00 00            add rsp, 0xa0
00761BA8  5D                              pop rbp
00761BA9  C3                              ret
00761BAA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceIoCoalescingOn(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6982775)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m60 = a4;
    v_stack_m80 = (unsigned int)((unsigned int)(a4));
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6986354)));
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6986354)));
    v_stack_m70 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6986317)));
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8802792)));
    result = PopPrintEx(3, v_rip + 3803091, (unsigned int)(*(unsigned int *)(v_rip + 8802792)), (unsigned int)(*(unsigned int *)(v_rip + 6986317)));
    if ((*(unsigned __int8 *)(v_rip + 7363905)) == 0) goto loc_00761B95;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8034536), v_rip - 7604967, (unsigned int)(*(unsigned int *)(v_rip + 8802792)), (unsigned int)(*(unsigned int *)(v_rip + 6986317)));
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m78;
        a2 = v_rip - 7604995;
        a4 = 4;
        a3 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 8034477);
        v_stack_m58 = result;
        result = v_stack_m70;
        v_stack_m48 = result;
        result = v_stack_m68;
        v_stack_m38 = result;
        result = v_stack_m60;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m88 = result;
        v_stack_m50 = a4;
        v_stack_m40 = a4;
        v_stack_m30 = a4;
        v_stack_m20 = a4;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceIoCoalescingOn(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x6A8C77)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m60 = Arg4;
    v_stack_m80 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6A9A72)));
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6A9A72)));
    v_stack_m70 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6A9A4D)));
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8651E8)));
    result = PopPrintEx(3, v_rip + 3803091, (uint32_t)(*(uint32_t *)(v_rip + 0x8651E8)), (uint32_t)(*(uint32_t *)(v_rip + 0x6A9A4D)));
    if ((*(uint8_t *)(v_rip + 0x705D41)) == 0) goto loc_00761B95;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7A98E8), v_rip - 7604967, (uint32_t)(*(uint32_t *)(v_rip + 0x8651E8)), (uint32_t)(*(uint32_t *)(v_rip + 0x6A9A4D)));
    if ((uint8_t)(result) != 0) {
        result = v_stack_m78;
        Arg2 = v_rip - 7604995;
        Arg4 = 4;
        Arg3 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0x7A98AD);
        v_stack_m58 = result;
        result = v_stack_m70;
        v_stack_m48 = result;
        result = v_stack_m68;
        v_stack_m38 = result;
        result = v_stack_m60;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m88 = result;
        v_stack_m50 = Arg4;
        v_stack_m40 = Arg4;
        v_stack_m30 = Arg4;
        v_stack_m20 = Arg4;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00761AB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00761AB4[BB_00761AB4]
  bb_00761B19[BB_00761B19]
  bb_00761B30[BB_00761B30]
  bb_00761B95[BB_00761B95]
  bb_00761BAA[BB_00761BAA]
  bb_00761AB4 -->|branch| bb_00761B95
  bb_00761AB4 -->|fallthrough| bb_00761B19
  bb_00761B19 -->|branch| bb_00761B95
  bb_00761B19 -->|fallthrough| bb_00761B30
  bb_00761B30 -->|flow| bb_00761B95
```
