# HalpTscTraceProcessorSynchronization

- RVA: `0x0054B268`–`0x0054B35F` (길이 `247` bytes)
- VA: `0x000000014054B268`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6C08`
- 디코드: `57`개 명령, `247/247` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0054B2AE` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0054B344` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x0054B350` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HalpTscAdvSynchToLeader](../49/HalpTscAdvSynchToLeader_function_00494494.md) at `0x004946BD`
- [HalpTscAdvSynchToTarget](HalpTscAdvSynchToTarget_function_0054A978.md) at `0x0054AAB9`

### Static image references
- `0x0054B285` → RVA `0x00E0A740` (`.data`; read)
- `0x0054B293` → RVA `0x00FC22C0` (`.data`; read)
- `0x0054B2A0` → RVA `0x00FC22B8` (`.data`; read)
- `0x0054B2A7` → RVA `0x00022670` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054B268  48 8B C4                        mov rax, rsp
0054B26B  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
0054B26F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0054B273  89 50 10                        mov dword ptr [rax + 0x10], edx
0054B276  89 48 08                        mov dword ptr [rax + 8], ecx
0054B279  55                              push rbp
0054B27A  48 8D 68 A9                     lea rbp, [rax - 0x57]
0054B27E  48 81 EC A0 00 00 00            sub rsp, 0xa0
0054B285  48 8B 05 B4 F4 8B 00            mov rax, qword ptr [rip + 0x8bf4b4]
0054B28C  48 33 C4                        xor rax, rsp
0054B28F  48 89 45 3F                     mov qword ptr [rbp + 0x3f], rax
0054B293  80 3D 26 70 A7 00 00            cmp byte ptr [rip + 0xa77026], 0
0054B29A  0F 84 A9 00 00 00               je 0x14054b349
0054B2A0  48 8B 0D 11 70 A7 00            mov rcx, qword ptr [rip + 0xa77011]
0054B2A7  48 8D 15 C2 73 AD FF            lea rdx, [rip - 0x528c3e]
0054B2AE  E8 9D 71 E4 FF                  call 0x140392450
0054B2B3  84 C0                           test al, al
0054B2B5  0F 84 8E 00 00 00               je 0x14054b349
0054B2BB  83 65 FB 00                     and dword ptr [rbp - 5], 0
0054B2BF  48 8D 45 5F                     lea rax, [rbp + 0x5f]
0054B2C3  83 65 0B 00                     and dword ptr [rbp + 0xb], 0
0054B2C7  48 8D 15 A2 73 AD FF            lea rdx, [rip - 0x528c5e]
0054B2CE  83 65 1B 00                     and dword ptr [rbp + 0x1b], 0
0054B2D2  41 B8 04 00 00 00               mov r8d, 4
0054B2D8  83 65 2B 00                     and dword ptr [rbp + 0x2b], 0
0054B2DC  45 33 C9                        xor r9d, r9d
0054B2DF  83 65 3B 00                     and dword ptr [rbp + 0x3b], 0
0054B2E3  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
0054B2E7  48 8D 45 67                     lea rax, [rbp + 0x67]
0054B2EB  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0054B2EF  41 8D 48 04                     lea ecx, [r8 + 4]
0054B2F3  48 8D 45 6F                     lea rax, [rbp + 0x6f]
0054B2F7  44 89 45 F7                     mov dword ptr [rbp - 9], r8d
0054B2FB  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
0054B2FF  48 8D 45 77                     lea rax, [rbp + 0x77]
0054B303  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
0054B307  48 8D 45 7F                     lea rax, [rbp + 0x7f]
0054B30B  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
0054B30F  48 8D 45 EF                     lea rax, [rbp - 0x11]
0054B313  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0054B318  C7 44 24 30 05 00 00 00         mov dword ptr [rsp + 0x30], 5
0054B320  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0054B326  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0054B32C  44 89 45 07                     mov dword ptr [rbp + 7], r8d
0054B330  89 4D 17                        mov dword ptr [rbp + 0x17], ecx
0054B333  89 4D 27                        mov dword ptr [rbp + 0x27], ecx
0054B336  48 8B 0D 7B 6F A7 00            mov rcx, qword ptr [rip + 0xa76f7b]
0054B33D  44 89 45 37                     mov dword ptr [rbp + 0x37], r8d
0054B341  45 33 C0                        xor r8d, r8d
0054B344  E8 87 3D D1 FF                  call 0x14025f0d0
0054B349  48 8B 4D 3F                     mov rcx, qword ptr [rbp + 0x3f]
0054B34D  48 33 CC                        xor rcx, rsp
0054B350  E8 EB 12 16 00                  call 0x1406ac640
0054B355  48 81 C4 A0 00 00 00            add rsp, 0xa0
0054B35C  5D                              pop rbp
0054B35D  C3                              ret
0054B35E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTscTraceProcessorSynchronization(int a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 9172148)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 87 + 63) = result;
    if ((*(unsigned __int8 *)(v_rip + 10973222)) == 0) goto loc_0054B349;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10973201), v_rip - 5409854, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 87 + 95;
        a2 = v_rip - 5409886;
        a3 = 4;
        a4 = 0;
        *(unsigned __int64 *)(v_rsp - 87 - 17) = result;
        result = v_rsp - 87 + 103;
        *(unsigned __int64 *)(v_rsp - 87 - 1) = result;
        a1 = a3 + 4;
        result = v_rsp - 87 + 111;
        *(unsigned int *)(v_rsp - 87 - 9) = (unsigned int)(a3);
        *(unsigned __int64 *)(v_rsp - 87 + 15) = result;
        result = v_rsp - 87 + 119;
        *(unsigned __int64 *)(v_rsp - 87 + 31) = result;
        result = v_rsp - 87 + 127;
        *(unsigned __int64 *)(v_rsp - 87 + 47) = result;
        result = v_rsp - 87 - 17;
        v_stack_m70 = result;
        v_stack_m78 = 5;
        *(unsigned int *)(v_rsp - 87 + 7) = (unsigned int)(a3);
        *(unsigned int *)(v_rsp - 87 + 23) = a1;
        *(unsigned int *)(v_rsp - 87 + 39) = a1;
        a1 = *(unsigned __int64 *)(v_rip + 10973051);
        *(unsigned int *)(v_rsp - 87 + 55) = (unsigned int)(a3);
        a3 = 0;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 87 + 63)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpTscTraceProcessorSynchronization(int32_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x8BF4B4)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x57 + 0x3F) = result;
    if ((*(uint8_t *)(v_rip + 0xA77026)) == 0) goto loc_0054B349;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA77011), v_rip - 5409854, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 87 + 95;
        Arg2 = v_rip - 5409886;
        Arg3 = 4;
        Arg4 = 0;
        *(uint64_t *)(local_rsp - 0x57 - 0x11) = result;
        result = local_rsp - 87 + 103;
        *(uint64_t *)(local_rsp - 0x57 - 0x1) = result;
        Arg1 = Arg3 + 4;
        result = local_rsp - 87 + 111;
        *(uint32_t *)(local_rsp - 0x57 - 0x9) = (uint32_t)(Arg3);
        *(uint64_t *)(local_rsp - 0x57 + 0xF) = result;
        result = local_rsp - 87 + 119;
        *(uint64_t *)(local_rsp - 0x57 + 0x1F) = result;
        result = local_rsp - 87 + 127;
        *(uint64_t *)(local_rsp - 0x57 + 0x2F) = result;
        result = local_rsp - 87 - 17;
        v_stack_m70 = result;
        v_stack_m78 = 5;
        *(uint32_t *)(local_rsp - 0x57 + 0x7) = (uint32_t)(Arg3);
        *(uint32_t *)(local_rsp - 0x57 + 0x17) = Arg1;
        *(uint32_t *)(local_rsp - 0x57 + 0x27) = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0xA76F7B);
        *(uint32_t *)(local_rsp - 0x57 + 0x37) = (uint32_t)(Arg3);
        Arg3 = 0;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x57 + 0x3F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054B268&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054B268[BB_0054B268]
  bb_0054B2A0[BB_0054B2A0]
  bb_0054B2BB[BB_0054B2BB]
  bb_0054B349[BB_0054B349]
  bb_0054B35E[BB_0054B35E]
  bb_0054B268 -->|branch| bb_0054B349
  bb_0054B268 -->|fallthrough| bb_0054B2A0
  bb_0054B2A0 -->|branch| bb_0054B349
  bb_0054B2A0 -->|fallthrough| bb_0054B2BB
  bb_0054B2BB -->|flow| bb_0054B349
```
