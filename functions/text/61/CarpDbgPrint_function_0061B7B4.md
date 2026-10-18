# CarpDbgPrint

- RVA: `0x0061B7B4`–`0x0061B7FC` (길이 `72` bytes)
- VA: `0x000000014061B7B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CF7BC`
- 디코드: `20`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0061B7F1` → [vDbgPrintExWithPrefixInternal](../35/vDbgPrintExWithPrefixInternal_function_00359314.md) (function, `0x00359314`)

### Direct callers
- [CarHandleEtwEvent](CarHandleEtwEvent_function_00617FBC.md) at `0x00618086`
- [CarInitLogging](CarInitLogging_function_006180B0.md) at `0x00618108`
- [DifRegisterPlugin](DifRegisterPlugin_function_0061ABE0.md) at `0x0061AC86`
- [DifRegisterPlugin](DifRegisterPlugin_function_0061ABE0.md) at `0x0061AED7`
- [DifRegisterPlugin](DifRegisterPlugin_function_0061ABE0.md) at `0x0061AF5C`
- [CarInitiateBugcheck](CarInitiateBugcheck_function_0061BAB0.md) at `0x0061BAD8`
- [CarLiveDump](CarLiveDump_function_0061BB30.md) at `0x0061BBC8`

### Static image references
- `0x0061B7E2` → RVA `0x006C7800` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061B7B4  4C 8B DC                        mov r11, rsp
0061B7B7  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
0061B7BB  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
0061B7BF  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
0061B7C3  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
0061B7C7  48 83 EC 48                     sub rsp, 0x48
0061B7CB  44 0F 20 C0                     mov rax, cr8
0061B7CF  84 C0                           test al, al
0061B7D1  75 23                           jne 0x14061b7f6
0061B7D3  45 33 C0                        xor r8d, r8d
0061B7D6  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0061B7DB  49 8D 43 10                     lea rax, [r11 + 0x10]
0061B7DF  4C 8B C9                        mov r9, rcx
0061B7E2  48 8D 0D 17 C0 0A 00            lea rcx, [rip + 0xac017]
0061B7E9  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0061B7ED  41 8D 50 65                     lea edx, [r8 + 0x65]
0061B7F1  E8 1E DB D3 FF                  call 0x140359314
0061B7F6  48 83 C4 48                     add rsp, 0x48
0061B7FA  C3                              ret
0061B7FB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CarpDbgPrint(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m20;

    *(unsigned __int64 *)(v_rsp + 8) = a1;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (72);
    result = v_cr8;
    if ((unsigned __int8)(v_cr8) == 0) {
        a3 = 0;
        v_stack_m20 = 1;
        result = v_rsp + 16;
        a4 = a1;
        a1 = v_rip + 704535;
        *(unsigned __int64 *)(v_rsp - 40) = result;
        a2 = a3 + 101;
        result = vDbgPrintExWithPrefixInternal(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CarpDbgPrint(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m20;

    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (72);
    result = v_cr8;
    if ((uint8_t)(v_cr8) == 0) {
        Arg3 = 0;
        v_stack_m20 = 1;
        result = local_rsp + 16;
        Arg4 = Arg1;
        Arg1 = v_rip + 704535;
        *(uint64_t *)(local_rsp - 0x28) = result;
        Arg2 = Arg3 + 101;
        result = vDbgPrintExWithPrefixInternal(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061B7B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061B7B4[BB_0061B7B4]
  bb_0061B7D3[BB_0061B7D3]
  bb_0061B7F6[BB_0061B7F6]
  bb_0061B7FB[BB_0061B7FB]
  bb_0061B7B4 -->|branch| bb_0061B7F6
  bb_0061B7B4 -->|fallthrough| bb_0061B7D3
  bb_0061B7D3 -->|flow| bb_0061B7F6
```
