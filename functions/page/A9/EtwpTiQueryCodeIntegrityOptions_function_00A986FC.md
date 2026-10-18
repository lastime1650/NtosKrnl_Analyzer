# EtwpTiQueryCodeIntegrityOptions

- RVA: `0x00A986FC`–`0x00A98742` (길이 `70` bytes)
- VA: `0x0000000140A986FC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BA054`
- 디코드: `23`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A98726` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)

### Direct callers
- [EtwTiLogDriverObjectLoad](EtwTiLogDriverObjectLoad_function_00A985E0.md) at `0x00A9867F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A98726` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A986FC  48 8B C4                        mov rax, rsp
00A986FF  53                              push rbx
00A98700  48 83 EC 20                     sub rsp, 0x20
00A98704  48 83 60 18 00                  and qword ptr [rax + 0x18], 0
00A98709  4C 8D 48 10                     lea r9, [rax + 0x10]
00A9870D  83 60 10 00                     and dword ptr [rax + 0x10], 0
00A98711  48 8D 50 18                     lea rdx, [rax + 0x18]
00A98715  41 B8 08 00 00 00               mov r8d, 8
00A9871B  48 8B D9                        mov rbx, rcx
00A9871E  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00A98722  41 8D 48 5F                     lea ecx, [r8 + 0x5f]
00A98726  E8 65 50 C1 FF                  call 0x1406ad790
00A9872B  8B D0                           mov edx, eax
00A9872D  85 C0                           test eax, eax
00A9872F  79 07                           jns 0x140a98738
00A98731  48 83 C4 20                     add rsp, 0x20
00A98735  5B                              pop rbx
00A98736  C3                              ret
00A98737  CC                              int3
00A98738  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00A9873C  89 03                           mov dword ptr [rbx], eax
00A9873E  8B C2                           mov eax, edx
00A98740  EB EF                           jmp 0x140a98731
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpTiQueryCodeIntegrityOptions(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p44;

    v_rsp = (v_rsp) - (32);
    *(unsigned int *)(v_rsp + 24) = 8;
    result = ZwQuerySystemInformation(8 + 95, v_rsp + 24, 8, v_rsp + 16);
    if (!sign_flag) goto loc_00A98738;
loc_00A98731:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A98738:
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(v_stack_p44));
    goto loc_00A98731;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpTiQueryCodeIntegrityOptions(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p44;

    local_rsp = (local_rsp) - (32);
    *(uint32_t *)(local_rsp + 0x18) = 8;
    result = ZwQuerySystemInformation(8 + 95, local_rsp + 24, 8, local_rsp + 16);
    if (!sign_flag) goto loc_00A98738;
loc_00A98731:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A98738:
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(v_stack_p44));
    goto loc_00A98731;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A986FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A986FC[BB_00A986FC]
  bb_00A98731[BB_00A98731]
  bb_00A98737[BB_00A98737]
  bb_00A98738[BB_00A98738]
  bb_00A986FC -->|branch| bb_00A98738
  bb_00A986FC -->|fallthrough| bb_00A98731
  bb_00A98737 -->|flow| bb_00A98738
  bb_00A98738 -->|branch| bb_00A98731
```
