# PopCheckTestsigningEnabled

- RVA: `0x00753FE0`–`0x0075401F` (길이 `63` bytes)
- VA: `0x0000000140753FE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF520`
- 디코드: `22`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00754004` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)

### Direct callers
- [PopDripsWatchdogTakeAction](../77/PopDripsWatchdogTakeAction_function_007732D0.md) at `0x00773566`
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8B8C9`
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8B92C`
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8B9A5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00754004` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00753FE0  48 8B C4                        mov rax, rsp
00753FE3  53                              push rbx
00753FE4  48 83 EC 20                     sub rsp, 0x20
00753FE8  33 DB                           xor ebx, ebx
00753FEA  4C 8D 48 08                     lea r9, [rax + 8]
00753FEE  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00753FF2  48 8D 50 10                     lea rdx, [rax + 0x10]
00753FF6  89 58 08                        mov dword ptr [rax + 8], ebx
00753FF9  44 8D 43 08                     lea r8d, [rbx + 8]
00753FFD  8D 4B 67                        lea ecx, [rbx + 0x67]
00754000  44 89 40 10                     mov dword ptr [rax + 0x10], r8d
00754004  E8 87 97 F5 FF                  call 0x1406ad790
00754009  85 C0                           test eax, eax
0075400B  78 09                           js 0x140754016
0075400D  F6 44 24 3C 02                  test byte ptr [rsp + 0x3c], 2
00754012  74 02                           je 0x140754016
00754014  B3 01                           mov bl, 1
00754016  8A C3                           mov al, bl
00754018  48 83 C4 20                     add rsp, 0x20
0075401C  5B                              pop rbx
0075401D  C3                              ret
0075401E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopCheckTestsigningEnabled(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int8 v_stack_p14;

    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp + 16) = 0;
    *(unsigned int *)(v_rsp + 8) = 0;
    *(unsigned int *)(v_rsp + 16) = (unsigned int)(v_rbx + 8);
    result = ZwQuerySystemInformation(v_rbx + 103, v_rsp + 16, v_rbx + 8, v_rsp + 8);
    if (sign_flag) goto loc_00754016;
    if (((v_stack_p14) & (2)) != 0) {
        v_rbx = 1;
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_rbx);
}
```

## 5. (Beta) C Style

```c
void PopCheckTestsigningEnabled(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint8_t v_stack_p14;

    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    *(uint64_t *)(local_rsp + 0x10) = 0;
    *(uint32_t *)(local_rsp + 0x8) = 0;
    *(uint32_t *)(local_rsp + 0x10) = (uint32_t)(local_rbx + 8);
    result = ZwQuerySystemInformation(local_rbx + 103, local_rsp + 16, local_rbx + 8, local_rsp + 8);
    if (sign_flag) goto loc_00754016;
    if (((v_stack_p14) & (2)) != 0) {
        local_rbx = 1;
    }
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(local_rbx);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00753FE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00753FE0[BB_00753FE0]
  bb_0075400D[BB_0075400D]
  bb_00754014[BB_00754014]
  bb_00754016[BB_00754016]
  bb_0075401E[BB_0075401E]
  bb_00753FE0 -->|branch| bb_00754016
  bb_00753FE0 -->|fallthrough| bb_0075400D
  bb_0075400D -->|branch| bb_00754016
  bb_0075400D -->|fallthrough| bb_00754014
  bb_00754014 -->|flow| bb_00754016
```
